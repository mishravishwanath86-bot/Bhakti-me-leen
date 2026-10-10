import json, os, re
from html.parser import HTMLParser

cache_path = os.path.join("chalisa_cache", "43_shakambhari-mata-chalisa.html")
with open(cache_path, "r", encoding="utf-8") as f:
    html = f.read()

# Let's find where lyrics are in the html
# Drik Panchang lyrics are usually inside <div class="dpLyricsCard"> or <div class="dpVerse"> etc.
# Or let's search for "शाकम्भरी"
match = re.search(r'शाकम्भरी', html)
if match:
    start = max(0, match.start() - 500)
    end = min(len(html), match.start() + 3000)
    print("Found Shakambhari at index", match.start())
    # write snippet to file to inspect
    with open("shakambhari_snippet.txt", "w", encoding="utf-8") as f:
        f.write(html[start:end])
    print("Snippet written to shakambhari_snippet.txt")

# Let's check where the chalisa is in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found_items = []
for cat_id, cat in cols.items():
    for item in cat.get("items", []):
        if "shakambhari" in item.get("id", "").lower() or "shakambhari" in item.get("drik_url", "").lower() or "43" in item.get("id", "") or "शाकम्भरी" in item.get("title", ""):
            found_items.append((cat_id, item['id'], item.get('title'), item.get('title_en'), item.get('drik_url')))

with open("shakambhari_match.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(found_items, ensure_ascii=False, indent=2))
print("Match items:", len(found_items))
