import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in c.fetchall()]
print('Tables:', tables)

print('\n--- Content Types ---')
c.execute("SELECT id, name_hi, name_en FROM content_types")
for r in c.fetchall():
    print(r)

print('\n--- Categories ---')
c.execute("SELECT id, name_hi, name_en FROM categories")
for r in c.fetchall():
    print(r)

print('\n--- Content Items Count by Type ---')
c.execute("SELECT content_type, COUNT(1) FROM content_items GROUP BY content_type")
for r in c.fetchall():
    print(r)

print('\n--- Total Content Items ---')
c.execute("SELECT COUNT(1) FROM content_items")
print('Total:', c.fetchone()[0])

print('\n--- Check for Gita, Sundarkand, Mantra, Chalisa, Aarti items ---')
for term in ['gita', 'geeta', 'sundarkand', 'sundar', 'mantra', 'chalisa', 'aarti']:
    c.execute("SELECT COUNT(1) FROM content_items WHERE content_type = ? OR id LIKE ? OR title LIKE ?", (term, f'%{term}%', f'%{term}%'))
    print(f'Matches for {term}:', c.fetchone()[0])

conn.close()
