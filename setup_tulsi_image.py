import shutil
import os

src = r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\bal_tulsi_little_1790272782533.jpg"

dst1 = r"assets\gallery\bal_tulsi_little.jpg"
dst2 = r"assets\deity_tulsi.jpg"

if os.path.exists(src):
    shutil.copyfile(src, dst1)
    shutil.copyfile(src, dst2)
    print(f"Copied to {dst1} ({os.path.getsize(dst1)} bytes)")
    print(f"Copied to {dst2} ({os.path.getsize(dst2)} bytes)")
else:
    print(f"Source file {src} not found!")
