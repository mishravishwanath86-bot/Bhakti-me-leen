import sys
import codecs
import sqlite3

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print(f"Tables in db/bhakti.db: {tables}")

for t in tables:
    cur.execute(f"SELECT COUNT(*) FROM {t}")
    cnt = cur.fetchone()[0]
    print(f"Table {t}: {cnt} rows")

print("\n--- content_items Breakdown by content_type ---")
cur.execute("SELECT content_type, COUNT(*) FROM content_items GROUP BY content_type")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]} records")

print("\n--- content_items Sample for aarti ---")
cur.execute("SELECT id, title, deity_id, category_id, length(content) FROM content_items WHERE content_type='aarti' LIMIT 5")
for row in cur.fetchall():
    print(f"  {row}")

print("\n--- content_items Sample for chalisa ---")
cur.execute("SELECT id, title, deity_id, category_id, length(content) FROM content_items WHERE content_type='chalisa' LIMIT 5")
for row in cur.fetchall():
    print(f"  {row}")

print("\n--- content_items Sample for mantra ---")
cur.execute("SELECT id, title, deity_id, category_id, length(content) FROM content_items WHERE content_type='mantra' LIMIT 5")
for row in cur.fetchall():
    print(f"  {row}")

print("\n--- content_items Sample for sundarkand ---")
cur.execute("SELECT id, title, deity_id, category_id, length(content) FROM content_items WHERE content_type='sundarkand' LIMIT 5")
for row in cur.fetchall():
    print(f"  {row}")

conn.close()
