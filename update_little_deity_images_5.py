import shutil, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

uploaded_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9\.user_uploaded')
gallery_dir = Path(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets\gallery')
gallery_dir.mkdir(exist_ok=True)

# 5 newest files uploaded in batch 5 (at 20:07:27)
files = [
    uploaded_dir / 'media_1788184898539.jpg',  # Image 1 = Little Devi Annapurna
    uploaded_dir / 'media_1788184918006.jpg',  # Image 2 = Little Devi Kamadhenu
    uploaded_dir / 'media_1788184941824.jpg',  # Image 3 = Little Bal Hayagriva
    uploaded_dir / 'media_1788184963982.jpg',  # Image 4 = Little Devi Gayatri
    uploaded_dir / 'media_1788184984162.jpg',  # Image 5 = Little Devi Ganga
]

mapping = {
    0: ('bal_annapurna_little.jpg', 'Little Devi Annapurna'),
    1: ('bal_kamadhenu_little.jpg', 'Little Devi Kamadhenu'),
    2: ('bal_hayagriva_little.jpg', 'Little Bal Hayagriva'),
    3: ('bal_gayatri_little.jpg',   'Little Devi Gayatri'),
    4: ('bal_ganga_little.jpg',     'Little Devi Ganga'),
}

print('=== 1. Copying Batch 5 Deity Images ===')
for i, f in enumerate(files):
    dest_name, label = mapping[i]
    dest = gallery_dir / dest_name
    shutil.copy2(f, dest)
    print(f'  Image {i+1} ({label}) -> assets/gallery/{dest_name} ({f.stat().st_size} bytes)')

# Update index.html
print('\n=== 2. Updating index.html ===')
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Ganga in Slide 2
old_slide2_bg = "url('assets/media_1787439357668.png');"
new_slide2_bg = "url('assets/gallery/bal_ganga_little.jpg');"
if old_slide2_bg in html:
    html = html.replace(old_slide2_bg, new_slide2_bg, 1)
    print('✓ Slide 2 background -> bal_ganga_little.jpg')

old_slide2_art = 'src="assets/media_1787439357668.png" class="slide-glow-artwork" alt="Ganga Maha Aarti"'
new_slide2_art = 'src="assets/gallery/bal_ganga_little.jpg" class="slide-glow-artwork" alt="Ganga Maha Aarti"'
if old_slide2_art in html:
    html = html.replace(old_slide2_art, new_slide2_art, 1)
    print('✓ Slide 2 artwork -> bal_ganga_little.jpg')

# Slide 4 background (currently deity_vishnu.jpg) -> bal_vishnu_little.jpg
old_slide4_bg = "url('assets/deity_vishnu.jpg');"
new_slide4_bg = "url('assets/gallery/bal_vishnu_little.jpg');"
if old_slide4_bg in html:
    html = html.replace(old_slide4_bg, new_slide4_bg, 1)
    print('✓ Slide 4 background -> bal_vishnu_little.jpg')

# Slide 5 background (currently deity_krishna.jpg) -> bal_chandra_little.jpg
old_slide5_bg = "url('assets/deity_krishna.jpg');"
new_slide5_bg = "url('assets/gallery/bal_chandra_little.jpg');"
if old_slide5_bg in html:
    html = html.replace(old_slide5_bg, new_slide5_bg, 1)
    print('✓ Slide 5 background -> bal_chandra_little.jpg')

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)

# Update app.js gallery dataset for all 25 Little Bal Deities
print('\n=== 3. Updating app.js Gallery Dataset ===')
with open('app.js', encoding='utf-8') as f:
    js = f.read()

gallery_replacements = [
    # Batch 1
    ("id: 'bal-ganesha',\n    nameHi: 'बाल गणेश',\n    nameEn: 'Little Bal Ganesha',\n    category: 'deva',\n    mantra: '॥ ॐ गं गणपतये नमः ॥',\n    img: 'assets/gallery/bal_ganesha.jpg'",
     "id: 'bal-ganesha',\n    nameHi: 'बाल गणेश',\n    nameEn: 'Little Bal Ganesha',\n    category: 'deva',\n    mantra: '॥ ॐ गं गणपतये नमः ॥',\n    img: 'assets/gallery/bal_ganesha_little.jpg'"),
    ("id: 'bal-rama',\n    nameHi: 'बाल राम',\n    nameEn: 'Little Bal Rama',\n    category: 'avatar',\n    mantra: '॥ श्री राम जय राम जय जय राम ॥',\n    img: 'assets/gallery/bal_rama.jpg'",
     "id: 'bal-rama',\n    nameHi: 'बाल राम',\n    nameEn: 'Little Bal Rama',\n    category: 'avatar',\n    mantra: '॥ श्री राम जय राम जय जय राम ॥',\n    img: 'assets/gallery/bal_rama_little.jpg'"),
    ("id: 'bal-lakshmi',\n    nameHi: 'बाल लक्ष्मी',\n    nameEn: 'Little Devi Lakshmi',\n    category: 'devi',\n    mantra: '॥ ॐ श्रीं ह्रीं क्लीं श्रीं नमः ॥',\n    img: 'assets/gallery/bal_lakshmi.jpg'",
     "id: 'bal-lakshmi',\n    nameHi: 'बाल लक्ष्मी',\n    nameEn: 'Little Devi Lakshmi',\n    category: 'devi',\n    mantra: '॥ ॐ श्रीं ह्रीं क्लीं श्रीं नमः ॥',\n    img: 'assets/gallery/bal_lakshmi_little.jpg'"),
    ("id: 'bal-saraswati',\n    nameHi: 'बाल सरस्वती',\n    nameEn: 'Little Devi Saraswati',\n    category: 'devi',\n    mantra: '॥ ॐ ऐं सरस्वत्यै नमः ॥',\n    img: 'assets/gallery/bal_saraswati.jpg'",
     "id: 'bal-saraswati',\n    nameHi: 'बाल सरस्वती',\n    nameEn: 'Little Devi Saraswati',\n    category: 'devi',\n    mantra: '॥ ॐ ऐं सरस्वत्यै नमः ॥',\n    img: 'assets/gallery/bal_saraswati_little.jpg'"),
    ("id: 'bal-durga',\n    nameHi: 'बाल दुर्गा',\n    nameEn: 'Little Devi Durga',\n    category: 'devi',\n    mantra: '॥ ॐ दुं दुर्गायै नमः ॥',\n    img: 'assets/gallery/bal_durga.jpg'",
     "id: 'bal-durga',\n    nameHi: 'बाल दुर्गा',\n    nameEn: 'Little Devi Durga',\n    category: 'devi',\n    mantra: '॥ ॐ दुं दुर्गायै नमः ॥',\n    img: 'assets/gallery/bal_durga_little.jpg'"),

    # Batch 2
    ("id: 'bal-kartikeya',\n    nameHi: 'बाल कार्तिकेय / मुरुगन',\n    nameEn: 'Little Bal Kartikeya / Murugan',\n    category: 'deva',\n    mantra: '॥ ॐ षण्मुखाय नमः ॥',\n    img: 'assets/deity_kartikeya.jpg'",
     "id: 'bal-kartikeya',\n    nameHi: 'बाल कार्तिकेय / मुरुगन',\n    nameEn: 'Little Bal Kartikeya / Murugan',\n    category: 'deva',\n    mantra: '॥ ॐ षण्मुखाय नमः ॥',\n    img: 'assets/gallery/bal_murugan_little.jpg'"),
    ("id: 'bal-vishnu',\n    nameHi: 'बाल विष्णु',\n    nameEn: 'Little Bal Vishnu',\n    category: 'avatar',\n    mantra: '॥ ॐ नमो नारायणाय ॥',\n    img: 'assets/deity_vishnu.jpg'",
     "id: 'bal-vishnu',\n    nameHi: 'बाल विष्णु',\n    nameEn: 'Little Bal Vishnu',\n    category: 'avatar',\n    mantra: '॥ ॐ नमो नारायणाय ॥',\n    img: 'assets/gallery/bal_vishnu_little.jpg'"),
    ("id: 'bal-indra',\n    nameHi: 'बाल इंद्र',\n    nameEn: 'Little Bal Indra',\n    category: 'vedic',\n    mantra: '॥ ॐ इन्द्राय नमः ॥',\n    img: 'assets/deity_indra.jpg'",
     "id: 'bal-indra',\n    nameHi: 'बाल इंद्र',\n    nameEn: 'Little Bal Indra',\n    category: 'vedic',\n    mantra: '॥ ॐ इन्द्राय नमः ॥',\n    img: 'assets/gallery/bal_indra_little.jpg'"),
    ("id: 'bal-parvati',\n    nameHi: 'बाल पार्वती',\n    nameEn: 'Little Devi Parvati',\n    category: 'devi',\n    mantra: '॥ ॐ शिवायै नमः ॥',\n    img: 'assets/deity_parvati.jpg'",
     "id: 'bal-parvati',\n    nameHi: 'बाल पार्वती',\n    nameEn: 'Little Devi Parvati',\n    category: 'devi',\n    mantra: '॥ ॐ शिवायै नमः ॥',\n    img: 'assets/gallery/bal_parvati_little.jpg'"),
    ("id: 'bal-agni',\n    nameHi: 'बाल अग्नि',\n    nameEn: 'Little Bal Agni',\n    category: 'vedic',\n    mantra: '॥ ॐ अग्नये नमः ॥',\n    img: 'assets/deity_agni.jpg'",
     "id: 'bal-agni',\n    nameHi: 'बाल अग्नि',\n    nameEn: 'Little Bal Agni',\n    category: 'vedic',\n    mantra: '॥ ॐ अग्नये नमः ॥',\n    img: 'assets/gallery/bal_agni_little.jpg'"),

    # Batch 3
    ("id: 'bal-vayu',\n    nameHi: 'बाल वायु',\n    nameEn: 'Little Bal Vayu',\n    category: 'vedic',\n    mantra: '॥ ॐ वायवे नमः ॥',\n    img: 'assets/deity_vayu.jpg'",
     "id: 'bal-vayu',\n    nameHi: 'बाल वायु',\n    nameEn: 'Little Bal Vayu',\n    category: 'vedic',\n    mantra: '॥ ॐ वायवे नमः ॥',\n    img: 'assets/gallery/bal_vayu_little.jpg'"),
    ("id: 'bal-varuna',\n    nameHi: 'बाल वरुण',\n    nameEn: 'Little Bal Varuna',\n    category: 'vedic',\n    mantra: '॥ ॐ वरुणाय नमः ॥',\n    img: 'assets/deity_varuna.jpg'",
     "id: 'bal-varuna',\n    nameHi: 'बाल वरुण',\n    nameEn: 'Little Bal Varuna',\n    category: 'vedic',\n    mantra: '॥ ॐ वरुणाय नमः ॥',\n    img: 'assets/gallery/bal_varuna_little.jpg'"),
    ("id: 'bal-surya',\n    nameHi: 'बाल सूर्य',\n    nameEn: 'Little Bal Surya',\n    category: 'navgraha',\n    mantra: '॥ ॐ सूर्याय नमः ॥',\n    img: 'assets/deity_surya.jpg'",
     "id: 'bal-surya',\n    nameHi: 'बाल सूर्य',\n    nameEn: 'Little Bal Surya',\n    category: 'navgraha',\n    mantra: '॥ ॐ सूर्याय नमः ॥',\n    img: 'assets/gallery/bal_surya_little.jpg'"),
    ("id: 'bal-chandra',\n    nameHi: 'बाल चंद्र',\n    nameEn: 'Little Devi Chandra',\n    category: 'navgraha',\n    mantra: '॥ ॐ सोमाय नमः ॥',\n    img: 'assets/deity_chandra.jpg'",
     "id: 'bal-chandra',\n    nameHi: 'बाल चंद्र',\n    nameEn: 'Little Devi Chandra',\n    category: 'navgraha',\n    mantra: '॥ ॐ सोमाय नमः ॥',\n    img: 'assets/gallery/bal_chandra_little.jpg'"),
    ("id: 'bal-kali',\n    nameHi: 'बाल काली',\n    nameEn: 'Little Devi Kali',\n    category: 'devi',\n    mantra: '॥ ॐ क्रीं कालिकायै नमः ॥',\n    img: 'assets/deity_kali.jpg'",
     "id: 'bal-kali',\n    nameHi: 'बाल काली',\n    nameEn: 'Little Devi Kali',\n    category: 'devi',\n    mantra: '॥ ॐ क्रीं कालिकायै नमः ॥',\n    img: 'assets/gallery/bal_kali_little.jpg'"),

    # Batch 4
    ("id: 'bal-brahma',\n    nameHi: 'बाल ब्रह्मा',\n    nameEn: 'Little Bal Brahma',\n    category: 'deva',\n    mantra: '॥ ॐ ब्रह्मणे नमः ॥',\n    img: 'assets/deity_brahma.jpg'",
     "id: 'bal-brahma',\n    nameHi: 'बाल ब्रह्मा',\n    nameEn: 'Little Bal Brahma',\n    category: 'deva',\n    mantra: '॥ ॐ ब्रह्मणे नमः ॥',\n    img: 'assets/gallery/bal_brahma_little.jpg'"),
    ("id: 'bal-narasimha',\n    nameHi: 'बाल नरसिंह',\n    nameEn: 'Little Bal Narasimha',\n    category: 'avatar',\n    mantra: '॥ ॐ नृसिंहाय नमः ॥',\n    img: 'assets/deity_narasimha.jpg'",
     "id: 'bal-narasimha',\n    nameHi: 'बाल नरसिंह',\n    nameEn: 'Little Bal Narasimha',\n    category: 'avatar',\n    mantra: '॥ ॐ नृसिंहाय नमः ॥',\n    img: 'assets/gallery/bal_narasimha_little.jpg'"),
    ("id: 'bal-radha',\n    nameHi: 'बाल राधा',\n    nameEn: 'Little Devi Radha',\n    category: 'devi',\n    mantra: '॥ ॐ राधायै नमः ॥',\n    img: 'assets/deity_radha.jpg'",
     "id: 'bal-radha',\n    nameHi: 'बाल राधा',\n    nameEn: 'Little Devi Radha',\n    category: 'devi',\n    mantra: '॥ ॐ राधायै नमः ॥',\n    img: 'assets/gallery/bal_radha_little.jpg'"),
    ("id: 'bal-balarama',\n    nameHi: 'बाल बलराम',\n    nameEn: 'Little Bal Balarama',\n    category: 'avatar',\n    mantra: '॥ ॐ बलरामाय नमः ॥',\n    img: 'assets/deity_balarama.jpg'",
     "id: 'bal-balarama',\n    nameHi: 'बाल बलराम',\n    nameEn: 'Little Bal Balarama',\n    category: 'avatar',\n    mantra: '॥ ॐ बलरामाय नमः ॥',\n    img: 'assets/gallery/bal_balarama_little.jpg'"),
    ("id: 'bal-kubera',\n    nameHi: 'बाल कुबेर',\n    nameEn: 'Little Bal Kubera',\n    category: 'deva',\n    mantra: '॥ ॐ यक्षाय कुबेराय नमः ॥',\n    img: 'assets/deity_kubera.jpg'",
     "id: 'bal-kubera',\n    nameHi: 'बाल कुबेर',\n    nameEn: 'Little Bal Kubera',\n    category: 'deva',\n    mantra: '॥ ॐ यक्षाय कुबेराय नमः ॥',\n    img: 'assets/gallery/bal_kubera_little.jpg'"),

    # Batch 5
    ("id: 'bal-annapurna',\n    nameHi: 'बाल अन्नपूर्णा',\n    nameEn: 'Little Devi Annapurna',\n    category: 'devi',\n    mantra: '॥ ॐ अन्नपूर्णायै नमः ॥',\n    img: 'assets/deity_annapurna.jpg'",
     "id: 'bal-annapurna',\n    nameHi: 'बाल अन्नपूर्णा',\n    nameEn: 'Little Devi Annapurna',\n    category: 'devi',\n    mantra: '॥ ॐ अन्नपूर्णायै नमः ॥',\n    img: 'assets/gallery/bal_annapurna_little.jpg'"),
    ("id: 'bal-kamadhenu',\n    nameHi: 'बाल कामधेनु',\n    nameEn: 'Little Devi Kamadhenu',\n    category: 'vedic',\n    mantra: '॥ ॐ सुरभ्यै नमः ॥',\n    img: 'assets/deity_kamadhenu.jpg'",
     "id: 'bal-kamadhenu',\n    nameHi: 'बाल कामधेनु',\n    nameEn: 'Little Devi Kamadhenu',\n    category: 'vedic',\n    mantra: '॥ ॐ सुरभ्यै नमः ॥',\n    img: 'assets/gallery/bal_kamadhenu_little.jpg'"),
    ("id: 'bal-hayagriva',\n    nameHi: 'बाल हयग्रीव',\n    nameEn: 'Little Bal Hayagriva',\n    category: 'avatar',\n    mantra: '॥ ॐ हयग्रीवाय नमः ॥',\n    img: 'assets/deity_hayagriva.jpg'",
     "id: 'bal-hayagriva',\n    nameHi: 'बाल हयग्रीव',\n    nameEn: 'Little Bal Hayagriva',\n    category: 'avatar',\n    mantra: '॥ ॐ हयग्रीवाय नमः ॥',\n    img: 'assets/gallery/bal_hayagriva_little.jpg'"),
    ("id: 'bal-gayatri',\n    nameHi: 'बाल गायत्री',\n    nameEn: 'Little Devi Gayatri',\n    category: 'devi',\n    mantra: '॥ ॐ भूर्भुवः स्वः ॥',\n    img: 'assets/deity_gayatri.jpg'",
     "id: 'bal-gayatri',\n    nameHi: 'बाल गायत्री',\n    nameEn: 'Little Devi Gayatri',\n    category: 'devi',\n    mantra: '॥ ॐ भूर्भुवः स्वः ॥',\n    img: 'assets/gallery/bal_gayatri_little.jpg'"),
    ("id: 'bal-ganga',\n    nameHi: 'बाल गंगा',\n    nameEn: 'Little Devi Ganga',\n    category: 'river',\n    mantra: '॥ ॐ गंगायै नमः ॥',\n    img: 'assets/deity_ganga.jpg'",
     "id: 'bal-ganga',\n    nameHi: 'बाल गंगा',\n    nameEn: 'Little Devi Ganga',\n    category: 'river',\n    mantra: '॥ ॐ गंगायै नमः ॥',\n    img: 'assets/gallery/bal_ganga_little.jpg'"),
]

applied_count = 0
for old, new in gallery_replacements:
    # Normalize newlines for match
    old_c = old.replace('\r\n', '\n')
    js_c = js.replace('\r\n', '\n')
    if old_c in js_c:
        js = js_c.replace(old_c, new.replace('\r\n', '\n'), 1)
        applied_count += 1
        print(f"✓ Gallery mapping updated: {new.splitlines()[0]}")
    else:
        print(f"✗ Not matched: {old.splitlines()[0]}")

with open('app.js', 'w', encoding='utf-8', newline='') as f:
    f.write(js)

print(f'\nTotal gallery dataset mappings updated: {applied_count}/25')
