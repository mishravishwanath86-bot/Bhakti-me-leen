import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1.1 Add 24x7 Live Bhakti Radio Card to Home Page right below Kalyan Kund Card
live_radio_card_html = """
      <!-- 📻 24x7 LIVE DIVINE BHAKTI RADIO (अखंड भक्ति रेडियो) 📻 -->
      <div id="home-live-radio-card" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(145deg, #2A0D4E 0%, #150628 60%, #0B0116 100%); border: 1.5px solid rgba(248,200,59,0.4); border-radius: 22px; padding: 1.2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.6), 0 0 15px rgba(248,200,59,0.1) inset; position:relative; overflow:hidden;">
        
        <!-- Live Glowing Badge & Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div style="font-size:1rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.3rem;">📻</span>
            <span>24×7 लाइव भक्ति रेडियो</span>
          </div>
          <div style="display:flex; align-items:center; gap:6px; background:rgba(239,68,68,0.2); border:1px solid #EF4444; padding:3px 10px; border-radius:12px;">
            <span style="width:8px; height:8px; background:#EF4444; border-radius:50%; box-shadow:0 0 8px #EF4444; animation:pulse 1.5s infinite;"></span>
            <span style="font-size:0.72rem; font-weight:900; color:#F87171; letter-spacing:0.5px;">LIVE 24x7</span>
          </div>
        </div>

        <!-- Station Info & Animated Wave -->
        <div style="display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); border-radius:16px; padding:10px 14px; margin-bottom:12px;">
          <div style="display:flex; align-items:center; gap:10px;">
            <div id="radio-disc-icon" style="width:42px; height:42px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 80%); border:2px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:1.2rem; box-shadow:0 0 12px rgba(248,200,59,0.4);">
              🎶
            </div>
            <div>
              <div id="radio-station-title" style="font-size:0.92rem; font-weight:900; color:#FFFDF8;">
                🌸 दिव्य भजन तरंग
              </div>
              <div id="radio-track-now" style="font-size:0.75rem; color:#FDE68A; font-weight:700;">
                अखंड मधुर भजन एवं संकीर्तन
              </div>
            </div>
          </div>

          <!-- Play / Pause Button -->
          <button id="radio-play-btn" onclick="toggleLiveRadioPlayback()" style="width:42px; height:42px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 15px rgba(248,200,59,0.4); flex-shrink:0; transition:transform 0.2s;">
            ▶
          </button>
        </div>

        <!-- Station Selector Channels -->
        <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
          <button onclick="switchRadioChannel('bhajan', '🌸 दिव्य भजन तरंग', 'अखंड मधुर भजन एवं संकीर्तन', this)" class="radio-chan-btn active" style="padding:6px 4px; border-radius:10px; font-size:0.72rem; font-weight:800; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; text-align:center; white-space:nowrap;">
            🌸 भजन
          </button>
          <button onclick="switchRadioChannel('mantra', '🕉️ अखंड महामंत्र', 'गायत्री व महामृत्युंजय जाप', this)" class="radio-chan-btn" style="padding:6px 4px; border-radius:10px; font-size:0.72rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            🕉️ मंत्र
          </button>
          <button onclick="switchRadioChannel('katha', '📖 अमृत रामकथा', 'पावन श्रीराम चरित मानस रस', this)" class="radio-chan-btn" style="padding:6px 4px; border-radius:10px; font-size:0.72rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            📖 कथा
          </button>
          <button onclick="switchRadioChannel('aarti', '🪔 नित्य आरती धाम', 'संध्या व प्रातः कालीन दिव्य आरती', this)" class="radio-chan-btn" style="padding:6px 4px; border-radius:10px; font-size:0.72rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            🪔 आरती
          </button>
        </div>

      </div>"""

# Insert Live Radio Card right after Kalyan Kund
kk_marker = 'id="kalyan-kund-cta-btn"'
if kk_marker in html and 'id="home-live-radio-card"' not in html:
    idx = html.find('</div>', html.find(kk_marker)) + 6
    html = html[:idx] + "\n" + live_radio_card_html + html[idx:]
    print("✓ Added 24x7 Live Bhakti Radio Card to Home Page")

# 1.2 Update the Radio Button options in the Sankalp Modal to be prominent, high-contrast, crystal-clear!
old_sankalp_radio = """        <!-- Field 3: Sankalp Purpose -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            संकल्प उद्देश्य:
          </label>
          <div style="display:flex; gap:6px;">
            <label style="flex:1; background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); border-radius:10px; padding:6px 8px; font-size:0.72rem; color:#FFF; font-weight:700; display:flex; align-items:center; gap:4px; cursor:pointer;">
              <input type="radio" name="sankalp_purpose" value="स्वास्थ्य" checked style="accent-color:#F8C83B;" />
              स्वास्थ्य व दीर्घायु
            </label>
            <label style="flex:1; background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); border-radius:10px; padding:6px 8px; font-size:0.72rem; color:#FFF; font-weight:700; display:flex; align-items:center; gap:4px; cursor:pointer;">
              <input type="radio" name="sankalp_purpose" value="परिवार शांति" style="accent-color:#F8C83B;" />
              परिवार शांति व समृद्धि
            </label>
          </div>
        </div>"""

new_sankalp_radio = """        <!-- Field 3: Sankalp Purpose (Prominent Radio Option Selector) -->
        <div>
          <label style="font-size:0.78rem; font-weight:900; color:#FDE68A; display:flex; align-items:center; gap:5px; margin-bottom:6px;">
            <span>🔘</span> संकल्प उद्देश्य (Radio Options):
          </label>
          <div style="display:flex; flex-direction:column; gap:8px;">
            
            <label class="sankalp-radio-card active" onclick="selectSankalpRadio(this)" style="background:rgba(248,200,59,0.18); border:1.5px solid #F8C83B; border-radius:12px; padding:9px 12px; font-size:0.84rem; color:#FFFDF8; font-weight:800; display:flex; align-items:center; justify-content:space-between; cursor:pointer; box-shadow:0 0 10px rgba(248,200,59,0.2);">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:1.1rem;">🌿</span>
                <span>स्वास्थ्य एवं दीर्घायु</span>
              </div>
              <input type="radio" name="sankalp_purpose" value="स्वास्थ्य" checked style="accent-color:#F8C83B; width:18px; height:18px; cursor:pointer;" />
            </label>

            <label class="sankalp-radio-card" onclick="selectSankalpRadio(this)" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.18); border-radius:12px; padding:9px 12px; font-size:0.84rem; color:#FFFDF8; font-weight:800; display:flex; align-items:center; justify-content:space-between; cursor:pointer;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:1.1rem;">🕊️</span>
                <span>परिवार शांति व समृद्धि</span>
              </div>
              <input type="radio" name="sankalp_purpose" value="परिवार शांति" style="accent-color:#F8C83B; width:18px; height:18px; cursor:pointer;" />
            </label>

            <label class="sankalp-radio-card" onclick="selectSankalpRadio(this)" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.18); border-radius:12px; padding:9px 12px; font-size:0.84rem; color:#FFFDF8; font-weight:800; display:flex; align-items:center; justify-content:space-between; cursor:pointer;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:1.1rem;">🎯</span>
                <span>मनोकामना सिद्धि व संकट निवारण</span>
              </div>
              <input type="radio" name="sankalp_purpose" value="मनोकामना सिद्धि" style="accent-color:#F8C83B; width:18px; height:18px; cursor:pointer;" />
            </label>

          </div>
        </div>"""

if old_sankalp_radio in html:
    html = html.replace(old_sankalp_radio, new_sankalp_radio, 1)

# Bump version query string
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with Live Radio Card and Prominent Radio Options (v={ts})")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

live_radio_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 📻 24x7 LIVE BHAKTI RADIO & SANKALP RADIO CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.isLiveRadioPlaying = false;
window.currentRadioChannel = 'bhajan';
window.radioAudioElement = new Audio();

window.radioChannelStreams = {
  'bhajan': 'assets/audio/shree_ganesh_aarti.mp3',
  'mantra': 'assets/audio/shree_ganesh_aarti.mp3',
  'katha': 'assets/audio/shree_ganesh_aarti.mp3',
  'aarti': 'assets/audio/shree_ganesh_aarti.mp3'
};

window.toggleLiveRadioPlayback = function() {
  const btn = document.getElementById('radio-play-btn');
  const disc = document.getElementById('radio-disc-icon');

  if (window.isLiveRadioPlaying) {
    window.radioAudioElement.pause();
    window.isLiveRadioPlaying = false;
    if (btn) btn.innerHTML = '▶';
    if (disc) disc.style.animation = 'none';
    if (typeof showToast === 'function') showToast('⏸️ लाइव रेडियो रोका गया');
  } else {
    // Pick active audio stream
    const src = window.radioChannelStreams[window.currentRadioChannel] || 'assets/audio/shree_ganesh_aarti.mp3';
    window.radioAudioElement.src = src;
    window.radioAudioElement.play().catch(() => {});
    window.isLiveRadioPlaying = true;
    if (btn) btn.innerHTML = '❚❚';
    if (disc) disc.style.animation = 'spinSlow 4s linear infinite';
    if (typeof showToast === 'function') showToast('📻 24×7 लाइव भक्ति रेडियो बज रहा है...');
  }
};

window.switchRadioChannel = function(chanKey, title, sub, btnEl) {
  window.currentRadioChannel = chanKey;
  
  const titleEl = document.getElementById('radio-station-title');
  const subEl = document.getElementById('radio-track-now');

  if (titleEl) titleEl.textContent = title;
  if (subEl) subEl.textContent = sub;

  document.querySelectorAll('.radio-chan-btn').forEach(b => {
    b.classList.remove('active');
    b.style.background = 'rgba(255,255,255,0.08)';
    b.style.color = '#CBD5E1';
    b.style.border = '1px solid rgba(255,255,255,0.15)';
  });

  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
  }

  if (window.isLiveRadioPlaying) {
    window.radioAudioElement.src = window.radioChannelStreams[chanKey] || 'assets/audio/shree_ganesh_aarti.mp3';
    window.radioAudioElement.play().catch(() => {});
  }
};

// Interactive Radio card selector in Sankalp Modal
window.selectSankalpRadio = function(labelEl) {
  document.querySelectorAll('.sankalp-radio-card').forEach(c => {
    c.classList.remove('active');
    c.style.background = 'rgba(255,255,255,0.06)';
    c.style.borderColor = 'rgba(255,255,255,0.18)';
    c.style.boxShadow = 'none';
    const r = c.querySelector('input[type="radio"]');
    if (r) r.checked = false;
  });

  if (labelEl) {
    labelEl.classList.add('active');
    labelEl.style.background = 'rgba(248,200,59,0.18)';
    labelEl.style.borderColor = '#F8C83B';
    labelEl.style.boxShadow = '0 0 10px rgba(248,200,59,0.2)';
    const r = labelEl.querySelector('input[type="radio"]');
    if (r) r.checked = true;
  }
};
"""

js += "\n\n" + live_radio_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Updated app.js with Live Radio Engine & Sankalp Radio Selectors")
