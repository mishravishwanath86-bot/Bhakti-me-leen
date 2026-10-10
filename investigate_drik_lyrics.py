import re
import json
import sys
import io
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('ekadashi_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all dpLyric related patterns
lyric_contexts = []
for m in re.finditer(r'dpLyric\w*', html):
    start = max(0, m.start()-100)
    end = min(len(html), m.end()+200)
    ctx = html[start:end]
    if ctx not in lyric_contexts:
        lyric_contexts.append(ctx)

print(f"Found {len(lyric_contexts)} unique dpLyric contexts")
for i, ctx in enumerate(lyric_contexts[:5]):
    print(f"\n--- Context {i+1} ---")
    # Remove tags
    clean = re.sub(r'<[^>]+>', ' ', ctx)
    clean = re.sub(r'\s+', ' ', clean).strip()
    print(repr(clean[:300]))

# Look for script src that loads lyrics
script_srcs = re.findall(r'<script[^>]+src="([^"]*lyric[^"]*)"', html, re.IGNORECASE)
print(f"\nLyrics-related scripts: {script_srcs}")

# Look for data- attributes
data_attrs = re.findall(r'data-\w+="([^"]{5,})"', html)
print(f"\nData attributes ({len(data_attrs)}):")
for da in data_attrs[:20]:
    print(f"  {da}")

# Find ajax/api calls
ajax_calls = re.findall(r'ajax[^;]{0,200}', html, re.IGNORECASE)
print(f"\nAJAX calls found: {len(ajax_calls)}")
for a in ajax_calls[:5]:
    print(" ", a[:200])
