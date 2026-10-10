import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
assets_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets"
webp_p = os.path.join(assets_dir, "speaker_rajan.webp")
jpg_p = os.path.join(assets_dir, "speaker_rajan.jpg")

if os.path.exists(webp_p):
    subprocess.run([ffmpeg_exe, "-y", "-i", webp_p, jpg_p], check=True)
    print("Successfully generated assets/speaker_rajan.jpg!")
