import shutil
import os

src = r"assets\deity_bhairav.jpg"
dst = r"assets\gallery\bal_bhairav_little.jpg"

if os.path.exists(src):
    shutil.copyfile(src, dst)
    print(f"Copied {src} to {dst}, size: {os.path.getsize(dst)} bytes")
else:
    print(f"Source {src} does not exist!")
