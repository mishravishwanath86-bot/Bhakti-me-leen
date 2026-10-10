import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/5_shani-dev-chalisa.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's extract all <p>...</p> tags
paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
print(f"Total <p> tags: {len(paras)}")

cleaned = []
for i, p in enumerate(paras):
    txt = re.sub(r'<br\s*/?>', '\n', p)
    txt = re.sub(r'<[^>]+>', '', txt).strip()
    if txt:
        cleaned.append(txt)

print(f"Total non-empty cleaned paragraphs: {len(cleaned)}")
for i, p in enumerate(cleaned):
    print(f"--- [{i}] ---")
    print(p)
