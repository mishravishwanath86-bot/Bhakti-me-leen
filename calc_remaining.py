import json, sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('final_granular_aarti_collections.json', encoding='utf-8'))

remaining_cats = [k for k in data if k not in ['sants', 'gita', 'gods', 'goddesses']]
print("Remaining granular categories:", remaining_cats)

total_items = 0
for k in remaining_cats:
    cnt = len(data[k]['items'])
    total_items += cnt
    print(f"  {k}: {cnt} items ({data[k]['title']})")

print(f"\nTotal unique aartis across active granular categories: {total_items}")
