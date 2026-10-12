import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    aartis = json.load(f)

print(f'Total collections: {len(aartis)}')
empty_content = []
for k, coll in aartis.items():
    items = coll.get('items', [])
    for idx, item in enumerate(items):
        cnt = (item.get('content') or item.get('text') or '').strip()
        if not cnt:
            empty_content.append((k, idx, item.get('title'), item.get('id')))

print(f'Aartis with empty content: {len(empty_content)}')
for e in empty_content[:10]:
    print(' ', e)
