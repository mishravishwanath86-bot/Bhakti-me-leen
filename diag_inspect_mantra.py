import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('mantra_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print('Mantra engine total lines:', len(lines))
# print first 30 lines
for i in range(min(30, len(lines))):
    print(f'{i+1}: {lines[i]}', end='')

# print lines around readMantraItemDirect
for i, line in enumerate(lines):
    if 'readMantraItemDirect' in line:
        print(f'\n--- Found readMantraItemDirect around line {i+1} ---')
        for j in range(max(0, i-5), min(len(lines), i+80)):
            print(f'{j+1}: {lines[j]}', end='')
        break
