# -*- coding: utf-8 -*-
"""
Update drik_krishna_3 (आरती जुगल किशोर की कीजै / श्री गोपाल आरती) in:
1. final_granular_aarti_collections.json
2. app.js
with 100% complete Drik Panchang data:
- Full Devanagari lyrics
- Verse-by-verse detailed Bhavarth
- 4-2-1-7 Jugal Kishor Aarti Vidhi
- Significance (माहात्म्य)
- English Roman Transliteration
- Drik Panchang verified metadata
"""

import json

GOPALA_DATA = {
    "id": "drik_krishna_3",
    "title": "आरती जुगल किशोर की कीजै",
    "title_en": "Shri Gopala Aarti (Aarti Jugal Kishor Ki Kijai)",
    "en_line": "Aarti Jugal Kishor Ki Kijai, Radhe Dhan Nyauchhavar Kijai",
    "hi_line": "आरती जुगल किशोर की कीजै, राधे धन न्यौछावर कीजै",
    "sub": "श्री गोपाल • युगल किशोर • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_krishna_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=xcVv68gwc5Y",
    "video_id": "xcVv68gwc5Y",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-krishna/shri-gopala-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री गोपाल की आरती ॥
(आरती जुगल किशोर की कीजै)

आरती जुगल किशोर की कीजै,
राधे धन न्यौछावर कीजै॥ (x2)

रवि शशि कोटि बदन की शोभा,
ताहि निरखि मेरा मन लोभा।
आरती जुगल किशोर की कीजै...।

गौर श्याम मुख निरखत रीझै,
प्रभु को स्वरुप नयन भर पीजै।
कंचन थार कपूर की बाती,
हरि आये निर्मल भई छाती।
आरती जुगल किशोर की कीजै...।

फूलन की सेज फूलन की माला,
रतन सिंहासन बैठे नन्दलाला।
मोर मुकुट कर मुरली सोहै,
नटवर वेष देखि मन मोहै।
आरती जुगल किशोर की कीजै...।

आधा नील पीत पटसारी,
कुञ्ज बिहारी गिरिवरधारी।
श्री पुरुषोत्तम गिरवरधारी,
आरती करें सकल ब्रजनारी।
आरती जुगल किशोर की कीजै...।

नन्द लाला वृषभानु किशोरी,
परमानन्द स्वामी अविचल जोरी।
आरती जुगल किशोर की कीजै,
राधे धन न्यौछावर कीजै।
आरती जुगल किशोर की कीजै...।""",

    "meaning": """॥ आरती जुगल किशोर की कीजै — पद्यवार सम्पूर्ण पावन भावार्थ ॥

१. मंगलाचरण एवं युगल-स्वरूप समर्पण:
"आरती जुगल किशोर की कीजै, राधे धन न्यौछावर कीजै।
रवि शशि कोटि बदन की शोभा, ताहि निरखि मेरा मन लोभा।"

भावार्थ:
ब्रह्म और पराशक्ति के संयुक्त स्वरूप श्रीराधा-कृष्ण (युगल किशोर) की हम अनन्य प्रेमभाव से पावन आरती उतारते हैं। इस अलौकिक युगल छवि पर अपना सर्वस्व, समस्त धन-संपदा और प्राण न्यौछावर करते हैं।
युगल सरकार के मुखारविन्द की दिव्य आभा करोड़ों सूर्यों के समान तेजस्वी और करोड़ों चंद्रमाओं के समान परम शीतल व सुखदायिनी है। इस अलौकिक, अनिर्वचनीय सौंदर्य को देखकर मेरा मन अनायास ही मुग्ध और प्रेमासक्त हो गया है।

२. गौर-श्याम छवि एवं कंचन-थाल दीप आराधना:
"गौर श्याम मुख निरखत रीझै, प्रभु को स्वरुप नयन भर पीजै।
कंचन थार कपूर की बाती, हरि आये निर्मल भई छाती।"

भावार्थ:
एक ओर श्री राधारानी का तप्त-कांचन-वर्ण (गौर) मुखमंडल और दूसरी ओर श्यामसुंदर का नव-जलधर-वर्ण (श्याम) मुखारविन्द—इस गौर-श्याम के अद्भुत संगम को देखकर हृदय परम तृप्त और रीझ जाता है। भक्त अपने नेत्र-कमलों के प्याले भरकर प्रभु के इस दिव्य रूप-रस का निरंतर पान करना चाहता है।
स्वर्ण (कंचन) की थाली में कपूर की दिव्य ज्योति जगमगा रही है। हृदय के मंदिर में युगल सरकार के पधारते ही चित्त के समस्त विकार, मलिनताएं और संताप शांत हो गए हैं तथा हृदय परम निर्मल व शांत हो गया है।

३. पुष्प-सज्जा, रत्न सिंहासन एवं नटवर रूप:
"फूलन की सेज फूलन की माला, रतन सिंहासन बैठे नन्दलाला।
मोर मुकुट कर मुरली सोहै, नटवर वेष देखि मन मोहै।"

भावार्थ:
सुगंधित वनपुष्पों की दिव्य सेज बिछी है, कंठ में दिव्य पुष्पमालाएं सुशोभित हैं और मणियों-रत्नों से जटित भव्य सिंहासन पर नंदनंदन श्रीकृष्ण श्रीराधा जी के संग विराजित हैं।
मस्तक पर मोर-मुकुट और हाथों में अमृत-वर्षी मुरली अत्यंत शोभायमान है। प्रभु के इस त्रिभंग, नटवर वेश को देखकर तीनों लोकों का मन सम्मोहित हो जाता है।

४. पीतांबर-नीलांबर संगम एवं ब्रज-नारियों की आरती:
"आधा नील पीत पटसारी, कुञ्ज बिहारी गिरिवरधारी।
श्री पुरुषोत्तम गिरवरधारी, आरती करें सकल ब्रजनारी।"

भावार्थ:
युगल विग्रह में एक ओर राधारानी की नीली साड़ी (नीलांबर) और दूसरी ओर श्रीकृष्ण का पीतांबर (पीत पट) मिलकर युगल-वस्त्राभूषणों की अद्वितीय छटा प्रस्तुत कर रहे हैं। वे निकुंजों में विहार करने वाले कुंजबिहारी तथा गोवर्धन पर्वत को धारण करने वाले पुरुषोत्तम भगवान हैं।
ब्रज की समस्त गोपिकाएं और सखियां मिलकर अपार आनंद व निष्काम प्रेम से अपने आराध्य युगल किशोर की आरती उतार रही हैं।

५. अविचल युगल जोड़ी एवं परम आनंद की प्राप्ति:
"नन्द लाला वृषभानु किशोरी, परमानन्द स्वामी अविचल जोरी।
आरती जुगल किशोर की कीजै, राधे धन न्यौछावर कीजै।"

भावार्थ:
नंदबाबा के दुलारे कन्हैया और राजा वृषभानु की राजदुलारी श्री राधा जी की यह दिव्य युगल जोड़ी नित्य, शाश्वत और अविचल (सदा एकरस रहने वाली) है। यह जोड़ी ही समस्त जीवों को परम आनंद प्रदान करने वाली स्वामिनी और स्वामी हैं।
ऐसी सर्व-मंगलकारी युगल सरकार की हम बारंबार आरती उतारते हैं और अपने जीवन का सर्वस्व उनके पावन चरणों में समर्पित करते हैं।""",

    "vidhi": """॥ श्री जुगल किशोर आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधि ॥

श्रीराधा-कृष्ण (युगल किशोर) की संयुक्त आरती उतारने का विशेष शास्त्रोक्त एवं रसिक-परंपरा का विधान है:

१. थाल सज्जा एवं युगल भाव:
स्वर्ण अथवा पीतल की थाल में कपूर या शुद्ध देसी घी का दीपक प्रज्वलित करें। थाल में पीले पुष्प (श्रीकृष्ण हेतु), लाल/श्वेत पुष्प (श्रीराधा हेतु), तुलसी दल, चंदन, रोली और अक्षत रखें। 'ॐ श्रीराधा-कृष्णाभ्यां नमः' का ध्यान करें।

२. पावन चरणों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में श्री युगल सरकार (राधा-कृष्ण) के दोनों पावन चरणकमलों में ४ बार घुमाएं। यह चार वेदों और चारों पुरुषार्थों (धर्म, अर्थ, काम, मोक्ष) का युगल चरणों में समर्पण है।

३. नाभि-मंडल पर २ बार घुमाएं:
इसके उपरांत दीपक को दोनों के दिव्य नाभि-कमल के समक्ष २ बार घुमाएं। यह चराचर ब्रह्मांड के सृजन स्थल का नमन है।

४. युगल मुखारविन्द पर १ बार घुमाएं:
तत्पश्चात दीपक को श्रीराधा और श्रीकृष्ण के मंद-मंद मुस्कराते, अमृतमयी गौर-श्याम मुखकमलों के समक्ष १ बार घुमाएं। इससे अज्ञान और संशय का नाश होता है।

५. सम्पूर्ण युगल विग्रह पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को मोरमुकुट व शीश से लेकर चरणकमलों तक सम्पूर्ण युगल विग्रह पर भावपूर्वक ७ बार घुमाएं। यह सातों लोकों के स्वामियों की समग्र वंदना है।

(४ + २ + १ + ७ = कुल १४ बार प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण एवं पुष्पांजलि:
आरती पूर्ण होने पर आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती का पावन ताप ग्रहण कर शीश व नेत्रों पर लगाएं तथा 'श्री युगल सरकार की जय' का जयघोष करें।""",

    "significance": """॥ आरती जुगल किशोर की कीजै — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. संपूर्ण युगल कृपा एवं प्रेम-भक्ति:
'आरती जुगल किशोर की कीजै' भगवान श्रीकृष्ण और श्रीराधारानी की संयुक्त आराधना की सर्वश्रेष्ठ आरती है। जहां केवल कृष्ण की आराधना से ज्ञान और वैराग्य मिलता है, वहीं युगल आराधना से पराभक्ति और परम प्रेम की प्राप्ति होती है।

२. चित्त की निर्मलता एवं संताप नाश:
"हरि आये निर्मल भई छाती"—इस आरती के नियमित गान से हृदय के संशय, कलह, वासना और अशांति का नाश होता है तथा मन में शीतलता व पवित्रता का वास होता है।

३. दांपत्य सुख एवं अविचल प्रेम:
युगल किशोर की यह अविचल जोड़ी दांपत्य जीवन में सुख, शांति, परस्पर प्रेम और सौहार्द का वरदान देती है।

४. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छंदों पर आधारित है।""",

    "english_lyrics": """॥ Shri Gopala Ki Aarti ॥
(Aarti Jugal Kishor Ki Kijai)

Aarti Jugal Kishor Ki Kijai,
Radhe Dhan Nyauchhavar Kijai॥ (x2)

Ravi Shashi Koti Badan Ki Shobha,
Tahi Nirakhi Mera Man Lobha।
Aarti Jugal Kishor Ki Kijai...।

Gaur Shyam Mukh Nirakhat Reejhai,
Prabhu Ko Swarup Nayan Bhar Peejai।
Kanchan Thaar Kapoor Ki Baati,
Hari Aaye Nirmal Bhai Chhaati।
Aarti Jugal Kishor Ki Kijai...।

Phoolan Ki Sej Phoolan Ki Mala,
Ratan Singhasan Baithe Nandlala।
Mor Mukut Kar Murli Sohai,
Natwar Vesh Dekhi Man Mohai।
Aarti Jugal Kishor Ki Kijai...।

Aadha Neel Peet Patsari,
Kunj Bihari Girivardhari।
Shri Purushottam Girvardhari,
Aarti Karein Sakal Brijnari।
Aarti Jugal Kishor Ki Kijai...।

Nand Lala Vrishbhanu Kishori,
Paramanand Swami Avichal Jori।
Aarti Jugal Kishor Ki Kijai,
Radhe Dhan Nyauchhavar Kijai।
Aarti Jugal Kishor Ki Kijai...।"""
}

# 1. Update final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

if 'krishna' in collections and 'items' in collections['krishna']:
    k_items = collections['krishna']['items']
    found = False
    for i, it in enumerate(k_items):
        if it.get('id') == 'drik_krishna_3' or 'जुगल किशोर' in it.get('hi_line', '') or 'जुगल किशोर' in it.get('title', ''):
            k_items[i] = GOPALA_DATA
            found = True
            print(f"[OK] Replaced Gopala item at index {i} in JSON")
            break
    if not found:
        k_items.insert(2, GOPALA_DATA)
        print("[OK] Inserted Gopala item at index 2 in JSON")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)
print("[OK] Saved final_granular_aarti_collections.json")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Locate drik_krishna_3 in app.js
obj_start = app_js.find('"id": "drik_krishna_3"')
if obj_start != -1:
    brace_start = app_js.rfind('{', 0, obj_start)
    next_obj = app_js.find('"id": "drik_krishna_4"', obj_start)
    if next_obj != -1:
        brace_end = app_js.rfind('}', brace_start, next_obj) + 1
        new_block = json.dumps(GOPALA_DATA, ensure_ascii=False, indent=8)
        app_js = app_js[:brace_start] + new_block + app_js[brace_end:]
        print("[OK] Successfully replaced drik_krishna_3 block in app.js")
    else:
        print("[WARN] Could not find drik_krishna_4")
else:
    print("[WARN] drik_krishna_3 not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("[OK] Saved app.js")
