import sqlite3, os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

# Open database strictly read-only
conn = sqlite3.connect('file:db/bhakti.db?mode=ro', uri=True)
cursor = conn.cursor()

# Check total katha and audio counts
cursor.execute("SELECT COUNT(*) FROM katha_content")
total_katha = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM katha_content WHERE audio_url IS NOT NULL AND audio_url != ''")
playable_audio = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM katha_content WHERE audio_url LIKE '%youtube%' OR audio_url LIKE '%youtu.be%'")
yt_audio = cursor.fetchone()[0]

print(f"Total Katha: {total_katha}")
print(f"Playable Audio: {playable_audio}")
print(f"YouTube Audio: {yt_audio}")

# Inspect some old known-good audio items
cursor.execute("""
    SELECT id, title, deity, category, audio_url, duration, audio_type 
    FROM katha_content 
    WHERE audio_url IS NOT NULL AND audio_url != ''
    LIMIT 10
""")
old_samples = cursor.fetchall()
print("\n--- Sample Audio Records in DB ---")
for row in old_samples:
    print(f"ID: {row[0]} | Title: {row[1]} | Audio: {row[4]} | Type: {row[6]}")

conn.close()
