import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for ch in [1, 2, 3, 4, 5]:
    fn_en = f"chapter_{ch}_en.html"
    fn_hi = f"chapter_{ch}_hi.html"
    
    with open(fn_en, 'r', encoding='utf-8') as f:
        html_en = f.read()
    with open(fn_hi, 'r', encoding='utf-8') as f:
        html_hi = f.read()
        
    # Extract title, desc
    title_match = re.search(r'<title>(.*?)</title>', html_hi)
    desc_match = re.search(r'<meta name="description" content="(.*?)"', html_hi)
    
    # Extract verses from HI
    verses_hi = re.findall(r'<div id="verse-([^"]+)".*?href="(/chapter/[^"]+)".*?<p class="[^"]*">(.*?)</p>', html_hi, re.DOTALL)
    # Extract verses from EN
    verses_en = re.findall(r'<div id="verse-([^"]+)".*?href="(/chapter/[^"]+)".*?<p class="[^"]*">(.*?)</p>', html_en, re.DOTALL)
    
    en_dict = {v[0]: re.sub(r'<[^>]+>', '', v[2]).strip() for v in verses_en}
    
    print(f"=== Chapter {ch}: {title_match.group(1) if title_match else ''} ===")
    print(f"  Description: {desc_match.group(1)[:120] if desc_match else ''}...")
    print(f"  HI verses count: {len(verses_hi)} | EN verses count: {len(verses_en)}")
    
    sample_v = verses_hi[0]
    clean_hi = re.sub(r'<[^>]+>', '', sample_v[2]).strip()
    clean_en = en_dict.get(sample_v[0], '')
    print(f"  Sample Verse {sample_v[0]}:")
    print(f"    HI: {clean_hi[:100]}...")
    print(f"    EN: {clean_en[:100]}...")
