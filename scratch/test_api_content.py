import sys
import codecs
import requests

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

base_url = "http://localhost:8000"

for ctype in ['aarti', 'chalisa', 'mantra', 'sundarkand']:
    try:
        r = requests.get(f"{base_url}/api/content?type={ctype}&limit=5")
        if r.status_code == 200:
            data = r.json()
            total = data.get('total', 0)
            items = data.get('items', [])
            print(f"API /api/content?type={ctype}: total={total}, items_returned={len(items)}")
            if items:
                print(f"  First item: id={items[0].get('id')} title={items[0].get('title')[:40]} content_len={len(items[0].get('content', ''))}")
        else:
            print(f"API /api/content?type={ctype}: status {r.status_code} {r.text[:100]}")
    except Exception as e:
        print(f"API /api/content?type={ctype}: error {e}")
