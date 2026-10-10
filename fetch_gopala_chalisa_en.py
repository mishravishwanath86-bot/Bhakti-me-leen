import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url_en = 'https://www.drikpanchang.com/lyrics/chalisa/lord-gopala/shri-gopala-chalisa.html?lang=en'
try:
    req = urllib.request.Request(url_en, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as res:
        en_html = res.read().decode('utf-8')
    with open('chalisa_cache/8_shri-gopala-chalisa_en.html', 'w', encoding='utf-8') as f:
        f.write(en_html)
    print("Successfully fetched English page, length:", len(en_html))
except Exception as e:
    print("Error fetching English page:", e)
