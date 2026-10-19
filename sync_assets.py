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
    "chalisa_engine.js", "i18n_engine.js", "light_theme.css", "bhagavad_gita_chapters.json"
]

print("--- Syncing Root Web Files ---")
for fname in sync_files:
    src = os.path.join(app_dir, fname)
    dst = os.path.join(android_assets, fname)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Synced file: {fname}")

sync_folders = [
    "assets/wall_of_fame",
    "assets/games",
    "assets/videos",
    "assets/symbols/cards",
    "assets/ai_audio",
    "assets/cards",
    "assets/gates",
    "assets/gallery",
    "data"
]

print("\n--- Syncing Folders ---")
for folder in sync_folders:
    src_f = os.path.join(app_dir, folder)
    dst_f = os.path.join(android_assets, folder)
    if os.path.exists(src_f):
        os.makedirs(dst_f, exist_ok=True)
        count = 0
        for root, dirs, files in os.walk(src_f):
            rel_dir = os.path.relpath(root, src_f)
            target_sub = os.path.join(dst_f, rel_dir) if rel_dir != "." else dst_f
            os.makedirs(target_sub, exist_ok=True)
            for f in files:
                s_file = os.path.join(root, f)
                d_file = os.path.join(target_sub, f)
                shutil.copy2(s_file, d_file)
                count += 1
        print(f"Synced folder: {folder} ({count} files)")

print("\nSUCCESS: ALL ASSETS & CARDS & GITA IMAGES SYNCED TO ANDROID!")
