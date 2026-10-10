import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
assets_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets"
rajan_img = os.path.join(assets_dir, "speaker_rajan.jpg")

# Extract thumbnail directly via yt-dlp
cmd = [
    "python", "-m", "yt_dlp",
    "--extractor-args", "youtube:player_client=android",
    "--skip-download",
    "--write-thumbnail",
    "--convert-thumbnails", "jpg",
    "-o", os.path.join(assets_dir, "speaker_rajan"),
    "https://www.youtube.com/watch?v=IbD67NM7HSc"
]
try:
    subprocess.run(cmd, check=True)
    if os.path.exists(os.path.join(assets_dir, "speaker_rajan.jpg")):
        print("Thumbnail saved successfully!")
    elif os.path.exists(os.path.join(assets_dir, "speaker_rajan.webp")):
        # convert to jpg
        cmd_c = [ffmpeg_exe, "-y", "-i", os.path.join(assets_dir, "speaker_rajan.webp"), rajan_img]
        subprocess.run(cmd_c, check=True)
        print("Converted webp to jpg!")
except Exception as e:
    print(f"Error: {e}")
