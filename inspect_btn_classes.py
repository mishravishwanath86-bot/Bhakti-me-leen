import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\epic_games.css', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'btn-', text)]
for idx in matches[:5]:
    print(text[idx-20:idx+150])
    print('-'*40)
