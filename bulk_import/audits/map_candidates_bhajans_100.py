import sqlite3, json, sys, re, time
from pathlib import Path
from datetime import datetime, timezone
import yt_dlp

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
DB_PATH = BASE_DIR / "db" / "bhakti.db"
OUTPUT_JSON = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_bhajans_100.json"
OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)

SEP = "=" * 80
SEP2 = "-" * 80

print(SEP)
print("BHAKTI AUDIO LIBRARY — BHAJAN HIGH-CONFIDENCE CANDIDATE EXTRACTION (100 RECORDS)")
print(SEP)

# 1. Fetch top 100 unmapped Bhajan records
conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
    SELECT c.id, c.title, c.content_type, c.deity_id, c.audio_url,
           d.name_hi as deity_name_hi
    FROM content_items c
    LEFT JOIN deities d ON c.deity_id = d.id
    WHERE c.content_type = 'bhajan'
      AND (c.audio_url IS NULL OR c.audio_url = '' OR c.audio_url LIKE '/audio/%')
    ORDER BY c.is_popular DESC, c.is_featured DESC, c.view_count DESC, c.id ASC
    LIMIT 100
""")
bhajan_records = [dict(r) for r in cur.fetchall()]
conn.close()

print(f"Loaded {len(bhajan_records)} unmapped Bhajan records for matching.\n")

# 2. Trusted channels
TRUSTED_CHANNELS = [
    't-series bhakti sagar', 't-series bhakti', 'sanskar tv', 'bhajan marg',
    'rajshri soul', 'shemaroo bhakti', 'ambey bhakti', 'bhakti darshan',
    'gopalkrishn bhakti ganga', 'neelmadhav bhakti', 'sonotek bhakti',
    'wave bhakti', 'spiritual activity', 't-series', 'shemaroo', 'venus',
    'tips official', 'brijwani cassettes', 'bhakti gyan'
]

def clean_tokens(text):
    if not text: return set()
    cleaned = re.sub(r'\(.*?\)', '', text)
    cleaned = re.sub(r'[^\w\s]', ' ', cleaned)
    tokens = [t.lower() for t in cleaned.split() if len(t) > 1 and t not in ('की', 'के', 'का', 'में', 'पर', 'से', 'को', 'और', 'एवं', 'ji', 'shri', 'ji', 'ki', 'ka', 'ke', 'b20', 'b19', 'b18', 'b17', 'b16')]
    return set(tokens)

def compute_match_score(db_record, video_info):
    v_title = video_info.get('title', '')
    v_channel = (video_info.get('uploader') or video_info.get('channel') or '').lower()
    duration = video_info.get('duration') or 0
    
    db_tokens = clean_tokens(db_record['title'])
    v_tokens = clean_tokens(v_title)
    
    if not db_tokens:
        return 0.0, "Empty DB tokens", "NO_MATCH"
        
    overlap = db_tokens.intersection(v_tokens)
    overlap_ratio = len(overlap) / len(db_tokens)
    
    score = overlap_ratio * 55.0  # Up to 55 pts
    reasons = [f"Token overlap: {len(overlap)}/{len(db_tokens)} ({round(overlap_ratio*100)}%)"]
    
    # English title match
    eng_tokens = {'bhajan', 'kirtan', 'krishna', 'ram', 'shiv', 'hanuman', 'shyam', 'durga', 'aarti'}
    v_eng_match = [t for t in eng_tokens if t in v_title.lower()]
    if v_eng_match:
        score += min(15.0, len(v_eng_match) * 7.5)
        reasons.append(f"Keywords: {', '.join(v_eng_match)}")
        
    # 'bhajan' or 'kirtan' in candidate title
    if 'भजन' in v_title or 'bhajan' in v_title.lower() or 'कीर्तन' in v_title or 'kirtan' in v_title.lower() or 'धुनि' in v_title:
        score += 15.0
        reasons.append("Type 'bhajan' confirmed in candidate")
        
    # Trusted channel bonus
    is_trusted = any(tc in v_channel for tc in TRUSTED_CHANNELS)
    if is_trusted:
        score += 15.0
        reasons.append(f"Trusted channel: '{v_channel}'")
        
    # Duration sanity check: ideal bhajan 3m - 15m
    if 180 <= duration <= 900:
        score += 5.0
        reasons.append(f"Optimal duration: {duration//60}m {duration%60}s")
    elif duration > 0 and duration < 90:
        score -= 25.0
        reasons.append(f"Short clip penalty: {duration}s")
    elif duration > 14400: # >4 hours
        score -= 20.0
        reasons.append(f"Compilation marathon penalty: {duration//3600}h")
        
    score = min(100.0, max(0.0, score))
    
    if score >= 80.0 and overlap_ratio >= 0.50:
        level = "HIGH"
    elif score >= 50.0:
        level = "MEDIUM"
    elif score >= 20.0:
        level = "LOW"
    else:
        level = "NO_MATCH"
        
    return score, "; ".join(reasons), level

# 3. YDL Configuration (Flat search, metadata only)
ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'skip_download': True,
    'default_search': 'ytsearch3',
    'socket_timeout': 10,
    'no_warnings': True,
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

candidates_output = []
high_count = 0
med_count = 0
low_count = 0
no_match_count = 0

start_time = time.time()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for idx, rec in enumerate(bhajan_records, 1):
        clean_t = re.sub(r'\(.*?\)', '', rec['title']).strip()
        search_query = f"{clean_t} भजन bhajan"
        
        best_candidate = None
        best_score = -1.0
        best_reason = ""
        best_level = "NO_MATCH"
        
        try:
            res = ydl.extract_info(f"ytsearch3:{search_query}", download=False)
            entries = res.get('entries', []) if res else []
            
            for ent in entries:
                if not ent: continue
                s, r, lvl = compute_match_score(rec, ent)
                if s > best_score:
                    best_score = s
                    best_reason = r
                    best_level = lvl
                    best_candidate = ent
        except Exception as e:
            best_reason = f"Search error: {str(e)}"
            
        if best_level == "HIGH": high_count += 1
        elif best_level == "MEDIUM": med_count += 1
        elif best_level == "LOW": low_count += 1
        else: no_match_count += 1
        
        v_url = f"https://www.youtube.com/watch?v={best_candidate.get('id')}" if best_candidate and best_candidate.get('id') else None
        
        candidate_entry = {
            'record_id': rec['id'],
            'title': rec['title'],
            'content_type': rec['content_type'],
            'deity_id': rec['deity_id'],
            'search_query': search_query,
            'candidate_url': v_url,
            'candidate_title': best_candidate.get('title') if best_candidate else None,
            'candidate_channel': best_candidate.get('uploader') or best_candidate.get('channel') if best_candidate else None,
            'confidence_score': round(best_score, 1),
            'confidence_level': best_level,
            'matching_reason': best_reason
        }
        candidates_output.append(candidate_entry)
        
        print(f"[{idx:03d}/100] [{best_level:8s}] Score: {best_score:4.1f} | DB: {rec['title'][:32]} -> {candidate_entry['candidate_title'][:40] if candidate_entry['candidate_title'] else 'None'}")

# 4. Save JSON Report
audit_report = {
    'metadata': {
        'batch_name': 'Bhajan Top 100 High-Confidence Audio Mapping',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'total_examined': len(candidates_output),
        'high_confidence_count': high_count,
        'medium_confidence_count': med_count,
        'low_confidence_count': low_count,
        'no_match_count': no_match_count,
        'database_modified': False,
        'db_modifications_count': 0,
        'batch_021_started': False,
        'time_taken_seconds': round(time.time() - start_time, 2)
    },
    'candidates': candidates_output
}

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(audit_report, f, ensure_ascii=False, indent=2)

print("\n" + SEP)
print("BHAJAN CANDIDATE MAPPING COMPLETE (READ-ONLY)")
print(SEP)
print(f"Total Examined    : {len(candidates_output)}")
print(f"HIGH Confidence   : {high_count}")
print(f"MEDIUM Confidence : {med_count}")
print(f"LOW Confidence    : {low_count}")
print(f"NO MATCH          : {no_match_count}")
print(f"Report File       : {OUTPUT_JSON}")
print("=" * 80)
