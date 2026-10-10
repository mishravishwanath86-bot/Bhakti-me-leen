# -*- coding: utf-8 -*-
"""
Update drik_gods_13 (Lord Batuka Bhairava Aarti / जय भैरव देवा प्रभु जय) in:
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

BATUKA_DATA = {
    "id": "drik_gods_13",
    "title": "जय भैरव देवा प्रभु जय",
    "title_en": "Lord Batuka Bhairava Aarti (Jai Bhairava Deva Prabhu Jai)",
    "en_line": "Jai Bhairava Deva Prabhu Jai Bhairava Deva",
    "hi_line": "जय भैरव देवा प्रभु जय भैरव देवा",
    "sub": "आपदुद्धारक भगवान बटुक भैरव जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_bhairav_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=KeZbSn3sTVY",
    "video_id": "KeZbSn3sTVY",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/lord-bhairava/batuka-bhairava-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री भैरव आरती ॥
(जय भैरव देवा, प्रभु जय भैरव देवा)

जय भैरव देवा प्रभु
जय भैरव देवा,
सुर नर मुनि सब
करते प्रभु तुम्हरी सेवा॥

ॐ जय भैरव देवा...॥

तुम पाप उद्धारक
दुःख सिन्धु तारक,
भक्तों के सुखकारक
भीषण वपु धारक॥

ॐ जय भैरव देवा...॥

वाहन श्वान विराजत
कर त्रिशूल धारी,
महिमा अमित तुम्हारी
जय जय भयहारी॥

ॐ जय भैरव देवा...॥

तुम बिन शिव सेवा
सफल नहीं होवे,
चतुर्वतिका दीपक
दर्शन दुःख खोवे॥

ॐ जय भैरव देवा...॥

तेल चटकि दधि मिश्रित
भाषावलि तेरी,
कृपा कीजिये भैरव
करिये नहिं देरी॥

ॐ जय भैरव देवा...॥

पाँवों घूंघरू बाजत
डमरू डमकावत,
बटुकनाथ बन बालक
जन मन हरषावत॥

ॐ जय भैरव देवा...॥

बटुकनाथ की आरती
जो कोई जन गावे,
कहे धरणीधर वह नर
मन वांछित फल पावे॥

ॐ जय भैरव देवा...॥""",
    "meaning": """॥ श्री बटुक भैरव आरती (जय भैरव देवा प्रभु जय) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती देवाधिदेव भगवान शिव के अत्यंत सौम्य व तेजस्वी बाल/बटुक रुद्रावतार 'आपदुद्धारक श्री बटुक भैरव नाथ' की पावन स्तुति है। जीवन के घोर संकटों, अकाल मृत्यु के भय, ग्रह-दोषों तथा तांत्रिक बाधाओं के शमन हेतु इस आरती का नित्य सांध्य गायन सर्व-सिद्धिप्रद माना गया है।)

१. प्रथम पद (टेक / मुखड़ा — प्रभु वंदना व सुर-मुनि सेवा):
"जय भैरव देवा प्रभु जय भैरव देवा,
सुर नर मुनि सब करते प्रभु तुम्हरी सेवा॥
ॐ जय भैरव देवा...॥"
भावार्थ: हे देवाधिदेव, आपदुद्धारक भगवान भैरव! आपकी सदा ही जय हो, जय-जयकार हो। समस्त देवगण, मनुष्य, सिद्ध मुनिजन और गंधर्व आपकी नित्य अनन्य भाव से सेवा, पूजा और वंदना करते हैं।

२. द्वितीय पद (पाप-उद्धारक, दुःख-सिन्धु तारक व भीषण वपु धारक):
"तुम पाप उद्धारक दुःख सिन्धु तारक,
भक्तों के सुखकारक भीषण वपु धारक॥
ॐ जय भैरव देवा...॥"
भावार्थ: हे कृपानिधान भैरव देव! आप शरणागत जीवों के समस्त संचित पापों का नाश कर उनका उद्धार करने वाले हैं। आप संसार रूपी दुःख के अथाह सागर से पार लगाने वाले परम तारक हैं। अपने अनन्य भक्तों को समस्त सुख, शांति व आनंद प्रदान करने वाले हैं तथा अधर्मियों, दुष्टों व असुरों के संहार हेतु अत्यंत तेजस्वी व भयानक शरीर (भीषण वपु) धारण करते हैं।

३. तृतीय पद (श्वान सवारी, त्रिशूल धारण व भयहारी स्वरूप):
"वाहन श्वान विराजत कर त्रिशूल धारी,
महिमा अमित तुम्हारी जय जय भयहारी॥
ॐ जय भैरव देवा...॥"
भावार्थ: हे प्रभु! आप निष्ठावान श्वान (कुत्ते) की दिव्य सवारी पर अत्यंत सुशोभित हैं और अपने करकमलों में तीक्ष्ण त्रिशूल धारण किए हुए हैं। आपकी पावन महिमा असीम, अपार और वेदों द्वारा भी अगम्य है। हे समस्त प्रकार के भयों, संकटों, रोगों और मृत्यु-त्रास का हरण करने वाले 'भयहारी' भैरवनाथ! आपकी बारंबार जय हो।

४. चतुर्थ पद (शिव सेवा की सफलता व चतुर्वतिका दीपक दर्शन):
"तुम बिन शिव सेवा सफल नहीं होवे,
चतुर्वतिका दीपक दर्शन दुःख खोवे॥
ॐ जय भैरव देवा...॥"
भावार्थ: हे क्षेत्रपाल भैरव देव! आपकी कृपा और अनुमति के बिना भगवान शिव की उपासना, मंत्र-साधना अथवा काशी-दर्शन कभी पूर्ण व सफल नहीं हो सकता। जो भी भक्त आपके सम्मुख सरसों अथवा तिल के तेल का चार बत्तियों वाला चौमुखी दीपक (चतुर्वतिका दीपक) प्रज्वलित करता है, उसके दर्शन मात्र से ही जीवन के समस्त दुःख, दारिद्र्य और व्याधियां तत्काल नष्ट हो जाती हैं।

५. पंचम पद (दधि-मिश्रित भोग, भाषावलि व त्वरित कृपा याचना):
"तेल चटकि दधि मिश्रित भाषावलि तेरी,
कृपा कीजिये भैरव करिये नहिं देरी॥
ॐ जय भैरव देवा...॥"
भावार्थ: हे बटुकनाथ! आपको शुद्ध तेल, उड़द के वड़े तथा दही-भात (दधि-मिश्रित अन्न) की दिव्य भाषावलि (नैवेद्य/बलि-भोग) अत्यंत प्रिय है। हे भक्तवत्सल भैरव! अपने इस दीन-हीन सेवक पर शीघ्र ही कृपा कीजिए और हमारे संकटों को हरने में तनिक भी विलंब न कीजिए।

६. षष्ठ पद (पाँवों में घुंघरू, डमरू-नाद व बाल रूप में आनंद-संचार):
"पाँवों घूंघरू बाजत डमरू डमकावत,
बटुकनाथ बन बालक जन मन हरषावत॥
ॐ जय भैरव देवा...॥"
भावार्थ: हे प्रभु! आपके पावन श्रीचरणों में नूपुर व घुंघरू मधुर झंकार कर रहे हैं और आपके करकमल में सुशोभित डमरू 'डम-डम' की दिव्य मंगल ध्वनि उत्पन्न कर रहा है। आप परम कृपालु बाल रूप 'बटुकनाथ' बनकर अपने सभी भक्तों के मन को अलौकिक आनंद और वात्सल्य से प्रफुल्लित (हरषावत) कर देते हैं।

७. सप्तम पद (फलश्रुति — धरणीधर कृत स्तुति व मनोवांछित फल प्राप्ति):
"बटुकनाथ की आरती जो कोई जन गावे,
कहे धरणीधर वह नर मन वांछित फल पावे॥
ॐ जय भैरव देवा...॥"
भावार्थ: जो भी पुण्यात्मा मनुष्य भगवान बटुक भैरव की इस दिव्य आरती का नित्य प्रातः अथवा सांध्यकाल में श्रद्धापूर्वक गान करता है, भक्त धरणीधर जी कहते हैं कि वह साधक इस लोक में समस्त सुख-सौभाग्य और मनोवांछित फल प्राप्त कर अंत में परम कल्याण को प्राप्त करता है।""",
    "vidhi": """॥ श्री बटुक भैरव जी की आरती — काशी व उज्जैन शास्त्रोक्त 4-2-1-7 विधान ॥

भगवान आपदुद्धारक बटुक भैरव जी की आरती उतारने का विशेष शास्त्रोक्त एवं संकट-निवारक विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
आरती में विशेष रूप से 'चतुर्वतिका दीपक' (चार बत्तियों वाला चौमुखी दीपक) प्रज्वलित करने का विधान है। इसमें सरसों का तेल, तिल का तेल अथवा शुद्ध गाय का घी उपयोग करें। धूप में गुग्गल व लोबान सुलगाएं। थाली में सिंदूर, अष्टगंध, चमेली का तेल, उड़द की दाल के वड़े, दही-भात, इमरती या जलेबी, बेसन के लड्डू, कलावा, मदार/आक के पुष्प, बिल्वपत्र और एक साबुत नींबू अर्पित करें।

२. आरती घुमाने का विशेष तांत्रिक व वैदिक '४-२-१-७' क्रम:
आरती को केवल सामान्य रूप से नहीं, अपितु भैरव रक्षा-चक्र के अनुसार '४-२-१-७' क्रम में घुमाएं:
• श्रीचरणों के समक्ष ४ बार: चारों पुरुषार्थों (धर्म, अर्थ, काम, मोक्ष) की प्राप्ति, अहंकार विसर्जन व पृथ्वी तत्व की शुद्धि हेतु।
• नाभि मंडल के समक्ष २ बार: उदर-रोग, मानसिक तनाव, नाभि-चक्र (मणिपूर चक्र) की शुद्धि व भय-मुक्ति हेतु।
• मुखारविंद के समक्ष १ बार: बटुकनाथ के सौम्य बाल रूप के दर्शन, वाणी-सिद्धि व दृष्टि-दोष निवारण हेतु।
• समग्र विग्रह के समक्ष ७ बार: दसों दिशाओं, सप्त धातुओं और सातों चक्रों से समस्त तांत्रिक, ऊपरी व नकारात्मक शक्तियों के निष्कासन हेतु गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की शुद्धि व संपूर्ण भैरव प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष बटुक भैरव मंत्र:
आरती आरंभ करने से पूर्व 'ॐ ह्रीं बटुकाय आपदुद्धारणाय कुरु कुरु बटुकाय ह्रीं ॐ' अथवा 'ॐ भ्रं बटुक भैरवाय नमः' मंत्र का उच्चारण करें।

४. आरती उपरांत झाड़ा, तिलक व प्रसाद:
आरती पूर्ण होने पर कर्पूर दीप को शीतल जल की तीन बूंदें देकर आचमन करें। भैरव जी के चरणों से सिंदूर लेकर मस्तक या कंठ पर तिलक लगाएं। उपस्थित भक्तों में दही-भात, उड़द के बड़े या इमरती का प्रसाद वितरित करें।""",
    "significance": """॥ श्री बटुक भैरव आरती (जय भैरव देवा प्रभु जय) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'तुम बिन शिव सेवा सफल नहीं होवे' — शिव-पूजा की अनिवार्यता:
शास्त्रों और पुराणों में स्पष्ट विधान है कि भगवान भैरव देवाधिदेव शिव के प्रधान गण और काशी के क्षेत्रपाल हैं। इनकी अनुमति और पूजन के बिना भगवान शिव की उपासना, काशी-यात्रा और ज्योतिर्लिंग दर्शन का पूर्ण फल प्राप्त नहीं होता।

२. आपदुद्धारक स्वरूप — घोर संकटों से तत्काल मुक्ति:
भगवान बटुक भैरव को 'आपदुद्धारक' (आपदाओं का उद्धार करने वाला) कहा गया है। इस आरती के नियमित गान से जीवन के असाध्य संकट, अकाल मृत्यु का भय, गंभीर दुर्घटनाएं, झूठे मुकदमे और आकस्मिक विपत्तियां तत्काल दूर हो जाती हैं।

३. 'चतुर्वतिका दीपक दर्शन दुःख खोवे' — चौमुखी दीपक का चमत्कार:
आरती में साक्षात उल्लेख है कि चार बत्तियों वाले चौमुखी दीपक के दर्शन से साधक के समस्त संचित दुःख और दरिद्रता नष्ट हो जाते हैं। यह दीपक घर में सकारात्मक ऊर्जा और सुरक्षा कवच का निर्माण करता है।

४. राहु-केतु, शनि व नजर-दोष से अभय रक्षा:
ज्योतिष शास्त्र के अनुसार भगवान बटुक भैरव की उपासना से क्रूर ग्रह राहु-केतु के सर्प-दोष, नजर-दोष तथा शनि देव की साढ़ेसाती व ढैया के दुष्प्रभाव पूर्णतः शांत हो जाते हैं।

५. धरणीधर कृत प्रामाणिक फलश्रुति:
भक्त धरणीधर के अनुसार, जो भी साधक निष्कपट भाव से इस आरती का नित्य पाठ करता है, उसे धर्म, अर्थ, काम और मोक्ष सहित समस्त मनवांछित फल प्राप्त होते हैं।""",
    "english_lyrics": """॥ Shri Bhairava Aarti ॥
(Jai Bhairava Deva Prabhu Jai)

Jai Bhairava Deva Prabhu
Jai Bhairava Deva,
Sura Nara Muni Saba
Karate Prabhu Tumharee Seva॥

Om Jai Bhairava Deva...॥

Tuma Papa Uddhaaraka
Duhkha Sindhu Taaraka,
Bhakton Ke Sukhakaaraka
Bheeshana Vapu Dhaaraka॥

Om Jai Bhairava Deva...॥

Vaahana Shwana Viraajata
Kara Trishoola Dhaaree,
Mahima Amita Tumharee
Jai Jai Bhayaharee॥

Om Jai Bhairava Deva...॥

Tuma Bina Shiva Seva
Saphala Naheen Hove,
Chaturvatika Deepaka
Darshana Duhkha Khove॥

Om Jai Bhairava Deva...॥

Tela Chataki Dadhi Mishrita
Bhashavali Teree,
Kripa Keejiye Bhairava
Kariye Nahin Deree॥

Om Jai Bhairava Deva...॥

Paanvon Ghoongharoo Baajata
Damaroo Damakaavata,
Batukanaatha Bana Baalaka
Jana Mana Harashaavata॥

Om Jai Bhairava Deva...॥

Batukanaatha Kee Aarti
Jo Koee Jana Gaave,
Kahe Dharaneedhara Vaha Nara
Mana Vaanchhita Phala Paave॥

Om Jai Bhairava Deva...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['bhairav', 'gods']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_gods_13':
                fg_data[cat_name]['items'][i] = BATUKA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_gods_13 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_gods_13':
                    cdata['items'][i] = BATUKA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_gods_13 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(BATUKA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_gods_13"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_gods_13 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_gods_13 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
