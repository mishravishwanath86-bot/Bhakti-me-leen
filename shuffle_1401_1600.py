import json
import random
import re

# Load parsed 1401-1598
with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\raw_mcqs_1401.txt', 'r', encoding='utf-8') as f:
    text = f.read()

items = []
chunks = re.split(r'\{\s*"id":\s*', text)
for c in chunks[1:]:
    obj_str = '{\n  "id": ' + c
    idx = obj_str.find('\n  }')
    if idx != -1:
        valid_obj_str = obj_str[:idx+4]
    else:
        idx = obj_str.rfind('}')
        if idx != -1:
            valid_obj_str = obj_str[:idx+1]
        else:
            continue
    try:
        obj = json.loads(valid_obj_str)
        items.append(obj)
    except Exception:
        cleaned = valid_obj_str.rstrip().rstrip(',')
        try:
            obj = json.loads(cleaned)
            items.append(obj)
        except Exception:
            pass

# Add 1599 and 1600
q1599 = {
    "id": 1599,
    "question": "महाभारत और पुराणों के अनुसार कलियुग का आरंभ किस ऐतिहासिक व खगोलीय घटना के तत्काल बाद माना जाता है?",
    "options": [
        "भगवान श्री कृष्ण के अपने परम धाम (स्वधाम) गमन के ठीक बाद",
        "कुरुक्षेत्र युद्ध के प्रथम दिन",
        "राजा परीक्षित के जन्म के समय",
        "युधिष्ठिर के राज्याभिषेक के समय"
    ],
    "correct_answer": 0,
    "explanation": "श्रीमद्भागवत एवं महाभारत मौसल पर्व के अनुसार, जिस दिन और जिस क्षण भगवान श्री कृष्ण ने पृथ्वी से स्वधाम गमन किया, उसी क्षण से कलियुग का प्रभाव आरंभ हुआ।"
}

q1600 = {
    "id": 1600,
    "question": "महाभारत के 18 पर्वों में 'शांति पर्व' के पश्चात कौन सा पर्व आता है जिसमें दान, सदाचार और मोक्ष के गूढ़ नियमों का वर्णन है?",
    "options": [
        "अनुशासन पर्व (Anushasana Parva)",
        "अश्वमेधिक पर्व",
        "स्त्री पर्व",
        "सौप्तिक पर्व"
    ],
    "correct_answer": 0,
    "explanation": "शांति पर्व के उपरांत 13वां पर्व 'अनुशासन पर्व' है, जिसमें पितामह भीष्म द्वारा युधिष्ठिर को दिए गए धर्म, नीति, दान और विष्णु सहस्रनाम का विस्तार से वर्णन है।"
}

items.append(q1599)
items.append(q1600)

print(f"Total items before shuffling: {len(items)}")
assert len(items) == 200, f"Expected 200 items, got {len(items)}"

random.seed(42)  # For deterministic shuffling

shuffled_items = []
for item in items:
    options = list(item["options"])
    correct_option = options[item["correct_answer"]]
    random.shuffle(options)
    new_correct_idx = options.index(correct_option)
    
    shuffled_items.append({
        "id": item["id"],
        "question": item["question"],
        "options": options,
        "correct_answer": new_correct_idx,
        "explanation": item["explanation"]
    })

# Save all 200
with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\shuffled_1401_1600.json', 'w', encoding='utf-8') as f:
    json.dump(shuffled_items, f, ensure_ascii=False, indent=2)

# Save 1401-1500
with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\shuffled_1401_1500.json', 'w', encoding='utf-8') as f:
    json.dump(shuffled_items[:100], f, ensure_ascii=False, indent=2)

# Save 1501-1600
with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\shuffled_1501_1600.json', 'w', encoding='utf-8') as f:
    json.dump(shuffled_items[100:], f, ensure_ascii=False, indent=2)

print("Saved all shuffled datasets successfully!")
