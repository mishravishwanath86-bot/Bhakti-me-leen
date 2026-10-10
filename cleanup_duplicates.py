import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Initial length:", len(html))

# 1. Deduplicate home_gita_section
home_marker = '<!-- 📖 BHAGAVAD GITA 18 CHAPTERS COLLECTION (श्रीमद्भगवद्गीता सम्पूर्ण १८ अध्याय — BHAGAVADGITA.COM VERIFIED) 📖 -->'
c_home = html.count(home_marker)
print(f"Count of home_marker: {c_home}")
if c_home > 1:
    # remove the second occurrence
    first_idx = html.find(home_marker)
    second_idx = html.find(home_marker, first_idx + len(home_marker))
    # Find the end of this duplicate block (right before <!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->)
    banner_marker = '<!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->'
    banner_idx = html.find(banner_marker, second_idx)
    html = html[:second_idx] + html[banner_idx:]
    print("Deduplicated home_marker.")

# 2. Deduplicate page-gita
page_marker = '<!-- ══════════ BHAGAVAD GITA 18 CHAPTERS PAGE ══════════ -->'
c_page = html.count(page_marker)
print(f"Count of page_marker: {c_page}")
if c_page > 1:
    first_idx = html.find(page_marker)
    second_idx = html.find(page_marker, first_idx + len(page_marker))
    desh_marker = '<!-- ══════════ DESH BHAKTI ══════════ -->'
    desh_idx = html.find(desh_marker, second_idx)
    html = html[:second_idx] + html[desh_idx:]
    print("Deduplicated page_marker.")

# 3. Deduplicate modals
modal_marker = '<!-- 📖 BHAGAVAD GITA CHAPTER OPTIONS MODAL 📖 -->'
c_modal = html.count(modal_marker)
print(f"Count of modal_marker: {c_modal}")
if c_modal > 1:
    first_idx = html.find(modal_marker)
    second_idx = html.find(modal_marker, first_idx + len(modal_marker))
    jaap_marker = '<!-- 📿 VIRTUAL 108 JAAP MALA FULL MODAL 📿 -->'
    jaap_idx = html.find(jaap_marker, second_idx)
    html = html[:second_idx] + html[jaap_idx:]
    print("Deduplicated modal_marker.")

# 4. Deduplicate script tags
script_str = '<script src="gita_engine.js?v=1790000000"></script>'
c_script = html.count(script_str)
print(f"Count of script_str: {c_script}")
if c_script > 1:
    html = html.replace(script_str + '\n  ' + script_str, script_str)
    print("Deduplicated script_str.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Final length:", len(html))
print("home_marker count now:", html.count(home_marker))
print("page_marker count now:", html.count(page_marker))
print("modal_marker count now:", html.count(modal_marker))
print("script_str count now:", html.count(script_str))
