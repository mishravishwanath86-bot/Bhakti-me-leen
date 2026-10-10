# -*- coding: utf-8 -*-
"""
Update drik_krishna_1 (आरती कुंजबिहारी की) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics
- Verse-by-verse detailed Bhavarth
- 4-2-1-7 Krishna Aarti Vidhi
- Significance (माहात्म्य)
- English Roman Transliteration
- Drik Panchang verified metadata (url, source, video_id, clean audio)
"""

import json
import re

KUNJ_BIHARI_DATA = {
    "id": "drik_krishna_1",
    "title": "आरती कुंजबिहारी की",
    "title_en": "Aarti Kunj Bihari Ki (Shri Krishna Aarti)",
    "en_line": "Aarti Kunj Bihari Ki, Shri Giridhar Krishna Murari Ki",
    "hi_line": "आरती कुंजबिहारी की, श्री गिरिधर कृष्णमुरारी की",
    "sub": "श्री गिरिधर कृष्ण मुरारी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_krishna_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=xcVv68gwc5Y",
    "video_id": "xcVv68gwc5Y",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-krishna/kunj-bihari-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ आरती कुंजबिहारी की, श्री गिरिधर कृष्ण मुरारी की ॥

आरती कुंजबिहारी की,
श्री गिरिधर कृष्ण मुरारी की।

गले में बैजंती माला, बजावै मुरली मधुर बाला।
श्रवण में कुण्डल झलकाला, नंद के आनंद नंदलाला।
गगन सम अंग कांति काली, राधिका चमक रही आली।
लतन में ठाढ़े बनमाली;
भ्रमर सी अलक, कस्तूरी तिलक,
चन्द्र सी झलक; ललित छवि श्यामा प्यारी की॥
श्री गिरिधर कृष्णमुरारी की॥

आरती कुंजबिहारी की,
श्री गिरिधर कृष्ण मुरारी की॥ (x2)

कनकमय मोर मुकुट बिलसै, देवता दरसन को तरसैं।
गगन सों सुमन रासि बरसै;
बजे मुरचंग, मधुर मिरदंग, ग्वालिन संग;
अतुल रति गोप कुमारी की॥
श्री गिरिधर कृष्णमुरारी की॥

आरती कुंजबिहारी की,
श्री गिरिधर कृष्ण मुरारी की॥ (x2)

जहां ते प्रकट भई गंगा, कलुष कलि हारिणि श्रीगंगा।
स्मरन ते होत मोह भंगा;
बसी सिव सीस, जटा के बीच, हरै अघ कीच;
चरन छवि श्रीबनवारी की॥
श्री गिरिधर कृष्णमुरारी की॥

आरती कुंजबिहारी की,
श्री गिरिधर कृष्ण मुरारी की॥ (x2)

चमकती उज्ज्वल तट रेनू, बज रही वृंदावन बेनू।
चहुं दिसि गोपि ग्वाल धेनू;
हंसत मृदु मंद, चांदनी चंद, कटत भव फंद;
टेर सुन दीन भिखारी की॥
श्री गिरिधर कृष्णमुरारी की॥

आरती कुंजबिहारी की,
श्री गिरिधर कृष्ण मुरारी की॥ (x2)

आरती कुंजबिहारी की, श्री गिरिधर कृष्ण मुरारी की॥
आरती कुंजबिहारी की, श्री गिरिधर कृष्ण मुरारी की॥""",

    "meaning": """॥ आरती कुंजबिहारी की — पद्यवार सम्पूर्ण पावन भावार्थ ॥

१. मंगलाचरण एवं युगल स्वरूप वंदना:
"आरती कुंजबिहारी की, श्री गिरिधर कृष्ण मुरारी की।
गले में बैजंती माला, बजावै मुरली मधुर बाला।
श्रवण में कुण्डल झलकाला, नंद के आनंद नंदलाला।
गगन सम अंग कांति काली, राधिका चमक रही आली।
लतन में ठाढ़े बनमाली; भ्रमर सी अलक, कस्तूरी तिलक,
चन्द्र सी झलक; ललित छवि श्यामा प्यारी की॥"

भावार्थ:
कुंज (वृंदावन के निकुंज वनों) में दिव्य रास-क्रीड़ा करने वाले परमब्रह्म भगवान श्री कृष्ण तथा गोवर्धन पर्वत को अपनी कनिष्ठिका अंगुली पर धारण करने वाले 'श्री गिरिधर' एवं मुर नामक असुर का संहार कर धर्म की स्थापना करने वाले 'श्री कृष्ण मुरारी' की हम श्रद्धापूर्वक आरती उतारते हैं।
भगवान के वक्षस्थल पर वनपुष्पों की दिव्य 'वैजयंती माला' सुशोभित है और वे अपने अधरों पर रखकर परम मधुर मुरली की तान छेड़ रहे हैं। उनके दोनों कानों में सूर्य-तुल्य दिव्य कुण्डल झिलमिला रहे हैं। वे नंदबाबा को परम आनंद प्रदान करने वाले प्यारे नंदनंदन हैं।
श्यामसुंदर के श्रीअंगों की आभा सघन मेघों (आकाश) के समान श्यामवर्ण और कांतिमान है, जिसके निकट उनकी आह्लादिनी शक्ति परम सुंदरी श्री राधारानी सखी के रूप में विद्युत की भांति दैदीप्यमान चमक रही हैं। निकुंज लताओं के बीच वनमाली श्रीकृष्ण त्रिभंगी मुद्रा में विराजमान हैं। उनके मस्तक पर भौंरों के समान घुंघराली अलकें (केश) लहरा रही हैं, ललाट पर सुगंधित कस्तूरी का तिलक सुशोभित है, और उनका मुखमंडल पूर्ण चंद्रमा की भांति चमक रहा है। इस प्रकार श्री श्यामा-प्यारी (राधा जी) और श्री गिरिधर कृष्णमुरारी की यह संयुक्त दिव्य छवि परम पावन व मनमोहिनी है।

२. मुकुट सौंदर्य, देव-वंदना एवं रास-उल्लास:
"कनकमय मोर मुकुट बिलसै, देवता दरसन को तरसैं।
गगन सों सुमन रासि बरसै; बजे मुरचंग, मधुर मिरदंग,
ग्वालिन संग; अतुल रति गोप कुमारी की॥"

भावार्थ:
भगवान श्रीकृष्ण के शीश पर स्वर्ण जटित दिव्य मोर मुकुट अनुपम शोभा बिखेर रहा है। इस अलौकिक सौंदर्य का एक पल दर्शन पाने के लिए स्वर्ग के समस्त देवगण भी तरसते हैं। भगवान के प्राकट्य और दिव्य दर्शन पर आकाश से देवतागण पुष्पों की अपार वर्षा कर रहे हैं।
वृंदावन में मोरचंग और मधुर मृदंग के दिव्य ताल बज रहे हैं। गोपियों और ग्वाल-बालों के संग ब्रज की गोप कुमारियां भगवान के प्रति अनन्य, अतुलनीय और निष्काम प्रेमरस (रति) में मग्न होकर आनंदपूर्वक नृत्य कर रही हैं। ऐसे सर्व-आकर्षक श्री गिरिधर कृष्णमुरारी की हम आरती करते हैं।

३. चरण-गंगा महिमा एवं मोक्ष प्रदायिनी शक्ति:
"जहां ते प्रकट भई गंगा, कलुष कलि हारिणि श्रीगंगा।
स्मरन ते होत मोह भंगा; बसी सिव सीस, जटा के बीच,
हरै अघ कीच; चरन छवि श्रीबनवारी की॥"

भावार्थ:
जिनके पावन चरणकमलों से कलयुग के समस्त पापों और मलों का हरण करने वाली परम पवित्र 'श्री गंगा जी' प्रकट हुई हैं। गंगा जी का केवल श्रद्धापूर्वक स्मरण करने मात्र से ही जीवों के सांसारिक मोह, अज्ञान और जन्म-मरण के बंधन छिन्न-भिन्न हो जाते हैं।
वही पावन गंगा जी भगवान देवाधिदेव महादेव शिव जी के मस्तक और जटाओं के मध्य विराजित होकर संसार के समस्त पाप रूपी कीचड़ को धो डालती हैं। ऐसे मोक्षदाता और त्रिभुवन-पति श्री वनवारी भगवान श्रीकृष्ण के पावन चरणकमलों की दिव्य छवि की हम आरती उतारते हैं।

४. यमुना तट, वेणु-नाद एवं भव-बंधन मुक्ति की प्रार्थना:
"चमकती उज्ज्वल तट रेनू, बज रही वृंदावन बेनू।
चहुं दिसि गोपि ग्वाल धेनू; हंसत मृदु मंद, चांदनी चंद,
कटत भव फंद; टेर सुन दीन भिखारी की॥"

भावार्थ:
यमुना जी के किनारे की उज्ज्वल बालू (रेणुका) श्वेत मोतियों की भांति चमक रही है और उस पावन तट पर भगवान श्रीकृष्ण की अमृतमयी वेणु (बांसुरी) गूंज रही है। उस अलौकिक मुरली की ध्वनि सुनकर चारों दिशाओं से गोपियां, ग्वाल-सखा और सुरभि गौएं प्रभु के चारों ओर खिंची चली आती हैं।
शरद पूर्णिमा के चंद्रमा की अमृतमयी चांदनी में प्रभु मंद-मंद मुस्करा रहे हैं। हे प्रभु! इस दीन-हीन, शरणागत भक्त की विनम्र पुकार (टेर) सुनकर कृपा करें और हमारे समस्त सांसारिक बंधनों (भव-फंदों) को काटकर हमें अपने श्रीचरणों की अविचल भक्ति व कृपा प्रदान करें। ऐसे परम करुणामय श्री गिरिधर कृष्णमुरारी की हम भाव-विभोर होकर आरती गाते हैं।""",

    "vidhi": """॥ श्री कृष्ण आरती शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधि ॥

शास्त्रों (हरिभक्तिविलास एवं नारद पंचरात्र) के अनुसार भगवान श्रीकृष्ण की आरती उतारने का विशेष विधान है:

१. ॐ (प्रणव) अथवा 'कृं' बीज से प्रारंभ:
आरती की थाल में कपूर या शुद्ध देसी घी का पंचमुखी अथवा सप्तमुखी दीपक प्रज्वलित करें। थाल में तुलसी दल, पीले पुष्प, रोली, चंदन, अक्षत और मोरपंख अवश्य रखें।

२. चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में भगवान श्रीकृष्ण के दोनों पावन चरणकमलों में ४ बार घुमाएं। यह भगवान के चरणों से गंगा-प्राकट्य और संसार-तारण की वंदना है।

३. नाभि-कमल पर २ बार घुमाएं:
इसके उपरांत दीपक को भगवान के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह संपूर्ण ब्रह्मांड के सृजन केंद्र और ब्रह्मा जी के प्राकट्य स्थल का नमन है।

४. मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को भगवान श्रीकृष्ण के परम सुंदर, मंद-मंद मुस्कराते हुए और मुरली धरे मुखारविन्द के समक्ष १ बार घुमाएं। इससे भक्त के चित्त का समस्त मोह और अज्ञान दूर होता है।

५. सम्पूर्ण श्रीविग्रह (सर्वांग) पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को भगवान के मोरमुकुट-मंडित मस्तक से लेकर चरणकमलों तक सम्पूर्ण श्रीअंगों पर भावपूर्वक ७ बार घुमाएं। यह सातों लोकों के स्वामी और पूर्ण पुरुषोत्तम की समग्र वंदना है।

(४ + २ + १ + ७ = कुल १४ बार चक्र पूर्ण करने से चौदह भुवनों की परिक्रमा का पुण्य फल प्राप्त होता है।)

६. समर्पण, पुष्पांजलि एवं आरती ग्रहण:
आरती पूर्ण होने पर शंखनाद और घंटे-घड़ियाल बजाएं। इसके उपरांत आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर छोड़ें (देवता को अर्पण करें)। दोनों हाथों से आरती की दिव्य अग्नि का तेज ग्रहण करें और शीश तथा नेत्रों पर लगाएं। अंत में 'ॐ श्री कृष्णाय नमः' बोलते हुए पीले पुष्पों की पुष्पांजलि अर्पित करें।""",

    "significance": """॥ आरती कुंजबिहारी की — आध्यात्मिक महत्व एवं फलश्रुति ॥

१. युगल स्वरूप की संपूर्ण आराधना:
'आरती कुंजबिहारी की' भगवान श्रीकृष्ण की सर्वाधिक लोकप्रिय और सर्वोत्कृष्ट आरती है। इसमें श्रीकृष्ण के बाल, किशोर और युगल (श्रीराधा-कृष्ण) तीनों स्वरूपों का एक साथ अलौकिक दर्शन होता है।

२. भव-बंधन और कलि-कल्मष का नाश:
आरती में स्पष्ट वर्णित है—"कटत भव फंद; टेर सुन दीन भिखारी की"। जो भक्त नित्य प्रातः अथवा संध्याकाल इस आरती का शुद्ध अंतःकरण से गान या श्रवण करता है, उसके जन्म-जन्मांतर के संचित पाप कट जाते हैं और सांसारिक बाधाएं समाप्त हो जाती हैं।

३. वैकुंठ एवं गोलोक धाम की प्राप्ति:
भगवान श्रीकृष्ण के चरणकमलों से प्रकट गंगा जी और उनके दिव्य वेणु-नाद का स्मरण करने से चित्त को परम शांति मिलती है। यह आरती घर में सुख-समृद्धि, गृहक्लेश का निवारण और मृत्यु उपरांत परम पद (गोलोक धाम) प्रदान करने वाली मानी गई है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छंदों पर आधारित है, जो अशुद्धियों से मुक्त और पूर्णतः प्रामाणिक है।""",

    "english_lyrics": """॥ Aarti Kunjabihari Ki, Shri Giridhara Krishna Murari Ki ॥

Aarti Kunjabihari Ki,
Shri Giridhara Krishna Murari Ki।

Gale Mein Baijanti Mala, Bajavai Murli Madhur Bala।
Shravan Mein Kundal Jhalkala, Nand Ke Anand Nandlala।
Gagan Sam Ang Kanti Kali, Radhika Chamak Rahi Aali।
Latan Mein Thadhe Banmali;
Bhramar Si Alak, Kasturi Tilak,
Chandra Si Jhalak; Lalit Chhavi Shyama Pyari Ki॥
Shri Giridhara Krishna Murari Ki॥

Aarti Kunjabihari Ki,
Shri Giridhara Krishna Murari Ki॥ (x2)

Kanakmay Mor Mukut Bilsai, Devta Darsan Ko Tarsain।
Gagan Son Suman Rasi Barsai;
Baje Murchang, Madhur Mirdang, Gwalin Sang;
Atul Rati Gop Kumari Ki॥
Shri Giridhara Krishna Murari Ki॥

Aarti Kunjabihari Ki,
Shri Giridhara Krishna Murari Ki॥ (x2)

Jahan Te Prakat Bhai Ganga, Kalush Kali Harini Shri Ganga।
Smaran Te Hot Moh Bhanga;
Basi Siv Sees, Jata Ke Beech, Harai Agh Keech;
Charan Chhavi Shri Banwari Ki॥
Shri Giridhara Krishna Murari Ki॥

Aarti Kunjabihari Ki,
Shri Giridhara Krishna Murari Ki॥ (x2)

Chamakati Ujjwal Tat Renu, Baj Rahi Vrindavan Benu।
Chahun Disi Gopi Gwal Dhenu;
Hansat Mridu Mand, Chandani Chand, Katat Bhav Fand;
Ter Sun Deen Bhikhari Ki॥
Shri Giridhara Krishna Murari Ki॥

Aarti Kunjabihari Ki,
Shri Giridhara Krishna Murari Ki॥ (x2)

Aarti Kunjabihari Ki, Shri Giridhara Krishna Murari Ki॥
Aarti Kunjabihari Ki, Shri Giridhara Krishna Murari Ki॥"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'krishna' in collections and 'items' in collections['krishna']:
    k_items = collections['krishna']['items']
    found = False
    for i, it in enumerate(k_items):
        if it.get('id') == 'drik_krishna_1' or 'कुंजबिहारी' in it.get('hi_line', ''):
            k_items[i] = KUNJ_BIHARI_DATA
            found = True
            print(f"[OK] Replaced item at index {i} in JSON")
            break
    if not found:
        k_items.insert(0, KUNJ_BIHARI_DATA)
        print("[OK] Inserted Kunj Bihari Aarti at index 0 in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate the drik_krishna_1 item block inside app.js
pattern = r'\{\s*"id":\s*"drik_krishna_1"[^}]*\}'
# Since content is multiline and has nested quotes, let's locate the krishna collection's items array
krishna_idx = app_js.find('"krishna": {')
if krishna_idx != -1:
    items_idx = app_js.find('"items": [', krishna_idx)
    if items_idx != -1:
        # Find start of first object in items
        obj_start = app_js.find('{', items_idx)
        # Find end of this object (look for id: drik_krishna_2 or next object)
        next_obj = app_js.find('"id": "drik_krishna_2"', obj_start)
        if next_obj != -1:
            # find the comma or closing brace right before next_obj
            obj_end = app_js.rfind('}', obj_start, next_obj) + 1
            old_block = app_js[obj_start:obj_end]
            new_block = json.dumps(KUNJ_BIHARI_DATA, ensure_ascii=False, indent=8)
            app_js = app_js[:obj_start] + new_block + app_js[obj_end:]
            print("[OK] Successfully replaced drik_krishna_1 block in app.js")
        else:
            print("[WARN] Could not find drik_krishna_2 to delimit block")
else:
    print("[WARN] krishna collection not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
