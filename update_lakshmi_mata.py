import json

content_hindi = """॥ आरती श्री लक्ष्मी माता जी ॥

ॐ जय लक्ष्मी माता, मैया जय लक्ष्मी माता।
तुमको निशिदिन सेवत, हरि विष्णु विधाता॥
ॐ जय लक्ष्मी माता॥

उमा, रमा, ब्रह्माणी, तुम ही जग-माता।
सूर्य-चन्द्रमा ध्यावत, नारद ऋषि गाता॥
ॐ जय लक्ष्मी माता॥

दुर्गा रुप निरंजनी, सुख सम्पत्ति दाता।
जो कोई तुमको ध्यावत, ऋद्धि-सिद्धि धन पाता॥
ॐ जय लक्ष्मी माता॥

तुम पाताल-निवासिनि, तुम ही शुभदाता।
कर्म-प्रभाव-प्रकाशिनी, भवनिधि की त्राता॥
ॐ जय लक्ष्मी माता॥

जिस घर में तुम रहतीं, सब सद्गुण आता।
सब सम्भव हो जाता, मन नहीं घबराता॥
ॐ जय लक्ष्मी माता॥

तुम बिन यज्ञ न होते, वस्त्र न कोई पाता।
खान-पान का वैभव, सब तुमसे आता॥
ॐ जय लक्ष्मी माता॥

शुभ-गुण मन्दिर सुन्दर, क्षीरोदधि-जाता।
रत्न चतुर्दश तुम बिन, कोई नहीं पाता॥
ॐ जय लक्ष्मी माता॥

महालक्ष्मीजी की आरती, जो कोई जन गाता।
उर आनन्द समाता, पाप उतर जाता॥
ॐ जय लक्ष्मी माता॥"""

meaning_text = """पद्यवार सम्पूर्ण पावन भावार्थ:

१. टेक — प्रणवाक्षर 'ॐ' समन्वित जगत्-जननी महालक्ष्मी व त्रिदेव-आराध्य स्वरूप:
हे ओंकार स्वरूपा, सकल चराचर की प्राण-धात्री माँ महालक्ष्मी! आपकी सदा सर्वदा जय हो! देवाधिदेव महादेव (हर), पालनकर्ता भगवान श्रीहरि विष्णु और सृष्टिकर्ता ब्रह्मा जी (विधाता) तीनों देव अहर्निश (निशिदिन) आपके पावन श्रीचरणों की सेवा व वंदना करते हैं।

२. पद १ — त्रिदेवी एकात्मता, जगन्माता एवं सूर्य-चंद्र-नारद द्वारा वंदना:
आप ही भगवान शिव की शक्ति 'उमा', श्रीहरि की नित्य आह्लादिनी 'रमा' और ब्रह्मा जी की ज्ञान-शक्ति 'ब्रह्माणी' हैं; वास्तव में आप ही इस संपूर्ण ब्रह्मांड की एक अद्वितीय जननी (जग-माता) हैं। प्रत्यक्ष देवता सूर्य और चंद्रमा नित्य आपका ध्यान धरते हैं तथा देवर्षि नारद अपनी वीणा पर प्रेमपूर्वक आपकी महिमा का गान करते हैं।

३. पद २ — दुर्गा रूप, निरंजन तत्त्व एवं ऋद्धि-सिद्धि-धन प्रदाता:
आप ही दुष्टों का दलन करने वाली दुर्गा हैं और मायातीत परम शुद्ध 'निरंजनी' शक्ति हैं। आप समस्त अलौकिक व लौकिक सुख तथा अखंड ऐश्वर्य की दात्री हैं। जो भी निष्काम या सकाम भाव से आपका ध्यान धरता है, उसे ऋद्धि, सिद्धि, नव-निधियां एवं अक्षय धन-सम्पदा सहज ही प्राप्त हो जाती है।

४. पद ३ — सर्वव्यापकता (पाताल-भू-स्वर्ग), कर्म-फल प्रदीपन व भवसागर से उद्धार:
आप पाताल से लेकर स्वर्ग तक सर्वत्र व्याप्त हैं, भक्त प्रह्लाद व बलि के पाताल-लोक में भी निवास कर शुभ फल देने वाली हैं। आप ही जीवों के कर्म-प्रभाव (भाग्य व प्रारब्ध) को आलोकित व प्रकाशित करने वाली हैं तथा जन्म-मरण रूपी भव-सागर (भवनिधि) से पार उतारने वाली परम त्राता हैं।

५. पद ४ — सद्गुण-प्राकट्य, निर्भयता व असंभव का संभव होना:
हे कल्याणी माँ! जिस घर, परिवार अथवा अंतःकरण में आपका वास होता है, वहाँ सत्य, प्रेम, संतोष, शील आदि समस्त दैवीय सद्गुण स्वयं खिंचे चले आते हैं। आपकी कृपा से कठिन से कठिन कार्य भी संभव हो जाता है और भक्त का मन कभी किसी विपत्ति में भयभीत या विचलित नहीं होता।

६. पद ५ — यज्ञ-स्वाहा-स्वधा स्वरूप, आवरण-वस्त्र व खान-पान का वैभव:
हे माँ! आपकी कृपा (द्रव्य व श्रद्धा) के बिना संसार में कोई भी यज्ञ, अनुष्ठान या देव-कार्य संपन्न नहीं हो सकता। शरीर को ढकने वाले वस्त्र, जीवन का पोषण करने वाले अन्न, रस, फल और खान-पान का समस्त वैभव केवल और केवल आपकी अनुकंपा से ही प्राप्त होता है।

७. पद ६ — समुद्र-मंथन प्राकट्य, चौदह रत्नों की अधिष्ठात्री व शुभ-मंदिर:
आप समस्त शुभ गुणों का पावन मंदिर हैं, अत्यंत रूपवान व लावण्यमयी हैं। सागर-मंथन के समय आप क्षीरसागर (क्षीरोदधि) से अमृत-कलश व कमल-पुष्प लिए प्रकट हुईं। समुद्र-मंथन से निकले चौदह रत्नों में सर्वश्रेष्ठ रत्न आप स्वयं हैं और आपकी कृपा के बिना किसी भी जीव को चौदह रत्नों का ऐश्वर्य प्राप्त नहीं हो सकता।

८. पद ७ — हृदय-आनंद, पाप-मुक्ति व परम मोक्ष फलश्रुति:
माँ महालक्ष्मी जी की इस परम पावन व सिद्ध आरती का जो भी नर-नारी नित्य प्रातः व संध्या प्रेमपूर्वक गान करते हैं, उनके हृदय (उर) में अलौकिक ब्रह्मानंद समा जाता है, उनके जन्म-जन्मांतरों के पाप तत्काल उतर (धुल) जाते हैं और उन्हें अंत में श्रीहरि के वैकुंठ धाम की प्राप्ति होती है।"""

vidhi_text = """माँ महालक्ष्मी शास्त्रोक्त ४-२-१-७ दीप समर्पण विधि:

माँ महालक्ष्मी जी की आरती करते समय शुद्ध गौ-घृत अथवा तिल के तेल के दीपक से कुल १४ बार प्रदक्षिणा चक्र निम्न शास्त्रसम्मत क्रम में संपन्न करें:

१. चरणकमलों में (४ बार): माँ महालक्ष्मी के पावन चरणकमलों में दीप को ४ बार घुमाएं (समस्त दरिद्रता, कलह व पापों के निवारण हेतु)।
२. नाभि-मण्डल पर (२ बार): सम्पूर्ण ऐश्वर्य व सृष्टि-पोषण के केंद्र नाभि-कमल के समक्ष २ बार दीप घुमाएं (सृष्टि की सुख-समृद्धि का ध्यान करते हुए)।
३. मुखारविन्द पर (१ बार): मंद मुस्कान युक्त, कमल-नयनी माँ के तेजोमय मुखमण्डल के समक्ष १ बार दीप घुमाएं।
४. समस्त श्रीविग्रह पर (७ बार): कमल-पुष्प, सुवर्ण-मुद्रा, अभय व वरद मुद्रा धारण किए हुए, क्षीरसागर-तनया माँ महालक्ष्मी के समस्त तेजोमय विग्रह पर ७ बार दीप घुमाएं (कुल १४ बार प्रदक्षिणा चक्र)।
५. विशेष समर्पण: माँ महालक्ष्मी की आरती में कमलगट्टे, खीर, श्वेत/पीत मिष्ठान्न, कमल या गुलाब के पुष्प एवं इत्र समर्पित करें (विशेषकर दीपावली, शरद पूर्णिमा, शुक्रवार, धनतेरस व वरलक्ष्मी व्रत पर)।"""

significance_text = """आध्यात्मिक माहात्म्य एवं फलश्रुति:

१. सनातन की सार्वभौम महाआरती: दीपावली की महापूजा, धनतेरस, शरद पूर्णिमा एवं प्रत्येक शुक्रवार को गाई जाने वाली यह संपूर्ण विश्व में सर्वाधिक लोकप्रिय, सर्वमान्य व जाग्रत महाआरती है।
२. दरिद्रता का समूल नाश व अष्टलक्ष्मी कृपा: इस आरती के नित्य गान से गृह में अलक्ष्मी (दरिद्रता, क्लेश, आलस्य, रोग) का सर्वथा नाश होता है और आदिलक्ष्मी, धनलक्ष्मी, धान्यलक्ष्मी, गजलक्ष्मी, संतानलक्ष्मी, वीरलक्ष्मी, विजयलक्ष्मी व विद्यालक्ष्मी — इन अष्टलक्ष्मियों का नित्य स्थाई वास होता है।
३. सद्गुण व आंतरिक शुद्धि: 'जिस घर में तुम रहतीं सब सद्गुण आता' — केवल भौतिक संपदा ही नहीं, अपितु सात्त्विक विचार, पारिवारिक सौहार्द, धर्म-निष्ठा और आत्म-संतोष रूपी वास्तविक धन की प्राप्ति होती है।"""

english_lyrics_text = """(Tek)
Om Jai Lakshmi Mata, Maiya Jai Lakshmi Mata।
Tumako Nishidina Sevata, Hari Vishnu Vidhata॥
Om Jai Lakshmi Mata॥

(Pada 1)
Uma, Rama, Brahmani, Tum Hi Jaga-Mata।
Soorya-Chandrama Dhyavata, Narada Rishi Gata॥
Om Jai Lakshmi Mata॥

(Pada 2)
Durga Roopa Niranjani, Sukha Sampatti Data।
Jo Koi Tumako Dhyavata, Riddhi-Siddhi Dhana Pata॥
Om Jai Lakshmi Mata॥

(Pada 3)
Tum Patala-Nivasini, Tum Hi Shubhadhata।
Karma-Prabhava-Prakashini, Bhavanidhi Ki Trata॥
Om Jai Lakshmi Mata॥

(Pada 4)
Jisa Ghara Mein Tum Rahatin, Saba Sadguna Aata।
Saba Sambhava Ho Jata, Mana Nahin Ghabarata॥
Om Jai Lakshmi Mata॥

(Pada 5)
Tum Bina Yajna Na Hote, Vastra Na Koi Pata।
Khana-Pana Ka Vaibhava, Saba Tumase Aata॥
Om Jai Lakshmi Mata॥

(Pada 6)
Shubha-Guna Mandira Sundara, Ksheerodadhi-Jata।
Ratna Chaturdasha Tum Bina, Koi Nahin Pata॥
Om Jai Lakshmi Mata॥

(Pada 7)
Mahalakshmiji Ki Aarati, Jo Koi Jana Gata।
Ura Aananda Samata, Papa Utara Jata॥
Om Jai Lakshmi Mata॥"""

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    colls = json.load(f)

updated_item = {
    "id": "drik_goddesses_2",
    "title": "लक्ष्मी माता आरती",
    "title_en": "Lakshmi Mata Aarti",
    "originalHindi": "ॐ जय लक्ष्मी माता, मैया जय लक्ष्मी माता",
    "en_line": "Om Jai Lakshmi Mata, Maiya Jai Lakshmi Mata",
    "hi_line": "ॐ जय लक्ष्मी माता, मैया जय लक्ष्मी माता",
    "sub": "Om Jai Lakshmi Mata • ॐ जय लक्ष्मी माता, मैया जय",
    "thumb": "assets/gallery/bal_durga.jpg",
    "audio_url": "https://www.youtube.com/watch?v=oec7CXRAfeE",
    "video_id": "oec7CXRAfeE",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lakshmi-mata/lakshmi-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang",
    "content": content_hindi,
    "meaning": meaning_text,
    "vidhi": vidhi_text,
    "significance": significance_text,
    "english_lyrics": english_lyrics_text
}

# Update in lakshmi
for i, it in enumerate(colls.get('lakshmi', {}).get('items', [])):
    if it['id'] == 'drik_goddesses_2':
        colls['lakshmi']['items'][i] = updated_item
        print("Updated lakshmi.items for drik_goddesses_2")

# Update in goddesses if present
for i, it in enumerate(colls.get('goddesses', {}).get('items', [])):
    if it['id'] == 'drik_goddesses_2':
        colls['goddesses']['items'][i] = updated_item
        print("Updated goddesses.items for drik_goddesses_2")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(colls, f, ensure_ascii=False, indent=2)
print("Saved final_granular_aarti_collections.json successfully.")

# 2. Update app.js at the last window.AARTI_COLLECTIONS
with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = None
for i, line in enumerate(lines):
    if i > 20000 and 'window.AARTI_COLLECTIONS = {' in line:
        start_idx = i
        break

if start_idx is None:
    raise Exception("Could not find start_idx for window.AARTI_COLLECTIONS")

end_idx = None
for i in range(start_idx, len(lines)):
    if lines[i].strip() == '};':
        end_idx = i
        break

if end_idx is None:
    raise Exception("Could not find end_idx for window.AARTI_COLLECTIONS")

print(f"Replacing lines {start_idx+1} to {end_idx+1} in app.js...")

new_json_str = json.dumps(colls, ensure_ascii=False, indent=2)
replacement_block = f"window.AARTI_COLLECTIONS = {new_json_str};\n"

new_lines = lines[:start_idx] + [replacement_block] + lines[end_idx+1:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully updated app.js with updated window.AARTI_COLLECTIONS!")
