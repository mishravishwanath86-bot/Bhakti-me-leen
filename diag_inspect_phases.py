import json, sys

sys.stdout.reconfigure(encoding='utf-8')

phases = {
    'Phase 2N': 'bulk_import/audits/audio_video_katha_phase2n_e_apply.json',
    'Phase 2O': 'bulk_import/audits/audio_video_katha_phase2o_e_apply.json',
    'Phase 2P': 'bulk_import/audits/audio_video_katha_phase2p_e_apply.json',
    'Phase 2Q': 'bulk_import/audits/audio_video_katha_phase2q_e_apply.json'
}

for pname, pfile in phases.items():
    with open(pfile, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n================ {pname} ================")
    print("Keys:", list(data.keys()) if isinstance(data, dict) else f"List with {len(data)} items")
    items = data if isinstance(data, list) else data.get('applied_records', data.get('applied_items', data.get('mappings', [])))
    print(f"Total Applied Count: {len(items)}")
    
    # Sample items
    yt_count = 0
    mp3_count = 0
    sample_urls = []
    for it in items:
        url = it.get('audio_url', it.get('media_url', it.get('video_url', '')))
        if 'youtube' in url or 'youtu.be' in url:
            yt_count += 1
        elif '.mp3' in url:
            mp3_count += 1
        if len(sample_urls) < 3:
            sample_urls.append((it.get('id', it.get('content_id')), it.get('title'), url))
            
    print(f"YouTube items: {yt_count}, MP3 items: {mp3_count}")
    print("Sample items:")
    for s in sample_urls:
        print(f"  - ID: {s[0]} | Title: {s[1]} | URL: {s[2]}")
