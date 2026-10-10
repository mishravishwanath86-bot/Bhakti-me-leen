import sqlite3, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print('Existing tables:', [r[0] for r in c.fetchall()])
conn.close()
