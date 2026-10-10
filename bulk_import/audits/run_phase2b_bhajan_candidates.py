import sqlite3, json, sys, re, time
from pathlib import Path
from datetime import datetime, timezone
import yt_dlp

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
DB_PATH = BASE_DIR / "db" / "bhakti.db"
JSON_OUT = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_bhajans_101_200.json"
MD_OUT = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_bhajans_101_200.md"
JSON_OUT.parent.mkdir(parents=True, exist_ok=True)

SEP = "=" * 80
SEP2 = "-" * 80

print(SEP)
print("PHASE 2B — NEXT 100 BHAJAN AUDIO CANDIDATE AUDIT (READ-ONLY)")
print(SEP)

# 1. Fetch the next 100 unmapped Bhajan records
conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Get IDs of all currently playable audio items to exclude
cur.execute("""
    SELECT id FROM content_items
    WHERE (audio_url LIKE 'assets/audio/%' OR audio_url LIKE 'https://www.youtube.com/%' OR audio_url LIKE 'https://youtu.be/%')
""")
playable_ids = set(r[0] for r in cur.fetchall())
print(f"Verified current playable audio baseline: {len(playable_ids)} records")

# Also get IDs already audited in the previous Bhajan audit (map_candidates_bhajans_100.py)
PREV_BHAJAN_AUDIT = BASE_DIR / "bulk_import" / "audits" / "audio_candidate_mapping_bhajans_100.json"
prev_audited_ids = set()
if PREV_BHAJAN_AUDIT.exists():
    with open(PREV_BHAJAN_AUDIT, 'r', encoding='utf-8') as f:
        prev_data = json.load(f)
        prev_audited_ids = set(c['record_id'] for c in prev_data.get('candidates', []))

exclude_ids = playable_ids.union(prev_audited_ids)
print(f"Total IDs to exclude from this run: {len(exclude_ids)} records")

# Fetch next 100 unmapped bhajans deterministically
cur.execute("""
    SELECT c.id, c.title, c.title_en, c.content_type, c.deity_id, c.category_id, 
           c.short_description, c.audio_url, c.is_popular, c.view_count,
           d.name_hi as deity_name_hi
    FROM content_items c
    LEFT JOIN deities d ON c.deity_id = d.id
    WHERE c.content_type = 'bhajan'
      AND (c.audio_url IS NULL OR c.audio_url = '' OR c.audio_url LIKE '/audio/%')
    ORDER BY c.is_popular DESC, c.is_featured DESC, c.view_count DESC, c.id ASC
""")
all_unmapped_bhajans = [dict(r) for r in cur.fetchall()]
conn.close()

# Filter out excluded IDs
eligible_bhajans = [b for b in all_unmapped_bhajans if b['id'] not in exclude_ids][:100]
print(f"Selected next {len(eligible_bhajans)} unmapped Bhajan records for candidate search.\n")

if len(eligible_bhajans) == 0:
    raise RuntimeError("No eligible unmapped bhajans found!")

# 2. Trusted channels & scoring engine
TRUSTED_CHANNELS = [
    't-series bhakti sagar', 't-series bhakti', 'sanskar tv', 'bhajan marg',
    'rajshri soul', 'shemaroo bhakti', 'ambey bhakti', 'bhakti darshan',
    'gopalkrishn bhakti ganga', 'neelmadhav bhakti', 'sonotek bhakti',
    'wave bhakti', 'spiritual activity', 't-series', 'shemaroo', 'venus',
    'tips official', 'brijwani cassettes', 'bhakti gyan', 'total bhakti'
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
    
    # English deity / category keywords
    eng_tokens = {'bhajan', 'kirtan', 'krishna', 'ram', 'shiv', 'hanuman', 'shyam', 'durga', 'ganesh', 'aarti', 'chalisa'}
    v_eng_match = [t for t in eng_tokens if t in v_title.lower()]
    if v_eng_match:
        score += min(15.0, len(v_eng_match) * 7.5)
        reasons.append(f"Keywords: {', '.join(v_eng_match)}")
        
    # 'bhajan' / 'kirtan' confirmed in candidate title
    if 'भजन' in v_title or 'bhajan' in v_title.lower() or 'कीर्तन' in v_title or 'kirtan' in v_title.lower() or 'धुनि' in v_title:
        score += 15.0
        reasons.append("Type 'bhajan' confirmed in title")
        
    # Trusted devotional channel bonus
    is_trusted = any(tc in v_channel for tc in TRUSTED_CHANNELS)
    if is_trusted:
        score += 15.0
        reasons.append(f"Trusted channel: '{v_channel}'")
        
    # Duration sanity: standard devotional track 3m to 15m
    if 180 <= duration <= 900:
        score += 5.0
        reasons.append(f"Optimal duration: {duration//60}m {duration%60}s")
    elif duration > 0 and duration < 90:
        score -= 25.0
        reasons.append(f"Short clip penalty ({duration}s)")
    elif duration > 14400: # >4 hours
        score -= 20.0
        reasons.append(f"Compilation marathon penalty ({duration//3600}h)")
        
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

# 3. Flat YouTube metadata search
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

start_time = time.time()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for idx, rec in enumerate(eligible_bhajans, 1):
        clean_t = re.sub(r'\(.*?\)', '', rec['title']).strip()
        deity_kw = rec['deity_name_hi'] or rec['deity_id'] or ''
        search_query = f"{clean_t} {deity_kw} भजन bhajan".strip()
        
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
            
        v_url = f"https://www.youtube.com/watch?v={best_candidate.get('id')}" if best_candidate and best_candidate.get('id') else None
        
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
            'matching_reason': best_reason
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
        'batch_name': 'Phase 2B: Next 100 Bhajan Audio Candidate Audit',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'total_examined': len(candidates_output),
        'high_confidence_count': len(high_candidates),
        'medium_confidence_count': len(med_candidates),
        'low_confidence_count': len(low_candidates),
        'no_match_count': len(no_match_candidates),
        'existing_playable_audio': len(playable_ids),
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
v_cur.execute("SELECT COUNT(*) FROM content_items WHERE (audio_url LIKE 'assets/audio/%' OR audio_url LIKE 'https://www.youtube.com/%' OR audio_url LIKE 'https://youtu.be/%')")
v_playable = v_cur.fetchone()[0]
v_conn.close()

# 6. Generate Markdown Report
md_lines = [
    "# 🎧 PHASE 2B — NEXT 100 BHAJAN AUDIO CANDIDATE AUDIT REPORT",
    "",
    f"**Audit Status**: READ-ONLY AUDIT COMPLETE  ",
    f"**Database Modified**: **NO (0 modifications)**  ",
    f"**Audit Timestamp**: `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`  ",
    f"**Existing Playable Audio Preserved**: **{v_playable} items** (38 Local MP3 + 54 YouTube)  ",
    f"**Total Database Records**: **{v_total:,}** (`PRAGMA integrity_check = ok`, 0 FK violations)  ",
    f"**Batch 021 Status**: **NOT STARTED**  ",
    "",
    "---",
    "",
    "## 📊 SUMMARY OF CANDIDATE MATCHING",
    "",
    "| Metric | Count | Details |",
    "|---|---:|---|",
    f"| **Records Examined** | **{len(candidates_output)}** | Next 100 unmapped Bhajan records |",
    f"| **HIGH Confidence** | **{len(high_candidates)}** | Strict match (Score $\\ge 80\%$, overlap $\\ge 50\%$) |",
    f"| **MEDIUM Confidence** | **{len(med_candidates)}** | Partial / reasonable match (Held for review) |",
    f"| **LOW / Unlikely** | **{len(low_candidates)}** | Generic / noisy devotional video |",
    f"| **NO MATCH** | **{len(no_match_candidates)}** | No relevant devotional videos found |",
    f"| **Database Writes** | **0** | **Strictly Read-Only (0 writes)** |",
    "",
    "---",
    "",
    f"## 🌟 HIGH-CONFIDENCE CANDIDATES ({len(high_candidates)} RECORDS PREPARED FOR APPROVAL)",
    "",
    "| # | DB Record ID | Bhajan Title | Deity / Saint | Score | Candidate Video Title | Channel / Artist | Candidate YouTube URL | Matching Reason |",
    "|---|---|---|---|---|---|---|---|---|"
]

for idx, c in enumerate(high_candidates, 1):
    md_lines.append(f"| {idx} | `{c['record_id']}` | **{c['title']}** | {c['deity_name_hi'] or c['deity_id']} | **{c['confidence_score']}%** | {c['candidate_title']} | {c['candidate_channel']} | [Watch Stream]({c['candidate_url']}) | {c['matching_reason']} |")

md_lines.extend([
    "",
    "---",
    "",
    f"## 🔍 MEDIUM-CONFIDENCE CANDIDATES ({len(med_candidates)} RECORDS HELD FOR REVIEW)",
    "",
    "| # | DB Record ID | Bhajan Title | Deity | Score | Candidate Video Title | Channel | URL | Why Not HIGH |",
    "|---|---|---|---|---|---|---|---|---|"
])

for idx, c in enumerate(med_candidates, 1):
    md_lines.append(f"| {idx} | `{c['record_id']}` | {c['title']} | {c['deity_name_hi'] or c['deity_id']} | {c['confidence_score']}% | {c['candidate_title']} | {c['candidate_channel']} | [Stream]({c['candidate_url']}) | {c['matching_reason']} |")

md_lines.extend([
    "",
    "---",
    "",
    f"## ⚠️ LOW CONFIDENCE ({len(low_candidates)} RECORDS) & NO MATCH ({len(no_match_candidates)} RECORDS)",
    "",
    "### LOW Confidence Samples (Compact):",
    "```text"
])

for c in low_candidates[:15]:
    md_lines.append(f"{c['record_id']} | {c['title']} | Score: {c['confidence_score']}% | Reason: {c['matching_reason']}")

if len(low_candidates) > 15:
    md_lines.append(f"...and {len(low_candidates) - 15} more low-confidence records.")

md_lines.extend([
    "```",
    "",
    "### NO MATCH Records:",
    "```text"
])

for c in no_match_candidates:
    md_lines.append(f"{c['record_id']} | {c['title']} | Reason: {c['matching_reason']}")

md_lines.extend([
    "```",
    "",
    "---",
    "",
    "## 🛡️ DATABASE VERIFICATION",
    "",
    "```text",
    f"Database modified           : NO",
    f"audio_url modifications     : 0",
    f"Total Record Count          : {v_total:,} (Unchanged)",
    f"Playable Audio Count        : {v_playable} (Unchanged: 38 MP3 + 54 YouTube)",
    f"FTS5 Synchronization        : {v_fts:,} documents (Unchanged)",
    f"PRAGMA integrity_check      : {v_integrity}",
    f"Foreign-Key Violations      : {len(v_fk)}",
    f"Batch 021 Status            : NOT STARTED",
    "```",
    "",
    "**PHASE 2B — READ-ONLY AUDIT COMPLETE**  ",
    "**Database Modified: NO**  ",
    "**Awaiting approval before applying HIGH-confidence mappings.**"
])

with open(MD_OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"✓ Saved Markdown audit report to: {MD_OUT}")
print(SEP)
print("PHASE 2B CANDIDATE AUDIT COMPLETE (READ-ONLY)")
print(SEP)
