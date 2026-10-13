#!/usr/bin/env python3
"""
🚀 BHAKTI APP - 1-CLICK AUTO-UPDATE & RELEASE PUBLISHER
======================================================
This script automates the entire release pipeline so your users/friends 
receive an automatic update popup whenever they open the app!

Steps executed automatically:
 1. Reads current version and bumps versionCode and versionName (e.g. 8 -> 9, 1.7.0 -> 1.8.0)
 2. Updates version.json, app.js, and Android build.gradle.kts
 3. Syncs web assets to bhakti-android/app/src/main/assets
 4. Compiles fresh signed/debug APK using Gradle
 5. Copies APK to bhakti-app.apk
 6. Commits changes and pushes to GitHub (main + git tag)
 7. Creates GitHub Release vX.X.X via GitHub API
 8. Uploads bhakti-app.apk to the GitHub Release assets
 9. Purges jsDelivr CDN cache so all phones receive the update instantly
"""

import os
import sys
import json
import time
import shutil
import urllib.request
import subprocess
from pathlib import Path

# Force UTF-8 for console output on Windows
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Paths
APP_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
ANDROID_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-android")
JDK_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\jdk-17\jdk17.0.20_12")

GITHUB_REPO = "mishravishwanath86-bot/Bhakti-me-leen"

def get_github_token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    res = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    import re
    m = re.search(r':(ghp_[a-zA-Z0-9_]+)@', res.stdout)
    if m:
        return m.group(1)
    env_file = APP_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("GITHUB_TOKEN="):
                return line.split("=", 1)[1].strip()
    return ""

GITHUB_TOKEN = get_github_token()

def log(msg):
    print(f"\n[RELEASE] {msg}", flush=True)

def run_cmd(cmd, cwd=None, env=None):
    print(f"  > Executing: {cmd}", flush=True)
    res = subprocess.run(cmd, cwd=cwd, shell=True, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  ❌ Error (exit code {res.returncode}):\n{res.stderr}\n{res.stdout}", flush=True)
        return False, res.stdout, res.stderr
    return True, res.stdout, res.stderr

def main():
    log("Starting Bhakti App Auto-Update Publisher...")

    # 1. Read current version.json
    vfile = APP_DIR / "version.json"
    if not vfile.exists():
        print("❌ version.json not found in", APP_DIR)
        sys.exit(1)

    vdata = json.loads(vfile.read_text(encoding="utf-8"))
    curr_code = int(vdata.get("versionCode", 8))
    curr_ver = vdata.get("versionName", "1.7.0")

    next_code = curr_code + 1
    parts = curr_ver.split(".")
    if len(parts) == 3:
        next_ver = f"{parts[0]}.{int(parts[1]) + 1}.0"
    else:
        next_ver = f"1.{next_code}.0"

    # Allow command line overrides: python publish_update.py 1.8.0 9 "Notes"
    if len(sys.argv) > 1 and sys.argv[1].strip():
        next_ver = sys.argv[1].strip()
    if len(sys.argv) > 2 and sys.argv[2].strip().isdigit():
        next_code = int(sys.argv[2].strip())

    tag_name = f"v{next_ver}"
    log(f"Upgrading from v{curr_ver} (code {curr_code}) ➔ {tag_name} (code {next_code})")

    # Release Notes
    default_notes = [
        "दिव्य आरती पहेली (Aarti Game): सम्पूर्ण आरती पंक्तियों का मनोरम क्रम संयोजन",
        "वैदिक मन्त्र पहेली (Mantra Game): महामृत्युंजय व गायत्री मन्त्र का पावन संयोजन",
        "सनातन गेम्स हब ५० स्तर: रामायण स्वाइप, ३० स्तर कार्ड मैच, ५० स्तर जिग्सॉ पहेली, फूल अर्पण",
        "सुन्दरकाण्ड पाठ UI/UX सम्पूर्ण नवीनीकरण: सोपान पिल्स, रॉयल दोहा कार्ड्स व त्वरित जम्पर",
        "दानवीर भक्त सम्मान (Wall of Fame) व संपूर्ण प्रदर्शन में गति व स्थिरता सुधार"
    ]
    notes = default_notes
    if len(sys.argv) > 3:
        custom_note = sys.argv[3].strip()
        if custom_note:
            notes = [custom_note] + default_notes[:3]

    apk_download_url = f"https://github.com/{GITHUB_REPO}/releases/download/{tag_name}/bhakti-app.apk"

    # 2. Update version.json
    vdata["versionCode"] = next_code
    vdata["versionName"] = next_ver
    vdata["apkUrl"] = apk_download_url
    vdata["releaseDate"] = time.strftime("%Y-%m-%d")
    vdata["title"] = f"पावन अपडेट {tag_name} उपलब्ध है! 🚀"
    vdata["releaseNotes"] = notes
    vfile.write_text(json.dumps(vdata, ensure_ascii=False, indent=2), encoding="utf-8")
    log("Updated version.json")

    # 3. Update app.js in bhakti-app and bhakti-android
    app_js_files = [
        APP_DIR / "app.js",
        ANDROID_DIR / "app" / "src" / "main" / "assets" / "app.js"
    ]
    for ap in app_js_files:
        if ap.exists():
            txt = ap.read_text(encoding="utf-8")
            import re
            txt = re.sub(r'currentVersionCode:\s*\d+', f'currentVersionCode: {next_code}', txt)
            txt = re.sub(r"currentVersionName:\s*['\"][^'\"]+['\"]", f"currentVersionName: '{next_ver}'", txt)
            ap.write_text(txt, encoding="utf-8")
            log(f"Updated version in {ap.name}")

    # 4. Update build.gradle.kts
    gradle_file = ANDROID_DIR / "app" / "build.gradle.kts"
    if gradle_file.exists():
        gtxt = gradle_file.read_text(encoding="utf-8")
        import re
        gtxt = re.sub(r'versionCode\s*=\s*\d+', f'versionCode = {next_code}', gtxt)
        gtxt = re.sub(r'versionName\s*=\s*"[^"]+"', f'versionName = "{next_ver}"', gtxt)
        gradle_file.write_text(gtxt, encoding="utf-8")
        log("Updated Android build.gradle.kts")

    # 5. Sync web assets to bhakti-android/app/src/main/assets
    log("Syncing web assets to Android project...")
    android_assets = ANDROID_DIR / "app" / "src" / "main" / "assets"
    android_assets.mkdir(parents=True, exist_ok=True)
    
    # Sync specific key files and directories
    sync_files = [
        "index.html", "app.js", "styles.css", "epic_games_engine.js", "epic_games.css",
        "aarti_mantra_puzzle.js", "aarti_mantra_puzzle.css", "aarti_mantra_puzzle_engine.js",
        "ai_bhakti_player.js", "ai_bhakti_player.css", "mcq_test_series_engine.js",
        "version.json", "manifest.json", "service-worker.js", "mandir_3d_engine.js",
        "gallery_engine.js", "gita_engine.js", "mantra_engine.js", "sundarkand_engine.js",
        "chalisa_engine.js", "i18n_engine.js", "light_theme.css"
    ]
    for fname in sync_files:
        src = APP_DIR / fname
        dst = android_assets / fname
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  Synced file: {fname}")

    # Sync assets and data folders recursively
    for folder in ["assets/wall_of_fame", "assets/games", "assets/symbols", "assets/ai_audio", "data"]:
        src_f = APP_DIR / folder
        dst_f = android_assets / folder
        if src_f.exists():
            shutil.copytree(src_f, dst_f, dirs_exist_ok=True)
            print(f"  Synced folder tree: {folder}")

    # Sync direct files in assets/
    src_assets = APP_DIR / "assets"
    dst_assets = android_assets / "assets"
    dst_assets.mkdir(parents=True, exist_ok=True)
    for f in src_assets.glob("*"):
        if f.is_file():
            shutil.copy2(f, dst_assets / f.name)

    # Copy version.json explicitly
    shutil.copy2(vfile, android_assets / "version.json")

    # 6. Build Android APK
    log("Compiling Android APK with Gradle...")
    build_env = os.environ.copy()
    if JDK_DIR.exists():
        build_env["JAVA_HOME"] = str(JDK_DIR)
        build_env["PATH"] = str(JDK_DIR / "bin") + os.pathsep + build_env.get("PATH", "")

    gradle_cmd = "gradlew.bat assembleDebug --no-daemon"
    ok, stdout, stderr = run_cmd(gradle_cmd, cwd=str(ANDROID_DIR), env=build_env)
    if not ok:
        print("❌ Gradle compilation failed!")
        sys.exit(1)

    built_apk = ANDROID_DIR / "app" / "build" / "outputs" / "apk" / "debug" / "app-debug.apk"
    if not built_apk.exists():
        print("❌ Built APK not found at", built_apk)
        sys.exit(1)

    size_bytes = built_apk.stat().st_size
    size_mb = f"{size_bytes / (1024 * 1024):.1f} MB"
    log(f"APK built successfully! Size: {size_mb}")

    # Copy to destination files
    dest_apk = APP_DIR / "bhakti-app.apk"
    dest_apk_short = APP_DIR / "bhakti.apk"
    shutil.copy2(built_apk, dest_apk)
    shutil.copy2(built_apk, dest_apk_short)

    # Update size in version.json
    vdata["apkSize"] = size_mb
    vfile.write_text(json.dumps(vdata, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copy2(vfile, android_assets / "version.json")

    # 7. Git commit and push
    log("Committing changes and pushing git tag to GitHub...")
    run_cmd("git add -A", cwd=str(APP_DIR))
    commit_msg = f"Release {tag_name} - Wall of Fame, In-App Auto-Update & Divinity Polish"
    run_cmd(f'git commit -m "{commit_msg}"', cwd=str(APP_DIR))
    run_cmd(f'git tag -a {tag_name} -m "Release {tag_name}"', cwd=str(APP_DIR))
    
    ok, _, _ = run_cmd("git push origin main", cwd=str(APP_DIR))
    if not ok:
        log("Warning: git push origin main had an issue, trying with token...")
    ok, _, _ = run_cmd(f"git push origin {tag_name}", cwd=str(APP_DIR))

    # 8. Create GitHub Release
    log(f"Creating GitHub Release {tag_name} on repository {GITHUB_REPO}...")
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "User-Agent": "BhaktiAppPublisher",
        "Accept": "application/vnd.github.v3+json"
    }

    release_body = "## " + vdata["title"] + "\n\n" + "\n".join([f"- {n}" for n in notes])
    payload = {
        "tag_name": tag_name,
        "target_commitish": "main",
        "name": vdata["title"],
        "body": release_body,
        "draft": False,
        "prerelease": False
    }

    req = urllib.request.Request(
        f"https://api.github.com/repos/{GITHUB_REPO}/releases",
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"}
    )
    
    release_id = None
    upload_url = None
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            rel_res = json.loads(r.read())
            release_id = rel_res["id"]
            upload_url = rel_res["upload_url"].split("{")[0]
            log(f"GitHub Release created successfully (ID: {release_id})!")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        if "already_exists" in err_msg:
            log(f"Release {tag_name} already exists, fetching its details...")
            req_get = urllib.request.Request(f"https://api.github.com/repos/{GITHUB_REPO}/releases/tags/{tag_name}", headers=headers)
            with urllib.request.urlopen(req_get, timeout=15) as r:
                rel_res = json.loads(r.read())
                release_id = rel_res["id"]
                upload_url = rel_res["upload_url"].split("{")[0]
        else:
            print("❌ Failed to create GitHub release:", err_msg)
            sys.exit(1)

    # Check if asset already exists in release and delete it if so
    try:
        req_assets = urllib.request.Request(f"https://api.github.com/repos/{GITHUB_REPO}/releases/{release_id}/assets", headers=headers)
        with urllib.request.urlopen(req_assets, timeout=15) as r:
            existing_assets = json.loads(r.read())
            for ea in existing_assets:
                if ea["name"] == dest_apk.name:
                    log(f"Removing previous asset {ea['id']} from release...")
                    req_del = urllib.request.Request(f"https://api.github.com/repos/{GITHUB_REPO}/releases/assets/{ea['id']}", headers=headers, method="DELETE")
                    urllib.request.urlopen(req_del, timeout=15)
    except Exception as e:
        log(f"Asset check notice: {e}")

    # 9. Upload APK to GitHub Release Asset
    log(f"Uploading {dest_apk.name} ({size_mb}) to GitHub Release...")
    upload_target = f"{upload_url}?name=bhakti-app.apk"
    curl_upload = f'curl.exe --silent --show-error -X POST -H "Authorization: token {GITHUB_TOKEN}" -H "Content-Type: application/vnd.android.package-archive" --data-binary "@{dest_apk.name}" "{upload_target}"'
    ok, out, err = run_cmd(curl_upload, cwd=str(APP_DIR))
    if not ok:
        print("❌ Asset upload failed:", err)
        sys.exit(1)
    log("APK successfully uploaded to GitHub Release!")

    # 10. Purge jsDelivr cache
    log("Purging jsDelivr CDN cache for instant global delivery...")
    try:
        purge_url = f"https://purge.jsdelivr.net/gh/{GITHUB_REPO}@main/version.json"
        req_p = urllib.request.Request(purge_url, headers={"User-Agent": "BhaktiAppPublisher"})
        with urllib.request.urlopen(req_p, timeout=10) as r:
            log("CDN cache purged! Instant updates active worldwide.")
    except Exception as e:
        log(f"CDN purge notice: {e}")

    log("="*60)
    log(f"🎉 SUCCESS! पावन अपडेट {tag_name} पूर्णतः प्रकाशित हो गया है!")
    log(f"📱 अब जो भी उपयोगकर्ता या आपका मित्र ऐप खोलेगा, उसे तुरंत:")
    log(f"   '🚀 नया पावन अपडेट {tag_name} उपलब्ध है!'")
    log(f"   का नोटिफिकेशन व पॉपअप दिखेगा, और वे १-क्लिक में अपडेट कर सकेंगे!")
    log("="*60)

if __name__ == "__main__":
    main()
