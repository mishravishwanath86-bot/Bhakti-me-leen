import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.drikpanchang.com/lyrics/chalisa/chalisa-collection.html?lang=hi"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    with open('chalisa_collection_raw.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fetched successfully! Length:", len(html))
except Exception as e:
    print("Fetch error:", e)
