import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()
cur.execute("SELECT id, title FROM content_items WHERE id LIKE '%aarti%' LIMIT 35")
for row in cur.fetchall():
    print(row[0], "-->", row[1])
