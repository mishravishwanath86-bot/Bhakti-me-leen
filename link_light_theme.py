import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

target = '<link rel="stylesheet" href="styles.css?v=1789846695" />'
if target in html:
    replacement = target + '\n  <link rel="stylesheet" href="light_theme.css?v=1" />'
    new_html = html.replace(target, replacement, 1)
    with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully linked light_theme.css in index.html!")
else:
    print("Target string not found in index.html")
