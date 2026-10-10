# -*- coding: utf-8 -*-
"""
Update drik_rama_6 (श्री राम रघुपति आरती / बन्दौं रघुपति करुना निधान) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics (all 9 stanzas + tek/refrain)
- Verse-by-verse detailed Bhavarth (विनयपत्रिका - गोस्वामी तुलसीदास जी)
- 4-2-1-7 Shri Rama Raghupati Aarti Vidhi
- Significance (माहात्म्य व फलश्रुति)
- English Roman Transliteration
- Drik Panchang verified metadata (Video ID: Uaw7uJva7EE)
"""

import json

RAGHUPATI_DATA = {
    "id": "drik_rama_6",
    "title": "बन्दौं रघुपति करुना निधान",
    "title_en": "Lord Rama Raghupati Aarti (Bandoun Raghupati Karuna Nadhana)",
    "en_line": "Bandoun Raghupati Karuna Nadhana, Jaate Chhootai Bhava-Bheda Gyana",
    "hi_line": "बन्दौं रघुपति करुना निधान, जाते छूटै भव-भेद ग्यान",
    "sub": "गोस्वामी तुलसीदास कृत 'विनयपत्रिका' स्तुति-आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_rama.jpg",
    "audio_url": "https://www.youtube.com/watch?v=Uaw7uJva7EE",
    "video_id": "Uaw7uJva7EE",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shree-rama/shri-rama-raghupati-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री राम रघुपति आरती ॥
(बन्दौं रघुपति करुना निधान)

बन्दौं रघुपति करुना निधान।
जाते छूटै भव-भेद ग्यान॥
बन्दौं रघुपति करुना निधान॥

रघुबन्स-कुमुद-सुखप्रद निसेस।
सेवत पद-पन्कज अज-महेस॥
बन्दौं रघुपति करुना निधान॥

निज भक्त-हृदय पाथोज-भृन्ग।
लावन्यबपुष अगनित अनन्ग॥
बन्दौं रघुपति करुना निधान॥

अति प्रबल मोह-तम-मारतण्ड।
अग्यान-गहन-पावक-प्रचण्ड॥
बन्दौं रघुपति करुना निधान॥

अभिमान-सिन्धु-कुम्भज उदार।
सुररन्जन, भन्जन भूमिभार॥
बन्दौं रघुपति करुना निधान॥

रागादि-सर्पगन पन्नगारि।
कन्दर्प-नाग-मृगपति, मुरारि॥
बन्दौं रघुपति करुना निधान॥

भव-जलधि-पोत चरनारबिन्द।
जानकी-रवन आनन्द कन्द॥
बन्दौं रघुपति करुना निधान॥

हनुमन्त प्रेम बापी मराल।
निष्काम कामधुक गो दयाल॥
बन्दौं रघुपति करुना निधान॥

त्रैलोक-तिलक, गुनगहन राम।
कह तुलसिदास बिश्राम-धाम॥
बन्दौं रघुपति करुना निधान॥""",

    "meaning": """॥ श्री राम रघुपति आरती (बन्दौं रघुपति करुना निधान) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह महाकाव्य-तुल्य पावन स्तुति-आरती महाकवि गोस्वामी तुलसीदास जी द्वारा 'विनयपत्रिका' में रचित अद्वैत-भक्ति और परम तत्त्व-दर्शन का शिखर है।)

१. मंगलाचरण एवं भव-भेद निवृत्ति:
"बन्दौं रघुपति करुना निधान।
जाते छूटै भव-भेद ग्यान॥"

भावार्थ:
मैं साक्षात् करुणा के सागर, परम कृपालु भगवान श्री रघुपति की नित्य वंदना और आरती करता हूँ; जिनके पावन स्मरण और भजन से संसार का यह मिथ्या भेद-ज्ञान (द्वैत, राग-द्वेष और अज्ञान रूपी सांसारिक भ्रम) सदा-सर्वदा के लिए छूट जाता है।

२. रघुकुल-चंद्र एवं ब्रह्मा-शिव द्वारा चरण-सेवा:
"रघुबन्स-कुमुद-सुखप्रद निसेस।
सेवत पद-पन्कज अज-महेस॥"

भावार्थ:
जो रघुकुल रूपी कुमुदिनी को परम सुख और आनंद प्रदान करने वाले पूर्ण चंद्रमा (निशेश) हैं। जिनके पावन चरणकमलों की नित्य सेवा साक्षात् सृष्टि के रचयिता ब्रह्मा (अज) और देवाधिदेव महादेव शिव अत्यंत श्रद्धापूर्वक करते हैं।

३. भक्त-हृदय-कमल के भ्रमर एवं कोटि-कामदेव लावण्य:
"निज भक्त-हृदय पाथोज-भृन्ग।
लावन्यबपुष अगनित अनन्ग॥"

भावार्थ:
जो अपने अनन्य निष्काम भक्तों के हृदय रूपी कमल (पाथोज) के पराग-रस का आस्वादन करने वाले दिव्य भ्रमर (भृंग) हैं। जिनका सुकोमल, श्यामवर्ण श्रीविग्रह अनगिनत कामदेवों (अगणित अनंग) के अलौकिक लावण्य और सौंदर्य से परिपूर्ण है।

४. मोह-नाशक सूर्य एवं अज्ञान-वन की दावानल:
"अति प्रबल मोह-तम-मारतण्ड।
अग्यान-गहन-पावक-प्रचण्ड॥"

भावार्थ:
जो सांसारिक जीवों के अत्यंत बलवान और घोर मोह रूपी अंधकार को तत्क्षण मिटाने वाले देदीप्यमान सूर्य (मार्तंड) हैं; तथा अज्ञान रूपी घने और दुर्गम वन (गहन) को पलक झपकते भस्म करने वाली प्रचंड पावक (अग्नि) हैं।

५. अभिमान-सिंधु के अगस्त्य मुनि एवं भू-भार भंजन:
"अभिमान-सिन्धु-कुम्भज उदार।
सुररन्जन, भन्जन भूमिभार॥"

भावार्थ:
जो देहाभिमान, काम और मद रूपी अथाह सागर को एक ही आचमन में सोख लेने वाले परम उदार महर्षि अगस्त्य (कुंभज) हैं। जो देवताओं को आनंदित करने वाले तथा असुरों व दुष्टों का संहार कर पृथ्वी के भारी बोझ को हरने वाले हैं।

६. रागादि-सर्पों के गरुड़ एवं कामदेव-गज के सिंह:
"रागादि-सर्पगन पन्नगारि।
कन्दर्प-नाग-मृगपति, मुरारि॥"

भावार्थ:
जो राग, द्वेष, ईर्ष्या आदि विषैले सर्पों के समूह का नाश करने वाले साक्षात् गरुड़ (पन्नगारि) हैं। जो कामदेव रूपी मतवाले ऐरावत हाथी का दलन करने वाले पराक्रमी सिंह (मृगपति) हैं, तथा समस्त संकटों के संहारक मुरारि हैं।

७. भव-सागर के जहाज एवं जानकी-रमण आनंदकंद:
"भव-जलधि-पोत चरनारबिन्द।
जानकी-रवन आनन्द कन्द॥"

भावार्थ:
इस अपार और अथाह संसार-सागर (भव-जलधि) से पार कराने वाले सशक्त जहाज (पोत) जिनके पावन चरणारविंद हैं। वे जनकनंदिनी माता जानकी के प्राणपति (जानकी-रमण) और समस्त ब्रह्मांड को अखंड आनंद प्रदान करने वाले सच्चिदानंद के मूल कंद हैं।

८. हनुमान-प्रेम-सरोवर के राजहंस एवं कामधेनु:
"हनुमन्त प्रेम बापी मराल।
निष्काम कामधुक गो दयाल॥"

भावार्थ:
जो भक्तशिरोमणि श्री हनुमान जी के विशुद्ध प्रेम रूपी सरोवर (बापी) में नित्य क्रीड़ा करने वाले सुंदर राजहंस (मराल) हैं। और जो अपने निष्काम शरणागत भक्तों के समस्त मनोरथों को पूर्ण करने वाली परम दयालु कामधेनु गौ हैं।

९. त्रैलोक्य-तिलक, गुण-सागर एवं परम विश्राम-धाम:
"त्रैलोक-तिलक, गुनगहन राम।
कह तुलसिदास बिश्राम-धाम॥"

भावार्थ:
जो तीनों लोकों के मुकुट-तिलक और अगाध, अनंत दिव्य गुणों के सागर हैं। गोस्वामी तुलसीदास जी कहते हैं कि ऐसे करुणामय श्री राम ही संपूर्ण ब्रह्मांड, मुनियों और थके हुए सांसारिक जीवों के एकमात्र परम विश्राम-धाम (अंतिम शांति व मोक्ष के आश्रय) हैं।""",

    "vidhi": """॥ श्री राम रघुपति आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधान ॥

मर्यादा पुरुषोत्तम भगवान श्री राम रघुपति जी की आरती उतारने का विशेष शास्त्रोक्त एवं वैष्णव विधान:

१. दीप प्रज्वलन व आचमन:
स्वर्ण, पीतल अथवा चांदी की थाली में शुद्ध गाय के घी का पंचमुखी दीपक या कर्पूर प्रज्वलित करें। थाल में पीत पुष्प, तुलसी दल, रोली, चंदन, अक्षत और सुगंधित धूप रखें। 'ॐ रां रामाय नमः' अथवा 'ॐ नमो भगवते रघुनन्दनाय' का स्मरण करें।

२. पावन चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में प्रभु के दोनों कोमल चरणकमलों में ४ बार घुमाएं। यह भव-सागर से पार उतारने वाले चरणारविंद की वंदना है।

३. नाभि-कमल पर २ बार घुमाएं:
इसके उपरांत दीपक को प्रभु के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह त्रिभुवन के आधार और आनंदकंद के केंद्र का नमन है।

४. मंद मुस्कराते मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को भगवान श्री राम के कोमल, शांत, मंद-मंद मुस्कराते मुखारविन्द के समक्ष १ बार घुमाएं। इससे अविद्या, काम-क्रोध और मानसिक विकारों का नाश होता है।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मुकुट से लेकर चरणकमलों तक (कोदंड धनुष, बाण व त्रैलोक्य-तिलक छवि सहित) सम्पूर्ण श्रीविग्रह पर भावपूर्वक ७ बार घुमाएं।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, पुष्पांजलि एवं आरती ग्रहण:
आरती पूर्ण होने पर शंखनाद करें, आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती का पावन ताप ग्रहण कर शीश व नेत्रों पर लगाएं तथा 'सियावर रामचंद्र की जय' का जयघोष करें।""",

    "significance": """॥ बन्दौं रघुपति करुना निधान — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. भव-भेद एवं अज्ञान का नाश:
"जाते छूटै भव-भेद ग्यान"—इस स्तुति-आरती के नियमित पाठ व श्रवण से मनुष्य का अज्ञान, सांसारिक भ्रम और द्वैत-भाव मिट जाता है तथा परमतत्त्व का बोध होता है।

२. मोह-तम एवं अहंकार का शमन:
"अभिमान-सिन्धु-कुम्भज उदार"—हृदय से प्रचंड मोह और बलवान देहाभिमान समाप्त होकर चित्त में निर्मलता, शांति और विनम्रता का प्रादुर्भाव होता है।

३. परम विश्राम एवं मोक्ष प्राप्ति:
"कह तुलसिदास बिश्राम-धाम"—सांसारिक चिंताओं और तापों से व्यथित जीवात्मा को भगवान श्री राम के चरणों में अखंड विश्राम और परम पद (मोक्ष) की प्राप्ति होती है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक नौ पदों पर पूर्णतः आधारित है।""",

    "english_lyrics": """॥ Shri Rama Raghupati Aarti ॥
(Bandoun Raghupati Karuna Nadhana)

Bandoun Raghupati Karuna Nadhana।
Jaate Chhootai Bhava-Bheda Gyana॥
Bandoun Raghupati Karuna Nadhana॥

Raghubansa-Kumuda-Sukhaprada Nisesa।
Sevata Pada-Pankaja Aja-Mahesa॥
Bandoun Raghupati Karuna Nadhana॥

Nija Bhakta-Hridaya Paathoja-Bhringa।
Lavanyavapusha Aganita Ananga॥
Bandoun Raghupati Karuna Nadhana॥

Ati Prabala Moha-Tama-Maaratanda।
Agyana-Gahana-Paavaka-Prachanda॥
Bandoun Raghupati Karuna Nadhana॥

Abhimaana-Sindhu-Kumbhaja Udaara।
Suraranjana, Bhanjana Bhoomibhaara॥
Bandoun Raghupati Karuna Nadhana॥

Raagaadi-Sarpagana Pannagaari।
Kandarpa-Naaga-Mrigapati, Muraari॥
Bandoun Raghupati Karuna Nadhana॥

Bhava-Jaladhi-Pota Charanaarabinda।
Jaanaki-Ravana Aananda Kanda॥
Bandoun Raghupati Karuna Nadhana॥

Hanumanta Prema Baapi Maraala।
Nishkaama Kaamadhuka Go Dayaala॥
Bandoun Raghupati Karuna Nadhana॥

Trailoka-Tilaka, Gunagahana Raama।
Kaha Tulasidasa Bishrama-Dhaama॥
Bandoun Raghupati Karuna Nadhana॥"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'rama' in collections and 'items' in collections['rama']:
    r_items = collections['rama']['items']
    found = False
    for i, it in enumerate(r_items):
        if it.get('id') == 'drik_rama_6' or 'बन्दौं रघुपति' in it.get('hi_line', '') or 'बन्दौं रघुपति' in it.get('title', ''):
            r_items[i] = RAGHUPATI_DATA
            found = True
            print(f"[OK] Replaced Raghupati item at index {i} in JSON")
            break
    if not found:
        r_items.append(RAGHUPATI_DATA)
        print("[OK] Appended Raghupati item in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate drik_rama_6 in app.js
obj_start = app_js.find('"id": "drik_rama_6"')
if obj_start != -1:
    brace_start = app_js.rfind('{', 0, obj_start)
    # The end of drik_rama_6 is right before the closing bracket of items array in rama
    shiva_start = app_js.find('"shiva": {', obj_start)
    if shiva_start != -1:
        brace_end = app_js.rfind('}', brace_start, shiva_start) + 1
        new_block = json.dumps(RAGHUPATI_DATA, ensure_ascii=False, indent=8)
        app_js = app_js[:brace_start] + new_block + app_js[brace_end:]
        print("[OK] Successfully replaced drik_rama_6 block in app.js")
    else:
        print("[WARN] Could not find shiva section")
else:
    print("[WARN] drik_rama_6 not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
