import sqlite3, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('file:db/bhakti.db?mode=ro', uri=True)
cursor = conn.cursor()

# Check total katha items
cursor.execute("SELECT COUNT(*) FROM content_items WHERE content_type = 'katha'")
total_katha = cursor.fetchone()[0]

# Query all katha items with audio
cursor.execute("""
    SELECT id, title, audio_url, video_url, duration, deity_id, category_id
    FROM content_items 
    WHERE content_type = 'katha' AND audio_url IS NOT NULL AND audio_url != ''
""")
all_katha_audio = cursor.fetchall()
playable_count = len(all_katha_audio)

print(f"Total Katha in DB: {total_katha}")
print(f"Total Playable Katha Audio: {playable_count}")

# Check YouTube vs MP3 in DB
yt_katha = [r for r in all_katha_audio if 'youtube.com' in r[2] or 'youtu.be' in r[2]]
mp3_katha = [r for r in all_katha_audio if r[2].endswith('.mp3') or 'assets/audio' in r[2]]
other_katha = [r for r in all_katha_audio if r not in yt_katha and r not in mp3_katha]

print(f"YouTube Audio Katha: {len(yt_katha)}")
print(f"Local/Remote MP3 Katha: {len(mp3_katha)}")
print(f"Other Katha: {len(other_katha)}")

# Check audit files for Phase 2N, 2O, 2P, 2Q if they exist in bulk_import/audits
audit_files = [f for f in os.listdir('bulk_import/audits') if f.endswith('.json') or f.endswith('.md')]
print("\nAudit files in bulk_import/audits:")
for af in sorted(audit_files):
    print(f"  - {af}")

conn.close()
