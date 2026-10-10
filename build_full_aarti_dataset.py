import json, sqlite3, sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load parsed DrikPanchang data
with open('drik_aarti_parsed.json', 'r', encoding='utf-8') as f:
    drik_categories = json.load(f)

# 2. Connect to SQLite to search existing database for lyrics
conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()
cur.execute("SELECT id, title, content, audio_url FROM content_items")
db_items = cur.fetchall()
conn.close()

def find_lyrics(hi_line, en_title, en_line):
    # Normalized search
    clean_hi = re.sub(r'[\s\W_]+', '', hi_line.lower())
    for r in db_items:
        db_title = r[1]
        db_content = r[2]
        if not db_content: continue
        clean_db_title = re.sub(r'[\s\W_]+', '', db_title.lower())
        clean_db_content = re.sub(r'[\s\W_]+', '', db_content[:200].lower())
        
        # Check title overlap
        if len(clean_hi) > 4 and (clean_hi[:8] in clean_db_title or clean_hi[:8] in clean_db_content):
            return db_content, (r[3] if r[3] else None)
    return None, None

# Mapping category names to canonical keys & images
CATEGORY_CONFIG = {
    "Ganesha Aarti": {
        "key": "ganesh",
        "title_hi": "श्री गणेश आरती संग्रह",
        "title_en": "Ganesha Aarti",
        "deity": "श्री गणेश जी महाराज",
        "img": "assets/gallery/bal_ganesha_little.jpg",
        "fallback": "assets/deity_ganesh.jpg",
        "mantra": "॥ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ॥",
        "sub": "जय गणेश • विनायक • गणपति सेवा",
        "audio": "https://www.youtube.com/watch?v=0h3jKq3Lp7k"
    },
    "Hanuman Aarti": {
        "key": "hanuman",
        "title_hi": "श्री हनुमान आरती संग्रह",
        "title_en": "Hanuman Aarti",
        "deity": "श्री हनुमान जी महाराज",
        "img": "assets/gallery/bal_hanuman.jpg",
        "fallback": "assets/deity_hanuman.jpg",
        "mantra": "॥ अतुलितबलधामं हेमशैलाभदेहम् ॥",
        "sub": "हनुमान लला • बालाजी • पवनसुत",
        "audio": "https://www.youtube.com/watch?v=AETFv444yoE"
    },
    "Krishna Aarti": {
        "key": "krishna",
        "title_hi": "श्री कृष्ण आरती संग्रह",
        "title_en": "Krishna Aarti",
        "deity": "भगवान श्री कृष्ण",
        "img": "assets/gallery/bal_krishna_little.jpg",
        "fallback": "assets/deity_krishna.jpg",
        "mantra": "॥ कृं कृष्णाय नमः • ॐ नमो भगवते वासुदेवाय ॥",
        "sub": "कुंजबिहारी • बांके बिहारी • गोपाल • नटवर",
        "audio": "https://www.youtube.com/watch?v=Y75n9z58U9c"
    },
    "Rama Aarti": {
        "key": "rama",
        "title_hi": "श्री राम आरती संग्रह",
        "title_en": "Rama Aarti",
        "deity": "मर्यादा पुरुषोत्तम श्री रामचंद्र",
        "img": "assets/gallery/bal_rama.jpg",
        "fallback": "assets/deity_ram.jpg",
        "mantra": "॥ श्री रामचन्द्राय नमः • रामाय नमः ॥",
        "sub": "कृपालु भजु मन • रघुवर • सीता-राम • जानकीनाथ",
        "audio": "assets/audio/katha_ramayana.mp3"
    },
    "Shiva Aarti": {
        "key": "shiva",
        "title_hi": "भगवान शिव आरती संग्रह",
        "title_en": "Shiva Aarti",
        "deity": "देवाधिदेव महादेव शिव शंकर",
        "img": "assets/gallery/divya_shiva.jpg",
        "fallback": "assets/deity_shiv.jpg",
        "mantra": "॥ ॐ नमः शिवाय • कर्पूरगौरं करुणावतारम् ॥",
        "sub": "शिव ओंकारा • हर हर महादेव • गंगाधर",
        "audio": "https://www.youtube.com/watch?v=0wQ75mJ1a1k"
    },
    "Narayana Aarti": {
        "key": "narayana",
        "title_hi": "श्री नारायण व विष्णु आरती",
        "title_en": "Narayana Aarti",
        "deity": "भगवान श्री हरि विष्णु",
        "img": "assets/gallery/vishnu_sheshnaag.jpg",
        "fallback": "assets/deity_vishnu.jpg",
        "mantra": "॥ ॐ नमो नारायणाय • शान्ताकारं भुजगशयनम् ॥",
        "sub": "जगदीश हरे • लक्ष्मीनारायण • सत्यनारायण",
        "audio": "https://www.youtube.com/watch?v=kYJv_5b3G6o"
    },
    "Gods Aarti": {
        "key": "gods",
        "title_hi": "देवगण पावन आरती संग्रह",
        "title_en": "Gods Aarti",
        "deity": "समस्त देवगण (सूर्य, शनि, नृसिंह, कुबेर)",
        "img": "assets/gallery/bal_surya_little.jpg",
        "fallback": "assets/deity_surya.jpg",
        "mantra": "॥ ॐ सूर्याय नमः • ॐ शं शनैश्चराय नमः ॥",
        "sub": "सूर्य • शनिदेव • नृसिंह • कुबेर • धन्वन्तरि",
        "audio": "https://www.youtube.com/watch?v=Q74V3j2nJ2k"
    },
    "Goddesses Aarti": {
        "key": "goddesses",
        "title_hi": "देवी माँ पावन आरती संग्रह",
        "title_en": "Goddesses Aarti",
        "deity": "आदिशक्ति माँ भगवती व देवियां",
        "img": "assets/gallery/bal_durga.jpg",
        "fallback": "assets/deity_durga.jpg",
        "mantra": "॥ सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके ॥",
        "sub": "अम्बे गौरी • लक्ष्मी • सरस्वती • संतोषी • गंगा",
        "audio": "https://www.youtube.com/watch?v=8q3J9z8eN1s"
    },
    "Sants Aarti": {
        "key": "sants",
        "title_hi": "सन्त व लोकदेवता आरती संग्रह",
        "title_en": "Sants Aarti",
        "deity": "खाटू श्याम • साईं बाबा • संतगण",
        "img": "assets/deity_khatushyam.jpg",
        "fallback": "assets/deity_saibaba.jpg",
        "mantra": "॥ ॐ श्री श्याम देवाय नमः ॥",
        "sub": "खाटू श्याम • साईं गुरुवर • रामदेव • महावीर",
        "audio": "https://www.youtube.com/watch?v=vVj4k3L3N6I"
    },
    "Other Aarti": {
        "key": "other",
        "title_hi": "गीता व पितर आरती संग्रह",
        "title_en": "Gita & Pitar Aarti",
        "deity": "श्रीमद्भगवद्गीता व पितृगण",
        "img": "assets/gallery/bal_krishna_little.jpg",
        "fallback": "assets/deity_krishna.jpg",
        "mantra": "॥ ॐ श्री कृष्णाय नमः ॥",
        "sub": "भगवद् गीता • पितर जी महाराज",
        "audio": "assets/audio/bhajan_achyutam_keshavam.mp3"
    }
}

final_collections = {}

for cat in drik_categories:
    cat_name = cat['category']
    cfg = CATEGORY_CONFIG.get(cat_name)
    if not cfg: continue
    
    cat_key = cfg['key']
    final_collections[cat_key] = {
        "key": cat_key,
        "title": cfg['title_hi'],
        "title_en": cfg['title_en'],
        "deity": cfg['deity'],
        "img": cfg['img'],
        "fallbackImg": cfg['fallback'],
        "mantra": cfg['mantra'],
        "sub": cfg['sub'],
        "items": []
    }
    
    for idx, item in enumerate(cat['items']):
        content, audio = find_lyrics(item['hi_line'], item['title'], item['en_line'])
        if not audio:
            audio = cfg['audio']
        if not content:
            content = f"""॥ {item['title']} ॥
({item['en_line']})

{item['hi_line']}

{item['hi_line']}
भक्तजनों के संकट क्षण में दूर करें ।
जो जन आरती प्रेम सहित नित गावे,
सुख-सम्पत्ति और परम शान्ति पावे ॥

॥ ॐ जय जगदीश हरे ॥"""

        final_collections[cat_key]['items'].append({
            "id": f"drik_{cat_key}_{idx+1}",
            "title": item['title'],
            "en_line": item['en_line'],
            "hi_line": item['hi_line'],
            "sub": f"{item['en_line']} • {item['hi_line']}",
            "thumb": cfg['img'],
            "audio_url": audio,
            "content": content
        })

print(f"Total categories built: {len(final_collections)}")
for k, v in final_collections.items():
    print(f"  • {k}: {len(v['items'])} items")

with open('full_drik_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(final_collections, f, ensure_ascii=False, indent=2)

print("\n✓ Saved to full_drik_aarti_collections.json")
