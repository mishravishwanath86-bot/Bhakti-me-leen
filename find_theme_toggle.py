import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'<button[^>]*theme[^>]*>', html, re.IGNORECASE)
print("Theme buttons in HTML:", matches)

matches2 = re.findall(r'function toggle[a-zA-Z0-9_]*Theme[a-zA-Z0-9_]*\([^)]*\)', html)
print("Theme functions in HTML:", matches2)
