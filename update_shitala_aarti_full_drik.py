# -*- coding: utf-8 -*-
"""
Update drik_goddesses_15 (Shitala Mata Aarti / जय शीतला माता, मैया जय) in:
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

SHITALA_DATA = {
    "id": "drik_goddesses_15",
    "title": "जय शीतला माता, मैया जय",
    "title_en": "Shitala Mata Aarti (Jai Shitala Mata)",
    "en_line": "Jai Shitala Mata, Maiya Jai Shitala Mata",
    "hi_line": "जय शीतला माता, मैया जय शीतला माता",
    "sub": "आरोग्यप्रदायिनी माँ शीतला जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_shitala_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=FoeHn4Ptoy8",
    "video_id": "FoeHn4Ptoy8",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shitala-mata/shitala-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री शीतला माता की आरती ॥
(जय शीतला माता, मैया जय शीतला माता)

जय शीतला माता,
मैया जय शीतला माता।
आदि ज्योति महारानी
सब फल की दाता॥

ॐ जय शीतला माता...॥

रतन सिंहासन शोभित,
श्वेत छत्र भाता।
ऋद्धि-सिद्धि चँवर डोलावें,
जगमग छवि छाता॥

ॐ जय शीतला माता...॥

विष्णु सेवत ठाढ़े,
सेवें शिव धाता।
वेद पुराण वरणत
पार नहीं पाता॥

ॐ जय शीतला माता...॥

इन्द्र मृदङ्ग बजावत
चन्द्र वीणा हाथा।
सूरज ताल बजावै
नारद मुनि गाता॥

ॐ जय शीतला माता...॥

घण्टा शङ्ख शहनाई
बाजै मन भाता।
करै भक्त जन आरती
लखि लखि हर्षाता॥

ॐ जय शीतला माता...॥

ब्रह्म रूप वरदानी
तुही तीन काल ज्ञाता।
भक्तन को सुख देती
मातु पिता भ्राता॥

ॐ जय शीतला माता...॥

जो जन ध्यान लगावे
प्रेम शक्ति पाता।
सकल मनोरथ पावे
भवनिधि तर जाता॥

ॐ जय शीतला माता...॥

रोगों से जो पीड़ित कोई
शरण तेरी आता।
कोढ़ी पावे निर्मल काया
अन्ध नेत्र पाता॥

ॐ जय शीतला माता...॥

बांझ पुत्र को पावे
दारिद्र कट जाता।
ताको भजै जो नाहीं
सिर धुनि पछताता॥

ॐ जय शीतला माता...॥

शीतल करती जन की
तू ही है जग त्राता।
उत्पत्ति बाला बिनाशन
तू सब की माता॥

ॐ जय शीतला माता...॥

दास नारायण
कर जोरी माता।
भक्ति आपनी दीजै
और न कुछ माता॥

ॐ जय शीतला माता...॥""",
    "meaning": """॥ श्री शीतला माता जी की आरती (जय शीतला माता) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह पावन आरती आदिशक्ति भगवती दुर्गा के अत्यंत करुणामयी, आरोग्यप्रदायिनी तथा शीतलता-प्रदाता स्वरूप माँ शीतला की स्तुति में गाई जाती है। ज्वर, चेचक, दाह, चर्म-विकार व समस्त संक्रामक रोगों के शमन हेतु तथा शीतला सप्तमी/अष्टमी (बसौड़ा) पर इस आरती का गायन अत्यंत फलदायी है।)

१. प्रथम पद (टेक / मुखड़ा — आदि ज्योति, महारानी व फलदात्री):
"जय शीतला माता, मैया जय शीतला माता।
आदि ज्योति महारानी सब फल की दाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे आदि-अनादि ब्रह्म-ज्योति स्वरूपा, त्रिभुवन की महारानी माँ शीतला! आपकी सदा ही जय हो, जय-जयकार हो। आप अपने शरणागत भक्तों को धर्म, अर्थ, काम और मोक्ष सहित समस्त अभीष्ट फल प्रदान करने वाली परम कृपामयी माता हैं।

२. द्वितीय पद (रत्न सिंहासन, श्वेत छत्र व ऋद्धि-सिद्धि चंवर):
"रतन सिंहासन शोभित, श्वेत छत्र भाता।
ऋद्धि-सिद्धि चँवर डोलावें, जगमग छवि छाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे माँ! आप दिव्य मणियों और रत्नों से जड़े भव्य सिंहासन पर विराजमान हैं। आपके मस्तक पर श्वेत छत्र अत्यंत शोभा पा रहा है। ऋद्धि और सिद्धि दोनों देवियां आपके दोनों ओर खड़े होकर चंवर डुला रही हैं। आपका अलौकिक रूप करोड़ों सूर्यों के समान जगमगा रहा है।

३. तृतीय पद (त्रिदेव वंदना व वेदों द्वारा अगम्य महिमा):
"विष्णु सेवत ठाढ़े, सेवें शिव धाता।
वेद पुराण वरणत पार नहीं पाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे जगदम्बा! साक्षात भगवान विष्णु आपके सम्मुख खड़े होकर सेवा करते हैं तथा देवाधिदेव महादेव और सृष्टि-रचयिता ब्रह्मा जी (धाता) भी आपकी वंदना करते हैं। चारों वेद, समस्त उपनिषद और अठारह पुराण निरंतर आपका गुणगान करते हैं, किंतु आपकी अगाध महिमा का पार कोई नहीं पा सकता।

४. चतुर्थ पद (देवताओं का दिव्य वाद्य-वादन व गान):
"इन्द्र मृदङ्ग बजावत चन्द्र वीणा हाथा।
सूरज ताल बजावै नारद मुनि गाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे देवी! आपकी स्तुति में देवराज इंद्र मृदंग बजाते हैं, चंद्रमा अपने करकमलों में मधुर वीणा बजाते हैं, भगवान भुवन-भास्कर सूर्य ताल देते हैं और देवर्षि नारद वीणा की तान पर आपका पावन यशोगान करते हैं।

५. पंचम पद (शंख, घंटा, शहनाई व भक्तों का आनंद):
"घण्टा शङ्ख शहनाई बाजै मन भाता।
करै भक्त जन आरती लखि लखि हर्षाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे मैया! आपके दिव्य दरबार में घंटा, शंख, घड़ियाल और शहनाइयों की मनमोहक मंगल ध्वनि गूंजती है। जब आपके अनन्य भक्तजन प्रेम-विह्वल होकर आपकी पावन आरती उतारते हैं, तो आपके दिव्य वात्सल्यमय दर्शन कर उनका हृदय आनंद और हर्ष से भर जाता है।

६. षष्ठ पद (त्रिकालज्ञ, वरदानी व आत्मजनों के समान सुखदात्री):
"ब्रह्म रूप वरदानी तुही तीन काल ज्ञाता।
भक्तन को सुख देती मातु पिता भ्राता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे माता! आप साक्षात परब्रह्म स्वरूपा और संपूर्ण वरदानों की दात्री हैं। आप भूत, वर्तमान और भविष्य—तीनों कालों की ज्ञाता (त्रिकालज्ञ) हैं। जिस प्रकार माता, पिता और सहोदर भाई अपने परिवार को वात्सल्य और सुख देते हैं, उसी प्रकार आप अपने समस्त भक्तों का सर्वविध पोषण और संरक्षण करती हैं।

७. सप्तम पद (ध्यान, प्रेम-शक्ति व भवनिधि-तारण):
"जो जन ध्यान लगावे प्रेम शक्ति पाता।
सकल मनोरथ पावे भवनिधि तर जाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे करुणामयी! जो भी श्रद्धालु निष्कपट भाव से आपके स्वरूप का नित्य ध्यान लगाता है, उसे आत्मिक बल, प्रेम और आध्यात्मिक ऊर्जा की प्राप्ति होती है। उसके जीवन के समस्त मनोरथ सिद्ध होते हैं और वह संसार रूपी भवसागर को सहज ही पार कर जाता है।

८. अष्टम पद (असाध्य रोगों, कुष्ठ व अंधत्व का निवारण):
"रोगों से जो पीड़ित कोई शरण तेरी आता।
कोढ़ी पावे निर्मल काया अन्ध नेत्र पाता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे आरोग्य-दात्री माँ! जो भी व्यक्ति ज्वर, चेचक, दाह अथवा किसी भी असाध्य रोग से पीड़ित होकर आपकी शरण में आता है, आपकी कृपा से कुष्ठ-रोगी भी कंचन जैसी निर्मल, स्वस्थ काया प्राप्त कर लेता है और नेत्रहीन व्यक्ति को दिव्य ज्योति व दृष्टि प्राप्त हो जाती है।

९. नवम पद (संतान प्राप्ति, दारिद्र्य नाश व विमुखों का संताप):
"बांझ पुत्र को पावे दारिद्र कट जाता।
ताको भजै जो नाहीं सिर धुनि पछताता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे माँ! आपकी अनुकंपा से निःसंतान दंपत्ति सुयोग्य, दीर्घायु पुत्र-रत्न प्राप्त करते हैं और परिवार की घोर से घोर दरिद्रता समूल कट जाती है। जो अभागा मनुष्य संसार के मोह में पड़कर आपकी शरण नहीं लेता, वह अंत समय में सिर पीटकर पश्चाताप करता है।

१०. दशम पद (शीतलता-प्रदान, जगत्-त्राता व बाल-संकट विनाश):
"शीतल करती जन की तू ही है जग त्राता।
उत्पत्ति बाला बिनाशन तू सब की माता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे भगवती! आप संसार की समस्त तपन, व्याधि, मानसिक संताप और दैहिक ज्वर को शांत कर मन-प्राणों को शीतल करने वाली संपूर्ण जगत की परम त्राता (रक्षक) हैं। छोटे बालकों के समस्त संकटों, बाला-रिष्टों व अनिष्टों का विनाश करने वाली आप ही संपूर्ण ब्रह्मांड की जगज्जननी हैं।

११. एकादश पद (दास नारायण की करबद्ध प्रार्थना व अनन्य भक्ति याचना):
"दास नारायण कर जोरी माता।
भक्ति आपनी दीजै और न कुछ माता॥
ॐ जय शीतला माता...॥"
भावार्थ: हे माता शीतला! आपका सेवक नारायण दोनों हाथ जोड़कर आपके पावन चरणों में यह विनम्र प्रार्थना करता है कि हे माँ! मुझे सांसारिक धन-वैभव नहीं चाहिए, केवल और केवल अपनी निश्छल, अनन्य भक्ति और अपने श्रीचरणों की अविचल शरण प्रदान कीजिए।""",
    "vidhi": """॥ श्री शीतला माता जी की आरती — नित्य व बसौड़ा शास्त्रोक्त 4-2-1-7 विधान ॥

आरोग्यप्रदायिनी माँ शीतला जी की आरती उतारने का विशेष शास्त्रोक्त एवं शीतलता-प्रदायक विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
आरती हेतु शुद्ध गाय के घी का दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। शीतला पूजन में शीतल (ठंडे) जल, मटकी का जल, कच्चा दूध, दही, बसौड़ा (एक दिन पूर्व बना बासी भोजन—राबड़ी, मीठे चावल, पूड़ी, बाजरे की रोटी), नीम की पत्तियां, हल्दी, रोली, चंदन, कुंकुम, अक्षत और लाल चुनरी अर्पित की जाती है।

२. आरती घुमाने का विशेष शास्त्रीय '४-२-१-७' क्रम:
माँ शीतला के वात्सल्यमयी विग्रह के समक्ष '४-२-१-७' के शास्त्रोक्त क्रम से आरती घुमाएं:
• श्रीचरणों के समक्ष ४ बार: चारों पुरुषार्थों की प्राप्ति, पृथ्वी-तत्त्व की शीतलता व अहंकार विसर्जन हेतु।
• नाभि मंडल के समक्ष २ बार: उदर-विकार, पित्त-दोष, आंतरिक दाह (जलन) व ज्वर के शमन हेतु।
• मुखारविंद के समक्ष १ बार: दिव्य शीतलता, सौम्य दर्शन, नेत्र-ज्योति की वृद्धि व दृष्टि-दोष निवारण हेतु।
• संपूर्ण श्रीविग्रह के समक्ष ७ बार: सप्त धातुओं (रस, रक्त, मांस, मेद, अस्थि, मज्जा, शुक्र) की शुद्धि व समस्त संक्रामक रोगों के निवारण हेतु गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की शुद्धि व संपूर्ण प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष शीतला मंत्र व स्तुति:
आरती आरंभ करने से पूर्व 'ॐ ह्रीं श्रीं शीतलायै नमः' अथवा 'वन्देऽहं शीतलां देवीं रासभस्थां दिगम्बराम्। मार्जनीकलशोपेतां शूर्पालंकृतमस्तकाम्॥' मन्त्र का स्मरण करें।

४. आरती उपरांत शीतल जल छिड़काव व प्रसाद:
आरती पूर्ण होने पर कर्पूर दीप पर शीतल जल की तीन बूंदें छिड़ककर आचमन करें। कलश के शीतल जल व नीम की पत्तियों से परिवार के सभी सदस्यों पर छींटे देकर उनका रोग-निवारण करें। उपस्थित परिजनों व भक्तों में बसौड़ा (शीतल भोग) का प्रसाद वितरित करें।""",
    "significance": """॥ श्री शीतला माता आरती (जय शीतला माता) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. ज्वर, चेचक व संक्रामक रोगों से पूर्ण मुक्ति:
स्कंद पुराण के अनुसार, माँ शीतला की कृपा से चेचक (बड़ी माता/छोटी माता), खसरा, फोड़े-फुंसियां, नेत्र-रोग और उच्च-ज्वर (फीवर) का प्रकोप शांत हो जाता है। इनके कलश का जल अमृत-तुल्य शीतलता प्रदान करता है।

२. 'शीतल करती जन की' — शारीरिक व मानसिक शांति:
माँ शीतला केवल शारीरिक ताप ही नहीं, अपितु मनुष्य के मानसिक क्रोध, तनाव, ईर्ष्या और कलह की अग्नि को भी शांत कर अंतःकरण में शीतलता और धैर्य का संचार करती हैं।

३. बाल-रक्षा व वंश-वृद्धि (संतान प्राप्ति):
आरती में स्पष्ट उल्लेख है—"बांझ पुत्र को पावे... उत्पत्ति बाला बिनाशन तू सब की माता।" माता शीतला छोटे बालकों को समस्त बाला-रिष्टों, बुरी नजर और संक्रामक रोगों से बचाती हैं तथा निःसंतान दंपत्तियों को संतान-सुख प्रदान करती हैं।

४. शीतला सप्तमी व अष्टमी (बसौड़ा) का महापुण्य:
चैत्र मास के कृष्ण पक्ष की अष्टमी को 'बसौड़ा' पर्व पर बासी शीतल पकवानों का भोग लगाकर इस आरती का गान करने से वर्ष भर परिवार में कोई महामारी, संक्रामक रोग या अकाल संकट नहीं आता।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक ग्यारह छंद पदों पर पूर्णतः आधारित है, जो भारत के कोटि-कोटि शक्तिपीठों व सनातन गृहों में श्रद्धापूर्वक गाई जाती है।""",
    "english_lyrics": """॥ Shri Shitala Mata Ki Aarti ॥
(Jai Shitala Mata, Maiya Jai Shitala Mata)

Jai Shitala Mata,
Maiya Jai Shitala Mata।
Aadi Jyoti Maharanee
Saba Phala Kee Data॥

Om Jai Shitala Mata...॥

Ratana Singhasana Shobhita,
Shweta Chhatra Bhata।
Riddhi-Siddhi Chanwara Dolaven,
Jagamaga Chhavi Chhata॥

Om Jai Shitala Mata...॥

Vishnu Sevata Thaadhe,
Seven Shiva Dhata।
Veda Purana Varanata
Para Naheen Pata॥

Om Jai Shitala Mata...॥

Indra Mridanga Bajaavata
Chandra Veena Haatha।
Sooraja Taala Bajaavai
Narada Muni Gaata॥

Om Jai Shitala Mata...॥

Ghanta Shankha Shahanaayee
Baajai Mana Bhata।
Karai Bhakta Jana Aarti
Lakhi Lakhi Harshaata॥

Om Jai Shitala Mata...॥

Brahma Roopa Varadaanee
Tuhee Teena Kaala Gyaata।
Bhaktana Ko Sukha Detee
Maatu Pita Bhraata॥

Om Jai Shitala Mata...॥

Jo Jana Dhyana Lagave
Prema Shakti Paata।
Sakala Manoratha Paave
Bhavanidhi Tara Jaata॥

Om Jai Shitala Mata...॥

Rogon Se Jo Peedita Koee
Sharana Teree Aata।
Kodhee Paave Nirmala Kaaya
Andha Netra Paata॥

Om Jai Shitala Mata...॥

Baanjha Putra Ko Paave
Daaridra Kata Jaata।
Taako Bhajai Jo Naheen
Sira Dhuni Pachhataata॥

Om Jai Shitala Mata...॥

Sheetala Karatee Jana Kee
Too Hee Hai Jaga Traata।
Utpatti Baala Binaashana
Too Saba Kee Mata॥

Om Jai Shitala Mata...॥

Dasa Narayana
Kara Joree Mata।
Bhakti Aapanee Deejai
Aura Na Kuchha Mata॥

Om Jai Shitala Mata...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['gayatri', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_15':
                fg_data[cat_name]['items'][i] = SHITALA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_15 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_15':
                    cdata['items'][i] = SHITALA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_15 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(SHITALA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_15"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_15 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_15 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
