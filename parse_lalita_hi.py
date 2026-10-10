import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/29_lalita-mata-chalisa.html', 'r', encoding='utf-8') as f:
    text = f.read()

title_m = re.search(r'<title>(.*?)</title>', text)
print('Title:', title_m.group(1) if title_m else 'None')

# Check YouTube IDs
yt_ids = re.findall(r'(?:youtube\.com/embed/|youtu\.be/|youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})', text)
print('YouTube IDs found in page:', set(yt_ids))

start = text.find('id="dpLyricsBlockId"')
block_end = text.find('class="dpLyricsVideoWrapper"', start)
if block_end == -1:
    block_end = text.find('class="dpPageNavigation', start)

lyrics_html = text[start:block_end]

parts = re.findall(r'(<h3[^>]*>.*?</h3>|<div class="dpLyricsChalisaGroup">.*?</div>)', lyrics_html, re.DOTALL)
print(f"Total parts in Hindi lyrics: {len(parts)}")

all_verses_hi = []
for p in parts:
    if '<h3' in p:
        heading = re.sub(r'<[^>]+>', '', p).strip()
        all_verses_hi.append(f"\n{heading}\n")
    else:
        groups = re.findall(r'<p class="dpGroup">(.*?)</p>', p, re.DOTALL)
        for g in groups:
            rows = re.findall(r'<span class="dpRow">(.*?)</span>', g)
            line = ' '.join(r.strip() for r in rows).strip()
            if line:
                all_verses_hi.append(line)

print("\n--- HINDI LYRICS ---")
for v in all_verses_hi:
    print(v)
