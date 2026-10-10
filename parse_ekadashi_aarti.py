import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read the saved HTML
with open('ekadashi_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML length:", len(html))

# Try multiple patterns for lyrics
m1 = re.search(r'dpLyricsText', html)
print("dpLyricsText found:", m1 is not None)

# Search for jai ekadashi
search_term = '\u091c\u092f \u090f\u0915\u093e\u0926\u0936\u0940'  # जय एकादशी
idx = html.find(search_term)
print(f"Search term index: {idx}")
if idx > 0:
    snippet = html[max(0, idx-500):idx+5000]
    # Remove HTML tags from snippet
    clean = re.sub(r'<[^>]+>', '', snippet)
    clean = re.sub(r'&nbsp;', ' ', clean)
    clean = re.sub(r'&[a-z]+;', '', clean)
    clean = re.sub(r'\s+', '\n', clean).strip()
    print("Cleaned lyrics:")
    print(clean[:3000])
else:
    # Show the full HTML structure to understand
    # Find any div/section with lyrics
    classes = re.findall(r'class="([^"]*)"', html)
    unique_classes = list(set(classes))
    print("All classes found:")
    for c in sorted(unique_classes):
        if 'lyric' in c.lower() or 'text' in c.lower() or 'content' in c.lower() or 'verse' in c.lower():
            print(" -", c)
