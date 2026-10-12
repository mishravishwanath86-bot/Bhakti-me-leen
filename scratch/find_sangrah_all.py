import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.js', '.html', '.json', '.py', '.txt')):
            fpath = os.path.join(root, f)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                    text = fp.read()
                matches = re.findall(r'.{0,30}संग्रहालय.{0,30}', text)
                if matches:
                    print(f'=== {fpath}: {len(matches)} matches ===')
                    for m in matches[:3]:
                        print('  ', m.strip().replace('\n', ' '))
            except Exception as e:
                pass
