import json
import random
import re

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\raw_mcqs_1801.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse JSON array
start_idx = text.find('[')
end_idx = text.rfind(']')
if start_idx != -1 and end_idx != -1:
    json_str = text[start_idx:end_idx+1]
    items = json.loads(json_str)
else:
    raise ValueError("Could not find JSON array brackets")

print(f"Total parsed items: {len(items)}")
assert len(items) == 100
assert items[0]['id'] == 1801
assert items[-1]['id'] == 1900

random.seed(42)

shuffled_1801_1900 = []
for item in items:
    options = list(item["options"])
    correct_option = options[item["correct_answer"]]
    random.shuffle(options)
    new_correct_idx = options.index(correct_option)
    
    shuffled_1801_1900.append({
        "id": item["id"],
        "question": item["question"],
        "options": options,
        "correct_answer": new_correct_idx,
        "explanation": item["explanation"]
    })

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\shuffled_1801_1900.json', 'w', encoding='utf-8') as f:
    json.dump(shuffled_1801_1900, f, ensure_ascii=False, indent=2)

print("Saved shuffled_1801_1900.json successfully!")
