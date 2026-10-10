# -*- coding: utf-8 -*-
"""
Update drik_krishna_7 (आरती करत यसोदा प्रमुदित / श्री यशोदालाल आरती) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics
- Verse-by-verse detailed Bhavarth
- 4-2-1-7 Yashodalala Aarti Vidhi
- Significance (माहात्म्य)
- English Roman Transliteration
- Drik Panchang verified metadata
"""

import json

YASHODALALA_DATA = {
    "id": "drik_krishna_7",
    "title": "आरती करत यसोदा प्रमुदित",
    "title_en": "Shri Yashodalala Aarti (Aarti Karata Yasoda Pramudita)",
    "en_line": "Aarati Karata Yasoda Pramudita, Phooli Anga Na Maata",
    "hi_line": "आरति करत यसोदा प्रमुदित, फूली अङ्ग न मात",
    "sub": "मैया यशोदा वात्सल्य आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_krishna_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ty_BRH3b9lY",
    "video_id": "ty_BRH3b9lY",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-krishna/shri-yashodalala-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री यशोदालाल आरती ॥
(आरति करत यसोदा प्रमुदित)

आरति करत यसोदा प्रमुदित, फूली अङ्ग न मात।
बल-बल कहि दुलरावत, आनन्द मगन भई पुलकात॥
आरति करत यसोदा प्रमुदित...॥

सुबरन-थार रत्न-दीपावलि, चित्रित घृत-भीनी बात।
कल सिन्दूर दूब दधि अच्छत, तिलक करत बहु भाँत॥
आरति करत यसोदा प्रमुदित...॥

अन्न चतुर्विध बिबिध भोग, दुन्दुभि बाजत बहु जात।
नाचत गोप कुम्कुमा छिरकत, देत अखिल नगदात॥
आरति करत यसोदा प्रमुदित...॥

बरसत कुसुम निकर सुर-नर-मुनि, व्रजजुवती मुसकात।
कृष्णदास-प्रभु गिरधर को मुख, निरख लजत ससि-काँत॥
आरति करत यसोदा प्रमुदित...॥

आरति करत यसोदा प्रमुदित, फूली अङ्ग न मात।
बल-बल कहि दुलरावत, आनन्द मगन भई पुलकात॥""",

    "meaning": """॥ श्री यशोदालाल आरती — पद्यवार सम्पूर्ण पावन भावार्थ ॥

१. वात्सल्य भाव एवं मैया यशोदा का परमानंद:
"आरति करत यसोदा प्रमुदित, फूली अङ्ग न मात।
बल-बल कहि दुलरावत, आनन्द मगन भई पुलकात॥"

भावार्थ:
माता यशोदा अपने नन्हे लाड़ले कन्हैया (बालगोपाल) की परम प्रसन्नता व वात्सल्य भाव से आरती उतार रही हैं। अपने प्यारे लल्ला के अलौकिक सौंदर्य और मंद मुस्कान को देखकर मैया के हृदय में इतना अपार आनंद उमड़ रहा है कि वह अपने अंगों में समा नहीं पा रहा है (फूली न समाना)।
मैया बारंबार 'बलिहारी जाऊँ, मेरे लल्ला पर न्यौछावर जाऊँ' कहकर कन्हैया को दुलार कर रही हैं, और उनका संपूर्ण शरीर परमानंद में मग्न होकर पुलकित व रोमांचित हो रहा है।

२. स्वर्ण-थाल, रत्न-दीप एवं मंगल-तिलक:
"सुबरन-थार रत्न-दीपावलि, चित्रित घृत-भीनी बात।
कल सिन्दूर दूब दधि अच्छत, तिलक करत बहु भाँत॥"

भावार्थ:
मैया यशोदा ने कन्हैया की आरती हेतु शुद्ध स्वर्ण (सुवर्ण) की थाल सजाई है, जिसमें मणियों और रत्नों से अलंकृत दीपकों की कतारें (दीपावली) जगमगा रही हैं तथा शुद्ध देशी गाय के घी से भीगी हुई बत्तियां मंद-मंद जल रही हैं।
मैया अपने लाड़ले को बुरी नजर और विघ्नों से बचाने हेतु पवित्र सिन्दूर, हरी दूर्वा (दूब), ताजा दही और अक्षत (चावल) का मिश्रण लेकर उसके सुंदर ललाट पर विविध प्रकार से मंगल तिलक कर रही हैं।

३. छप्पन-भोग, वाद्य-नाद एवं ग्वालों का उल्लास:
"अन्न चतुर्विध बिबिध भोग, दुन्दुभि बाजत बहु जात।
नाचत गोप कुम्कुमा छिरकत, देत अखिल नगदात॥"

भावार्थ:
ठाकुर जी के सम्मुख चार प्रकार के अन्न—चर्व्य (चबाकर खाने योग्य), चोष्य (चूसने योग्य), लेह्य (चाटने योग्य) और पेय (पीने योग्य)—सहित विविध प्रकार के स्वादिष्ट व्यंजनों का छप्पन-भोग लगाया गया है; और नंदभवन में अनेक जातियों के मंगल दुंदुभि, मृदंग व ढोलक बज रहे हैं।
समस्त ग्वाल-गोप आनंद में भरकर नाच रहे हैं, एक-दूसरे पर सुगंधित कुमकुम और गुलाल छिड़क रहे हैं, तथा लल्ला की दीर्घायु और मंगल की कामना करते हुए याचकों और संतों को खुले हाथों से वस्त्र, गोधन व नकद दान (नगदात) लुटा रहे हैं।

४. देव-पुष्पवृष्टि, गोपी-मुस्कान एवं चंद्र-लज्जा:
"बरसत कुसुम निकर सुर-नर-मुनि, व्रजजुवती मुसकात।
कृष्णदास-प्रभु गिरधर को मुख, निरख लजत ससि-काँत॥"

भावार्थ:
आकाश से देवता, यक्ष, गंधर्व और मुनिगण बालगोपाल के इस पावन दर्शन पर पुष्पों के अपार समूहों की वर्षा कर रहे हैं, और ब्रज की गोपांगनाएं (ब्रज-युवतियां) प्रेम-विह्वल होकर मंद-मंद मुस्कुरा रही हैं।
अष्टछाप के अनन्य संत-कवि कृष्णदास जी कहते हैं कि गोवर्धन पर्वत को धारण करने वाले मेरे आराध्य प्रभु 'गिरिधर' के परम सुंदर मुखारविन्द की अलौकिक कांति को देखकर शरद पूर्णिमा का चंद्रमा और चंद्रकांत मणि भी लज्जित हो जाते हैं। ऐसी पावन वात्सल्यमयी यशोदालाल आरती का हम भाव-विभोर होकर गान करते हैं।""",

    "vidhi": """॥ श्री यशोदालाल आरती — शास्त्रोक्त व पुष्टिमार्गीय 4-2-1-7 दीप विधान ॥

मैया यशोदा के वात्सल्य भाव से बालगोपाल की आरती उतारने का विशेष शास्त्रोक्त एवं पुष्टिमार्गीय विधान:

१. दीप प्रज्वलन व थाल सज्जा:
स्वर्ण, चांदी अथवा पीतल की थाल में शुद्ध गाय के घी का पंचमुखी दीपक या कर्पूर प्रज्वलित करें। थाल में ताजा दही, दूर्वा, सिन्दूर, अक्षत, माखन-मिश्री का भोग और पीले पुष्प रखें। वात्सल्य भाव से 'ॐ नमो भगवते वासुदेवाय' का स्मरण करें।

२. चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में नन्हे कन्हैया के दोनों कोमल चरणकमलों में ४ बार घुमाएं। यह घुटनों के बल चलकर ब्रज की गलियों को पावन करने वाले चरणों की वंदना है।

३. नाभि-कमल पर २ बार घुमाएं:
इसके उपरांत दीपक को बालगोपाल के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह चराचर ब्रह्मांड के सृजन केंद्र का वात्सल्य नमन है।

४. मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को माखन-लगे, मंद मुस्कराते मुखारविन्द के समक्ष १ बार घुमाएं। इससे बालक की नजर उतरती है और समस्त अज्ञान व नकारात्मक शक्तियों का नाश होता है।

५. सम्पूर्ण विग्रह (सर्वांग) पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मोरपंखी-मंडित मस्तक से लेकर चरणकमलों तक सम्पूर्ण बालगोपाल विग्रह पर भावपूर्वक ७ बार घुमाएं। यह सातों लोकों के स्वामी की समग्र परिक्रमा और रक्षा-कवच है।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, तिलक एवं आरती ग्रहण:
आरती पूर्ण होने पर आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। कन्हैया को सिन्दूर, दही व अक्षत का रक्षा-तिलक करें। दोनों हाथों से आरती का तेज ग्रहण कर शीश व नयनों पर लगाएं।""",

    "significance": """॥ श्री यशोदालाल आरती — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. वात्सल्य रस की सर्वोत्कृष्ट आरती:
अष्टछाप के संत कृष्णदास जी द्वारा विरचित यह आरती पुष्टि-मार्ग और ब्रज-संस्कृति में वात्सल्य भाव की सर्वोच्च आरती मानी जाती है। इसमें माता यशोदा के निष्काम मातृत्व प्रेम का साक्षात अनुभव होता है।

२. बाल-रक्षा एवं संतान सुख:
इस आरती का नित्य गान या श्रवण करने से घर के बच्चों की बुरी नजर, अकाल भय और रोगों से रक्षा होती है। निःसंतान दंपत्तियों को सुयोग्य, संस्कारी और दीर्घायु संतान की प्राप्ति होती है।

३. गृह में आनंद और सुख-शांति का संचार:
"आनन्द मगन भई पुलकात"—जिस घर में नित्य यशोदालाल आरती का गान होता है, वहां का वातावरण नंदभवन के समान सदा प्रफुल्लित, क्लेश-मुक्त और सुख-समृद्धि से परिपूर्ण रहता है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक ब्रजभाषा छंदों पर आधारित है।""",

    "english_lyrics": """॥ Shri Yashodalala Aarti ॥
(Aarti Karata Yasoda Pramudita)

Aarati Karata Yasoda Pramudita, Phooli Anga Na Maata।
Bala-Bala Kahi Dularavata, Aananda Magana Bhai Pulakaata॥
Aarati Karata Yasoda Pramudita...॥

Subarana-Thaara Ratna-Deepavali, Chotrita Ghrita-Bheeni Baata।
Kala Sindoora Dooba Dadhi Achhhata, Tilaka Karata Bahu Bhaanta॥
Aarati Karata Yasoda Pramudita...॥

Anna Chaturvidha Bibidha Bhoga, Dundubhi Baajata Bahu Jaata।
Naachata Gopa Kumkuma Chhirakata, Deta Akhila Nagadaata॥
Aarati Karata Yasoda Pramudita...॥

Barasata Kusuma Nikara Sura-Nara-Muni, Vrajajuvati Musakaata।
Krishnadasa-Prabhu Giradhara Ko Mukha, Nirakha Lajaata Sasi-Kaanta॥
Aarati Karata Yasoda Pramudita...॥

Aarati Karata Yasoda Pramudita, Phooli Anga Na Maata।
Bala-Bala Kahi Dularavata, Aananda Magana Bhai Pulakaata॥"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'krishna' in collections and 'items' in collections['krishna']:
    k_items = collections['krishna']['items']
    found = False
    for i, it in enumerate(k_items):
        if it.get('id') == 'drik_krishna_7' or 'यसोदा' in it.get('hi_line', '') or 'यशोदा' in it.get('title', ''):
            k_items[i] = YASHODALALA_DATA
            found = True
            print(f"[OK] Replaced Yashodalala item at index {i} in JSON")
            break
    if not found:
        k_items.insert(6, YASHODALALA_DATA)
        print("[OK] Inserted Yashodalala item at index 6 in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate drik_krishna_7 in app.js
obj_start = app_js.find('"id": "drik_krishna_7"')
if obj_start != -1:
    brace_start = app_js.rfind('{', 0, obj_start)
    # drik_krishna_7 is the last item in krishna items, find the closing of this item before ]
    # which is right before "    ]\n  },"
    rama_start = app_js.find('"rama": {', obj_start)
    if rama_start != -1:
        # find the closing brace of drik_krishna_7 before the closing bracket of items
        bracket_end = app_js.rfind(']', obj_start, rama_start)
        brace_end = app_js.rfind('}', obj_start, bracket_end) + 1
        new_block = json.dumps(YASHODALALA_DATA, ensure_ascii=False, indent=8)
        app_js = app_js[:brace_start] + new_block + app_js[brace_end:]
        print("[OK] Successfully replaced drik_krishna_7 block in app.js")
    else:
        print("[WARN] Could not find rama collection to delimit block")
else:
    print("[WARN] drik_krishna_7 not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
