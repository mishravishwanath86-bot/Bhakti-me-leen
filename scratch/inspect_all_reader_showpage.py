import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

target_lines = [7822, 18958, 19938, 21578, 21666, 28635, 30018]

for ln in target_lines:
    print(f'================ Line {ln} ================')
    start = max(0, ln - 25)
    end = min(len(lines), ln + 15)
    for i in range(start, end):
        prefix = '>>> ' if i+1 == ln else '    '
        print(f'{prefix}{i+1}: {lines[i].rstrip()[:110]}')
    print()
