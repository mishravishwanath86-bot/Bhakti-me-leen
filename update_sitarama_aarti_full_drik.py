# -*- coding: utf-8 -*-
"""
Update drik_rama_4 (श्री सीताराम आरती / गाओ गाओ री, प्रियाप्रीतम की आरती) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics (all 4 stanzas + tek/refrain)
- Verse-by-verse detailed Bhavarth (सखी-भाव युगल माधुर्य)
- 4-2-1-7 Shri Sitarama Aarti Vidhi
- Significance (माहात्म्य व फलश्रुति)
- English Roman Transliteration
- Drik Panchang verified metadata (Video ID: ty_BRH3b9lY)
"""

import json

SITARAMA_DATA = {
    "id": "drik_rama_4",
    "title": "गाओ गाओ री, प्रियाप्रीतम की आरती",
    "title_en": "Shri Sitarama Aarti (Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao)",
    "en_line": "Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao, Aas-Paas Sakhiyan Sukha Daini",
    "hi_line": "गाओ गाओ री, प्रियाप्रीतम की आरती गाओ, आसपास सखियाँ सुख दैनी",
    "sub": "श्री सीताराम युगल सरकार की मधुर आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_rama.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ty_BRH3b9lY",
    "video_id": "ty_BRH3b9lY",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shree-rama/shri-sitarama-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री सीताराम आरती ॥
(गाओ गाओ री, प्रियाप्रीतम की आरती)

गाओ गाओ री, प्रियाप्रीतम की आरती गाओ।
गाओ गाओ री, प्रियाप्रीतम की आरती गाओ॥

आसपास सखियाँ सुख दैनी,
सजि नव साज सिन्गार सुनैनी,
बीन सितार लिएँ पिकबैनी,
गाइ सुराग सुनाओ॥
गाओ गाओ री, प्रियाप्रीतम की आरती गाओ॥

अनुपम छबि धरि दन्पति राजत,
नील पीत पट भूषन भ्राजत,
निरखत अगनित रति छबि लाजत,
नैनन को फल पाओ॥
गाओ गाओ री, प्रियाप्रीतम की आरती गाओ॥

नीरज नैन चपल चितवनमें,
रुचिर अरुनिमा सुचि अधरनमें,
चन्द्रबदन की मधु मुसकनमें,
निज नयनाँ अरुझाओ॥
गाओ गाओ री, प्रियाप्रीतम की आरती गाओ॥

कंचन थार सँवारि मनोहर,
घृत कपूर सुभ बाति ज्योतिकर,
मुरछल चवँर लिएँ रामेस्वर,
हरषि सुमन बरसाओ॥
गाओ गाओ री, प्रियाप्रीतम की आरती गाओ॥""",

    "meaning": """॥ श्री सीताराम आरती (गाओ गाओ री, प्रियाप्रीतम की आरती) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह पावन आरती मिथिला एवं अवध धाम की सखी-भाव उपासना परंपरा में साक्षात् युगल सरकार श्री सीता-राम जी के मधुर शृंगारिक दर्शन की दिव्य आरती है।)

१. टेक एवं मंगलाचरण:
"गाओ गाओ री, प्रियाप्रीतम की आरती गाओ।
गाओ गाओ री, प्रियाप्रीतम की आरती गाओ॥"

भावार्थ:
हे सखियों! आओ मिलकर अपने नयनाभिराम, प्राणवल्लभ युगल सरकार श्री किशोरी जी एवं श्री राघवेंद्र सरकार (प्रिया-प्रीतम) की परम पावन और मंगलमयी आरती का मधुर गान करें।

२. सखियों का शृंगार, वीणा-सितार एवं राग-गान:
"आसपास सखियाँ सुख दैनी,
सजि नव साज सिन्गार सुनैनी,
बीन सितार लिएँ पिकबैनी,
गाइ सुराग सुनाओ॥"

भावार्थ:
युगल सरकार के चारों ओर परम आनंद और सुख प्रदान करने वाली जनकपुर व अवध की प्रिय सखियां उपस्थित हैं। वे सुंदर नयनों वाली सखियां (सुनैनी) नवीन वस्त्र-आभूषणों से दिव्य शृंगार सजाए हुए हैं। कोयल जैसी मीठी वाणी बोलने वाली (पिकबैनी) सखियां अपने हाथों में वीणा और सितार लेकर दिव्य सुर और राग-रागिनियों में युगल प्रभु का यशोगान कर रही हैं। हे सखियों! तुम भी इस मधुर गान में सम्मिलित होकर प्रिया-प्रीतम को रिझाओ।

३. अनुपम युगल छबि, नील-पीत पट एवं रति-मदन लावण्य:
"अनुपम छबि धरि दन्पति राजत,
नील पीत पट भूषन भ्राजत,
निरखत अगनित रति छबि लाजत,
नैनन को फल पाओ॥"

भावार्थ:
साक्षात् महाभाव स्वरूपा श्री किशोरी जी (सीता जी) और रघुकुल शिरोमणि श्री रामचंद्र जी—यह दिव्य युगल दंपत्ति अनुपम अलौकिक छवि धारण किए हुए सिंहासन पर सुशोभित हैं। माता सीता के श्रीअंगों पर नील पट्टिका (नीली साड़ी) और प्रभु श्री राम के श्रीअंगों पर दिव्य पीत पीतांबर व रत्नजटित आभूषण दैदीप्यमान हैं। जिनकी दिव्य सुंदरता को देखकर अनगिनत कामदेव और रति का सौंदर्य भी लज्जित हो जाता है। हे सखियों! इस अलौकिक युगल रूप के दर्शन करके अपने मानव नेत्रों का परम फल प्राप्त करो।

४. कमल-नयन, चपल चितवन, अरुण अधर एवं मंद मुस्कान:
"नीरज नैन चपल चितवनमें,
रुचिर अरुनिमा सुचि अधरनमें,
चन्द्रबदन की मधु मुसकनमें,
निज नयनाँ अरुझाओ॥"

भावार्थ:
जिनके दोनों नयन कमल के सदृश विशाल व कोमल हैं (नीरज नैन) और जिनकी प्रेम-भरी चितवन अत्यंत चपल व मनमोहक है। जिनके पवित्र अधरों पर प्राकृतिक मनोरम रक्तिमा (अरुणिमा) सुशोभित है। और जिनके चंद्रमा के समान शीतल मुखारविन्द पर अमृतमयी मधुर मंद-मंद मुस्कान खिली हुई है—हे मन और सखियों! अपने दोनों नेत्रों को प्रिया-प्रीतम की इस दिव्य माधुरी में सदा के लिए उलझा लो (लीन कर लो)।

५. स्वर्ण-थाल, कर्पूर-ज्योति, चँवर-सेवा एवं पुष्प-वर्षा:
"कंचन थार सँवारि मनोहर,
घृत कपूर सुभ बाति ज्योतिकर,
मुरछल चवँर लिएँ रामेस्वर,
हरषि सुमन बरसाओ॥"

भावार्थ:
सोने की थाली (कंचन थार) को सुंदर सुगंधित द्रव्यों, कुमकुम, अक्षत से सजाकर, उसमें शुद्ध गाय के घी और कर्पूर की शुभ बत्तियों की दिव्य ज्योति प्रज्वलित करो। मोरपंख के मुरछल और कस्तूरी-सुगंधित चँवर डुलाते हुए युगल प्रभु रामेश्वर की वंदना करो, तथा हृदय में असीम हर्ष और उल्लास भरकर आकाश से सुर-वृंदों के साथ युगल सरकार के चरणों में सुरभित पुष्पों की वर्षा करो।""",

    "vidhi": """॥ श्री सीताराम युगल आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधान ॥

युगल सरकार (श्री सीता-राम जी) की आरती उतारने का विशेष शास्त्रोक्त एवं मधुर विधान:

१. दीप प्रज्वलन व आचमन:
स्वर्ण, पीतल अथवा चांदी की थाली में शुद्ध गाय के घी का दीपक या कर्पूर प्रज्वलित करें। थाल में पीत व रक्त पुष्प, तुलसी दल, रोली, चंदन, अक्षत और सुगंधित इत्र रखें। 'ॐ श्री सीता-रामाभ्यां नमः' का ध्यान करें।

२. युगल चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में श्री किशोरी जी एवं प्रभु श्री राम के कोमल चरणकमलों में भावपूर्वक ४ बार घुमाएं। यह युगल चरणों में सर्वस्व समर्पण की वंदना है।

३. नाभि-कमल पर २ बार घुमाएं:
इसके उपरांत दीपक को युगल सरकार के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह त्रिभुवन के आधार और दिव्य माधुर्य का नमन है।

४. युगल मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को माता सीता व भगवान श्री राम के मंद-मंद मुस्कराते दोनों मुखकमलों के समक्ष १ बार घुमाएं। इससे काम-क्रोध मिटकर मन में दिव्य प्रेम की ज्योति जगती है।

५. सम्पूर्ण युगल विग्रह पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मुकुट से लेकर चरणों तक सम्पूर्ण युगल विग्रह पर भावपूर्वक ७ बार घुमाएं। 

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. चँवर-सेवा, पुष्प-वर्षा एवं आरती ग्रहण:
आरती पूर्ण होने पर चँवर डुलाएं, युगल विग्रह पर पुष्प बरसाएं। आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती का पावन ताप ग्रहण कर शीश व नेत्रों पर लगाएं तथा 'सियावर रामचंद्र की जय, जानकी माता की जय' का जयघोष करें।""",

    "significance": """॥ गाओ गाओ री, प्रियाप्रीतम की आरती — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. युगल माधुर्य एवं सखी-भाव उपासना की सर्वोच्च आरती:
यह आरती मिथिला व अवध की सखी-परंपरा में साक्षात् युगल सरकार (श्री सीताराम जी) के नित्य-विहार दर्शन का रसपान कराती है।

२. दांपत्य सुख एवं अखंड सौभाग्य की प्राप्ति:
"नील पीत पट भूषन भ्राजत"—इस आरती का नित्य भावपूर्वक गायन करने से दांपत्य जीवन में परस्पर अनुराग, सुख, शांति और परिवार में अखंड सौभाग्य की वृद्धि होती है।

३. काम-वासना का दिव्य प्रेम में रूपांतरण:
"निरखत अगनित रति छबि लाजत"—प्रिया-प्रीतम के इस अनुपम स्वरूप का ध्यान करने से चित्त की सांसारिक चंचलता मिटती है और अंतःकरण में विशुद्ध भगवत्-प्रेम का प्राकट्य होता है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक चार पदों एवं टेक पर पूर्णतः आधारित है।""",

    "english_lyrics": """॥ Shri Sitarama Aarti ॥
(Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao)

Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao।
Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao॥

Aas-Paas Sakhiyan Sukha Daini,
Saji Nava Saaja Singara Sunaini,
Beena Sitaara Liyen Pikabaini,
Gaai Suraaga Sunaao॥
Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao॥

Anupama Chhabi Dhari Danpati Raajata,
Neela Peeta Pata Bhooshana Bhraajata,
Nirakhata Aganita Rati Chhabi Laajata,
Nainana Ko Phala Paao॥
Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao॥

Neeraja Naina Chapala Chitavana-Men,
Ruchira Arunima Suchi Adharana-Men,
Chandrabadana Ki Madhu Musakana-Men,
Nija Nayanan Arujhaao॥
Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao॥

Kanchana Thaara Sanvaari Manohara,
Ghrita Kapoora Shubha Baati Jyotikara,
Murachhala Chawanra Liyen Raameswara,
Harashi Sumana Barasaao॥
Gaao Gaao Ree, Priya-Pritam Ki Aarti Gaao॥"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'rama' in collections and 'items' in collections['rama']:
    r_items = collections['rama']['items']
    found = False
    for i, it in enumerate(r_items):
        if it.get('id') == 'drik_rama_4' or 'प्रियाप्रीतम' in it.get('hi_line', '') or 'प्रियाप्रीतम' in it.get('title', ''):
            r_items[i] = SITARAMA_DATA
            found = True
            print(f"[OK] Replaced Sitarama item at index {i} in JSON")
            break
    if not found:
        r_items.append(SITARAMA_DATA)
        print("[OK] Appended Sitarama item in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate drik_rama_4 in app.js
obj_start = app_js.find('"id": "drik_rama_4"')
if obj_start != -1:
    brace_start = app_js.rfind('{', 0, obj_start)
    next_obj = app_js.find('"id": "drik_rama_5"', obj_start)
    if next_obj != -1:
        brace_end = app_js.rfind('}', brace_start, next_obj) + 1
        new_block = json.dumps(SITARAMA_DATA, ensure_ascii=False, indent=8)
        app_js = app_js[:brace_start] + new_block + app_js[brace_end:]
        print("[OK] Successfully replaced drik_rama_4 block in app.js")
    else:
        print("[WARN] Could not find drik_rama_5")
else:
    print("[WARN] drik_rama_4 not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
