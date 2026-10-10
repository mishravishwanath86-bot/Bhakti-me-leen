import os
import subprocess

audio_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets\audio"
os.makedirs(audio_dir, exist_ok=True)

# List of search queries to fetch real devotional audio
kathas = [
    ("katha_bhagwat.mp3", "ytsearch1:shrimad bhagwat katha short pravachan bhajan"),
    ("katha_ramayana.mp3", "ytsearch1:ramcharitmanas chaupai bhaye pragat kripala"),
    ("katha_shiva.mp3", "ytsearch1:shiv mahapuran katha stuti har har mahadev"),
    ("katha_satyanarayan.mp3", "ytsearch1:shri satyanarayan vrat katha aarti"),
    ("katha_hanuman.mp3", "ytsearch1:shree hanuman chalisa gulshan kumar"),
    ("katha_vaishnodevi.mp3", "ytsearch1:mata vaishno devi katha aarti bhajan"),
    ("katha_narsingh.mp3", "ytsearch1:bhagwan narsingh aarti stuti"),
    ("katha_harishchandra.mp3", "ytsearch1:satya prem bhagwan bhakti dhun katha")
]

for filename, query in kathas:
    out_path = os.path.join(audio_dir, filename)
    print(f"Downloading {filename} from {query}...")
    cmd = [
        "python", "-m", "yt_dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "128K",
        "--max-filesize", "15M",
        "--no-playlist",
        "-o", out_path.replace(".mp3", ".%(ext)s"),
        query
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Success: {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

print("Done processing all downloads!")
