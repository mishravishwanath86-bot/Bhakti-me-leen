import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = {
    'hi': 'https://www.drikpanchang.com/lyrics/aarti/lakshmi-mata/lakshmi-mata-aarti.html?lang=hi&ck=1',
    'en': 'https://www.drikpanchang.com/lyrics/aarti/lakshmi-mata/lakshmi-mata-aarti.html?lang=en&ck=1'
}

for lang, url in urls.items():
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            content = response.read().decode('utf-8')
            with open(f'lakshmi_mata_{lang}.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Saved lakshmi_mata_{lang}.html ({len(content)} bytes)')
    except Exception as e:
        print(f'Error fetching {lang}: {e}')
