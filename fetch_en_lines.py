import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

url_en = 'https://www.drikpanchang.com/lyrics/aarti/shri-radha/devi-radhika-aarti.html?lang=en'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url_en, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

p_tags = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
for idx in range(min(22, len(p_tags))):
    clean = re.sub(r'<[^>]+>', ' ', p_tags[idx]).strip()
    clean = re.sub(r'\s+', ' ', clean)
    print(f'EN P {idx}:', clean)
