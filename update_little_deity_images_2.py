import shutil, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

uploaded_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9\.user_uploaded')
assets_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets')
gallery_dir = assets_dir / 'gallery'
gallery_dir.mkdir(exist_ok=True)

# Newest 5 files (uploaded this session) in ascending upload order
new_files = sorted(
    [f for f in uploaded_dir.glob('media_178818[34]*.jpg') if f.stat().st_mtime > 1788183200],
    key=lambda f: f.stat().st_mtime
)
print('Files in upload order (1=Vishnu, 2=Murugan, 3=Indra, 4=Parvati, 5=Agni):')
for i, f in enumerate(new_files, 1):
    print(f'  Image {i}: {f.name} ({f.stat().st_size} bytes)')

# User's mapping:
# 1 = Little Bal Vishnu
# 2 = Little Bal Murugan / Kartikeya
# 3 = Little Bal Indra
# 4 = Little Devi Parvati
# 5 = Little Bal Agni
mapping = {
    1: ('bal_vishnu_little.jpg',   'Little Bal Vishnu'),
    2: ('bal_murugan_little.jpg',  'Little Bal Murugan/Kartikeya'),
    3: ('bal_indra_little.jpg',    'Little Bal Indra'),
    4: ('bal_parvati_little.jpg',  'Little Devi Parvati'),
    5: ('bal_agni_little.jpg',     'Little Bal Agni'),
}

print()
for i, f in enumerate(new_files[:5], 1):
    dest_name, label = mapping[i]
    dest = gallery_dir / dest_name
    shutil.copy2(f, dest)
    print(f'Copied Image {i} ({label}) -> assets/gallery/{dest_name}')

print('\nDone! All 5 little deity images copied to assets/gallery/')

# Now update index.html: replace these deities' existing images in coverflow
# Existing:
#   deity_vishnu.jpg  -> bal_vishnu_little.jpg
#   deity_hanuman.jpg (used as Kartikeya proxy is not great, let's find where Vishnu/Hanuman/Indra appear)
# Let's check what's currently in the coverflow for vishnu & hanuman
with open('index.html', encoding='utf-8') as f:
    html = f.read()

lines = html.split('\n')
print('\n=== Current coverflow deity image references ===')
for i, line in enumerate(lines, 1):
    if ('coverflow' in line or 'cat-icon' in line or 'deity_vishnu' in line or 'deity_hanuman' in line) and 'img' in line.lower():
        print(f'Line {i}: {line.strip()[:120]}')
