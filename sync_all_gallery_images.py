import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', encoding='utf-8') as f:
    js = f.read()

# Dictionary of bal deity ID -> target little image path
deity_image_map = {
    'bal-ganesha': 'assets/gallery/bal_ganesha_little.jpg',
    'bal-rama': 'assets/gallery/bal_rama_little.jpg',
    'bal-lakshmi': 'assets/gallery/bal_lakshmi_little.jpg',
    'bal-saraswati': 'assets/gallery/bal_saraswati_little.jpg',
    'bal-durga': 'assets/gallery/bal_durga_little.jpg',
    'bal-kartikeya': 'assets/gallery/bal_murugan_little.jpg',
    'bal-vishnu': 'assets/gallery/bal_vishnu_little.jpg',
    'bal-indra': 'assets/gallery/bal_indra_little.jpg',
    'bal-parvati': 'assets/gallery/bal_parvati_little.jpg',
    'bal-agni': 'assets/gallery/bal_agni_little.jpg',
    'bal-vayu': 'assets/gallery/bal_vayu_little.jpg',
    'bal-varuna': 'assets/gallery/bal_varuna_little.jpg',
    'bal-surya': 'assets/gallery/bal_surya_little.jpg',
    'bal-chandra': 'assets/gallery/bal_chandra_little.jpg',
    'bal-kali': 'assets/gallery/bal_kali_little.jpg',
    'bal-brahma': 'assets/gallery/bal_brahma_little.jpg',
    'bal-narasimha': 'assets/gallery/bal_narasimha_little.jpg',
    'bal-radha': 'assets/gallery/bal_radha_little.jpg',
    'bal-balarama': 'assets/gallery/bal_balarama_little.jpg',
    'bal-kubera': 'assets/gallery/bal_kubera_little.jpg',
    'bal-annapurna': 'assets/gallery/bal_annapurna_little.jpg',
    'bal-kamadhenu': 'assets/gallery/bal_kamadhenu_little.jpg',
    'bal-hayagriva': 'assets/gallery/bal_hayagriva_little.jpg',
    'bal-gayatri': 'assets/gallery/bal_gayatri_little.jpg',
    'bal-ganga': 'assets/gallery/bal_ganga_little.jpg',
}

def update_bal_entry(match):
    full_block = match.group(0)
    item_id = match.group(1)
    if item_id in deity_image_map:
        target_img = deity_image_map[item_id]
        # Replace the img field within this block
        updated_block = re.sub(r"(img:\s*')[^']+'", r"\g<1>" + target_img + "'", full_block)
        return updated_block
    return full_block

# Match individual object inside array
js_updated = re.sub(r"\{\s*id:\s*'(bal-[a-z0-9_-]+)'[\s\S]*?fallbackImg:[^\}]+\}", update_bal_entry, js)

with open('app.js', 'w', encoding='utf-8', newline='') as f:
    f.write(js_updated)

print("Updated app.js with regex-based precise mapping.")
