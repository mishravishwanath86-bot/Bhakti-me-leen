import re, sys

sys.stdout.reconfigure(encoding='utf-8')

content = open('chalisa_cache/17_shri-parashurama-chalisa.html', encoding='utf-8').read()

# YouTube Video ID
vids = re.findall(r'youtube\.com/embed/([a-zA-Z0-9_-]+)', content)
print("Video IDs found:", vids)

# dpYoutubeVideoId
m_dp = re.search(r'id=\"dpYoutubeVideoId\"\s+src=\"https://www.youtube.com/embed/([a-zA-Z0-9_-]+)', content)
print("dpYoutubeVideoId:", m_dp.group(1) if m_dp else "Not found")

# Lyrics wrapper
idx = content.find('dpLyricsWrapper')
end_idx = content.find('</article>', idx)
article = content[idx:end_idx]

clean = re.sub(r'<[^>]+>', '\n', article)
lines = [l.strip() for l in clean.splitlines() if l.strip()]

print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines):
    print(f"{i}: {l}")
