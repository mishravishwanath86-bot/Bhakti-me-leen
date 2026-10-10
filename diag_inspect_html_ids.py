import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Length of index.html:", len(html))

# Search for all id attributes in index.html related to audio, player, katha, reader
ids = re.findall(r'id=["\']([^"\']*(?:audio|player|katha|modal|reader|youtube|media)[^"\']*)["\']', html, re.I)
print("\nUnique matching IDs in index.html:")
for i in sorted(set(ids)):
    print(f"  - {i}")

# Check audio elements in HTML
audio_tags = re.findall(r'<audio[\s\S]*?>', html, re.I)
print(f"\nAudio tags in index.html ({len(audio_tags)}):", audio_tags)

# Check iframe tags in HTML
iframe_tags = re.findall(r'<iframe[\s\S]*?>', html, re.I)
print(f"\nIFrame tags in index.html ({len(iframe_tags)}):")
for ifr in iframe_tags:
    print(f"  - {ifr[:120]}...")
