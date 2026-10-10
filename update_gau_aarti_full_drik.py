# -*- coding: utf-8 -*-
"""
Update drik_goddesses_16 (Gau Mata Aarti / आरती श्री गैय्या मैंय्या की) in:
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

GAU_DATA = {
    "id": "drik_goddesses_16",
    "title": "आरती श्री गैय्या मैंय्या की",
    "title_en": "Gau Mata Aarti (Aarti Shri Gaiya Maiya Ki)",
    "en_line": "Aarti Shri Gaiya Maiya Ki, Aarti Harani Vishwa Dhaiya Ki",
    "hi_line": "आरती श्री गैय्या मैंय्या की, आरती हरनि विश्व धैय्या की",
    "sub": "कामधेनु सुरभि विश्वमाता गौ माता जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_kamadhenu_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=xbujgiIRVJw",
    "video_id": "xbujgiIRVJw",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/gau-mata/gau-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री गौमाताजी की आरती ॥
(आरती श्री गैय्या मैंय्या की)

आरती श्री गैय्या मैंय्या की,
आरती हरनि विश्व धैय्या की।

आरती श्री गैय्या मैंय्या की...॥

अर्थकाम सद्धर्म प्रदायिनी,
अविचल अमल मुक्तिपद्दायिनी।
सुर मानव सौभाग्या विधायिनी,
प्यारी पूज्य नन्द छैय्या की॥

आरती श्री गैय्या मैंय्या की...॥

अखिल विश्व प्रतिपालिनी माता,
मधुर अमिय दुग्धान्न प्रदाता।
रोग शोक संकट परित्राता,
भवसागर हित दृढ नैय्या की॥

आरती श्री गैय्या मैंय्या की...॥

आयु ओज आरोग्य विकाशिनी,
दुःख दैन्य दारिद्रय विनाशिनी।
सुष्मा सौख्य समृद्धि प्रकाशिनी,
विमल विवेक बुद्धि दैय्या की॥

आरती श्री गैय्या मैंय्या की...॥

सेवक हो चाहे दुखदाई,
सम पय सुधा पियावति माई।
शत्रु-मित्र सबको सुखदायी,
स्नेह स्वभाव विश्व जैय्या की॥

आरती श्री गैय्या मैंय्या की...॥

आरती श्री गैय्या मैंय्या की,
आरती हरनि विश्व धैय्या की।

आरती श्री गैय्या मैंय्या की...॥""",
    "meaning": """॥ श्री गौ माता जी की आरती (आरती श्री गैय्या मैंय्या की) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती कामधेनु, सुरभि, तैंतीस कोटि देवताओं की अधिष्ठात्री तथा साक्षात विश्वमाता गौ माता की पावन स्तुति में गाई जाती है। गोपाष्टमी, नित्य गो-पूजन तथा सांध्यकाल में इस आरती का गान समस्त पापों, व्याधियों और दारिद्र्य का समूल नाश करने वाला है।)

१. प्रथम पद (टेक / मुखड़ा — विश्व-धैर्य संहारिणी व आरती-वंदना):
"आरती श्री गैय्या मैंय्या की, आरती हरनि विश्व धैय्या की।
आरती श्री गैय्या मैंय्या की...॥"
भावार्थ: हे समस्त चराचर जगत का वात्सल्यपूर्वक पालन करने वाली परम पावनी गौ माता! हम आपकी पावन मंगल आरती उतारते हैं। आप संपूर्ण विश्व के धैर्य (व्याकुलता, अशांति व ताप) का हरण कर समस्त जीवों को अगाध शांति, शीतलता और संतोष प्रदान करने वाली ममतामयी माता हैं।

२. द्वितीय पद (चतुर्विध फलदात्री, मोक्षदायिनी व श्रीकृष्ण की प्राणप्रिया):
"अर्थकाम सद्धर्म प्रदायिनी, अविचल अमल मुक्तिपद्दायिनी।
सुर मानव सौभाग्या विधायिनी, प्यारी पूज्य नन्द छैय्या की॥
आरती श्री गैय्या मैंय्या की...॥"
भावार्थ: हे कामधेनु स्वरूपा गौ माता! आप धर्म, अर्थ, काम और मोक्ष—चारों पुरुषार्थों को सहज ही प्रदान करने वाली तथा अविचल, निष्कलंक परम मुक्ति (मोक्षपद) देने वाली हैं। आप समस्त देवताओं और मनुष्यों दोनों के सौभाग्य का विधान करने वाली हैं तथा नंदनंदन भगवान श्रीकृष्ण (नन्द छैय्या) की अतिशय प्रिय और पूजनीया हैं, जिनके पीछे-पीछे कन्हैया नंगे पाँव गऊ-चारण करते हुए दौड़े चले आते हैं।

३. तृतीय पद (विश्व-प्रतिपालिनी, अमिय दुग्ध-प्रदाता व भवसागर-तारिणी):
"अखिल विश्व प्रतिपालिनी माता, मधुर अमिय दुग्धान्न प्रदाता।
रोग शोक संकट परित्राता, भवसागर हित दृढ नैय्या की॥
आरती श्री गैय्या मैंय्या की...॥"
भावार्थ: हे माँ! आप संपूर्ण अखिल ब्रह्मांड का अपनी संतान के समान पोषण करने वाली जगत-माता हैं। आप अपने स्तनों से अमृत-तुल्य (अमिय) मधुर दुग्ध, दही और घृत रूपी दिव्य पोषण प्रदान करती हैं। आप समस्त रोगों, शोकों और घोर संकटों से जीवों की रक्षा करने वाली तथा इस दुर्गम संसार-सागर को पार कराने वाली सबसे सुदृढ़ नौका (नैय्या) के समान हैं, जिनकी पूंछ पकड़कर जीवात्मा समस्त वैतरणी कष्टों से पार उतर जाता है।

४. चतुर्थ पद (आयु-आरोग्य-ओज विकाशिनी व विमल सद्बुद्धि प्रदात्री):
"आयु ओज आरोग्य विकाशिनी, दुःख दैन्य दारिद्रय विनाशिनी।
सुष्मा सौख्य समृद्धि प्रकाशिनी, विमल विवेक बुद्धि दैय्या की॥
आरती श्री गैय्या मैंय्या की...॥"
भावार्थ: हे भगवती! आपकी सेवा और पंचगव्य के सेवन से मनुष्य की दीर्घायु, ओज (तेज) और आरोग्य का विकास होता है। आप जीवन के समस्त दुःख, दीनता और दरिद्रता का समूल विनाश करने वाली हैं। आप घर-परिवार में अलौकिक सौंदर्य (सुषमा), सुख और समृद्धि का प्रकाश बिखेरती हैं तथा साधक को निर्मल विवेक और सात्विक सद्बुद्धि प्रदान करने वाली हैं।

५. पंचम पद (समदर्शी वात्सल्य, स्नेह-स्वभाव व विश्व-विजयी प्रेम):
"सेवक हो चाहे दुखदाई, सम पय सुधा पियावति माई।
शत्रु-मित्र सबको सुखदायी, स्नेह स्वभाव विश्व जैय्या की॥
आरती श्री गैय्या मैंय्या की...॥"
भावार्थ: हे करुणामयी माँ! आपका वात्सल्य अद्वितीय और समदर्शी है। चाहे कोई आपकी श्रद्धा से सेवा करने वाला सेवक हो अथवा आपको कष्ट पहुंचाने वाला अज्ञानी, आप बिना किसी भेदभाव के सभी को अपना अमृत-तुल्य दूध (पय सुधा) पिलाकर जीवनदान देती हैं। आप शत्रु और मित्र दोनों का ही सर्वदा कल्याण और सुख करती हैं। आपके इस निश्छल, क्षमाशील और वात्सल्यपूर्ण प्रेम-स्वभाव ने संपूर्ण विश्व को जीत (विश्व जैय्या) लिया है।

६. षष्ठ पद (पूर्णाहुति व पुनः मंगल-गान):
"आरती श्री गैय्या मैंय्या की, आरती हरनि विश्व धैय्या की।
आरती श्री गैय्या मैंय्या की...॥"
भावार्थ: ऐसी परम पूज्या, दयामयी, त्रिभुवन-तारिणी माँ सुरभि (गौ माता) के पावन चरणों में हम नतमस्तक होकर बारंबार आरती गाते हैं और सर्वकल्याण की याचना करते हैं।""",
    "vidhi": """॥ श्री गौ माता जी की आरती — नित्य व गोपाष्टमी शास्त्रोक्त 4-2-1-7 विधान ॥

विश्वमाता गौ माता जी की आरती उतारने का विशेष शास्त्रोक्त एवं गो-पूजन विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
आरती हेतु शुद्ध गाय के घी का दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। तांबे के लोटे में गंगाजल मिश्रित शुद्ध जल, रोली, कुंकुम, हल्दी, चंदन, अक्षत, सुंगधित पुष्पमाला, कलावा, गुड़, भीगी हुई चने की दाल या आटे का पेड़ा (लोई), हरी ताजी घास अथवा पालक सजाएं।

२. आरती घुमाने का विशेष शास्त्रीय '४-२-१-७' क्रम:
गौ माता के साक्षात विग्रह के समक्ष '४-२-१-७' के शास्त्रोक्त क्रम से आरती घुमाएं:
• गौ माता के खुरों (चरणों) के समक्ष ४ बार: चारों वेदों, चारों धामों की प्राप्ति, पृथ्वी-तत्त्व की शुद्धि व अहंकार विसर्जन हेतु।
• गौ माता के उदर/स्तनों (नाभि मंडल) के समक्ष २ बार: कामधेनु अमृत, पंचगव्य शुद्धि व पारिवारिक पोषण एवं स्वास्थ्य लाभ हेतु।
• गौ माता के सींगों व मस्तक (मुखारविंद) के समक्ष १ बार: तैंतीस कोटि देवताओं के दर्शन, सद्बुद्धि, विवेक व दृष्टि-दोष निवारण हेतु।
• संपूर्ण गौ विग्रह के समक्ष ७ बार: सप्त-चक्रों, सप्त-लोकों की शुद्धि, सर्व-पाप निवारण व संपूर्ण आत्म-समर्पण के साथ गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की शुद्धि व संपूर्ण गो-प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष गो-पूजन मंत्र:
आरती आरंभ करने से पूर्व 'ॐ नमो गोभ्यः श्रीमतीभ्यः सौरभेयीभ्य एव च। नमो ब्रह्मसुताभ्यश्च पवित्राभ्यो नमो नमः॥' अथवा 'गावो विश्वस्य मातरः' मन्त्र का स्मरण करें।

४. आरती उपरांत गोग्रास व प्रदक्षिणा:
आरती पूर्ण होने पर कर्पूर दीप पर शीतल जल छिड़ककर आचमन करें। गौ माता को श्रद्धापूर्वक गुड़-रोटी, हरा चारा अथवा भीगी चने की दाल का गोग्रास खिलाएं। गौ माता की पीठ पर हाथ फेरकर उनकी ३ अथवा ७ बार प्रदक्षिणा करें तथा उनके खुरों की पवित्र रज को अपने मस्तक पर धारण करें।""",
    "significance": """॥ श्री गौ माता आरती (आरती श्री गैय्या मैंय्या की) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'गावो विश्वस्य मातरः' — ३३ कोटि देवताओं की संयुक्त कृपा:
शास्त्रों के अनुसार गौ माता के रोम-रोम में तैंतीस कोटि देवताओं का वास है। इनके दर्शन, स्पर्श और नित्य आरती करने से समस्त देवी-देवताओं की एक साथ पूजा का परम फल अनायास ही प्राप्त हो जाता है।

२. सर्व-तीर्थमय स्वरूप व वैतरणी-तारण:
गौ माता के खुरों में समस्त तीर्थ और पृष्ठ भाग में साक्षात माँ लक्ष्मी का वास है। गो-सेवा और नित्य आरती करने से मनुष्य मृत्यु के उपरांत वैतरणी नदी के समस्त कष्टों से मुक्त होकर सीधे श्रीहरि के वैकुंठ धाम को प्राप्त होता है।

३. वास्तु-दोष, नजर-दोष व पितृ-दोष का समूल निवारण:
जिस घर में नित्य प्रथम रोटी (गोग्रास) गौ माता के लिए निकाली जाती है और उनकी आरती होती है, वहाँ कोई भी वास्तु-दोष, नजर-दोष, ग्रह-दोष अथवा पितृ-दोष कभी नहीं टिकता।

४. आयु, ओज, आरोग्य व दरिद्रता नाश:
आरती में स्पष्ट उल्लेख है—"आयु ओज आरोग्य विकाशिनी, दुःख दैन्य दारिद्रय विनाशिनी।" गौ माता के दुग्ध, घृत और पंचगव्य से असाध्य रोगों से मुक्ति मिलती है और घर में सुख, शांति तथा लक्ष्मी का स्थायी वास होता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छह छंद पदों पर पूर्णतः आधारित है, जो भारत की समस्त गोशालाओं, शक्तिपीठों व सनातन गृहों में श्रद्धापूर्वक गाई जाती है।""",
    "english_lyrics": """॥ Shri Gau Mata Ki Aarti ॥
(Aarti Shri Gaiya Maiya Ki)

Aarti Shri Gaiya Maiya Ki,
Aarti Harani Vishwa Dhaiya Ki।

Aarti Shri Gaiya Maiya Ki...॥

Artha-Kaama Saddharma Pradaayinee,
Avichala Amala Muktipaddaayinee।
Sura Maanava Saubhaagya Vidhaayinee,
Pyaaree Poojya Nanda Chhaiya Ki॥

Aarti Shri Gaiya Maiya Ki...॥

Akhila Vishwa Pratipaalinee Mata,
Madhura Amiya Dugdhaanna Pradaata।
Roga Shoka Sankata Paritraata,
Bhavasaagara Hita Dridha Naiya Ki॥

Aarti Shri Gaiya Maiya Ki...॥

Aayu Oja Aarogya Vikaashinee,
Duhkha Dainya Daaridrya Vinaashinee।
Sushama Saukhya Samriddhi Prakaashinee,
Vimala Viveka Buddhi Daiya Ki॥

Aarti Shri Gaiya Maiya Ki...॥

Sevaka Ho Chaahe Dukhadaayee,
Sama Paya Sudha Piyaavati Maaee।
Shatru-Mitra Sabako Sukhadaayee,
Sneha Swabhaava Vishwa Jaiya Ki॥

Aarti Shri Gaiya Maiya Ki...॥

Aarti Shri Gaiya Maiya Ki,
Aarti Harani Vishwa Dhaiya Ki।

Aarti Shri Gaiya Maiya Ki...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['gayatri', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_16':
                fg_data[cat_name]['items'][i] = GAU_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_16 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_16':
                    cdata['items'][i] = GAU_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_16 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(GAU_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_16"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_16 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_16 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
