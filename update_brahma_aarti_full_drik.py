# -*- coding: utf-8 -*-
"""
Update drik_gods_11 (Lord Brahma Aarti / पितु मातु सहायक स्वामी सखा) in:
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

BRAHMA_DATA = {
    "id": "drik_gods_11",
    "title": "पितु मातु सहायक स्वामी सखा",
    "title_en": "Lord Brahma Aarti (Pitu Matu Sahayaka Swami Sakha)",
    "en_line": "Pitu Matu Sahayaka Swami Sakha, Tuma Hee Eka Naatha Hamaare Ho",
    "hi_line": "पितु मातु सहायक स्वामी सखा, तुम ही एक नाथ हमारे हो",
    "sub": "सृष्टिकर्ता भगवान श्री ब्रह्मा जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_brahma_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=vEhKiZFlDKc",
    "video_id": "vEhKiZFlDKc",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-brahma/shri-brahma-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ आरती श्री ब्रह्मा जी ॥
(पितु मातु सहायक स्वामी सखा)

पितु मातु सहायक स्वामी सखा,
तुम ही एक नाथ हमारे हो।
जिनके कुछ और आधार नहीं,
तिनके तुम ही रखवारे हो॥

सब भाँति सदा सुखदायक हो,
दुःख निर्गुण नाशन हारे हो।
प्रतिपाल करो सिगरे जग को,
अतिशय करुणा उर धारे हो॥

भुलि हैं हम तो तुमको,
तुम तो हमरी सुधि नाहिं बिसारे हो।
उपकारन को कछु अन्त नहीं,
छिन ही छिन जो विस्तारे हो॥

महाराज महा महिमा तुम्हरी,
मुझसे बिरले बुधवारे हो।
शुभ शान्ति निकेतन प्रेमनिधि,
मन मन्दिर के उजियारे हो॥

इस जीवन के तुम जीवन हो,
इन प्राणन के तुम प्यारे हो।
तुम सों प्रभु पाय 'प्रताप' हरि,
केहि के अब और सहारे हो॥""",
    "meaning": """॥ आरती श्री ब्रह्मा जी (पितु मातु सहायक स्वामी सखा) — सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती सृष्टि के रचयिता, चतुर्मुख प्रजापति भगवान ब्रह्मा जी की परम करुणा, शरणागति और वात्सल्य भाव की अत्यंत मार्मिक वंदना है।)

१. प्रथम पद — एक मात्र परम आश्रय व नाथ वंदना:
"पितु मातु सहायक स्वामी सखा,
तुम ही एक नाथ हमारे हो।
जिनके कुछ और आधार नहीं,
तिनके तुम ही रखवारे हो॥"

भावार्थ:
हे जगत्पिता ब्रह्मा जी! आप ही हमारे पिता हैं, आप ही माता हैं, आप ही हर परिस्थिति में सहायक, हमारे स्वामी और परम आत्मीय सखा (मित्र) हैं। इस संपूर्ण ब्रह्मांड में आप ही हमारे एकमात्र सच्चे प्रभु और नाथ हैं। इस संसार में जिनका कोई अन्य सहारा या अवलंब नहीं होता, जो सर्वथा निराश्रित और असहाय हैं, उनके एकमात्र रक्षक और पालनकर्ता केवल आप ही हैं।

२. द्वितीय पद — सर्वसुखदाता, दुःखनिवारक व जगत्पालक:
"सब भाँति सदा सुखदायक हो,
दुःख निर्गुण नाशन हारे हो।
प्रतिपाल करो सिगरे जग को,
अतिशय करुणा उर धारे हो॥"

भावार्थ:
हे प्रजापति देव! आप सब प्रकार से अपने भक्तों को सदा सुख और आनंद प्रदान करने वाले हैं। आप जीवों के समस्त भौतिक, दैहिक, दैविक और सांसारिक दुखों का समूल नाश करने वाले हैं। आप अपने हृदय (उर) में अपार और अहैतुकी करुणा धारण करके इस समस्त चराचर जगत (सिगरे जग) का नित्य वात्सल्यपूर्वक प्रतिपालन व पोषण करते हैं।

३. तृतीय पद — असीम उपकार व विस्मृति निवारक कृपा:
"भुलि हैं हम तो तुमको,
तुम तो हमरी सुधि नाहिं बिसारे हो।
उपकारन को कछु अन्त नहीं,
छिन ही छिन जो विस्तारे हो॥"

भावार्थ:
हे कृपालु पिता! सांसारिक माया और अज्ञान के वशीभूत होकर हम भले ही आपको भूल जाते हैं, किंतु आप अपनी परम वात्सल्यमयी दया से हमारी सुध (स्मृति व चिंता) कभी नहीं बिसारते। प्रत्येक क्षण आप हमारे ऊपर कृपा बरसाते रहते हैं। आपके हम पर किए गए उपकारों का कोई ओर-छोर अथवा अंत नहीं है, जो प्रति-पल, क्षण-प्रतिक्षण हमारे जीवन में निरंतर विस्तृत और प्रकट होते रहते हैं।

४. चतुर्थ पद — अपरंपार महिमा, शांति निकेतन व मन-उजियारे:
"महाराज महा महिमा तुम्हरी,
मुझसे बिरले बुधवारे हो।
शुभ शान्ति निकेतन प्रेमनिधि,
मन मन्दिर के उजियारे हो॥"

भावार्थ:
हे महाराजाधिराज! आपकी महिमा अत्यंत अपार, दिव्य और अगम्य है। संसारी बुद्धिजीवी अथवा अल्पज्ञ प्राणी आपकी इस विराट महिमा का पार नहीं पा सकते। आप परम शुभता, अखंड शांति के पावन धाम (निकेतन) और अलौकिक प्रेम के अथाह निधि (सागर) हैं। आप हमारे अंतःकरण रूपी मन-मंदिर के समस्त अंधकार को दूर करने वाले परम दिव्य प्रकाश (उजियारे) हैं।

५. पंचम पद — जीवन-प्राण आधार व अनन्य शरणागति:
"इस जीवन के तुम जीवन हो,
इन प्राणन के तुम प्यारे हो।
तुम सों प्रभु पाय 'प्रताप' हरि,
केहि के अब और सहारे हो॥"

भावार्थ:
हे परमात्मा! आप इस नश्वर जीवन के मूल जीवन (चेतना तत्त्व) हैं और हमारे इन प्राणों के सर्वाधिक प्रियतम आधार हैं। हे प्रभु! आपके चरणों में शरणागति और आपका परम 'प्रताप' व कृपा पाकर अब हमें किसी अन्य सांसारिक सहारे की तनिक भी आवश्यकता नहीं रह गई है। हम सर्वभाव से आपके ही पावन चरणकमलों में समर्पित हैं।""",
    "vidhi": """॥ भगवान श्री ब्रह्मा जी आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधान ॥

सृष्टि के आदि-रचयिता, चतुर्मुख ब्रह्मा जी की पावन आरती का शास्त्रोक्त विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल, तांबे या रजत की शुद्ध थाली में गाय के शुद्ध घी का दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाल में श्वेत व पीले पुष्प, कमल पुष्प, रोली, अक्षत, दुर्वा, श्वेत चंदन, यज्ञोपवीत तथा शुद्ध जल का पात्र रखें। 'ॐ ब्रह्मणे नमः' अथवा 'ॐ चतुराननाय विद्महे कमण्डलुधराय धीमहि तन्नो ब्रह्मा प्रचोदयात्' मन्त्र का भावपूर्वक स्मरण करें।

२. पावन चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में भगवान ब्रह्मा जी के कोमल चरणकमलों के समक्ष ४ बार घुमाएं। यह चराचर सृष्टि में धर्म, अर्थ, काम और मोक्ष के चार पुरुषार्थों की सिद्धि तथा चरण-शरण प्राप्ति का प्रतीक है।

३. नाभि-कमल पर २ बार घुमाएं:
तत्पश्चात दीपक को भगवान ब्रह्मा जी के नाभि-मंडल के समक्ष २ बार घुमाएं। यह हिरण्यगर्भ और सृष्टि के उद्गम मूल परब्रह्म का आदरपूर्वक वंदन है।

४. चतुर्मुख मुखारविन्द पर १ बार घुमाएं:
इसके उपरांत दीपक को ब्रह्मा जी के चारों वेदों (ऋक्, यजुः, साम, अथर्व) का उद्घोष करने वाले पावन मुखारविन्द के समक्ष १ बार घुमाएं। यह ज्ञान, विद्या और सत्य की प्राप्ति हेतु प्रार्थना है।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को कमण्डलु, अक्षमाला, वेद-ग्रंथ व पद्मासन से लेकर चरणकमलों तक सम्पूर्ण पावन विग्रह पर ७ बार श्रद्धापूर्वक घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवन की शुद्धि व प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, शंख-नाद एवं आरती ग्रहण:
आरती पूर्ण होने पर घंटा, शंख और मृदंग बजाएं। आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती का पावन ताप ग्रहण कर अपने शीश, मुख और नयनों पर लगाएं तथा 'ब्रह्मा जी की जय', 'सृष्टिकर्ता प्रभु की जय' का जयघोष करें।""",
    "significance": """॥ श्री ब्रह्मा आरती (पितु मातु सहायक स्वामी सखा) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. परम शरणागति व वात्सल्य भाव की पराकाष्ठा:
"पितु मातु सहायक स्वामी सखा" — यह आरती साधक को ईश्वर के साथ माता, पिता, स्वामी और सखा चारों घनिष्ठ संबंधों का अनुभव कराती है। इसके नित्य गान से साधक का अकेलापन दूर होता है और जीवन में सर्वत्र ईश्वरीय संरक्षण की अनुभूति होती है।

२. बुद्धि, ज्ञान व अध्ययन में असीम सफलता:
भगवान ब्रह्मा वेदों के ज्ञाता और ज्ञान के अधिष्ठाता हैं। विद्यार्थियों और साधकों द्वारा इस आरती का पाठ करने से एकाग्रता, मेधा शक्ति, स्मृति और आध्यात्मिक विवेक में अभूतपूर्व वृद्धि होती है।

३. समस्त कष्टों व दुखों का शमन:
"सब भाँति सदा सुखदायक हो, दुःख निर्गुण नाशन हारे हो" — इस पावन आरती के भावपूर्ण गायन से गृहस्थ जीवन के कलह, मानसिक अवसाद, अज्ञात भय और जीवन के संकट दूर होते हैं तथा घर में सुख, शांति और सौभाग्य का वास होता है।

४. कृतज्ञता एवं मन-मंदिर की शुद्धि:
"शुभ शान्ति निकेतन प्रेमनिधि, मन मन्दिर के उजियारे हो" — यह आरती मनुष्य को ईश्वर के उपकारों के प्रति कृतज्ञ बनाती है और हृदय को अहंकार, काम, क्रोध से मुक्त कर अंतःकरण में दिव्य शांति व प्रेम का दीप प्रज्वलित करती है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक पाठ पर शत-प्रतिशत आधारित है, जो पुष्कर तीर्थ सहित समस्त पावन अवसरों पर ब्रह्मा जी की पूजा में श्रद्धापूर्वक गाई जाती है।""",
    "english_lyrics": """॥ Lord Brahma Aarti ॥
(Pitu Matu Sahayaka Swami Sakha)

Pitu Maatu Sahaayaka Swaamee Sakhaa,
Tuma Hee Eka Naatha Hamaare Ho।
Jinake Kuchha Aura Aadhaar Naheen,
Tinake Tuma Hee Rakhavaare Ho॥

Saba Bhaanti Sadaa Sukhadaayaka Ho,
Duhkha Nirguna Naashana Haare Ho।
Pratipaala Karo Sigare Jaga Ko,
Atishaya Karunaa Ura Dhaare Ho॥

Bhuli Hain Hama To Tumako,
Tuma To Hamaree Sudhi Naahin Bisaare Ho।
Upakaarana Ko Kachhu Anta Naheen,
Chhina Hee Chhina Jo Vistaare Ho॥

Mahaaraaja Mahaa Mahimaa Tumharee,
Mujhase Birale Budhavaare Ho।
Shubha Shaanti Niketana Premanidhi,
Mana Mandira Ke Ujiyaare Ho॥

Isa Jeevana Ke Tuma Jeevana Ho,
Ina Praanana Ke Tuma Pyaare Ho।
Tuma Son Prabhu Paaya 'Prataapa' Hari,
Kehi Ke Aba Aura Sahaare Ho॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['surya', 'gods']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_gods_11':
                fg_data[cat_name]['items'][i] = BRAHMA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_gods_11 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_gods_11':
                    cdata['items'][i] = BRAHMA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_gods_11 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Replace all occurrences of the drik_gods_11 block in app.js
# We can find each occurrence of `"id": "drik_gods_11"` and replace its enclosing object `{ ... }`
new_block_str = json.dumps(BRAHMA_DATA, ensure_ascii=False, indent=8)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_gods_11"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_gods_11 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_gods_11 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
