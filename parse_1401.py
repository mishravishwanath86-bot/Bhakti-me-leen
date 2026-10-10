import json
import re
import sys

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\raw_mcqs_1401.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find each object by scanning for `{\n    "id":`
items = []
# Split by {\n    "id":
chunks = re.split(r'\{\s*"id":\s*', text)
for c in chunks[1:]:
    obj_str = '{\n  "id": ' + c
    # find closing bracket of this object
    idx = obj_str.find('\n  }')
    if idx != -1:
        valid_obj_str = obj_str[:idx+4]
    else:
        # try finding last }
        idx = obj_str.rfind('}')
        if idx != -1:
            valid_obj_str = obj_str[:idx+1]
        else:
            continue
    try:
        obj = json.loads(valid_obj_str)
        items.append(obj)
    except Exception as e:
        # maybe trailing comma
        cleaned = valid_obj_str.rstrip().rstrip(',')
        try:
            obj = json.loads(cleaned)
            items.append(obj)
        except Exception as e2:
            pass

print(f"Total parsed objects: {len(items)}")
if items:
    print(f"First ID: {items[0]['id']}, Last ID: {items[-1]['id']}")
    ids = [x['id'] for x in items]
    print(f"Any missing IDs between {ids[0]} and {ids[-1]}: {set(range(ids[0], ids[-1]+1)) - set(ids)}")
