import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()
cur.execute("SELECT id, title, audio_url FROM content_items WHERE id LIKE '%aarti%'")
rows = cur.fetchall()
print(f"Total aartis in db: {len(rows)}")
for r in rows:
    print(f"{r[0]} --> {r[1]} [{r[2][:35] if r[2] else 'NO AUDIO'}]")
conn.close()
