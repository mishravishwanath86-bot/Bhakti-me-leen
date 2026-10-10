import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/11_shri-vishnu-chalisa_en.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="dpLyricsBlockId"')
block_end = text.find('class="dpLyricsVideoWrapper"', start)
if block_end == -1:
    block_end = text.find('class="dpPageNavigation', start)

lyrics_html = text[start:block_end]

parts = re.findall(r'(<h3[^>]*>.*?</h3>|<div class="dpLyricsChalisaGroup">.*?</div>)', lyrics_html, re.DOTALL)
print(f"Total parts in English: {len(parts)}")

all_verses = []
for p in parts:
    if '<h3' in p:
        heading = re.sub(r'<[^>]+>', '', p).strip()
        all_verses.append(f"\n{heading}\n")
    else:
        groups = re.findall(r'<p class="dpGroup">(.*?)</p>', p, re.DOTALL)
        for g in groups:
            rows = re.findall(r'<span class="dpRow">(.*?)</span>', g)
            line = ' '.join(r.strip() for r in rows).strip()
            if line:
                all_verses.append(line)

for v in all_verses:
    print(v)
