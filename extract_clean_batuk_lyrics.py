import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/chalisa_cache/13_shri-batuka-bhairava-chalisa.html', 'r', encoding='utf-8') as f:
    html = f.read()

divs = re.findall(r'<div class="dpLyrics[^"]*">(.*?)</div>', html, re.DOTALL)
print(f"Total divs: {len(divs)}")

clean_lines = []
for i, d in enumerate(divs):
    # clean HTML tags
    # replace <br/>, <br> with newline
    t = re.sub(r'<br\s*/?>', '\n', d)
    t = re.sub(r'<[^>]+>', '', t).strip()
    clean_lines.append((i, t))
    print(f"[{i}] {t}\n")
