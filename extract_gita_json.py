import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://bhagavadgita.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Extract all JSON arrays in self.__next_f.push
pushes = re.findall(r'self\.__next_f\.push\(\[1,"([\s\S]*?)"\]\)', html)
print(f"Total pushes: {len(pushes)}")

all_text = ""
for p in pushes:
    # unescape
    unescaped = p.encode('utf-8').decode('unicode_escape', errors='ignore')
    all_text += unescaped

# Find chapters array in unescaped text
idx = all_text.find('"chapters":[')
if idx != -1:
    print("Found chapters array at:", idx)
    # find ending
    end_idx = all_text.find(']}', idx)
    snippet = all_text[idx:end_idx+2]
    print("Snippet length:", len(snippet))
    try:
        data = json.loads('{' + snippet + '}')
        chapters = data['chapters']
        print("Total chapters parsed:", len(chapters))
        for c in chapters:
            print(f"Chapter {c.get('chapter_number')}: {c.get('name')} | {c.get('name_transliterated')} | {c.get('name_translated')} | Verses: {c.get('verses_count')}")
    except Exception as e:
        print("Parse error on snippet:", e)
        print(snippet[:500])
else:
    print("Could not find chapters array")
