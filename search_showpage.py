import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'showPage' in line and ('function' in line or '=' in line):
        print(f"L{i+1}: {line.strip()[:100]}")
