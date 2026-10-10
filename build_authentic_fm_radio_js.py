import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

radio_full_engine_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 📻 24x7 AUTHENTIC VEDIC FM BROADCAST RADIO ENGINE
// Multi-Channel • Station Jingles & RJ Drops • Retro Analog Tuner Needle • Live Shows
// ══════════════════════════════════════════════════════════════════════════════

window.BHAKTI_RADIO_STATIONS = [
  {
    id: 'shiv_bhajan',
    freq: '108.1 FM',
    mhz: 108.1,
    needlePos: '82%',
    deity: 'shiva',
    icon: '🔱',
    name: 'महाकाल शिव भजन',
    badge: 'Non-stop Shiv Bhajans',
    currentTrack: 'ॐ नमः शिवाय • महाकाल भस्म आरती स्तुति',
    singer: 'पंडित जसराज व काशी विद्वत परिषद',
    jingleText: '१०८.१ FM... महाकाल शिव तरंग! हर हर महादेव... आप सुन रहे हैं दिव्य आराधना।',
    streamUrl: 'assets/audio/katha_shiva.mp3'
  },
  {
    id: 'krishna_ras',
    freq: '108.5 FM',
    mhz: 108.5,
    needlePos: '88%',
    deity: 'krishna',
    icon: '🪷',
    name: 'श्री राधा-कृष्ण रस',
    badge: '⭐ लोकप्रिय स्टेशन',
    currentTrack: 'अच्युतम केशवम कृष्ण दामोदरम',
    singer: 'श्री अनिरुद्धाचार्य जी महाराज',
    jingleText: '१०८.५ FM... दिव्य भक्ति तरंग... मन पावन, जीवन पावन! चलिए सुनते हैं यह पावन स्तुति...',
    streamUrl: 'assets/audio/bhajan_achyutam_keshavam.mp3'
  },
  {
    id: 'hanuman_vani',
    freq: '108.9 FM',
    mhz: 108.9,
    needlePos: '95%',
    deity: 'hanuman',
    icon: '🚩',
    name: 'संकटमोचन हनुमान वाणी',
    badge: 'Sundarkand & Chalisa',
    currentTrack: 'श्री सुंदरकांड अमृत धारा व हनुमान चालीसा',
    singer: 'राजन जी महाराज',
    jingleText: '१०८.९ FM... संकटमोचन हनुमान वाणी! जय श्री राम... संकट कटे मिटे सब पीरा।',
    streamUrl: 'assets/audio/katha_hanuman.mp3'
  },
  {
    id: 'om_mantra',
    freq: '100.8 FM',
    mhz: 100.8,
    needlePos: '8%',
    deity: 'general',
    icon: '🕉️',
    name: 'दिव्य 24×7 ओंकार व महामंत्र',
    badge: 'Continuous Meditation',
    currentTrack: 'अखंड ओंकार नाद व महामृत्युंजय महामंत्र',
    singer: 'स्वामी शिवानंद आश्रम (ऋषिकेश)',
    jingleText: '१००.८ FM... अखंड ओंकार व महामंत्र... चित्त शांत, आत्मा तृप्त।',
    streamUrl: 'assets/audio/katha_bhagwat.mp3'
  },
  {
    id: 'mandir_aarti',
    freq: '102.4 FM',
    mhz: 102.4,
    needlePos: '28%',
    deity: 'aarti',
    icon: '🪔',
    name: 'प्रसिद्ध मंदिर लाइव आरती',
    badge: 'Live Temple Aartis',
    currentTrack: 'श्री सत्यनारायण भगवान पावन महाआरती',
    singer: 'काशी विश्वनाथ व तिरुपति धाम',
    jingleText: '१०२.४ FM... प्रसिद्ध मंदिर लाइव आरती! घर बैठे पावन दर्शन।',
    streamUrl: 'assets/audio/katha_satyanarayan.mp3'
  }
];

window.currentRadioStationIndex = 1; // Default to Krishna Ras 108.5 FM
window.isLiveRadioPlaying = false;
window.liveListenerBaseCount = 14280;

if (!window.radioAudioElement) {
  window.radioAudioElement = new Audio();
  window.radioAudioElement.loop = true;
  window.radioAudioElement.preload = 'auto';
}

// 1. Live Show & RJ Scheduler Engine
window.updateLiveRadioShowSchedule = function() {
  const now = new Date();
  const hour = now.getHours();

  let showName = 'अमृत वेला प्रभात';
  let rjName = 'RJ दिव्या';
  let nextShow = 'दोपहर 12:00 बजे • मधुर कथा प्रवाह';

  if (hour >= 4 && hour < 7) {
    showName = 'अमृत वेला प्रभात';
    rjName = 'RJ दिव्या';
    nextShow = 'सुबह 07:00 बजे • आरती वंदना & संकीर्तन धारा';
  } else if (hour >= 7 && hour < 12) {
    showName = 'आरती वंदना & संकीर्तन धारा';
    rjName = 'RJ राघव';
    nextShow = 'दोपहर 12:00 बजे • मधुर कथा प्रवाह';
  } else if (hour >= 12 && hour < 16) {
    showName = 'मधुर कथा प्रवाह';
    rjName = 'RJ आनंद';
    nextShow = 'शाम 04:00 बजे • भक्ति रस माधुरी';
  } else if (hour >= 16 && hour < 18) {
    showName = 'भक्ति रस माधुरी';
    rjName = 'RJ प्रिया';
    nextShow = 'शाम 06:00 बजे • महाकाल संध्या आरती & दीप दर्शन';
  } else if (hour >= 18 && hour < 21) {
    showName = 'महाकाल संध्या आरती & दीप दर्शन';
    rjName = 'RJ रुद्राक्ष';
    nextShow = 'रात 09:00 बजे • अखंड ध्यान व निद्रा स्तुति';
  } else {
    showName = 'अखंड ध्यान व निद्रा स्तुति';
    rjName = 'RJ सौम्य';
    nextShow = 'भोर 04:00 बजे • अमृत वेला प्रभात';
  }

  const showEl = document.getElementById('radio-live-show-name');
  const rjEl = document.getElementById('radio-live-rj-name');
  const nextEl = document.getElementById('radio-upcoming-show-ticker');

  if (showEl) showEl.textContent = showName;
  if (rjEl) rjEl.textContent = rjName;
  if (nextEl) nextEl.textContent = `अगला कार्यक्रम: ${nextShow}`;
};

// 2. Tune to Station by Index (Analog Dial + Jingle & RJ Drop)
window.tuneRadioStation = function(index, skipJingle = false) {
  if (index < 0) index = window.BHAKTI_RADIO_STATIONS.length - 1;
  if (index >= window.BHAKTI_RADIO_STATIONS.length) index = 0;

  window.currentRadioStationIndex = index;
  const st = window.BHAKTI_RADIO_STATIONS[index];

  // 1. Play Authentic Radio Static Tuning Sound + Chime
  window.playRadioStaticAndChimeTuningFX();

  // 2. Haptic Vibration
  if (navigator.vibrate) navigator.vibrate([20, 35, 20]);

  // 3. Move Retro Analog Tuning Needle
  const needle = document.getElementById('analog-tuning-needle');
  const freqLabel = document.getElementById('analog-frequency-label');
  if (needle) needle.style.left = st.needlePos;
  if (freqLabel) freqLabel.textContent = `TUNED: ${st.mhz} MHz`;

  // 4. Update UI Elements
  const disc = document.getElementById('radio-disc-icon');
  const title = document.getElementById('radio-station-title');
  const track = document.getElementById('radio-track-now');
  const artist = document.getElementById('radio-artist-sub');
  const freqTag = document.getElementById('radio-freq-tag');

  if (disc) disc.textContent = st.icon;
  if (freqTag) freqTag.innerHTML = `<span>📡 ${st.freq}</span> • <span id="radio-station-title">${st.name}</span>`;
  if (track) track.textContent = st.currentTrack;
  if (artist) artist.textContent = `${st.singer} • 24×7 लाइव प्रसारण`;

  // 5. Update Active Pill Styling & Smooth Scroll
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

  const activePill = document.getElementById(`radio-pill-${index}`);
  if (activePill) {
    activePill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
  }

  // 6. Update Audio Stream & Play Jingle
  if (!window.radioAudioElement) window.radioAudioElement = new Audio();
  window.radioAudioElement.src = st.streamUrl;

  if (window.isLiveRadioPlaying) {
    if (!skipJingle) {
      window.playStationJingleAndRJDrop(st, () => {
        const p = window.radioAudioElement.play();
        if (p !== undefined) p.catch(() => {});
      });
    } else {
      const p = window.radioAudioElement.play();
      if (p !== undefined) p.catch(() => {});
    }
  }

  // 7. Update MediaSession API for Lockscreen
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

// 3. Interactive Analog Radio Scale Click Seeking
window.handleAnalogScaleClick = function(event) {
  const rect = event.currentTarget.getBoundingClientRect();
  const clickX = event.clientX - rect.left;
  const ratio = Math.max(0, Math.min(1, clickX / rect.width));

  // Find closest station by needle position percentage
  let closestIdx = 0;
  let minDiff = 999;

  window.BHAKTI_RADIO_STATIONS.forEach((st, idx) => {
    const stRatio = parseFloat(st.needlePos) / 100;
    const diff = Math.abs(ratio - stRatio);
    if (diff < minDiff) {
      minDiff = diff;
      closestIdx = idx;
    }
  });

  window.tuneRadioStation(closestIdx);
};

// 4. Play / Pause Controller
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
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (navigator.mediaSession) navigator.mediaSession.playbackState = 'paused';
    if (typeof showToast === 'function') showToast('⏸️ लाइव रेडियो रोका गया');
  } else {
    if (!window.radioAudioElement.src || window.radioAudioElement.src.indexOf(st.streamUrl) === -1) {
      window.radioAudioElement.src = st.streamUrl;
    }

    // Play Jingle on initial connect
    window.playStationJingleAndRJDrop(st, () => {
      const playPromise = window.radioAudioElement.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          window.isLiveRadioPlaying = true;
          window.updateRadioUIState(true);
          window.updateRadioMediaSession(st);
          if (typeof showToast === 'function') showToast(`📻 ${st.freq} ${st.name} लाइव प्रसारित हो रहा है...`);
        }).catch(err => {
          console.warn("Autoplay fallback:", err);
          window.radioAudioElement.src = 'assets/audio/bhajan_achyutam_keshavam.mp3';
          window.radioAudioElement.play().then(() => {
            window.isLiveRadioPlaying = true;
            window.updateRadioUIState(true);
          }).catch(() => {});
        });
      }
    });
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
      liveText.textContent = '🔴 LIVE ON AIR';
      liveText.style.color = '#F87171';
    }
  }
};

// 5. Station Jingle & RJ Voice Drop Engine (Big FM / Radio Mirchi Style)
window.playStationJingleAndRJDrop = function(station, onReadyCallback) {
  if (typeof onReadyCallback === 'function') {
    onReadyCallback();
  }

  // Voiceover RJ Drop
  if ('speechSynthesis' in window && station.jingleText) {
    try {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(station.jingleText);
      utterance.lang = 'hi-IN';
      utterance.rate = 1.05; // Radio RJ energetic pace
      utterance.pitch = 1.12;

      // Auto-duck music slightly while RJ speaks
      if (window.radioAudioElement && window.isLiveRadioPlaying) {
        window.radioAudioElement.volume = 0.25;
        utterance.onend = function() {
          if (window.radioAudioElement) window.radioAudioElement.volume = 1.0;
        };
      }

      window.speechSynthesis.speak(utterance);
    } catch(e) {}
  }
};

// 6. Realistic Analog Radio Static White Noise & Frequency Sweep Sound
window.playRadioStaticAndChimeTuningFX = function() {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();

    // 1. Generate short 0.15s analog white-noise burst
    const bufferSize = ctx.sampleRate * 0.15;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * 0.04; // Gentle static
    }

    const noise = ctx.createBufferSource();
    noise.buffer = buffer;
    const noiseGain = ctx.createGain();
    noiseGain.gain.setValueAtTime(0.06, ctx.currentTime);
    noiseGain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.14);

    noise.connect(noiseGain);
    noiseGain.connect(ctx.destination);
    noise.start();

    // 2. Synthetic resonant radio chime
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(600, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1200, ctx.currentTime + 0.18);

    gain.gain.setValueAtTime(0.08, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.22);

    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.24);
  } catch(e) {}
};

// 7. Lockscreen MediaSession API
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

// 8. Auto-Ducking for Bell, Conch & AI Voice
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

// 9. Periodic Live Listener & Schedule Updater
setInterval(() => {
  window.updateLiveRadioShowSchedule();

  // Fluctuate live listener count subtly
  const countEl = document.getElementById('radio-live-listener-count');
  if (countEl) {
    const delta = Math.floor(Math.random() * 25) - 12;
    window.liveListenerBaseCount = Math.max(13800, Math.min(15600, window.liveListenerBaseCount + delta));
    countEl.textContent = `${window.liveListenerBaseCount.toLocaleString('en-IN')}+`;
  }
}, 5000);

// Initialize schedule on startup
setTimeout(window.updateLiveRadioShowSchedule, 500);
"""

# Replace existing radio code in app.js
start_marker = '// ══════════════════════════════════════════════════════════════════════════════\n// 📻 24x7 REAL MULTI-CHANNEL LIVE BHAKTI RADIO ENGINE'
if start_marker not in js:
    start_marker = '// 📻 24x7 REAL MULTI-CHANNEL LIVE BHAKTI RADIO ENGINE'

s_idx = js.find(start_marker)
if s_idx != -1:
    e_idx = js.find('// ══════════════════════════════════════════════════════════════════════════════\n// 🎨 DYNAMIC LIVE THEME ENGINE', s_idx)
    if e_idx != -1:
        js = js[:s_idx] + radio_full_engine_code + "\n\n" + js[e_idx:]
        print("✓ Replaced radio engine in app.js with Authentic FM Broadcast Engine")
    else:
        js = js[:s_idx] + radio_full_engine_code
        print("✓ Updated radio engine in app.js")
else:
    # Append
    js = js + "\n\n" + radio_full_engine_code
    print("✓ Appended Authentic FM Broadcast Engine to app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ app.js written successfully!")
