import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://www.drikpanchang.com/lyrics/ramcharitmanas/sundarkand/sundarkand-lyrics.html', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Find all occurrences of dpPagination
for m in re.finditer(r'class="dpPagination"', html):
    print("dpPagination found at:", m.start())

# Find where the lyrics container ends
l_start = html.find('class="dpMiddleTitle"')
print("dpMiddleTitle at:", l_start)

# Next major section after lyrics
next_div = html.find('<div class="dpCardWrapper', l_start)
if next_div == -1:
    next_div = html.find('<div class="dpFooter', l_start)
print("Next section after lyrics at:", next_div)
print("Context around next section:")
print(html[next_div-200:next_div+100])
