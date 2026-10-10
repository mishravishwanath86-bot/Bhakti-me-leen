import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function showPage' in line:
        print(f"showPage defined at L{i+1}:")
        for j in range(i, min(len(lines), i+30)):
            print(f"  {lines[j]}", end='')
        break
