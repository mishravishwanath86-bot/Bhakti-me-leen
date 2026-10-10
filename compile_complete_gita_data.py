import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load raw verses & translations
with open('gita_raw_verses.json', 'r', encoding='utf-8') as f:
    raw_verses = json.load(f)

with open('gita_raw_translations.json', 'r', encoding='utf-8') as f:
    raw_translations = json.load(f)

# 2. Build translation lookup
# Prefer Swami Ramsukhdas -> Swami Tejomayananda for Hindi
# Prefer Swami Sivananda -> Swami Gambirananda for English
trans_hi = {}
trans_en = {}
for t in raw_translations:
    vid = t.get('verse_id')
    auth = t.get('authorName', '')
    desc = t.get('description', '').strip()
    
    if auth == 'Swami Ramsukhdas':
        trans_hi[vid] = desc
    elif auth == 'Swami Tejomayananda' and vid not in trans_hi:
        trans_hi[vid] = desc
        
    if auth == 'Swami Sivananda':
        trans_en[vid] = desc
    elif auth == 'Swami Gambirananda' and vid not in trans_en:
        trans_en[vid] = desc

print(f"Loaded {len(raw_verses)} raw verses.")
print(f"Mapped {len(trans_hi)} Hindi translations and {len(trans_en)} English translations.")

# 3. Load chapter intros for 1 to 18 from chapter_{ch}_hi.html
chapter_intros = {}
for ch in range(1, 19):
    try:
        with open(f"chapter_{ch}_hi.html", 'r', encoding='utf-8') as f:
            html = f.read()
        m = re.search(r'<p class="text-justify font-serif text-lg leading-loose text-foreground/90">(.*?)</p>', html, re.DOTALL)
        if m:
            clean = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            chapter_intros[ch] = clean
    except Exception as e:
        print(f"Notice reading chapter_{ch}_hi.html: {e}")

print("Chapter intros loaded for chapters:", list(chapter_intros.keys()))

# 4. Load existing bhagavad_gita_chapters.json to keep existing chapter metadata
with open('bhagavad_gita_chapters.json', 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

existing_chapters = {c['chapter_number']: c for c in existing_data['chapters']}

# 5. Build full chapters list
compiled_chapters = []
for ch_num in range(1, 19):
    meta = existing_chapters.get(ch_num, {})
    
    # Filter verses for this chapter
    ch_verses_raw = [v for v in raw_verses if v.get('chapter_number') == ch_num]
    ch_verses_raw.sort(key=lambda x: x.get('verse_number', 0))
    
    compiled_verses = []
    for v in ch_verses_raw:
        vid = v.get('id')
        v_num = v.get('verse_number')
        sanskrit = v.get('text', '').strip()
        translit = v.get('transliteration', '').strip()
        word_m = v.get('word_meanings', '').strip()
        hi_desc = trans_hi.get(vid, '').strip()
        # Clean Hindi text of internal bracket citations like (टिप्पणी प0 1.2)
        hi_clean = re.sub(r'\(टिप्पणी[^)]+\)', '', hi_desc).strip()
        # Clean leading ॥1.1॥ or ।।1.1।।
        hi_clean = re.sub(r'^[।\s\.\d-]+', '', hi_clean).strip()
        if not hi_clean:
            hi_clean = hi_desc
            
        en_desc = trans_en.get(vid, '').strip()
        
        # Audio URL
        audio_url = f"https://gita-audio.jkyog.org/audio/sanskrit/gita_audios/{ch_num:03d}_{v_num:03d}.mp3"
        
        compiled_verses.append({
            "id": vid,
            "verse_number": v_num,
            "title": f"श्लोक {ch_num}.{v_num}",
            "sanskrit": sanskrit,
            "transliteration": translit,
            "word_meanings": word_m,
            "hindi": hi_clean,
            "english": en_desc,
            "audio_url": audio_url
        })
    
    # Update intro from bhagavadgita.com if available
    intro = chapter_intros.get(ch_num, meta.get('summary', ''))
    
    compiled_chap = {
        "id": ch_num,
        "chapter_number": ch_num,
        "name": meta.get('name', f"अध्याय {ch_num}"),
        "name_transliterated": meta.get('name_transliterated', ''),
        "name_english": meta.get('name_english', ''),
        "verses_count": len(compiled_verses),
        "yoga_group": meta.get('yoga_group', ''),
        "section": meta.get('section', ''),
        "thumb": meta.get('thumb', 'assets/gallery/gita_upadesh_card.jpg'),
        "summary": intro,
        "key_shlokas": meta.get('key_shlokas', []),
        "life_lesson": meta.get('life_lesson', ''),
        "verses": compiled_verses
    }
    compiled_chapters.append(compiled_chap)

print("Compiled all 18 chapters!")
for c in compiled_chapters:
    print(f"Chapter {c['chapter_number']}: {c['name']} has {len(c['verses'])} full verses. Summary len: {len(c['summary'])}")

# Save updated dataset
final_dataset = {
    "title": existing_data.get("title", "श्रीमद्भगवद्गीता — सम्पूर्ण १८ अध्याय"),
    "subtitle": existing_data.get("subtitle", "गीता उपदेश • सम्पूर्ण १८ अध्याय, ७०१ श्लोक एवं पावन भावार्थ (bhagavadgita.com Verified)"),
    "description": existing_data.get("description", ""),
    "total_chapters": 18,
    "total_verses": sum(len(c['verses']) for c in compiled_chapters),
    "audio_source": existing_data.get("audio_source", "assets/audio/bhajan_achyutam_keshavam.mp3"),
    "katha_source": existing_data.get("katha_source", "assets/audio/katha_bhagwat.mp3"),
    "source_url": "https://bhagavadgita.com/",
    "hero_img": "assets/gallery/gita_upadesh_card.jpg",
    "sections": existing_data.get("sections", []),
    "chapters": compiled_chapters
}

with open('bhagavad_gita_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(final_dataset, f, ensure_ascii=False, indent=2)

print(f"\nSaved bhagavad_gita_chapters.json successfully! Total verses: {final_dataset['total_verses']}")
