import json, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

m = re.search(r'window\.DIVINE_AARTI_DATASET\s*=\s*(\[.*?\]);', js, re.DOTALL)
if not m:
    print("DIVINE_AARTI_DATASET not found!")
    sys.exit(1)

items = json.loads(m.group(1))
print(f"Total items in DIVINE_AARTI_DATASET: {len(items)}\n")

for i, item in enumerate(items):
    aid = item.get('id')
    title = item.get('title')
    deity = item.get('deity')
    audio = item.get('audio')
    thumb = item.get('thumb')
    
    is_yt = 'youtube' in audio or 'youtu.be' in audio
    is_local = audio.startswith('assets/')
    local_exists = os.path.exists(audio) if is_local else None
    
    print(f"{i+1:2d}. [{deity}] {title}")
    print(f"    Audio: {audio} (Type: {'YouTube' if is_yt else 'Local' if is_local else 'Other'}, Exists: {local_exists})")
    print(f"    Thumb: {thumb} (Exists: {os.path.exists(thumb)})")
