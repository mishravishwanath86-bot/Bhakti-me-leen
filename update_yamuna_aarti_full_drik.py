# -*- coding: utf-8 -*-
"""
Update drik_goddesses_28 (Yamuna Mata Aarti / ॐ जय यमुना माता) in:
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

YAMUNA_DATA = {
    "id": "drik_goddesses_28",
    "title": "ॐ जय यमुना माता",
    "title_en": "Yamuna Mata Aarti (Om Jai Yamuna Mata)",
    "en_line": "Om Jai Yamuna Mata, Hari Om Jai Yamuna Mata",
    "hi_line": "ॐ जय यमुना माता, हरि ॐ जय यमुना माता",
    "sub": "सूर्यसुता यमभगिनी माँ यमुना जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_yamuna_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=wlKH9AH0_mI",
    "video_id": "wlKH9AH0_mI",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/yamuna-mata/yamuna-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री यमुना माता आरती ॥
(ॐ जय यमुना माता)

ॐ जय यमुना माता,
हरि ॐ जय यमुना माता।
जो नहावे फल पावे
सुख दुःख की दाता॥

ॐ जय यमुना माता...॥

पावन श्रीयमुना जल
शीतल अगम बहै धारा।
जो जन शरण में आया
कर दिया निस्तारा॥

ॐ जय यमुना माता...॥

जो जन प्रातः ही उठकर
नित्य स्नान करे।
यम के त्रास न पावे
जो नित्य ध्यान करे॥

ॐ जय यमुना माता...॥

कलिकाल में महिमा
तुम्हारी अटल रही।
तुम्हारा बड़ा महातम
चारों वेद कही॥

ॐ जय यमुना माता...॥

आन तुम्हारे माता
प्रभु अवतार लियो।
नित्य निर्मल जल पीकर
कंस को मार दियो॥

ॐ जय यमुना माता...॥

नमो मात भय हरणी
शुभ मन्गल करणी।
मन बेचैन भया है
तुम बिन वैतरणी॥

ॐ जय यमुना माता...॥

ॐ जय यमुना माता,
हरि ॐ जय यमुना माता।
जो नहावे फल पावे
सुख दुःख की दाता॥

ॐ जय यमुना माता...॥""",
    "meaning": """॥ श्री यमुना माता जी की आरती (ॐ जय यमुना माता) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह जगत्प्रसिद्ध दिव्य आरती भगवान सूर्य देव की आत्मजा, धर्मराज यमराज की प्रिय भगिनी तथा भगवान श्रीकृष्ण की पटरानी परम पावनी माँ यमुना (कालिन्दी) की स्तुति में गाई जाती है। यमुनोत्री धाम, मथुरा के विश्राम घाट, वृन्दावन के केशी घाट और प्रयागराज संगम पर नित्य सांध्य आरती में इस स्तुति का सस्वर गायन होता है।)

१. प्रथम पद (मुखड़ा / टेक — वंदना व फल प्राप्ति):
"ॐ जय यमुना माता, हरि ॐ जय यमुना माता।
जो नहावे फल पावे, सुख दुःख की दाता॥
ॐ जय यमुना माता...॥"
भावार्थ: हे ॐकार-स्वरूपिणी, कलि-मल-नाशिनी माँ यमुना! आपकी जय हो, श्री हरि की परम वल्लभा मैया यमुना जी की जय हो। जो भी श्रद्धालु आपके पावन शीतल जल में भक्तिपूर्वक स्नान व आचमन करता है, वह धर्म, अर्थ, काम और मोक्ष रूपी चतुर्विध फल प्राप्त करता है। आप सांसारिक सुखों की प्रदाता हैं और भक्तों के समस्त संकटों व दुःखों का हरण कर अंत में परम पद प्रदान करने वाली हैं।

२. द्वितीय पद (अगम शीतल धारा व शरणागत-कल्याण):
"पावन श्रीयमुना जल, शीतल अगम बहै धारा।
जो जन शरण में आया, कर दिया निस्तारा॥
ॐ जय यमुना माता...॥"
भावार्थ: हे माँ कालिन्दी! आपका पावन श्याम-धवल जल अत्यंत शीतल, पवित्र और अपार गहराई (अगम्यता) लिए हुए अनवरत बहता है। जो भी आर्त, दीन अथवा पापी जीव संसार के तापों से व्यथित होकर आपके पावन तट पर आकर आपकी शरण लेता है, आप अपनी वात्सल्यमयी कृपा से उसका भवसागर से निस्तारा (सदा के लिए उद्धार) कर देती हैं।

३. तृतीय पद (प्रातः स्नान व यम-भय से मुक्ति):
"जो जन प्रातः ही उठकर, नित्य स्नान करे।
यम के त्रास न पावे, जो नित्य ध्यान करे॥
ॐ जय यमुना माता...॥"
भावार्थ: हे यम-भगिनी! जो पुण्यात्मा मनुष्य प्रातःकाल ब्रह्ममुहूर्त में उठकर आपके पावन जल में नित्य श्रद्धा से स्नान करता है अथवा आपके दिव्य स्वरूप का नित्य ध्यान व स्मरण करता है, उसे मृत्यु के देवता यमराज और उनके दूतों के किसी भी त्रास, दंड या नरक-यातना का भय नहीं रहता। आप अपने भक्तों को यम-यातना से सदा के लिए अभय कर देती हैं।

४. चतुर्थ पद (कलिकाल में अखंड महिमा व वेदोक्त माहात्म्य):
"कलिकाल में महिमा, तुम्हारी अटल रही।
तुम्हारा बड़ा महातम, चारों वेद कही॥
ॐ जय यमुना माता...॥"
भावार्थ: हे माता! घोर कलयुग में जब पाप और अधर्म का बोलबाला है, तब भी आपकी पावन महिमा, पवित्रता और तारक शक्ति सर्वदा अटल, अमर और निष्कलंक रही है। ऋग्वेद, यजुर्वेद, सामवेद और अथर्ववेद—चारों वेदों तथा समस्त पुराणों ने आपके पावन अवतरण और अलौकिक माहात्म्य का गान किया है।

५. पंचम पद (श्रीकृष्ण का प्राकट्य, ब्रज-लीला व कंस-वध):
"आन तुम्हारे माता, प्रभु अवतार लियो।
नित्य निर्मल जल पीकर, कंस को मार दियो॥
ॐ जय यमुना माता...॥"
भावार्थ: हे माँ यमुना! आपके ही पावन तटों (गोकुल, मथुरा, वृन्दावन) की धन्यता के लिए साक्षात परात्पर ब्रह्म भगवान श्रीकृष्ण ने इस धराधाम पर अवतार धारण किया। बाल्यकाल में आपके तटों पर गऊ-चारण व रास-लीलाएं करते हुए तथा आपके अमृत-तुल्य निर्मल जल का नित्य पान कर प्रभु ने असीम सामर्थ्य प्रकट किया और अत्याचारी दैत्यराज कंस का संहार कर धर्म और सज्जनों की रक्षा की।

६. षष्ठ पद (भय-हारिणी, शुभ-मंगल-कारिणी व वैतरणी-उद्धार):
"नमो मात भय हरणी, शुभ मन्गल करणी।
मन बेचैन भया है, तुम बिन वैतरणी॥
ॐ जय यमुना माता...॥"
भावार्थ: हे समस्त सांसारिक भयों का नाश करने वाली और जीवन में सर्वविध शुभ, मंगल व कल्याण करने वाली करुणामयी माँ! हम आपको कोटिशः नमन करते हैं। माया-मोह और पापों के कारण यह चंचल मन अत्यंत बेचैन और व्याकुल है। मृत्यु के अनंतर दुर्गम वैतरणी नदी को पार कराने वाली नौका आपके अनुग्रह के अतिरिक्त कोई नहीं है। आप ही जीवात्मा को भव-पार उतारने वाली परम तारिणी हैं।

७. सप्तम पद (पूर्णाहुति व पुनः मंगल-गान):
"ॐ जय यमुना माता, हरि ॐ जय यमुना माता।
जो नहावे फल पावे, सुख दुःख की दाता॥
ॐ जय यमुना माता...॥"
भावार्थ: हे सूर्यसुता, यम-भगिनी, कृष्ण-प्रिया माँ यमुना! हम सभी भक्तजन एकमुख होकर आपकी आरती गाते हैं और आपके पावन चरणों में आत्मसमर्पण करते हैं।""",
    "vidhi": """॥ श्री यमुना माता जी की आरती — मथुरा-विश्राम घाट व यमुनोत्री शास्त्रोक्त 4-2-1-7 विधान ॥

सूर्यपुत्री माँ यमुना (कालिन्दी) की आरती उतारने का विशेष शास्त्रोक्त एवं पारम्परिक ब्रज-विधान:

१. दीप प्रज्वलन व थाल सज्जा:
पीतल, कांसा या तांबे की पवित्र थाली में शुद्ध गाय के घी का पंचमुखी दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाली में रोली, कुंकुम, अक्षत, नीलकमल या सुगंधित लाल-गुलाब पुष्प, कलावा, अगरबत्ती, इत्र, मिश्री और माखन या पेड़े का नैवेद्य सजाएं।

२. आरती घुमाने का शास्त्रोक्त '४-२-१-७' क्रम:
आरती केवल सामान्य रूप से घुमाना नहीं, अपितु एक दिव्य तांत्रिक व वैदिक क्रिया है। इसे '४-२-१-७' क्रम से संपन्न करें:
• माँ यमुना के श्रीचरणों में ४ बार: चार पुरुषार्थों (धर्म, अर्थ, काम और मोक्ष) की याचना व अहंकार विसर्जन हेतु।
• नाभि मंडल के समक्ष २ बार: संसार-माया से मुक्ति और प्राण-ऊर्जा की शुद्धि हेतु।
• मुखारविंद (चेहरे) के समक्ष १ बार: दिव्य कृपा-दृष्टि और सौम्य दर्शन हेतु।
• समग्र विग्रह / प्रवाहित जलधारा के समक्ष ७ बार: सप्त-चक्रों, सप्त-लोकों की शुद्धि और संपूर्ण आत्म-समर्पण के प्रतीक रूप में गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवन की शुद्धि व प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष मंत्र व आचमन:
आरती आरंभ करने से पूर्व 'ॐ नमो भगवत्यै कालिन्द्यै नमः' अथवा 'ॐ श्री यमुनायै नमः' मंत्र का उच्चारण करें। श्रीमद्वल्लभाचार्य जी विरचित 'यमुनाष्टकम्' (नमामि यमुनामहं सकल सिद्धि हेतुं मुदा...) का पाठ करने से विशेष सान्निध्य प्राप्त होता है।

४. आरती उपरांत प्रदक्षिणा व प्रसाद:
आरती पूर्ण होने पर कर्पूर दीप पर शीतल जल की तीन बूंदें छिड़ककर आचमनी करें (जल-शीतलीकरण)। आरती की पावन ज्योति को दोनों हाथों से ग्रहण कर नेत्रों, मस्तक और हृदय से स्पर्श कराएं। उपस्थित भक्तों में चरणामृत व माखन-मिश्री का प्रसाद वितरित करें।""",
    "significance": """॥ श्री यमुना माता आरती (ॐ जय यमुना माता) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'स्मरणादेव यमुना' — स्मरण मात्र से पापनाश:
पद्म पुराण और स्कंद पुराण में स्पष्ट रूप से कहा गया है:
"स्नानेन गंगा तरति, स्मरणादेव यमुना।"
अर्थात् गंगा जी में स्नान करने से जो पुण्य प्राप्त होता है, वह माँ यमुना के केवल श्रद्धापूर्वक नाम-स्मरण और ध्यान करने मात्र से ही सुलभ हो जाता है। इनके दर्शन और आचमन से जन्म-जन्मांतर के संचित पाप भस्म हो जाते हैं।

२. यमराज से अभय दान (यम द्वितीया / भाईदूज का पावन वरदान):
माँ यमुना और धर्मराज यमराज दोनों भगवान सूर्य देव की संतान और सहोदर भाई-बहन हैं। कार्तिक शुक्ल द्वितीया (भाई दूज) के दिन यमराज ने अपनी बहन यमुना जी के आतिथ्य को स्वीकार किया था और वरदान दिया था कि—जो भी भाई-बहन इस पावन तिथि पर यमुना जी में स्नान कर एक-दूसरे का सत्कार करेंगे, उन्हें कभी यमदूतों का भय और अकाल मृत्यु का संताप नहीं सहना पड़ेगा।

३. श्रीकृष्ण की पटरानी व ब्रज-लीला की अधिष्ठात्री (कालिन्दी):
माँ यमुना भगवान श्रीकृष्ण की पटरानियों (अष्टभार्याओं) में अत्यंत प्रमुख हैं। भगवान के बाल्यकाल से लेकर मथुरा गमन तक की समस्त लीलाएं—कालिया नाग का दमन, चीरहरण, गोपी-रास और बंसी-वादन माँ यमुना के ही पावन तट पर संपन्न हुईं। यमुना जी की कृपा के बिना श्रीकृष्ण की अनन्य प्रेम-भक्ति (रागानुगा भक्ति) प्राप्त नहीं हो सकती।

४. सूर्य-तनया होने से ओज, तेज व आरोग्य प्रदाता:
भगवान भुवन-भास्कर सूर्य देव की पुत्री होने के कारण माँ यमुना का जल सूर्य की ऊर्जा और दिव्य औषधीय तत्वों से परिपूर्ण है। इनकी नित्य आरती व स्नान करने से साधक को तेजस्विता, मानसिक शांति, आत्मबल और समस्त शारीरिक व्याधियों से मुक्ति मिलती है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक सात छंद पदों पर पूर्णतः आधारित है, जो यमुनोत्री धाम, मथुरा विश्राम घाट और वृन्दावन केशी घाट पर नित्य सांध्य महाआरती में गाई जाती है।""",
    "english_lyrics": """॥ Shri Yamuna Mata Aarti ॥
(Om Jai Yamuna Mata)

Om Jai Yamuna Mata,
Hari Om Jai Yamuna Mata।
Jo Nahave Phala Pave
Sukha Duhkha Kee Data॥

Om Jai Yamuna Mata...॥

Pavana Shri Yamuna Jala
Sheetala Agama Bahai Dhara।
Jo Jana Sharana Mein Aaya
Kari Diya Nistara॥

Om Jai Yamuna Mata...॥

Jo Jana Pratah Hee Uthakara
Nitya Snana Kare।
Yama Ke Trasa Na Pave
Jo Nitya Dhyana Kare॥

Om Jai Yamuna Mata...॥

Kalikaala Mein Mahima
Tumharee Atala Rahee।
Tumhara Bada Mahatama
Charon Veda Kahee॥

Om Jai Yamuna Mata...॥

Aana Tumhare Mata
Prabhu Avatara Liyo।
Nitya Nirmala Jala Peekara
Kansa Ko Mara Diyo॥

Om Jai Yamuna Mata...॥

Namo Mata Bhaya Haranee
Shubha Mangala Karanee।
Mana Baichaina Bhaya Hai
Tuma Bina Vaitaranee॥

Om Jai Yamuna Mata...॥

Om Jai Yamuna Mata,
Hari Om Jai Yamuna Mata।
Jo Nahave Phala Pave
Sukha Duhkha Kee Data॥

Om Jai Yamuna Mata...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['ganga', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_28':
                fg_data[cat_name]['items'][i] = YAMUNA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_28 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_28':
                    cdata['items'][i] = YAMUNA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_28 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(YAMUNA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_28"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_28 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_28 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
