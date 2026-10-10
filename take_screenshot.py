import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
out_img = r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\nav_dock_screenshot.png"

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    "--window-size=412,860",
    f"--screenshot={out_img}",
    "http://localhost:8000/index.html"
]

print("Running headless Edge...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("Return code:", res.returncode)
print("File exists:", os.path.exists(out_img))
if os.path.exists(out_img):
    print("File size:", os.path.getsize(out_img))
