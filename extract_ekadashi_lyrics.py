import re
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('ekadashi_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the aarti section - it's around "एकादशी माता की आरती"
marker = '\u090f\u0915\u093e\u0926\u0936\u0940 \u092e\u093e\u0924\u093e \u0915\u0940 \u0906\u0930\u0924\u0940'  # एकादशी माता की आरती
idx = html.find(marker)
print(f"Marker found at: {idx}")

if idx > 0:
    # Extract a large chunk around the aarti
    chunk = html[max(0, idx-100):idx+20000]
    
    # Find where the aarti content ends (look for common end markers)
    end_markers = ['dpContentComments', 'dpAdsWidget', 'dpFooter', 'dpSubscription']
    end_pos = len(chunk)
    for em in end_markers:
        ep = chunk.find(em)
        if ep > 0 and ep < end_pos:
            end_pos = ep
    
    aarti_html = chunk[:end_pos]
    
    # Extract text by removing HTML tags
    # First, replace <br> and </p> with newlines
    aarti_html = re.sub(r'<br\s*/?>', '\n', aarti_html, flags=re.IGNORECASE)
    aarti_html = re.sub(r'</p>', '\n', aarti_html, flags=re.IGNORECASE)
    aarti_html = re.sub(r'</div>', '\n', aarti_html, flags=re.IGNORECASE)
    aarti_html = re.sub(r'</span>', '', aarti_html, flags=re.IGNORECASE)
    
    # Remove all remaining tags
    aarti_text = re.sub(r'<[^>]+>', '', aarti_html)
    
    # Decode HTML entities
    aarti_text = aarti_text.replace('&nbsp;', ' ')
    aarti_text = aarti_text.replace('&amp;', '&')
    aarti_text = aarti_text.replace('&#x2715;', '×')
    aarti_text = re.sub(r'&#\d+;', '', aarti_text)
    aarti_text = re.sub(r'&[a-z]+;', '', aarti_text)
    
    # Clean up whitespace
    lines = []
    for line in aarti_text.split('\n'):
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
    
    # Print the extracted lyrics
    print(f"\nExtracted {len(lines)} non-empty lines:")
    for i, l in enumerate(lines[:100]):
        print(f"{i+1:3}. {l}")
