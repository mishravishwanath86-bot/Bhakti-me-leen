import shutil
import os
import glob

app_dir = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
android_assets = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-android\app\src\main\assets"

sync_files = [
    "index.html", "app.js", "styles.css", "epic_games_engine.js", "epic_games.css",
    "aarti_mantra_puzzle.js", "aarti_mantra_puzzle.css", "aarti_mantra_puzzle_engine.js",
    "ai_bhakti_player.js", "ai_bhakti_player.css", "mcq_test_series_engine.js",
    "version.json", "manifest.json", "service-worker.js", "mandir_3d_engine.js",
    "gallery_engine.js", "gita_engine.js", "mantra_engine.js", "sundarkand_engine.js",
    "chalisa_engine.js", "i18n_engine.js", "light_theme.css"
]

for fname in sync_files:
    src = os.path.join(app_dir, fname)
    dst = os.path.join(android_assets, fname)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print("Synced file:", fname)

for folder in ["assets/wall_of_fame", "assets/games", "assets/symbols/cards", "assets/ai_audio", "data"]:
    src_f = os.path.join(app_dir, folder)
    dst_f = os.path.join(android_assets, folder)
    if os.path.exists(src_f):
        os.makedirs(dst_f, exist_ok=True)
        for item in glob.glob(os.path.join(src_f, "*")):
            if os.path.isfile(item):
                shutil.copy2(item, os.path.join(dst_f, os.path.basename(item)))
        print("Synced folder:", folder)

print("SUCCESS: ALL ASSETS SYNCED TO ANDROID!")
