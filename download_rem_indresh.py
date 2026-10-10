import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
audio_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app\assets\audio"

rem_kathas = [
    {
        "filename": "katha_indresh_tajbegum.mp3",
        "query": "ytsearch1:bhakti taj begum katha indresh upadhyay ji"
    },
    {
        "filename": "katha_indresh_chhitupanda.mp3",
        "query": "ytsearch1:story of devotee chhitu panda indresh upadhyay"
    },
    {
        "filename": "katha_indresh_surdas.mp3",
        "query": "ytsearch1:surdas ji ka jeevan katha indresh upadhyay"
    }
]

for item in rem_kathas:
    fn = item["filename"]
    query = item["query"]
    temp_webm = os.path.join(audio_dir, fn.replace(".mp3", "_temp.webm"))
    final_mp3 = os.path.join(audio_dir, fn)
    
    print(f"Downloading {fn} via search...")
    cmd_dl = [
        "python", "-m", "yt_dlp",
        "--extractor-args", "youtube:player_client=android",
        "-f", "ba/b",
        "--no-playlist",
        "-o", temp_webm,
        query
    ]
    try:
        subprocess.run(cmd_dl, check=True)
        cmd_conv = [
            ffmpeg_exe, "-y",
            "-i", temp_webm,
            "-vn", "-ar", "44100", "-ac", "2", "-b:a", "128k",
            final_mp3
        ]
        subprocess.run(cmd_conv, check=True)
        print(f"SUCCESS: {final_mp3} (Size: {os.path.getsize(final_mp3)} bytes)")
        if os.path.exists(temp_webm):
            os.remove(temp_webm)
    except Exception as e:
        print(f"Error on {fn}: {e}")

print("Done with remaining Indresh Kathas!")
