import requests

base_url = "http://localhost:8000"
for ctype in ['aarti', 'chalisa', 'mantra', 'sundarkand']:
    r = requests.get(f"{base_url}/api/content?type={ctype}&limit=5")
    data = r.json()
    total = data['pagination']['total_items']
    print(f"API /api/content?type={ctype}: total_items={total}, returned={len(data['items'])}")
