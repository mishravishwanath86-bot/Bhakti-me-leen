import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html Radio Card UI with Live Sound Wave Visualizer
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

rich_radio_card_html = """      <!-- 📻 24x7 LIVE DIVINE BHAKTI RADIO (अखंड भक्ति रेडियो) 📻 -->
      <div id="home-live-radio-card" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(145deg, #2A0D4E 0%, #150628 60%, #0B0116 100%); border: 1.5px solid rgba(248,200,59,0.45); border-radius: 24px; padding: 1.2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 15px rgba(248,200,59,0.12) inset; position:relative; overflow:hidden;">
        
        <!-- Live Glowing Badge & Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="font-size:1.02rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.35rem;">📻</span>
            <span>24×7 लाइव भक्ति रेडियो</span>
          </div>
          <div id="radio-live-status-badge" style="display:flex; align-items:center; gap:6px; background:rgba(239,68,68,0.2); border:1.2px solid #EF4444; padding:3px 10px; border-radius:12px;">
            <span id="radio-pulse-dot" style="width:8px; height:8px; background:#EF4444; border-radius:50%; box-shadow:0 0 8px #EF4444;"></span>
            <span id="radio-live-text" style="font-size:0.72rem; font-weight:900; color:#F87171; letter-spacing:0.5px;">24×7 LIVE</span>
          </div>
        </div>

        <!-- Station Info & Animated Wave Box -->
        <div style="display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:11px 14px; margin-bottom:12px;">
          
          <div style="display:flex; align-items:center; gap:12px; flex:1;">
            <!-- Spinning Disc Icon -->
            <div id="radio-disc-icon" style="width:44px; height:44px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 70%, #78350F 100%); border:2px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:1.3rem; box-shadow:0 0 14px rgba(248,200,59,0.45); flex-shrink:0;">
              🎶
            </div>

            <!-- Station Title & Subtitle -->
            <div style="flex:1;">
              <div id="radio-station-title" style="font-size:0.95rem; font-weight:900; color:#FFFDF8; line-height:1.2;">
                🌸 दिव्य भजन तरंग
              </div>
              <div id="radio-track-now" style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-top:2px;">
                अच्युतम केशवम कृष्ण दामोदरम
              </div>

              <!-- Animated Equalizer Sound Bars -->
              <div id="radio-sound-bars" style="display:none; align-items:flex-end; gap:3px; height:12px; margin-top:4px;">
                <span style="width:3px; height:100%; background:#10B981; border-radius:2px; animation:bounceBar 0.8s infinite ease-in-out;"></span>
                <span style="width:3px; height:60%; background:#F59E0B; border-radius:2px; animation:bounceBar 0.6s infinite ease-in-out 0.2s;"></span>
                <span style="width:3px; height:80%; background:#10B981; border-radius:2px; animation:bounceBar 0.9s infinite ease-in-out 0.4s;"></span>
                <span style="width:3px; height:40%; background:#F59E0B; border-radius:2px; animation:bounceBar 0.5s infinite ease-in-out 0.1s;"></span>
                <span style="width:3px; height:90%; background:#10B981; border-radius:2px; animation:bounceBar 0.7s infinite ease-in-out 0.3s;"></span>
              </div>
            </div>
          </div>

          <!-- Large Glowing Play / Pause Button -->
          <button id="radio-play-btn" onclick="toggleLiveRadioPlayback()" title="रेडियो बजाएं / रोकें" style="width:48px; height:48px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; font-size:1.3rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 18px rgba(248,200,59,0.5); flex-shrink:0; transition:transform 0.15s ease;">
            ▶
          </button>
        </div>

        <!-- 4 Station Selector Channels -->
        <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
          <button onclick="switchRadioChannel('bhajan', '🌸 दिव्य भजन तरंग', 'अच्युतम केशवम कृष्ण दामोदरम', this)" class="radio-chan-btn active" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; text-align:center; white-space:nowrap;">
            🌸 भजन
          </button>
          <button onclick="switchRadioChannel('mantra', '🕉️ अखंड महामंत्र', 'भगवान शिव महिमा व महामृत्युंजय', this)" class="radio-chan-btn" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            🕉️ मंत्र
          </button>
          <button onclick="switchRadioChannel('katha', '📖 अमृत रामकथा', 'पावन श्रीराम चरित मानस रस', this)" class="radio-chan-btn" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            📖 कथा
          </button>
          <button onclick="switchRadioChannel('aarti', '🪔 नित्य आरती धाम', 'श्री सत्यनारायण पावन कथा व आरती', this)" class="radio-chan-btn" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            🪔 आरती
          </button>
        </div>

      </div>"""

# Replace in index.html
s_rad = html.find('<!-- 📻 24x7 LIVE DIVINE BHAKTI RADIO')
if s_rad != -1:
    e_rad = html.find('<!-- 🪔 NITYA AARTI COLLECTION CARDS', s_rad)
    if e_rad == -1:
        e_rad = html.find('<!--', s_rad + 40)
    html = html[:s_rad] + rich_radio_card_html + "\n\n      " + html[e_rad:]

# Add bounceBar animation in CSS if not present
if '@keyframes bounceBar' not in html:
    css_anim = """
<style>
@keyframes bounceBar {
  0%, 100% { height: 20%; }
  50% { height: 100%; }
}
@keyframes pulseGlow {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}
</style>
"""
    html = html.replace('</head>', css_anim + "\n</head>")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Updated index.html with Animated Sound Wave Visualizer & Radio UI")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_live_radio_js = """// ══════════════════════════════════════════════════════════════════════════════
// 📻 24x7 LIVE BHAKTI RADIO CONTROLLER (With Real MP3 Audio Streams & Loops)
// ══════════════════════════════════════════════════════════════════════════════

window.isLiveRadioPlaying = false;
window.currentRadioChannel = 'bhajan';

// Create dedicated radio audio player with audio context settings
if (!window.radioAudioElement) {
  window.radioAudioElement = new Audio();
}

window.radioChannelStreams = {
  'bhajan': 'assets/audio/bhajan_achyutam_keshavam.mp3',
  'mantra': 'assets/audio/katha_shiva.mp3',
  'katha': 'assets/audio/katha_ramayana.mp3',
  'aarti': 'assets/audio/katha_satyanarayan.mp3'
};

// Set audio loop so radio never stops!
window.radioAudioElement.loop = true;

// Audio Event Handlers
window.radioAudioElement.onplay = function() {
  window.isLiveRadioPlaying = true;
  window.updateRadioUIState(true);
};

window.radioAudioElement.onpause = function() {
  window.isLiveRadioPlaying = false;
  window.updateRadioUIState(false);
};

window.radioAudioElement.onerror = function(e) {
  console.warn("Radio audio error:", e);
  // Fallback to local bhajan
  if (window.radioAudioElement.src.indexOf('bhajan_achyutam_keshavam.mp3') === -1) {
    window.radioAudioElement.src = 'assets/audio/bhajan_achyutam_keshavam.mp3';
    window.radioAudioElement.play().catch(() => {});
  }
};

window.updateRadioUIState = function(isPlaying) {
  const btn = document.getElementById('radio-play-btn');
  const disc = document.getElementById('radio-disc-icon');
  const bars = document.getElementById('radio-sound-bars');
  const badge = document.getElementById('radio-live-status-badge');
  const liveText = document.getElementById('radio-live-text');

  if (isPlaying) {
    if (btn) btn.innerHTML = '❚❚';
    if (disc) disc.style.animation = 'spinSlow 3s linear infinite';
    if (bars) bars.style.display = 'flex';
    if (badge) {
      badge.style.background = 'rgba(16, 185, 129, 0.25)';
      badge.style.borderColor = '#10B981';
    }
    if (liveText) {
      liveText.textContent = 'प्रसारण चालू 🔴';
      liveText.style.color = '#34D399';
    }
  } else {
    if (btn) btn.innerHTML = '▶';
    if (disc) disc.style.animation = 'none';
    if (bars) bars.style.display = 'none';
    if (badge) {
      badge.style.background = 'rgba(239, 68, 68, 0.2)';
      badge.style.borderColor = '#EF4444';
    }
    if (liveText) {
      liveText.textContent = '24×7 LIVE';
      liveText.style.color = '#F87171';
    }
  }
};

window.toggleLiveRadioPlayback = function() {
  const currentSrc = window.radioChannelStreams[window.currentRadioChannel] || 'assets/audio/bhajan_achyutam_keshavam.mp3';

  if (window.isLiveRadioPlaying) {
    window.radioAudioElement.pause();
    window.isLiveRadioPlaying = false;
    window.updateRadioUIState(false);
    if (typeof showToast === 'function') showToast('⏸️ लाइव रेडियो रोका गया');
  } else {
    // If src is different or empty, set src
    if (!window.radioAudioElement.src || window.radioAudioElement.src.indexOf(currentSrc) === -1) {
      window.radioAudioElement.src = currentSrc;
    }
    
    // Play with promise handler
    const playPromise = window.radioAudioElement.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        window.isLiveRadioPlaying = true;
        window.updateRadioUIState(true);
        if (typeof showToast === 'function') showToast('📻 24×7 लाइव भक्ति रेडियो बज रहा है...');
      }).catch(err => {
        console.warn("Audio play prevented:", err);
        // Force fallback to bhajan
        window.radioAudioElement.src = 'assets/audio/bhajan_achyutam_keshavam.mp3';
        window.radioAudioElement.play().catch(() => {});
      });
    }
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

  const newSrc = window.radioChannelStreams[chanKey] || 'assets/audio/bhajan_achyutam_keshavam.mp3';
  window.radioAudioElement.src = newSrc;

  if (window.isLiveRadioPlaying) {
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

# Replace in app.js
start_marker = "// ══════════════════════════════════════════════════════════════════════════════\n// 📻 24x7 LIVE BHAKTI RADIO"
if start_marker in js:
    js = js[:js.find(start_marker)] + new_live_radio_js
else:
    js += "\n\n" + new_live_radio_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"✓ Updated app.js with real Audio playback engine and auto-looping (v={ts})")
