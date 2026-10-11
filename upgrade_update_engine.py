import re
from pathlib import Path

NEW_UPDATE_ENGINE = '''window.APP_UPDATE_CONFIG = {
  currentVersionCode: 8,
  currentVersionName: '1.7.0',
  manifestUrls: [
    'https://cdn.jsdelivr.net/gh/mishravishwanath86-bot/Bhakti-me-leen@main/version.json',
    'https://api.github.com/repos/mishravishwanath86-bot/Bhakti-me-leen/contents/version.json',
    'https://api.github.com/repos/mishravishwanath86-bot/Bhakti-me-leen/releases/latest',
    'https://raw.githubusercontent.com/mishravishwanath86-bot/Bhakti-me-leen/main/version.json'
  ],
  downloadUrl: 'https://github.com/mishravishwanath86-bot/Bhakti-me-leen/releases/latest/download/bhakti-app.apk',
  latestReleaseInfo: null,
  isChecking: false
};

window.checkForAppUpdates = async function(isManualUserCheck = false) {
  if (window.APP_UPDATE_CONFIG.isChecking) return;
  window.APP_UPDATE_CONFIG.isChecking = true;

  if (isManualUserCheck && typeof showToast === 'function') {
    showToast('🔄 नए अपडेट की जांच हो रही है...');
  }

  let updateData = null;

  for (const endpoint of window.APP_UPDATE_CONFIG.manifestUrls) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 4500);
      const cacheBust = endpoint.includes('?') ? '&_t=' + Date.now() : '?_t=' + Date.now();

      const resp = await fetch(endpoint + cacheBust, {
        signal: controller.signal,
        headers: { 'Accept': 'application/json' }
      });
      clearTimeout(timeoutId);

      if (!resp.ok) continue;
      const raw = await resp.json();

      // Case 1: GitHub /contents/ API (base64 payload)
      if (raw && raw.content && raw.encoding === 'base64') {
        try {
          const decodedStr = decodeURIComponent(escape(atob(raw.content.replace(/\\s/g, ''))));
          updateData = JSON.parse(decodedStr);
          if (updateData && updateData.versionCode) break;
        } catch (_) {}
      }
      // Case 2: Direct version.json (jsDelivr or Raw GitHub)
      else if (raw && raw.versionCode) {
        updateData = raw;
        break;
      }
      // Case 3: GitHub /releases/latest API
      else if (raw && raw.tag_name) {
        const apkAsset = Array.isArray(raw.assets) ? raw.assets.find(a => a.name && a.name.endsWith('.apk')) : null;
        const tagVer = raw.tag_name.replace(/^v/, '');
        const verNum = parseInt(tagVer.replace(/[^0-9]/g, '') || '0', 10);
        updateData = {
          versionCode: verNum > 0 ? verNum : 999,
          versionName: tagVer,
          apkUrl: apkAsset ? apkAsset.browser_download_url : `https://github.com/mishravishwanath86-bot/Bhakti-me-leen/releases/download/${raw.tag_name}/bhakti-app.apk`,
          title: raw.name || `पावन अपडेट ${raw.tag_name} उपलब्ध है! 🚀`,
          releaseNotes: raw.body ? raw.body.split('\\n').map(l => l.trim()).filter(l => l.length > 0) : ['समस्त पावन फीचर्स व सुधार'],
          forceUpdate: false
        };
        break;
      }
    } catch (e) {
      // Endpoint timed out or blocked by ISP; continue to next mirror
    }
  }

  window.APP_UPDATE_CONFIG.isChecking = false;

  if (!updateData) {
    console.log('[UpdateChecker] Offline or mirrors unreachable');
    if (isManualUserCheck && typeof showToast === 'function') {
      showToast(`ℹ️ वर्तमान संस्करण: v${window.APP_UPDATE_CONFIG.currentVersionName} (इंटरनेट उपलब्ध होने पर पुनः जांचें)`);
    }
    return;
  }

  window.APP_UPDATE_CONFIG.latestReleaseInfo = updateData;
  if (updateData.apkUrl) {
    window.APP_UPDATE_CONFIG.downloadUrl = updateData.apkUrl;
  }

  const remoteCode = parseInt(updateData.versionCode || 0, 10);
  const currentCode = window.APP_UPDATE_CONFIG.currentVersionCode;
  const isNewer = remoteCode > currentCode || (
    updateData.versionName && 
    updateData.versionName !== window.APP_UPDATE_CONFIG.currentVersionName && 
    remoteCode >= currentCode
  );

  if (isNewer) {
    // 1. Show Red Badge in Drawer and Settings
    const badges = document.querySelectorAll('#update-badge, .update-badge');
    badges.forEach(b => { b.style.display = 'inline-block'; });

    // 2. Show persistent Top Update Notification Banner
    const topBanner = document.getElementById('app-update-top-banner');
    const bannerTag = document.getElementById('banner-version-tag');
    if (topBanner) {
      if (bannerTag && updateData.versionName) bannerTag.textContent = 'v' + updateData.versionName;
      topBanner.style.display = 'flex';
    }

    // 3. Open full modal popup
    window.openUpdateModal(updateData);
  } else {
    if (isManualUserCheck && typeof showToast === 'function') {
      showToast(`✅ आपका ऐप नवीनतम संस्करण पर है (v${window.APP_UPDATE_CONFIG.currentVersionName})!`);
    }
  }
};

window.openUpdateModal = function(data) {
  const modal = document.getElementById('app-update-modal');
  if (!modal) return;

  const versionTag = document.getElementById('update-version-tag');
  if (versionTag && data.versionName) versionTag.textContent = 'v' + data.versionName;

  const titleEl = document.getElementById('update-title-text');
  if (titleEl && data.title) titleEl.textContent = data.title;

  const notesList = document.getElementById('update-notes-list');
  if (notesList && Array.isArray(data.releaseNotes)) {
    notesList.innerHTML = data.releaseNotes.map(n => `<li>${n}</li>`).join('');
  }

  if (data.apkUrl) {
    window.APP_UPDATE_CONFIG.downloadUrl = data.apkUrl;
  }

  const dwnBtn = document.getElementById('update-download-btn');
  if (dwnBtn && data.apkSize) {
    dwnBtn.innerHTML = `<span>📲</span> अभी अपडेट डाउनलोड करें (${data.apkSize}) ➔`;
  }

  const laterBtn = document.getElementById('update-later-btn');
  const closeBtn = document.getElementById('update-modal-close-btn');
  if (data.forceUpdate) {
    if (laterBtn) laterBtn.style.display = 'none';
    if (closeBtn) closeBtn.style.display = 'none';
  } else {
    if (laterBtn) laterBtn.style.display = 'block';
    if (closeBtn) closeBtn.style.display = 'flex';
  }

  modal.style.display = 'flex';
  if (navigator.vibrate) navigator.vibrate([40, 30, 80]);
  if (typeof showToast === 'function') {
    showToast('🚀 नया पावन अपडेट v' + (data.versionName || '1.8.0') + ' उपलब्ध है!');
  }
};

window.closeUpdateModal = function() {
  const modal = document.getElementById('app-update-modal');
  if (modal) modal.style.display = 'none';
};

window.triggerApkDownload = function() {
  const url = window.APP_UPDATE_CONFIG.downloadUrl;
  if (!url) return;

  if (typeof showToast === 'function') showToast('📥 अपडेट डाउनलोड शुरू हो रहा है...');

  if (window.AndroidBridge && typeof window.AndroidBridge.downloadApk === 'function') {
    window.AndroidBridge.downloadApk(url);
  } else {
    window.open(url, '_system');
  }
};

// Automatic silent background check on launch
setTimeout(() => {
  window.checkForAppUpdates(false);
}, 2000);

// Check again whenever app comes back to foreground
document.addEventListener('visibilitychange', () => {
  if (!document.hidden) {
    window.checkForAppUpdates(false);
  }
});
window.addEventListener('focus', () => {
  window.checkForAppUpdates(false);
});'''

app_js_paths = [
    Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js"),
    Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-android\app\src\main\assets\app.js")
]

for p in app_js_paths:
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    start_marker = "window.APP_UPDATE_CONFIG = {"
    end_marker = "// 🔐 PURE SACRED AUTHENTICATION ENGINE"
    
    start_pos = text.find(start_marker)
    end_pos = text.find(end_marker)
    
    if start_pos != -1 and end_pos != -1:
        # Find comments right before end_marker
        comment_header = "// ═"
        prev_comment_pos = text.rfind(comment_header, start_pos, end_pos)
        if prev_comment_pos != -1:
            end_pos = prev_comment_pos
            
        new_text = text[:start_pos] + NEW_UPDATE_ENGINE + "\n\n\n" + text[end_pos:]
        p.write_text(new_text, encoding="utf-8")
        print(f"Updated {p} successfully!")
    else:
        print(f"Markers not found in {p}")
