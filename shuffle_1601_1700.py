import json
import random
import re

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\raw_mcqs_1601.txt', 'r', encoding='utf-8') as f:
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

# Filter 1601-1700
items_1601_1700 = [x for x in items if 1601 <= x['id'] <= 1700]
print(f"Total items for 1601-1700: {len(items_1601_1700)}")
assert len(items_1601_1700) == 100

random.seed(42)

shuffled_1601_1700 = []
for item in items_1601_1700:
    options = list(item["options"])
    correct_option = options[item["correct_answer"]]
    random.shuffle(options)
    new_correct_idx = options.index(correct_option)
    
    shuffled_1601_1700.append({
        "id": item["id"],
        "question": item["question"],
        "options": options,
        "correct_answer": new_correct_idx,
        "explanation": item["explanation"]
    })

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\shuffled_1601_1700.json', 'w', encoding='utf-8') as f:
    json.dump(shuffled_1601_1700, f, ensure_ascii=False, indent=2)

print("Saved shuffled_1601_1700.json successfully!")
