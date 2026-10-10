import urllib.request, os, sys
sys.stdout.reconfigure(encoding='utf-8')

urls = {
    'chalisa_cache/narasimha_chalisa_hi.html': 'https://www.drikpanchang.com/lyrics/chalisa/lord-narasimha/narasimha-chalisa.html?lang=hi&ck=1',
    'chalisa_cache/narasimha_chalisa_en.html': 'https://www.drikpanchang.com/lyrics/chalisa/lord-narasimha/narasimha-chalisa.html?lang=en&ck=1'
}

for path, url in urls.items():
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"Saved to {path}, size: {len(data)} chars")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
