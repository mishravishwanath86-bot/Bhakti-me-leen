import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Downloading translation.json...")
req = urllib.request.Request("https://raw.githubusercontent.com/gita/gita/master/data/translation.json", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = r.read().decode('utf-8')
    with open('gita_raw_translations.json', 'w', encoding='utf-8') as out:
        out.write(data)

print(f"Saved gita_raw_translations.json ({len(data)} bytes).")
