import re, sys
sys.stdout.reconfigure(encoding='utf-8')

cache_path = r'C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/chalisa_cache/24_gayatri-mata-chalisa.html'
with open(cache_path, 'r', encoding='utf-8') as f:
    html = f.read()

divs = re.findall(r'<div class="dpLyrics[^"]*">(.*?)</div>', html, re.DOTALL)
print(f"Total divs: {len(divs)}")

for i, d in enumerate(divs):
    t = re.sub(r'<br\s*/?>', '\n', d)
    t = re.sub(r'<[^>]+>', '', t).strip()
    print(f"=== DIV {i} ===")
    print(t)
