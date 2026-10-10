# -*- coding: utf-8 -*-
"""
Update drik_goddesses_6 (Ganga Mata Aarti / ॐ जय गंगे माता, मैया जय गंगे माता) in:
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

GANGA_DATA = {
    "id": "drik_goddesses_6",
    "title": "ॐ जय गंगे माता, मैया जय गंगे माता",
    "title_en": "Ganga Mata Aarti (Om Jai Gange Mata)",
    "en_line": "Om Jai Gange Mata, Maiya Jai Gange Mata",
    "hi_line": "ॐ जय गंगे माता, मैया जय गंगे माता",
    "sub": "मोक्षदायिनी पतितपावनी माँ गंगा जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_ganga_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=fUkRcVulBlQ",
    "video_id": "fUkRcVulBlQ",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/ganga-mata/ganga-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ आरती श्री गंगाजी ॥
(ॐ जय गंगे माता)

ॐ जय गंगे माता,
मैया जय गंगे माता।
जो नर तुमको ध्याता,
मनवांछित फल पाता॥

ॐ जय गंगे माता॥

चन्द्र-सी ज्योति तुम्हारी,
जल निर्मल आता।
शरण पड़े जो तेरी,
सो नर तर जाता॥

ॐ जय गंगे माता॥

पुत्र सगर के तारे,
सब जग को ज्ञाता।
कृपा दृष्टि हो तुम्हारी,
त्रिभुवन सुख दाता॥

ॐ जय गंगे माता॥

एक बार जो प्राणी,
शरण तेरी आता।
यम की त्रास मिटाकर,
परमगति पाता॥

ॐ जय गंगे माता॥

आरती मातु तुम्हारी,
जो नर नित गाता।
सेवक वही सहज में,
मुक्ति को पाता॥

ॐ जय गंगे माता॥""",
    "meaning": """॥ आरती श्री गंगाजी (ॐ जय गंगे माता) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती भगवान विष्णु के पावन श्रीचरणों से निःसृत, देवाधिदेव महादेव की जटाओं में विराजित और राजा भगीरथ के तप से भूतल पर अवतरित पतितपावनी मोक्षदायिनी माँ गंगा की पावन वंदना है।)

१. प्रथम पद (टेक / मुखड़ा — पतितपावनी माँ गंगा वंदना व मनोरथ सिद्धि):
"ॐ जय गंगे माता, मैया जय गंगे माता।
जो नर तुमको ध्याता, मनवांछित फल पाता॥
ॐ जय गंगे माता॥"

भावार्थ:
हे समस्त पापों का संहार करने वाली जगत्जननी माँ गंगे! आपकी सदा ही जय हो, जय-जयकार हो। जो भी श्रद्धालु मनुष्य पूर्ण श्रद्धा और निष्ठा से आपका ध्यान व स्मरण करता है, वह धर्म, अर्थ, काम और मोक्ष सहित समस्त मनवांछित फल प्राप्त करता है।

२. द्वितीय पद (चन्द्र-समान दिव्य ज्योति, निर्मल जल व भव-तारण):
"चन्द्र-सी ज्योति तुम्हारी, जल निर्मल आता।
शरण पड़े जो तेरी, सो नर तर जाता॥
ॐ जय गंगे माता॥"

भावार्थ:
हे माँ! आपकी दिव्य कांति और आभा पूर्णिमा के शीतल चंद्रमा के समान अत्यंत मनोरम और तेजोमयी है। आपका पावन अमृततुल्य जल सदा निर्मल, पवित्र और दोषरहित प्रवाहित होता रहता है। जो भी आर्त जीव आपकी पावन शरण में आ जाता है, वह इस भव-सागर के जन्म-मरण के चक्र से सहज ही पार उतर (तर) जाता है।

३. तृतीय पद (सगर-पुत्रों का उद्धार व त्रिभुवन सुखदाता):
"पुत्र सगर के तारे, सब जग को ज्ञाता।
कृपा दृष्टि हो तुम्हारी, त्रिभुवन सुख दाता॥
ॐ जय गंगे माता॥"

भावार्थ:
हे देवनदी! राजा सगर के साठ हजार शापग्रस्त पुत्रों का उद्धार कर आपने उन्हें सद्गति प्रदान की—यह सत्य संपूर्ण संसार भली-भांति जानता है। हे जगत्कल्याणी माँ! जिस पर आपकी एक बार भी कृपा-दृष्टि हो जाती है, उसे तीनों लोकों (स्वर्ग, मर्त्य, पाताल) का सम्पूर्ण सुख और आनंद सहज ही प्राप्त हो जाता है।

४. चतुर्थ पद (यम-त्रास निवारण व परमगति प्राप्ति):
"एक बार जो प्राणी, शरण तेरी आता।
यम की त्रास मिटाकर, परमगति पाता॥
ॐ जय गंगे माता॥"

भावार्थ:
हे मोक्षदायिनी सुरसरि! जो भी प्राणी जीवन में केवल एक बार भी सच्चे हृदय से आपकी पावन शरण में आकर आपका जल स्पर्श या आचमन कर लेता है, उसके यमराज का समस्त भय और यम-यातनाएं सदा के लिए मिट जाती हैं और वह अंत में श्रीहरि के परम पद (परमगति) को प्राप्त होता है।

५. पंचम पद (फलश्रुति — नित्य आरती गान से सहज मुक्ति):
"आरती मातु तुम्हारी, जो नर नित गाता।
सेवक वही सहज में, मुक्ति को पाता॥
ॐ जय गंगे माता॥"

भावार्थ:
हे करुणामयी मैया! जो भी साधक अथवा सेवक नित्य-नियम से प्रेमपूर्वक आपकी यह पावन आरती गाता है, वह इस संसार के समस्त बंधनों और कष्टों से मुक्त होकर सहज रूप से मोक्ष और परम शांति को प्राप्त करता है।""",
    "vidhi": """॥ माँ गंगा जी की आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीपदान विधान ॥

हरिद्वार (हर की पौड़ी), ऋषिकेश तथा काशी के दशाश्वमेध घाट की परम पावन परंपरानुसार आरती विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल के पंचमुखी अथवा बहुमुखी दीप-स्तंभ में गाय के शुद्ध घी का दीपक अथवा कर्पूर प्रज्वलित करें। थाल में लाल व पीले पुष्प, गुलाब की पंखुड़ियां, रोली, चंदन, अक्षत, धूप और नैवेद्य (दूध की मिठाई या बताशे) रखें। 'ॐ नमो भगवत्यै गङ्गायै नमः' अथवा 'गङ्गे च यमुने चैव गोदावरि सरस्वति। नर्मदे सिन्धु कावेरि जलेऽस्मिन् संनिधिं कुरु॥' मन्त्र का स्मरण करें।

२. पावन जल-तरंगों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में माँ गंगा की अमृतमयी जलधारा के सम्मुख ४ बार घुमाएं। यह चारों वेदों, चारों पुरुषार्थों की सिद्धि और चरण-शरण प्राप्ति का प्रतीक है।

३. प्रवाह-मध्य में २ बार घुमाएं:
तत्पश्चात दीपक को गंगा जी के पावन प्रवाह-केंद्र के समक्ष २ बार घुमाएं। यह जीवन-दायिनी शक्ति और सृष्टि के पालन-पोषण का नमन है।

४. शांत जल-दर्पण पर १ बार घुमाएं:
इसके उपरांत दीपक को माँ गंगा के शांत, शीतल मुखारविन्द-तुल्य जल-दर्पण के समक्ष १ बार घुमाएं। इससे मानसिक संताप, अहंकार और अविद्या का नाश होता है।

५. सम्पूर्ण विस्तीर्ण जल-धारा पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को हिमालय के उद्गम (गोमुख) से लेकर सागर-संगम तक विस्तीर्ण संपूर्ण पावन धारा पर भावपूर्वक ७ बार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवन की शुद्धि व प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, शंख-नाद एवं दीपदान:
आरती पूर्ण होने पर शंख, घंटा, डमरू बजाएं और 'हर हर गंगे, जय माँ गंगे' का त्रिवार जयघोष करें। पत्तों के दोने में पुष्प व दीप सजाकर बहते जल में भावपूर्वक दीपदान करें तथा आरती का पावन ताप दोनों हाथों से ग्रहण कर शीश व नयनों पर लगाएं।""",
    "significance": """॥ श्री गंगा माता आरती (ॐ जय गंगे माता) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. त्रिपथगा व मोक्षदायिनी महिमा:
माँ गंगा स्वर्ग, पृथ्वी और पाताल तीनों लोकों में प्रवाहित होकर 'त्रिपथगा' कहलाती हैं। यह आरती साधक को तीनों लोकों के अधिपति भगवान विष्णु, भगवान शिव और माँ गंगा के संयुक्त आशीर्वाद से परिपूर्ण करती है।

२. जन्म-जन्मांतर के पापों का क्षालन:
"शरण पड़े जो तेरी, सो नर तर जाता" — गंगा जी केवल एक नदी नहीं, साक्षात ब्रह्म-द्रव हैं। इस आरती के नित्य गान अथवा गंगा तट पर इसके श्रवण से मनुष्य के कायिक, वाचिक और मानसिक तीनों प्रकार के पाप भस्म हो जाते हैं।

३. सगर-सुत उद्धार — पितृ-शांति व मुक्ति:
जैसे भगीरथ की प्रार्थना पर माँ गंगा ने राजा सगर के ६०,००० पुत्रों का उद्धार किया, वैसे ही इस आरती के श्रद्धापूर्वक पाठ से कुल के पितरों को परम शांति व सद्गति मिलती है और पितृदोष शांत होता है।

४. यम-भय निवारण व अकाल संकट मुक्ति:
"यम की त्रास मिटाकर, परमगति पाता" — इस आरती के नियमित पाठ से अकाल मृत्यु का भय दूर होता है, घर-परिवार में असाध्य रोग शांत होते हैं और अंत समय में सद्गति प्राप्त होती है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक पाठ पर शत-प्रतिशत आधारित है, जो हरिद्वार, काशी और प्रयागराज के पावन घाटों पर नित्य संध्या-आरती में श्रद्धापूर्वक गाई जाती है।""",
    "english_lyrics": """॥ Shri Ganga Mata Aarti ॥
(Om Jai Gange Mata)

Om Jai Gange Mata,
Maiya Jai Gange Mata।
Jo Nara Tumako Dhyaata,
Manavaanchhita Phala Paata॥

Om Jai Gange Mata॥

Chandra-See Jyoti Tumhaaree,
Jala Nirmala Aata।
Sharana Pade Jo Teree,
So Nara Tara Jaata॥

Om Jai Gange Mata॥

Putra Sagara Ke Taare,
Saba Jaga Ko Gyaata।
Kripaa Drishti Ho Tumhaaree,
Tribhuvana Sukha Daata॥

Om Jai Gange Mata॥

Eka Baara Jo Praanee,
Sharana Teree Aata।
Yama Kee Traasa Mitaakara,
Paramagati Paata॥

Om Jai Gange Mata॥

Aarti Maatu Tumhaaree,
Jo Nara Nita Gaata।
Sevaka Wahee Sahaja Mein,
Mukti Ko Paata॥

Om Jai Gange Mata॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['ganga', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_6':
                fg_data[cat_name]['items'][i] = GANGA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_6 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_6':
                    cdata['items'][i] = GANGA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_6 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(GANGA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_6"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_6 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_6 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
