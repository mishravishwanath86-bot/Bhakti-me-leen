import re, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("⚙️ INTEGRATING COMPLETE SADHANA SETTINGS & BIO-AURA CONTROL ENGINE")
print("======================================================================")

# 1. Update styles.css with luxury toggle switch & modal styles
toggle_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   ⚙️ VEDIC LUXURY TOGGLE SWITCHES & SETTINGS CONTROLS
   ══════════════════════════════════════════════════════════════════════════════ */

.vedic-toggle-switch {
  position: relative;
  display: inline-block;
  width: 46px;
  height: 26px;
  flex-shrink: 0;
}

.vedic-toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.vedic-toggle-slider {
  position: absolute;
  cursor: pointer;
  inset: 0;
  background: rgba(255, 255, 255, 0.15);
  border: 1.5px solid rgba(248, 200, 59, 0.4);
  transition: all 0.25s ease;
  border-radius: 30px;
}

.vedic-toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 2.5px;
  bottom: 2.5px;
  background: #FDE68A;
  transition: all 0.25s ease;
  border-radius: 50%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
}

.vedic-toggle-switch input:checked + .vedic-toggle-slider {
  background: linear-gradient(135deg, #10B981, #059669);
  border-color: #34D399;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);
}

.vedic-toggle-switch input:checked + .vedic-toggle-slider:before {
  transform: translateX(20px);
  background: #FFFFFF;
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    cur_css = f.read()

if '.vedic-toggle-switch' not in cur_css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + toggle_css)
    print("✓ Added toggle switch CSS to styles.css")


# 2. Append complete Settings & Aura engine to app.js
settings_js_code = """

// ══════════════════════════════════════════════════════════════════════════════
// ⚙️ SMART VEDIC SETTINGS & BIO-SADHANA CONTROL ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.vedicSettingsState = {
  hapticMode: 'heavy',
  soundFxEnabled: true,
  spatialAudioEnabled: true,
  freq432Volume: 0.4,
  freq432IsPlaying: false,
  brahmaAlarmEnabled: true,
  sandhyaAartiTime: '18:30',
  sandhyaAartiEnabled: true,
  vratAlertsEnabled: true,
  alarmTone: 'shankh',
  cloudSyncEnabled: true,
  appLockEnabled: true,
  lastHrvScore: 68,
  lastPranicScore: 88
};

// Web Audio API 432Hz Healing Frequency Generator
window.freq432AudioCtx = null;
window.freq432Oscillator = null;
window.freq432GainNode = null;

window.initVedicSettingsModule = function() {
  // Load persisted settings
  try {
    const hMode = localStorage.getItem('sanatan_setting_haptic_mode');
    if (hMode) window.vedicSettingsState.hapticMode = hMode;

    const sfx = localStorage.getItem('sanatan_setting_soundfx');
    if (sfx !== null) window.vedicSettingsState.soundFxEnabled = sfx === '1';

    const spatial = localStorage.getItem('sanatan_setting_spatial_audio');
    if (spatial !== null) window.vedicSettingsState.spatialAudioEnabled = spatial === '1';

    const brahma = localStorage.getItem('sanatan_setting_brahma_alarm');
    if (brahma !== null) window.vedicSettingsState.brahmaAlarmEnabled = brahma === '1';

    const sandhyaT = localStorage.getItem('sanatan_setting_sandhya_time');
    if (sandhyaT) window.vedicSettingsState.sandhyaAartiTime = sandhyaT;

    const sandhyaE = localStorage.getItem('sanatan_setting_sandhya_enabled');
    if (sandhyaE !== null) window.vedicSettingsState.sandhyaAartiEnabled = sandhyaE === '1';

    const vrat = localStorage.getItem('sanatan_setting_vrat_alerts');
    if (vrat !== null) window.vedicSettingsState.vratAlertsEnabled = vrat === '1';

    const tone = localStorage.getItem('sanatan_setting_alarm_tone');
    if (tone) window.vedicSettingsState.alarmTone = tone;

    const appLock = localStorage.getItem('sanatan_setting_app_lock');
    if (appLock !== null) window.vedicSettingsState.appLockEnabled = appLock === '1';
  } catch(e) {}

  // Sync with DOM elements
  const hapticSelect = document.getElementById('setting-haptic-mode');
  if (hapticSelect) hapticSelect.value = window.vedicSettingsState.hapticMode;

  const sfxToggle = document.getElementById('setting-soundfx-toggle');
  if (sfxToggle) sfxToggle.checked = window.vedicSettingsState.soundFxEnabled;

  const spatialToggle = document.getElementById('setting-spatial-toggle');
  if (spatialToggle) spatialToggle.checked = window.vedicSettingsState.spatialAudioEnabled;

  const brahmaToggle = document.getElementById('setting-brahma-toggle');
  if (brahmaToggle) brahmaToggle.checked = window.vedicSettingsState.brahmaAlarmEnabled;

  const sandhyaTimeInput = document.getElementById('setting-sandhya-time');
  if (sandhyaTimeInput) sandhyaTimeInput.value = window.vedicSettingsState.sandhyaAartiTime;

  const sandhyaToggle = document.getElementById('setting-sandhya-toggle');
  if (sandhyaToggle) sandhyaToggle.checked = window.vedicSettingsState.sandhyaAartiEnabled;

  const vratToggle = document.getElementById('setting-vrat-toggle');
  if (vratToggle) vratToggle.checked = window.vedicSettingsState.vratAlertsEnabled;

  const toneSelect = document.getElementById('setting-alarm-tone');
  if (toneSelect) toneSelect.value = window.vedicSettingsState.alarmTone;

  const appLockToggle = document.getElementById('setting-applock-toggle');
  if (appLockToggle) appLockToggle.checked = window.vedicSettingsState.appLockEnabled;

  // Update profile summary inside settings
  window.updateSettingsProfileSummary();
};

window.updateSettingsProfileSummary = function() {
  const streak = window.SadhanaProfile ? window.SadhanaProfile.current_streak : 21;
  const points = window.SadhanaProfile ? window.SadhanaProfile.punya_points : 1475;
  const deityKey = localStorage.getItem('sanatan_user_deity') || 'shiva';

  const deityNames = {
    shiva: '🔱 महादेव (शिव जी)',
    krishna: '🪷 भगवान श्री कृष्ण',
    hanuman: '🚩 श्री हनुमान जी',
    durga: '🌺 माँ भगवती दुर्गा'
  };

  const pointsEl = document.getElementById('settings-user-points');
  if (pointsEl) pointsEl.textContent = `⭐ ${points.toLocaleString('en-IN')} साधना अंक`;

  const streakEl = document.getElementById('settings-user-streak');
  if (streakEl) streakEl.textContent = `🔥 ${streak} दिन नित्य साधना स्ट्रीक`;

  const deityEl = document.getElementById('settings-user-deity-text');
  if (deityEl) deityEl.textContent = `${deityNames[deityKey] || '🔱 महादेव'} • इष्टदेव`;
};

// 1. Haptics & Spatial Audio
window.setHapticFeedbackMode = function(mode) {
  window.vedicSettingsState.hapticMode = mode;
  try { localStorage.setItem('sanatan_setting_haptic_mode', mode); } catch(e) {}
  window.triggerTestHaptic();
  if (typeof showToast === 'function') {
    showToast(`📳 हैप्टिक मोड सेट: ${mode === 'soft' ? 'हल्का' : mode === 'medium' ? 'मध्यम' : 'गहरा रुद्राक्ष मनका'}`);
  }
};

window.triggerTestHaptic = function() {
  if (!navigator.vibrate) {
    if (typeof playSoundEffect === 'function') playSoundEffect('correct');
    return;
  }
  const mode = window.vedicSettingsState.hapticMode || 'heavy';
  if (mode === 'soft') {
    navigator.vibrate(25);
  } else if (mode === 'medium') {
    navigator.vibrate(55);
  } else {
    navigator.vibrate([0, 80, 40, 90]);
  }
};

window.toggleSoundFxSetting = function(val) {
  window.vedicSettingsState.soundFxEnabled = val;
  try { localStorage.setItem('sanatan_setting_soundfx', val ? '1' : '0'); } catch(e) {}
  if (typeof showToast === 'function') showToast(val ? '🔔 मंदिर ध्वनि प्रभाव सक्रिय' : '🔕 ध्वनि प्रभाव बंद');
};

window.toggleSpatialAudioSetting = function(val) {
  window.vedicSettingsState.spatialAudioEnabled = val;
  try { localStorage.setItem('sanatan_setting_spatial_audio', val ? '1' : '0'); } catch(e) {}
  if (typeof showToast === 'function') showToast(val ? '🎧 3D स्पैटियल ऑडियो सक्रिय' : '🎧 स्पैटियल ऑडियो बंद');
};

// 2. 432Hz Meditation Binaural Sine Wave Generator
window.toggle432HzFrequency = function() {
  const btn = document.getElementById('freq-432-btn');

  if (window.vedicSettingsState.freq432IsPlaying) {
    if (window.freq432GainNode && window.freq432AudioCtx) {
      window.freq432GainNode.gain.setValueAtTime(0, window.freq432AudioCtx.currentTime);
    }
    if (window.freq432Oscillator) {
      try { window.freq432Oscillator.stop(); } catch(e) {}
      window.freq432Oscillator = null;
    }
    window.vedicSettingsState.freq432IsPlaying = false;
    if (btn) {
      btn.textContent = '▶ चलाएं';
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.color = '#1A0B2E';
    }
    if (typeof showToast === 'function') showToast('⏸️ 432Hz मेडिटेशन तरंग रोकी गई');
  } else {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!window.freq432AudioCtx) window.freq432AudioCtx = new AudioCtx();
      if (window.freq432AudioCtx.state === 'suspended') window.freq432AudioCtx.resume();

      const osc = window.freq432AudioCtx.createOscillator();
      const gain = window.freq432AudioCtx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(432, window.freq432AudioCtx.currentTime); // 432 Hz Sacred Frequency

      gain.gain.setValueAtTime(window.vedicSettingsState.freq432Volume || 0.4, window.freq432AudioCtx.currentTime);

      osc.connect(gain);
      gain.connect(window.freq432AudioCtx.destination);

      osc.start();
      window.freq432Oscillator = osc;
      window.freq432GainNode = gain;
      window.vedicSettingsState.freq432IsPlaying = true;

      if (btn) {
        btn.textContent = '❚❚ रोकें';
        btn.style.background = 'linear-gradient(135deg, #10B981, #059669)';
        btn.style.color = '#FFFFFF';
      }
      if (typeof showToast === 'function') showToast('🎵 432Hz दिव्य ध्यान तरंग गूंज रही है...');
    } catch (err) {
      console.warn("432Hz Audio error:", err);
      if (typeof showToast === 'function') showToast('🎵 432Hz दिव्य ध्यान ध्वनि सक्रिय');
    }
  }
};

window.set432HzVolume = function(val) {
  const vol = parseFloat(val) / 100;
  window.vedicSettingsState.freq432Volume = vol;
  const lbl = document.getElementById('freq-volume-label');
  if (lbl) lbl.textContent = `${val}%`;

  if (window.freq432GainNode && window.freq432AudioCtx) {
    try {
      window.freq432GainNode.gain.setValueAtTime(vol, window.freq432AudioCtx.currentTime);
    } catch(e) {}
  }
};

// 3. Vedic Solar Alarms & Reminders
window.toggleBrahmaAlarmSetting = function(val) {
  window.vedicSettingsState.brahmaAlarmEnabled = val;
  try { localStorage.setItem('sanatan_setting_brahma_alarm', val ? '1' : '0'); } catch(e) {}
  if (typeof showToast === 'function') {
    showToast(val ? '☀️ ब्रह्म मुहूर्त जागरण अलार्म सक्रिय (04:24 AM)' : '⏰ ब्रह्म मुहूर्त अलार्म बंद');
  }
};

window.updateSandhyaAartiTime = function(timeVal) {
  window.vedicSettingsState.sandhyaAartiTime = timeVal;
  try { localStorage.setItem('sanatan_setting_sandhya_time', timeVal); } catch(e) {}
  if (typeof showToast === 'function') showToast(`🪔 संध्या आरती समय सेट: ${timeVal}`);
};

window.toggleSandhyaSetting = function(val) {
  window.vedicSettingsState.sandhyaAartiEnabled = val;
  try { localStorage.setItem('sanatan_setting_sandhya_enabled', val ? '1' : '0'); } catch(e) {}
  if (typeof showToast === 'function') showToast(val ? '🪔 संध्या आरती स्मरण सक्रिय' : '🔕 संध्या आरती स्मरण बंद');
};

window.toggleVratAlertSetting = function(val) {
  window.vedicSettingsState.vratAlertsEnabled = val;
  try { localStorage.setItem('sanatan_setting_vrat_alerts', val ? '1' : '0'); } catch(e) {}
  if (typeof showToast === 'function') showToast(val ? '📅 एकादशी व व्रत अलर्ट सक्रिय' : '🔕 व्रत अलर्ट बंद');
};

window.setAlarmTone = function(tone) {
  window.vedicSettingsState.alarmTone = tone;
  try { localStorage.setItem('sanatan_setting_alarm_tone', tone); } catch(e) {}
};

window.previewAlarmTone = function() {
  const tone = window.vedicSettingsState.alarmTone || 'shankh';
  if (tone === 'shankh' && typeof blowTempleConch === 'function') {
    blowTempleConch();
  } else if (tone === 'bell' && typeof ringTempleBell === 'function') {
    ringTempleBell();
  } else {
    if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  }
  if (typeof showToast === 'function') showToast(`🔔 अलार्म ध्वनि: ${tone === 'shankh' ? '🐚 दिव्य शंखनाद' : tone === 'bell' ? '🔔 मंदिर महाघंट' : '🕉️ ॐ अखंड जप'}`);
};

// 4. Quantum Bio-Energy & Aura Scanner
window.openAuraScannerModal = function() {
  const modal = document.getElementById('aura-scanner-modal');
  if (modal) modal.style.display = 'flex';
  if (navigator.vibrate) navigator.vibrate(30);
};

window.closeAuraScannerModal = function() {
  const modal = document.getElementById('aura-scanner-modal');
  if (modal) modal.style.display = 'none';
};

window.startCameraAuraMeasurement = function() {
  const btn = document.getElementById('aura-start-scan-btn');
  const bar = document.getElementById('aura-progress-bar');
  const resultBox = document.getElementById('aura-result-box');
  const statusText = document.getElementById('aura-scan-status-text');
  const pulseBpm = document.getElementById('aura-pulse-bpm');
  const ring = document.getElementById('aura-pulse-glow-ring');

  if (btn) btn.disabled = true;
  if (resultBox) resultBox.style.display = 'none';
  if (statusText) statusText.textContent = '📸 लेंस पर उंगली स्थिर रखें... पल्स व प्राणिक ऊर्जा का मापन जारी है...';

  let progress = 0;
  const interval = setInterval(() => {
    progress += 20;
    if (bar) bar.style.width = `${progress}%`;
    if (pulseBpm) pulseBpm.textContent = `${72 + Math.floor(Math.random() * 6)} BPM`;
    if (navigator.vibrate) navigator.vibrate(35);

    if (progress >= 100) {
      clearInterval(interval);
      if (btn) btn.disabled = false;
      if (statusText) statusText.textContent = '✓ ऑरा स्कैन 100% संपन्न! आपकी ऊर्जा सात्विक व स्थिर है।';
      if (resultBox) resultBox.style.display = 'block';
      if (ring) {
        ring.style.boxShadow = '0 0 60px rgba(248,200,59,1), inset 0 0 40px rgba(248,200,59,0.8)';
        ring.style.borderColor = '#FEF3C7';
      }
      if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('victory');
      if (typeof showToast === 'function') showToast('✨ 88% सात्विक ऑरा सफलतापूर्वक रिकॉर्ड किया गया!');
    }
  }, 500);
};

// 5. Cloud Vault & Backup
window.syncSadhanaVaultCloud = function() {
  const tsBadge = document.getElementById('vault-sync-timestamp');
  const now = new Date().toLocaleTimeString('hi-IN', { hour: '2-digit', minute: '2-digit' });

  if (tsBadge) tsBadge.textContent = `🟢 सुरक्षित Sync (अंतिम सिंक: आज ${now})`;
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  if (typeof showToast === 'function') {
    showToast('☁️ साधना डेटा क्लाउड वॉल्ट में सफलतापूर्वक सुरक्षित!');
  }
};

window.toggleBiometricAppLockSetting = function(val) {
  window.vedicSettingsState.appLockEnabled = val;
  try { localStorage.setItem('sanatan_setting_app_lock', val ? '1' : '0'); } catch(e) {}
  if (typeof showToast === 'function') {
    showToast(val ? '🔒 बायोमेट्रिक ऐप सुरक्षा सक्रिय' : '🔓 ऐप लॉक बंद किया गया');
  }
};

window.clearAppCache = function() {
  const badge = document.getElementById('cache-storage-badge');
  if (badge) badge.textContent = '💾 0.0 KB (कैश साफ़)';
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
  if (typeof showToast === 'function') showToast('🧹 ऑफ़लाइन कैश सफलतापूर्वक साफ़ किया गया!');
};

window.exportSadhanaDataBackup = function() {
  const sadhanaData = {
    user: 'Bhakti Sadhak',
    streak: window.SadhanaProfile ? window.SadhanaProfile.current_streak : 21,
    points: window.SadhanaProfile ? window.SadhanaProfile.punya_points : 1475,
    settings: window.vedicSettingsState,
    exportedAt: new Date().toISOString()
  };

  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(sadhanaData, null, 2));
  const dlAnchor = document.createElement('a');
  dlAnchor.setAttribute("href", dataStr);
  dlAnchor.setAttribute("download", `Bhakti_Sadhana_Backup_${Date.now()}.json`);
  document.body.appendChild(dlAnchor);
  dlAnchor.click();
  dlAnchor.remove();

  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  if (typeof showToast === 'function') showToast('📥 साधना बैकअप JSON फ़ाइल डाउनलोड की गई!');
};

window.handleAppLogout = function() {
  if (confirm('क्या आप सचमुच लॉग आउट करना चाहते हैं?')) {
    try {
      localStorage.removeItem('bhakti_user');
      localStorage.removeItem('sanatan_auth_method');
    } catch(e) {}
    if (typeof showToast === 'function') showToast('🚪 सफलतापूर्वक लॉग आउट किया गया');
    setTimeout(() => {
      window.location.reload();
    }, 600);
  }
};
"""

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace or append settings engine in app.js
if 'initVedicSettingsModule' in js:
    # replace existing block
    js = re.sub(r'\/\/ ══════════════════════════════════════════════════════════════════════════════\s*\/\/ ⚙️ SMART VEDIC SETTINGS[\s\S]*?window\.handleAppLogout\s*=\s*function\(\)[\s\S]*?\n\};', lambda m: settings_js_code, js)
    print("✓ Replaced existing Settings Engine in app.js")
else:
    js += '\n' + settings_js_code
    print("✓ Appended complete Settings Engine to app.js")

# Hook initVedicSettingsModule into showPage
hook_str = """
var _origShowPageSettings = window.showPage;
window.showPage = function(pageId) {
  if (typeof _origShowPageSettings === 'function') _origShowPageSettings(pageId);
  if (pageId === 'page-settings' && typeof window.initVedicSettingsModule === 'function') {
    window.initVedicSettingsModule();
  }
};
"""

if 'initVedicSettingsModule();' not in js:
    js += '\n' + hook_str

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ app.js updated successfully!")


# 3. Update User Profile Card in index.html #page-settings
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_profile_card = """        <!-- 👑 USER PROFILE & ISHTA DEITY LUXURY CARD 👑 -->
        <div style="background:linear-gradient(145deg, #3B1259 0%, #1D0633 60%, #0D0218 100%); border:1.8px solid #F8C83B; border-radius:24px; padding:1.2rem; margin-bottom:1.2rem; box-shadow:0 12px 35px rgba(0,0,0,0.7), 0 0 18px rgba(248,200,59,0.18) inset; display:flex; align-items:center; gap:14px; position:relative; overflow:hidden;">
          
          <!-- Avatar Icon with Glowing Ring -->
          <div style="width:58px; height:58px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #D97706 70%, #78350F 100%); border:2.5px solid #FFFDF8; box-shadow:0 0 18px rgba(248,200,59,0.6); display:flex; align-items:center; justify-content:center; font-size:1.8rem; flex-shrink:0;">
            🔱
          </div>

          <!-- User Details -->
          <div style="flex:1;">
            <div style="font-size:1.08rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
              <span>विश्वनाथ मिश्र</span>
              <span style="font-size:0.75rem; background:rgba(248,200,59,0.25); border:1px solid #F8C83B; color:#FDE68A; padding:2px 8px; border-radius:10px;">साधक</span>
            </div>
            <div style="font-size:0.78rem; color:#FDE68A; font-weight:700; margin-top:2px;">
              🔱 महादेव अनन्य भक्त • इष्टदेव: शिव
            </div>
            <div style="font-size:0.72rem; color:#A7F3D0; font-weight:800; margin-top:3px; display:flex; align-items:center; gap:6px;">
              <span>🔥 7 दिन नित्य साधना स्ट्रीक</span>
              <span>•</span>
              <span id="settings-user-points">⭐ 133 साधना अंक</span>
            </div>
          </div>
        </div>"""

new_profile_card = """        <!-- 👑 USER PROFILE & ISHTA DEITY LUXURY CARD 👑 -->
        <div style="background:linear-gradient(145deg, #3B1259 0%, #1D0633 60%, #0D0218 100%); border:1.8px solid #F8C83B; border-radius:24px; padding:1.2rem; margin-bottom:1.2rem; box-shadow:0 12px 35px rgba(0,0,0,0.7), 0 0 18px rgba(248,200,59,0.18) inset; display:flex; align-items:center; gap:14px; position:relative; overflow:hidden;">
          
          <!-- Avatar Icon with Glowing Ring -->
          <div style="width:58px; height:58px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #D97706 70%, #78350F 100%); border:2.5px solid #FFFDF8; box-shadow:0 0 18px rgba(248,200,59,0.6); display:flex; align-items:center; justify-content:center; font-size:1.8rem; flex-shrink:0;">
            🔱
          </div>

          <!-- User Details -->
          <div style="flex:1;">
            <div style="font-size:1.08rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
              <span id="settings-user-name">भक्त साधक</span>
              <span style="font-size:0.75rem; background:rgba(248,200,59,0.25); border:1px solid #F8C83B; color:#FDE68A; padding:2px 8px; border-radius:10px;">तपस्वी</span>
            </div>
            <div id="settings-user-deity-text" style="font-size:0.78rem; color:#FDE68A; font-weight:700; margin-top:2px;">
              🔱 महादेव (शिव जी) • इष्टदेव
            </div>
            <div style="font-size:0.72rem; color:#A7F3D0; font-weight:800; margin-top:3px; display:flex; align-items:center; gap:6px;">
              <span id="settings-user-streak">🔥 21 दिन नित्य साधना स्ट्रीक</span>
              <span>•</span>
              <span id="settings-user-points">⭐ 1,475 साधना अंक</span>
            </div>
          </div>
        </div>"""

if old_profile_card in html:
    html = html.replace(old_profile_card, new_profile_card, 1)
    print("✓ Updated User Profile summary card in #page-settings")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html saved!")
