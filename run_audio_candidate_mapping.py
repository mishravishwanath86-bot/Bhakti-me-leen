import sqlite3, sys, json, os, re, time, urllib.request, urllib.parse
from pathlib import Path
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
sys.path.insert(0, str(BASE_DIR))
from core.normalizer import normalize_devanagari

DB_PATH = BASE_DIR / "db" / "bhakti.db"
REPORT_PATH = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_001_100.json"

SEP = "=" * 75
SEP2 = "-" * 75

print(SEP)
print("AUTOMATIC AUDIO SOURCE MAPPING SYSTEM — 100 RECORDS CANDIDATE SEARCH")
print(SEP)
print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")

# 1. Fetch first 100 records without usable local audio
conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'assets/audio/%'")
working_audio_count = cur.fetchone()[0]

cur.execute("""
    SELECT id, title, title_en, deity_id, category_id, content_type, audio_url, short_description, tags
    FROM content_items
    WHERE audio_url IS NULL OR audio_url = '' OR audio_url NOT LIKE 'assets/audio/%'
    ORDER BY rowid
    LIMIT 100
""")
records_to_process = [dict(r) for r in cur.fetchall()]
conn.close()

print(f"Total records fetched for candidate search: {len(records_to_process)}")
print(f"Preserved working local audio records: {working_audio_count}")
print()

TRUSTED_CHANNELS = [
    't-series bhakti sagar', 'rajshri soul', 'sanskar tv', 'shemaroo bhakti',
    'bhakti', 'spiritual mantra', 'yuki music', 'tips devotional',
    'super digital bhakti', 'geetanjali devotional', 'times music spiritual',
    'sur mandir', 'satsang tv', 'subh tv', 'vedic mantras', 'stotra nidhi',
    'suresh wadkar', 'anuradha paudwal', 'gulshan kumar', 'bhajan india',
    'bhakti sangeet', 'anup jalota', 'hariharan', 'jagjit singh', 'sonotek bhakti',
    'ambey bhakti', 'nova spiritual india', 't-series', 'tseries'
]

def clean_for_search(title: str, content_type: str, deity_id: str) -> str:
    # remove punctuation
    t_clean = re.sub(r'[\(\)\[\]\-—:]', ' ', title).strip()
    t_clean = re.sub(r'\s+', ' ', t_clean)
    
    # Add genre keyword if helpful
    if content_type in ['aarti', 'chalisa', 'stotram', 'mantra', 'bhajan']:
        if content_type.lower() not in t_clean.lower() and content_type != 'stotram':
            t_clean += f" {content_type}"
    return t_clean.strip()

def direct_yt_search(query: str, max_results=3):
    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={encoded}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'hi,en;q=0.9'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        m = re.search(r'var ytInitialData = ({.*?});</script>', html)
        if not m:
            m = re.search(r'window\["ytInitialData"\] = ({.*?});', html)
            
        results = []
        if m:
            data = json.loads(m.group(1))
            try:
                sections = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']
                for sec in sections:
                    item_sec = sec.get('itemSectionRenderer', {}).get('contents', [])
                    for item in item_sec:
                        if 'videoRenderer' in item:
                            vr = item['videoRenderer']
                            vid_id = vr.get('videoId')
                            title = vr.get('title', {}).get('runs', [{}])[0].get('text', '')
                            channel = vr.get('ownerText', {}).get('runs', [{}])[0].get('text', '')
                            dur_txt = vr.get('lengthText', {}).get('simpleText', '')
                            if vid_id and title:
                                results.append({
                                    'id': vid_id,
                                    'title': title,
                                    'channel': channel,
                                    'duration_txt': dur_txt,
                                    'url': f"https://www.youtube.com/watch?v={vid_id}"
                                })
                                if len(results) >= max_results:
                                    break
            except Exception:
                pass
        return results
    except Exception as ex:
        return []

def score_candidate(rec: dict, yt_entry: dict) -> tuple[float, str, str]:
    if not yt_entry:
        return 0.0, "NO_MATCH", "No candidate video found from search"
    
    yt_title = yt_entry.get('title', '')
    yt_channel = (yt_entry.get('channel') or '').lower()
    
    db_title = rec['title']
    db_title_en = rec.get('title_en') or ''
    content_type = rec.get('content_type') or ''
    
    score = 0.0
    reasons = []
    
    norm_db = normalize_devanagari(db_title).lower()
    norm_yt = normalize_devanagari(yt_title).lower()
    
    tokens_db = set(re.findall(r'[a-zA-Z0-9\u0900-\u097F]+', norm_db))
    tokens_yt = set(re.findall(r'[a-zA-Z0-9\u0900-\u097F]+', norm_yt))
    
    stopwords = {'श्री', 'की', 'का', 'के', 'में', 'से', 'पर', 'और', 'एवं', 'द्वारा', 'पावन', 'दिव्य', 'सम्पूर्ण', 'पूर्ण', '108'}
    sig_db = {t for t in tokens_db if len(t) > 1 and t not in stopwords}
    
    overlap_ratio = 0.0
    if sig_db:
        overlap = sig_db.intersection(tokens_yt)
        overlap_ratio = len(overlap) / len(sig_db)
        score += overlap_ratio * 55.0
        reasons.append(f"Title Hindi token overlap {len(overlap)}/{len(sig_db)} ({int(overlap_ratio*100)}%)")
        
    if db_title_en:
        sig_en = {t.lower() for t in re.findall(r'[a-zA-Z0-9]+', db_title_en) if len(t) > 2 and t.lower() not in {'shri', 'the', 'and', 'with'}}
        sig_yt_en = {t.lower() for t in re.findall(r'[a-zA-Z0-9]+', yt_title) if len(t) > 2}
        if sig_en:
            en_overlap = sig_en.intersection(sig_yt_en)
            if en_overlap:
                en_ratio = len(en_overlap) / len(sig_en)
                score += min(15.0, en_ratio * 15.0)
                reasons.append(f"English token match: {', '.join(list(en_overlap)[:3])}")
                
    TYPE_SYNONYMS = {
        'aarti': ['aarti', 'आरती', 'arti'],
        'chalisa': ['chalisa', 'चालीसा'],
        'stotram': ['stotram', 'स्तोत्र', 'स्तोत्रम्', 'stotra', 'stuti', 'स्तुति', 'अष्टकम', 'ashtakam', 'कवच', 'kavach'],
        'mantra': ['mantra', 'मंत्र', 'जाप', 'jaap', '108'],
        'bhajan': ['bhajan', 'भजन', 'गीत', 'song', 'kirtan', 'कीर्तन', 'पद'],
        'katha': ['katha', 'कथा', 'प्रसंग', 'कहानी', 'prasang', 'story'],
        'vrat_katha': ['vrat', 'व्रत', 'katha', 'कथा'],
        'naam_jaap': ['naam', 'नाम', 'jaap', 'जप', 'dhun', 'धुन'],
        'satsang': ['satsang', 'सत्संग', 'pravachan', 'प्रवचन']
    }
    syns = TYPE_SYNONYMS.get(content_type, [content_type])
    if any(s.lower() in norm_yt for s in syns):
        score += 15.0
        reasons.append(f"Type '{content_type}' matched in candidate")
        
    if any(tc in yt_channel for tc in TRUSTED_CHANNELS):
        score += 15.0
        reasons.append(f"Trusted channel: '{yt_entry.get('channel')}'")
        
    final_score = max(0.0, min(100.0, round(score, 1)))
    
    if final_score >= 80.0 and overlap_ratio >= 0.55:
        level = "HIGH"
    elif final_score >= 48.0:
        level = "MEDIUM"
    else:
        level = "LOW"
        
    return final_score, level, "; ".join(reasons)

results = []
high_count = 0
med_count = 0
low_count = 0
no_match_count = 0

for idx, rec in enumerate(records_to_process, 1):
    query = clean_for_search(rec['title'], rec.get('content_type'), rec.get('deity_id'))
    print(f"[{idx:03d}/100] ID: {rec['id'][:45]:<45}")
    print(f"      Query: {query}")
    
    cand_url = None
    cand_title = None
    cand_channel = None
    cand_score = 0.0
    cand_level = "NO_MATCH"
    cand_reason = "Search returned no results"
    
    entries = direct_yt_search(query, max_results=3)
    time.sleep(0.15) # polite rate-limiting
    
    best_entry = None
    best_score = -1.0
    best_level = "NO_MATCH"
    best_reason = ""
    
    for entry in entries:
        sc, lvl, rsn = score_candidate(rec, entry)
        if sc > best_score:
            best_score = sc
            best_level = lvl
            best_reason = rsn
            best_entry = entry
            
    if best_entry and best_score > 0:
        cand_url = best_entry['url']
        cand_title = best_entry['title']
        cand_channel = best_entry['channel']
        cand_score = best_score
        cand_level = best_level
        cand_reason = best_reason
    else:
        cand_level = "NO_MATCH"
        cand_reason = "No relevant matches found"
        
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
        print(f"      Candidate: {cand_title[:75]}")
    print(f"      URL: {cand_url}")
    print()
    
    # Speaker identification
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
    elif 'मृदुल' in rec['title']:
        speaker = 'पूज्य मृदुल कृष्ण शास्त्री जी'
    elif 'चित्र विचित्र' in rec['title']:
        speaker = 'रसिका पागल / चित्र विचित्र'
        
    results.append({
        "record_id": rec['id'],
        "title": rec['title'],
        "type": rec['content_type'],
        "deity_id": rec.get('deity_id'),
        "speaker": speaker,
        "search_query": query,
        "candidate_url": cand_url,
        "candidate_title": cand_title,
        "source_channel": cand_channel,
        "confidence_score": cand_score,
        "confidence_level": cand_level,
        "matching_reason": cand_reason
    })

print(SEP)
print("AUDIT & GENERATION SUMMARY")
print(SEP)
print(f"TOTAL TESTED             : {len(results)}")
print(f"HIGH CONFIDENCE          : {high_count}")
print(f"MEDIUM CONFIDENCE        : {med_count}")
print(f"LOW CONFIDENCE           : {low_count}")
print(f"NO MATCH                 : {no_match_count}")
print(f"EXISTING AUDIO PRESERVED : {working_audio_count} (unchanged)")
print(f"DATABASE MODIFIED        : NO (Read-only candidate generation)")
print(SEP)

audit_data = {
    "workflow_type": "AUTOMATIC AUDIO SOURCE MAPPING SYSTEM (FIRST 100 RECORDS)",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "summary": {
        "TOTAL_TESTED": len(results),
        "HIGH_CONFIDENCE": high_count,
        "MEDIUM_CONFIDENCE": med_count,
        "LOW_CONFIDENCE": low_count,
        "NO_MATCH": no_match_count,
        "EXISTING_AUDIO_PRESERVED": working_audio_count,
        "DATABASE_MODIFIED": "NO"
    },
    "candidates": results
}

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
REPORT_PATH.write_text(json.dumps(audit_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Candidate report saved to: {REPORT_PATH}")
