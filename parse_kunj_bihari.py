import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('kunj_bihari_en.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('dpLyricsWrapper')
print('dpLyricsWrapper in EN at:', pos)
if pos != -1:
    print(text[pos:pos+3000])
