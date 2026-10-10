import json, sys

sys.stdout.reconfigure(encoding='utf-8')

for pfile in [
    'bulk_import/audits/audio_video_katha_phase2n_e_apply.json',
    'bulk_import/audits/audio_video_katha_phase2o_e_apply.json',
    'bulk_import/audits/audio_video_katha_phase2p_e_apply.json',
    'bulk_import/audits/audio_video_katha_phase2q_e_apply.json'
]:
    with open(pfile, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\nFile: {pfile}")
    for k, v in data.items():
        if isinstance(v, list) and len(v) > 0:
            print(f"  Key '{k}' has {len(v)} items. Sample item: {v[0]}")
        elif isinstance(v, dict):
            print(f"  Key '{k}' is dict with keys: {list(v.keys())[:5]}")
        elif isinstance(v, (int, str, bool)):
            print(f"  Key '{k}': {v}")
