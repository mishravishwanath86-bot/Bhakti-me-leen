import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Length of index.html:", len(html))

matches = list(re.finditer(r'(?:mandir|parikrama|temple|3d|दर्शन)', html, re.IGNORECASE))
print(f"Total matching keywords: {len(matches)}")

for m in matches[:15]:
    start = max(0, m.start() - 40)
    end = min(len(html), m.end() + 80)
    print(f"[{m.start()}]: {html[start:end]}")
    print("-" * 30)
