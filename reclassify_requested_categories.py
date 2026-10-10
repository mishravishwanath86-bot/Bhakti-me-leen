import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('all_sanatan_mcqs.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions to categorize: {len(questions)}")

for q in questions:
    full_text = (q['question'] + " " + q.get('explanation', '') + " " + " ".join(q.get('options', []))).lower()
    
    # 1. Bhakti Sahitya & Saints
    if any(w in full_text for w in ['कबीर', 'मीराबाई', 'सूरदास', 'रसखान', 'चैतन्य महाप्रभु', 'संत ज्ञानेश्वर', 'तुकाराम', 'नामदेव', 'रविदास', 'नरसी मेहता', 'भक्ति आंदोलन', 'वल्लभाचार्य', 'रामानुजाचार्य', 'माध्वाचार्य', 'निम्बार्क', 'शंकराचार्य', 'अष्टछाप', 'पद्मावत', 'साखी', 'बीजक', 'दोहावली', 'कवितावली', 'विनय पत्रिका', 'भक्तमाल']):
        q['category'] = 'bhakti_sahitya'
    
    # 2. Aarti
    elif any(w in full_text for w in ['आरती', 'जय जगदीश हरे', 'ओम जय जगदीश', 'कर्पूरगौरं', 'आरती कीजै', 'पंचारती', 'दीप दान', 'अखंड जोत']):
        q['category'] = 'aarti'

    # 3. Chalisa
    elif any(w in full_text for w in ['चालीसा', 'हनुमान चालीसा', 'शिव चालीसा', 'दुर्गा चालीसा', 'गायत्री चालीसा', 'गणेश चालीसा', 'लक्ष्मी चालीसा', 'शनि चालीसा', 'अष्ट सिद्धि नवनिधि', 'जुग सहस्र जोजन', 'संकटमोचन']):
        q['category'] = 'chalisa'

    # 4. Mantra & Stotra
    elif any(w in full_text for w in ['मंत्र', 'स्तोत्र', 'महामृत्युंजय', 'गायत्री मंत्र', 'बीज मंत्र', 'रुद्राष्टकम', 'विष्णु सहस्रनाम', 'ललिता सहस्रनाम', 'शिव तांडव', 'हनुमान बाहुक', 'कवच', 'न्यास', 'जप', 'संध्या वंदन']):
        q['category'] = 'mantra'

    # 5. Ramayana
    elif any(w in full_text for w in ['रामायण', 'रामचरितमानस', 'वाल्मीकि', 'श्री राम', 'सीता', 'लक्ष्मण', 'भरत', 'शत्रुघ्न', 'दशरथ', 'कौशल्या', 'सुमित्रा', 'कैकेयी', 'जनक', 'विश्वामित्र', 'वशिष्ठ', 'हनुमान', 'सुग्रीव', 'बाली', 'अंगद', 'जाम्बवंत', 'विभीषण', 'रावण', 'मेघनाद', 'कुंभकर्ण', 'ताड़का', 'सूर्पणखा', 'शबरी', 'जटायु', 'संपाती', 'मारीच', 'खर-दूषण', 'पंचवटी', 'किष्किंधा', 'अशोक वाटिका', 'लंका', 'सरयू', 'अयोध्या', 'दंडकारण्य']):
        q['category'] = 'ramayan'

    # 6. Mahabharat & Gita
    elif any(w in full_text for w in ['महाभारत', 'गीता', 'भगवद्गीता', 'कृष्ण', 'अर्जुन', 'युधिष्ठिर', 'भीम', 'नकुल', 'सहदेव', 'द्रौपदी', 'कुंती', 'गांधारी', 'धृतराष्ट्र', 'दुर्योधन', 'दुशासन', 'कर्ण', 'भीष्म', 'द्रोणाचार्य', 'कृपाचार्य', 'अश्वत्थामा', 'विदुर', 'संजय', 'शकुनि', 'कुरुक्षेत्र', 'गांडीव', 'सुदर्शन', 'अक्षौहिणी', 'हस्तिनापुर', 'इंद्रप्रस्थ', 'विश्वरूप', 'स्थितप्रज्ञ', 'निष्काम कर्म']):
        q['category'] = 'mahabharat'

    # 7. Ved & Upanishad
    elif any(w in full_text for w in ['वेद', 'ऋग्वेद', 'सामवेद', 'यजुर्वेद', 'अथर्ववेद', 'उपनिषद', 'मांडूक्य', 'कठोपनिषद', 'ईशावास्य', 'छांदोग्य', 'बृहदारण्यक', 'ब्राह्मण ग्रंथ', 'आरण्यक', 'वेदांग', 'श्रुति', 'स्मृति', 'षड्दर्शन', 'सांख्य', 'योग सूत्र', 'न्याय', 'वैशेषिक', 'मीमांसा', 'वेदांत', 'ब्रह्मसूत्र', 'महर्षि व्यास', 'याज्ञवल्क्य', 'गार्गी', 'मैत्रेयी', 'सत्यमेव जयते', 'अहं ब्रह्मास्मि', 'तत्त्वमसि']):
        q['category'] = 'ved'

    # 8. God / Deities / Avatars
    else:
        q['category'] = 'god'

with open('all_sanatan_mcqs.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

from collections import Counter
counts = Counter([q['category'] for q in questions])
print("\nUpdated Categories Distribution:")
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

for cat, cnt in counts.items():
    print(f"  {category_names.get(cat, cat)} ({cat}): {cnt} questions")
