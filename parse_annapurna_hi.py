import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/40_annapurna-mata-chalisa.html', 'r', encoding='utf-8') as f:
    text_hi = f.read()

title_m = re.search(r'<title>(.*?)</title>', text_hi)
print('Title:', title_m.group(1) if title_m else 'None')

yt_ids = re.findall(r'(?:youtube\.com/embed/|youtu\.be/|youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})', text_hi)
print('YouTube IDs found:', set(yt_ids))

m = re.findall(r'iframe[^>]*src=["\']([^"\']+)["\']', text_hi)
print('iframe srcs:', m)

start = text_hi.find('id="dpLyricsBlockId"')
block_end = text_hi.find('class="dpLyricsVideoWrapper"', start)
if block_end == -1:
    block_end = text_hi.find('class="dpPageNavigation', start)

lyrics_html = text_hi[start:block_end]
parts = re.findall(r'(<h3[^>]*>.*?</h3>|<div class="dpLyricsChalisaGroup">.*?</div>)', lyrics_html, re.DOTALL)
print(f"Total parts: {len(parts)}")

lines = []
for p in parts:
    if '<h3' in p:
        heading = re.sub(r'<[^>]+>', '', p).strip()
        lines.append(f"\n{heading}\n")
    else:
        groups = re.findall(r'<p class="dpGroup">(.*?)</p>', p, re.DOTALL)
        for g in groups:
            rows = re.findall(r'<span class="dpRow">(.*?)</span>', g)
            line = ' '.join(r.strip() for r in rows).strip()
            if line:
                lines.append(line)

print("--- ANNAPURNA MATA CHALISA LINES ---")
for idx, l in enumerate(lines):
    print(f"{idx}: {l}")
