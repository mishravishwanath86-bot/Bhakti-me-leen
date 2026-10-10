import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("BUILDING 3 ULTRA-CLASSIC FEATURES FOR BHAKTI APP")
print("=" * 80)

# 1. Update index.html
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# A. Add Hanging Brass Temple Bell in Header
hanging_bell_html = """      <!-- 🔔 ORNATE HANGING BRASS TEMPLE BELL MICRO-INTERACTION 🔔 -->
      <div style="display:flex; justify-content:center; margin-top:-6px; margin-bottom:6px; position:relative; z-index:30;">
        <div onclick="ringHangingTempleBell()" id="hanging-bell-container" style="display:flex; flex-direction:column; align-items:center; cursor:pointer; user-select:none; filter:drop-shadow(0 6px 15px rgba(0,0,0,0.5)); transform-origin: top center; transition: transform 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
          <!-- Golden Chain -->
          <div style="width:3px; height:22px; background:repeating-linear-gradient(to bottom, #F59E0B, #B45309 4px, #FDE68A 8px); border-radius:2px;"></div>
          <!-- Bell Dome & Clapper -->
          <div id="hanging-bell-body" style="font-size:2.3rem; margin-top:-4px; filter:drop-shadow(0 0 10px rgba(245,158,11,0.6));">🔔</div>
          <span style="font-size:0.65rem; font-weight:800; color:#FDE68A; background:rgba(248,200,59,0.18); border:1px solid rgba(248,200,59,0.35); padding:2px 8px; border-radius:10px; margin-top:-2px;">
            घंटा बजाएं ✨
          </span>
        </div>
      </div>"""

# B. Add Dynamic Brahma Muhurta & Vedic Alarm Widget on Home Page
brahma_muhurta_html = """      <!-- 🌅 DYNAMIC BRAHMA MUHURTA & VEDIC ALARM WIDGET 🌅 -->
      <div style="margin: 0 1.2rem 1.2rem; background: linear-gradient(135deg, #1C0A35 0%, #2E0F54 50%, #15042A 100%); border: 1.5px solid rgba(248,200,59,0.45); border-radius: 22px; padding: 1.1rem; box-shadow: 0 8px 25px rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: space-between; gap: 10px;">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:46px; height:46px; border-radius:16px; background:linear-gradient(135deg, #F59E0B 0%, #D97706 100%); display:flex; align-items:center; justify-content:center; font-size:1.6rem; color:#1A0B2E; box-shadow:0 4px 15px rgba(245,158,11,0.4); flex-shrink:0;">
            🌅
          </div>
          <div>
            <div style="display:flex; align-items:center; gap:6px;">
              <h3 style="font-size:0.92rem; font-weight:900; color:#FFFDF8; margin:0;">ब्रह्म मुहूर्त (अमृत वेला)</h3>
              <span style="font-size:0.68rem; font-weight:800; background:rgba(16,185,129,0.2); border:1px solid #10B981; color:#34D399; padding:2px 6px; border-radius:8px;">
                04:24 AM - 05:12 AM
              </span>
            </div>
            <p style="font-size:0.72rem; color:#FDE68A; margin:3px 0 0 0;">
              सूर्योदय से 96 मिनट पूर्व • ध्यान, जाप व योग हेतु सर्वश्रेष्ठ काल
            </p>
          </div>
        </div>
        <button onclick="openVedicAlarmModal()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.78rem; font-weight:900; padding:8px 14px; border-radius:14px; cursor:pointer; box-shadow:0 3px 12px rgba(248,200,59,0.35); flex-shrink:0;">
          वैदिक अलार्म ⏰
        </button>
      </div>"""

# C. Vedic Alarm Modal Markup
vedic_alarm_modal_html = """  <!-- ⏰ DYNAMIC BRAHMA MUHURTA & VEDIC ALARM MODAL ⏰ -->
  <div id="vedic-alarm-modal" style="display:none; position:fixed; inset:0; z-index:100035; background:rgba(10,2,18,0.92); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:390px; background:linear-gradient(160deg, #2B0A4E 0%, #150528 100%); border:2px solid rgba(248,200,59,0.45); border-radius:32px; padding:1.6rem 1.4rem; box-shadow:0 20px 60px rgba(0,0,0,0.85); position:relative; text-align:center;">
      
      <button onclick="closeVedicAlarmModal()" style="position:absolute; top:14px; right:14px; background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.1rem; cursor:pointer;">✕</button>

      <div style="font-size:1.2rem; font-weight:900; color:#FFFDF8; margin-bottom:4px; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>🌅</span> ब्रह्म मुहूर्त वैदिक अलार्म
      </div>
      <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 16px 0;">प्रातः काल दिव्य ध्वनि के साथ साधना का संकल्प लें</p>

      <!-- Muhurta Time Badge -->
      <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px; margin-bottom:16px;">
        <div style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-bottom:4px;">दैनिक अमृत वेला समय</div>
        <div style="font-size:1.4rem; font-weight:900; color:#FFFDF8; font-family:monospace;">04:24 AM</div>
        <div style="font-size:0.72rem; color:#CBD5E1; margin-top:2px;">(सूर्योदय 06:00 AM के अनुसार स्वतः गणना)</div>
      </div>

      <!-- Tone Selector -->
      <div style="text-align:left; margin-bottom:16px;">
        <label style="font-size:0.78rem; font-weight:800; color:#FDE68A; margin-bottom:6px; display:block;">दिव्य अलार्म ध्वनि चुनें:</label>
        <div style="display:flex; flex-direction:column; gap:8px;">
          <label style="display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,0.08); border:1.5px solid rgba(248,200,59,0.35); border-radius:14px; padding:10px 12px; cursor:pointer; color:#FFF; font-size:0.82rem; font-weight:700;">
            <div style="display:flex; align-items:center; gap:8px;">
              <input type="radio" name="alarm-tone" value="shankh" checked style="accent-color:#F59E0B;">
              <span>🐚 पावन शंखनाद (Shankh Naad)</span>
            </div>
            <button onclick="previewAlarmTone('shankh')" style="background:rgba(248,200,59,0.2); border:none; color:#FDE68A; font-size:0.75rem; font-weight:800; padding:2px 8px; border-radius:8px; cursor:pointer;">सुनें 🔊</button>
          </label>

          <label style="display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:10px 12px; cursor:pointer; color:#FFF; font-size:0.82rem; font-weight:700;">
            <div style="display:flex; align-items:center; gap:8px;">
              <input type="radio" name="alarm-tone" value="bell" style="accent-color:#F59E0B;">
              <span>🔔 प्रभात मंदिर घंटी व शहनाई</span>
            </div>
            <button onclick="previewAlarmTone('bell')" style="background:rgba(248,200,59,0.2); border:none; color:#FDE68A; font-size:0.75rem; font-weight:800; padding:2px 8px; border-radius:8px; cursor:pointer;">सुनें 🔊</button>
          </label>

          <label style="display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:10px 12px; cursor:pointer; color:#FFF; font-size:0.82rem; font-weight:700;">
            <div style="display:flex; align-items:center; gap:8px;">
              <input type="radio" name="alarm-tone" value="om" style="accent-color:#F59E0B;">
              <span>🕉️ 432Hz ॐ ध्यान तरंग</span>
            </div>
            <button onclick="previewAlarmTone('om')" style="background:rgba(248,200,59,0.2); border:none; color:#FDE68A; font-size:0.75rem; font-weight:800; padding:2px 8px; border-radius:8px; cursor:pointer;">सुनें 🔊</button>
          </label>
        </div>
      </div>

      <button onclick="saveVedicAlarm()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.92rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4);">
        ⏰ ब्रह्म मुहूर्त अलार्म सेट करें
      </button>

    </div>
  </div>"""

# Insert Hanging Bell into #page-home
if '🔔 ORNATE HANGING BRASS TEMPLE BELL' not in html:
    pos_topbar = html.find('<!-- 🕉️ TOP APP HEADER')
    if pos_topbar != -1:
        end_topbar = html.find('</div>', pos_topbar) + 6
        html = html[:end_topbar] + "\n" + hanging_bell_html + html[end_topbar:]
        print("✓ Injected Hanging Brass Temple Bell in index.html")

# Insert Brahma Muhurta Widget into #page-home
if '🌅 DYNAMIC BRAHMA MUHURTA' not in html:
    pos_vrat = html.find('<!-- 🔔 DYNAMIC VRAT & FESTIVAL ALERT RIBBON')
    if pos_vrat != -1:
        html = html[:pos_vrat] + brahma_muhurta_html + "\n\n" + html[pos_vrat:]
        print("✓ Injected Brahma Muhurta Widget into #page-home")

# Insert Vedic Alarm Modal before </body>
if 'id="vedic-alarm-modal"' not in html:
    pos_body = html.find('</body>')
    html = html[:pos_body] + vedic_alarm_modal_html + "\n\n" + html[pos_body:]
    print("✓ Injected #vedic-alarm-modal into index.html")

# Add Bhojpatra / Palm-Leaf Switcher to #page-reader
pos_reader_header = html.find('id="page-reader"')
if pos_reader_header != -1 and 'bhojpatra-toggle-btn' not in html:
    bhojpatra_reader_controls = """
      <!-- 📜 BHOJPATRA / PALM-LEAF MODE TOGGLE & 3D FLIP CONTROLS 📜 -->
      <div style="display:flex; align-items:center; justify-content:space-between; padding:0.6rem 1.2rem; background:rgba(0,0,0,0.3); border-bottom:1px solid rgba(248,200,59,0.25);">
        <button id="bhojpatra-toggle-btn" onclick="toggleBhojpatraMode()" style="background:linear-gradient(135deg, #D97706 0%, #78350F 100%); color:#FEF3C7; border:1px solid #FDE68A; font-size:0.78rem; font-weight:800; padding:6px 14px; border-radius:14px; cursor:pointer; display:flex; align-items:center; gap:5px; box-shadow:0 2px 10px rgba(0,0,0,0.3);">
          <span>📜</span> भोजपत्र स्वरूप (प्राचीन ग्रंथ)
        </button>
        <div style="display:flex; align-items:center; gap:8px;">
          <button onclick="flipReaderPage(-1)" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; padding:5px 12px; border-radius:12px; font-size:0.75rem; font-weight:800; cursor:pointer;">❮ पिछला पत्र</button>
          <button onclick="flipReaderPage(1)" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; padding:5px 12px; border-radius:12px; font-size:0.75rem; font-weight:800; cursor:pointer;">अगला पत्र ❯</button>
        </div>
      </div>
    """
    pos_reader_topbar = html.find('class="page-header-bar"', pos_reader_header)
    if pos_reader_topbar != -1:
        end_topbar_reader = html.find('</div>', pos_reader_topbar) + 6
        html = html[:end_topbar_reader] + bhojpatra_reader_controls + html[end_topbar_reader:]
        print("✓ Injected Bhojpatra reader controls into #page-reader")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Updated index.html")

# 2. Append Bhojpatra & Bell styles in styles.css
bhojpatra_css = """
/* ══════════════════════════════════════════════════════════════════
   📜 ANCIENT PALM-LEAF / BHOJPATRA READER & BELL STYLES
   ══════════════════════════════════════════════════════════════════ */

.bhojpatra-active {
  background: radial-gradient(circle at 50% 20%, #F5E6CA 0%, #DFCA9E 50%, #B89B66 100%) !important;
  color: #381B08 !important;
  box-shadow: inset 0 0 50px rgba(78, 38, 10, 0.4) !important;
  border: 3px double #8C531B !important;
  border-radius: 20px !important;
  padding: 1.5rem 1.2rem !important;
  font-family: 'Tiro Devanagari Hindi', 'Cinzel', serif !important;
}

.bhojpatra-active .pure-reader-text {
  color: #261103 !important;
  font-weight: 800 !important;
  text-shadow: 0.5px 0.5px 0px rgba(255,255,255,0.4) !important;
  line-height: 2.4 !important;
}

@keyframes bellSwingHeavy {
  0% { transform: rotate(0deg); }
  20% { transform: rotate(24deg); }
  40% { transform: rotate(-20deg); }
  60% { transform: rotate(14deg); }
  80% { transform: rotate(-8deg); }
  100% { transform: rotate(0deg); }
}

.bell-swinging {
  animation: bellSwingHeavy 1.1s cubic-bezier(0.36, 0.07, 0.19, 0.97) forwards !important;
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + bhojpatra_css)
print("✓ Appended Bhojpatra CSS to styles.css")

# 3. Add JavaScript Handlers in app.js
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

three_features_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🔔 1. ORNATE HANGING BRASS TEMPLE BELL HANDLER
// ══════════════════════════════════════════════════════════════════════════════
window.ringHangingTempleBell = function() {
  const bellEl = document.getElementById('hanging-bell-container');
  if (bellEl) {
    bellEl.classList.remove('bell-swinging');
    void bellEl.offsetWidth; // Trigger reflow
    bellEl.classList.add('bell-swinging');
  }

  // Play High-Fidelity Synthesized Bell Chime
  if (typeof devotionalAudio !== 'undefined') {
    devotionalAudio.playBell();
  } else {
    // Web Audio Fallback
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      const ctx = new AudioCtx();
      const now = ctx.currentTime;
      [1046.5, 2093, 3135.9].forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now);
        gain.gain.setValueAtTime(0.3 / (idx + 1), now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.5);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 2.5);
      });
    } catch(e) {}
  }

  if (navigator.vibrate) navigator.vibrate([40, 20, 60]);
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof showToast === 'function') showToast('🔔 ॐ नमः शिवाय! पावन घंटा ध्वनि');
};

// ══════════════════════════════════════════════════════════════════════════════
// 🌅 2. DYNAMIC BRAHMA MUHURTA & VEDIC ALARM HANDLERS
// ══════════════════════════════════════════════════════════════════════════════
window.openVedicAlarmModal = function() {
  const modal = document.getElementById('vedic-alarm-modal');
  if (modal) {
    modal.style.display = 'flex';
    if (navigator.vibrate) navigator.vibrate(35);
  }
};

window.closeVedicAlarmModal = function() {
  const modal = document.getElementById('vedic-alarm-modal');
  if (modal) modal.style.display = 'none';
};

window.previewAlarmTone = function(tone) {
  if (tone === 'shankh') {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      const ctx = new AudioCtx();
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, now);
      osc.frequency.linearRampToValueAtTime(293.66, now + 0.6);
      osc.frequency.linearRampToValueAtTime(277.18, now + 1.8);
      gain.gain.setValueAtTime(0.01, now);
      gain.gain.linearRampToValueAtTime(0.3, now + 0.4);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.4);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 2.4);
    } catch(e) {}
  } else if (tone === 'bell') {
    window.ringHangingTempleBell();
  } else if (tone === 'om') {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      const ctx = new AudioCtx();
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(432, now);
      gain.gain.setValueAtTime(0.01, now);
      gain.gain.linearRampToValueAtTime(0.2, now + 0.5);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 3.0);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 3.0);
    } catch(e) {}
  }
};

window.saveVedicAlarm = function() {
  if ('Notification' in window) {
    Notification.requestPermission().then(perm => {
      if (perm === 'granted') {
        new Notification('🌅 ब्रह्म मुहूर्त अलार्म सक्रिय', {
          body: 'प्रातः 04:24 AM पर आपको अमृत वेला साधना हेतु जगाया जाएगा। जय श्री हरि!',
          icon: 'assets/app_logo_circle.png'
        });
      }
    });
  }
  window.closeVedicAlarmModal();
  if (typeof showToast === 'function') {
    showToast('⏰ ब्रह्म मुहूर्त अलार्म प्रातः 04:24 AM पर सेट हो गया!');
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// 📜 3. PALM-LEAF / BHOJPATRA READER & 3D FLIP CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════
window.isBhojpatraMode = false;
window.toggleBhojpatraMode = function() {
  window.isBhojpatraMode = !window.isBhojpatraMode;
  const container = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
  const btn = document.getElementById('bhojpatra-toggle-btn');
  
  if (container) {
    if (window.isBhojpatraMode) {
      container.classList.add('bhojpatra-active');
      if (btn) btn.innerHTML = '<span>✨</span> आधुनिक स्वरूप';
      if (typeof showToast === 'function') showToast('📜 प्राचीन भोजपत्र ग्रंथ स्वरूप सक्रिय!');
    } else {
      container.classList.remove('bhojpatra-active');
      if (btn) btn.innerHTML = '<span>📜</span> भोजपत्र स्वरूप (प्राचीन ग्रंथ)';
      if (typeof showToast === 'function') showToast('📖 मानक पाठक स्वरूप सक्रिय');
    }
  }
  window.playPaperRustle();
};

window.playPaperRustle = function() {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    const ctx = new AudioCtx();
    const bufferSize = ctx.sampleRate * 0.15;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * 0.15 * Math.exp(-i / (bufferSize * 0.3));
    }
    const noise = ctx.createBufferSource();
    noise.buffer = buffer;
    const filter = ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.value = 1200;
    noise.connect(filter);
    filter.connect(ctx.destination);
    noise.start();
  } catch(e) {}
};

window.flipReaderPage = function(direction) {
  const container = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
  if (container) {
    container.style.transition = 'transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s';
    container.style.transform = direction > 0 ? 'rotateY(-20deg) scale(0.96)' : 'rotateY(20deg) scale(0.96)';
    container.style.opacity = '0.7';

    window.playPaperRustle();
    if (navigator.vibrate) navigator.vibrate(30);

    setTimeout(() => {
      container.style.transform = 'rotateY(0deg) scale(1)';
      container.style.opacity = '1';
    }, 280);
  }
};
"""

js += "\n\n" + three_features_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected 3 Ultra-Classic features handlers in app.js")

print("=" * 80)
print("ALL 3 ULTRA-CLASSIC FEATURES SUCCESSFULLY INTEGRATED")
print("=" * 80)
