import shutil, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

uploaded_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9\.user_uploaded')
gallery_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets\gallery')
gallery_dir.mkdir(exist_ok=True)

# 5 newest files in ascending upload order (by filename/timestamp)
files = [
    uploaded_dir / 'media_1788184299297.jpg',  # Image 1 = Little Bal Brahma
    uploaded_dir / 'media_1788184328232.jpg',  # Image 2 = Little Bal Narasimha
    uploaded_dir / 'media_1788184351660.jpg',  # Image 3 = Little Devi Radha
    uploaded_dir / 'media_1788184374964.jpg',  # Image 4 = Little Bal Balarama
    uploaded_dir / 'media_1788184397311.jpg',  # Image 5 = Little Bal Kubera
]

mapping = {
    0: ('bal_brahma_little.jpg',   'Little Bal Brahma'),
    1: ('bal_narasimha_little.jpg','Little Bal Narasimha'),
    2: ('bal_radha_little.jpg',    'Little Devi Radha'),
    3: ('bal_balarama_little.jpg', 'Little Bal Balarama'),
    4: ('bal_kubera_little.jpg',   'Little Bal Kubera'),
}

print('Copying images...')
for i, f in enumerate(files):
    dest_name, label = mapping[i]
    dest = gallery_dir / dest_name
    shutil.copy2(f, dest)
    print(f'  Image {i+1} ({label}) -> assets/gallery/{dest_name}  ({f.stat().st_size}b)')

# Now update index.html
print('\n=== Updating index.html ===')
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Find what slides/slots are still available
# Already used slides: 1=Mix Gods, 2=Ganga, 3=Kali, 4=Vishnu, 5=Chandra
# Let's check remaining hero slides
lines = html.split('\n')
print('\nAvailable hero slides:')
for i, line in enumerate(lines, 1):
    if 'slide-glow-artwork' in line:
        print(f'  Line {i}: {line.strip()[:100]}')

# Check aarti section cards (Hanuman aarti card has bal_hanuman.jpg)
print('\nAarti section cards:')
for i, line in enumerate(lines, 1):
    if 'onclick="window.openAartiCollectionModal' in line or ('aarti' in line.lower() and 'card' in line.lower() and 'onclick' in line.lower()):
        print(f'  Line {i}: {line.strip()[:100]}')

# Strategic placements:
# Brahma    -> replace deity_radha_krishna in slide/reward/wherever (Brahma = creator deity)
# Narasimha -> replace deity_narasimha / deity_narsingh if present
# Radha     -> replace bal_radha_krishna.jpg or deity_radha_krishna
# Balarama  -> new reference in Aarti section (Balarama = Krishna's brother)
# Kubera    -> reward section (Kubera = wealth god, perfect for divine rewards)

replacements = [
    # Brahma -> replace first slide (Mix Gods slide has media_png, use for Brahma)
    # Actually let's replace deity_radha_krishna with Radha little
    ('assets/deity_radha_krishna.jpg"',
     'assets/gallery/bal_radha_little.jpg"'),

    # Narasimha -> deity_narasimha or narsingh
    ('assets/deity_narasimha.jpg"',
     'assets/gallery/bal_narasimha_little.jpg"'),
    ('assets/deity_narsingh.jpg"',
     'assets/gallery/bal_narasimha_little.jpg"'),

    # Kubera -> reward wallpaper section (perfect — Kubera = wealth, divine rewards)
    ('assets/gallery/bal_ganesha_little.jpg" id="glass-modal-img"',
     'assets/gallery/bal_kubera_little.jpg" id="glass-modal-img"'),

    # Reward wallpaper img
    ('assets/gallery/bal_ganesha_little.jpg" alt="4K Wallpaper"',
     'assets/gallery/bal_kubera_little.jpg" alt="4K Wallpaper"'),

    # Reward download btn
    ('assets/gallery/bal_ganesha_little.jpg" download="Bhakti_Divine_4K_Wallpaper.jpg"',
     'assets/gallery/bal_kubera_little.jpg" download="Bhakti_Divine_4K_Wallpaper.jpg"'),

    # Hanuman aarti card -> Balarama (in Aarti section, Balarama fits devotional)
    ('assets/gallery/bal_hanuman.jpg" onerror="this.src=\'assets/deity_hanuman.jpg\'',
     'assets/gallery/bal_balarama_little.jpg" onerror="this.src=\'assets/deity_hanuman.jpg\''),
]

changed = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        changed += 1
        print(f'✓ {old[:65]}')
    else:
        print(f'✗ NOT FOUND: {old[:65]}')

# Now inject Brahma into a hero slide by replacing the Ganga slide (slide 2)
# Ganga slide uses media_1787439357668.png - let's replace slide 4 (Vishnu) with Brahma
# Actually, add Brahma to the onboarding slide that uses Vishnu's position
# Better: use Brahma as the slide 1 background
old_slide1_bg = "url('assets/media_1787439477306.png');"
new_slide1_bg = "url('assets/gallery/bal_brahma_little.jpg');"
if old_slide1_bg in html:
    html = html.replace(old_slide1_bg, new_slide1_bg, 1)
    changed += 1
    print('✓ Brahma added to Slide 1 background')

# Also add Brahma as slide 1 artwork
old_slide1_art = 'assets/media_1787439477306.png" class="slide-glow-artwork"'
new_slide1_art = 'assets/gallery/bal_brahma_little.jpg" class="slide-glow-artwork"'
if old_slide1_art in html:
    html = html.replace(old_slide1_art, new_slide1_art, 1)
    changed += 1
    print('✓ Brahma added to Slide 1 artwork')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nTotal: {changed} replacements made.\n')

# Full verification — all 20 little images
print('=== COMPLETE VERIFICATION (All 20 Little Deity Images) ===')
with open('index.html', encoding='utf-8') as f:
    html2 = f.read()

all_little = [
    # Batch 1
    'bal_ganesha_little', 'bal_rama_little', 'bal_lakshmi_little',
    'bal_saraswati_little', 'bal_durga_little',
    # Batch 2
    'bal_vishnu_little', 'bal_murugan_little', 'bal_indra_little',
    'bal_parvati_little', 'bal_agni_little',
    # Batch 3
    'bal_vayu_little', 'bal_varuna_little', 'bal_surya_little',
    'bal_chandra_little', 'bal_kali_little',
    # Batch 4 (new)
    'bal_brahma_little', 'bal_narasimha_little', 'bal_radha_little',
    'bal_balarama_little', 'bal_kubera_little',
]

ok = 0
for name in all_little:
    cnt = html2.count(name)
    status = 'OK' if cnt > 0 else 'MISSING'
    if cnt > 0:
        ok += 1
    print(name + ': ' + str(cnt) + ' [' + status + ']')

print('\nSCORE: ' + str(ok) + '/20 little deity images active in app')
