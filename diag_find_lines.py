import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'parikrama-sankalp-home-card' in line or 'mandir-3d-modal' in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
