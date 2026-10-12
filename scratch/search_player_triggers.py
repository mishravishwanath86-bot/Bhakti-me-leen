import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['index.html', 'app.js', 'ai_bhakti_player.js', 'mantra_engine.js', 'sundarkand_engine.js', 'chalisa_engine.js', 'gita_engine.js']:
    try:
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        matches = re.findall(r'.{0,50}(?:AiBhaktiPlayer|ai-play-btn|togglePlay|ai-bhakti).{0,50}', content)
        print(f'=== {fname}: {len(matches)} matches ===')
        for m in matches[:5]:
            print('  ', m.strip().replace('\n', ' '))
    except Exception as e:
        print(f'{fname}: {e}')
