import sqlite3, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

print("=== STEP 1 & STEP 2: PRE-APPLY AND SAFETY VALIDATION ===")

conn = sqlite3.connect('db/bhakti.db')
cursor = conn.cursor()

# 1. Load Phase 2Y JSON
with open('bulk_import/audits/phase_2Y_human_assisted_verification.json', 'r', encoding='utf-8') as f:
    p2y = json.load(f)

group_a = p2y.get('group_a_review_records', [])
group_b = p2y.get('group_b_no_suitable_records', [])

approved_mappings = []
uncertain_mappings = []
no_suitable_mappings = []

for r in group_a:
    kid = r['katha_id']
    title = r['title']
    
    # Audio
    audio = r.get('audio', {})
    a_rec = audio.get('recommendation')
    if a_rec == 'APPROVE':
        approved_mappings.append({
            'katha_id': kid,
            'title': title,
            'type': 'AUDIO',
            'candidate_title': audio.get('candidate_title'),
            'url': audio.get('candidate_url'),
            'canonical_url': audio.get('candidate_url'),
            'source': audio.get('source'),
            'confidence': audio.get('confidence'),
            'human_decision': 'APPROVE',
            'evidence': audio.get('evidence')
        })
    else:
        uncertain_mappings.append({
            'katha_id': kid,
            'title': title,
            'type': 'AUDIO',
            'url': audio.get('candidate_url'),
            'human_decision': a_rec or 'UNCERTAIN'
        })
        
    # Video
    video = r.get('video', {})
    v_rec = video.get('recommendation')
    if v_rec == 'APPROVE':
        approved_mappings.append({
            'katha_id': kid,
            'title': title,
            'type': 'VIDEO',
            'candidate_title': video.get('candidate_title'),
            'url': video.get('candidate_url'),
            'canonical_url': video.get('candidate_url'),
            'source': video.get('source'),
            'confidence': video.get('confidence'),
            'human_decision': 'APPROVE',
            'evidence': video.get('evidence')
        })
    else:
        uncertain_mappings.append({
            'katha_id': kid,
            'title': title,
            'type': 'VIDEO',
            'url': video.get('candidate_url'),
            'human_decision': v_rec or 'UNCERTAIN'
        })

for r in group_b:
    no_suitable_mappings.append({
        'katha_id': r['katha_id'],
        'title': r['title'],
        'status': 'NO_SUITABLE'
    })

print(f"Total Approved Mappings to Process: {len(approved_mappings)}")
print(f"Total Uncertain Mappings (NOT applied): {len(uncertain_mappings)}")
print(f"Total No-Suitable Records (NOT applied): {len(no_suitable_mappings)}")

# Validate each approved mapping
safety_errors = []
for m in approved_mappings:
    kid = m['katha_id']
    mtype = m['type']
    url = m['url']
    
    # Check Katha exists in DB
    cursor.execute("SELECT id, title, audio_url, video_url FROM content_items WHERE id=?;", (kid,))
    row = cursor.fetchone()
    if not row:
        safety_errors.append(f"Katha {kid} not found in database!")
        continue
    
    cur_audio = row[2]
    cur_video = row[3]
    
    if mtype == 'AUDIO' and cur_audio and cur_audio.strip():
        safety_errors.append(f"Katha {kid} already has existing audio: {cur_audio}")
        
    if mtype == 'VIDEO' and cur_video and cur_video.strip():
        safety_errors.append(f"Katha {kid} already has existing video: {cur_video}")
        
    # Check if URL is already used anywhere in database
    cursor.execute("SELECT id, title FROM content_items WHERE (audio_url=? OR video_url=?) AND id != ?;", (url, url, kid))
    conflict = cursor.fetchone()
    if conflict:
        safety_errors.append(f"URL {url} is already mapped to {conflict[0]} ({conflict[1]})!")

print(f"\nSafety Validation Errors: {len(safety_errors)}")
if safety_errors:
    for e in safety_errors:
        print("  ERROR:", e)
else:
    print("✓ All approved mappings passed Katha, URL, and conflict validation!")

for idx, m in enumerate(approved_mappings):
    print(f"\nApproved Mapping {idx+1}:")
    print(f"  Katha ID: {m['katha_id']}")
    print(f"  Title: {m['title']}")
    print(f"  Type: {m['type']}")
    print(f"  URL: {m['url']}")
    print(f"  Human Decision: {m['human_decision']}")

conn.close()
