import json
import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

types = ['sundarkand', 'mantra', 'chalisa', 'aarti']
for t in types:
    url = f'http://localhost:8000/api/content?type={t}&limit=5'
    try:
        with urllib.request.urlopen(url) as r:
            data = json.loads(r.read().decode('utf-8'))
            print(f'=== API /api/content?type={t} ===')
            print(f'Total in DB: {data.get("total")}, Items returned: {len(data.get("items", []))}')
            for item in data.get('items', [])[:2]:
                print(f'  ID: {item.get("id")}, Title: {item.get("title")}, Content len: {len(item.get("content", ""))} chars')
    except Exception as e:
        print(f'Error fetching {t}: {e}')
