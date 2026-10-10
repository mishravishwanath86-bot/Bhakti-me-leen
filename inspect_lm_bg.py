import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# find body.theme-light rules with background
matches = re.findall(r'body\.theme-light[^{]*\{[^}]*background[^}]*\}', css)
print(f"Total body.theme-light rules with background: {len(matches)}")
for m in matches[:10]:
    print(m.replace('\n', ' '))
    print('---')
