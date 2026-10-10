import json, sqlite3, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('drik_aarti_parsed.json', 'r', encoding='utf-8') as f:
    drik_cats = json.load(f)

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()

cur.execute("SELECT id, title, content, audio_url FROM content_items WHERE category_id LIKE '%aarti%' OR id LIKE '%aarti%'")
db_rows = cur.fetchall()
print(f"Total db aarti rows: {len(db_rows)}")

matched = 0
total = 0

for cat in drik_cats:
    for item in cat['items']:
        total += 1
        hi = item['hi_line']
        title = item['title']
        
        # match in db
        found = False
        for r in db_rows:
            db_id, db_title, db_content, db_audio = r
            # check if title or first line matches
            if any(term in db_title for term in [hi[:10], title.replace('Aarti', '').strip()]):
                found = True
                item['db_id'] = db_id
                item['db_title'] = db_title
                item['audio_url'] = db_audio
                item['content'] = db_content[:300] if db_content else ''
                matched += 1
                break
                
print(f"Matched {matched} / {total} items directly against SQLite db!")

with open('drik_aarti_matched.json', 'w', encoding='utf-8') as f:
    json.dump(drik_cats, f, ensure_ascii=False, indent=2)

conn.close()
