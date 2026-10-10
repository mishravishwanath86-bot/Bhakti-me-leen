import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Look at light-mode text rules
print("=== LIGHT-MODE TEXT RULES IN STYLES.CSS ===")
for line in css.splitlines():
    if ('body.theme-light' in line or 'body.light-mode' in line or '[data-theme="light"]' in line) and ('color' in line or 'text' in line):
        print(line[:120])
