# -*- coding: utf-8 -*-
"""
Update drik_gods_12 (Lord Bhairava Aarti / सुनो जी भैरव लाड़िले) in:
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

BHAIRAVA_DATA = {
    "id": "drik_gods_12",
    "title": "सुनो जी भैरव लाड़िले",
    "title_en": "Lord Bhairava Aarti (Suno Ji Bhairava Ladile)",
    "en_line": "Suno Ji Bhairava Ladile, Kara Joda Kara Vinati Karoon",
    "hi_line": "सुनो जी भैरव लाड़िले, कर जोड़ कर विनती करूँ",
    "sub": "रुद्रावतार काशी व मेंहदीपुर कोतवाल भैरव जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_bhairav_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=xcVv68gwc5Y",
    "video_id": "xcVv68gwc5Y",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-bhairava/shri-bhairava-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री भैरव आरती ॥
(सुनो जी भैरव लाड़िले)

सुनो जी भैरव लाड़िले,
कर जोड़ कर विनती करूँ।
कृपा तुम्हारी चाहिए,
मैं ध्यान तुम्हारा ही धरूँ।
मैं चरण छुता आपके,
अर्जी मेरी सुन लीजिये॥

सुनो जी भैरव लाड़िले...॥

मैं हूँ मति का मन्द,
मेरी कुछ मदद तो कीजिये।
महिमा तुम्हारी बहुत,
कुछ थोड़ी सी मैं वर्णन करूँ॥

सुनो जी भैरव लाड़िले...॥

करते सवारी स्वान की,
चारों दिशा में राज्य है।
जितने भूत और प्रेत,
सबके आप ही सरताज हैं॥

सुनो जी भैरव लाड़िले...॥

हथियार हैं जो आपके,
उसका क्या वर्णन करूँ।
माता जी के सामने तुम,
नृत्य भी करते सदा॥

सुनो जी भैरव लाड़िले...॥

गा गा के गुण अनुवाद से,
उनको रिझाते हो सदा।
एक सांकली है आपकी,
तारीफ उसकी क्या करूँ॥

सुनो जी भैरव लाड़िले...॥

बहुत सी महिमा तुम्हारी,
मेंहदीपुर सरनाम है।
आते जगत के यात्री,
बजरंग का स्थान है॥

सुनो जी भैरव लाड़िले...॥

श्री प्रेतराज सरकार के,
मैं शीश चरणों में धरूँ।
निशदिन तुम्हारे खेल से,
माताजी खुश रहें॥

सुनो जी भैरव लाड़िले...॥

सिर पर तुम्हारे हाथ रख कर,
आशीर्वाद देती रहें।
कर जोड़ कर विनती करूँ,
अरु शीश चरणों में धरूँ॥

सुनो जी भैरव लाड़िले...॥""",
    "meaning": """॥ श्री भैरव आरती (सुनो जी भैरव लाड़िले) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती देवाधिदेव भगवान शिव के तेजस्वी रुद्रावतार, काशी के कोतवाल तथा मेंहदीपुर बालाजी धाम के प्रधान रक्षक श्री बटुक/बाल भैरव जी की वंदना में गाई जाती है। समस्त तांत्रिक, वैदिक संकटों और नकारात्मक शक्तियों के निवारण हेतु इस आरती का नित्य सांध्य गायन अत्यंत फलदायी है।)

१. प्रथम पद (करबद्ध प्रार्थना, शरणागति व दया-याचना):
"सुनो जी भैरव लाड़िले, कर जोड़ कर विनती करूँ।
कृपा तुम्हारी चाहिए, मैं ध्यान तुम्हारा ही धरूँ।
मैं चरण छुता आपके, अर्जी मेरी सुन लीजिये॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे देवाधिदेव महादेव व आदिशक्ति माँ भगवती के परम लाड़िले बाल रूप भैरव देव! मैं दोनों हाथ जोड़कर अत्यंत दीन भाव से आपके सम्मुख प्रार्थना करता हूँ। मुझे केवल आपकी अहैतुकी कृपा चाहिए, मैं अनन्य भाव से आपके ही तेजस्वी स्वरूप का ध्यान करता हूँ। हे करुणामय नाथ! मैं आपके पावन श्रीचरणों का स्पर्श करता हूँ, कृपया मेरी यह दीन पुकार (अर्जी) सुनकर मुझ पर अपनी अनुकंपा कीजिए।

२. द्वितीय पद (अल्पमति की दीनता व महिमा-गान का प्रयास):
"मैं हूँ मति का मन्द, मेरी कुछ मदद तो कीजिये।
महिमा तुम्हारी बहुत, कुछ थोड़ी सी मैं वर्णन करूँ॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे दयालु प्रभु! मैं बुद्धि से मंद, अज्ञानी और सांसारिक माया-मोह में फंसा हुआ एक साधारण जीव हूँ। कृपया आप आगे बढ़कर मेरी सहायता कीजिए और मुझे सन्मार्ग प्रदान कीजिए। आपकी दिव्य महिमा तो अनंत, अगाध और वेदों द्वारा भी अनिर्वचनीय है, फिर भी अपनी तुच्छ बुद्धि से मैं आपके पावन गुणों का थोड़ा-सा यशोगान करने का विनम्र प्रयास कर रहा हूँ।

३. तृतीय पद (श्वान-सवारी, सर्वदिक्-साम्राज्य व भूत-प्रेत अधिपति):
"करते सवारी स्वान की, चारों दिशा में राज्य है।
जितने भूत और प्रेत, सबके आप ही सरताज हैं॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे भैरव नाथ! आप निष्ठावान श्वान (काले श्वान) की दिव्य सवारी करते हैं और दसों दिशाओं तथा चारों लोकों में आपका ही एकछत्र न्याय व साम्राज्य प्रतिष्ठित है। संसार में जितने भी भूत, प्रेत, पिशाच, बेताल, डाकिनी, शाकिनी और तामसी उपद्रवी तत्व हैं, आप उन सबके सर्वोपरि अधिपति (सरताज) व नियंत्रक हैं। आपकी आज्ञा के बिना कोई भी अनिष्टकारी शक्ति किसी का अहित नहीं कर सकती।

४. चतुर्थ पद (दिव्य अस्त्र-शस्त्र व माँ भगवती के सम्मुख आनंद-नृत्य):
"हथियार हैं जो आपके, उसका क्या वर्णन करूँ।
माता जी के सामने तुम, नृत्य भी करते सदा॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे प्रभु! आपके करकमलों में सुशोभित दिव्य त्रिशूल, खप्पर, दंड और पाश जैसे भयंकर व पाप-संहारक आयुधों के तेज का वर्णन करने में कोई भी समर्थ नहीं है। एक ओर जहाँ आप दुष्टों और असुरों के लिए साक्षात काल-स्वरूप हैं, वहीं दूसरी ओर आप परम करुणामयी आदिशक्ति माँ जगदम्बा के सम्मुख परम वात्सल्य और आनंद से भरकर नित्य मनोहर नृत्य करते हैं।

५. पंचम पद (गुणानुवाद, माँ को रिझाना व चमत्कारी लोह-सांकली):
"गा गा के गुण अनुवाद से, उनको रिझाते हो सदा।
एक सांकली है आपकी, तारीफ उसकी क्या करूँ॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे लाड़िले! आप मधुर गुणानुवाद गा-गाकर और अगाध भक्ति-भाव से जगज्जननी माँ भगवती को सर्वदा प्रसन्न व मुदित रखते हैं। आपके पावन धाम में संकट-निवारण हेतु स्थापित वह दिव्य लोह-सांकली (संकटमोचक जंजीर) इतनी चमत्कारी है कि उसकी महिमा का बखान शब्दों में नहीं किया जा सकता। जो भी पीड़ित व्यक्ति उस पावन सांकली का स्पर्श या शरण लेता है, उसके समस्त रोग, शोक और बंधन तत्क्षण कट जाते हैं।

६. षष्ठ पद (मेंहदीपुर बालाजी धाम, जगत के यात्री व बजरंगबली का सान्निध्य):
"बहुत सी महिमा तुम्हारी, मेंहदीपुर सरनाम है।
आते जगत के यात्री, बजरंग का स्थान है॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे नाथ! आपकी महिमा संपूर्ण चराचर में व्याप्त है, किंतु राजस्थान के पावन धाम 'मेंहदीपुर' में आपका नाम सर्वोच्च कोतवाल के रूप में प्रसिद्ध व जाग्रत है। संपूर्ण संसार के कोने-कोने से व्याधिग्रस्त, संकटग्रस्त और पीड़ित यात्री आपके पावन दरबार में आते हैं। यह धाम साक्षात संकटमोचन वीर बजरंगबली (श्री बालाजी महाराज) का स्थान है, जहाँ आप प्रधान कोतवाल के रूप में न्याय करते हैं।

७. सप्तम पद (श्री प्रेतराज सरकार वंदन, दिव्य खेल व माता की प्रसन्नता):
"श्री प्रेतराज सरकार के, मैं शीश चरणों में धरूँ।
निशदिन तुम्हारे खेल से, माताजी खुश रहें॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे भैरव बाबा! मेंहदीपुर दरबार में विराजित श्री प्रेतराज सरकार के पावन चरणों में भी मैं अपना मस्तक झुकाकर श्रद्धापूर्वक प्रणाम करता हूँ। आपके इस जाग्रत दरबार में जो नित्य न्याय, संकट-निवारण और कृपा का दिव्य खेल (लीला) चलता है, उससे साक्षात माँ भगवती जगदम्बा अत्यंत प्रसन्न और संतुष्ट रहती हैं।

८. अष्टम पद (वरदहस्त का आशीर्वाद, करबद्ध विनती व पूर्ण समर्पण):
"सिर पर तुम्हारे हाथ रख कर, आशीर्वाद देती रहें।
कर जोड़ कर विनती करूँ, अरु शीश चरणों में धरूँ॥
सुनो जी भैरव लाड़िले...॥"
भावार्थ: हे बाल भैरव! माँ भगवती सदैव आपके मस्तक पर अपना वरदहस्त रखकर आपको अखंड वात्सल्य और सामर्थ्य का आशीर्वाद प्रदान करती हैं। हम सभी भक्तजन दोनों हाथ जोड़कर आपके पावन चरणों में बारंबार शीश नवाते हैं और आपसे भय-मुक्ति, सर्वकल्याण और अपनी भक्ति का वरदान मांगते हैं।""",
    "vidhi": """॥ श्री भैरव जी की आरती — मेंहदीपुर धाम व काशी कोतवाल शास्त्रोक्त 4-2-1-7 विधान ॥

रुद्रावतार श्री भैरव नाथ जी की आरती उतारने का विशेष शास्त्रोक्त एवं संकट-निवारक विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
सरसों के तेल, चमेली के तेल अथवा शुद्ध गाय के घी का चौमुखी दीपक प्रज्वलित करें। धूप (गुग्गल, लोबान अथवा कर्पूर) सुलगाएं। थाली में सिंदूर, चमेली का तेल, उड़द की दाल के वड़े, इमरती या जलेबी, बेसन के लड्डू, कलावा, मदार/आक के पुष्प, आक की माला और नींबू अर्पित करें।

२. आरती घुमाने का विशेष तांत्रिक व वैदिक '४-२-१-७' क्रम:
आरती को केवल सामान्य रूप से नहीं, अपितु भैरव रक्षा-चक्र के अनुसार '४-२-१-७' क्रम में घुमाएं:
• श्रीचरणों के समक्ष ४ बार: चारों दिशाओं से रक्षा, तामसी शक्तियों के शमन तथा चार पुरुषार्थों (धर्म, अर्थ, काम, मोक्ष) की प्राप्ति हेतु।
• नाभि मंडल के समक्ष २ बार: उदर-विकार, मानसिक भय, असाध्य रोग तथा नाभि-चक्र (मणिपूर चक्र) की शुद्धि हेतु।
• मुखारविंद के समक्ष १ बार: भैरव देव के तीक्ष्ण व सौम्य दर्शन, दृष्टि-दोष निवारण तथा अकाल मृत्यु के भय से मुक्ति हेतु।
• समग्र विग्रह के समक्ष ७ बार: दसों दिशाओं, सप्त धातुओं और सातों चक्रों से समस्त नकारात्मक, ऊपरी व तांत्रिक बाधाओं के निष्कासन हेतु गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की रक्षा व संपूर्ण भैरव प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष भैरव रक्षा मंत्र:
आरती आरंभ करने से पूर्व 'ॐ भ्रं भैरवाय नमः' अथवा 'ॐ ह्रीं बटुकाय आपदुद्धारणाय कुरु कुरु बटुकाय ह्रीं ॐ नमः शिवाय' मन्त्र का स्मरण करें।

४. आरती उपरांत झाड़ा, तिलक व रक्षा-सूत्र:
आरती पूर्ण होने पर भैरव जी के चरणों से सिंदूर लेकर मस्तक या कंठ पर तिलक लगाएं। आरती की ज्योति का स्पर्श कर मस्तक से लगाएं तथा उपस्थित भक्तों में उड़द के बड़े या बूंदी/इमरती का प्रसाद वितरित करें।""",
    "significance": """॥ श्री भैरव आरती (सुनो जी भैरव लाड़िले) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'भय हरति इति भैरवः' — समस्त भयों का समूल नाश:
'भैरव' शब्द का अर्थ ही है समस्त भयों का हरण करने वाला। भगवान भैरव साक्षात देवाधिदेव महादेव के अत्यंत तेजस्वी व कृपालु रुद्रावतार हैं। इस आरती के श्रवण व गान से अकाल मृत्यु, दुर्घटना, भूत-प्रेत बाधा, तंत्र-मंत्र और शत्रुओं का भय तत्काल समाप्त हो जाता है।

२. काशी व मेंहदीपुर के कोतवाल (परम न्याय के अधिपति):
भगवान कालभैरव काशी के कोतवाल हैं और मेंहदीपुर बालाजी धाम में श्री बाल/बटुक भैरव के रूप में दुष्ट शक्तियों का दमन व न्याय करते हैं। इस आरती का नित्य पाठ करने से जीवन के बड़े से बड़े विवाद, शत्रु-बाधा, झूठे मुकदमों और गृह-क्लेश से मुक्ति मिलती है।

३. राहु-केतु व शनि दोषों का तत्काल शमन:
ज्योतिष शास्त्र के अनुसार भैरव जी की नित्य उपासना व आरती से राहु-केतु के सर्प-दोष, नजर-दोष तथा शनि देव की साढ़ेसाती व ढैया के कुप्रभाव पूर्णतः शांत हो जाते हैं और जीवन में स्थिरता आती है।

४. माँ भगवती की त्वरित वात्सल्य कृपा:
चूँकि भैरव जी माँ भगवती के परम लाड़िले और अंगरक्षक हैं, अतः भैरव जी की आरती करने से माँ दुर्गा, काली, कामाख्या और वैष्णो देवी की अमोघ कृपा स्वतः ही प्राप्त हो जाती है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक आठ छंद पदों पर पूर्णतः आधारित है, जो मेंहदीपुर बालाजी धाम और काशी के भैरव मंदिरों में नित्य सांध्य महाआरती में गाई जाती है।""",
    "english_lyrics": """॥ Shri Bhairava Aarti ॥
(Suno Ji Bhairava Ladile)

Suno Ji Bhairava Ladile,
Kara Joda Kara Vinati Karoon।
Kripa Tumhari Chahiye,
Main Dhyana Tumhara Hee Dharoon।
Main Charana Chhoota Aapke,
Arjee Meree Suna Leejiye॥

Suno Ji Bhairava Ladile...॥

Main Hoon Mati Ka Manda,
Meree Kuchha Madada To Keejiye।
Mahima Tumhari Bahuta,
Kuchha Thodee See Main Varnana Karoon॥

Suno Ji Bhairava Ladile...॥

Karate Savaree Swana Kee,
Charon Disha Mein Raajya Hai।
Jitane Bhoota Aura Preta,
Sabake Aapa Hee Sarataaja Hain॥

Suno Ji Bhairava Ladile...॥

Hathiyara Hain Jo Aapke,
Usaka Kya Varnana Karoon।
Mata Ji Ke Samane Tuma,
Nritya Bhee Karate Sada॥

Suno Ji Bhairava Ladile...॥

Ga Ga Ke Guna Anuvada Se,
Unako Rijhate Ho Sada।
Eka Saankalee Hai Aapkee,
Taareefa Usakee Kya Karoon॥

Suno Ji Bhairava Ladile...॥

Bahuta See Mahima Tumhari,
Mehandeepura Saranama Hai।
Aate Jagata Ke Yatri,
Bajaranga Ka Sthana Hai॥

Suno Ji Bhairava Ladile...॥

Shri Pretaraja Sarakara Ke,
Main Sheesha Charanon Mein Dharoon।
Nishadina Tumhare Khela Se,
Mataji Khusha Rahen॥

Suno Ji Bhairava Ladile...॥

Sira Para Tumhare Hatha Rakha Kara,
Aasheervada Detee Rahen।
Kara Joda Kara Vinati Karoon,
Aru Sheesha Charanon Mein Dharoon॥

Suno Ji Bhairava Ladile...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['bhairav', 'gods']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_gods_12':
                fg_data[cat_name]['items'][i] = BHAIRAVA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_gods_12 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_gods_12':
                    cdata['items'][i] = BHAIRAVA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_gods_12 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(BHAIRAVA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_gods_12"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_gods_12 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_gods_12 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
