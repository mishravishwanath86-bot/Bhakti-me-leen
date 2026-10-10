import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\.system_generated\steps\4390\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all <div id="verse-([^"]+)" and see the structure
verses = re.findall(r'<div id="verse-([^"]+)".*?href="(/chapter/[^"]+)".*?<p class="[^"]*">(.*?)</p>', text, re.DOTALL)
print("Verses found with loose regex:", len(verses))

for v in verses[:10]:
    clean_text = re.sub(r'<[^>]+>', '', v[2]).strip()
    print(f"Verse {v[0]}: {clean_text[:100]}")

with open('scraped_ch1_verses_raw.json', 'w', encoding='utf-8') as f:
    json.dump([{"verse_id": v[0], "url": v[1], "text": re.sub(r'<[^>]+>', '', v[2]).strip()} for v in verses], f, ensure_ascii=False, indent=2)
print("Saved scraped_ch1_verses_raw.json")
