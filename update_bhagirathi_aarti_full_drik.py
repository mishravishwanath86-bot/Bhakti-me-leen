# -*- coding: utf-8 -*-
"""
Update drik_goddesses_7 (Ganga Bhagiratha Nandini Aarti / जय जय भगीरथनन्दिनि) in:
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

BHAGIRATHI_DATA = {
    "id": "drik_goddesses_7",
    "title": "जय जय भगीरथनन्दिनि",
    "title_en": "Ganga Bhagiratha Nandini Aarti (Jai Jai Bhagirathanandini)",
    "en_line": "Jai Jai Bhagirathanandini, Muni-Chaya Chakora-Chandini",
    "hi_line": "जय जय भगीरथनन्दिनि, मुनि-चय चकोर-चन्दिनि",
    "sub": "गोस्वामी तुलसीदास कृत काशी दशाश्वमेध घाट पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_ganga_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ZpfdoY3X1_8",
    "video_id": "ZpfdoY3X1_8",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/ganga-mata/ganga-bhagiratha-nandini-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ गंगा माता आरती ॥
(जय जय भगीरथनन्दिनि)

जय जय भगीरथनन्दिनि,
मुनि-चय चकोर-चन्दिनि,
नर-नाग-बिबुध-बन्दिनि,
जय जह्नुबालिका।

जय जय भगीरथनन्दिनि...।

विष्णु-पद-सरोजजासि,
ईस-सीस पर बिभासि,
त्रिपथगासि, पुन्यरासि,
पाप-छालिका॥

जय जय भगीरथनन्दिनि...।

बिमल बिपुल बहसि बारि,
सीतल त्रयताप-हारि,
भँवर बर बिभन्गतर
तरन्ग-मालिका।

जय जय भगीरथनन्दिनि...।

पुरजन पूजोपहार सोभित
ससि धवल धार,
भंजन भव-भार,
भक्ति-कल्प थालिका॥

जय जय भगीरथनन्दिनि...।

निज तट बासी बिहन्ग,
जल-थल-चर पसु-पतन्ग,
कीट, जटिल तापस,
सब सरिस पालिका।

जय जय भगीरथनन्दिनि...।

तुलसी तव तीर तीर
सुमिरत रघुवन्स-बीर,
बिचरत मति देहि
मोह-महिष-कालिका॥

जय जय भगीरथनन्दिनि...।""",
    "meaning": """॥ श्री गंगा भगीरथनन्दिनि आरती (जय जय भगीरथनन्दिनि) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य स्तुति-आरती महाकवि गोस्वामी तुलसीदास जी द्वारा रचित 'विनय पत्रिका' का परम पावन गंगा-स्तवन है, जो काशी के दशाश्वमेध घाट पर नित्य संध्या महाआरती में भावविभोर होकर गाई जाती है।)

१. प्रथम पद (टेक / मुखड़ा — भगीरथनन्दिनी, मुनि-मन चकोर चन्द्रिका व जह्नुतनया):
"जय जय भगीरथनन्दिनि, मुनि-चय चकोर-चन्दिनि,
नर-नाग-बिबुध-बन्दिनि, जय जह्नुबालिका।
जय जय भगीरथनन्दिनि...।"

भावार्थ:
हे राजा भगीरथ की तपस्या से भूतल पर अवतरित होने वाली भगीरथनन्दिनी माँ गंगे! आपकी सदा ही जय हो, जय-जयकार हो। मुनिजनों और संतों के चित्त रूपी चकोर पक्षियों को तृप्त करने के लिए आप पूर्णिमा की शीतल चन्द्रिका (चांदनी) के समान हैं। मनुष्य, नाग और समस्त देवता (विबुध) नित्य भावपूर्वक आपकी वंदना करते हैं। हे महर्षि जह्नु की पावन कन्या (जह्नुबालिका / जाह्नवी)! आपकी अनंत-अनंत बार जय हो।

२. द्वितीय पद (विष्णुपदी, शिव-शीश निवासिनी, त्रिपथगा व पापनाशिनी):
"विष्णु-पद-सरोजजासि, ईस-सीस पर बिभासि,
त्रिपथगासि, पुन्यरासि, पाप-छालिका॥
जय जय भगीरथनन्दिनि...।"

भावार्थ:
आप भगवान श्रीहरि विष्णु के पावन चरणकमलों (पद-सरोज) से प्रादुर्भूत हुई हैं और देवाधिदेव भगवान शिव (ईश) के मस्तक (शीश) पर जटाजूट में परम शोभा पा रही हैं। आप स्वर्ग, मर्त्य और पाताल तीनों लोकों में प्रवाहित होने वाली 'त्रिपथगा' हैं; आप साक्षात पुण्यों की अक्षय राशि (पुण्यराशि) हैं और शरणागत जीवों के जन्म-जन्मांतर के घोर पापों का क्षालन (नाश) करने वाली हैं।

३. तृतीय पद (शीतल विमल जल, त्रिविध ताप-हरण व तरंग-मालिका):
"बिमल बिपुल बहसि बारि, सीतल त्रयताप-हारि,
भँवर बर बिभन्गतर तरन्ग-मालिका।
जय जय भगीरथनन्दिनि...।"

भावार्थ:
आपकी पावन धारा में विपुल (अथाह), विमल और अत्यंत निर्मल जल निरंतर प्रवाहित होता रहता है, जो जीवों के आधि-व्याधि, दैहिक, दैविक और भौतिक—तीनों प्रकार के संतापों (त्रयताप) को शांत करने वाला परम शीतल अमृत है। आपके जल में सुंदर चक्राकार भंवर और उठती-गिरती मनोरम तरंगों की अनंत मालाएं अद्भुत छटा बिखेरती हैं।

४. चतुर्थ पद (शशि-धवल धार, पुरजन-पूजोपहार व भव-भार भंजन):
"पुरजन पूजोपहार सोभित ससि धवल धार,
भंजन भव-भार, भक्ति-कल्प थालिका॥
जय जय भगीरथनन्दिनि...।"

भावार्थ:
काशी आदि तीर्थों के नगरवासी (पुरजन) विविध पुष्प, दीप और उपहारों से आपकी पूजा करते हैं, जिससे आपकी चंद्रमा के समान धवल, उज्ज्वल धारा अनुपम रूप से सुशोभित होती है। आप सांसारिक बंधनों और जन्म-मरण के भारी बोझ (भव-भार) का भंजन (नाश) करने वाली हैं तथा अपने भक्तों की समस्त सात्विक कामनाओं को कल्पवृक्ष की भांति पूर्ण करने वाली दिव्य भक्ति की थाली हैं।

५. पंचम पद (समदृष्टि मातृत्व — कीट, पतंग, पशु व तपस्वियों का समान पालन):
"निज तट बासी बिहन्ग, जल-थल-चर पसु-पतन्ग,
कीट, जटिल तापस, सब सरिस पालिका।
जय जय भगीरथनन्दिनि...।"

भावार्थ:
हे जगन्माता! आपके पावन तट पर निवास करने वाले पक्षी (विहंग), जल और थल में विचरण करने वाले प्राणी, पशु, पतंग, कीट-पतंगे और जटाधारी तपस्वी मुनि—आप इन सभी का बिना किसी भेद-भाव के अपने पुत्रों के समान समभाव (सरिस) से वात्सल्यपूर्वक पालन-पोषण करती हैं।

६. षष्ठम पद (गोस्वामी तुलसीदास जी की शरणागति व मोह-विनाश की प्रार्थना):
"तुलसी तव तीर तीर सुमिरत रघुवन्स-बीर,
बिचरत मति देहि मोह-महिष-कालिका॥
जय जय भगीरथनन्दिनि...।"

भावार्थ:
गोस्वामी तुलसीदास जी करबद्ध प्रार्थना करते हैं: हे माँ गंगे! आपके पावन तट-तट पर विचरण करते हुए मैं रघुकुल शिरोमणि भगवान श्रीराम (रघुवंश-वीर) का निरंतर स्मरण करता रहूँ। हे माँ! आप मेरी बुद्धि को ऐसी निर्मल शक्ति प्रदान कीजिए, जो मेरे अंतःकरण के 'मोहरूपी महिषासुर' का संहार करने के लिए साक्षात भगवती कालिका बन जाए।""",
    "vidhi": """॥ श्री गंगा भगीरथनन्दिनी आरती — काशी दशाश्वमेध घाट शास्त्रोक्त 4-2-1-7 विधान ॥

काशी के परम पावन दशाश्वमेध घाट की शास्त्रोक्त अर्चक परंपरा अनुसार दीप व प्रदक्षिणा विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल के विशाल पंचमुखी, सप्तमुखी अथवा सहस्रमुखी दीप-स्तंभ में गाय के शुद्ध घी के दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाल में लाल गुलाब, गेंदा पुष्प, रोली, चंदन, अक्षत, इत्र, धूप-दशांग तथा शंख-घंटा रखें। 'ॐ नमो भगवत्यै गङ्गायै नमः' अथवा 'विष्णुपादाब्जसंभूते गङ्गे त्रिपथगामिनि' मन्त्र का स्मरण करें।

२. पावन जल-तरंगों में ४ बार घुमाएं:
सर्वप्रथम आरती के ज्योति-स्तंभ को दक्षिणावर्त (Clockwise) दिशा में माँ गंगा की अमृतमयी जलधारा के सम्मुख ४ बार घुमाएं। यह चारों वेदों, चारों पुरुषार्थों की सिद्धि और विष्णुपदी चरणों की वंदना है।

३. भंवर व प्रवाह-मध्य में २ बार घुमाएं:
तत्पश्चात दीपक को गंगा जी के मध्य प्रवाह के समक्ष २ बार घुमाएं। यह संपूर्ण जगत के पोषण केंद्र का सम्मान है।

४. शांत जल-दर्पण पर १ बार घुमाएं:
इसके उपरांत दीपक को गंगा जी के शांत, शीतल जल-दर्पण के समक्ष १ बार घुमाएं। इससे काम, क्रोध, मोह और मानसिक संतापों का शमन होता है।

५. सम्पूर्ण विस्तीर्ण जल-धारा पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को काशी के घाटों से विस्तीर्ण सम्पूर्ण पावन धारा पर भावपूर्वक ७ बार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवन की शुद्धि व प्रदक्षिणा चक्र पूर्ण होता है।)

६. चंवर सेवा, डमरू-नाद एवं दीपदान:
आरती पूर्ण होने पर डमरू, शंख, घड़ियाल बजाएं। मोरछड़ी व चंवर डुलाएं तथा 'हर हर महादेव', 'हर हर गंगे' का त्रिवार जयघोष करें। जल में दीपदान करें और दोनों हाथों से पावन ताप ग्रहण करें।""",
    "significance": """॥ श्री गंगा भगीरथनन्दिनी आरती — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. गोस्वामी तुलसीदास कृत प्रामाणिक स्तोत्र:
यह आरती गोस्वामी तुलसीदास जी द्वारा रचित 'विनय पत्रिका' का एक अत्यंत सिद्ध एवं तेजस्वी पद है। इसके पाठ से साक्षात माँ गंगा और भगवान श्रीराम दोनों की परम कृपा एक साथ प्राप्त होती है।

२. मोह-महिषासुर का संहार:
"बिचरत मति देहि मोह-महिष-कालिका" — इस आरती के नियमित गान से साधक की बुद्धि जाग्रत होती है और अज्ञान, मोह, सांसारिक आसक्ति व मानसिक भ्रम समूल नष्ट हो जाते हैं।

३. त्रिविध तापों से मुक्ति:
"सीतल त्रयताप-हारि" — जो साधक इस आरती का पाठ करता है, उसके जीवन के तीनों ताप (आधिभौतिक, आधिदैविक, आध्यात्मिक) शांत हो जाते हैं और हृदय में असीम शांति स्थापित होती है।

४. काशी महाआरती का पुण्य फल:
काशी के दशाश्वमेध घाट पर होने वाली विश्वप्रसिद्ध महाआरती का मूल आधार यही स्तुति है। घर पर भी इसका गान करने से काशी-तीर्थ में गंगा-स्नान व दर्शन का पावन फल प्राप्त होता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छह छंद पदों (सहित टेक) पर पूर्णतः आधारित है।""",
    "english_lyrics": """॥ Shri Ganga Bhagiratha Nandini Aarti ॥
(Jai Jai Bhagirathanandini)

Jai Jai Bhagirathanandini,
Muni-Chaya Chakora-Chandini,
Nara-Naaga-Bibudha-Bandini,
Jaya Jahnubaalika।

Jai Jai Bhagirathanandini...।

Vishnu-Pada-Sarojajaasi,
Eesa-Seesa Para Bibhaasi,
Tripathagaasi, Punyaraasi,
Paapa-Chhaalika॥

Jai Jai Bhagirathanandini...।

Bimala Bipula Bahasi Baari,
Seetala Trayataapa-Haari,
Bhanvara Bara Bibhangatara
Taranga-Maalika।

Jai Jai Bhagirathanandini...।

Purajana Poojopahaara Sobhita
Sasi Dhavala Dhaara,
Bhanjana Bhava-Bhaara,
Bhakti-Kalpa Thaalika॥

Jai Jai Bhagirathanandini...।

Nija Tata Baasee Bihanga,
Jala-Thala-Chara Pasu-Patanga,
Keeta, Jatila Taapasa,
Saba Sarisa Paalika।

Jai Jai Bhagirathanandini...।

Tulasee Tava Teera Teera
Sumirata Raghuwansa-Beera,
Bicharata Mati Dehi
Moha-Mahisha-Kaalika॥

Jai Jai Bhagirathanandini...।"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['ganga', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_7':
                fg_data[cat_name]['items'][i] = BHAGIRATHI_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_7 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_7':
                    cdata['items'][i] = BHAGIRATHI_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_7 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(BHAGIRATHI_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_7"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_7 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_7 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
