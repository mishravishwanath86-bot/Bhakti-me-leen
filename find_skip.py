import os, glob

for fn in ["index.html", "app.js", "sw.js"]:
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            if "skipIntroVideo" in c:
                print(f"Found in {fn}")
                idx = c.find("skipIntroVideo")
                print(c[idx-50:idx+250])
