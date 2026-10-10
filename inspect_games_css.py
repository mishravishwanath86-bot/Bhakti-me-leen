import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\epic_games.css', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== EPIC_GAMES.CSS LENGTH ===', len(text))
print(text[:400])
