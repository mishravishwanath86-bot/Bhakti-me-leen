import sqlite3, json, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('db/bhakti.db')
cursor = conn.cursor()

circle_id = 'circle_om1008' # canonical circle id in DB
user_id = 'usr_987654'
mantra_count = 108
sadhana_type = 'MAHAMRITYUNJAYA_JAP'

# 1. Record contribution in circle_contributions
cursor.execute("""
    INSERT INTO circle_contributions (circle_id, user_id, contributed_count)
    VALUES (?, ?, ?);
""", (circle_id, user_id, mantra_count))

# 2. Update sadhana_circles current_count
cursor.execute("""
    UPDATE sadhana_circles
    SET current_count = current_count + ?
    WHERE circle_id = ?;
""", (mantra_count, circle_id))

# 3. Update user punya points
punya_earned = round(mantra_count / 10 * 1.2) # 13 points with 1.2x Tapaswi multiplier

cursor.execute("""
    UPDATE user_sadhana_profile
    SET punya_points = punya_points + ?
    WHERE user_id = 'user_self';
""", (punya_earned,))

conn.commit()

# Query latest state
cursor.execute("SELECT title, target_count, current_count, mantra_type FROM sadhana_circles WHERE circle_id = ?;", (circle_id,))
circle_row = cursor.fetchone()

cursor.execute("SELECT user_id, current_streak, punya_points, active_shields, vedic_rank FROM user_sadhana_profile WHERE user_id = 'user_self';")
profile_row = cursor.fetchone()

cursor.execute("SELECT user_id, SUM(contributed_count) as total FROM circle_contributions WHERE circle_id = ? GROUP BY user_id ORDER BY total DESC;", (circle_id,))
contributors = [{"user_id": r[0], "total_contributed": r[1]} for r in cursor.fetchall()]

conn.close()

result = {
    "status": "SUCCESS",
    "message": "📿 108 महामृत्युंजय जप सामूहिक अनुष्ठान में सफलतापूर्वक समर्पित हुए!",
    "transaction": {
        "circle_id": circle_id,
        "user_id": user_id,
        "mantra_count": mantra_count,
        "sadhana_type": sadhana_type,
        "punya_points_awarded": punya_earned
    },
    "circle_progress": {
        "title": circle_row[0],
        "mantra_type": circle_row[3],
        "target_count": circle_row[1],
        "current_count": circle_row[2],
        "completion_percentage": f"{round((circle_row[2] / circle_row[1]) * 100, 2)}%",
        "remaining_count": circle_row[1] - circle_row[2]
    },
    "user_sadhana_profile": {
        "current_streak": f"{profile_row[1]} दिन",
        "total_punya_points": profile_row[2],
        "active_shields": profile_row[3],
        "vedic_rank": f"🔱 {profile_row[4]} (Level 2)"
    },
    "top_contributors": contributors
}

print(json.dumps(result, indent=2, ensure_ascii=False))
