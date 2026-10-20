import os
import sys
import json
import re
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = r"C:\Users\vishw\OneDrive\Videos\Bhagavad Gita"
JSON_PATH = os.path.join(BASE_DIR, "bhagavad_gita_chapters.json")
GITA_ENGINE_PATH = os.path.join(BASE_DIR, "gita_engine.js")
GALLERY_ENGINE_PATH = os.path.join(BASE_DIR, "gallery_engine.js")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

print("--- Step 1: Loading bhagavad_gita_chapters.json ---")
with open(JSON_PATH, "r", encoding="utf-8") as f:
    gita_data = json.load(f)

chapters = gita_data.get("chapters", [])
print(f"Total chapters loaded: {len(chapters)}")

print("\n--- Step 2: Processing and Resizing 18 Chapter Images ---")
processed_files = []

for ch in chapters:
    ch_num = ch["chapter_number"]
    src_filename = f"Bhagavad Gita Chapter {ch_num}.png"
    src_file = os.path.join(SRC_DIR, src_filename)
    
    if not os.path.exists(src_file):
        print(f"ERROR: Source file not found: {src_file}")
        continue
    
    # Destination from thumb path in json
    rel_thumb = ch.get("thumb", f"assets/gallery/gita_ch{ch_num}.jpg")
    dest_path = os.path.join(BASE_DIR, rel_thumb.replace("/", os.sep))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Also create standard alias path
    alias_rel = f"assets/gallery/gita_ch_{ch_num}.jpg"
    alias_path = os.path.join(BASE_DIR, alias_rel.replace("/", os.sep))

    # Read and resize
    orig_size_mb = os.path.getsize(src_file) / (1024 * 1024)
    with Image.open(src_file) as im:
        # Convert transparent/RGBA to RGB
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            bg = Image.new('RGB', im.size, (255, 255, 255))
            if im.mode != 'RGBA':
                im = im.convert('RGBA')
            bg.paste(im, mask=im.split()[3])
            im = bg
        else:
            im = im.convert('RGB')
        
        # High quality resize to 1024x1024
        im_resized = im.resize((1024, 1024), Image.Resampling.LANCZOS)
        
        # Save to primary destination
        im_resized.save(dest_path, "JPEG", quality=92, optimize=True)
        # Save alias
        im_resized.save(alias_path, "JPEG", quality=92, optimize=True)
    
    new_size_kb = os.path.getsize(dest_path) / 1024
    print(f"✓ Ch {ch_num:2d} ({ch['name']}): {orig_size_mb:.2f}MB -> {new_size_kb:.1f}KB saved to {rel_thumb}")
    processed_files.append((ch_num, rel_thumb))

# Save back json
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(gita_data, f, ensure_ascii=False, indent=2)
print("✓ bhagavad_gita_chapters.json successfully verified & saved.")

print("\n--- Step 3: Updating window.GITA_DATA in gita_engine.js ---")
with open(GITA_ENGINE_PATH, "r", encoding="utf-8") as f:
    gita_engine_lines = f.readlines()

# Line 6 is window.GITA_DATA = ...
compact_gita_json = json.dumps(gita_data, ensure_ascii=False)
for idx, line in enumerate(gita_engine_lines):
    if line.strip().startswith("window.GITA_DATA ="):
        gita_engine_lines[idx] = f"window.GITA_DATA = {compact_gita_json};\n"
        print(f"✓ Replaced window.GITA_DATA on line {idx + 1}")
        break

with open(GITA_ENGINE_PATH, "w", encoding="utf-8") as f:
    f.writelines(gita_engine_lines)
print("✓ gita_engine.js updated successfully.")

print("\n--- Step 4: Building window.GITA_GALLERY and Updating gallery_engine.js ---")
gita_gallery_items = []
for ch in chapters:
    ch_num = ch["chapter_number"]
    first_shloka = ""
    if ch.get("key_shlokas") and len(ch["key_shlokas"]) > 0:
        raw_sk = ch["key_shlokas"][0].get("sanskrit", "")
        # Single line clean
        first_shloka = " ".join(raw_sk.split())
        v_num = ch["key_shlokas"][0].get("verse_num", "")
        if v_num:
            first_shloka += f" ({v_num})"

    summary_short = ch.get("summary", "")
    if len(summary_short) > 220:
        summary_short = summary_short[:217] + "..."

    item = {
        "id": f"gita_ch_{ch_num}",
        "nameHi": f"अध्याय {ch_num}: {ch['name']}",
        "nameEn": f"Chapter {ch_num}: {ch.get('name_english', '')}",
        "category": "श्रीमद्भगवद्गीता",
        "img": ch.get("thumb", f"assets/gallery/gita_ch_{ch_num}.jpg"),
        "fallbackImg": "assets/gallery/bal_krishna.jpg",
        "desc": summary_short or ch.get("life_lesson", ""),
        "mantra": first_shloka,
        "famous": f"श्रीमद्भगवद्गीता • {ch['verses_count']} श्लोक • {ch['yoga_group']}"
    }
    gita_gallery_items.append(item)

print(f"Built {len(gita_gallery_items)} Gita gallery items.")

with open(GALLERY_ENGINE_PATH, "r", encoding="utf-8") as f:
    gallery_code = f.read()

# Add window.GITA_GALLERY definition
gita_gallery_json = json.dumps(gita_gallery_items, ensure_ascii=False, indent=2)
gita_gallery_js_block = f"\n  window.GITA_GALLERY = {gita_gallery_json};\n"

# Check if window.GITA_GALLERY is already present
if "window.GITA_GALLERY =" in gallery_code:
    gallery_code = re.sub(
        r'window\.GITA_GALLERY\s*=\s*\[[\s\S]*?\];',
        f'window.GITA_GALLERY = {gita_gallery_json};',
        gallery_code,
        count=1
    )
    print("✓ Updated existing window.GITA_GALLERY in gallery_engine.js")
else:
    # Insert right before getActiveDataset
    target = "function getActiveDataset()"
    if target in gallery_code:
        gallery_code = gallery_code.replace(target, gita_gallery_js_block + "\n  " + target, 1)
        print("✓ Inserted window.GITA_GALLERY before getActiveDataset()")
    else:
        # Or at top after opening IIFE
        gallery_code = gallery_code.replace("(function() {\n", "(function() {\n" + gita_gallery_js_block, 1)
        print("✓ Inserted window.GITA_GALLERY at beginning of gallery_engine.js")

# Update getActiveDataset() to include gita
if "window.galleryActiveTab === 'gita'" not in gallery_code:
    old_get_dataset = "function getActiveDataset() {"
    new_get_dataset = """function getActiveDataset() {
    if (window.galleryActiveTab === 'gita') {
      return (window.GITA_GALLERY && window.GITA_GALLERY.length) ? window.GITA_GALLERY : [];
    } else"""
    gallery_code = gallery_code.replace(old_get_dataset, new_get_dataset, 1)
    print("✓ Added 'gita' tab handling in getActiveDataset()")

# Update badgeText in gallery_engine.js
if "window.galleryActiveTab === 'gita'" not in gallery_code:
    gallery_code = gallery_code.replace(
        "window.galleryActiveTab === 'bal' ? '👶 बाल स्वरूप' :",
        "window.galleryActiveTab === 'bal' ? '👶 बाल स्वरूप' : (window.galleryActiveTab === 'gita' ? '📖 भगवद्गीता' : (window.galleryActiveTab === 'mahakavya' ? '🏹 महाकाव्य' :",
        1
    )
    print("✓ Updated badgeText in gallery_engine.js for gita & mahakavya")

# Add Gita deity synonyms
if "'gita':" not in gallery_code:
    target_syn = "const DEITY_SYNONYMS = {"
    if target_syn in gallery_code:
        gita_syn = """const DEITY_SYNONYMS = {
    'gita': ['gita', 'geeta', 'भगवद्गीता', 'गीता', 'shloka', 'श्लोक', 'upadesh', 'उपदेश', 'arjuna', 'krishna', 'कुरुक्षेत्र', 'अध्याय'],"""
        gallery_code = gallery_code.replace(target_syn, gita_syn, 1)
        print("✓ Added 'gita' synonyms to DEITY_SYNONYMS")

with open(GALLERY_ENGINE_PATH, "w", encoding="utf-8") as f:
    f.write(gallery_code)
print("✓ gallery_engine.js updated successfully.")

print("\n--- Step 5: Updating index.html Gallery Tabs ---")
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_html = f.read()

# Check gal-tabs-bar in index.html
tabs_bar_target = '<div class="gal-tabs-bar">'
if tabs_bar_target in index_html:
    # See if gita tab already in index.html
    if 'data-tab="gita"' not in index_html:
        # Replace the tabs bar content
        old_tabs_block = re.search(r'<div class="gal-tabs-bar">[\s\S]*?</div>', index_html)
        if old_tabs_block:
            new_tabs_html = """<div class="gal-tabs-bar">
        <button class="gal-tab-pill active" data-tab="bal" onclick="switchGalleryTab('bal')">
          👶 बाल रूप (60)
        </button>
        <button class="gal-tab-pill" data-tab="divya" onclick="switchGalleryTab('divya')">
          🕉️ दिव्य रूप (60)
        </button>
        <button class="gal-tab-pill" data-tab="gita" onclick="switchGalleryTab('gita')">
          📖 भगवद्गीता (18)
        </button>
        <button class="gal-tab-pill" data-tab="mahakavya" onclick="switchGalleryTab('mahakavya')">
          🏹 महाकाव्य पात्र (100)
        </button>
        <button class="gal-tab-pill" data-tab="india" onclick="switchGalleryTab('india')">
          🇮🇳 भारत के प्रमुख मंदिर (69)
        </button>
        <button class="gal-tab-pill" data-tab="world" onclick="switchGalleryTab('world')">
          🌍 विश्व के प्रमुख मंदिर (32)
        </button>
      </div>"""
            index_html = index_html[:old_tabs_block.start()] + new_tabs_html + index_html[old_tabs_block.end():]
            with open(INDEX_PATH, "w", encoding="utf-8") as f:
                f.write(index_html)
            print("✓ Added '📖 भगवद्गीता (18)' and '🏹 महाकाव्य पात्र (100)' to gal-tabs-bar in index.html")
        else:
            print("WARNING: Could not find exact gal-tabs-bar match in index.html")
    else:
        print("✓ 'gita' tab already present in index.html")

print("\n=== All Steps Completed Successfully! ===")
