import os, sys

scratch_dir = r"C:\Users\vishw\.gemini\antigravity-ide\scratch"
target = "प्रारंभिक".encode('utf-8')

for root, dirs, files in os.walk(scratch_dir):
    # skip large binaries
    for f in files:
        if f.endswith(('.js', '.html', '.css', '.json', '.txt', '.py')):
            p = os.path.join(root, f)
            try:
                with open(p, 'rb') as fp:
                    data = fp.read()
                    if target in data:
                        print(f"Match: {p}")
            except Exception:
                pass
print("Search finished.")
