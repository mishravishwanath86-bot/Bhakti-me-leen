import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("Length of app.js:", len(js))

# Search for Katha rendering and playlist definitions
matches = re.findall(r'(function\s+(?:initKatha|renderKatha|playKatha|openKatha)[^{]*\{[\s\S]*?\n\})', js)
print("Found katha functions:", len(matches))
for m in matches:
    print("\n----------------------")
    print(m[:250] + "...")

# Check FULL_KATHA_PLAYLIST or KATHA_LIST
for name in ['FULL_KATHA_PLAYLIST', 'KATHA_PLAYLIST', 'KATHA_LIST', 'KATHAS']:
    if name in js:
        pos = js.find(name)
        print(f"\nFound {name} at position {pos}:")
        print(js[pos:pos+350])
