import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
audio_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets\audio"

# Download authentic Satyanarayan Vrat Katha
out_webm = os.path.join(audio_dir, "satyanarayan_temp.webm")
cmd = [
    "python", "-m", "yt_dlp",
    "-f", "ba/b",
    "--max-filesize", "30M",
    "--no-playlist",
    "-o", out_webm,
    "ytsearch1:satyanarayan vrat katha sampoorna anuradha paudwal"
]
subprocess.run(cmd, check=True)

# Convert to katha_satyanarayan.mp3
mp3_out = os.path.join(audio_dir, "katha_satyanarayan.mp3")
cmd_conv = [
    ffmpeg_exe, "-y",
    "-i", out_webm,
    "-vn", "-ar", "44100", "-ac", "2", "-b:a", "128k",
    mp3_out
]
subprocess.run(cmd_conv, check=True)
if os.path.exists(out_webm):
    os.remove(out_webm)

print("Downloaded and replaced katha_satyanarayan.mp3 successfully!")
