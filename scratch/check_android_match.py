import os

android_dir = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-android"

for root, dirs, files in os.walk(android_dir):
    for f in files:
        if f.endswith(('.js', '.html', '.css')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    if 'match-level-hub-grid' in content:
                        print(f"Found match-level-hub-grid in: {p}")
                    if 'match-level-card' in content:
                        print(f"Found match-level-card in: {p}")
            except Exception:
                pass
print("Android scan complete.")
