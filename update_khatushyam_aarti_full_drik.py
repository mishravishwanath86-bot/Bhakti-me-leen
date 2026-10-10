# -*- coding: utf-8 -*-
"""
Update drik_sants_1 (Lord Khatu Shyam Aarti / ॐ जय श्री श्याम हरे, बाबा जय) in:
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

KHATU_SHYAM_DATA = {
    "id": "drik_sants_1",
    "title": "ॐ जय श्री श्याम हरे, बाबा जय",
    "title_en": "Shyam Baba Aarti (Om Jai Shri Shyam Hare)",
    "en_line": "Om Jai Shri Shyam Hare, Baba Jai Shri Shyam Hare",
    "hi_line": "ॐ जय श्री श्याम हरे, बाबा जय श्री श्याम हरे",
    "sub": "हारे का सहारा लखदातार बाबा श्याम की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/deity_khatushyam.jpg",
    "audio_url": "https://www.youtube.com/watch?v=v1OvMbpPMQw",
    "video_id": "v1OvMbpPMQw",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shyam-baba/shyam-baba-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री खाटू श्यामजी की आरती ॥
(ॐ जय श्री श्याम हरे)

ॐ जय श्री श्याम हरे,
बाबा जय श्री श्याम हरे।
खाटू धाम विराजत,
अनुपम रूप धरे॥

ॐ जय श्री श्याम हरे॥

रतन जड़ित सिंहासन,
सिर पर चंवर ढुरे।
तन केसरिया बागो,
कुण्डल श्रवण पड़े॥

ॐ जय श्री श्याम हरे॥

गल पुष्पों की माला,
सिर पर मुकुट धरे।
खेवत धूप अग्नि पर,
दीपक ज्योति जले॥

ॐ जय श्री श्याम हरे॥

मोदक खीर चूरमा,
सुवरण थाल भरे।
सेवक भोग लगावत,
सेवा नित्य करे॥

ॐ जय श्री श्याम हरे॥

झांझ कटोरा और घड़ि़यावल,
शंख मृदंग धुरे।
भक्त आरती गावे,
जय-जयकार करे॥

ॐ जय श्री श्याम हरे॥

जो ध्यावे फल पावे,
सब दुःख से उबरे।
सेवक जन निज मुख से,
श्री श्याम-श्याम उचरे॥

ॐ जय श्री श्याम हरे॥

'श्री श्याम बिहारीजी' की आरती,
जो कोई नर गावे।
कहत भक्त जन,
मनवांछित फल पावे॥

ॐ जय श्री श्याम हरे॥

तन मन धन सब कुछ है तेरा,
हो बाबा सब कुछ है तेरा।
तेरा तुझको अर्पण,
क्या लोग मेरा॥

ॐ जय श्री श्याम हरे॥

जय श्री श्याम हरे,
बाबा जी श्री श्याम हरे।
निज भक्तों के तुमने,
पूरण काज करे॥

ॐ जय श्री श्याम हरे॥""",
    "meaning": """॥ श्री खाटू श्यामजी की आरती (ॐ जय श्री श्याम हरे) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती कलियुग के साक्षात अवतारी, शीश के दानी, मोरवीनंदन, हारे के सहारे भगवान श्री खाटू श्याम जी के अनुपम सौंदर्य, भोग, भक्ति और शरणागति की परम पावन स्तुति है।)

१. प्रथम पद (टेक / मुखड़ा — खाटू धाम निवास व अनुपम रूप वंदना):
"ॐ जय श्री श्याम हरे, बाबा जय श्री श्याम हरे।
खाटू धाम विराजत, अनुपम रूप धरे॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
हे भक्तों के समस्त कष्टों का हरण करने वाले भगवान श्री श्याम प्रभु! आपकी सदा ही जय हो, जय-जयकार हो। आप राजस्थान के परम पावन खाटू धाम में दिव्य रूप से विराजमान हैं तथा आपने भक्तों को दर्शन व आनंद देने हेतु अति मनोहारी व अनुपम रूप धारण किया हुआ है।

२. द्वितीय पद (रत्नजड़ित सिंहासन, चंवर, केसरिया बागा व कुंडल):
"रतन जड़ित सिंहासन, सिर पर चंवर ढुरे।
तन केसरिया बागो, कुण्डल श्रवण पड़े॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
हे लखदातार! आप बहुमूल्य रत्नों से जड़े हुए दिव्य स्वर्ण सिंहासन पर शोभायमान हैं और आपके पावन शीश पर देवगण श्रद्धापूर्वक चंवर डुला रहे हैं। आपके श्रीअंगों पर दिव्य केसरिया बागा (वस्त्र) सुशोभित है तथा आपके दोनों पावन कानों (श्रवण) में रत्नजड़ित कुंडल अनुपम कांति बिखेर रहे हैं।

३. तृतीय पद (पुष्पमाला, शीश मुकुट, सुगंधित धूप व अखंड ज्योति):
"गल पुष्पों की माला, सिर पर मुकुट धरे।
खेवत धूप अग्नि पर, दीपक ज्योति जले॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
हे श्याम प्यारे! आपके वक्षस्थल और गले में ताजे सुवासित पुष्पों और गलाब की दिव्य माला सुशोभित है तथा शीश पर मोरपंख-मंडित भव्य मुकुट विराजित है। भक्तगण पावन अग्नि पर गुग्गल, लोबान और चंदन की धूप महकाते हैं तथा आपके सम्मुख देशी घी की अखंड पावन ज्योति प्रज्वलित कर आरती करते हैं।

४. चतुर्थ पद (छप्पन भोग — मोदक, खीर, चूरमा व नित्य सेवा):
"मोदक खीर चूरमा, सुवरण थाल भरे।
सेवक भोग लगावत, सेवा नित्य करे॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
हे बाबा श्याम! सोने की पवित्र थालियों (सुवरण थाल) में भरकर आपको प्रिय मोदक, मेवा-युक्त खीर और मारवाड़ी चूरमे का पावन छप्पन भोग अर्पित किया जाता है। निष्काम भाव से आपके सेवक व भक्तजन नित्य आपकी प्रेमपूर्वक सेवा और अर्चना में लीन रहते हैं।

५. पंचम पद (वाद्य-नाद — झांझ, कटोरा, घड़ियावल, शंख व मृदंग):
"झांझ कटोरा और घड़ि़यावल, शंख मृदंग धुरे।
भक्त आरती गावे, जय-जयकार करे॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
आपके पावन दरबार में झांझ, कटोरा, घड़ियाल (घंटे), शंख और मृदंग का मंगलमय दिव्य नाद गूंजता रहता है। समस्त भक्तजन एक स्वर में आपकी पावन आरती गाते हैं और 'हारे के सहारे की जय', 'खाटू नरेश की जय' का गगनभेदी जयघोष करते हैं।

६. षष्ठम पद (संकट-निवारण, फल-प्राप्ति व श्याम नाम जप):
"जो ध्यावे फल पावे, सब दुःख से उबरे।
सेवक जन निज मुख से, श्री श्याम-श्याम उचरे॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
जो भी श्रद्धालु सच्चे मन से आपका ध्यान करता है, वह जीवन के समस्त संकटों, अभावों और दुखों से तर जाता है और मनवांछित फल प्राप्त करता है। आपके निष्ठावान सेवक व भक्तजन अपने मुख से प्रतिक्षण केवल 'श्री श्याम-श्याम' महामंत्र का ही पावन उच्चारण करते हैं।

७. सप्तम पद (फलश्रुति — श्याम बिहारी जी की आरती से मनोरथ सिद्धि):
"'श्री श्याम बिहारीजी' की आरती, जो कोई नर गावे।
कहत भक्त जन, मनवांछित फल पावे॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
श्री श्याम बिहारी जी (भगवान श्रीकृष्ण के स्वरूप खाटू नरेश) की जो भी नर-नारी यह पावन आरती नित्य गाता है, संत और भक्तजन कहते हैं कि उस साधक को धर्म, अर्थ, काम और मोक्ष सहित समस्त मनवांछित फल अनायास ही प्राप्त हो जाते हैं।

८. अष्टम पद (पूर्ण आत्मसमर्पण व शरणागति):
"तन मन धन सब कुछ है तेरा, हो बाबा सब कुछ है तेरा।
तेरा तुझको अर्पण, क्या लागे मेरा॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
हे प्रभु! यह शरीर, मन, बुद्धि, धन-संपत्ति और संपूर्ण जीवन सब कुछ आपका ही दिया हुआ है। हे बाबा! इस संसार में मेरा अपना कुछ भी नहीं है; आपकी दी हुई वस्तुएं मैं पूर्ण कृतज्ञता से आपके ही श्रीचरणों में समर्पित करता हूँ।

९. नवम पद (मंगल समापन व भक्तों के कार्य-सिद्धि की वंदना):
"जय श्री श्याम हरे, बाबा जी श्री श्याम हरे।
निज भक्तों के तुमने, पूरण काज करे॥
ॐ जय श्री श्याम हरे॥"

भावार्थ:
हे बाबा श्याम! आपकी अनंत-अनंत बार जय हो। आपने युगों-युगों से अपने शरणागत भक्तों के कठिन से कठिन बिगड़े कार्यों को पूर्ण (सिद्ध) किया है। हे कृपासिंधु! आप हम पर भी अपनी दया दृष्टि सदा बनाए रखें।""",
    "vidhi": """॥ भगवान श्री खाटू श्याम जी आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व मोरछड़ी दीप विधान ॥

हारे के सहारे, शीश के दानी भगवान श्री खाटू श्याम जी की आरती उतारने का विशेष शास्त्रोक्त एवं मंदिर परंपरानुसार विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल या चांदी की थाली में शुद्ध गाय के घी का पंचमुखी दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाल में गुलाब व गेंदे के ताजे पुष्प, इत्र (गुलाब/चंदन), केसरिया बागा, मोरछड़ी (मयूर पंख), चूरमा, पेड़ा या खीर का भोग रखें। 'ॐ श्री श्याम देवाय नमः' अथवा 'ॐ मोर्वीनन्दनाय विद्महे श्यामदेवाय धीमहि तन्नो श्यामः प्रचोदयात्' मन्त्र का स्मरण करें।

२. चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में प्रभु के पावन चरणों में ४ बार घुमाएं। यह चार पुरुषार्थों की सिद्धि और चरण-शरण प्राप्ति का प्रतीक है।

३. नाभि-मंडल पर २ बार घुमाएं:
तत्पश्चात दीपक को प्रभु के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह सृष्टि के पालनकर्ता श्रीहरि के स्वरूप का नमन है।

४. त्रिभंग-शोभित शीश व मोरमुकुट पर १ बार घुमाएं:
इसके उपरांत दीपक को बाबा श्याम के मोरमुकुट, कुंडल-मंडित पावन मुखारविन्द के समक्ष १ बार घुमाएं। यह 'शीश के दानी' के दिव्य बलिदान और अमर तेज का वंदन है।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मोरछड़ी, केसरिया बागा, पुष्पमाला से लेकर चरणकमलों तक सम्पूर्ण पावन विग्रह पर ७ बार श्रद्धापूर्वक घुमाएं।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, मोरछड़ी स्पर्श एवं आरती ग्रहण:
आरती पूर्ण होने पर शंख, घंटा और 'हारे का सहारा बाबा श्याम हमारा' का जयघोष करें। आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती की पावन ज्योति का ताप ग्रहण कर शीश व नयनों पर लगाएं तथा मोरछड़ी का पावन झाड़ा लें।""",
    "significance": """॥ श्री खाटू श्यामजी आरती (ॐ जय श्री श्याम हरे) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'हारे का सहारा' — संकटों में अमोघ संबल:
संसार में जब मनुष्य हर ओर से निराश हो जाता है, तब बाबा श्याम की यह आरती उसके जीवन में नई आशा, आत्मबल और विजय का संचार करती है। इसीलिए इन्हें 'हारे का सहारा' कहा जाता है।

२. शीश के दानी का साक्षात वरदान:
महाभारत युद्ध के समय घटोत्कच-पुत्र बर्बरीक ने धर्म की रक्षा हेतु भगवान श्रीकृष्ण को अपने शीश का दान दिया था। भगवान कृष्ण ने प्रसन्न होकर उन्हें अपना स्वयं का नाम 'श्याम' और कलियुग में घर-घर पूजे जाने का वरदान दिया। इस आरती के गान से साक्षात श्रीकृष्ण की कृपा प्राप्त होती है।

३. एकादशी व द्वादशी पर विशेष फल:
शुक्ल पक्ष की एकादशी और फाल्गुन लक्खी मेले के पावन अवसर पर इस आरती का पाठ करने से जन्म-जन्मांतर के पापों का क्षय होता है और घर में सुख, शांति, समृद्धि व अखंड लक्ष्मी का वास होता है।

४. असाध्य रोगों व मानसिक संतापों से मुक्ति:
"जो ध्यावे फल पावे, सब दुःख से उबरे" — इस आरती के नित्य गान व श्रवण से मानसिक तनाव, अवसाद, भय और जटिल पारिवारिक बाधाएं दूर होती हैं।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक नौ छंद पदों पर पूर्णतः आधारित है, जो खाटू धाम में प्रतिदिन प्रातः-संध्या आरती में गाया जाता है।""",
    "english_lyrics": """॥ Shri Khatu Shyamji Ki Aarti ॥
(Om Jai Shri Shyam Hare)

Om Jai Shri Shyam Hare,
Baba Jai Shri Shyam Hare।
Khatu Dhaama Viraajata,
Anupama Roopa Dhare॥

Om Jai Shri Shyam Hare॥

Ratana Jadita Simhaasana,
Sira Para Chanvara Dhure।
Tana Kesariya Baago,
Kundala Shravana Pade॥

Om Jai Shri Shyam Hare॥

Gala Pushpon Ki Maala,
Sira Para Mukuta Dhare।
Khevata Dhoopa Agni Para,
Deepaka Jyoti Jale॥

Om Jai Shri Shyam Hare॥

Modaka Kheera Choorama,
Suvarana Thaala Bhare।
Sevaka Bhoga Lagaavata,
Seva Nitya Kare॥

Om Jai Shri Shyam Hare॥

Jhaanjha Katora Aura Ghadiyaawala,
Shankha Mridanga Dhure।
Bhakta Aarti Gaave,
Jaya-Jayakaara Kare॥

Om Jai Shri Shyam Hare॥

Jo Dhyaave Phala Paave,
Saba Duhkha Se Ubare।
Sevaka Jana Nija Mukha Se,
Shri Shyam-Shyam Uchare॥

Om Jai Shri Shyam Hare॥

'Shri Shyam Bihariji' Ki Aarti,
Jo Koee Nara Gaave।
Kahata Bhakta Jana,
Manavaanchhita Phala Paave॥

Om Jai Shri Shyam Hare॥

Tana Mana Dhana Saba Kuchha Hai Tera,
Ho Baba Saba Kuchha Hai Tera।
Tera Tujhako Arpana,
Kya Laage Mera॥

Om Jai Shri Shyam Hare॥

Jai Shri Shyam Hare,
Baba Ji Shri Shyam Hare।
Nija Bhakton Ke Tumane,
Poorana Kaaja Kare॥

Om Jai Shri Shyam Hare॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['khatushyam', 'sants']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_sants_1':
                fg_data[cat_name]['items'][i] = KHATU_SHYAM_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_sants_1 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_sants_1':
                    cdata['items'][i] = KHATU_SHYAM_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_sants_1 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(KHATU_SHYAM_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_sants_1"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_sants_1 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_sants_1 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
