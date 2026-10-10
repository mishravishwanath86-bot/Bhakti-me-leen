import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("--- Occurrences of openGlassPlayer ---")
for m in re.finditer(r'openGlassPlayer', js):
    start = max(0, m.start() - 50)
    end = min(len(js), m.end() + 100)
    print(js[start:end])
    print("-" * 40)
