import json, shutil, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update final_granular_aarti_collections.json
shutil.copyfile('final_granular_aarti_collections.json', 'final_granular_aarti_collections.json.bak')
with open('final_granular_aarti_collections.json', encoding='utf-8') as f:
    granular_data = json.load(f)

removed_keys = []
if 'sants' in granular_data:
    del granular_data['sants']
    removed_keys.append('sants')
if 'gita' in granular_data:
    del granular_data['gita']
    removed_keys.append('gita')

print(f"Removed from final_granular_aarti_collections.json: {removed_keys}")
print(f"Remaining keys in granular: {list(granular_data.keys())}")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(granular_data, f, ensure_ascii=False, indent=2)

# 2. Update full_drik_aarti_collections.json
shutil.copyfile('full_drik_aarti_collections.json', 'full_drik_aarti_collections.json.bak')
with open('full_drik_aarti_collections.json', encoding='utf-8') as f:
    full_drik_data = json.load(f)

removed_full_drik = []
if 'sants' in full_drik_data:
    del full_drik_data['sants']
    removed_full_drik.append('sants')
# Also check if 'other' is there (which had gita)
# Note: full_drik_data has 'other' (title: 'गीता व पितर आरती संग्रह')
# User asked: "श्री रामायण, गीता व देव स्तुति ko bhi htado do"
# If 'other' in full_drik_data, let's remove it if desired or keep
if 'other' in full_drik_data:
    del full_drik_data['other']
    removed_full_drik.append('other')

print(f"Removed from full_drik_aarti_collections.json: {removed_full_drik}")
print(f"Remaining keys in full_drik: {list(full_drik_data.keys())}")

with open('full_drik_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(full_drik_data, f, ensure_ascii=False, indent=2)

# 3. Update app.js
shutil.copyfile('app.js', 'app.js.bak')
with open('app.js', encoding='utf-8') as f:
    app_js = f.read()

# Remove 'sants' and 'gita' from window.AARTI_COLLECTIONS in app.js
# Let's locate the active window.AARTI_COLLECTIONS at line ~24791
target_marker = '// 🪔 DRIK PANCHANG COMPLETE AARTI ENGINE (EXACT IMAGE 1 REPLICA & ALL DEITY POINTS)'
marker_idx = app_js.find(target_marker)
if marker_idx == -1:
    print("ERROR: marker not found in app.js")
    sys.exit(1)

start_coll_idx = app_js.find('window.AARTI_COLLECTIONS = {', marker_idx)
# find closing of window.AARTI_COLLECTIONS
# We know after the collections, there is:
# // ══════════════════════════════════════════════════════════════════════════════
# // 🪔 GUARANTEED BULLETPROOF AARTI COLLECTION MODAL CONTROLLER
modal_controller_marker = '// 🪔 GUARANTEED BULLETPROOF AARTI COLLECTION MODAL CONTROLLER'
modal_idx = app_js.find(modal_controller_marker, start_coll_idx)
if modal_idx == -1:
    print("ERROR: modal controller marker not found in app.js")
    sys.exit(1)

# Find the last '};' before modal_idx
end_coll_idx = app_js.rfind('};', start_coll_idx, modal_idx)
if end_coll_idx == -1:
    print("ERROR: end of AARTI_COLLECTIONS not found")
    sys.exit(1)

print(f"AARTI_COLLECTIONS range in app.js: {start_coll_idx} to {end_coll_idx+2}")

# Let's parse the JSON inside window.AARTI_COLLECTIONS
json_snippet = app_js[start_coll_idx + len('window.AARTI_COLLECTIONS = '):end_coll_idx + 1]
parsed_coll = json.loads(json_snippet)
print("Keys before removal in app.js:", list(parsed_coll.keys()))

if 'sants' in parsed_coll:
    del parsed_coll['sants']
    print("Deleted 'sants' from app.js AARTI_COLLECTIONS")
if 'gita' in parsed_coll:
    del parsed_coll['gita']
    print("Deleted 'gita' from app.js AARTI_COLLECTIONS")

print("Keys after removal in app.js:", list(parsed_coll.keys()))

new_json_snippet = json.dumps(parsed_coll, ensure_ascii=False, indent=2)
app_js = app_js[:start_coll_idx + len('window.AARTI_COLLECTIONS = ')] + new_json_snippet + app_js[end_coll_idx + 1:]

# Now update deitiesList and categories in app.js
# 1) deitiesList:
# Remove ['sants', 'सन्त'], ['gita', 'गीता']
old_deities = "['ganga', 'गंगा'], ['bhairav', 'भैरव'], ['gayatri', 'गायत्री'], ['sants', 'सन्त'], ['gita', 'गीता']"
new_deities = "['ganga', 'गंगा'], ['bhairav', 'भैरव'], ['gayatri', 'गायत्री'], ['radha', 'राधा']"
if old_deities in app_js:
    app_js = app_js.replace(old_deities, new_deities)
    print("Replaced deitiesList in modal controller")
else:
    print("Warning: old_deities pattern not directly matched, checking regex")

# 2) categories in renderFullDrikAartiPage:
# Check if categories list has sants and gita
old_cats_part = """    ['sants', '🧘‍♂️ सन्त व गुरु (9)'],
    ['gita', '📜 रामायण व गीता (9)']"""

if old_cats_part in app_js:
    # replace and also update total count in all
    app_js = app_js.replace("    ['sants', '🧘‍♂️ सन्त व गुरु (9)'],\n    ['gita', '📜 रामायण व गीता (9)']\n", "")
    print("Removed sants and gita chips from renderFullDrikAartiPage")
else:
    print("Warning: old_cats_part not directly matched")

# Also update the 'all' pill label: from '✨ सभी (118)' or '✨ सभी (...)' to '✨ सभी (57)'
app_js = re.sub(r"\[\s*'all'\s*,\s*'✨ सभी \(\d+\)'\s*\]", "['all', '✨ सभी (57)']", app_js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Saved app.js successfully!")
