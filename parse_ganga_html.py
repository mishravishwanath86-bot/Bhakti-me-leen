import re, urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/27_ganga-mata-chalisa.html', 'r', encoding='utf-8') as f:
    html = f.read()

# YouTube embeds
yt_matches = re.findall(r'youtube\.com/embed/([a-zA-Z0-9_-]+)|youtu\.be/([a-zA-Z0-9_-]+)', html)
print("YouTube embeds in HTML:", yt_matches)

# Extract paragraphs
paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
cleaned = []
for p in paras:
    cp = re.sub(r'<br\s*/?>', '\n', p)
    cp = re.sub(r'<[^>]+>', '', cp).strip()
    if cp:
        cleaned.append(cp)

print(f"\nTotal cleaned paragraphs: {len(cleaned)}")
for i, p in enumerate(cleaned):
    print(f"[{i}] {p}")
