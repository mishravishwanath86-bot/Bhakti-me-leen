import re, glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['app.js', 'index.html', 'drik_app_addon.js', 'mantra_engine.js', 'sundarkand_engine.js', 'chalisa_engine.js', 'ai_bhakti_player.js']:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
    
    matches = []
    for idx, line in enumerate(lines):
        if 'reader-cosmic-content' in line or 'reader-content' in line or 'pure-reader-wrapper' in line:
            matches.append((idx + 1, line.strip()))
    
    print(f'=== {fname}: {len(matches)} matches ===')
    for lno, text in matches:
        print(f'  L{lno}: {text[:140]}')
