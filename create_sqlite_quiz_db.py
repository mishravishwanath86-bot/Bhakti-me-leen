import sqlite3, json, os

with open('all_sanatan_mcqs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

os.makedirs('assets', exist_ok=True)
db_path = 'assets/quiz_database.db'
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    options TEXT NOT NULL,
    correct_answer INTEGER NOT NULL,
    explanation TEXT,
    category TEXT,
    is_bookmarked INTEGER DEFAULT 0
)
""")

for q in data:
    cursor.execute("""
    INSERT INTO questions (id, question, options, correct_answer, explanation, category, is_bookmarked)
    VALUES (?, ?, ?, ?, ?, ?, 0)
    """, (
        q['id'],
        q['question'],
        json.dumps(q['options'], ensure_ascii=False),
        q['correct_answer'],
        q.get('explanation', ''),
        q.get('category', 'All')
    ))

conn.commit()
count = cursor.execute("SELECT count(*) FROM questions").fetchone()[0]
print(f"Created SQLite database {db_path} with {count} questions successfully!")
conn.close()
