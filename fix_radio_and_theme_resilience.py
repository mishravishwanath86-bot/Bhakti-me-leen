import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Make document.body safe in applyGlobalTheme
old_theme_block = """    document.documentElement.setAttribute('data-theme', 'light');
    document.body.classList.add('theme-light');
    document.body.classList.remove('theme-dark');"""

new_theme_block = """    if (document.documentElement) document.documentElement.setAttribute('data-theme', 'light');
    if (document.body && document.body.classList) {
      document.body.classList.add('theme-light');
      document.body.classList.remove('theme-dark');
    }"""

js = js.replace(old_theme_block, new_theme_block)

old_dark_block = """    document.documentElement.setAttribute('data-theme', 'dark');
    document.body.classList.remove('theme-light');
    document.body.classList.add('theme-dark');"""

new_dark_block = """    if (document.documentElement) document.documentElement.setAttribute('data-theme', 'dark');
    if (document.body && document.body.classList) {
      document.body.classList.remove('theme-light');
      document.body.classList.add('theme-dark');
    }"""

js = js.replace(old_dark_block, new_dark_block)

# 2. Ultra-reliable Live Radio Engine
radio_engine_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 📻 24x7 LIVE BHAKTI RADIO & SANKALP STREAMING CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.isLiveRadioPlaying = false;
window.currentRadioChannel = 'bhajan';

window.radioChannelStreams = {
  'bhajan': 'assets/audio/bhajan_achyutam_keshavam.mp3',
  'mantra': 'assets/audio/katha_shiva.mp3',
  'katha': 'assets/audio/katha_ramayana.mp3',
  'aarti': 'assets/audio/katha_satyanarayan.mp3'
};

if (!window.radioAudioElement) {
  window.radioAudioElement = new Audio();
  window.radioAudioElement.loop = true;
  window.radioAudioElement.preload = 'auto';
}

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

  if (!window.radioAudioElement) {
    window.radioAudioElement = new Audio();
    window.radioAudioElement.loop = true;
  }

  if (window.isLiveRadioPlaying) {
    window.radioAudioElement.pause();
    window.isLiveRadioPlaying = false;
    window.updateRadioUIState(false);
    if (typeof showToast === 'function') showToast('⏸️ लाइव रेडियो रोका गया');
  } else {
    // Set src if not loaded
    if (!window.radioAudioElement.src || window.radioAudioElement.src.indexOf(currentSrc) === -1) {
      window.radioAudioElement.src = currentSrc;
    }

    const playPromise = window.radioAudioElement.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        window.isLiveRadioPlaying = true;
        window.updateRadioUIState(true);
        if (typeof showToast === 'function') showToast('📻 24×7 लाइव भक्ति रेडियो बज रहा है...');
      }).catch(err => {
        console.warn("Autoplay audio blocked, attempting user gesture unlock:", err);
        window.radioAudioElement.src = 'assets/audio/bhajan_achyutam_keshavam.mp3';
        window.radioAudioElement.play().then(() => {
          window.isLiveRadioPlaying = true;
          window.updateRadioUIState(true);
          if (typeof showToast === 'function') showToast('📻 24×7 लाइव भक्ति रेडियो बज रहा है...');
        }).catch(() => {});
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
  if (!window.radioAudioElement) window.radioAudioElement = new Audio();
  window.radioAudioElement.src = newSrc;

  if (window.isLiveRadioPlaying) {
    window.radioAudioElement.play().catch(() => {});
  }
};
"""

# Replace radio code section in app.js
start_r = js.find('// 📻 24x7 LIVE BHAKTI RADIO')
if start_r != -1:
    end_r = js.find('// ══════════════════════════════════════════════════════════════════════════════\n// 🎨 DYNAMIC LIVE THEME ENGINE', start_r)
    if end_r != -1:
        js = js[:start_r] + radio_engine_code + "\n\n" + js[end_r:]
        print("✓ Replaced radio code in app.js with ultra-reliable version")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Bump cache buster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ app.js and index.html synchronized (v={ts})")
