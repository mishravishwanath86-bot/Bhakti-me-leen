import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('gita_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'window.playVerseAudio' in l:
        for j in range(max(0, i-5), min(len(lines), i+60)):
            print(f'{j+1}: {lines[j]}', end='')
        break
