import sys, json, sqlite3, os
sys.stdout.reconfigure(encoding='utf-8')

with open('all_sanatan_mcqs.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

existing_ids = set(q['id'] for q in questions)
max_id = max(existing_ids)

aarti_questions = [
  {
    "id": max_id + 1,
    "question": "प्रसिद्ध आरती 'जय जगदीश हरे' की रचना 19वीं सदी में किस महान विद्वान ने की थी?",
    "options": ["पंडित श्रद्धाराम फिल्लौरी", "स्वामी दयानंद सरस्वती", "गोस्वामी तुलसीदास जी", "संत सूरदास जी"],
    "correct_answer": 0,
    "explanation": "पंजाब के फिल्लौर में 1870 के आसपास पंडित श्रद्धाराम फिल्लौरी जी ने 'जय जगदीश हरे' की अमर रचना की थी।",
    "category": "aarti"
  },
  {
    "id": max_id + 2,
    "question": "आरती करते समय थाल को भगवान के विग्रह के समक्ष किस प्रकार घुमाने का शास्त्रसम्मत नियम है?",
    "options": ["घड़ी की सुई की दिशा में (दक्षिणावर्त - Clockwise) 'ॐ' की आकृति में", "वामावर्त (Anti-clockwise)", "केवल ऊपर-नीचे", "केवल दाएं-बाएं"],
    "correct_answer": 0,
    "explanation": "आरती की थाली को भगवान के चरणों से लेकर मुखारविंद तक दक्षिणावर्त क्रम में 'ॐ' स्वरूप बनाते हुए घुमाया जाता है।",
    "category": "aarti"
  },
  {
    "id": max_id + 3,
    "question": "भगवान शिव की पावन आरती 'कर्पूरगौरं करुणावतारं...' किस प्राचीन स्तोत्र का श्लोक है?",
    "options": ["यजुर्वेद (शिव संकप्ल सूक्त)", "सामवेद", "ऋग्वेद", "अथर्ववेद"],
    "correct_answer": 0,
    "explanation": "'कर्पूरगौरं करुणावतारं संसारसारं भुजगेन्द्रहारम्' भगवान शिव की स्तुति का वेदोक्त और अत्यंत मंगलकारी श्लोक है।",
    "category": "aarti"
  },
  {
    "id": max_id + 4,
    "question": "आरती में कर्पूर (Camphor) जलाने का आध्यात्मिक एवं वैज्ञानिक रहस्य क्या है?",
    "options": ["कर्पूर बिना कोई राख छोड़े पूर्णतः जल जाता है, जो अहंकार के पूर्ण विलय का प्रतीक है", "केवल सुगंध के लिए", "केवल प्रकाश के लिए", "केवल सजावट के लिए"],
    "correct_answer": 0,
    "explanation": "कर्पूर का जलना भक्त के अहंकार और वासनाओं के प्रभु के चरणों में पूर्ण भस्म होकर लीन होने का प्रतीक है।",
    "category": "aarti"
  },
  {
    "id": max_id + 5,
    "question": "श्री गणेश जी की प्रसिद्ध आरती 'जय गणेश जय गणेश देवा' में 'बांझन को पुत्र देत...' अगली पंक्ति क्या है?",
    "options": ["कोढ़िन को काया", "निर्धन को माया", "अंधे को आंख देत", "दीनन को छाया"],
    "correct_answer": 0,
    "explanation": "'अंधे को आंख देत, कोढ़िन को काया। बांझन को पुत्र देत, निर्धन को माया॥'",
    "category": "aarti"
  },
  {
    "id": max_id + 6,
    "question": "आरती के अंत में भक्त दोनों हाथों को आरती की लौ के ऊपर फिराकर अपने सिर व नेत्रों पर क्यों लगाते हैं?",
    "options": ["दिव्य ज्योति की सकारात्मक ऊर्जा व प्रभु का तेज ग्रहण करने हेतु", "हाथ गर्म करने हेतु", "परंपरा मात्र के लिए", "हाथ धोने के लिए"],
    "correct_answer": 0,
    "explanation": "आरती की पावन ज्योति से प्रभु की दिव्य आभा और सकारात्मक ऊर्जा को अपने मस्तक और नेत्रों में स्थापित किया जाता है।",
    "category": "aarti"
  },
  {
    "id": max_id + 7,
    "question": "संध्या आरती (संध्याकाल की आरती) में मुख्य रूप से किस तत्व के शुद्धिकरण का विधान माना गया है?",
    "options": ["अग्नि तत्व एवं वायु तत्व", "जल तत्व", "पृथ्वी तत्व", "आकाश तत्व"],
    "correct_answer": 0,
    "explanation": "संध्या समय आरती करने से वातावरण की नकारात्मक ऊर्जा नष्ट होती है और अग्नि व वायु का शुद्धिकरण होता है।",
    "category": "aarti"
  },
  {
    "id": max_id + 8,
    "question": "माँ अंबे की प्रसिद्ध आरती 'जय अंबे गौरी' में 'मांग सिंदूर विराजत...' के आगे क्या है?",
    "options": ["टीको मृगमद को", "कुंडल शोभित को", "माला फूलों की", "कंगन हाथों में"],
    "correct_answer": 0,
    "explanation": "'मांग सिंदूर विराजत टीको मृगमद को। उज्ज्वल से दोउ नैना चंद्रवदन नीको॥'",
    "category": "aarti"
  },
  {
    "id": max_id + 9,
    "question": "भगवान श्री राम की आरती 'आरती कीजै रामचन्द्र जी की' में 'कंचन थार कपूर की बाती...' अगली पंक्ति क्या है?",
    "options": ["आरती करत संतन की पाती", "आरती करत जनक सुता साथ", "आरती करत कौशल्या मातु", "आरती करत भरत भ्रातु"],
    "correct_answer": 0,
    "explanation": "'कंचन थार कपूर की बाती। आरती करत संतन की पाती॥'",
    "category": "aarti"
  },
  {
    "id": max_id + 10,
    "question": "आरती के समय शंखनाद और घंटी बजाने का क्या आध्यात्मिक प्रभाव होता है?",
    "options": ["'ॐ' की ध्वनि उत्पन्न कर वातावरण की नकारात्मक तरंगों को नष्ट करना", "केवल भक्तों को बुलाना", "केवल संगीत उत्पन्न करना", "समय बताना"],
    "correct_answer": 0,
    "explanation": "शंख व घंटी की ध्वनि नादब्रह्म की तरंगें उत्पन्न करती है जो मस्तिष्क के बाएं व दाएं गोलार्ध को संतुलित करती है।",
    "category": "aarti"
  }
]

chalisa_questions = [
  {
    "id": max_id + 11,
    "question": "हनुमान चालीसा के अनुसार अष्ट सिद्धि और नौ निधियों के दाता होने का वरदान किसने दिया?",
    "options": ["माता सीता", "प्रभु श्री राम", "सूर्य देव", "भगवान शिव"],
    "correct_answer": 0,
    "explanation": "माता सीता ने अशोक वाटिका में प्रसन्न होकर हनुमान जी को 'अष्ट सिद्धि नवनिधि के दाता। अस बर दीन जानकी माता॥' का वरदान दिया था।",
    "category": "chalisa"
  },
  {
    "id": max_id + 12,
    "question": "हनुमान चालीसा में सूर्य और पृथ्वी के बीच की दूरी का वर्णन किस चौपाई में मिलता है?",
    "options": ["जुग सहस्र जोजन पर भानू। लील्यो ताहि मधुर फल जानू॥", "जय हनुमान ज्ञान गुन सागर", "भीम रूप धरि असुर संहारे", "दुर्गम काज जगत के जेते"],
    "correct_answer": 0,
    "explanation": "जुग (12000) × सहस्र (1000) × जोजन (8 मील) = 96,000,000 मील (15.36 करोड़ किमी), जो सूर्य की खगोलीय दूरी है।",
    "category": "chalisa"
  },
  {
    "id": max_id + 13,
    "question": "शिव चालीसा के अनुसार भगवान शिव ने समुद्र मंथन से निकले हलाहल विष को कहाँ धारण किया था?",
    "options": ["कंठ में (जिससे वे नीलकंठ कहलाए)", "मस्तक पर", "हृदय में", "जटाओं में"],
    "correct_answer": 0,
    "explanation": "भगवान शिव ने संपूर्ण सृष्टि की रक्षा के लिए विष को अपने कंठ में रोक लिया, जिससे उनका कंठ नीला पड़ गया।",
    "category": "chalisa"
  },
  {
    "id": max_id + 14,
    "question": "हनुमान चालीसा की शुरुआत किस प्रसिद्ध दोहे से होती है?",
    "options": ["श्रीगुरु चरन सरोज रज निज मनु मुकुरु सुधारि।", "जय हनुमान ज्ञान गुन सागर", "पवनतनय संकट हरन", "रामदूत अतुलित बलधामा"],
    "correct_answer": 0,
    "explanation": "'श्रीगुरु चरन सरोज रज निज मनु मुकुरु सुधारि। बरनउँ रघुबर बिमल जसु जो दायकु फल चारि॥'",
    "category": "chalisa"
  },
  {
    "id": max_id + 15,
    "question": "दुर्गा चालीसा में 'नमो नमो दुर्गे सुख करनी...' के बाद अगली पंक्ति क्या है?",
    "options": ["नमो नमो अंबे दुःख हरनी", "निरंकार है ज्योति तुम्हारी", "सब उजियार तिहूं लोक मंजारी", "शशि ललाट मुख महाविशाला"],
    "correct_answer": 0,
    "explanation": "'नमो नमो दुर्गे सुख करनी। नमो नमो अंबे दुःख हरनी॥'",
    "category": "chalisa"
  },
  {
    "id": max_id + 16,
    "question": "हनुमान चालीसा में 'लाय सजीवन लखन जियाये। श्रीरघुबीर...' अगली पंक्ति क्या है?",
    "options": ["हरषि उर लाये", "अति बड़भागी", "प्रेम बढ़ायो", "हर्ष अपारा"],
    "correct_answer": 0,
    "explanation": "'लाय सजीवन लखन जियाये। श्रीरघुबीर हरषि उर लाये॥'",
    "category": "chalisa"
  },
  {
    "id": max_id + 17,
    "question": "गायत्री चालीसा के अनुसार माँ गायत्री को किस रूप में स्तुति की गई है?",
    "options": ["वेदमाता एवं ज्ञानदायिनी", "केवल धनदायिनी", "केवल शक्तिदायिनी", "केवल अन्नपूर्णा"],
    "correct_answer": 0,
    "explanation": "माँ गायत्री को चारों वेदों की जननी (वेदमाता) और सद्बुद्धि प्रदान करने वाली ज्ञानदायिनी माना गया है।",
    "category": "chalisa"
  },
  {
    "id": max_id + 18,
    "question": "हनुमान चालीसा के अंतिम दोहे 'पवनतनय संकट हरन मंगल मूरति रूप...' में किन-किन को हृदय में बसने की प्रार्थना की गई है?",
    "options": ["राम, लखन और सीता सहित", "केवल श्री राम", "केवल लक्ष्मण", "केवल भरत"],
    "correct_answer": 0,
    "explanation": "'पवनतनय संकट हरन, मंगल मूरति रूप। राम लखन सीता सहित, हृदय बसहु सुर भूप॥'",
    "category": "chalisa"
  },
  {
    "id": max_id + 19,
    "question": "शनि चालीसा में शनि देव के किस वाहन का विशेष महत्व बताया गया है?",
    "options": ["कौआ (काक)", "मयूर", "हंस", "गज (हाथी)"],
    "correct_answer": 0,
    "explanation": "शनि देव का मुख्य वाहन काक (कौआ) है, यद्यपि विभिन्न राशियों में वे गज, अश्व आदि पर भी सवार होते हैं।",
    "category": "chalisa"
  },
  {
    "id": max_id + 20,
    "question": "हनुमान चालीसा में 'सूक्ष्म रूप धरि सियहिं दिखावा...' के बाद कौन सा रूप धारण करने का वर्णन है?",
    "options": ["बिकट रूप धरि लंक जरावा", "भीम रूप धरि असुर संहारे", "कनक बदन बिराज सुबेसा", "प्रभु चरित्र सुनिबे को रसिया"],
    "correct_answer": 0,
    "explanation": "'सूक्ष्म रूप धरि सियहिं दिखावा। बिकट रूप धरि लंक जरावा॥'",
    "category": "chalisa"
  }
]

questions.extend(aarti_questions)
questions.extend(chalisa_questions)

with open('all_sanatan_mcqs.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# Update SQLite db
os.makedirs('assets', exist_ok=True)
db_path = 'assets/quiz_database.db'
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    options TEXT NOT NULL,
    correct_answer INTEGER NOT NULL,
    explanation TEXT,
    category TEXT,
    is_bookmarked INTEGER DEFAULT 0
)
""")

for q in questions:
    cursor.execute("""
    INSERT INTO questions (id, question, options, correct_answer, explanation, category, is_bookmarked)
    VALUES (?, ?, ?, ?, ?, ?, 0)
    """, (
        q['id'],
        q['question'],
        json.dumps(q['options'], ensure_ascii=False),
        q['correct_answer'],
        q.get('explanation', ''),
        q.get('category', 'All')
    ))

conn.commit()
total_cnt = cursor.execute("SELECT count(*) FROM questions").fetchone()[0]
conn.close()

print(f"Total MCQs after enrichment: {len(questions)}")
from collections import Counter
counts = Counter([q['category'] for q in questions])

category_names = {
    'all': '🎯 संपूर्ण क्विज़ (Mega)',
    'god': '🪔 देवी-देवता एवं अवतार',
    'ved': '📜 वेद एवं उपनिषद',
    'mahabharat': '⚔️ महाभारत एवं गीता',
    'ramayan': '🏹 रामायण एवं चरित',
    'mantra': '🕉️ मंत्र एवं स्तोत्र',
    'aarti': '🪔 पावन आरती',
    'chalisa': '📖 चालीसा',
    'bhakti_sahitya': '🌸 भक्ति आंदोलन व साहित्य'
}

print("\nFinal Verified Categories Breakdown:")
for cat, cnt in counts.items():
    print(f"  {category_names.get(cat, cat)} (`{cat}`): {cnt} questions")

