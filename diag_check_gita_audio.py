import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('gita_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for term in ['playVerseAudio', 'playAiGitaVerse', 'toggleGitaAudio']:
    matches = [m.start() for m in re.finditer(re.escape(term), text)]
    print(f'{term}: {len(matches)} occurrences')
    for m in matches[:3]:
        print(text[max(0, m-50):min(len(text), m+250)])
        print('---')
