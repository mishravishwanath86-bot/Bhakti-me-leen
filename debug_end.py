import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://www.drikpanchang.com/lyrics/ramcharitmanas/sundarkand/sundarkand-lyrics.html', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Find where dpPagination begins
pidx = html.find('class="dpPagination"')
print("dpPagination at:", pidx)
print("Context before dpPagination:")
print(html[pidx-400:pidx])
