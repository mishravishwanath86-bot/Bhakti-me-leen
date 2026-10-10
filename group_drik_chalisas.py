import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_collection_raw.html', encoding='utf-8') as f:
    html = f.read()

# Let's find each section and its links
# Sections in Drik:
# देवताओं की चालीसा
# देवियों की चालीसा
# सन्तों की चालीसा
# अन्य चालीसा

# Find where each section starts and ends
pattern = r'<h[23][^>]*>(.*?)</h[23]>'
matches = list(re.finditer(pattern, html, re.DOTALL))

for i, m in enumerate(matches):
    heading = re.sub(r'<[^>]+>', ' ', m.group(1)).strip()
    start_pos = m.end()
    end_pos = matches[i+1].start() if i + 1 < len(matches) else len(html)
    section_html = html[start_pos:end_pos]
    
    # find chalisa links in this section
    # On Drik panchang, items are in cards or list with hindi and english
    # Let's extract them
    links = re.findall(r'<a[^>]+href=[\'"]([^\'"]*?/chalisa/[^\'"]*lang=hi[^\'"]*)[\'"][^>]*>(.*?)</a>', section_html, re.DOTALL)
    if links:
        print(f"\n==========================================")
        print(f"SECTION: {heading} ({len(links)} Chalisas)")
        print(f"==========================================")
        for h, t in links:
            clean_title = re.sub(r'<[^>]+>', ' ', t).strip()
            print(f"  • {clean_title} -> {h}")
