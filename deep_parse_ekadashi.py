import urllib.request
import re
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# The aarti content - fetching via the DrikPanchang Hindi lyrics page
# The page renders via JS, but we can look at the data embedded in the page

with open('ekadashi_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# DrikPanchang embeds lyrics data in JS or as data attributes
# Let's look for JSON data structures
json_blocks = re.findall(r'var\s+\w+\s*=\s*(\{.*?\});', html, re.DOTALL)
print(f"Found {len(json_blocks)} JSON blocks")

# Also look for specific patterns
# Look for any structured data
json_ld = re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(json_ld)} JSON-LD blocks")
for jl in json_ld:
    print("JSON-LD:", jl[:500])
    print("---")

# Look for lyrics data in any form
lyrics_raw = re.findall(r'"lyrics[^"]*":\s*"([^"]{20,})"', html)
print(f"\nLyrics fields: {len(lyrics_raw)}")
for lr in lyrics_raw[:5]:
    print(repr(lr[:200]))

# Look for lyricsText or lyricData  
lt = re.findall(r'lyricsText|lyricData|dpLyric|lyricsData', html)
print(f"\nLyrics-related terms found: {lt}")

# Try to find the lyrics section by looking for stanza patterns
# The aarti has repeated lines like "भक्तजनों के संकट"
bh = html.find('\u092d\u0915\u094d\u0924\u091c\u0928\u094b\u0902')  # भक्तजनों
print(f"\nभक्तजनों at: {bh}")

om = html.find('\u0913\u092e\u094d \u091c\u092f \u090f\u0915\u093e\u0926\u0936\u0940')  # ॐ जय एकादशी  
print(f"ॐ जय एकादशी at: {om}")

# Show raw HTML around that area  
if om > 0:
    print("\nContext:")
    print(html[max(0,om-300):om+500])
