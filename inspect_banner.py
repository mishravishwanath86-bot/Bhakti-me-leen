import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('home-epic-games-banner')
print('=== BANNER SNIPPET ===')
print(text[idx-50:idx+900])
