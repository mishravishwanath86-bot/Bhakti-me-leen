import sqlite3, sys, json, os, re, time
from pathlib import Path
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

import yt_dlp

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
sys.path.insert(0, str(BASE_DIR))
from core.normalizer import normalize_devanagari

DB_PATH = BASE_DIR / "db" / "bhakti.db"
FIRST_100_JSON = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_001_100.json"
REPORT_PATH = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_101_200.json"

SEP = "=" * 80
SEP2 = "-" * 80

print(SEP)
print("AUTOMATIC AUDIO SOURCE MAPPING SYSTEM — RECORDS 101–200 (READ-ONLY AUDIT)")
print(SEP)
print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")

# 1. Load First 100 Audited IDs
with open(FIRST_100_JSON, 'r', encoding='utf-8') as f:
    first_100_data = json.load(f)
first_100_ids = [item['record_id'] for item in first_100_data['candidates']]
print(f"Loaded {len(first_100_ids)} previously audited record IDs from Batch 001–100.")

# 2. Fetch Next 100 Records
conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Verify working audio count before
cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'assets/audio/%'")
working_local_audio = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'https://www.youtube.com/%'")
working_youtube_audio = cur.fetchone()[0]
total_working_audio = working_local_audio + working_youtube_audio

placeholders = ','.join(['?'] * len(first_100_ids))
sql = f"""
    SELECT id, title, title_en, deity_id, category_id, content_type, audio_url, short_description, tags
    FROM content_items
    WHERE (audio_url IS NULL OR audio_url = '' OR audio_url NOT LIKE 'assets/audio/%')
      AND id NOT IN ({placeholders})
    ORDER BY rowid
    LIMIT 100
"""
cur.execute(sql, first_100_ids)
records_to_process = [dict(r) for r in cur.fetchall()]
conn.close()

print(f"Fetched next 100 records for candidate mapping (Total: {len(records_to_process)})")
print(f"Existing working audio preserved: {total_working_audio} (Local MP3: {working_local_audio}, YouTube: {working_youtube_audio})")
print()

TRUSTED_CHANNELS = [
    't-series bhakti sagar', 'rajshri soul', 'sanskar tv', 'shemaroo bhakti',
    'bhakti', 'spiritual mantra', 'yuki music', 'tips devotional',
    'super digital bhakti', 'geetanjali devotional', 'times music spiritual',
    'sur mandir', 'satsang tv', 'subh tv', 'vedic mantras', 'stotra nidhi',
    'suresh wadkar', 'anuradha paudwal', 'gulshan kumar', 'bhajan india',
    'bhakti sangeet', 'anup jalota', 'hariharan', 'jagjit singh',
    'devotional', 'bhakti geet', 'katha sagar'
]

def build_search_query(rec: dict) -> str:
    title = rec['title']
    ctype = rec.get('content_type') or ''
    deity = rec.get('deity_id') or ''
    
    # Clean noise
    t_clean = re.sub(r'[\(\)\[\]]', ' ', title).strip()
    t_clean = re.sub(r'\s+', ' ', t_clean)
    
    q = t_clean
    if ctype and ctype not in ['dharmik_gyan', 'festival_special'] and ctype.lower() not in t_clean.lower():
        q += f" {ctype}"
        
    return q.strip()

def score_candidate(rec: dict, yt_entry: dict) -> tuple[float, str, str]:
    if not yt_entry:
        return 0.0, "NO_MATCH", "No candidate video found from search"
    
    yt_title = yt_entry.get('title') or ''
    yt_channel = (yt_entry.get('uploader') or yt_entry.get('channel') or '').lower()
    yt_duration = yt_entry.get('duration') or 0
    
    db_title = rec['title']
    db_title_en = rec.get('title_en') or ''
    content_type = rec.get('content_type') or ''
    deity_id = rec.get('deity_id') or ''
    
    score = 0.0
    reasons = []
    
    # 1. Title Token Overlap (Devanagari)
    norm_db = normalize_devanagari(db_title).lower()
    norm_yt = normalize_devanagari(yt_title).lower()
    
    tokens_db = set(re.findall(r'[a-zA-Z0-9\u0900-\u097F]+', norm_db))
    tokens_yt = set(re.findall(r'[a-zA-Z0-9\u0900-\u097F]+', norm_yt))
    
    stopwords = {'श्री', 'की', 'का', 'के', 'में', 'से', 'पर', 'और', 'एवं', 'द्वारा', 'पावन', 'दिव्य', 'सम्पूर्ण', 'पूर्ण', '108'}
    sig_db = {t for t in tokens_db if len(t) > 1 and t not in stopwords}
    
    if sig_db:
        overlap = sig_db.intersection(tokens_yt)
        overlap_ratio = len(overlap) / len(sig_db)
        score += overlap_ratio * 55.0
        reasons.append(f"Title token overlap: {len(overlap)}/{len(sig_db)} ({int(overlap_ratio*100)}%)")
    else:
        overlap_ratio = 0.0
        
    # 2. English title overlap
    if db_title_en:
        sig_en = {t.lower() for t in re.findall(r'[a-zA-Z0-9]+', db_title_en) if len(t) > 2 and t.lower() not in {'shri', 'the', 'and', 'with'}}
        sig_yt_en = {t.lower() for t in re.findall(r'[a-zA-Z0-9]+', yt_title) if len(t) > 2}
        if sig_en:
            en_overlap = sig_en.intersection(sig_yt_en)
            if en_overlap:
                en_ratio = len(en_overlap) / len(sig_en)
                score += min(15.0, en_ratio * 15.0)
                reasons.append(f"English token match: {', '.join(list(en_overlap)[:3])}")
                
    # 3. Content Type Match
    TYPE_SYNONYMS = {
        'aarti': ['aarti', 'आरती', 'arti'],
        'chalisa': ['chalisa', 'चालीसा'],
        'stotram': ['stotram', 'स्तोत्र', 'स्तोत्रम्', 'stotra', 'stuti', 'स्तुति', 'अष्टकम', 'ashtakam', 'कवच', 'kavach', 'शतनाम', 'नाम'],
        'mantra': ['mantra', 'मंत्र', 'जाप', 'jaap', '108', 'धून', 'dhun'],
        'bhajan': ['bhajan', 'भजन', 'गीत', 'song', 'kirtan', 'कीर्तन', 'पद'],
        'katha': ['katha', 'कथा', 'प्रसंग', 'कहानी', 'prasang', 'story', 'चरित्र'],
        'vrat_katha': ['vrat', 'व्रत', 'katha', 'कथा'],
        'naam_jaap': ['naam', 'नाम', 'jaap', 'जप', 'dhun', 'धुन', 'नामावली', '108'],
        'satsang': ['satsang', 'सत्संग', 'pravachan', 'प्रवचन']
    }
    syns = TYPE_SYNONYMS.get(content_type, [content_type])
    if any(s.lower() in norm_yt for s in syns):
        score += 15.0
        reasons.append(f"Type '{content_type}' verified in candidate")
        
    # 4. Trusted Channel Bonus
    if any(tc in yt_channel for tc in TRUSTED_CHANNELS):
        score += 15.0
        reasons.append(f"Trusted channel: '{yt_entry.get('uploader') or yt_entry.get('channel')}'")
        
    # 5. Sanity Checks & Duration Penalties
    if yt_duration > 0:
        if yt_duration < 45:
            score -= 30.0
            reasons.append("Penalized: duration < 45s (teaser)")
        elif yt_duration > 18000:
            score -= 15.0
            reasons.append("Penalized: duration > 5h")
        else:
            reasons.append(f"Duration {int(yt_duration//60)}m {int(yt_duration%60)}s")
            
    final_score = max(0.0, min(100.0, round(score, 1)))
    
    # High confidence criteria: score >= 80 and overlap >= 60%
    if final_score >= 80.0 and overlap_ratio >= 0.6:
        level = "HIGH"
    elif final_score >= 50.0:
        level = "MEDIUM"
    else:
        level = "LOW"
        
    return final_score, level, "; ".join(reasons)

ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'noplaylist': True,
    'socket_timeout': 10
}

results = []
high_count = 0
med_count = 0
low_count = 0
no_match_count = 0

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for idx, rec in enumerate(records_to_process, 1):
        query = build_search_query(rec)
        print(f"[{idx:03d}/100] DB Record: {rec['id']}")
        print(f"      Title: {rec['title']} ({rec.get('content_type')})")
        print(f"      Search: {query}")
        
        cand_url = None
        cand_title = None
        cand_channel = None
        cand_score = 0.0
        cand_level = "NO_MATCH"
        cand_reason = "Search returned no results"
        cand_duration = None
        
        try:
            search_query = f"ytsearch3:{query}"
            info = ydl.extract_info(search_query, download=False)
            entries = info.get('entries', [])
            
            best_entry = None
            best_score = -1.0
            best_level = "NO_MATCH"
            best_reason = ""
            
            for entry in entries:
                if not entry:
                    continue
                sc, lvl, rsn = score_candidate(rec, entry)
                if sc > best_score:
                    best_score = sc
                    best_level = lvl
                    best_reason = rsn
                    best_entry = entry
            
            if best_entry and best_score > 0:
                video_id = best_entry.get('id')
                cand_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else None
                cand_title = best_entry.get('title')
                cand_channel = best_entry.get('uploader') or best_entry.get('channel')
                cand_duration = best_entry.get('duration')
                cand_score = best_score
                cand_level = best_level
                cand_reason = best_reason
            else:
                cand_level = "NO_MATCH"
                cand_reason = "No relevant matches found"
                
        except Exception as ex:
            cand_level = "NO_MATCH"
            cand_reason = f"Search query error: {ex}"
            
        if cand_level == "HIGH":
            high_count += 1
        elif cand_level == "MEDIUM":
            med_count += 1
        elif cand_level == "LOW":
            low_count += 1
        else:
            no_match_count += 1
            
        print(f"      Result: [{cand_level}] Score: {cand_score} | Channel: {cand_channel}")
        if cand_title:
            print(f"      Video: {cand_title[:75]}")
        print(f"      URL: {cand_url}")
        print()
        
        # Speaker detection
        speaker = None
        tags = rec.get('tags') or ''
        if 'इंद्रेश' in tags or 'इंद्रेश' in rec['title']:
            speaker = 'पूज्य इंद्रेश उपाध्याय जी'
        elif 'राजन' in tags or 'राजन' in rec['title']:
            speaker = 'पूज्य राजन जी महाराज'
        elif 'अनूप' in rec['title']:
            speaker = 'अनूप जलोटा'
        elif 'अनुराधा' in rec['title']:
            speaker = 'अनुराधा पौडवाल'
            
        results.append({
            'index': idx,
            'record_id': rec['id'],
            'title': rec['title'],
            'title_en': rec.get('title_en'),
            'content_type': rec.get('content_type'),
            'deity_id': rec.get('deity_id'),
            'speaker': speaker,
            'search_query': query,
            'candidate_url': cand_url,
            'candidate_title': cand_title,
            'candidate_channel': cand_channel,
            'candidate_duration': cand_duration,
            'confidence_score': cand_score,
            'confidence_level': cand_level,
            'matching_reason': cand_reason
        })
        
        # Rate limit pause
        time.sleep(0.2)

# Save Report JSON
report_data = {
    'metadata': {
        'batch_name': 'Candidate Source Mapping 101–200',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'total_examined': len(records_to_process),
        'high_confidence_count': high_count,
        'medium_confidence_count': med_count,
        'low_confidence_count': low_count,
        'no_match_count': no_match_count,
        'existing_audio_preserved': total_working_audio,
        'database_modified': False,
        'db_modifications_count': 0
    },
    'candidates': results
}

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(SEP)
print("AUDIT EXECUTION COMPLETE")
print(SEP)
print(f"Report written to: {REPORT_PATH}")
print(f"Records Examined       : {len(records_to_process)}")
print(f"HIGH Confidence        : {high_count}")
print(f"MEDIUM Confidence      : {med_count}")
print(f"LOW Confidence         : {low_count}")
print(f"NO MATCH               : {no_match_count}")
print(f"Existing Audio Preserved: {total_working_audio} (38 Local MP3 + 19 YouTube)")
print(f"Database Modifications : 0 (READ-ONLY)")
print(SEP)
