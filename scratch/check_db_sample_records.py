import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
c = conn.cursor()

for t in ['sundarkand', 'mantra', 'chalisa', 'aarti']:
    c.execute('SELECT id, title, length(content), substr(content, 1, 150) FROM content_items WHERE content_type = ? LIMIT 1', (t,))
    row = c.fetchone()
    print(f'Type: {t}')
    print(f'  ID: {row[0]}')
    print(f'  Title: {row[1]}')
    print(f'  Content Length: {row[2]}')
    print(f'  Sample: {row[3]}')
    print('---')
