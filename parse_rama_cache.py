import re, sys

sys.stdout.reconfigure(encoding='utf-8')

content = open('chalisa_cache/9_shree-rama-chalisa.html', encoding='utf-8').read()

# YouTube Video ID
m_vid = re.search(r'embed/([a-zA-Z0-9_-]+)', content)
print("Video ID:", m_vid.group(1) if m_vid else "Not found")

# Lyrics wrapper
idx = content.find('dpLyricsWrapper')
end_idx = content.find('</article>', idx)
article = content[idx:end_idx]

clean = re.sub(r'<[^>]+>', '\n', article)
lines = [l.strip() for l in clean.splitlines() if l.strip()]

print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines):
    print(f"{i}: {l}")
