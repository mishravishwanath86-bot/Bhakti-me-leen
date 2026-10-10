# -*- coding: utf-8 -*-
"""
Update drik_goddesses_13 (Tulasi Mata Aarti / जय जय तुलसी माता) in:
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

TULASI_DATA = {
    "id": "drik_goddesses_13",
    "title": "जय जय तुलसी माता",
    "title_en": "Tulasi Mata Aarti (Jai Jai Tulasi Mata)",
    "en_line": "Jai Jai Tulasi Mata, Sabakee Sukhadata Vara Mata",
    "hi_line": "जय जय तुलसी माता, सबकी सुखदाता वर माता",
    "sub": "हरिप्रिया माँ तुलसी जी की पावन स्तुति-आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_tulsi_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=4yVdfundS_o",
    "video_id": "4yVdfundS_o",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/tulasi-mata/tulasi-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री तुलसी जी की आरती ॥
(जय जय तुलसी माता)

जय जय तुलसी माता, सबकी सुखदाता वर माता।
सब योगों के ऊपर, सब रोगों के ऊपर,
रुज से रक्षा करके भव त्राता।

जय जय तुलसी माता...॥

बहु पुत्री है श्यामा, सूर वल्ली है ग्राम्या,
विष्णु प्रिय जो तुमको सेवे, सो नर तर जाता।

जय जय तुलसी माता...॥

हरि के शीश विराजत त्रिभुवन से हो वंदित,
पतित जनों की तारिणि, तुम हो विख्याता।

जय जय तुलसी माता...॥

लेकर जन्म बिजन में आई दिव्य भवन में,
मानव लोक तुम्हीं से सुख सम्पत्ति पाता।

जय जय तुलसी माता...॥

हरि को तुम अति प्यारी श्याम वर्ण सुकुमारी,
प्रेम अजब है श्री हरि का तुम से नाता।

जय जय तुलसी माता...॥""",
    "meaning": """॥ श्री तुलसी माता जी की आरती (जय जय तुलसी माता) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती भगवान श्रीहरि विष्णु की परम प्रिया, समस्त आधि-व्याधियों का हरण करने वाली तथा साक्षात वैकुंठ-धाम की अधिष्ठात्री माँ तुलसी (वृंदा देवी) की स्तुति में गाई जाती है। प्रत्येक सनातनी गृहस्थ के आंगन में नित्य सांध्य आरती में इस पावन स्तुति का सस्वर गायन परम कल्याणकारी है।)

१. प्रथम पद (टेक / मुखड़ा — सुखदात्री, वरदात्री व रोग-रुज नाशिनी):
"जय जय तुलसी माता, सबकी सुखदाता वर माता।
सब योगों के ऊपर, सब रोगों के ऊपर,
रुज से रक्षा करके भव त्राता।
जय जय तुलसी माता...॥"
भावार्थ: हे समस्त चराचर जगत को भौतिक, दैहिक और आध्यात्मिक सुख प्रदान करने वाली तथा मनोवांछित वर देने वाली करुणामयी माँ तुलसी! आपकी सदा ही जय हो, जय-जयकार हो। आप संपूर्ण औषधियों, समस्त योग-विद्याओं तथा समस्त रोगों से सर्वोपरि हैं। आप शारीरिक व मानसिक व्याधियों (रुज) से अपने आश्रित भक्तों की रक्षा कर उन्हें इस भवसागर के कष्टों से पार लगाने वाली परम तारिणी हैं।

२. द्वितीय पद (श्यामा-रामा भेद, सूरवल्ली, ग्राम्या व विष्णु-प्रिया):
"बहु पुत्री है श्यामा, सूर वल्ली है ग्राम्या,
विष्णु प्रिय जो तुमको सेवे, सो नर तर जाता।
जय जय तुलसी माता...॥"
भावार्थ: हे माता! आपकी अनगिनत पावन शाखाएं-प्रशाखाएं (बहुपुत्री) हैं। आप गहरे हरित-श्याम वर्ण वाली 'श्यामा तुलसी' तथा 'रामा तुलसी' के रूप में प्रसिद्ध हैं। आप देवताओं द्वारा पूजित दिव्य लता (सूरवल्ली) तथा घर-घर, गांव-गांव में आंगन की शोभा बढ़ाने वाली 'ग्राम्या' हैं। हे भगवान विष्णु की परम वल्लभा! जो भी मनुष्य निष्काम भाव से आपकी नित्य सेवा, जल-सिंचन और वंदना करता है, वह अनायास ही इस संसार-सागर से तर जाता है।

३. तृतीय पद (हरि के शीश विराजना, त्रिभुवन-वंदिता व पतित-उद्धारिणी):
"हरि के शीश विराजत त्रिभुवन से हो वंदित,
पतित जनों की तारिणि, तुम हो विख्याता।
जय जय तुलसी माता...॥"
भावार्थ: हे देवि! आपका पावन स्थान स्वयं जगन्नियंता भगवान श्रीहरि के मस्तक व श्रीचरणों पर सुशोभित है। तीनों लोकों (स्वर्ग, मर्त्य, पाताल) के समस्त देवता, ऋषि और मनुष्य आपकी श्रद्धा से वंदना करते हैं। आप घोर से घोर पतित, पापी और दीन जीवों का भी उद्धार करने वाली परम तारिणी के रूप में संपूर्ण ब्रह्मांड में विख्यात हैं।

४. चतुर्थ पद (बिजन में जन्म, दिव्य भवनों में आगमन व सुख-संपत्ति प्रदाता):
"लेकर जन्म बिजन में आई दिव्य भवन में,
मानव लोक तुम्हीं से सुख सम्पत्ति पाता।
जय जय तुलसी माता...॥"
भावार्थ: हे माँ! यद्यपि आपका प्राकट्य प्रकृति के शांत, एकांत निर्जन वन (बिजन / वृंदावन) में हुआ, किंतु अपनी पावनता और कल्याणकारी स्वभाव के कारण आप प्रत्येक भक्त के दिव्य गृह-आंगन में पूजित होकर प्रतिष्ठित हुईं। संपूर्ण मानव समाज आपके ही अनुग्रह से आरोग्य, सुख, शांति, समृद्धि और समस्त आध्यात्मिक वैभव प्राप्त करता है।

५. पंचम पद (हरि की अति प्यारी, श्याम वर्ण सुकुमारी व अलौकिक प्रेम-नाता):
"हरि को तुम अति प्यारी श्याम वर्ण सुकुमारी,
प्रेम अजब है श्री हरि का तुम से नाता।
जय जय तुलसी माता...॥"
भावार्थ: हे श्यामल वर्ण की अत्यंत कोमल, सुकुमारी माँ तुलसी! आप भगवान श्रीहरि के प्राणों से भी अधिक प्रिय हैं। भगवान विष्णु और शालिग्राम जी का आपके साथ जो अलौकिक, विशुद्ध और अमर प्रेम का नाता (तुलसी विवाह का पावन संबंध) है, वह अवर्णनीय और अनुपम है। आपके बिना भगवान की कोई भी पूजा व नैवेद्य पूर्ण नहीं होता।""",
    "vidhi": """॥ श्री तुलसी जी की आरती — नित्य संध्या शास्त्रोक्त 4-2-1-7 विधान ॥

हरिप्रिया माँ तुलसी जी की आरती उतारने का विशेष शास्त्रोक्त एवं गृहस्थ-कल्याणक विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
शुद्ध गाय के घी का एकमुखी अथवा पंचमुखी दीपक प्रज्वलित करें। धूपबत्ती, रोली, चंदन, कुंकुम, अक्षत, सुंगधित लाल-पीले पुष्प, कलावा, चुनरी, शृंगार सामग्री, जल का लोटा (गंगाजल मिश्रित) और बताशे या खीर/मिश्री का भोग लगाएं।

२. आरती घुमाने का विशेष शास्त्रीय '४-२-१-७' क्रम:
आरती को तुलसी जी के समक्ष '४-२-१-७' के शास्त्रोक्त क्रम से संपन्न करें:
• तुलसी कोट/गमले की जड़ (मूल) के समक्ष ४ बार: चारों वेदों, चारों पुरुषार्थों की प्राप्ति, अहंकार विसर्जन व पृथ्वी-तत्त्व की शुद्धि हेतु।
• तुलसी जी के मुख्य तने (नाभि मंडल) के समक्ष २ बार: प्राण-ऊर्जा की शुद्धि, पारिवारिक शांति व आरोग्य-सिद्धि हेतु।
• तुलसी जी की मंजरी (शिखर/मुखारविंद) के समक्ष १ बार: भगवान विष्णु के प्रिय दर्शन, अखंड सौभाग्य व ज्ञान-वृद्धि हेतु।
• संपूर्ण तुलसी वृंद के समक्ष ७ बार: सप्त-चक्रों, सप्त-लोकों की शुद्धि व संपूर्ण आत्म-समर्पण के साथ गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की शुद्धि व संपूर्ण तुलसी प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष तुलसी मंत्र व स्तुति:
आरती आरंभ करने से पूर्व 'ॐ श्री तुलस्यै नमः' अथवा 'महाप्रसाद जननी सर्व सौभाग्यवर्धिनी । आधि व्याधि हरा नित्यं तुलसी त्वं नमोऽस्तु ते ॥' मन्त्र का स्मरण करें।

४. आरती उपरांत प्रदक्षिणा व नियम:
आरती पूर्ण होने पर कर्पूर दीप पर जल की तीन बूंदें छिड़ककर आचमन करें। तुलसी जी की ३ अथवा ७ बार प्रदक्षिणा करें। ध्यान रहे कि सांध्यकाल में तुलसी जी का स्पर्श नहीं करना चाहिए, केवल दीपदान व आरती करनी चाहिए।""",
    "significance": """॥ श्री तुलसी माता आरती (जय जय तुलसी माता) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'हरिप्रिया' — भगवान श्रीहरि की पूजा की पूर्णता:
पद्म पुराण और स्कंद पुराण के अनुसार, बिना तुलसी दल के भगवान विष्णु, शालिग्राम जी अथवा श्रीकृष्ण का कोई भी नैवेद्य, भोग अथवा पूजन स्वीकार नहीं होता। तुलसी पत्र अर्पित करने से अश्वमेध यज्ञ का फल प्राप्त होता है।

२. आधि-व्याधि हरण व सर्व-रोग निवारण:
आरती में स्पष्ट वर्णित है—"सब योगों के ऊपर, सब रोगों के ऊपर, रुज से रक्षा करके भव त्राता।" माँ तुलसी साक्षात संजीवनी स्वरूपा हैं। इनकी आरती व दर्शन से घर का वास्तु-दोष, नकारात्मक ऊर्जा, संक्रामक रोग और मानसिक तनाव समूल नष्ट हो जाते हैं।

३. अखंड सौभाग्य व माँ लक्ष्मी का स्थायी वास:
नित्य सांध्यकाल में तुलसी जी के समक्ष शुद्ध घी का दीपक जलाकर आरती करने से उस घर में माँ महालक्ष्मी और भगवान नारायण का स्थायी वास होता है तथा साधक को अखंड सौभाग्य और सुख-समृद्धि की प्राप्ति होती है।

४. यम-दूतों के भय से मुक्ति:
स्कंद पुराण के अनुसार, जिस घर के आंगन में हरी-भरी तुलसी जी विराजती हैं और जहाँ नित्य संध्या आरती होती है, वहाँ यमदूत और अकाल मृत्यु का भय कभी नहीं रहता।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक पांच छंद पदों पर पूर्णतः आधारित है, जो भारत के कोटि-कोटि सनातन गृहों में नित्य सांध्यकाल में गाई जाती है।""",
    "english_lyrics": """॥ Shri Tulasi Mata Aarti ॥
(Jai Jai Tulasi Mata)

Jai Jai Tulasi Mata, Sabakee Sukhadata Vara Mata।
Saba Yogon Ke Oopara, Saba Rogon Ke Oopara,
Ruja Se Raksha Karake Bhava Trata।

Jai Jai Tulasi Mata...॥

Bahu Putree Hai Shyama, Soora Vallee Hai Gramya,
Vishnu Priya Jo Tumako Seve, So Nara Tara Jata।

Jai Jai Tulasi Mata...॥

Hari Ke Sheesha Viraajata Tribhuvana Se Ho Vandita,
Patita Janon Kee Taarini, Tuma Ho Vikhyaata।

Jai Jai Tulasi Mata...॥

Lekara Janma Bijana Mein Aayee Divya Bhavana Mein,
Manava Loka Tumheen Se Sukha Sampatti Paata।

Jai Jai Tulasi Mata...॥

Hari Ko Tuma Ati Pyaaree Shyama Varna Sukumaaree,
Prema Ajaba Hai Shri Hari Ka Tuma Se Naata।

Jai Jai Tulasi Mata...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['gayatri', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_13':
                fg_data[cat_name]['items'][i] = TULASI_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_13 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_13':
                    cdata['items'][i] = TULASI_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_13 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(TULASI_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_13"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_13 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_13 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
