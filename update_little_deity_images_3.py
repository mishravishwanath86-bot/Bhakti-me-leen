import shutil, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

uploaded_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9\.user_uploaded')
gallery_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets\gallery')
gallery_dir.mkdir(exist_ok=True)

# Get the 5 newest files uploaded in this batch
new_files = sorted(
    [f for f in uploaded_dir.glob('media_17881835[4-9]*.jpg')],
    key=lambda f: f.stat().st_mtime
)
print('Files in upload order (1=Vayu, 2=Varuna, 3=Surya, 4=Chandra, 5=Kali):')
for i, f in enumerate(new_files, 1):
    print(f'  Image {i}: {f.name} ({f.stat().st_size} bytes)')

# User mapping:
# 1 = Little Bal Vayu
# 2 = Little Bal Varuna
# 3 = Little Bal Surya
# 4 = Little Devi Chandra
# 5 = Little Devi Kali
mapping = {
    1: ('bal_vayu_little.jpg',   'Little Bal Vayu'),
    2: ('bal_varuna_little.jpg', 'Little Bal Varuna'),
    3: ('bal_surya_little.jpg',  'Little Bal Surya'),
    4: ('bal_chandra_little.jpg','Little Devi Chandra'),
    5: ('bal_kali_little.jpg',   'Little Devi Kali'),
}

print()
for i, f in enumerate(new_files[:5], 1):
    dest_name, label = mapping[i]
    dest = gallery_dir / dest_name
    shutil.copy2(f, dest)
    print(f'Copied Image {i} ({label}) -> assets/gallery/{dest_name}')

# Now update index.html
print('\n=== Updating index.html ===')
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Strategic placements:
# Surya -> replace deity_surya anywhere + slide hero Krishna (slide 2 is Krishna)
# Kali  -> replace deity_kali
# Vayu  -> replace deity_hanuman cat-icon (चालीसा) — Vayu = Hanuman's father, fitting
# Varuna -> replace deity_ramayana cat-icon — water/ocean theme
# Chandra -> replace deity_krishna in category icon (भजन) — moon/night devotional

replacements = [
    # Vayu -> चालीसा category icon (Vayu=Hanuman's father, devotional context)
    ('assets/deity_hanuman.jpg" class="cat-icon-img" alt="चालीसा"',
     'assets/gallery/bal_vayu_little.jpg" class="cat-icon-img" alt="चालीसा"'),

    # Varuna -> रामायण category icon (water/ocean theme - समुद्र crossing, पावन)
    ('assets/deity_ramayana.jpg" class="cat-icon-img" alt="रामायण"',
     'assets/gallery/bal_varuna_little.jpg" class="cat-icon-img" alt="रामायण"'),

    # Surya -> deity_surya in hero slides area and surya existing refs
    ('assets/deity_surya.jpg"',
     'assets/gallery/bal_surya_little.jpg"'),

    # Chandra -> replace Krishna cat-icon (भजन) - चंद्र = रात्रि भजन theme
    ('assets/deity_krishna.jpg" class="cat-icon-img" alt="भजन"',
     'assets/gallery/bal_chandra_little.jpg" class="cat-icon-img" alt="भजन"'),

    # Kali -> replace deity_kali wherever referenced
    ('assets/deity_kali.jpg"',
     'assets/gallery/bal_kali_little.jpg"'),

    # Surya slide hero (Krishna slide is index 1, Surya could replace slide if exists)
    ('assets/deity_krishna.jpg" class="slide-glow-artwork" alt="Shri Krishna"',
     'assets/gallery/bal_chandra_little.jpg" class="slide-glow-artwork" alt="चंद्र देव"'),

    # Reader deity central image -> Surya (morning puja / reader context)
    ('assets/deity_hanuman.jpg" class="deity-central-img" id="reader-deity-img"',
     'assets/gallery/bal_surya_little.jpg" class="deity-central-img" id="reader-deity-img"'),
]

changed = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        changed += 1
        print(f'✓ {old[:60]}')
    else:
        print(f'✗ NOT FOUND: {old[:60]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nTotal: {changed} replacements made.\n')

# Final verification
print('=== Verification ===')
with open('index.html', encoding='utf-8') as f:
    html2 = f.read()

all_little = [
    'bal_ganesha_little','bal_rama_little','bal_lakshmi_little',
    'bal_saraswati_little','bal_durga_little',
    'bal_vishnu_little','bal_murugan_little','bal_indra_little',
    'bal_parvati_little','bal_agni_little',
    'bal_vayu_little','bal_varuna_little','bal_surya_little',
    'bal_chandra_little','bal_kali_little'
]
print(f'\n{"Deity Image":<30} {"Count":>5}  Status')
print('-' * 45)
for name in all_little:
    cnt = html2.count(name)
    status = '✅' if cnt > 0 else '⚠️ MISSING'
    print(f'{name:<30} {cnt:>5}  {status}')
