import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

handler_code = """
// Handle Server Response for Settings & Sadhana Vault Synchronization
window.handleSettingsServerResponse = function(response) {
  if (!response) return;
  if (response.status === 'success') {
    const syncTimeStr = response.lastSyncedAt ? new Date(response.lastSyncedAt).toLocaleTimeString('hi-IN', { hour: '2-digit', minute: '2-digit' }) : 'अभी-अभी';
    const tsBadge = document.getElementById('vault-sync-timestamp');
    if (tsBadge) {
      tsBadge.textContent = `🟢 सुरक्षित Sync (अंतिम सिंक: आज ${syncTimeStr})`;
      tsBadge.style.color = '#34D399';
    }
    localStorage.setItem('sanatan_last_synced_at', response.lastSyncedAt || new Date().toISOString());
    
    if (typeof showToast === 'function') {
      showToast(`☁️ ${response.message || 'साधना डेटा क्लाउड वॉल्ट में सुरक्षित!'}`);
    }
    if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
    if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  }
};
"""

if 'window.handleSettingsServerResponse' not in js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write("\n" + handler_code)
    print("✓ Added handleSettingsServerResponse to app.js")
else:
    print("handleSettingsServerResponse already in app.js")

# Bump cache buster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ All files synchronized (v={ts})")
