import subprocess, json

video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
# Extract audio info or check if audio track exists
cmd = f"powershell -Command \"(New-Object -ComObject Shell.Application).Namespace('C:\\Users\\vishw\\Downloads').ParseName('WhatsApp Video 2026-09-27 at 17.16.59.mp4').ExtendedProperty('System.Audio.ChannelCount')\""
res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
print("Audio channel check:", res.stdout.strip())
