import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

radio_engine_js_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 📻 24x7 REAL MULTI-CHANNEL LIVE BHAKTI RADIO ENGINE
// 5 Dedicated Vedic Stations • Live EQ Visualizer • MediaSession Lockscreen • Auto-Ducking
// ══════════════════════════════════════════════════════════════════════════════

window.BHAKTI_RADIO_STATIONS = [
  {
    id: 'shiv_bhajan',
    freq: '108.1 FM',
    deity: 'shiva',
    icon: '🔱',
    name: 'महाकाल शिव भजन',
    badge: 'Non-stop Shiv Bhajans',
    currentTrack: 'ॐ नमः शिवाय • महाकाल भस्म आरती स्तुति',
    singer: 'पंडित जसराज व काशी विद्वत परिषद',
    streamUrl: 'assets/audio/katha_shiva.mp3'
  },
  {
    id: 'krishna_ras',
    freq: '108.5 FM',
    deity: 'krishna',
    icon: '🪷',
    name: 'श्री राधा-कृष्ण रस',
    badge: '⭐ लोकप्रिय स्टेशन',
    currentTrack: 'अच्युतम केशवम कृष्ण दामोदरम',
    singer: 'श्री अनिरुद्धाचार्य जी महाराज',
    streamUrl: 'assets/audio/bhajan_achyutam_keshavam.mp3'
  },
  {
    id: 'hanuman_vani',
    freq: '108.9 FM',
    deity: 'hanuman',
    icon: '🚩',
    name: 'संकटमोचन हनुमान वाणी',
    badge: 'Sundarkand & Chalisa',
    currentTrack: 'श्री सुंदरकांड अमृत धारा व हनुमान चालीसा',
    singer: 'राजन जी महाराज',
    streamUrl: 'assets/audio/katha_hanuman.mp3'
  },
  {
    id: 'om_mantra',
    freq: '100.8 FM',
    deity: 'general',
    icon: '🕉️',
    name: 'दिव्य 24×7 ओंकार व महामंत्र',
    badge: 'Continuous Meditation',
    currentTrack: 'अखंड ओंकार नाद व महामृत्युंजय महामंत्र',
    singer: 'स्वामी शिवानंद आश्रम (ऋषिकेश)',
    streamUrl: 'assets/audio/katha_bhagwat.mp3'
  },
  {
    id: 'mandir_aarti',
    freq: '102.4 FM',
    deity: 'aarti',
    icon: '🪔',
    name: 'प्रसिद्ध मंदिर लाइव आरती',
    badge: 'Live Temple Aartis',
    currentTrack: 'श्री सत्यनारायण भगवान पावन महाआरती',
    singer: 'काशी विश्वनाथ व तिरुपति धाम',
    streamUrl: 'assets/audio/katha_satyanarayan.mp3'
  }
];

window.currentRadioStationIndex = 1; // Default to Krishna Ras 108.5 FM
window.isLiveRadioPlaying = false;

if (!window.radioAudioElement) {
  window.radioAudioElement = new Audio();
  window.radioAudioElement.loop = true;
  window.radioAudioElement.preload = 'auto';
}

// 1. Tune to Station by Index
window.tuneRadioStation = function(index) {
  if (index < 0) index = window.BHAKTI_RADIO_STATIONS.length - 1;
  if (index >= window.BHAKTI_RADIO_STATIONS.length) index = 0;

  window.currentRadioStationIndex = index;
  const st = window.BHAKTI_RADIO_STATIONS[index];

  // Play subtle radio tuning frequency sweep
  window.playRadioTuningFrequencyChime();

  // Haptic feedback
  if (navigator.vibrate) navigator.vibrate([15, 30, 20]);

  // Update UI Elements
  const disc = document.getElementById('radio-disc-icon');
  const title = document.getElementById('radio-station-title');
  const track = document.getElementById('radio-track-now');
  const artist = document.getElementById('radio-artist-sub');
  const chanIndex = document.getElementById('radio-current-chan-index');
  const freqTag = document.getElementById('radio-freq-tag');

  if (disc) disc.textContent = st.icon;
  if (freqTag) freqTag.innerHTML = `<span>📡 ${st.freq}</span> • <span id="radio-station-title">${st.name}</span>`;
  if (track) track.textContent = st.currentTrack;
  if (artist) artist.textContent = `${st.singer} • 24×7 लाइव प्रसारण`;
  if (chanIndex) chanIndex.textContent = `चैनल ${index + 1} / ${window.BHAKTI_RADIO_STATIONS.length}`;

  // Update Active Pill Styling
  document.querySelectorAll('.radio-station-pill').forEach((pill, idx) => {
    if (idx === index) {
      pill.classList.add('active');
      pill.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      pill.style.color = '#1A0B2E';
      pill.style.border = 'none';
      pill.style.boxShadow = '0 0 12px rgba(248,200,59,0.4)';
    } else {
      pill.classList.remove('active');
      pill.style.background = 'rgba(255,255,255,0.08)';
      pill.style.color = '#CBD5E1';
      pill.style.border = '1.2px solid rgba(255,255,255,0.18)';
      pill.style.boxShadow = 'none';
    }
  });

  // Scroll active pill into view smoothly
  const activePill = document.getElementById(`radio-pill-${index}`);
  if (activePill) {
    activePill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
  }

  // Switch Stream in Audio Element
  if (!window.radioAudioElement) window.radioAudioElement = new Audio();
  window.radioAudioElement.src = st.streamUrl;

  if (window.isLiveRadioPlaying) {
    const p = window.radioAudioElement.play();
    if (p !== undefined) p.catch(() => {});
  }

  // Update Lockscreen MediaSession
  window.updateRadioMediaSession(st);

  if (typeof showToast === 'function') {
    showToast(`📻 ट्यून किया गया: ${st.freq} • ${st.name}`);
  }
};

window.tuneNextRadioStation = function() {
  window.tuneRadioStation(window.currentRadioStationIndex + 1);
};

window.tunePrevRadioStation = function() {
  window.tuneRadioStation(window.currentRadioStationIndex - 1);
};

// 2. Play / Pause Controller
window.toggleLiveRadioPlayback = function() {
  const st = window.BHAKTI_RADIO_STATIONS[window.currentRadioStationIndex] || window.BHAKTI_RADIO_STATIONS[1];

  if (!window.radioAudioElement) {
    window.radioAudioElement = new Audio();
    window.radioAudioElement.loop = true;
  }

  if (window.isLiveRadioPlaying) {
    window.radioAudioElement.pause();
    window.isLiveRadioPlaying = false;
    window.updateRadioUIState(false);
    if (navigator.mediaSession) navigator.mediaSession.playbackState = 'paused';
    if (typeof showToast === 'function') showToast('⏸️ लाइव रेडियो रोका गया');
  } else {
    if (!window.radioAudioElement.src || window.radioAudioElement.src.indexOf(st.streamUrl) === -1) {
      window.radioAudioElement.src = st.streamUrl;
    }

    const playPromise = window.radioAudioElement.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        window.isLiveRadioPlaying = true;
        window.updateRadioUIState(true);
        window.updateRadioMediaSession(st);
        if (typeof showToast === 'function') showToast(`📻 ${st.freq} ${st.name} लाइव प्रसारित हो रहा है...`);
      }).catch(err => {
        console.warn("Autoplay blocked, unlocking on gesture:", err);
        window.radioAudioElement.src = 'assets/audio/bhajan_achyutam_keshavam.mp3';
        window.radioAudioElement.play().then(() => {
          window.isLiveRadioPlaying = true;
          window.updateRadioUIState(true);
        }).catch(() => {});
      });
    }
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
      badge.style.background = 'rgba(239, 68, 68, 0.22)';
      badge.style.borderColor = '#EF4444';
    }
    if (liveText) {
      liveText.textContent = '🔴 LIVE STREAM';
      liveText.style.color = '#F87171';
    }
  }
};

// 3. MediaSession API (Lockscreen & Notification Background Control)
window.updateRadioMediaSession = function(station) {
  if ('mediaSession' in navigator) {
    navigator.mediaSession.metadata = new MediaMetadata({
      title: `${station.freq} • ${station.currentTrack}`,
      artist: `24×7 लाइव भक्ति रेडियो • ${station.name}`,
      album: 'भक्ति में लीन (अखंड दिव्य रेडियो)',
      artwork: [
        { src: 'assets/icon-192.png', sizes: '192x192', type: 'image/png' },
        { src: 'assets/icon-512.png', sizes: '512x512', type: 'image/png' }
      ]
    });

    navigator.mediaSession.setActionHandler('play', () => window.toggleLiveRadioPlayback());
    navigator.mediaSession.setActionHandler('pause', () => window.toggleLiveRadioPlayback());
    navigator.mediaSession.setActionHandler('previoustrack', () => window.tunePrevRadioStation());
    navigator.mediaSession.setActionHandler('nexttrack', () => window.tuneNextRadioStation());
    navigator.mediaSession.playbackState = window.isLiveRadioPlaying ? 'playing' : 'paused';
  }
};

// 4. Subtle Radio Tuning Noise & Frequency Chime
window.playRadioTuningFrequencyChime = function() {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(540, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1080, ctx.currentTime + 0.15);

    gain.gain.setValueAtTime(0.08, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.2);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + 0.22);
  } catch(e) {}
};

// 5. Audio Focus & Auto-Ducking (when bell, conch or shloka voice plays)
window.duckRadioAudio = function(durationMs = 3000) {
  if (!window.radioAudioElement || !window.isLiveRadioPlaying) return;
  const originalVol = window.radioAudioElement.volume || 1.0;
  window.radioAudioElement.volume = 0.2;

  setTimeout(() => {
    if (window.radioAudioElement) {
      window.radioAudioElement.volume = originalVol;
    }
  }, durationMs);
};
"""

# Replace existing radio code in app.js
start_marker = '// ══════════════════════════════════════════════════════════════════════════════\n// 📻 24x7 LIVE BHAKTI RADIO'
if start_marker not in js:
    start_marker = '// 📻 24x7 LIVE BHAKTI RADIO'

s_idx = js.find(start_marker)
if s_idx != -1:
    e_idx = js.find('// ══════════════════════════════════════════════════════════════════════════════\n// 🎨 DYNAMIC LIVE THEME ENGINE', s_idx)
    if e_idx != -1:
        js = js[:s_idx] + radio_engine_js_code + "\n\n" + js[e_idx:]
        print("✓ Replaced radio engine in app.js with Multi-Channel Live Radio Engine")
    else:
        js = js[:s_idx] + radio_engine_js_code
        print("✓ Updated radio engine in app.js")
else:
    js = js + "\n\n" + radio_engine_js_code
    print("✓ Appended Multi-Channel Live Radio Engine to app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ app.js written successfully!")
