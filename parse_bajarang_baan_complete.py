import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/2_shri-bajarang-baan.html', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the dpLyricsDevanagariFontWrapper
start_idx = html.find('dpLyricsDevanagariFontWrapper')
end_idx = html.find('dpFontResizeWidgetWrapper', start_idx)

lyrics_block = html[start_idx:end_idx]

# Split by headings
sections = re.split(r'<h3 class="dpLyricsType\s*">(.*?)</h3>', lyrics_block)
print(f"Total sections split: {len(sections)}")

for i in range(1, len(sections), 2):
    heading = re.sub(r'<[^>]+>', '', sections[i]).strip()
    content = sections[i+1]
    
    # Extract groups and rows
    groups = re.findall(r'<p class="dpGroup">(.*?)</p>', content, re.S)
    print(f"\n=== {heading} (Groups: {len(groups)}) ===")
    for g in groups:
        rows = re.findall(r'<span class="dpRow">(.*?)</span>', g)
        if rows:
            clean_row = ' '.join([re.sub(r'<[^>]+>', '', r).strip() for r in rows if r.strip()])
            print(clean_row)
