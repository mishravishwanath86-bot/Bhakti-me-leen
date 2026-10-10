import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

matches = re.findall(r'(\.[a-zA-Z0-9_\-]*light[a-zA-Z0-9_\-]*)', css)
print("Matches for light:", set(matches))
matches2 = re.findall(r'(\.[a-zA-Z0-9_\-]*theme[a-zA-Z0-9_\-]*)', css)
print("Matches for theme:", set(matches2))
