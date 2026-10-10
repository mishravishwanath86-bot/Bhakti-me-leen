import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM content_items WHERE category_id='aarti' OR content_type='aarti'")
print("Aarti count in DB:", cur.fetchone()[0])

cur.execute("SELECT id, deity_id, title, audio_url FROM content_items WHERE category_id='aarti' OR content_type='aarti' ORDER BY deity_id")
rows = cur.fetchall()
print(f"\nListing all {len(rows)} Aarti items:")
for r in rows:
    print(r)
