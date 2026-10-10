import json, sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_all_chalisa_items import parsed_items
from build_chalisa_config import DEITY_CONFIG

mapping = {
    'hanuman': [1, 2, 18],
    'ganesh': [3],
    'shiva': [4],
    'shani': [5, 6],
    'krishna': [7, 8, 19],
    'rama': [9, 17, 20],
    'surya': [10, 15],
    'vishnu': [11, 12, 22],
    'bhairav': [13, 14],
    'durga': [23, 32, 43],
    'gayatri': [24, 30],
    'lakshmi': [25, 26],
    'ganga': [27, 41],
    'saraswati': [28, 42],
    'radha': [35],
    'devi': [29, 31, 33, 34, 36, 37, 38, 39, 40],
    'khatushyam': [50],
    'sants': [16, 21, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54]
}

# Image lookup helper
def get_item_thumb(item):
    t = item['title']
    if 'हनुमान' in t or 'बजरंग' in t or 'बालाजी' in t: return 'assets/gallery/bal_hanuman.jpg'
    if 'गणेश' in t: return 'assets/gallery/bal_ganesha_little.jpg'
    if 'शिव' in t: return 'assets/gallery/bal_shiva.jpg'
    if 'शनि' in t: return 'assets/deity_shanidev.jpg'
    if 'कृष्ण' in t or 'गोपाल' in t or 'गिरिराज' in t: return 'assets/gallery/bal_krishna.jpg'
    if 'राम' in t or 'परशुराम' in t: return 'assets/gallery/bal_rama_little.jpg'
    if 'सूर्य' in t or 'नवग्रह' in t: return 'assets/gallery/bal_surya_little.jpg'
    if 'विष्णु' in t: return 'assets/gallery/bal_vishnu_little.jpg'
    if 'ब्रह्मा' in t: return 'assets/gallery/bal_brahma_little.jpg'
    if 'नृसिंह' in t: return 'assets/gallery/bal_narasimha_little.jpg'
    if 'भैरव' in t: return 'assets/gallery/bal_bhairav_little.jpg'
    if 'दुर्गा' in t or 'विन्ध्येश्वरी' in t or 'शाकम्भरी' in t: return 'assets/gallery/bal_durga_little.jpg'
    if 'गायत्री' in t: return 'assets/gallery/bal_gayatri_little.jpg'
    if 'तुलसी' in t: return 'assets/gallery/bal_tulsi_little.jpg'
    if 'लक्ष्मी' in t: return 'assets/gallery/bal_lakshmi_little.jpg'
    if 'गंगा' in t or 'नर्मदा' in t: return 'assets/gallery/bal_ganga_little.jpg'
    if 'सरस्वती' in t or 'शारदा' in t: return 'assets/gallery/bal_saraswati_little.jpg'
    if 'राधा' in t: return 'assets/gallery/bal_radha_little.jpg'
    if 'पार्वती' in t: return 'assets/gallery/bal_parvati_little.jpg'
    if 'काली' in t: return 'assets/gallery/bal_kali_little.jpg'
    if 'शीतला' in t: return 'assets/gallery/bal_shitala_little.jpg'
    if 'अन्नपूर्णा' in t: return 'assets/gallery/bal_annapurna_little.jpg'
    if 'श्याम' in t: return 'assets/deity_khatushyam.jpg'
    if 'कुबेर' in t: return 'assets/gallery/bal_kubera_little.jpg'
    if 'साई' in t: return 'assets/deity_saibaba.jpg'
    if 'विश्वकर्मा' in t: return 'assets/deity_vishwakarma.jpg'
    if 'गीता' in t: return 'assets/gallery/bal_krishna.jpg'
    return 'assets/gallery/bal_agni_little.jpg'

final_chalisa_collections = {}

for cat_key, nums in mapping.items():
    cfg = DEITY_CONFIG[cat_key]
    items = []
    for n in nums:
        it = parsed_items[n-1]
        thumb = get_item_thumb(it)
        items.append({
            'id': it['id'],
            'title': it['title'],
            'en_line': it['en_line'],
            'hi_line': it['hi_line'],
            'sub': f"{it['hi_line']} • Drik Panchang Verified",
            'thumb': thumb,
            'audio_url': it['audio_url'],
            'video_id': it['video_id'],
            'drik_url': it['drik_url'],
            'source': 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)',
            'content': it['content'],
            'meaning': f"॥ {it['title']} — सम्पूर्ण पावन पाठ व भावार्थ ॥\n\nद्रिक पञ्चाङ्ग द्वारा प्रमाणित यह पवित्र चालीसा भक्तिपूर्वक पाठ करने से अभीष्ट फल की प्राप्ति होती है और समस्त संतापों का नाश होता है।",
            'deity': cfg['deity'],
            'section': it['section']
        })
    
    final_chalisa_collections[cat_key] = {
        'key': cat_key,
        'title': cfg['title'],
        'title_en': cfg['title_en'],
        'deity': cfg['deity'],
        'img': cfg['img'],
        'fallbackImg': cfg['fallbackImg'],
        'mantra': cfg['mantra'],
        'sub': cfg['sub'],
        'items': items
    }

with open('drik_chalisa_collections.json', 'w', encoding='utf-8') as f:
    json.dump(final_chalisa_collections, f, ensure_ascii=False, indent=2)

print("Saved drik_chalisa_collections.json successfully!")
print("Total collection points:", len(final_chalisa_collections))
total_chalisas = sum(len(c['items']) for c in final_chalisa_collections.values())
print("Total Chalisas:", total_chalisas)
