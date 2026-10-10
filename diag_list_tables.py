import sqlite3, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('file:db/bhakti.db?mode=ro', uri=True)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in db/bhakti.db:", tables)

for t in tables:
    tname = t[0]
    cursor.execute(f"PRAGMA table_info({tname});")
    cols = [c[1] for c in cursor.fetchall()]
    cursor.execute(f"SELECT COUNT(*) FROM {tname};")
    cnt = cursor.fetchone()[0]
    print(f"Table: {tname} ({cnt} rows) -> Columns: {cols}")

conn.close()
