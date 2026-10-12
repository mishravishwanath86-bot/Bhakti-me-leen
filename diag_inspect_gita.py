import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('gita_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print('Gita engine total lines:', len(lines))
# print first 50 lines
for i in range(min(50, len(lines))):
    print(f'{i+1}: {lines[i]}', end='')

# print lines around openGitaChapterReader
for i, line in enumerate(lines):
    if 'openGitaChapterReader' in line:
        print(f'\n--- Found openGitaChapterReader around line {i+1} ---')
        for j in range(max(0, i-5), min(len(lines), i+60)):
            print(f'{j+1}: {lines[j]}', end='')
        break
