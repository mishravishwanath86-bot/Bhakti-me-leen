import sqlite3, json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()

cur.execute("SELECT id, title, content, audio_url FROM content_items WHERE category_id LIKE '%aarti%' OR id LIKE '%aarti%'")
db_items = cur.fetchall()

print(f"Loaded {len(db_items)} items from db.")

with open('drik_aarti_parsed.json', 'r', encoding='utf-8') as f:
    drik_cats = json.load(f)

# Build a search index from db
# Normalize helper
def norm(s):
    if not s: return ''
    return re.sub(r'[\s\W_]+', '', s.lower())

for cat in drik_cats:
    for item in cat['items']:
        hi = norm(item['hi_line'])
        en = norm(item['title'])
        en_sub = norm(item['en_line'])
        
        best_match = None
        for r in db_items:
            db_id, db_title, db_content, db_audio = r
            db_t_norm = norm(db_title)
            
            # Check for substring matches
            if hi and (hi in db_t_norm or db_t_norm in hi):
                best_match = r
                break
            if en_sub and en_sub in db_t_norm:
                best_match = r
                break
                
        if best_match:
            item['matched_id'] = best_match[0]
            item['matched_title'] = best_match[1]
            item['audio_url'] = best_match[3]
            item['has_content'] = bool(best_match[2])
            item['content_len'] = len(best_match[2]) if best_match[2] else 0

total_items = sum(len(c['items']) for c in drik_cats)
matched_items = sum(1 for c in drik_cats for i in c['items'] if 'matched_id' in i)
print(f"Matched {matched_items} / {total_items} items!")

conn.close()

with open('drik_aarti_enriched.json', 'w', encoding='utf-8') as f:
    json.dump(drik_cats, f, ensure_ascii=False, indent=2)
