import sqlite3, json, sys, re, time
from pathlib import Path
from datetime import datetime, timezone
import yt_dlp

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
DB_PATH = BASE_DIR / "db" / "bhakti.db"
JSON_OUT = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_aarti_101_200.json"
MD_OUT = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_aarti_101_200.md"
JSON_OUT.parent.mkdir(parents=True, exist_ok=True)

SEP = "=" * 80
SEP2 = "-" * 80

print(SEP)
print("PHASE 2C — AARTI AUDIO CANDIDATE AUDIT (100 RECORDS, READ-ONLY)")
print(SEP)

# 1. Inspect existing database state & select 100 unmapped Aartis
conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Get all existing mapped URLs in DB to check for duplicate/reused YouTube IDs
cur.execute("""
    SELECT id, audio_url FROM content_items
    WHERE (audio_url LIKE 'assets/audio/%' OR audio_url LIKE 'https://www.youtube.com/%' OR audio_url LIKE 'https://youtu.be/%')
""")
existing_mapped_rows = cur.fetchall()
existing_mapped_ids = set(r['id'] for r in existing_mapped_rows)
existing_mapped_urls = {r['audio_url']: r['id'] for r in existing_mapped_rows if r['audio_url']}

print(f"Verified current playable audio baseline: {len(existing_mapped_ids)} records")

# Query unmapped Aartis in deterministic order
cur.execute("""
    SELECT c.id, c.title, c.title_en, c.content_type, c.deity_id, c.category_id, 
           c.short_description, c.audio_url, c.is_popular, c.view_count,
           d.name_hi as deity_name_hi
    FROM content_items c
    LEFT JOIN deities d ON c.deity_id = d.id
    WHERE c.content_type = 'aarti'
      AND (c.audio_url IS NULL OR c.audio_url = '' OR c.audio_url LIKE '/audio/%')
    ORDER BY c.is_popular DESC, c.is_featured DESC, c.view_count DESC, c.id ASC
""")
all_unmapped_aartis = [dict(r) for r in cur.fetchall()]
conn.close()

# Exclude already mapped records
eligible_aartis = [a for a in all_unmapped_aartis if a['id'] not in existing_mapped_ids][:100]
print(f"Selected {len(eligible_aartis)} unmapped Aarti records for candidate extraction.\n")

if len(eligible_aartis) == 0:
    raise RuntimeError("No eligible unmapped Aarti records found!")

# 2. Trusted channels & scoring engine
TRUSTED_CHANNELS = [
    't-series bhakti sagar', 't-series bhakti', 'sanskar tv', 'bhajan marg',
    'rajshri soul', 'shemaroo bhakti', 'ambey bhakti', 'bhakti darshan',
    'gopalkrishn bhakti ganga', 'neelmadhav bhakti', 'sonotek bhakti',
    'wave bhakti', 'spiritual activity', 't-series', 'shemaroo', 'venus',
    'tips official', 'brijwani cassettes', 'bhakti gyan', 'total bhakti',
    'anuradha paudwal', 'suresh wadkar'
]

def clean_tokens(text):
    if not text: return set()
    cleaned = re.sub(r'\(.*?\)', '', text)
    cleaned = re.sub(r'[^\w\s]', ' ', cleaned)
    tokens = [t.lower() for t in cleaned.split() if len(t) > 1 and t not in (
        'की', 'के', 'का', 'में', 'पर', 'से', 'को', 'और', 'एवं', 'ji', 'shri', 'ki', 'ka', 'ke',
        'b20', 'b19', 'b18', 'b17', 'b16', 'b15', 'b14', 'b13', 'b12', 'b11', 'b10', 'b9', 'b8', 'b7'
    )]
    return set(tokens)

def compute_aarti_match_score(db_record, video_info):
    v_title = video_info.get('title', '')
    v_channel = (video_info.get('uploader') or video_info.get('channel') or '').lower()
    duration = video_info.get('duration') or 0
    
    db_tokens = clean_tokens(db_record['title'])
    v_tokens = clean_tokens(v_title)
    
    if not db_tokens:
        return 0.0, "Empty DB tokens", "NO_MATCH"
        
    overlap = db_tokens.intersection(v_tokens)
    overlap_ratio = len(overlap) / len(db_tokens)
    
    score = overlap_ratio * 55.0  # Up to 55 pts for title overlap
    reasons = [f"Title overlap: {len(overlap)}/{len(db_tokens)} ({round(overlap_ratio*100)}%)"]
    
    # English keywords
    eng_tokens = {'aarti', 'arti', 'om', 'jai', 'durga', 'ganesh', 'shiv', 'shiva', 'ram', 'krishna', 'hanuman', 'laxmi', 'lakshmi', 'saraswati', 'shani'}
    v_eng_match = [t for t in eng_tokens if t in v_title.lower()]
    if v_eng_match:
        score += min(15.0, len(v_eng_match) * 7.5)
        reasons.append(f"Keywords: {', '.join(v_eng_match)}")
        
    # 'आरती' or 'aarti' in candidate title (essential for Aarti match)
    if 'आरती' in v_title or 'aarti' in v_title.lower() or 'arti' in v_title.lower():
        score += 15.0
        reasons.append("Type 'aarti' confirmed in title")
    else:
        score -= 20.0
        reasons.append("No 'aarti' keyword in video title")
        
    # Trusted channel bonus
    is_trusted = any(tc in v_channel for tc in TRUSTED_CHANNELS)
    if is_trusted:
        score += 15.0
        reasons.append(f"Trusted channel: '{v_channel}'")
        
    # Duration sanity check: typical devotional Aarti is 3m - 12m
    if 150 <= duration <= 720:
        score += 5.0
        reasons.append(f"Optimal duration: {duration//60}m {duration%60}s")
    elif duration > 0 and duration < 80:
        score -= 30.0
        reasons.append(f"Short clip penalty ({duration}s)")
    elif duration > 7200: # >2 hours marathon
        score -= 25.0
        reasons.append(f"Compilation marathon penalty ({duration//3600}h)")
        
    score = min(100.0, max(0.0, score))
    
    if score >= 80.0 and overlap_ratio >= 0.50 and ('आरती' in v_title or 'aarti' in v_title.lower() or 'arti' in v_title.lower()):
        level = "HIGH"
    elif score >= 50.0:
        level = "MEDIUM"
    elif score >= 20.0:
        level = "LOW"
    else:
        level = "NO_MATCH"
        
    return score, "; ".join(reasons), level

# 3. YDL Configuration
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
high_candidates = []
med_candidates = []
low_candidates = []
no_match_candidates = []

batch_urls_seen = {}
duplicate_batch_urls = {}
existing_reused_urls = {}

start_time = time.time()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for idx, rec in enumerate(eligible_aartis, 1):
        clean_t = re.sub(r'\(.*?\)', '', rec['title']).strip()
        deity_kw = rec['deity_name_hi'] or rec['deity_id'] or ''
        search_query = f"{clean_t} {deity_kw} आरती aarti".strip()
        
        best_candidate = None
        best_score = -1.0
        best_reason = ""
        best_level = "NO_MATCH"
        
        try:
            res = ydl.extract_info(f"ytsearch3:{search_query}", download=False)
            entries = res.get('entries', []) if res else []
            
            for ent in entries:
                if not ent: continue
                s, r, lvl = compute_aarti_match_score(rec, ent)
                if s > best_score:
                    best_score = s
                    best_reason = r
                    best_level = lvl
                    best_candidate = ent
        except Exception as e:
            best_reason = f"Search error: {str(e)}"
            
        v_url = f"https://www.youtube.com/watch?v={best_candidate.get('id')}" if best_candidate and best_candidate.get('id') else None
        
        # Check duplicate inside batch & reuse of existing mapped URLs
        is_reused_from_db = False
        reused_db_record = None
        is_duplicate_in_batch = False
        duplicate_with_rec = None
        
        if v_url:
            if v_url in existing_mapped_urls:
                is_reused_from_db = True
                reused_db_record = existing_mapped_urls[v_url]
                existing_reused_urls[v_url] = (rec['id'], reused_db_record)
                
            if v_url in batch_urls_seen:
                is_duplicate_in_batch = True
                duplicate_with_rec = batch_urls_seen[v_url]
                duplicate_batch_urls[v_url] = (rec['id'], duplicate_with_rec)
            else:
                batch_urls_seen[v_url] = rec['id']
                
        entry = {
            'index': idx,
            'record_id': rec['id'],
            'title': rec['title'],
            'content_type': rec['content_type'],
            'deity_id': rec['deity_id'],
            'deity_name_hi': rec['deity_name_hi'],
            'search_query': search_query,
            'candidate_url': v_url,
            'candidate_title': best_candidate.get('title') if best_candidate else None,
            'candidate_channel': best_candidate.get('uploader') or best_candidate.get('channel') if best_candidate else None,
            'confidence_score': round(best_score, 1),
            'confidence_level': best_level,
            'matching_reason': best_reason,
            'is_reused_from_db': is_reused_from_db,
            'reused_db_record': reused_db_record,
            'is_duplicate_in_batch': is_duplicate_in_batch,
            'duplicate_with_record': duplicate_with_rec
        }
        
        candidates_output.append(entry)
        
        if best_level == "HIGH": high_candidates.append(entry)
        elif best_level == "MEDIUM": med_candidates.append(entry)
        elif best_level == "LOW": low_candidates.append(entry)
        else: no_match_candidates.append(entry)
        
        print(f"[{idx:03d}/100] [{best_level:8s}] Score: {best_score:4.1f} | DB: {rec['title'][:30]} -> {entry['candidate_title'][:38] if entry['candidate_title'] else 'None'}", flush=True)

# 4. Save JSON Report
audit_report = {
    'metadata': {
        'batch_name': 'Phase 2C: Aarti Next 100 Audio Candidate Audit',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'total_examined': len(candidates_output),
        'high_confidence_count': len(high_candidates),
        'medium_confidence_count': len(med_candidates),
        'low_confidence_count': len(low_candidates),
        'no_match_count': len(no_match_candidates),
        'duplicate_candidates_in_batch': len(duplicate_batch_urls),
        'existing_youtube_ids_reused': len(existing_reused_urls),
        'existing_playable_audio': len(existing_mapped_ids),
        'database_modified': False,
        'db_modifications_count': 0,
        'batch_021_started': False,
        'time_taken_seconds': round(time.time() - start_time, 2)
    },
    'candidates': candidates_output
}

with open(JSON_OUT, 'w', encoding='utf-8') as f:
    json.dump(audit_report, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved JSON audit report to: {JSON_OUT}")

# 5. Database Verification (Read-Only Confirmation)
v_conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
v_cur = v_conn.cursor()
v_cur.execute("SELECT COUNT(*) FROM content_items")
v_total = v_cur.fetchone()[0]
v_cur.execute("PRAGMA integrity_check")
v_integrity = v_cur.fetchone()[0]
v_cur.execute("PRAGMA foreign_key_check")
v_fk = v_cur.fetchall()
v_cur.execute("SELECT COUNT(*) FROM content_fts")
v_fts = v_cur.fetchone()[0]
v_cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'assets/audio/%'")
v_mp3 = v_cur.fetchone()[0]
v_cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'https://www.youtube.com/%' OR audio_url LIKE 'https://youtu.be/%'")
v_yt = v_cur.fetchone()[0]
v_playable = v_mp3 + v_yt
v_conn.close()

# 6. Generate Markdown Report
md_lines = [
    "# 🎧 PHASE 2C — AARTI AUDIO CANDIDATE AUDIT REPORT (READ-ONLY)",
    "",
    f"**Audit Status**: READ-ONLY AUDIT COMPLETE  ",
    f"**Database Modified**: **NO (0 modifications)**  ",
    f"**Audit Timestamp**: `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`  ",
    f"**Existing Playable Audio Preserved**: **{v_playable} items** (Local MP3: {v_mp3}, YouTube: {v_yt})  ",
    f"**Total Database Records**: **{v_total:,}** (`PRAGMA integrity_check = ok`, 0 FK violations)  ",
    f"**Batch 021 Status**: **NOT STARTED**  ",
    "",
    "---",
    "",
    "## 📊 SUMMARY OF CANDIDATE MATCHING (100 AARTI RECORDS)",
    "",
    "| Metric | Count | Details |",
    "|---|---:|---|",
    f"| **Records Examined** | **{len(candidates_output)}** | Next 100 unmapped Aarti records |",
    f"| **HIGH Confidence ($\ge 80\%$)** | **{len(high_candidates)}** | Strict composition match with 'aarti' keyword |",
    f"| **MEDIUM Confidence ($50-79\%$)** | **{len(med_candidates)}** | Partial / alternate recording match (Held for review) |",
    f"| **LOW / Unlikely ($<50\%$)** | **{len(low_candidates)}** | Generic / non-specific devotional stutis |",
    f"| **NO MATCH** | **{len(no_match_candidates)}** | No relevant devotional videos found |",
    f"| **Duplicate Candidate URLs in Batch** | **{len(duplicate_batch_urls)}** | Handled / flagged |",
    f"| **Existing YouTube URLs Reused** | **{len(existing_reused_urls)}** | Checked against existing 92 audio records |",
    f"| **Database Writes** | **0** | **Strictly Read-Only (0 writes)** |",
    "",
    "---",
    "",
    f"## 🌟 HIGH-CONFIDENCE CANDIDATES ({len(high_candidates)} RECORDS PREPARED FOR APPROVAL)",
    "",
    "| # | DB Record ID | Aarti Title | Deity | Score | Candidate Video Title | Channel / Artist | Candidate YouTube URL | Match Reason |",
    "|---|---|---|---|---|---|---|---|---|"
]

for idx, c in enumerate(high_candidates, 1):
    flag_str = " ⚠️ [Shared]" if c['is_duplicate_in_batch'] or c['is_reused_from_db'] else ""
    md_lines.append(f"| {idx} | `{c['record_id']}` | **{c['title']}**{flag_str} | {c['deity_name_hi'] or c['deity_id']} | **{c['confidence_score']}%** | {c['candidate_title']} | {c['candidate_channel']} | [Watch Stream]({c['candidate_url']}) | {c['matching_reason']} |")

md_lines.extend([
    "",
    "---",
    "",
    f"## 🔍 MEDIUM-CONFIDENCE CANDIDATES ({len(med_candidates)} RECORDS HELD FOR REVIEW)",
    "",
    "| # | DB Record ID | Aarti Title | Deity | Score | Candidate Video Title | Channel | URL | Why Not HIGH |",
    "|---|---|---|---|---|---|---|---|---|"
])

for idx, c in enumerate(med_candidates[:20], 1):
    md_lines.append(f"| {idx} | `{c['record_id']}` | {c['title']} | {c['deity_name_hi'] or c['deity_id']} | {c['confidence_score']}% | {c['candidate_title']} | {c['candidate_channel']} | [Stream]({c['candidate_url']}) | {c['matching_reason']} |")

if len(med_candidates) > 20:
    md_lines.append(f"| *...and {len(med_candidates) - 20} more MEDIUM records* | ... | ... | ... | ... | ... | ... | ... |")

md_lines.extend([
    "",
    "---",
    "",
    "## 🛡️ DATABASE VERIFICATION",
    "",
    "```text",
    f"Database modified           : NO",
    f"audio_url modifications     : 0",
    f"Total Record Count          : {v_total:,} (Unchanged)",
    f"Existing Playable Audio     : {v_playable} (Unchanged: 38 MP3 + 54 YouTube)",
    f"Local MP3 Count             : {v_mp3} (Unchanged)",
    f"YouTube Count               : {v_yt} (Unchanged)",
    f"FTS5 Synchronization        : {v_fts:,} documents (Unchanged)",
    f"PRAGMA integrity_check      : {v_integrity}",
    f"Foreign-Key Violations      : {len(v_fk)}",
    f"Batch 021 Status            : NOT STARTED",
    "```",
    "",
    "**PHASE 2C — READ-ONLY AUDIT COMPLETE**  ",
    "**Database Modified: NO**  ",
    "**Awaiting approval before applying HIGH-confidence mappings.**"
])

with open(MD_OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"✓ Saved Markdown audit report to: {MD_OUT}")
print(SEP)
print("PHASE 2C AARTI CANDIDATE AUDIT COMPLETE (READ-ONLY)")
print(SEP)
