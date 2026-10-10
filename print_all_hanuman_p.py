import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/1_shree-hanuman-chalisa.html', encoding='utf-8') as f:
    html = f.read()

p_tags = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
for i in range(len(p_tags)):
    clean = re.sub(r'<[^>]+>', ' ', p_tags[i]).strip()
    clean = re.sub(r'\s+', ' ', clean)
    if clean:
        print(f"P {i}: {clean}")
