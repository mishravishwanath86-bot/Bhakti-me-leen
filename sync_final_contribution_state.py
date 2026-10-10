import sqlite3, json, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cursor = conn.cursor()

# Update 'आप (You)' contribution in circle_contributions to 18308
cursor.execute("""
    UPDATE circle_contributions 
    SET contributed_count = 18308
    WHERE circle_id = 'circle_om1008' AND user_id = 'आप (You)';
""")

# Update circle current_count to 68508
cursor.execute("""
    UPDATE sadhana_circles
    SET current_count = 68508
    WHERE circle_id = 'circle_om1008';
""")

# Update user_sadhana_profile punya_points to 1475 (1450 + 25)
cursor.execute("""
    UPDATE user_sadhana_profile
    SET punya_points = 1475, current_streak = 21, active_shields = 1
    WHERE user_id = 'user_self';
""")

conn.commit()

cursor.execute("SELECT * FROM user_sadhana_profile WHERE user_id = 'user_self';")
profile = cursor.fetchone()

cursor.execute("SELECT * FROM sadhana_circles WHERE circle_id = 'circle_om1008';")
circle = cursor.fetchone()

cursor.execute("SELECT user_id, contributed_count FROM circle_contributions WHERE circle_id = 'circle_om1008' ORDER BY contributed_count DESC;")
contributors = cursor.fetchall()

conn.close()

print("✓ Database successfully synchronized with confirmed contribution payload!")
print(f"Profile: Streak={profile[1]}, Punya={profile[3]}, Shields={profile[4]}, Rank={profile[5]}")
print(f"Circle: Title='{circle[2]}', Progress={circle[4]}/{circle[3]} ({round(circle[4]/circle[3]*100, 1)}%)")
print(f"Contributors: {contributors}")
