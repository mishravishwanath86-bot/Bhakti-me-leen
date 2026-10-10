import json

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate drik_rama_6
pos6 = text.find('"id": "drik_rama_6"')
shiva_pos = text.find('"shiva": {', pos6)

with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

raghupati_item = None
for it in collections['rama']['items']:
    if it.get('id') == 'drik_rama_6':
        raghupati_item = it
        break

if not raghupati_item:
    raise Exception("drik_rama_6 not found in JSON")

brace_start = text.rfind('{', 0, pos6)

# Format replacement block
new_item_str = json.dumps(raghupati_item, ensure_ascii=False, indent=8)
replacement = new_item_str + "\n    ]\n  },\n  "

text_fixed = text[:brace_start] + replacement + text[shiva_pos:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(text_fixed)

print("[OK] app.js syntax fixed around drik_rama_6 and shiva!")
