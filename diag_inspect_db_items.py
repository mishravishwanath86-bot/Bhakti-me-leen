import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
c = conn.cursor()

print("=== Content Types in DB ===")
c.execute("SELECT id, name_hi, name_en FROM content_types")
for row in c.fetchall():
    print(row)

print("\n=== Sample Sundarkand in DB ===")
c.execute("SELECT id, title, deity_id, category_id, content_type, length(content) FROM content_items WHERE content_type='sundarkand' LIMIT 5")
for row in c.fetchall():
    print(row)

print("\n=== Sample Mantra in DB ===")
c.execute("SELECT id, title, deity_id, category_id, content_type, length(content) FROM content_items WHERE content_type='mantra' LIMIT 5")
for row in c.fetchall():
    print(row)

print("\n=== Sample Chalisa in DB ===")
c.execute("SELECT id, title, deity_id, category_id, content_type, length(content) FROM content_items WHERE content_type='chalisa' LIMIT 5")
for row in c.fetchall():
    print(row)

print("\n=== Sample Aarti in DB ===")
c.execute("SELECT id, title, deity_id, category_id, content_type, length(content) FROM content_items WHERE content_type='aarti' LIMIT 5")
for row in c.fetchall():
    print(row)

print("\n=== Check Aarti Jugal Kishore in DB ===")
c.execute("SELECT id, title, deity_id, category_id, content_type, length(content), substr(content, 1, 100) FROM content_items WHERE title LIKE '%जुगल किशोर%' OR content LIKE '%जुगल किशोर%'")
rows = c.fetchall()
print(f"Found {len(rows)} rows for Jugal Kishore:")
for row in rows:
    print(row)

print("\n=== Check Gita in DB ===")
c.execute("SELECT id, title, deity_id, category_id, content_type, length(content) FROM content_items WHERE id LIKE '%gita%' OR title LIKE '%गीता%' OR title_en LIKE '%gita%' LIMIT 10")
for row in c.fetchall():
    print(row)

conn.close()
