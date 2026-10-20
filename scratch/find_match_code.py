import os

app_dir = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"

target_bytes = "जोड़ी".encode("utf-8")
alt_bytes = "जोड़े".encode("utf-8")
alt2_bytes = "प्रारंभिक".encode("utf-8")
alt3_bytes = "महारथी".encode("utf-8")

print("Searching for UTF-8 patterns across files...")
for root, dirs, files in os.walk(app_dir):
    for f in files:
        if f.endswith(('.js', '.html', '.py', '.css')):
            p = os.path.join(root, f)
            try:
                with open(p, "rb") as fp:
                    content = fp.read()
                    matches = []
                    if target_bytes in content: matches.append("जोड़ी")
                    if alt_bytes in content: matches.append("जोड़े")
                    if alt2_bytes in content: matches.append("प्रारंभिक")
                    if alt3_bytes in content: matches.append("महारथी")
                    if matches:
                        print(f"{os.path.relpath(p, app_dir)}: {matches}")
            except Exception as e:
                pass
print("Done search.")
