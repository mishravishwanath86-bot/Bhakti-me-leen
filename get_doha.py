import re

with open("chalisa_cache/43_shakambhari-mata-chalisa.html", "r", encoding="utf-8") as f:
    html = f.read()

pos = html.find("शाकम्भरी माँ अति सुखकारी")
before = html[max(0, pos-2000):pos+500]

s = re.sub(r'<br\s*/?>', '\n', before)
s = re.sub(r'</(p|div|h\d)>', '\n', s)
s = re.sub(r'<[^>]+>', '', s)
lines = [l.strip() for l in s.split('\n') if l.strip()]

with open("shakambhari_doha_before.txt", "w", encoding="utf-8") as out:
    for l in lines:
        out.write(l + "\n")

print(f"Lines before: {len(lines)}")
