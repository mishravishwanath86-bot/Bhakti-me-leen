import os
import subprocess
import glob

audio_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets\audio"

# Remove .part files
for f in glob.glob(os.path.join(audio_dir, "*.part")):
    try: os.remove(f)
    except: pass

rem_kathas = [
    ("katha_vaishnodevi.webm", "ytsearch1:mata rani aarti bhor bhai din"),
    ("katha_harishchandra.webm", "ytsearch1:shree ram amritvani katha audio")
]

for filename, query in rem_kathas:
    out_path = os.path.join(audio_dir, filename)
    print(f"Downloading {filename}...")
    cmd = [
        "python", "-m", "yt_dlp",
        "-f", "ba/b",
        "--max-filesize", "50M",
        "--no-playlist",
        "-o", out_path,
        query
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Success: {filename}")
    except Exception as e:
        print(f"Error {filename}: {e}")
