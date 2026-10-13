import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
c = conn.cursor()

print("--- Query Kunjbihari ---")
c.execute("SELECT id, title, deity_id, content_type, audio_url, length(content) FROM content_items WHERE title LIKE '%कुंजबिहारी%' OR content LIKE '%कुंजबिहारी%'")
rows = c.fetchall()
for r in rows:
    print(r)

print("\n--- Query Jugal Kishore ---")
c.execute("SELECT id, title, deity_id, content_type, audio_url, length(content) FROM content_items WHERE title LIKE '%जुगल किशोर%' OR content LIKE '%जुगल किशोर%'")
rows = c.fetchall()
for r in rows:
    print(r)

conn.close()
