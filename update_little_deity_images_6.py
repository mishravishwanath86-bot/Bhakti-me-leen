import shutil, sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

uploaded_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9\.user_uploaded')
gallery_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets\gallery')
gallery_dir.mkdir(exist_ok=True)

files = [
    (uploaded_dir / 'media_1788187133951.jpg', 'bal_yamuna_little.jpg', 'Little Devi Yamuna'),
    (uploaded_dir / 'media_1788187175039.jpg', 'bal_shakti_little.jpg', 'Little Devi Shakti'),
]

print('=== 1. Copying Batch 6 Deity Images ===')
for src, dest_name, label in files:
    dest = gallery_dir / dest_name
    shutil.copy2(src, dest)
    print(f'  {label} -> assets/gallery/{dest_name} ({dest.stat().st_size} bytes)')

print('\n=== 2. Updating app.js Gallery Dataset ===')
with open('app.js', encoding='utf-8') as f:
    js = f.read()

deity_map = {
    'bal-yamuna': 'assets/gallery/bal_yamuna_little.jpg',
    'bal-shakti': 'assets/gallery/bal_shakti_little.jpg',
}

def update_bal_entry(match):
    full_block = match.group(0)
    item_id = match.group(1)
    if item_id in deity_map:
        target_img = deity_map[item_id]
        updated_block = re.sub(r"(img:\s*')[^']+'", r"\g<1>" + target_img + "'", full_block)
        print(f'✓ Updated {item_id} -> {target_img}')
        return updated_block
    return full_block

js_updated = re.sub(r"\{\s*id:\s*'(bal-[a-z0-9_-]+)'[\s\S]*?fallbackImg:[^\}]+\}", update_bal_entry, js)

with open('app.js', 'w', encoding='utf-8', newline='') as f:
    f.write(js_updated)

print('\n=== 3. Verifying all bal- items in app.js ===')
pattern = re.compile(r"id:\s*'(bal-[a-z0-9_-]+)'[\s\S]*?nameHi:\s*'([^']+)'[\s\S]*?nameEn:\s*'([^']+)'[\s\S]*?img:\s*'([^']+)'")
matches = pattern.findall(js_updated)
little_count = sum(1 for m in matches if '_little.jpg' in m[3])
print(f'Total Little Deity images active in app.js gallery: {little_count}/60')

for item_id, name_hi, name_en, img in matches:
    if '_little.jpg' in img:
        print(f'  ✅ {item_id:20} | {name_hi:15} | {img}')
