import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('bhagavad_gita_chapters.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for c in d['chapters']:
    print(f"Ch {c['chapter_number']}: {c.get('name')} -> {c.get('thumb')}")
