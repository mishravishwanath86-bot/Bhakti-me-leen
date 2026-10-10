import sqlite3, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cursor = conn.cursor()

# 1. Create user_sadhana_profile
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_sadhana_profile (
    user_id VARCHAR(64) PRIMARY KEY,
    current_streak INT DEFAULT 0,
    longest_streak INT DEFAULT 0,
    punya_points INT DEFAULT 0,
    active_shields INT DEFAULT 1,
    vedic_rank VARCHAR(32) DEFAULT 'SADHAK',
    last_active_date DATE
);
""")

# 2. Create sadhana_circles
cursor.execute("""
CREATE TABLE IF NOT EXISTS sadhana_circles (
    circle_id VARCHAR(64) PRIMARY KEY,
    admin_user_id VARCHAR(64),
    title VARCHAR(128),
    target_count INT,
    current_count INT DEFAULT 0,
    mantra_type VARCHAR(64),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# 3. Create circle_contributions
cursor.execute("""
CREATE TABLE IF NOT EXISTS circle_contributions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    circle_id VARCHAR(64) REFERENCES sadhana_circles(circle_id),
    user_id VARCHAR(64),
    contributed_count INT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Seed initial default profile if not exists
cursor.execute("SELECT COUNT(*) FROM user_sadhana_profile WHERE user_id = 'user_self';")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
        INSERT INTO user_sadhana_profile (user_id, current_streak, longest_streak, punya_points, active_shields, vedic_rank, last_active_date)
        VALUES ('user_self', 21, 21, 1450, 1, 'TAPASWI', DATE('now'));
    """)

# Seed initial default circle if not exists
cursor.execute("SELECT COUNT(*) FROM sadhana_circles WHERE circle_id = 'circle_om1008';")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
        INSERT INTO sadhana_circles (circle_id, admin_user_id, title, target_count, current_count, mantra_type)
        VALUES ('circle_om1008', 'user_father', 'महामृत्युंजय 1 लाख महा-अनुष्ठान (मिश्रा परिवार)', 100000, 68400, 'महामृत्युंजय मंत्र');
    """)
    cursor.execute("""
        INSERT INTO circle_contributions (circle_id, user_id, contributed_count)
        VALUES 
        ('circle_om1008', 'पिता जी', 24000),
        ('circle_om1008', 'आप (You)', 18200),
        ('circle_om1008', 'माता जी', 15000),
        ('circle_om1008', 'राहुल', 11200);
    """)

conn.commit()

# Verify
cursor.execute("PRAGMA integrity_check;")
print("Integrity:", cursor.fetchone()[0])
cursor.execute("PRAGMA foreign_key_check;")
print("Foreign keys:", cursor.fetchall())
cursor.execute("SELECT COUNT(*) FROM user_sadhana_profile;")
print("User sadhana profiles:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM sadhana_circles;")
print("Sadhana circles:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM circle_contributions;")
print("Circle contributions:", cursor.fetchone()[0])

conn.close()
print("✓ Successfully initialized Sadhana Streak Shield & Collective Sangha database tables!")
