import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

url_en = 'https://www.drikpanchang.com/lyrics/aarti/shri-radha/devi-radhika-aarti.html?lang=en'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url_en, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    print('FETCH EN OK! Len:', len(html))
    p_tags = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
    for idx, p in enumerate(p_tags):
        clean = re.sub(r'<[^>]+>', ' ', p).strip()
        if 'Aarati' in clean or 'Vrishbhanu' in clean or 'lali' in clean or 'Radha' in clean:
            print(f'EN P {idx}:', clean[:200])
except Exception as e:
    print('ERR:', e)
