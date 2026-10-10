import os
import zipfile

app_dir = r"C:\Users\vishw\.gemini\antigravity\scratch\bhakti-app"
brain_dir = r"C:\Users\vishw\.gemini\antigravity\brain\e50f2a93-46d3-48c0-84de-1c22a15837d4"

zip_path1 = os.path.join(app_dir, 'bhakti-app.zip')
zip_path2 = os.path.join(brain_dir, 'bhakti-app.zip')

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.zip') or file.endswith('.tmp'):
                continue
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, path)
            ziph.write(full_p, rel_p)

with zipfile.ZipFile(zip_path1, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(app_dir, zipf)

with zipfile.ZipFile(zip_path2, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(app_dir, zipf)

print("Exported updated ZIP successfully!")
