import sqlite3, json, sys, os, glob, re

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🔍 PHASE 2Z — STEP 1 & 2: TARGET POOL IDENTIFICATION & BASELINE AUDIT")
print("======================================================================")

db_path = 'db/bhakti.db'
conn = sqlite3.connect(f'file:{os.path.abspath(db_path)}?mode=ro', uri=True)
cursor = conn.cursor()

# Total Authoritative Katha
cursor.execute("SELECT count(*) FROM content_items WHERE content_type='katha';")
total_katha = cursor.fetchone()[0]

# Katha with Audio
cursor.execute("SELECT count(*) FROM content_items WHERE content_type='katha' AND audio_url IS NOT NULL AND trim(audio_url) != '';")
with_audio = cursor.fetchone()[0]

# Katha with Video
cursor.execute("SELECT count(*) FROM content_items WHERE content_type='katha' AND video_url IS NOT NULL AND trim(video_url) != '';")
with_video = cursor.fetchone()[0]

# Katha with Both
cursor.execute("SELECT count(*) FROM content_items WHERE content_type='katha' AND audio_url IS NOT NULL AND trim(audio_url) != '' AND video_url IS NOT NULL AND trim(video_url) != '';")
with_both = cursor.fetchone()[0]

# Katha with Neither (Target Pool)
cursor.execute("SELECT count(*) FROM content_items WHERE content_type='katha' AND (audio_url IS NULL OR trim(audio_url) = '') AND (video_url IS NULL OR trim(video_url) = '');")
with_neither = cursor.fetchone()[0]

print(f"PHASE 2Z TARGET BASELINE\n")
print(f"Total Authoritative Katha : {total_katha}")
print(f"Already With Audio       : {with_audio}")
print(f"Already With Video       : {with_video}")
print(f"With Both                : {with_both}")
print(f"With Neither             : {with_neither}")
print(f"\nTarget Media-Less Pool   : {with_neither}")

assert total_katha == 505, f"Expected 505 total katha, got {total_katha}"
assert with_audio == 334, f"Expected 334 with audio, got {with_audio}"
assert with_video == 225, f"Expected 225 with video, got {with_video}"
assert with_both == 201, f"Expected 201 with both, got {with_both}"
assert with_neither == 147, f"Expected 147 target media-less pool, got {with_neither}"

# Fetch all 147 target records
cursor.execute("""
    SELECT id, title, deity_id, category_id, short_description, tags 
    FROM content_items 
    WHERE content_type='katha' AND (audio_url IS NULL OR trim(audio_url) = '') AND (video_url IS NULL OR trim(video_url) = '')
    ORDER BY id;
""")
target_rows = cursor.fetchall()
print(f"\nSuccessfully retrieved all {len(target_rows)} target media-less Katha records.")

# Inspect sample target rows
print("\nSample 5 Target Records:")
for r in target_rows[:5]:
    print(f"  [{r[0]}] {r[1]} (Deity: {r[2]}, Cat: {r[3]})")

conn.close()

# -------------------------------------------------------------------
# STEP 3 & 4: BUILD CANONICAL EXCLUSION SET FROM PREVIOUS PHASES
# -------------------------------------------------------------------
print("\n=== Building Exclusion Set from Previous Phases ===")
exclusion_urls = set()
exclusion_yt_ids = set()

# Load all existing candidate and audit JSON files
candidate_files = glob.glob('bulk_import/audits/*phase_2*.json') + glob.glob('bulk_import/audits/*katha*.json')
for fpath in candidate_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            cdata = json.load(f)
            # Recursively collect URLs and YouTube IDs
            s = json.dumps(cdata)
            # Find URLs
            urls = re.findall(r'https?://[^\s",\'\\]+', s)
            for u in urls:
                exclusion_urls.add(u)
                m = re.search(r'(?:v=|\/embed\/|\.be\/)([a-zA-Z0-9_-]{11})', u)
                if m:
                    exclusion_yt_ids.add(m.group(1))
    except Exception as e:
        pass

print(f"Total Previous URLs in Exclusion Set: {len(exclusion_urls)}")
print(f"Total Previous YouTube IDs in Exclusion Set: {len(exclusion_yt_ids)}")
