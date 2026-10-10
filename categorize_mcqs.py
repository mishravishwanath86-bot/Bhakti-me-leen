import json, re

with open('all_sanatan_mcqs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Auto-categorize based on keywords
for q in data:
    text = (q['question'] + " " + q.get('explanation', '') + " " + " ".join(q.get('options', []))).lower()
    
    if any(k in text for k in ['गीता', 'अर्जुन', 'कृष्ण', 'कुरुक्षेत्र', 'अध्याय', 'श्लोक', 'निष्काम', 'गांडीव', 'संजय', 'भीष्म', 'द्रौपदी', 'महाभारत', 'कर्ण', 'युधिष्ठिर']):
        q['category'] = 'gita'
    elif any(k in text for k in ['चालीसा', 'चौपाई', 'दोहा', 'हनुमान', 'अष्ट सिद्धि', 'लंकिनी', 'संजीवनी', 'सुग्रीव', 'जाम्बवंत', 'विभीषण', 'ताड़का', 'केसरी', 'अंजना']):
        q['category'] = 'chalisa'
    elif any(k in text for k in ['कम्बोडिया', 'अंगकोर', 'नेपाल', 'पशुपतिनाथ', 'इंडोनेशिया', 'जावा', 'बाली', 'प्रम्बानन', 'मलेशिया', 'बाटू', 'मॉरीशस', 'श्रीलंका', 'मुन्नेश्वरम', 'वियतनाम', 'पाकिस्तान', 'कटास राज', 'अमेरिका', 'अक्षरधाम न्यू जर्सी']):
        q['category'] = 'world'
    elif any(k in text for k in ['रामायण', 'रामचरितमानस', 'वाल्मीकि', 'अयोध्या', 'सरयू', 'जनकपुर', 'सीता', 'दशरथ', 'कौशल्या', 'विश्वामित्र', 'धनुष', 'वनवास', 'पंचवटी', 'शबरी', 'सेतु']):
        q['category'] = 'ramayana'
    elif any(k in text for k in ['मंदिर', 'ज्योतिर्लिंग', 'शक्तिपीठ', 'धाम', 'केदारनाथ', 'बद्रीनाथ', 'सोमनाथ', 'उज्जैन', 'महाकाल', 'काशी', 'विश्वनाथ', 'रामेश्वरम', 'तिरुपति', 'जगन्नाथ', 'पुरी', 'मीनाक्षी', 'कामाख्या', 'असम', 'गुजरात', 'गोपुरम']):
        q['category'] = 'india'
    else:
        # Default distribution
        q['category'] = 'india'

with open('all_sanatan_mcqs.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

from collections import Counter
cats = Counter([q['category'] for q in data])
print("Categorized counts:")
for cat, cnt in cats.items():
    print(f"  {cat}: {cnt} questions")
print(f"Total: {len(data)} questions categorized successfully!")
