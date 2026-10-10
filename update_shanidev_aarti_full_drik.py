# -*- coding: utf-8 -*-
"""
Update drik_gods_3 (Lord Shanidev Aarti / जय जय श्री शनिदेव) in:
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

SHANIDEV_DATA = {
    "id": "drik_gods_3",
    "title": "जय जय श्री शनिदेव",
    "title_en": "Lord Shanidev Aarti (Jai Jai Shri Shanidev)",
    "en_line": "Jai Jai Shri Shanidev Bhaktana Hitakari",
    "hi_line": "जय जय श्री शनिदेव भक्तन हितकारी, सूरज के पुत्र प्रभु छाया महतारी",
    "sub": "कर्मफल दाता न्यायप्रिय भगवान श्री शनिदेव जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/deity_shanidev.jpg",
    "audio_url": "https://www.youtube.com/watch?v=tcQMwShHwI8",
    "video_id": "tcQMwShHwI8",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-shanidev/shri-shanidev-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ शनिदेव की आरती ॥
(जय जय श्री शनिदेव)

जय जय श्री शनिदेव
भक्तन हितकारी।
सूरज के पुत्र प्रभु
छाया महतारी॥

जय जय श्री शनिदेव भक्तन हितकारी॥

श्याम अंग वक्र-दृष्टि
चतुर्भुजा धारी।
निलाम्बर धार नाथ
गज की असवारी॥

जय जय श्री शनिदेव भक्तन हितकारी॥

क्रीट मुकुट शीश सहज
दिपत है लिलारी।
मुक्तन की माल गले
शोभित बलिहारी॥

जय जय श्री शनिदेव भक्तन हितकारी॥

मोदक और मिष्ठान चढ़े,
चढ़ती पान सुपारी।
लोहा, तिल, तेल, उड़द
महिषी है अति प्यारी॥

जय जय श्री शनिदेव भक्तन हितकारी॥

देव दनुज ऋषि मुनि
सुमिरत नर नारी।
विश्वनाथ धरत ध्यान हम
हैं शरण तुम्हारी॥

जय जय श्री शनिदेव भक्तन हितकारी॥""",
    "meaning": """॥ श्री शनिदेव आरती (जय जय श्री शनिदेव) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती कर्मफलदाता, सूर्य-पुत्र, न्याय के अधिष्ठाता भगवान श्री शनिदेव जी की परम कृपालुता, स्वरूप-दर्शन, प्रिय भोग और शरणागति की पावन स्तुति है।)

१. प्रथम पद (टेक / मुखड़ा — सूर्यपुत्र, भक्तहितकारी वंदना):
"जय जय श्री शनिदेव भक्तन हितकारी।
सूरज के पुत्र प्रभु छाया महतारी॥
जय जय श्री शनिदेव भक्तन हितकारी॥"

भावार्थ:
हे भक्तों का नित्य कल्याण व हित करने वाले भगवान श्री शनिदेव! आपकी सदा ही जय हो, जय-जयकार हो। आप भगवान भुवन-भास्कर सूर्यदेव के पावन पुत्र हैं और माता छाया आपकी जननी (माता) हैं। आप अपने शरणागत निष्कपट भक्तों पर सदा दया की वर्षा करने वाले परम कृपालु देव हैं।

२. द्वितीय पद (दिव्य श्याम विग्रह, चतुर्भुज व गज-सवारी):
"श्याम अंग वक्र-दृष्टि चतुर्भुजा धारी।
निलाम्बर धार नाथ गज की असवारी॥
जय जय श्री शनिदेव भक्तन हितकारी॥"

भावार्थ:
हे प्रभु! आपका पावन श्रीविग्रह श्याम (नील-कृष्ण) वर्ण का है। आपकी दृष्टि वक्र (न्याययुक्त व गोपनीय कर्मों का भेद जानने वाली) तथा आप चार भुजाओं (चतुर्भुज) से युक्त हैं। आप दिव्य नीले वस्त्र (नीलांबर) धारण करते हैं और आपकी पावन सवारी गजराज (हाथी) है, जो शुभता, ऐश्वर्य और स्थिरता का प्रतीक है।

३. तृतीय पद (किरीट मुकुट, भाल-तेज व मुक्तामाला):
"क्रीट मुकुट शीश सहज दिपत है लिलारी।
मुक्तन की माल गले शोभित बलिहारी॥
जय जय श्री शनिदेव भक्तन हितकारी॥"

भावार्थ:
हे न्यायदेव! आपके शीश पर दिव्य किरीट मुकुट शोभायमान है और आपके ललाट (लिलारी) पर सहज ही अनुपम तेज दीप्त हो रहा है। आपके वक्षस्थल और गले में मोतियों (मुक्तन) की पावन माला सुशोभित है। आपके इस अलौकिक रूप-लावण्य पर हम बारंबार बलिहारी जाते हैं।

४. चतुर्थ पद (प्रिय नैवेद्य — मोदक, ताम्बूल, तिल, तेल व महिषी):
"मोदक और मिष्ठान चढ़े, चढ़ती पान सुपारी।
लोहा, तिल, तेल, उड़द महिषी है अति प्यारी॥
जय जय श्री शनिदेव भक्तन हितकारी॥"

भावार्थ:
भक्तगण आपको श्रद्धापूर्वक मोदक, विविध मिष्ठान, पावन ताम्बूल (पान) और सुपारी अर्पित करते हैं। आपको लोहे की वस्तुएं, काले तिल, शुद्ध सरसों का तेल, साबुत उड़द तथा महिषी (काली गाय/भैंस) अत्यंत प्रिय हैं। इन पवित्र वस्तुओं के दान और अर्पण से आप अत्यंत प्रसन्न होकर भक्तों के कष्ट हरते हैं।

५. पंचम पद (समस्त लोकों द्वारा वंदनीय व अनन्य शरणागति):
"देव दनुज ऋषि मुनि सुमिरत नर नारी।
विश्वनाथ धरत ध्यान हम हैं शरण तुम्हारी॥
जय जय श्री शनिदेव भक्तन हितकारी॥"

भावार्थ:
देवता, दानव, सिद्ध ऋषि-मुनि और समस्त नर-नारी आपके प्रचंड न्याय और प्रभाव का नित्य स्मरण करते हैं। स्वयं काशी विश्वनाथ भगवान शंकर भी आपके न्याय-तत्व का आदर करते हैं। हे कर्मफल विधाता प्रभु! हम सभी प्रकार से आपकी ही पावन शरण में उपस्थित हैं, हमारी रक्षा कीजिए और हमें अपने अनुग्रह से कृतार्थ कीजिए।""",
    "vidhi": """॥ भगवान श्री शनिदेव आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व शनिवार दीप विधान ॥

कर्मफलदाता भगवान श्री शनिदेव जी की आरती उतारने का विशेष शास्त्रोक्त एवं तांत्रिक-वैदिक विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
लोहे अथवा मिट्टी के स्वच्छ दीपक में शुद्ध सरसों का तेल अथवा तिल का तेल भरें और उसमें काले तिल डालकर नीली या लाल बत्ती प्रज्वलित करें। थाल में काले तिल, उड़द, नीले या बैंगनी पुष्प (अपराजिता), शमी पत्र, काला वस्त्र, सुपारी और लौंग रखें। 'ॐ शं शनैश्चराय नमः' अथवा 'ॐ प्रां प्रीं प्रौं सः शनैश्चराय नमः' मन्त्र का स्मरण करें।

२. चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में भगवान शनिदेव के पावन चरणकमलों में ४ बार घुमाएं। (विशेष ध्यान रहे: शनिदेव के नेत्रों में सीधे न देखकर उनके पावन चरणों का ही दर्शन व ध्यान किया जाता है)।

३. नाभि-मंडल पर २ बार घुमाएं:
तत्पश्चात दीपक को प्रभु के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह जीवन के कर्मों के संतुलन और न्याय के आधार का नमन है।

४. छत्र व मुकुट पर १ बार घुमाएं:
इसके उपरांत दीपक को शनिदेव के किरीट मुकुट और छत्र के समक्ष १ बार घुमाएं। यह उनके कर्मफल-विधान के सर्वोच्च अधिकार का सम्मान है।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को गदा, बाण, त्रिशूल व गज-आसन से लेकर चरणकमलों तक सम्पूर्ण पावन विग्रह पर ७ बार श्रद्धापूर्वक घुमाएं।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, दान एवं आरती ग्रहण:
आरती पूर्ण होने पर 'ॐ शं शनैश्चराय नमः' का जप करें। काले तिल व उड़द का दान करें। आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती की पावन ज्योति का ताप ग्रहण कर अपने शीश व नेत्रों पर लगाएं।""",
    "significance": """॥ श्री शनिदेव आरती (जय जय श्री शनिदेव) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. साढ़ेसाती, ढैय्या व शनि महादशा में अमोघ सुरक्षा:
शनि की साढ़ेसाती, ढैय्या अथवा कुंडली में शनि की प्रतिकूल दशा के समय शनिवार के दिन संध्याकाल में पीपल वृक्ष अथवा शमी वृक्ष के नीचे इस आरती का पाठ करने से शनिदेव के समस्त अनिष्ट प्रभाव शांत हो जाते हैं।

२. कर्म-शुद्धि एवं न्याय का वरदान:
शनिदेव दण्डदाता नहीं, अपितु निष्पक्ष न्यायाधीश हैं। इस आरती के नियमित गान से साधक का अंतःकरण शुद्ध होता है, वह असत्य, कपट, आलस्य और अधर्म के मार्ग से हटकर सत्य और सत्कर्म के मार्ग पर अग्रसर होता है।

३. असाध्य रोग, दरिद्रता व अकाल संकट मुक्ति:
"सूरज के पुत्र प्रभु छाया महतारी, भक्तन हितकारी" — जो भक्त पूर्ण श्रद्धा से शनिदेव की शरण लेते हैं, उनके असाध्य शारीरिक रोग (विशेषकर वात रोग, अस्थि रोग), घोर दरिद्रता और अचानक आने वाले संकट समूल नष्ट होते हैं।

४. लोहा, उद्योग, व्यापार व कार्यक्षेत्र में उन्नति:
लोहे, मशीनरी, तेल, भूमि-भवन, न्याय-व्यवस्था तथा प्रशासनिक कार्यों से जुड़े लोगों के लिए इस आरती का नित्य श्रवण व गान अत्यंत लाभकारी और सफलता प्रदायक है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छंदों पर पूर्णतः आधारित है।""",
    "english_lyrics": """॥ Shri Shanidev Aarti ॥
(Jai Jai Shri Shanidev)

Jai Jai Shri Shanidev
Bhaktana Hitakari।
Sooraja Ke Putra Prabhu
Chhaaya Mahatari॥

Jai Jai Shri Shanidev Bhaktana Hitakari॥

Shyaama Anga Vakra-Drishti
Chaturbhuja Dhaari।
Nilaambara Dhaara Naatha
Gaja Ki Asawaari॥

Jai Jai Shri Shanidev Bhaktana Hitakari॥

Kreeta Mukuta Sheesha Sahaja
Dipata Hai Lilaari।
Muktana Ki Maala Gale
Shobhita Balihaari॥

Jai Jai Shri Shanidev Bhaktana Hitakari॥

Modaka Aura Mishthaana Chadhain,
Chadhatee Paana Supaari।
Loha, Tila, Tela, Urada
Mahishee Hai Ati Pyaari॥

Jai Jai Shri Shanidev Bhaktana Hitakari॥

Deva Danuja Rishi Muni
Sumirata Nara Naari।
Vishwanaatha Dharata Dhyaana Hama
Hain Sharana Tumhaari॥

Jai Jai Shri Shanidev Bhaktana Hitakari॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['shanidev', 'gods']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_gods_3':
                fg_data[cat_name]['items'][i] = SHANIDEV_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_gods_3 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_gods_3':
                    cdata['items'][i] = SHANIDEV_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_gods_3 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(SHANIDEV_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_gods_3"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_gods_3 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_gods_3 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
