import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('final_granular_aarti_collections.json', encoding='utf-8') as f:
    data = json.load(f)

for k, coll in data.items():
    for item in coll.get('items', []):
        if 'जुगल किशोर' in item.get('title', '') or 'जुगल किशोर' in item.get('hi_line', ''):
            print('Coll:', k)
            print('Title:', item.get('title'))
            print('hi_line:', item.get('hi_line'))
            print('content len:', len(item.get('content', '') or ''))
            print('content preview:', repr((item.get('content') or '')[:80]))
            print('meaning len:', len(item.get('meaning', '') or ''))
            print('vidhi len:', len(item.get('vidhi', '') or ''))
            print('sig len:', len(item.get('significance', '') or ''))
