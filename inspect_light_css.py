import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# find body.light-mode or body.theme-light or [data-theme="light"]
matches = list(re.finditer(r'(body\.light-mode|body\.theme-light|\[data-theme=["\']light["\'])', css))
print(f"Total light mode blocks in styles.css: {len(matches)}")
for m in matches[:10]:
    idx = m.start()
    end = css.find('}', idx)
    print(css[idx:end+1])
    print('---')
