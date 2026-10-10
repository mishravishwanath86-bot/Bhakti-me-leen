# -*- coding: utf-8 -*-
"""
Update drik_goddesses_20 (Devi Radha Aarti / आरती श्री श्रीवृषभानुलली की) in:
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

RADHA_DATA = {
    "id": "drik_goddesses_20",
    "title": "आरती श्री श्रीवृषभानुलली की",
    "title_en": "Devi Radha Aarti (Aarti Shri Vrishbhanulali Ki)",
    "en_line": "Aarti Shri Vrishbhanulali Ki, Sata-Chita-Aananda Kanda-Kalee Ki",
    "hi_line": "आरति श्रीवृषभानुलली की, सत-चित-आनन्द कन्द-कली की",
    "sub": "ह्लादिनी शक्ति श्री राधा रानी जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_radha_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=03D0yCvg_G0",
    "video_id": "03D0yCvg_G0",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shri-radha/devi-radhika-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ देवी राधिका आरती ॥
(आरती श्री श्रीवृषभानुलली की)

आरति श्रीवृषभानुलली की।
सत-चित-आनन्द कन्द-कली की॥
भयभन्जिनि भव-सागर-तारिणि,
पाप-ताप-कलि-कल्मष-हारिणि,
दिव्यधाम गोलोक-विहारिणि,
जनपालिनि जगजननि भली की॥

आरति श्रीवृषभानुलली की।
सत-चित-आनन्द कन्द-कली की॥

अखिल विश्व-आनन्द-विधायिनि,
मंगलमयी सुमंगलदायिनि,
नन्दनन्दन-पदप्रेम प्रदायिनि,
अमिय-राग-रस रंग-रली की॥

आरति श्रीवृषभानुलली की।
सत-चित-आनन्द कन्द-कली की॥

नित्यानन्दमयी आह्लादिनि,
आनन्दघन-आनन्द-प्रसाधिनि,
रसमयि, रसमय-मन-उन्मादिनि,
सरस कमलिनी कृष्ण-अली की॥

आरति श्रीवृषभानुलली की।
सत-चित-आनन्द कन्द-कली की॥

नित्य निकुन्जेश्वरि राजेश्वरि,
परम प्रेमरूपा परमेश्वरि,
गोपिगणाश्रयि गोपिजनेश्वरि,
विमल विचित्र भाव-अवली की॥

आरति श्रीवृषभानुलली की।
सत-चित-आनन्द कन्द-कली की॥""",
    "meaning": """॥ श्री राधा रानी जी की आरती (आरती श्री श्रीवृषभानुलली की) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती साक्षात परब्रह्म भगवान श्रीकृष्ण की स्वरूपभूता ह्लादिनी महाशक्ति, गोलोक की स्वामिनी तथा बरसाने की अधीश्वरी श्री राधा रानी (लाड़ली जी) की पावन निकुंज-स्तुति है। राधाष्टमी, शरद पूर्णिमा तथा नित्य सांध्यकाल में इस आरती का गान साधक के हृदय में विशुद्ध प्रेमाभक्ति का संचार करता है।)

१. प्रथम पद (टेक / मुखड़ा — सच्चिदानंद कंद-कली व भवसागर-तारिणी):
"आरति श्रीवृषभानुलली की। सत-चित-आनन्द कन्द-कली की॥
भयभन्जिनि भव-सागर-तारिणि, पाप-ताप-कलि-कल्मष-हारिणि,
दिव्यधाम गोलोक-विहारिणि, जनपालिनि जगजननि भली की॥"
भावार्थ: हे वृषभानुनन्दिनी श्री राधा रानी! हम आपकी परम पावन आरती उतारते हैं। आप साक्षात सत्-चित्-आनंद (सच्चिदानंद) रूपी कंद (मूल) की मनोहर खिली हुई कली हैं। आप शरणागत भक्तों के समस्त सांसारिक भयों का भंजन करने वाली तथा इस अगम भवसागर से पार उतारने वाली परम तारिणी हैं। आप त्रिविध तापों (दैहिक, दैविक, भौतिक) तथा कलिकाल के समस्त पापों और कलुषताओं का हरण करने वाली हैं। आप नित्य दिव्य गोलोक धाम में प्रभु श्रीकृष्ण के संग लीला-विहार करने वाली, संपूर्ण जगत का वात्सल्यपूर्वक पालन करने वाली परम कृपालु जगज्जननी हैं।

२. द्वितीय पद (अखिल विश्व आनंद-विधायिनी व नंदनंदन-पदप्रेम प्रदायिनी):
"अखिल विश्व-आनन्द-विधायिनि, मंगलमयी सुमंगलदायिनि,
नन्दनन्दन-पदप्रेम प्रदायिनि, अमिय-राग-रस रंग-रली की॥
आरति श्रीवृषभानुलली की...॥"
भावार्थ: हे श्रीजी! आप संपूर्ण ब्रह्मांड में अलौकिक परमानंद का विधान करने वाली और समस्त मंगलों का भी परम मूल सुमंगल प्रदान करने वाली मंगलमयी देवी हैं। आप भगवान नंदनंदन श्रीकृष्ण के श्रीचरणों में अनन्य, निष्काम प्रेमाभक्ति प्रदान करने वाली हैं तथा प्रेम, रस और अमृतमयी दिव्य अनुराग की रंग-लीलाओं की अधिष्ठात्री हैं। आपकी अहैतुकी कृपा के बिना श्रीकृष्ण के अनन्य प्रेम-रस का आस्वादन असंभव है।

३. तृतीय पद (ह्लादिनी शक्ति, रस-उन्मादिनी व कृष्ण-भ्रमर की कमलिनी):
"नित्यानन्दमयी आह्लादिनि, आनन्दघन-आनन्द-प्रसाधिनि,
रसमयि, रसमय-मन-उन्मादिनि, सरस कमलिनी कृष्ण-अली की॥
आरति श्रीवृषभानुलली की...॥"
भावार्थ: हे नित्य आनंदस्वरूपा, परात्पर ह्लादिनी शक्ति! आप साक्षात आनंदघन भगवान श्रीकृष्ण को भी परम आनंदित और आह्लादित करने वाली हैं। आप प्रेम-रस से परिपूर्ण होकर रसिकराज श्रीकृष्ण के मन को अपने दिव्य अनुराग से उन्मादित करने वाली हैं। आप वह अमृतमयी, खिली हुई सरस कमलिनी हैं, जिसके चारों ओर कृष्ण रूपी मधुप (भ्रमर/अली) निरंतर मँडराते और रस-पान करते रहते हैं।

४. चतुर्थ पद (नित्य निकुंजेश्वरी, राजेश्वरी व गोपिजनों की अधिष्ठात्री):
"नित्य निकुन्जेश्वरि राजेश्वरि, परम प्रेमरूपा परमेश्वरि,
गोपिगणाश्रयि गोपिजनेश्वरि, विमल विचित्र भाव-अवली की॥
आरति श्रीवृषभानुलली की...॥"
भावार्थ: हे श्री वृंदावन धाम के दिव्य नित्य निकुंजों की स्वामिनी, त्रिभुवन की राजेश्वरी! आप साक्षात परम प्रेम-स्वरूपा परमेश्वरी हैं। आप समस्त गोपी-गणों की परम आश्रयदात्री और गोपियों की ईश्वरी हैं। आप विमल, अनिर्वचनीय और विचित्र दिव्य भाव-तरंगों की अधिष्ठात्री हैं। ऐसी परम दयामयी, करुणामयी श्री वृषभानुनंदिनी लाड़ली जी की हम बारंबार आरती गाते हैं और युगल चरणों में आत्मसमर्पण करते हैं।""",
    "vidhi": """॥ श्री राधा रानी जी की आरती — बरसाना व श्रीवृन्दावन शास्त्रोक्त 4-2-1-7 विधान ॥

श्री लाड़ली जी (वृषभानु-नन्दिनी) की आरती उतारने का विशेष शास्त्रोक्त एवं निकुंज-रस विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
आरती हेतु शुद्ध गाय के घी का पंचमुखी दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाली में रोली, कुंकुम, अष्टगंध चंदन, अक्षत, सुंगधित चमेली, मोगरा व गुलाब के पुष्प, नीलकमल, कलावा, इत्र, मिश्री, माखन, रबड़ी अथवा मालपुए का भोग सजाएं।

२. आरती घुमाने का विशेष शास्त्रीय '४-२-१-७' क्रम:
श्री राधा रानी के युगल विग्रह के समक्ष '४-२-१-७' के शास्त्रोक्त क्रम से आरती घुमाएं:
• श्रीचरणकमलों के समक्ष ४ बार: चारों पुरुषार्थों की प्राप्ति, चरण-शरण, दास्य-भाव व अहंकार विसर्जन हेतु।
• नाभि मंडल के समक्ष २ बार: काम-क्रोध के शमन, अंतःकरण की शुद्धि व ह्लादिनी ऊर्जा की प्राप्ति हेतु।
• मुखारविंद के समक्ष १ बार: दिव्य मंद-मुस्कान के दर्शन, ज्ञान-चक्षु जागरण व दृष्टि-दोष निवारण हेतु।
• संपूर्ण श्रीविग्रह के समक्ष ७ बार: सप्त-चक्रों, षड्रिपुओं के नाश और राधा-कृष्ण के युगल स्वरूप के प्रति संपूर्ण आत्म-समर्पण के साथ गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की शुद्धि व संपूर्ण युगल प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष राधा मंत्र व स्तुति:
आरती आरंभ करने से पूर्व 'ॐ श्री राधायै नमः' अथवा 'तप्तकाञ्चनगौराङ्गि राधे वृन्दावनेश्वरि । वृषभानुसुते देवि प्रणमामि हरिप्रिये ॥' मन्त्र का स्मरण करें।

४. आरती उपरांत प्रदक्षिणा व चरणामृत:
आरती पूर्ण होने पर कर्पूर दीप पर शीतल जल छिड़ककर आचमन करें। 'राधे-राधे' का संकीर्तन करते हुए ३ बार प्रदक्षिणा करें तथा उपस्थित भक्तों में माखन-मिश्री व चरणामृत का प्रसाद वितरित करें।""",
    "significance": """॥ श्री राधा रानी आरती (आरती श्री श्रीवृषभानुलली की) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. श्रीकृष्ण-प्रेम व अनुग्रह की एकमात्र कुंजी:
श्रीमद्भागवत व पद्म पुराण के अनुसार, भगवान श्रीकृष्ण की पूर्ण कृपा और प्रेम केवल श्री राधा रानी के माध्यम से ही सुलभ होता है। जो साधक निष्काम भाव से श्री राधा जी की शरण लेता है, श्रीकृष्ण उसके हृदय में स्वतः ही विराजित हो जाते हैं।

२. 'सत-चित-आनन्द कन्द-कली' — सच्चिदानंद स्वरूप की अनुभूति:
यह आरती गोलोक धाम के गूढ़ निकुंज-रस का साक्षात सार है। इसके नित्य गान से साधक का अंतःकरण रागानुगा भक्ति, अलौकिक शांति और परमानंद से परिपूर्ण हो जाता है।

३. समस्त पाप-ताप व कलि-कल्मष का शमन:
आरती में स्पष्ट वर्णित है—"भयभन्जिनि भव-सागर-तारिणि, पाप-ताप-कलि-कल्मष-हारिणि।" इसके नित्य श्रवण व गायन से जन्म-जन्मांतर के संचित पाप, आधि-व्याधियां और कलिकाल का भय तत्काल नष्ट हो जाता है।

४. राधाष्टमी व शरद पूर्णिमा का महापुण्य:
भाद्रपद मास के शुक्ल पक्ष की अष्टमी (राधाष्टमी) तथा शरद पूर्णिमा के पावन अवसर पर इस आरती का गान करने से गोलोक धाम की प्राप्ति और दांपत्य जीवन में अगाध माधुर्य व प्रेम का वरदान मिलता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक चार गहन छंद पदों पर पूर्णतः आधारित है, जो श्रीधाम बरसाना, नन्दगांव, वृन्दावन व कोटि-कोटि वैष्णव मंदिरों में नित्य सांध्यकाल में गाई जाती है।""",
    "english_lyrics": """॥ Shri Radha Rani Ki Aarti ॥
(Aarti Shri Vrishbhanulali Ki)

Aarti Shri Vrishbhanulali Ki।
Sata-Chita-Aananda Kanda-Kalee Ki॥
Bhayabhanjini Bhava-Saagara-Taarini,
Paapa-Taapa-Kali-Kalmasha-Haarini,
Divyadhaama Goloka-Vihaarini,
Janapaalini Jagajanani Bhalee Ki॥

Aarti Shri Vrishbhanulali Ki।
Sata-Chita-Aananda Kanda-Kalee Ki॥

Akhila Vishwa-Aananda-Vidhaayini,
Mangalamayee Sumangaladaayini,
Nandanandana-Padaprema Pradaayini,
Amiya-Raaga-Rasa Ranga-Ralee Ki॥

Aarti Shri Vrishbhanulali Ki।
Sata-Chita-Aananda Kanda-Kalee Ki॥

Nityaanandamayee Aahlaadini,
Aanandaghana-Aananda-Prasaadhini,
Rasamayee, Rasamaya-Mana-Unmaadini,
Sarasa Kamalinee Krishna-Alee Ki॥

Aarti Shri Vrishbhanulali Ki।
Sata-Chita-Aananda Kanda-Kalee Ki॥

Nitya Nikunjeshwari Raajeshwari,
Parama Premaroopaa Parameshwari,
Gopiganaashrayi Gopijaneshwari,
Vimala Vichitra Bhaava-Avali Ki॥

Aarti Shri Vrishbhanulali Ki।
Sata-Chita-Aananda Kanda-Kalee Ki॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['radha', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_20':
                fg_data[cat_name]['items'][i] = RADHA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_20 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_20':
                    cdata['items'][i] = RADHA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_20 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(RADHA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_20"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_20 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_20 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
