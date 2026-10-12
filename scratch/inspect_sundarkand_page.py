import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html = open('index.html', encoding='utf-8').read()
m = list(re.finditer(r'id=["\']page-sundarkand["\']', html))
print('matches in index.html:', len(m))
for x in m:
    print(html[x.start():x.start()+600])
    print('---')

with open('sundarkand_engine.js', encoding='utf-8') as f:
    sk_code = f.read()

print('render functions in sundarkand_engine.js:')
for line in sk_code.split('\n'):
    if 'function render' in line or 'renderFull' in line or 'init' in line or 'showSundarkand' in line:
        print(' ', line.strip())
