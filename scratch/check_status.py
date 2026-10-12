import sqlite3

conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()

for t in ['sundarkand', 'aarti', 'chalisa', 'mantra']:
    cur.execute("SELECT status, COUNT(*) FROM content_items WHERE content_type=? GROUP BY status", (t,))
    print(t, cur.fetchall())

conn.close()
