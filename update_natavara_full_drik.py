# -*- coding: utf-8 -*-
"""
Update drik_krishna_4 (आरती कीजै श्रीनटवर जी की / भगवान नटवर आरती) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics
- Verse-by-verse detailed Bhavarth
- 4-2-1-7 Natavara Aarti Vidhi
- Significance (माहात्म्य)
- English Roman Transliteration
- Drik Panchang verified metadata
"""

import json

NATAVARA_DATA = {
    "id": "drik_krishna_4",
    "title": "आरती कीजै श्रीनटवर जी की",
    "title_en": "Lord Natavara Aarti (Aarti Kije Shri Natavara Ji Ki)",
    "en_line": "Aarti Kijai Shri Natavara Ji Ki, Govardhana-Dhara Banshidhara Ki",
    "hi_line": "आरती कीजै श्रीनटवर जी की, गोवर्धन-धर बन्शीधर की",
    "sub": "गोवर्धन-धर बन्शीधर • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_krishna_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ty_BRH3b9lY",
    "video_id": "ty_BRH3b9lY",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-krishna/lord-natavara-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ भगवान नटवर आरती ॥
(आरती कीजै श्रीनटवर जी की)

नन्द-सुवन जसुमतिके लाला, गोधन गोपी प्रिय गोपाला।
देवप्रिय असुरनके काला, मोहन विश्वविमोहन वर की॥

आरती कीजै श्रीनटवर जी की।
गोवर्धन-धर बन्शीधर की॥

जय वसुदेव-देवकी-नन्दन, कालयवन-कन्सादि-निकन्दन।
जगदाधार अजय जगवन्दन, नित्य नवीन परम सुन्दर की॥

आरती कीजै श्रीनटवर जी की।
गोवर्धन-धर बन्शीधर की॥

अकल कलाधर सकल विश्वधर, विश्वम्भर कामद करुणाकर।
अजर, अमर, मायिक, मायाहर, निर्गुन चिन्मय गुणमन्दिर की॥

आरती कीजै श्रीनटवर जी की।
गोवर्धन-धर बन्शीधर की॥

पाण्डव-पूत परीक्षित रक्षक, अतुलित अहि अघ मूषक-भक्षक।
जगमय जगत निरीह निरीक्षक, ब्रह्म परात्पर परमेश्वर की॥

आरती कीजै श्रीनटवर जी की।
गोवर्धन-धर बन्शीधर की॥

नित्य सत्य गोलोकविहारी, अजाव्यक्त लीलावपुधारी।
लीलामय लीलाविस्तारी, मधुर मनोहर राधावर की॥

आरती कीजै श्रीनटवर जी की।
गोवर्धन-धर बन्शीधर की॥

आरती कीजै श्रीनटवर जी की, गोवर्धन-धर बन्शीधर की॥
आरती कीजै श्रीनटवर जी की, गोवर्धन-धर बन्शीधर की॥""",

    "meaning": """॥ भगवान नटवर आरती — पद्यवार सम्पूर्ण पावन भावार्थ ॥

१. मंगलाचरण, बाललीला एवं विश्वमोहन स्वरूप:
"नन्द-सुवन जसुमतिके लाला, गोधन गोपी प्रिय गोपाला।
देवप्रिय असुरनके काला, मोहन विश्वविमोहन वर की॥
आरती कीजै श्रीनटवर जी की। गोवर्धन-धर बन्शीधर की॥"

भावार्थ:
जो नंदबाबा के आत्मज (पुत्र) और माता यशोदा के परम दुलारे लाड़ले हैं, जिन्हें सुरभि गौएं (गोधन) और गोपियां अपने प्राणों से भी अधिक प्रिय हैं, तथा जो समस्त ग्वालबालों के स्नेही गोपाल हैं।
जो समस्त देवगणों के परम प्रिय आराध्य हैं तथा दुष्ट दानवों-असुरों के लिए साक्षात महाकाल स्वरूप हैं; जो स्वयं कामदेव को भी सम्मोहित कर देने वाले विश्वमोहन प्रभु हैं—ऐसे गोवर्धन पर्वत को धारण करने वाले, हाथों में दिव्य बंशी बजाने वाले 'श्रीनटवर' भगवान श्रीकृष्ण की हम भावपूर्ण आरती उतारते हैं।

२. अवतार लीला, कंस-दलन एवं नित्य-नवीन सौंदर्य:
"जय वसुदेव-देवकी-नन्दन, कालयवन-कन्सादि-निकन्दन।
जगदाधार अजय जगवन्दन, नित्य नवीन परम सुन्दर की॥"

भावार्थ:
वसुदेव जी और माता देवकी के पावन कुल को आनंदित करने वाले नंदनन्दन श्रीकृष्ण की जय हो! जिन्होंने कालयवन, दुराचारी कंस और तृणावर्त-बकासुर आदि दुष्ट असुरों का संहार (निकंदन) कर पृथ्वी का भार उतारा।
जो संपूर्ण चराचर ब्रह्मांड के एकमात्र आधार (जगदाधार), अजेय और समस्त लोकों द्वारा वंदनीय (जगवंदन) हैं, जिनका अलौकिक सौंदर्य क्षण-प्रतिक्षण नित्य नूतन व परम चित्ताकर्षक प्रतीत होता है—ऐसे नित्य-नवीन परम सुंदर नटवर प्रभु की हम आरती करते हैं।

३. वेदांत तत्व, निर्गुण-सगुण समन्वय एवं मायापति स्वरूप:
"अकल कलाधर सकल विश्वधर, विश्वम्भर कामद करुणाकर।
अजर, अमर, मायिक, मायाहर, निर्गुन चिन्मय गुणमन्दिर की॥"

भावार्थ:
जो स्वयं कलातीत (अकल) होकर भी समस्त चौंसठ कलाओं के स्वामी (कलाधर) हैं; जो संपूर्ण विश्व को धारण करने वाले, सबका भरण-पोषण करने वाले (विश्वंभर), भक्तों की समस्त सात्विक कामनाओं को पूर्ण करने वाले (कामद) और अपार करुणा के सागर हैं।
जो जन्म-जरा-मृत्यु से रहित अजर और अमर हैं; जो अपनी योगमाया से समस्त लीलाएं रचते हैं (मायिक) और शरणागत भक्तों के अज्ञान व मोह का हरण करने वाले (मायाहर) हैं; जो मूलतः निर्गुण-निराकार व विशुद्ध चिन्मय (चेतन) ब्रह्म होते हुए भी अपने भक्तों के प्रेमवश समस्त दिव्य गुणों के पावन आलय (गुणमंदिर) बने हैं—ऐसे परमब्रह्म नटवर भगवान की हम आरती करते हैं।

४. भक्त-रक्षण एवं परात्पर ब्रह्म महिमा:
"पाण्डव-पूत परीक्षित रक्षक, अतुलित अहि अघ मूषक-भक्षक।
जगमय जगत निरीह निरीक्षक, ब्रह्म परात्पर परमेश्वर की॥"

भावार्थ:
जिन्होंने अश्वत्थामा के ब्रह्मास्त्र से पाण्डव-कुल के एकमात्र वंशधर बालक परीक्षित की माता उत्तरा के गर्भ में साक्षात चक्र सुदर्शन से रक्षा की। जिन्होंने कालिया नाग (अतुलित अहि), अघासुर, बकासुर और समस्त विषधरों-शत्रुओं का मान-मर्दन किया।
जो संपूर्ण संसार में अणु-रेणु में व्याप्त होकर भी स्वयं अनासक्त, निर्लिप्त और साक्षी रूप से सम्पूर्ण सृष्टि के निरीक्षक हैं—ऐसे परात्पर ब्रह्म, जगदीश्वर, सर्वशक्तिमान परमेश्वर नटवर श्रीकृष्ण की हम आरती गाते हैं।

५. गोलोक धाम, लीला-विस्तार एवं श्रीराधा-वर वंदना:
"नित्य सत्य गोलोकविहारी, अजाव्यक्त लीलावपुधारी।
लीलामय लीलाविस्तारी, मधुर मनोहर राधावर की॥"

भावार्थ:
जो नित्य-सत्य, अविनाशी परमधाम गोलोक में नित्य विहार करने वाले हैं; जो अजन्मा और अव्यक्त होते हुए भी केवल अपने भक्तों को आनंद देने हेतु दिव्य लीलावपु (दिव्य चिन्मय देह) धारण करते हैं।
जो अपनी अलौकिक दिव्य लीलाओं का विस्तार कर कोटि-कोटि जीवों का उद्धार करते हैं—ऐसे परम मधुर, मनमोहन, श्री राधारानी के प्राणवल्लभ (राधावर) तथा गोवर्धन पर्वत को धारण करने वाले बंशीधर श्रीनटवर जी की हम बारंबार पावन आरती उतारते हैं।""",

    "vidhi": """॥ श्री नटवर आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधान ॥

भगवान श्रीनटवर (गोवर्धन-धर बंशीधर) की आरती उतारने का विशेष शास्त्रोक्त व वैष्णव नियम:

१. दीप प्रज्वलन व आचमन:
आरती की थाली में शुद्ध देसी घी का पंचमुखी दीपक या कर्पूर प्रज्वलित करें। थाल में पीत पुष्प, तुलसी दल, रोली, चंदन और अक्षत रखें। 'ॐ नमो भगवते वासुदेवाय' का उच्चारण करते हुए मन को स्थिर करें।

२. श्रीचरणों में ४ बार घुमाएं:
सर्वप्रथम आरती की थाल को दक्षिणावर्त (Clockwise) दिशा में भगवान नटवर के पावन चरणकमलों में ४ बार घुमाएं। यह कालिया-दमन करने वाले और गोवर्धन धारण के समय पृथ्वी को थामने वाले दिव्य चरणों की वंदना है।

३. नाभि-कमल पर २ बार घुमाएं:
इसके उपरांत दीपक को प्रभु के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह संपूर्ण जगत के आधार और सृष्टि-उद्गम का नमन है।

४. त्रिभंग मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को भगवान के मुरली-धरे, मंद मुस्कराते त्रिभुवन-मोहन मुखारविन्द के समक्ष १ बार घुमाएं। इससे अविद्या, भ्रम और चित्त के संशय नष्ट होते हैं।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मोरमुकुट-मंडित शीश से लेकर चरणकमलों तक सम्पूर्ण नटवर श्रीविग्रह पर भावपूर्वक ७ बार घुमाएं। यह चौदह भुवनों और सातों लोकों के स्वामी की समग्र परिक्रमा है।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण एवं आरती ग्रहण:
आरती पूर्ण होने पर शंख व घंटी बजाएं, आचमनी से तीन बार जल थाल के चारों ओर घुमाकर देवता को अर्पण करें। दोनों हाथों से आरती का तेज ग्रहण कर शीश व नेत्रों पर लगाएं।""",

    "significance": """॥ भगवान नटवर आरती — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. वेदांत और भक्ति का दिव्य समन्वय:
'आरती कीजै श्रीनटवर जी की' आरती में भगवान श्रीकृष्ण के निर्गुण ब्रह्म, मायिक-मायाहर, गोलोकविहारी और भक्तवत्सल नटवर स्वरूपों का अद्भुत दार्शनिक निरूपण है।

२. समस्त संकटों व काल-भय से रक्षा:
जैसे प्रभु ने कालयवन और कंस का संहार किया तथा गर्भ में परीक्षित की रक्षा की, वैसे ही इस आरती का नित्य पाठ करने वाले साधक की समस्त संकटों, आधि-व्याधियों और अकाल मृत्यु के भय से रक्षा होती है।

३. मोक्ष एवं नित्य गोलोक वास:
यह आरती साधक के हृदय में पराभक्ति का संचार करती है और मृत्यु के उपरांत भगवान श्रीकृष्ण के परम धाम (गोलोक धाम) की प्राप्ति कराती है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छंदों पर आधारित है।""",

    "english_lyrics": """॥ Bhagavan Natavara Aarti ॥
(Aarti Kijai Shri Natavara Ji Ki)

Nanda-Suvana Jasumatike Lala, Godhana Gopi Priya Gopala।
Devapriya Asuranke Kala, Mohana Vishvavimohana Vara Ki॥

Aarti Kijai Shri Natavara Ji Ki।
Govardhana-Dhara Banshidhara Ki॥

Jaya Vasudeva-Devaki-Nandana, Kalayavana-Kansadi-Nikandana।
Jagadadhara Ajaya Jagavandana, Nitya Naveena Parama Sundara Ki॥

Aarti Kijai Shri Natavara Ji Ki।
Govardhana-Dhara Banshidhara Ki॥

Akala Kaladhara Sakala Vishvadhara, Vishvambhara Kamada Karunakara।
Ajara, Amara, Mayika, Mayahara, Nirguna Chinmaya Gunamandira Ki॥

Aarti Kijai Shri Natavara Ji Ki।
Govardhana-Dhara Banshidhara Ki॥

Pandava-Poota Parikshita Rakshaka, Atulita Ahi Agha Mooshaka-Bhakshaka।
Jagamaya Jagata Nireeha Nireekshaka, Brahma Paratpara Parameshvara Ki॥

Aarti Kijai Shri Natavara Ji Ki।
Govardhana-Dhara Banshidhara Ki॥

Nitya Satya Golokavihari, Ajavyakta Leelavapudhari।
Leelamaya Leelavistari, Madhura Manohara Radhavara Ki॥

Aarti Kijai Shri Natavara Ji Ki।
Govardhana-Dhara Banshidhara Ki॥

Aarti Kijai Shri Natavara Ji Ki, Govardhana-Dhara Banshidhara Ki॥
Aarti Kijai Shri Natavara Ji Ki, Govardhana-Dhara Banshidhara Ki॥"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'krishna' in collections and 'items' in collections['krishna']:
    k_items = collections['krishna']['items']
    found = False
    for i, it in enumerate(k_items):
        if it.get('id') == 'drik_krishna_4' or 'नटवर' in it.get('hi_line', '') or 'नटवर' in it.get('title', ''):
            k_items[i] = NATAVARA_DATA
            found = True
            print(f"[OK] Replaced Natavara item at index {i} in JSON")
            break
    if not found:
        k_items.insert(3, NATAVARA_DATA)
        print("[OK] Inserted Natavara item at index 3 in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate drik_krishna_4 in app.js
obj_start = app_js.find('"id": "drik_krishna_4"')
if obj_start != -1:
    brace_start = app_js.rfind('{', 0, obj_start)
    next_obj = app_js.find('"id": "drik_krishna_5"', obj_start)
    if next_obj != -1:
        brace_end = app_js.rfind('}', brace_start, next_obj) + 1
        new_block = json.dumps(NATAVARA_DATA, ensure_ascii=False, indent=8)
        app_js = app_js[:brace_start] + new_block + app_js[brace_end:]
        print("[OK] Successfully replaced drik_krishna_4 block in app.js")
    else:
        print("[WARN] Could not find drik_krishna_5")
else:
    print("[WARN] drik_krishna_4 not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
