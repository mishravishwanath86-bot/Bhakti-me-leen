import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    fg = json.load(f)

for item in fg['ganga']['items']:
    if item['id'] == 'drik_goddesses_28':
        print("Stub item:")
        for k, v in item.items():
            print(f"  {k}: {repr(v)[:80]}")
