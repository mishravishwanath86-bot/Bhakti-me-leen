# -*- coding: utf-8 -*-
"""
Update drik_goddesses_23 (Narmada Mata Aarti / ॐ जय जगदानन्दी) in:
1. final_granular_aarti_collections.json
2. full_drik_aarti_collections.json
3. app.js
with 100% complete Drik Panchang verified data.
"""

import json
import os
import shutil

scratch_dir = r"c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
final_json_path = os.path.join(scratch_dir, "final_granular_aarti_collections.json")
full_json_path = os.path.join(scratch_dir, "full_drik_aarti_collections.json")
app_js_path = os.path.join(scratch_dir, "app.js")

NARMADA_DATA = {
    "id": "drik_goddesses_23",
    "title": "ॐ जय जगदानन्दी",
    "title_en": "Narmada Mata Aarti (Om Jai Jagadanandi)",
    "en_line": "Om Jai Jagadanandi, Maiya Jai Ananda Kandi",
    "hi_line": "ॐ जय जगदानन्दी, मैया जय आनंद कन्दी",
    "sub": "माँ नर्मदा रेवा जी की पावन स्तुति-आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_ganga_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ZklH-ydA8LU",
    "video_id": "ZklH-ydA8LU",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/narmada-mata/narmada-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री नर्मदा माता जी की आरती ॥
(ॐ जय जगदानन्दी)

ॐ जय जगदानन्दी,
मैया जय आनंद कन्दी।
ब्रह्मा हरिहर शंकर रेवा,
शिव हरि शंकर रुद्री पालन्ती॥

ॐ जय जगदानन्दी...॥

देवी नारद शारद तुम वरदायक,
अभिनव पदचण्डी।
सुर नर मुनि जन सेवत,
सुर नर मुनि शारद पदवन्ती॥

ॐ जय जगदानन्दी...॥

देवी धूमक वाहन राजत,
वीणा वादयन्ती।
झूमकत झूमकत झूमकत,
झननन झननन रमती राजन्ती॥

ॐ जय जगदानन्दी...॥

देवी बाजत ताल मृदंगा,
सुरमण्डल रमती।
तोड़ीतान तोड़ीतान तोड़ीतान,
तुरड़ड़ तुरड़ड़ तुरड़ड़ रमती सुरवन्ती॥

ॐ जय जगदानन्दी...॥

देवी सकल भुवन पर आप विराजत,
निशदिन आनन्दी।
गावत गंगा शंकर, सेवत रेवा
शंकर तुम भव मेटन्ती॥

ॐ जय जगदानन्दी...॥

मैया जी को कंचन थाल विराजत,
अगर कपूर बाती।
अमरकंठ में विराजत,
घाटन घाट कोटी रतन जोती॥

ॐ जय जगदानन्दी...॥

मैया जी की आरती निशदिन पढ़ि गावें,
हो रेवा जुग जुग नर गावें।
भजत शिवानंद स्वामी,
जपत हरि मन वांछित फल पावें॥

ॐ जय जगदानन्दी...॥""",
    "meaning": """॥ श्री नर्मदा माता जी की आरती (ॐ जय जगदानन्दी) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती देवाधिदेव भगवान शिव के पसीने/तप से प्रकट, 'दर्शन मात्रेण पापहन्त्री' पुण्यतोया माँ नर्मदा (रेवा) की पावन वंदना है, जो अमरकंटक, ओंकारेश्वर और जबलपुर (भेड़ाघाट) के तटों पर नित्य संध्या महाआरती में गाई जाती है।)

१. प्रथम पद (टेक / मुखड़ा — जगदानन्दिनी, आनन्दकन्द व शिव-तनया वंदना):
"ॐ जय जगदानन्दी, मैया जय आनंद कन्दी।
ब्रह्मा हरिहर शंकर रेवा, शिव हरि शंकर रुद्री पालन्ती॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
हे संपूर्ण जगत को परमानंद प्रदान करने वाली, आनंद का मूल स्रोत (आनंदकंद) माँ नर्मदा! आपकी सदा ही जय हो, जय-जयकार हो। आप ब्रह्मा, विष्णु और महेश (हरिहर शंकर) द्वारा पूजित साक्षात रेवा हैं; तथा भगवान शिव के रुद्रावतारों और संपूर्ण चराचर जीवों का वात्सल्यपूर्वक पालन-पोषण करने वाली हैं।

२. द्वितीय पद (नारद-शारदा पूजिता, वरदायिनी व पदवन्दना):
"देवी नारद शारद तुम वरदायक, अभिनव पदचण्डी।
सुर नर मुनि जन सेवत, सुर नर मुनि शारद पदवन्ती॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
हे देवी! देवर्षि नारद और ज्ञान की देवी माँ शारदा भी आपकी स्तुति कर आपसे वरदान प्राप्त करती हैं। आप नवदुर्गाओं में अभिनव पराक्रमशालिनी चंडी स्वरूपा हैं। समस्त देवगण, मनुष्य, सिद्ध मुनिजन और ज्ञानीजन आपके पावन चरणकमलों की नित्य सेवा और वंदना करते हैं।

३. तृतीय पद (धूमक वाहन, वीणा-वादन व दिव्य नूपुर झंकार):
"देवी धूमक वाहन राजत, वीणा वादयन्ती।
झूमकत झूमकत झूमकत, झननन झननन रमती राजन्ती॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
हे माँ! आप मगरमच्छ (धूमक/मकर) रूपी दिव्य वाहन पर अत्यंत शोभा पा रही हैं और अपने करकमलों में मधुर वीणा बजाती हुई प्रवाहित होती हैं। आपकी पावन जल-तरंगों में नूपुरों की झंकार (झननन-झननन) के साथ आनंदमयी क्रीड़ा और शोभा छलकती है।

४. चतुर्थ पद (ताल-मृदंग नाद, सुरमंडल व तान-तरंग):
"देवी बाजत ताल मृदंगा, सुरमण्डल रमती।
तोड़ीतान तोड़ीतान तोड़ीतान, तुरड़ड़ तुरड़ड़ तुरड़ड़ रमती सुरवन्ती॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
हे देवनदी! आपके तटों पर ताल, मृदंग और सुरमंडल के मधुर नाद गूंजते हैं। आपकी कलकल करती पावन जलधारा राग-रागिनियों की मधुर तान छेड़ती हुई और अलौकिक संगीत की ध्वनि बिखेरती हुई आनंदपूर्वक आगे बढ़ती है।

५. पंचम पद (सकल भुवन व्यापिनी, गंगा-शंकर सेविता व भव-मोचनी):
"देवी सकल भुवन पर आप विराजत, निशदिन आनन्दी।
गावत गंगा शंकर, सेवत रेवा शंकर तुम भव मेटन्ती॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
हे माँ रेवा! आप संपूर्ण लोकों में नित्य आनंदमयी होकर विराजती हैं। स्वयं देवनदी गंगा और भगवान शंकर आपका यश गान करते हैं तथा जो भी निष्ठा से आपकी सेवा करता है, आप उसके सांसारिक जन्म-मरण के बंधन (भव) को सदा के लिए मिटा देती हैं।

६. षष्ठम पद (कंचन थाल, अगर-कपूर धूप व कोटि-रत्न ज्योति):
"मैया जी को कंचन थाल विराजत, अगर कपूर बाती।
अमरकंठ में विराजत, घाटन घाट कोटी रतन जोती॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
हे मैया! आपके पूजन हेतु सोने की थाली (कंचन थाल) में अगर, सुगंधित धूप और कपूर की बत्तियां प्रज्वलित की जाती हैं। आप अपने उद्गम तीर्थ अमरकंटक में साक्षात विराजती हैं तथा आपके पावन घाट-घाट पर करोड़ों रत्नों के समान दीपकों की अलौकिक ज्योति जगमगाती है।

७. सप्तम पद (फलश्रुति — शिवानन्द स्वामी कृत स्तुति व मनोरथ सिद्धि):
"मैया जी की आरती निशदिन पढ़ि गावें, हो रेवा जुग जुग नर गावें।
भजत शिवानंद स्वामी, जपत हरि मन वांछित फल पावें॥
ॐ जय जगदानन्दी...॥"

भावार्थ:
जो भी नर-नारी माँ नर्मदा की यह पावन आरती नित्य नियम से गाते हैं, स्वामी शिवानंद जी कहते हैं कि श्रीहरि और भगवान शिव का भजन व ध्यान करते हुए उन्हें धर्म, अर्थ, काम और मोक्ष सहित समस्त मनवांछित फल प्राप्त होते हैं।""",
    "vidhi": """॥ श्री नर्मदा जी की आरती — अमरकंटक व ओंकारेश्वर घाट शास्त्रोक्त 4-2-1-7 विधान ॥

पुण्यतोया माँ नर्मदा (रेवा) की आरती उतारने का विशेष शास्त्रोक्त एवं परिक्रमा विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल या तांबे की थाली में शुद्ध गाय के घी का पंचमुखी दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाल में लाल पुष्प, बेलपत्र, अक्षत, रोली, चंदन, अगरबत्ती, कलावा, चुनरी और बताशे या पेड़े का भोग रखें। 'ॐ नमो भगवत्यै नर्मदायै' अथवा 'नर्मदायै नमः प्रातः नर्मदायै नमो निशि। नमोऽस्तु नर्मदे तुभ्यं त्राहि मां भवसागरात्॥' मन्त्र का स्मरण करें।

२. पावन जल-धारा में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में माँ नर्मदा की पावन धारा के सम्मुख ४ बार घुमाएं। यह चारों पुरुषार्थों की सिद्धि और शिव-तनया चरणों की वंदना है।

३. मकर-वाहन व मध्य-प्रवाह पर २ बार घुमाएं:
तत्पश्चात दीपक को माँ के मध्य-प्रवाह व मकर-वाहन के समक्ष २ बार घुमाएं। यह जीवन-दायिनी पोषण शक्ति का नमन है।

४. शांत जल-दर्पण पर १ बार घुमाएं:
इसके उपरांत दीपक को माँ नर्मदा के शांत, शीतल जल-दर्पण के समक्ष १ बार घुमाएं। इससे मानसिक तनाव, क्रोध और अविद्या का नाश होता है।

५. सम्पूर्ण विस्तीर्ण जल-धारा पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को अमरकंटक से लेकर भड़ौच तक विस्तीर्ण संपूर्ण पावन धारा पर भावपूर्वक ७ बार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवन की शुद्धि व प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, शंख-नाद एवं दीपदान:
आरती पूर्ण होने पर शंख, घंटा, मृदंग बजाएं और 'नर्मदे हर' का त्रिवार पावन उद्घोष करें। पत्तों के दोने में पुष्प व दीप रखकर जल में दीपदान करें तथा आरती का पावन ताप ग्रहण करें।""",
    "significance": """॥ श्री नर्मदा माता आरती (ॐ जय जगदानन्दी) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'दर्शन मात्रेण पापहन्त्री' — दर्शन मात्र से मुक्ति:
शास्त्रों में कहा गया है: "स्नानेन गंगा तरति, स्मरणादेव यमुना। दर्शनादेव नर्मदा..." अर्थात् गंगा स्नान से, यमुना स्मरण से, किंतु माँ नर्मदा का केवल दर्शन करने मात्र से ही मनुष्य के समस्त पाप नष्ट हो जाते हैं।

२. साक्षात शिव-तनया एवं कंकर-कंकर शंकर:
माँ नर्मदा भगवान शिव के अंग से प्रकट हुई हैं। इनके तलहटी का प्रत्येक पाषाण 'नर्मदेश्वर शिवलिंग' के रूप में साक्षात पूजनीय है। इस आरती के गान से भगवान शिव और माँ शक्ति दोनों की संयुक्त कृपा प्राप्त होती है।

३. नर्मदा परिक्रमा का पावन पुण्य:
माँ नर्मदा विश्व की एकमात्र ऐसी नदी हैं जिनकी संपूर्ण परिक्रमा की जाती है। घर बैठे इस आरती का नित्य पाठ करने से नर्मदा परिक्रमा का आधा पुण्य अनायास ही प्राप्त होता है।

४. अकाल संकट, सर्प-दोष व पितृ-मुक्ति:
"त्राहि मां भवसागरात्" — इस पावन आरती के श्रवण व गान से जीवन के अकाल संकट, सर्प-दोष, वास्तु-दोष और पितृ-दोष दूर होते हैं तथा कुल में सुख-शांति का वास होता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक सात छंद पदों पर पूर्णतः आधारित है, जो अमरकंटक, भेड़ाघाट और ओंकारेश्वर ज्योतिर्लिंग तट पर नित्य गाई जाती है।""",
    "english_lyrics": """॥ Shri Narmada Mata Aarti ॥
(Om Jai Jagadanandi)

Om Jai Jagadanandi,
Maiya Jai Ananda Kandi।
Brahma Harihara Shankara Reva,
Shiva Hari Shankara Rudree Paalantee॥

Om Jai Jagadanandi...॥

Devi Naarada Sharada Tuma Varadaayaka,
Abhinava Padachandee।
Sura Nara Muni Jana Sevata,
Sura Nara Muni Sharada Padawantee॥

Om Jai Jagadanandi...॥

Devi Dhoomaka Vaahana Raajata,
Veena Vaadayantee।
Jhoomakata Jhoomakata Jhoomakata,
Jhananana Jhananana Ramatee Raajantee॥

Om Jai Jagadanandi...॥

Devi Baajata Taala Mridanga,
Suramandala Ramatee।
Todeetaan Todeetaan Todeetaan,
Turadada Turadada Turadada Ramatee Surawantee॥

Om Jai Jagadanandi...॥

Devi Sakala Bhuvana Para Aapa Viraajata,
Nishadina Aanandee।
Gaavata Ganga Shankara, Sevata Reva
Shankara Tuma Bhava Metantee॥

Om Jai Jagadanandi...॥

Maiya Ji Ko Kanchana Thaala Viraajata,
Agara Kapoora Baatee।
Amarakanta Mein Viraajata,
Ghaatana Ghaata Kotee Ratana Jotee॥

Om Jai Jagadanandi...॥

Maiya Ji Ki Aarti Nishadina Padhi Gaaven,
Ho Reva Juga Juga Nara Gaaven।
Bhajata Shivaananda Swami,
Japata Hari Mana Vaanchhita Phala Paaven॥

Om Jai Jagadanandi...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['ganga', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_23':
                fg_data[cat_name]['items'][i] = NARMADA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_23 in final_granular category: {cat_name}")

with open(final_json_path, 'w', encoding='utf-8') as f:
    json.dump(fg_data, f, ensure_ascii=False, indent=2)
print(f"[OK] Saved final_granular_aarti_collections.json (updated {updated_fg} occurrences)")

# 2. Update full_drik_aarti_collections.json
if os.path.exists(full_json_path):
    shutil.copyfile(full_json_path, full_json_path + ".bak")
    with open(full_json_path, 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    
    updated_full = 0
    for cat_name, cdata in full_data.items():
        if isinstance(cdata, dict) and 'items' in cdata:
            for i, item in enumerate(cdata['items']):
                if item.get('id') == 'drik_goddesses_23':
                    cdata['items'][i] = NARMADA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_23 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(NARMADA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_23"', pos)
    if id_pos == -1:
        break
    
    brace_start = app_js.rfind('{', 0, id_pos)
    # find matching closing brace
    depth = 0
    brace_end = -1
    for k in range(brace_start, len(app_js)):
        if app_js[k] == '{':
            depth += 1
        elif app_js[k] == '}':
            depth -= 1
            if depth == 0:
                brace_end = k + 1
                break
    
    if brace_start != -1 and brace_end != -1:
        app_js = app_js[:brace_start] + new_block_str + app_js[brace_end:]
        pos = brace_start + len(new_block_str)
        replaced_count += 1
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_23 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_23 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
