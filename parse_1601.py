import json
import re
import sys

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

print(f"Total parsed items: {len(items)}")
if items:
    print(f"First ID: {items[0]['id']}, Last ID: {items[-1]['id']}")
    ids = [x['id'] for x in items]
    print("IDs count:", len(ids))
    missing = set(range(ids[0], ids[-1]+1)) - set(ids)
    print(f"Missing IDs: {missing}")

# Check end of file for truncated question
print("Last 300 chars of text:")
print(text[-300:])
