import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_collection_raw.html', encoding='utf-8') as f:
    html = f.read()

# Let's find headings and links
print("Title:", re.findall(r'<title>(.*?)</title>', html, re.I))

# Find sections or cards
# Look for links containing /chalisa/
links = re.findall(r'<a[^>]+href=[\'"]([^\'"]*?/chalisa/[^\'"]*)[\'"][^>]*>(.*?)</a>', html, re.DOTALL)
print(f"Total /chalisa/ links: {len(links)}")

# Clean up links and text
unique_chalisas = []
seen = set()

for href, text in links:
    clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
    clean_text = re.sub(r'\s+', ' ', clean_text)
    # ignore collection link itself
    if 'chalisa-collection' in href or not clean_text:
        continue
    if href not in seen:
        seen.add(href)
        unique_chalisas.append((href, clean_text))

print(f"Unique Chalisas found: {len(unique_chalisas)}")
for idx, (h, t) in enumerate(unique_chalisas):
    print(f"{idx+1}. {t} -> {h}")
