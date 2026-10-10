# -*- coding: utf-8 -*-
"""
Update drik_gods_14 (Lord Parashurama Aarti / ॐ जय परशुधारी) in:
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

PARASHURAMA_DATA = {
    "id": "drik_gods_14",
    "title": "ॐ जय परशुधारी",
    "title_en": "Lord Parashurama Aarti (Om Jai Parashudhari)",
    "en_line": "Om Jai Parashudhari, Swami Jai Parashudhari",
    "hi_line": "ॐ जय परशुधारी, स्वामी जय परशुधारी",
    "sub": "भगवान श्री परशुराम जी की पावन स्तुति-आरती • Drik Panchang Verified",
    "thumb": "assets/dwadashi_parashurama.jpg",
    "audio_url": "https://www.youtube.com/watch?v=HEk4veZhW_M",
    "video_id": "HEk4veZhW_M",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shri-parashurama/shri-parashurama-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री परशुराम आरती ॥
(ॐ जय परशुधारी)

ॐ जय परशुधारी,
स्वामी जय परशुधारी।
सुर नर मुनिजन सेवत,
श्रीपति अवतारी॥

ॐ जय परशुधारी...॥

जमदग्नी सुत नर-सिंह,
मां रेणुका जाया।
मार्तण्ड भृगु वंशज,
त्रिभुवन यश छाया॥

ॐ जय परशुधारी...॥

कांधे सूत्र जनेऊ,
गल रुद्राक्ष माला।
चरण खड़ाऊँ शोभे,
तिलक त्रिपुण्ड भाला॥

ॐ जय परशुधारी...॥

ताम्र श्याम घन केशा,
शीश जटा बांधी।
सुजन हेतु ऋतु मधुमय,
दुष्ट दलन आंधी॥

ॐ जय परशुधारी...॥

मुख रवि तेज विराजत,
रक्त वर्ण नैना।
दीन-हीन गो विप्रन,
रक्षक दिन रैना॥

ॐ जय परशुधारी...॥

कर शोभित बर परशु,
निगमागम ज्ञाता।
कंध चाप-शर वैष्णव,
ब्राह्मण कुल त्राता॥

ॐ जय परशुधारी...॥

माता पिता तुम स्वामी,
मीत सखा मेरे।
मेरी बिरद संभारो,
द्वार पड़ा मैं तेरे॥

ॐ जय परशुधारी...॥

अजर-अमर श्री परशुराम की,
आरती जो गावे।
'पूर्णेन्दु' शिव साखि,
सुख सम्पति पावे॥

ॐ जय परशुधारी...॥""",
    "meaning": """॥ श्री परशुराम आरती (ॐ जय परशुधारी) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह पावन आरती भगवान विष्णु के षष्ठम आवेशावतार, चिरंजीवी महर्षि भगवान श्री परशुराम जी के दिव्य शौर्य, तपस्या, विप्र-रक्षा और शरणागति की अनुपम स्तुति है।)

१. प्रथम पद (टेक / मुखड़ा — श्रीपति अवतारी वंदना):
"ॐ जय परशुधारी, स्वामी जय परशुधारी।
सुर नर मुनिजन सेवत, श्रीपति अवतारी॥"

भावार्थ:
हे दिव्य परशु (कुल्हाड़ा) धारण करने वाले प्रभु परशुराम! आपकी सदा ही जय हो, जय-जयकार हो। देवता, मनुष्य और मुनिजन नित्य भावपूर्वक आपकी सेवा-अर्चना करते हैं। आप साक्षात लक्ष्मीपति भगवान नारायण (श्रीपति) के पावन आवेशावतार हैं, जो धर्म की रक्षा हेतु अवतरित हुए।

२. द्वितीय पद (दिव्य कुल, मात-पिता एवं त्रिभुवन कीर्ति):
"जमदग्नी सुत नर-सिंह, मां रेणुका जाया।
मार्तण्ड भृगु वंशज, त्रिभुवन यश छाया॥"

भावार्थ:
आप परम तपस्वी महर्षि जमदग्नि के तेजस्वी पुत्र (सुत) और पुरुषों में सिंह के समान पराक्रमी हैं। आप माता रेणुका के पावन गर्भ से प्रकट हुए (जाया) हैं। आप भृगुकुल रूपी आकाश में सूर्य (मार्तण्ड) के समान देदीप्यमान हैं और आपका पावन यश तीनों लोकों (त्रिभुवन) में व्याप्त है।

३. तृतीय पद (तपस्वी ब्राह्मण वेशभूषा व त्रिपुण्ड शृंगार):
"कांधे सूत्र जनेऊ, गल रुद्राक्ष माला।
चरण खड़ाऊँ शोभे, तिलक त्रिपुण्ड भाला॥"

भावार्थ:
आपके पावन कंधे पर ब्रह्मतेज का प्रतीक पवित्र यज्ञोपवीत (जनेऊ) सुशोभित है और गले में पावन रुद्राक्ष की माला विराजमान है। आपके श्रीचरणों में काष्ठ की खड़ाऊँ शोभा पा रही हैं और ललाट (भाल) पर भगवान शिव की भक्ति का पावन भस्म त्रिपुण्ड तिलक अत्यंत दिव्य लग रहा है।

४. चतुर्थ पद (सज्जनों के लिए वसंत, दुष्टों के लिए प्रलयंकारी आंधी):
"ताम्र श्याम घन केशा, शीश जटा बांधी।
सुजन हेतु ऋतु मधुमय, दुष्ट दलन आंधी॥"

भावार्थ:
आपके केश ताम्र-श्याम और घने मेघों के समान हैं, जिन्हें आपने अपने मस्तक पर सन्यासियों व तपस्वियों की भांति सुंदर जटा के रूप में बांध रखा है। आप श्रेष्ठ सज्जनों व संतों के लिए वसंत ऋतु (मधुमय) के समान सुखदायी व आनंदप्रद हैं, किंतु अधर्मी दुष्टों और आतताइयों का दलन करने के लिए साक्षात महाविनाशक आंधी स्वरूप हैं।

५. पंचम पद (सूर्य-तेज मुखमंडल, रक्त वर्ण नयन व गो-विप्र रक्षा):
"मुख रवि तेज विराजत, रक्त वर्ण नैना।
दीन-हीन गो विप्रन, रक्षक दिन रैना॥"

भावार्थ:
आपके मुखमंडल पर भगवान सूर्य के समान अलौकिक ब्रह्मतेज और क्षात्रतेज प्रकाशित है। अधर्म का नाश करने हेतु आपके नेत्र क्रोध व तेज से रक्तिम वर्ण के प्रतीत होते हैं। आप दीन-दुखियों, असहायों, सुरभि गौओं और ब्राह्मणों की दिन-रात (दिन-रैना) नित्य रक्षा करने वाले परम त्राता हैं।

६. षष्ठम पद (वेद-ज्ञाता, वैष्णव धनुष व ब्राह्मण कुल त्राता):
"कर शोभित बर परशु, निगमागम ज्ञाता।
कंध चाप-शर वैष्णव, ब्राह्मण कुल त्राता॥"

भावार्थ:
आपके करकमल में भगवान शिव द्वारा प्रदत्त श्रेष्ठ 'परशु' (फरसा) शोभायमान है। आप समस्त वेदों, उपनिषदों और आगम-निगम शास्त्रों के परम मर्मज्ञ ज्ञाता हैं। आपके कंधे पर भगवान विष्णु का अमोघ वैष्णव धनुष और बाण (चाप-शर) विराजित है तथा आप ब्राह्मण कुल और सनातन धर्म की मर्यादा के परम रक्षक हैं।

७. सप्तम पद (माता-पिता, स्वामी-सखा व अनन्य शरणागति):
"माता पिता तुम स्वामी, मीत सखा मेरे।
मेरी बिरद संभारो, द्वार पड़ा मैं तेरे॥"

भावार्थ:
हे प्रभु परशुराम! आप ही मेरे सच्चे माता, पिता, स्वामी, परम हितैषी और प्रिय सखा हैं। हे दीनानाथ! मैं आपकी शरण में आकर आपके द्वार पर पड़ा हूँ, अतः अपने 'शरणपालक' और 'दीनबंधु' होने के विरद (यश-प्रतिष्ठा) की लाज रखते हुए मेरा उद्धार कीजिए।

८. अष्टम पद (फलश्रुति — अजर-अमर महिमा व सुख-सम्पत्ति प्राप्ति):
"अजर-अमर श्री परशुराम की, आरती जो गावे।
'पूर्णेन्दु' शिव साखि, सुख सम्पति पावे॥"

भावार्थ:
जो भी भक्त अष्ट-चिरंजीवियों में श्रेष्ठ, अजर-अमर भगवान श्री परशुराम जी की इस पावन आरती का नित्य प्रेमपूर्वक गान करता है—भगवान देवाधिदेव शिव साक्षी हैं, वह साधक जीवन में समस्त सुख, ऐश्वर्य, समृद्धि, धर्म-रक्षा का बल और अंत में परम शांति प्राप्त करता है।""",
    "vidhi": """॥ भगवान श्री परशुराम जी आरती — शास्त्रोक्त 4-2-1-7 प्रदक्षिणा व दीप विधान ॥

भगवान विष्णु के षष्ठम अवतार, चिरंजीवी भगवान परशुराम जी की आरती उतारने का विशेष शास्त्रोक्त विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल अथवा तांबे की थाली में शुद्ध गाय के घी का दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाल में श्वेत व पीले पुष्प, रुद्राक्ष, भस्म/चंदन, अक्षत, यज्ञोपवीत, तुलसी दल तथा शुद्ध जल का पात्र रखें। 'ॐ जामदग्न्याय विद्महे महावीराय धीमहि तन्नः परशुरामः प्रचोदयात्' अथवा 'ॐ ब्रह्मक्षत्राय नमः' मन्त्र का स्मरण करें।

२. पावन चरणकमलों में ४ बार घुमाएं:
सर्वप्रथम आरती की ज्योति को दक्षिणावर्त (Clockwise) दिशा में भगवान परशुराम जी के खड़ाऊँ-शोभित चरणकमलों में ४ बार घुमाएं। यह धर्म, अर्थ, काम और मोक्ष के चार पुरुषार्थों की प्राप्ति और चिरंजीवी कृपा की वंदना है।

३. नाभि-मंडल पर २ बार घुमाएं:
तत्पश्चात दीपक को प्रभु के दिव्य नाभि-मंडल के समक्ष २ बार घुमाएं। यह संपूर्ण जगत के आधार और शक्ति के केंद्र का नमन है।

४. तेजपुंज मुखारविन्द पर १ बार घुमाएं:
इसके उपरांत दीपक को भगवान परशुराम जी के त्रिपुण्ड-शोभित, सूर्य-समान तेजस्वी मुखारविन्द के समक्ष १ बार घुमाएं। इससे साधक के चित्त का अज्ञान, भय और कायरता नष्ट होती है तथा आत्मबल में वृद्धि होती है।

५. सम्पूर्ण सर्वांग पर ७ बार घुमाएं:
अंत में आरती की दिव्य ज्योति को जटाजूट, वैष्णव चाप, दिव्य परशु व रुद्राक्ष से लेकर चरणकमलों तक सम्पूर्ण पावन विग्रह पर ७ बार श्रद्धापूर्वक घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवन की शुद्धि व प्रदक्षिणा चक्र पूर्ण होता है।)

६. समर्पण, शंख-नाद एवं आरती ग्रहण:
आरती पूर्ण होने पर शंख, घंटा और 'जय परशुराम', 'जय भृगुनंदन' का जयघोष करें। आचमनी से तीन बार जल थाल के चारों ओर घुमाकर भूमि पर अर्पित करें। दोनों हाथों से आरती की पावन ज्योति का ताप ग्रहण कर अपने शीश, मुख और नेत्रों पर लगाएं।""",
    "significance": """॥ श्री परशुराम आरती (ॐ जय परशुधारी) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. ब्रह्मतेज और क्षात्रतेज का अनुपम संगम:
भगवान परशुराम शास्त्र और शस्त्र दोनों के अद्वितीय अधिष्ठाता हैं। इस आरती के नियमित गान से साधक के जीवन में ज्ञान, मेधा (ब्रह्मतेज) के साथ-साथ साहस, शौर्य और धर्म-रक्षा का पराक्रम (क्षात्रतेज) जाग्रत होता है।

२. अकाल मृत्यु, भय एवं शत्रुओं से सुरक्षा:
"दुष्ट दलन आंधी, दीन-हीन गो विप्रन रक्षक दिन रैना" — जो भक्त नित्य नियम से इस आरती का पाठ करते हैं, उन पर चिरंजीवी प्रभु की छत्रछाया सदा बनी रहती है। उन्हें किसी भी प्रकार के अज्ञात भय, घोर संकट, तंत्र-बाधा अथवा शत्रुओं का भय नहीं रहता।

३. पितृ-भक्ति एवं मातृ-भक्ति का आदर्श:
भगवान परशुराम संसार में पितृ-आज्ञा पालन और मातृ-स्नेह के सर्वोच्च आदर्श हैं। इनके स्मरण से परिवार में संस्कारों की वृद्धि, आज्ञाकारिता और माता-पिता के प्रति निष्ठावान संतानों का निर्माण होता है।

४. अष्ट-चिरंजीवी कृपा एवं अक्षय पुण्य:
भगवान परशुराम कल्प के अंत तक जीवित रहने वाले अष्ट चिरंजीवियों में प्रतिष्ठित हैं। अक्षय तृतीया (परशुराम जयंती) सहित किसी भी शुभ अवसर पर इनके पूजन व आरती से साधक को अक्षय सुख, समृद्धि और आत्मबल प्राप्त होता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक आठ छंद पदों पर पूर्णतः आधारित है।""",
    "english_lyrics": """॥ Shri Parashurama Aarti ॥
(Om Jai Parashudhari)

Om Jai Parashudhari,
Swami Jai Parashudhari।
Sura Nara Munijana Sevata,
Shripati Avatari॥

Om Jai Parashudhari...॥

Jamadagni Suta Nara-Simha,
Maan Renuka Jaaya।
Maartanda Bhrigu Vanshaaja,
Tribhuvana Yasha Chhaaya॥

Om Jai Parashudhari...॥

Kaandhe Sootra Janeoo,
Gala Rudraaksha Maala।
Charana Khadaaoon Shobhe,
Tilaka Tripunda Bhaala॥

Om Jai Parashudhari...॥

Taamra Shyaama Ghana Kesha,
Sheesha Jataa Baandhee।
Sujana Hetu Ritu Madhumaya,
Dushta Dalana Aandhee॥

Om Jai Parashudhari...॥

Mukha Ravi Teja Viraajata,
Rakta Varna Naina।
Deena-Heena Go Viprana,
Rakshaka Dina Raina॥

Om Jai Parashudhari...॥

Kara Shobhita Bara Parashu,
Nigamaagama Gyaata।
Kandha Chaapa-Shara Vaishnava,
Braahmana Kula Traata॥

Om Jai Parashudhari...॥

Maata Pita Tuma Swami,
Meeta Sakhaa Mere।
Meree Birada Sambhaaro,
Dwaara Padaa Main Tere॥

Om Jai Parashudhari...॥

Ajara-Amara Shri Parashurama Ki,
Aarti Jo Gaave।
'Poornendu' Shiva Saakhi,
Sukha Sampati Paave॥

Om Jai Parashudhari...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['surya', 'gods']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_gods_14':
                fg_data[cat_name]['items'][i] = PARASHURAMA_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_gods_14 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_gods_14':
                    cdata['items'][i] = PARASHURAMA_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_gods_14 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(PARASHURAMA_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_gods_14"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_gods_14 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_gods_14 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
