import json, shutil, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Backup app.js
shutil.copyfile('app.js', 'app.js.bak')

with open('app.js', encoding='utf-8') as f:
    lines = f.readlines()

start_line = 24790
end_line = 26814

code_block = "".join(lines[start_line:end_line])
json_text = code_block.replace("window.AARTI_COLLECTIONS = ", "", 1).rstrip()
if json_text.endswith(';'):
    json_text = json_text[:-1]

parsed = json.loads(json_text)
print("Before removal keys:", list(parsed.keys()))

if 'sants' in parsed:
    del parsed['sants']
    print("Deleted 'sants'")
if 'gita' in parsed:
    del parsed['gita']
    print("Deleted 'gita'")

print("After removal keys:", list(parsed.keys()))

new_json_str = json.dumps(parsed, ensure_ascii=False, indent=2)
new_coll_block = "window.AARTI_COLLECTIONS = " + new_json_str + ";\n"

# Reassemble lines
new_lines = lines[:start_line] + [new_coll_block] + lines[end_line:]
full_content = "".join(new_lines)

# 1. Update deitiesList
old_deities = "['ganga', 'गंगा'], ['bhairav', 'भैरव'], ['gayatri', 'गायत्री'], ['sants', 'सन्त'], ['gita', 'गीता']"
new_deities = "['ganga', 'गंगा'], ['bhairav', 'भैरव'], ['gayatri', 'गायत्री'], ['radha', 'राधा']"
if old_deities in full_content:
    full_content = full_content.replace(old_deities, new_deities)
    print("Replaced deitiesList successfully!")
else:
    print("Warning: old_deities not found!")

# 2. Update renderFullDrikAartiPage categories
old_sants_cat = "    ['sants', '🧘‍♂️ सन्त व गुरु (9)'],\n"
old_gita_cat = "    ['gita', '📜 रामायण व गीता (9)']\n"

if old_sants_cat in full_content:
    full_content = full_content.replace(old_sants_cat, "")
    print("Removed sants category chip!")
else:
    print("Warning: old_sants_cat not found!")

if old_gita_cat in full_content:
    full_content = full_content.replace(old_gita_cat, "")
    print("Removed gita category chip!")
else:
    print("Warning: old_gita_cat not found!")

# 3. Update 'all' label
full_content = re.sub(r"\[\s*'all'\s*,\s*'✨ सभी \(\d+\)'\s*\]", "['all', '✨ सभी (57)']", full_content)
print("Updated 'all' pill label to 57!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(full_content)

print("Saved app.js successfully!")
