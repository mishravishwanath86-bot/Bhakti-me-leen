import shutil
import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# The 5 uploaded files in chronological order
uploaded = [
    (1, r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\.user_uploaded\media_1790485584570.jpg", "assets/gallery/gita_ch1_arjuna_vishada.jpg", "अध्याय १: अर्जुनविषादयोग"),
    (2, r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\.user_uploaded\media_1790485592785.jpg", "assets/gallery/gita_ch2_sankhya_yoga.jpg", "अध्याय २: सांख्ययोग"),
    (3, r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\.user_uploaded\media_1790485599543.jpg", "assets/gallery/gita_ch3_karma_yoga.jpg", "अध्याय ३: कर्मयोग"),
    (4, r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\.user_uploaded\media_1790485605667.jpg", "assets/gallery/gita_ch4_jnana_karma_sanyasa.jpg", "अध्याय ४: ज्ञानकर्मसंन्यासयोग"),
    (5, r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\.user_uploaded\media_1790485625063.jpg", "assets/gallery/gita_ch5_karma_sanyasa_yoga.jpg", "अध्याय ५: कर्मसंन्यासयोग")
]

# 1. Copy to assets/gallery/
os.makedirs("assets/gallery", exist_ok=True)
for ch_num, src, dest, name in uploaded:
    shutil.copy2(src, dest)
    print(f"✓ Copied image for Chapter {ch_num} ({name}) -> {dest} ({os.path.getsize(dest)} bytes)")

# 2. Update bhagavad_gita_chapters.json
with open('bhagavad_gita_chapters.json', 'r', encoding='utf-8') as f:
    gita_json = json.load(f)

for ch_num, src, dest, name in uploaded:
    chap = next((c for c in gita_json['chapters'] if c['chapter_number'] == ch_num), None)
    if chap:
        chap['thumb'] = dest
        print(f"✓ Updated bhagavad_gita_chapters.json thumb for Chapter {ch_num}")

with open('bhagavad_gita_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(gita_json, f, ensure_ascii=False, indent=2)

# 3. Update index.html home-gita-chapters-grid
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace images in home-gita-card data-chap="1" through "5"
for ch_num, src, dest, name in uploaded:
    # Pattern matching the preview card for that chapter
    pattern = rf'(<div class="aarti-preview-card home-gita-card" data-chap="{ch_num}"[^>]*>.*?<img src=")[^"]*(")'
    new_html = re.sub(pattern, rf'\g<1>{dest}\g<2>', html, flags=re.DOTALL)
    if new_html != html:
        html = new_html
        print(f"✓ Updated index.html preview card for Chapter {ch_num}")
    else:
        print(f"✗ Failed to find preview card for Chapter {ch_num} in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone copying and updating JSON & index.html!")
