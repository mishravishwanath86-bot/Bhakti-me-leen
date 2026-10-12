import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
c = conn.cursor()

print("=== Content Types in content_items ===")
c.execute("SELECT content_type, count(*) FROM content_items GROUP BY content_type")
for r in c.fetchall():
    print(r)

print("\n=== Categories in content_items ===")
c.execute("SELECT category_id, count(*) FROM content_items GROUP BY category_id")
for r in c.fetchall():
    print(r)

print("\n=== Deities in content_items ===")
c.execute("SELECT deity_id, count(*) FROM content_items GROUP BY deity_id")
for r in c.fetchall():
    print(r)

print("\n=== Check Sundarkand items in DB ===")
c.execute("SELECT id, title, content_type, category_id, deity_id, length(content) FROM content_items WHERE content_type = 'sundarkand' LIMIT 5")
for r in c.fetchall():
    print(r)

print("\n=== Check Mantra items in DB ===")
c.execute("SELECT id, title, content_type, category_id, deity_id, length(content) FROM content_items WHERE content_type = 'mantra' LIMIT 5")
for r in c.fetchall():
    print(r)

print("\n=== Check Chalisa items in DB ===")
c.execute("SELECT id, title, content_type, category_id, deity_id, length(content) FROM content_items WHERE content_type = 'chalisa' LIMIT 5")
for r in c.fetchall():
    print(r)

print("\n=== Check Aarti items in DB ===")
c.execute("SELECT id, title, content_type, category_id, deity_id, length(content) FROM content_items WHERE content_type = 'aarti' LIMIT 5")
for r in c.fetchall():
    print(r)

conn.close()
