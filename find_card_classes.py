import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

card_classes = set(re.findall(r'\.([a-zA-Z0-9_\-]*card[a-zA-Z0-9_\-]*)', css))
print("Found card classes:", sorted(list(card_classes)))
