import os
import sys
import shutil
import subprocess
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

APP_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
ANDROID_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-android")
JDK_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\jdk-17\jdk17.0.20_12")

def main():
    print("[1/3] Syncing latest web assets to Android project...", flush=True)
    android_assets = ANDROID_DIR / "app" / "src" / "main" / "assets"
    android_assets.mkdir(parents=True, exist_ok=True)

    sync_files = [
        "index.html", "app.js", "styles.css", "epic_games_engine.js", "epic_games.css",
        "aarti_mantra_puzzle.js", "aarti_mantra_puzzle.css", "aarti_mantra_puzzle_engine.js",
        "ai_bhakti_player.js", "ai_bhakti_player.css", "mcq_test_series_engine.js",
        "version.json", "manifest.json", "mandir_3d_engine.js",
        "gallery_engine.js", "gita_engine.js", "mantra_engine.js", "sundarkand_engine.js",
        "chalisa_engine.js", "i18n_engine.js", "light_theme.css"
    ]

    for fname in sync_files:
        src = APP_DIR / fname
        dst = android_assets / fname
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  Synced: {fname}", flush=True)

    print("[2/3] Compiling fresh APK with Gradle...", flush=True)
    build_env = os.environ.copy()
    if JDK_DIR.exists():
        build_env["JAVA_HOME"] = str(JDK_DIR)
        build_env["PATH"] = str(JDK_DIR / "bin") + os.pathsep + build_env.get("PATH", "")

    gradle_cmd = "gradlew.bat assembleDebug --no-daemon"
    res = subprocess.run(gradle_cmd, cwd=str(ANDROID_DIR), shell=True, env=build_env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Gradle error ({res.returncode}):\n{res.stderr}\n{res.stdout}", flush=True)
        sys.exit(1)

    built_apk = ANDROID_DIR / "app" / "build" / "outputs" / "apk" / "debug" / "app-debug.apk"
    if not built_apk.exists():
        print("Built APK not found at:", built_apk, flush=True)
        sys.exit(1)

    size_mb = built_apk.stat().st_size / (1024 * 1024)
    print(f"APK built successfully! Size: {size_mb:.1f} MB", flush=True)

    print("[3/3] Copying APK to bhakti-app...", flush=True)
    dest_apk = APP_DIR / "bhakti-app.apk"
    dest_apk_short = APP_DIR / "bhakti.apk"
    shutil.copy2(built_apk, dest_apk)
    shutil.copy2(built_apk, dest_apk_short)

    print(f"COMPLETE! Fresh APK saved to:")
    print(f"  -> {dest_apk}")
    print(f"  -> {dest_apk_short}")

if __name__ == "__main__":
    main()
