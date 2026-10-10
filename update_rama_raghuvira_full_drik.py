# -*- coding: utf-8 -*-
"""
Update drik_rama_3 (भगवान राम रघुवीर आरती / ऐसी आरती राम रघुबीर की करहि मन) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics (all 5 stanzas + refrain/tek)
- Verse-by-verse detailed Bhavarth (विनयपत्रिका मानस नीराजन)
- 4-2-1-7 Shri Rama Aarti Vidhi
- Significance (माहात्म्य व फलश्रुति)
- English Roman Transliteration
- Drik Panchang verified metadata (Video ID: hq7U1be4YBM)
"""

import json

RAMA_RAGHUVIRA_DATA = {
    "id": "drik_rama_3",
    "title": "ऐसी आरती राम रघुबीर की करहि मन",
    "title_en": "Shri Rama Raghuvira Aarti (Aisi Aarti Rama Raghubeera Ki Karahi Mana)",
    "en_line": "Aisi Aarti Rama Raghubeera Ki Karahi Mana, Harana Dukhdunda Govinda Aanandaghana",
    "hi_line": "ऐसी आरती राम रघुबीर की करहि मन, हरण दुखदुन्द गोविन्द आनन्दघन",
    "sub": "गोस्वामी तुलसीदास कृत मानस नीराजन • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_rama.jpg",
    "audio_url": "https://www.youtube.com/watch?v=hq7U1be4YBM",
    "video_id": "hq7U1be4YBM",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shree-rama/shri-rama-raghuvira-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ भगवान राम रघुवीर आरती ॥
(ऐसी आरती राम रघुबीर की करहि मन)

ऐसी आरती राम रघुबीर की करहि मन।
हरण दुखदुन्द गोविन्द आनन्दघन॥
ऐसी आरती राम रघुबीर की करहि मन॥

अचर चर रुप हरि, सर्वगत, सर्वदा
बसत, इति बासना धूप दीजै।
दीप निजबोधगत कोह-मद-मोह-तम
प्रौढ़ अभिमान चित्तवृत्ति छीजै॥
ऐसी आरती राम रघुबीर की करहि मन॥

भाव अतिशय विशद प्रवर नैवेद्य शुभ
श्रीरमण परम सन्तोषकारी।
प्रेम-ताम्बूल गत शूल सन्शय सकल,
विपुल भव-बासना-बीजहारी॥
ऐसी आरती राम रघुबीर की करहि मन॥

अशुभ-शुभ कर्म घृतपूर्ण दशवर्तिका,
त्याग पावक, सतोगुण प्रकासं।
भक्ति-वैराग्य-विज्ञान दीपावली,
अर्पि नीराजनं जगनिवासं॥
ऐसी आरती राम रघुबीर की करहि मन॥

बिमल हृदि-भवन कृत शान्ति-पर्यंक शुभ,
शयन विश्राम श्रीरामराया।
क्षमा-करुणा प्रमुख तत्र परिचारिका,
यत्र हरि तत्र नहिं भेद-माया॥
ऐसी आरती राम रघुबीर की करहि मन॥

आरती-निरत सनकादि, श्रुति, शेष, शिव,
देवरिषि, अखिलमुनि तत्त्व-दरसी।
करै सोइ तरै, परिहरै कामादि मल,
वदति इति अमलमति दास तुलसी॥
ऐसी आरती राम रघुबीर की करहि मन॥""",

    "meaning": """॥ ऐसी आरती राम रघुबीर की करहि मन — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह पावन आरती गोस्वामी तुलसीदास जी द्वारा 'विनयपत्रिका' में रचित परम गुह्य 'मानस नीराजन' / आंतरिक ज्ञान-भक्ति आरती है।)

१. टेक एवं मंगलाचरण:
"ऐसी आरती राम रघुबीर की करहि मन।
हरण दुखदुन्द गोविन्द आनन्दघन॥"

भावार्थ:
हे मेरे चंचल मन! तू मर्यादा पुरुषोत्तम भगवान श्री राम रघुवीर की ऐसी अलौकिक एवं आंतरिक मानस-आरती उतार; जो संसार के समस्त 'द्वंद्वों' (सुख-दुःख, राग-द्वेष, हानि-लाभ) और संतापों का समूल हरण करने वाले हैं, तथा जो साक्षात् 'गोविंद' (समस्त इंद्रियों के प्रकाशक व स्वामी) एवं सच्चिदानंद के सघन घन (आनंद के सागर) हैं।

२. वासना-धूप एवं आत्मबोध-दीपक:
"अचर चर रुप हरि, सर्वगत, सर्वदा
बसत, इति बासना धूप दीजै।
दीप निजबोधगत कोह-मद-मोह-तम
प्रौढ़ अभिमान चित्तवृत्ति छीजै॥"

भावार्थ:
इस संपूर्ण चर और अचर (जड़ और चेतन) जगत में साक्षात् श्री हरि ही सर्वत्र व्याप्त हैं, वे सर्वगत हैं और सर्वदा प्रत्येक क्षण विद्यमान हैं—ऐसी दृढ़ सात्विक भावना (शुभ वासना) की धूप भगवान को अर्पित कर।
और अपने स्वरूप के यथार्थ ज्ञान (आत्मबोध रूपी दिव्य दीप) को प्रज्वलित कर, जिससे क्रोध (कोह), अहंकार (मद) और अज्ञान रूपी अंधकार (मोह-तम) तथा अत्यंत बलवान (प्रौढ़) देहाभिमान की चित्तवृत्तियां क्षीण और नष्ट हो जाएं।

३. परम भाव-नैवेद्य एवं प्रेम-तांबूल:
"भाव अतिशय विशद प्रवर नैवेद्य शुभ
श्रीरमण परम सन्तोषकारी।
प्रेम-ताम्बूल गत शूल सन्शय सकल,
विपुल भव-बासना-बीजहारी॥"

भावार्थ:
अत्यंत निर्मल, निष्काम और विशुद्ध प्रेमाभक्ति का श्रेष्ठ नैवेद्य लक्ष्मीपति प्रभु श्री राम को अर्पित कर, जो उन्हें परम तृप्ति और संतोष प्रदान करने वाला है।
और प्रभु के प्रति अनन्य अनुराग का ऐसा 'प्रेम-तांबूल' (पान) अर्पित कर, जिससे हृदय के समस्त संशय, संताप, शूल और जन्म-जन्मांतरों की विशाल भव-वासनाओं के बीज ही समूल नष्ट हो जाएं।

४. दशवर्त्तिका नीराजन, त्याग की अग्नि व ज्ञान-दीपावली:
"अशुभ-शुभ कर्म घृतपूर्ण दशवर्तिका,
त्याग पावक, सतोगुण प्रकासं।
भक्ति-वैराग्य-विज्ञान दीपावली,
अर्पि नीराजनं जगनिवासं॥"

भावार्थ:
शुभ और अशुभ कर्म रूपी घी से भरी हुई दसों इंद्रियों (५ ज्ञानेंद्रिय + ५ कर्मेंद्रिय) की दश-बत्तियों को तैयार कर। उनमें आसक्ति के 'त्याग' की पावन अग्नि प्रज्वलित कर, जिससे विशुद्ध सत्त्वगुण का दिव्य प्रकाश फैल जाए।
इस प्रकार पराभक्ति, तीव्र वैराग्य और ब्रह्म-विज्ञान की दिव्य दीपमाला (दीपावली) का यह पावन नीराजन (आरती) समस्त जगत में निवास करने वाले अंतर्यामी जगन्निवास प्रभु श्री राम को सादर समर्पित कर।

५. हृदय-मंदिर विश्राम, शांति-शैया एवं क्षमा-करुणा परिचारिका:
"बिमल हृदि-भवन कृत शान्ति-पर्यंक शुभ,
शयन विश्राम श्रीरामराया।
क्षमा-करुणा प्रमुख तत्र परिचारिका,
यत्र हरि तत्र नहिं भेद-माया॥"

भावार्थ:
अपने काम-क्रोध रहित निर्मल हृदय रूपी भवन में परम 'शांति' का शुभ पर्यंक (पलंग/सेज) तैयार कर, जिस पर कौशल्यानंदन महाराजाधिराज श्री राम विश्राम करें।
वहां क्षमा, दया और करुणा जैसी सात्विक सद्गुण-रूपी प्रमुख परिचारिकाएं (दासियां) प्रभु की सेवा में अनवरत उपस्थित रहें। क्योंकि जहां साक्षात् श्री हरि का वास होता है, वहां द्वैत और भेद उत्पन्न करने वाली अविद्या-माया का लेशमात्र भी अस्तित्व नहीं रहता।

६. सनकादि-शिव वंदना एवं तुलसीदास फलश्रुति:
"आरती-निरत सनकादि, श्रुति, शेष, शिव,
देवरिषि, अखिलमुनि तत्त्व-दरसी।
करै सोइ तरै, परिहरै कामादि मल,
वदति इति अमलमति दास तुलसी॥"

भावार्थ:
इस परम गुह्य आंतरिक मानस-आरती में सनकादिक महर्षि, वेद (श्रुति), सहस्रफणी शेषनाग, देवाधिदेव भगवान शिव, देवर्षि नारद और समस्त तत्त्वदर्शी मुनीश्वर नित्य निरत (लीन) रहते हैं।
निर्मल बुद्धि वाले गोस्वामी तुलसीदास जी कहते हैं कि जो भी साधक इस प्रकार अंतःकरण से भगवान रघुवीर की मानस-आरती करता है, वह काम, क्रोध आदि समस्त मानसिक मलों का त्याग कर अनायास ही भवसागर से तर जाता है और मोक्ष पद को प्राप्त करता है।""",

    "vidhi": """॥ श्री राम रघुवीर मानस एवं बाह्य आरती — शास्त्रोक्त 4-2-1-7 विधान ॥

भगवान श्री राम रघुवीर की यह आरती बाह्य पूजा के साथ-साथ अंतःकरण की शुद्धि का दिव्य समन्वय है:

१. दीप प्रज्वलन व आचमन:
शुद्ध गाय के घी का पंचमुखी दीपक या कर्पूर प्रज्वलित करें। थाल में पीत पुष्प, तुलसी दल, रोली, चंदन, अक्षत और सुगंधित धूप रखें। 'ॐ रां रामाय नमः' अथवा 'श्री सीता-रामाभ्यां नमः' का स्मरण करें।

२. पावन चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में प्रभु श्री रघुवीर के दोनों कोमल चरणकमलों में ४ बार घुमाएं। यह अहिल्या-उद्धारक चरणों में समर्पण और भवभय हरण की वंदना है।

३. नाभि-कमल पर २ बार घुमाएं:
इसके उपरांत दीपक को प्रभु के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह त्रिभुवन के आधार और मर्यादा के केंद्र का नमन है।

४. मंद मुस्कराते मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को भगवान श्री राम के कोमल, शांत, मंद-मंद मुस्कराते मुखारविन्द के समक्ष १ बार घुमाएं। इससे अविद्या, काम-क्रोध और मानसिक विकारों का नाश होता है।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मुकुट से लेकर चरणकमलों तक (कोदंड धनुष व बाण सहित) सम्पूर्ण श्रीविग्रह पर भावपूर्वक ७ बार घुमाएं। यह सातों लोकों के रक्षक और मर्यादा पुरुषोत्तम की समग्र वंदना है।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. मानस नीराजन एवं आरती ग्रहण:
आरती पूर्ण होने पर शंखनाद करें, आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती का पावन ताप ग्रहण कर शीश व नेत्रों पर लगाएं तथा मन ही मन प्रभु के 'सच्चिदानंद' स्वरूप का ध्यान करें।""",

    "significance": """॥ ऐसी आरती राम रघुबीर की करहि मन — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. विनयपत्रिका का सर्वोच्च मानस नीराजन:
यह स्तुति गोस्वामी तुलसीदास जी द्वारा रचित 'विनयपत्रिका' का पद संख्या ४३ है। इसमें बाह्य उपचारों (धूप, दीप, नैवेद्य, तांबूल) को आंतरिक साधना (आत्मबोध, त्याग, विशुद्ध भाव, सत्त्वगुण) के रूप में निरूपित किया गया है।

२. द्वंद्व एवं भव-वासनाओं का समूल नाश:
"हरण दुखदुन्द गोविन्द आनन्दघन"—इस आरती का नित्य भावपूर्वक श्रवण व गायन करने से जीवन के द्वंद्व (राग-द्वेष, सुख-दुःख, मान-अपमान) मिटते हैं और संशय दूर होते हैं।

३. षड्विकार निवारण एवं परम शांति:
"करै सोइ तरै, परिहरै कामादि मल"—हृदय में स्थित काम, क्रोध, मद, मोह का नाश होता है तथा अंतःकरण में क्षमा, दया व अखंड शांति का वास होता है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक पांच पदों एवं टेक पर पूर्णतः आधारित है।""",

    "english_lyrics": """॥ Aarti Shri Rama Raghuvira Ki ॥
(Aisi Aarti Rama Raghubeera Ki Karahi Mana)

Aisi Aarti Rama Raghubeera Ki Karahi Mana।
Harana Dukhdunda Govinda Aanandaghana॥
Aisi Aarti Rama Raghubeera Ki Karahi Mana॥

Achara Chara Rupa Hari, Sarvagata, Sarvada
Basata, Iti Baasana Dhoopa Deejai।
Deepa Nijabodhigata Koha-Mada-Moha-Tama
Praudha Abhimaana Chittavritti Chheejai॥
Aisi Aarti Rama Raghubeera Ki Karahi Mana॥

Bhaava Atishaya Vishada Pravara Naivedya Shubha
Shreeramana Parama Santosha-Kari।
Prema-Taambula Gata Shoola Sanshaya Sakala,
Vipula Bhava-Baasana-Beejahari॥
Aisi Aarti Rama Raghubeera Ki Karahi Mana॥

Ashubha-Shubha Karma Ghritapoorna Dashavartika,
Tyaaga Paavaka, Satoguna Prakaasam।
Bhakti-Vairaagya-Vijnaana Deepavali,
Arpi Neeraajanam Jagannivaasam॥
Aisi Aarti Rama Raghubeera Ki Karahi Mana॥

Bimala Hridi-Bhavana Krita Shaanti-Paryanka Shubha,
Shayana Vishrama Shreeramaraya।
Kshama-Karuna Pramukha Tatra Parichaarika,
Yatra Hari Tatra Nahin Bheda-Maaya॥
Aisi Aarti Rama Raghubeera Ki Karahi Mana॥

Aarti-Nirata Sanakaadi, Shruti, Shesha, Shiva,
Devarishi, Akhilamuni Tattva-Darasi।
Karai Soi Tarai, Pariharai Kaamaadi Mala,
Vadati Iti Amalamati Dasa Tulasi॥
Aisi Aarti Rama Raghubeera Ki Karahi Mana॥"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'rama' in collections and 'items' in collections['rama']:
    r_items = collections['rama']['items']
    found = False
    for i, it in enumerate(r_items):
        if it.get('id') == 'drik_rama_3' or 'ऐसी आरती' in it.get('hi_line', '') or 'ऐसी आरती' in it.get('title', ''):
            r_items[i] = RAMA_RAGHUVIRA_DATA
            found = True
            print(f"[OK] Replaced Rama Raghuvira item at index {i} in JSON")
            break
    if not found:
        r_items.append(RAMA_RAGHUVIRA_DATA)
        print("[OK] Appended Rama Raghuvira item in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate drik_rama_3 in app.js
obj_start = app_js.find('"id": "drik_rama_3"')
if obj_start != -1:
    brace_start = app_js.rfind('{', 0, obj_start)
    next_obj = app_js.find('"id": "drik_rama_4"', obj_start)
    if next_obj != -1:
        brace_end = app_js.rfind('}', brace_start, next_obj) + 1
        new_block = json.dumps(RAMA_RAGHUVIRA_DATA, ensure_ascii=False, indent=8)
        app_js = app_js[:brace_start] + new_block + app_js[brace_end:]
        print("[OK] Successfully replaced drik_rama_3 block in app.js")
    else:
        print("[WARN] Could not find drik_rama_4")
else:
    print("[WARN] drik_rama_3 not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
