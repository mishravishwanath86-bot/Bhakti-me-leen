# -*- coding: utf-8 -*-
"""
Update drik_goddesses_14 (Gayatri Mata Aarti / आरती श्री गायत्रीजी की) in:
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

GAYATRI_DATA = {
    "id": "drik_goddesses_14",
    "title": "आरती श्री गायत्रीजी की",
    "title_en": "Gayatri Mata Aarti (Aarti Shri Gayatriji Ki)",
    "en_line": "Aarti Shri Gayatri Ji Ki, Gyanadeepa Aur Shraddha Ki Baatee",
    "hi_line": "आरती श्री गायत्रीजी की, ज्ञानदीप और श्रद्धा की बाती",
    "sub": "वेदमाता देवमाता माँ गायत्री जी की पावन आरती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_gayatri_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=p_Tas013cKA",
    "video_id": "p_Tas013cKA",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/gayatri-mata/gayatri-mata-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री गायत्रीजी की आरती ॥
(आरती श्री गायत्रीजी की एवं जयति जय गायत्री माता)

आरती श्री गायत्रीजी की।
ज्ञानदीप और श्रद्धा की बाती।
सो भक्ति ही पूर्ति करै जहं घी की॥

आरती श्री गायत्रीजी की...॥

मानस की शुचि थाल के ऊपर।
देवी की ज्योत जगै, जहं नीकी॥

आरती श्री गायत्रीजी की...॥

शुद्ध मनोरथ ते जहां घण्टा।
बाजैं करै आसुह ही की॥

आरती श्री गायत्रीजी की...॥

जाके समक्ष हमें तिहुं लोक कै।
गद्दी मिलै सबहुं लगै फीकी॥

आरती श्री गायत्रीजी की...॥

संकट आवैं न पास कबौ तिन्हें।
सम्पदा और सुख की बनै लीकी॥

आरती श्री गायत्रीजी की...॥

आरती प्रेम सौ नेम सो करि।
ध्यावहिं मूरति ब्रह्म लली की॥

आरती श्री गायत्रीजी की...॥

---

॥ जयति जय गायत्री माता ॥

जयति जय गायत्री माता,
जयति जय गायत्री माता।
सत् मारग पर हमें चलाओ,
जो है सुखदाता॥

जयति जय गायत्री माता...॥

आदि शक्ति तुम अलख निरञ्जन
जग पालन कर्त्री।
दुःख, शोक, भय, क्लेश,
कलह दारिद्रय दैन्य हर्त्री॥

जयति जय गायत्री माता...॥

ब्रह्म रुपिणी, प्रणत पालिनी,
जगतधातृ अम्बे।
भवभयहारी, जनहितकारी,
सुखदा जगदम्बे॥

जयति जय गायत्री माता...॥

भयहारिणि भवतारिणि अनघे,
अज आनन्द राशी।
अविकारी, अघहरी, अविचलित,
अमले, अविनाशी॥

जयति जय गायत्री माता...॥

कामधेनु सत् चित् आनन्दा,
जय गंगा गीता।
सविता की शाश्वती शक्ति,
तुम सावित्री सीता॥

जयति जय गायत्री माता...॥

ऋग्, यजु, साम, अथर्व,
प्रणयिनी, प्रणव महामहिमे।
कुण्डलिनी सहस्रार,
सुषुम्ना, शोभा गुण गरिमे॥

जयति जय गायत्री माता...॥

स्वाहा, स्वधा, शची,
ब्रहाणी, राधा, रुद्राणी।
जय सतरुपा, वाणी, विद्या,
कमला, कल्याणी॥

जयति जय गायत्री माता...॥

जननी हम है, दीन, हीन,
दुःख, दरिद्र के घेरे।
यदपि कुटिल, कपटी कपूत,
तऊ बालक है तेरे॥

जयति जय गायत्री माता...॥

स्नेहसनी करुणामयि माता,
चरण शरण दीजै।
बिलख रहे हम शिशु सुत तेरे,
दया दृष्टि कीजै॥

जयति जय गायत्री माता...॥

काम, क्रोध, मद, लोभ,
दम्भ, दुर्भाव, द्वेष हरिये।
शुद्ध बुद्धि, निष्पाप हृदय,
मन को पवित्र करिये॥

जयति जय गायत्री माता...॥

तुम समर्थ सब भाँति तारिणी,
तुष्टि, पुष्टि त्राता।
सत् मार्ग पर हमें चलाओ,
जो है सुखदाता॥

जयति जय गायत्री माता...॥""",
    "meaning": """॥ श्री गायत्री माता जी की आरती — पद्यवार सम्पूर्ण पावन भावार्थ ॥

(यह पावन आरती समस्त वेदों की जननी, भुवन-भास्कर सविता देवता की प्राण-चेतना तथा सद्बुद्धि प्रदायिनी माँ गायत्री की स्तुति में गाई जाती है। इसके अंतर्गत आंतरिक ज्ञान-आरती 'आरती श्री गायत्रीजी की' तथा विश्व-प्रसिद्ध वैदिक प्रार्थना 'जयति जय गायत्री माता' दोनों का दिव्य समन्वय है।)

=== भाग १: आरती श्री गायत्रीजी की (अध्यात्म-आरती) ===

१. प्रथम पद (ज्ञानदीप, श्रद्धा की बाती व अनन्य भक्ति):
"आरती श्री गायत्रीजी की। ज्ञानदीप और श्रद्धा की बाती। सो भक्ति ही पूर्ति करै जहं घी की॥"
भावार्थ: हे ब्रह्ममयी माँ गायत्री! हम आपके सम्मुख केवल बाह्य दीपक नहीं, अपितु आत्म-ज्ञान का दीपक प्रज्वलित करते हैं, जिसमें हमारी अटूट श्रद्धा ही ज्योति-बत्ती बनती है और आपकी अनन्य, निष्काम भक्ति ही घृत (घी) का कार्य करती है। ऐसी पावन अध्यात्म-आरती हम आपके श्रीचरणों में अर्पित करते हैं।

२. द्वितीय पद (मानस की शुचि थाल व दिव्य ज्योति):
"मानस की शुचि थाल के ऊपर। देवी की ज्योत जगै, जहं नीकी॥"
भावार्थ: हे माता! हमारे इस निष्पाप, निर्मल अंतःकरण (मानस) रूपी पवित्र थाल के ऊपर आपकी ब्रह्म-चेतना की दिव्य ज्योति अत्यंत मनोरम और तेजोमय होकर जगमगा रही है, जो अज्ञान व मोह के अंधकार को समूल नष्ट कर देती है।

३. तृतीय पद (शुद्ध मनोरथ का घंटा-नाद व आशा-पूर्ति):
"शुद्ध मनोरथ ते जहां घण्टा। बाजैं करै आसुह ही की॥"
भावार्थ: जहाँ साधक के अंतःकरण में केवल लोक-कल्याण और सद्बुद्धि का निष्काम संकल्प रूपी घंटा गूंजता है, वहाँ केवल और केवल आपकी अहैतुकी अनुकंपा की ही आशा बंधी रहती है।

४. चतुर्थ पद (त्रैलोक्य के राज्य से भी श्रेष्ठ ब्रह्म-सुख):
"जाके समक्ष हमें तिहुं लोक कै। गद्दी मिलै सबहुं लगै फीकी॥"
भावार्थ: माँ गायत्री की इस पावन ब्रह्म-ज्योति और दर्शन के दिव्य आनंद के सम्मुख यदि हमें तीनों लोकों (स्वर्ग, मर्त्य, पाताल) का साम्राज्य और इंद्र का सिंहासन भी मिल जाए, तो वह सब फीका और तुच्छ प्रतीत होता है।

५. पंचम पद (संकट-मुक्ति व सुख-संपत्ति की अटूट रेखा):
"संकट आवैं न पास कबौ तिन्हें। सम्पदा और सुख की बनै लीकी॥"
भावार्थ: जो भक्त नित्य नियम से इस पावन आरती का गान व ध्यान करते हैं, उनके निकट कोई भी संकट, आधि-व्याधि या भय कभी नहीं फटक सकता। उनके जीवन में धर्म, अर्थ, काम, मोक्ष रूपी समस्त सुख-संपत्ति की अमिट रेखा खिंच जाती है।

६. षष्ठ पद (नियम, प्रेम व ब्रह्म-लली का ध्यान):
"आरती प्रेम सौ नेम सो करि। ध्यावहिं मूरति ब्रह्म लली की॥"
भावार्थ: जो भी पुण्यात्मा मनुष्य अगाध प्रेम और नियमित निष्ठा के साथ यह आरती उतारकर साक्षात परब्रह्म की पुत्री (ब्रह्म लली) माँ गायत्री की पावन मूर्ति का हृदय में ध्यान करता है, वह साक्षात ब्रह्मपद का साक्षात्कार करता है।

=== भाग २: जयति जय गायत्री माता (विश्ववंद्या स्तुति) ===

१. आदि-शक्ति, अलख-निरंजन, अखिल जगत की पालनकर्त्री तथा दुःख, शोक, भय, क्लेश, कलह और दारिद्र्य का समूल नाश करने वाली माँ गायत्री की जय हो।
२. आप ऋग्वेद, यजुर्वेद, सामवेद और अथर्ववेद—चारों वेदों की प्राण-स्वरूपा हैं। ॐकार (प्रणव) की अधिष्ठात्री, कुंडलिनी, सहस्रार और सुषुम्ना नाड़ी की जाग्रत प्राण-चेतना हैं।
३. स्वाहा, स्वधा, शची, ब्रह्माणी, राधा, रुद्राणी, शतरूपा, सरस्वती, लक्ष्मी और कल्याणी—समस्त देवियां आपके ही विग्रह रूप हैं।
४. हे करुणामयी माँ! हम बालक अज्ञानी, दीन-हीन और दुर्गुणों से घिरे हैं, फिर भी आपके ही अबोध शिशु हैं। कृपा कर हमारे काम, क्रोध, लोभ, मोह, दंभ और द्वेष का हरण कीजिए तथा हमें शुद्ध बुद्धि, निष्पाप हृदय और पवित्र मन प्रदान कर सुखदाता सत्पथ पर अग्रसर कीजिए।""",
    "vidhi": """॥ श्री गायत्री माता जी की आरती — नित्य संध्या व प्रभात शास्त्रोक्त 4-2-1-7 विधान ॥

वेदमाता माँ गायत्री जी की आरती उतारने का विशेष शास्त्रोक्त एवं सद्बुद्धि-प्रदायक विधान:

१. दीप प्रज्वलन व पूजा सामग्री:
पीतल, तांबे अथवा चांदी की थाली में शुद्ध गाय के घी का पंचमुखी दीपक अथवा भीमसेनी कर्पूर प्रज्वलित करें। थाली में पीला चंदन, कुंकुम, अक्षत, पीले पुष्प (गेंदा, पीला कमल या कनेर), कलावा, गंगाजल से भरा आचमनी पात्र, धूप (गुग्गल/लोबान) तथा पीले नैवेद्य (खीर, बेसन के लड्डू, हलवा अथवा फल) सजाएं।

२. आरती घुमाने का विशेष शास्त्रीय '४-२-१-७' क्रम:
माँ गायत्री के पंचमुखी सौम्य विग्रह के समक्ष '४-२-१-७' के शास्त्रोक्त क्रम से आरती घुमाएं:
• श्रीचरणों के समक्ष ४ बार: चारों वेदों (ऋक्, यजुः, साम, अथर्व) के ज्ञान, चार पुरुषार्थों की सिद्धि व अहंकार विसर्जन हेतु।
• नाभि मंडल के समक्ष २ बार: प्राण-ऊर्जा की शुद्धि, कुंडलिनी जागरण व मणिपुर चक्र की स्थिरता हेतु।
• मुखारविंद (पंचमुख) के समक्ष १ बार: सद्बुद्धि, विवेक, दिव्य ज्ञान-चक्षु के जागरण व अमृतमयी दृष्टि प्राप्ति हेतु।
• संपूर्ण श्रीविग्रह के समक्ष ७ बार: सप्त-व्याहृतियों (भूर्भुवः स्वः महः जनः तपः सत्यम्) तथा सप्त-चक्रों की जागृति के प्रतीक रूप में गोलाकार घुमाएं।

(४ + २ + १ + ७ = कुल १४ भुवनों की शुद्धि व संपूर्ण ब्रह्म-प्रदक्षिणा चक्र पूर्ण होता है।)

३. विशेष गायत्री महामंत्र:
आरती आरंभ करने से पूर्व 'ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्॥' महामंत्र का त्रिवार सस्वर जप करें।

४. आरती उपरांत आचमन व प्रदक्षिणा:
आरती पूर्ण होने पर कर्पूर दीप पर शीतल जल की तीन बूंदें छिड़ककर आचमन करें। दोनों हाथों से आरती की पावन ज्योति का ताप ग्रहण कर नेत्रों, मस्तक और हृदय से स्पर्श कराएं। माँ गायत्री की ३ बार प्रदक्षिणा करें।""",
    "significance": """॥ श्री गायत्री माता आरती (आरती श्री गायत्रीजी की) — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'गायत्री छन्दसामहम्' — वेदों का परम सार:
श्रीमद्भगवद्गीता (१०.३५) में भगवान श्रीकृष्ण ने स्वयं कहा है—"छन्दसामहं गायत्री" अर्थात् छंदों में मैं स्वयं गायत्री हूँ। माँ गायत्री समस्त वेदों, उपनिषदों और मंत्रों की जननी हैं। इनकी नित्य आरती करने से समस्त वैदिक यज्ञों का सम्मिलित पुण्य प्राप्त होता है।

२. सद्बुद्धि, प्रज्ञा व मेधा-शक्ति की जागृति:
गायत्री साधना का मूल उद्देश्य 'धियो यो नः प्रचोदयात्' है। यह आरती मनुष्य की कुबुद्धि, दुर्विचार, आलस्य और मानसिक अवसाद को दूर कर उसमें ओज, तेज, प्रज्ञा और सात्विक विवेक जाग्रत करती है।

३. त्रिविध तापों व दारिद्र्य का समूल नाश:
आरती के प्रभाव से मनुष्य के आधिभौतिक, आधिदैविक और आध्यात्मिक—तीनों प्रकार के ताप, शोक, कलह और आर्थिक दरिद्रता समूल नष्ट हो जाते हैं तथा घर में ज्ञान और ऐश्वर्य का वास होता है।

४. कुंडलिनी जागरण व आत्म-साक्षात्कार:
माँ गायत्री कुंडलिनी महाशक्ति, सहस्रार और सुषुम्ना की अधिष्ठात्री हैं। नित्य निष्ठा से इस आरती का गान करने से साधक के अंतःकरण के षट्चक्र शुद्ध होकर जाग्रत होते हैं और वह ब्रह्म-चेतना का अनुभव करता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह आरती द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक दोनों अंगों (आरती श्री गायत्रीजी की एवं जयति जय गायत्री माता) पर पूर्णतः आधारित है, जो शांतिकुंज हरिद्वार, गायत्री शक्तिपीठों व कोटि-कोटि सनातन गृहों में नित्य गाई जाती है।""",
    "english_lyrics": """॥ Shri Gayatriji Ki Aarti ॥
(Aarti Shri Gayatriji Ki & Jayati Jai Gayatri Mata)

Aarti Shri Gayatri Ji Ki।
Gyanadeepa Aur Shraddha Ki Baatee।
So Bhakti Hee Poorti Karai Jahan Ghee Ki॥

Aarti Shri Gayatri Ji Ki...॥

Manasa Ki Shuchi Thaala Ke Oopara।
Devi Ki Jyota Jagai, Jahan Neekee॥

Aarti Shri Gayatri Ji Ki...॥

Shuddha Manoratha Te Jahan Ghanta।
Baajain Karai Aasuha Hee Ki॥

Aarti Shri Gayatri Ji Ki...॥

Jaake Samaksha Hamein Tihun Loka Kai।
Gaddee Milai Sabahun Lagai Feekee॥

Aarti Shri Gayatri Ji Ki...॥

Sankata Aavain Na Paasa Kabau Tinhein।
Sampada Aur Sukha Ki Banai Leekee॥

Aarti Shri Gayatri Ji Ki...॥

Aarti Prema Sau Nema So Kari।
Dhyaavahin Moorati Brahma Lalee Ki॥

Aarti Shri Gayatri Ji Ki...॥

---

॥ Jayati Jai Gayatri Mata ॥

Jayati Jai Gayatri Mata,
Jayati Jai Gayatri Mata।
Sat Maaraga Para Hamein Chalao,
Jo Hai Sukhadaata॥

Jayati Jai Gayatri Mata...॥

Aadi Shakti Tuma Alakha Niranjana
Jaga Paalana Kartree।
Duhkha, Shoka, Bhaya, Klesha,
Kalaha Daäridrya Dainya Hartee॥

Jayati Jai Gayatri Mata...॥

Brahma Roopinee, Pranata Paalinee,
Jagatadhaatru Ambe।
Bhavabhayaharee, Janahitakaaree,
Sukhada Jagadambe॥

Jayati Jai Gayatri Mata...॥

Bhayahaarini Bhavataarini Anaghe,
Aja Aananda Raashee।
Avikaaree, Aghaharee, Avichalita,
Amale, Avinaashee॥

Jayati Jai Gayatri Mata...॥

Kaamadhenu Sat Chit Aananda,
Jai Ganga Geeta।
Savita Ki Shaashwatee Shakti,
Tuma Saavitree Seeta॥

Jayati Jai Gayatri Mata...॥

Rig, Yaju, Saama, Atharva,
Pranayinee, Pranava Mahamahime।
Kundalinee Sahasraara,
Sushumna, Shobha Guna Garime॥

Jayati Jai Gayatri Mata...॥

Swaaha, Swadha, Shachee,
Brahmaanee, Radha, Rudraanee।
Jai Satarupa, Vaanee, Vidya,
Kamala, Kalyaanee॥

Jayati Jai Gayatri Mata...॥

Jananee Hama Hai, Deena, Heena,
Duhkha, Daridra Ke Ghere।
Yadapi Kutila, Kapatee Kapoota,
Ta-oo Baalaka Hai Tere॥

Jayati Jai Gayatri Mata...॥

Snehasanee Karunaamayi Mata,
Charana Sharana Deejai।
Bilakha Rahe Hama Shishu Suta Tere,
Daya Drishti Keejai॥

Jayati Jai Gayatri Mata...॥

Kaama, Krodha, Mada, Lobha,
Dambha, Durbhaava, Dwesha Hariye।
Shuddha Buddhi, Nishpaapa Hridaya,
Mana Ko Pavitra Kariye॥

Jayati Jai Gayatri Mata...॥

Tuma Samartha Saba Bhaanti Taarinee,
Tushti, Pushti Traata।
Sat Maarga Para Hamein Chalao,
Jo Hai Sukhadaata॥

Jayati Jai Gayatri Mata...॥"""
}

# 1. Update final_granular_aarti_collections.json
shutil.copyfile(final_json_path, final_json_path + ".bak")
with open(final_json_path, 'r', encoding='utf-8') as f:
    fg_data = json.load(f)

updated_fg = 0
for cat_name in ['gayatri', 'goddesses']:
    if cat_name in fg_data and 'items' in fg_data[cat_name]:
        for i, item in enumerate(fg_data[cat_name]['items']):
            if item.get('id') == 'drik_goddesses_14':
                fg_data[cat_name]['items'][i] = GAYATRI_DATA
                updated_fg += 1
                print(f"[OK] Updated drik_goddesses_14 in final_granular category: {cat_name}")

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
                if item.get('id') == 'drik_goddesses_14':
                    cdata['items'][i] = GAYATRI_DATA
                    updated_full += 1
                    print(f"[OK] Updated drik_goddesses_14 in full_drik category: {cat_name}")
    
    with open(full_json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved full_drik_aarti_collections.json (updated {updated_full} occurrences)")

# 3. Update app.js
shutil.copyfile(app_js_path, app_js_path + ".bak")
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Build indented block
lines = json.dumps(GAYATRI_DATA, ensure_ascii=False, indent=2).splitlines()
indented_lines = ["      " + lines[0]]
for l in lines[1:-1]:
    indented_lines.append("        " + l)
indented_lines.append("      " + lines[-1])
new_block_str = "\n".join(indented_lines)

pos = 0
replaced_count = 0
while True:
    id_pos = app_js.find('"id": "drik_goddesses_14"', pos)
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
        print(f"[OK] Replaced occurrence {replaced_count} of drik_goddesses_14 in app.js")
    else:
        print(f"[ERROR] Could not parse block for drik_goddesses_14 at {id_pos}")
        break

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js)
print(f"[OK] Saved app.js (replaced {replaced_count} occurrences)")
