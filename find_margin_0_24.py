import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
matches = [m.start() for m in re.finditer(r'margin:\s*0\s+24px', css)]
print(f"Found {len(matches)} occurrences in styles.css:")
lines = css.split('\n')
for idx in matches:
    line_no = css[:idx].count('\n') + 1
    for j in range(max(0, line_no - 4), min(len(lines), line_no + 5)):
        print(f"L{j+1}: {lines[j]}")
    print("---")
