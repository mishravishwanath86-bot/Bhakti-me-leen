import sqlite3, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('file:db/bhakti.db?mode=ro', uri=True)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM content_items WHERE content_type = 'katha'")
total_katha = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM content_items WHERE content_type = 'katha' AND audio_url IS NOT NULL AND audio_url != ''")
playable_audio = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM content_items WHERE content_type = 'katha' AND (audio_url LIKE '%youtube%' OR audio_url LIKE '%youtu.be%')")
yt_audio = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM content_items WHERE content_type = 'katha' AND audio_url LIKE '%.mp3%'")
mp3_audio = cursor.fetchone()[0]

print(f"Total Katha: {total_katha}")
print(f"Playable Audio: {playable_audio}")
print(f"YouTube Audio: {yt_audio}")
print(f"MP3 Audio: {mp3_audio}")

cursor.execute("""
    SELECT id, title, audio_url, duration 
    FROM content_items 
    WHERE content_type = 'katha' AND audio_url IS NOT NULL AND audio_url != ''
    LIMIT 10
""")
print("\n--- First 10 Katha Audio Records ---")
for r in cursor.fetchall():
    print(r)

conn.close()
