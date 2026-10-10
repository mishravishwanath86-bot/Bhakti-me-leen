import os
import subprocess

audio_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets\audio"

rem_kathas = [
    ("katha_vaishnodevi.webm", "ytsearch1:mata vaishno devi aarti gulshan kumar"),
    ("katha_harishchandra.webm", "ytsearch1:raja harishchandra katha hindi kahani")
]

for filename, query in rem_kathas:
    out_path = os.path.join(audio_dir, filename)
    print(f"Downloading {filename}...")
    cmd = [
        "python", "-m", "yt_dlp",
        "-f", "ba/b",
        "--max-filesize", "30M",
        "--no-playlist",
        "-o", out_path,
        query
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Success: {filename}")
    except Exception as e:
        print(f"Error {filename}: {e}")
