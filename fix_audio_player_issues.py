import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1.1 Fix Top-Left Back Arrow (Change down chevron '⌄' to Left Chevron '❮')
old_topbar_btn = """      <!-- Top Bar -->
      <div class="classic-player-topbar">
        <button class="classic-topbar-btn" onclick="closeGlassPlayer()" title="छोटा करें">
          <span style="font-size:1.3rem; font-weight:900; line-height:1;">⌄</span>
        </button>"""

new_topbar_btn = """      <!-- Top Bar -->
      <div class="classic-player-topbar">
        <button class="classic-topbar-btn" onclick="closeGlassPlayer()" title="पीछे जाएं (Back)" style="display:flex; align-items:center; justify-content:center;">
          <span style="font-size:1.4rem; font-weight:900; line-height:1; display:flex; align-items:center; justify-content:center; margin-right:2px;">❮</span>
        </button>"""

if old_topbar_btn in html:
    html = html.replace(old_topbar_btn, new_topbar_btn, 1)
else:
    # Regex replace
    html = re.sub(
        r'<div class="classic-player-topbar">\s*<button class="classic-topbar-btn" onclick="closeGlassPlayer\(\)"[^>]*>\s*<span[^>]*>[^<]*<\/span>\s*<\/button>',
        new_topbar_btn,
        html,
        count=1
    )

print("✓ Fixed 1: Replaced down arrow with Left Arrow (❮) in top-left back button")

# 2. Update styles.css to Enlarge Artwork Image (Red Box)
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

enlarged_artwork_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🎧 ENLARGED MAJESTIC DEITY ARTWORK & SYNCED PLAY/PAUSE FOR AUDIO PLAYER
   ══════════════════════════════════════════════════════════════════════════════ */

.classic-artwork-wrapper {
  margin: 0.8rem 0 1.4rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
}

.classic-artwork-ring {
  width: 300px !important;
  height: 300px !important;
  max-width: 82vw !important;
  max-height: 82vw !important;
  border-radius: 32px !important;
  padding: 6px !important;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 50%, #B45309 100%) !important;
  border: 2.5px solid #FEF3C7 !important;
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.85), 0 0 35px rgba(248, 200, 59, 0.35) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.classic-artwork-img {
  width: 100% !important;
  height: 100% !important;
  border-radius: 26px !important;
  object-fit: cover !important;
  display: block !important;
}

/* Big Vibrant Play/Pause Main Button */
.classic-play-main-btn {
  width: 72px !important;
  height: 72px !important;
  border-radius: 50% !important;
  background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #D97706 100%) !important;
  border: 3.5px solid #FEF3C7 !important;
  color: #1A0B2E !important;
  font-size: 1.7rem !important;
  font-weight: 900 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  box-shadow: 0 8px 30px rgba(245, 158, 11, 0.65), 0 0 25px rgba(248, 200, 59, 0.45) !important;
  transition: all 0.2s ease !important;
}

.classic-play-main-btn:active {
  transform: scale(0.92) !important;
}
"""

css += "\n\n" + enlarged_artwork_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Fixed 2: Enlarged Artwork to 300px with luxurious golden frame & shadow")

# 3. Update app.js for 100% Reliable Play / Pause Button State Synchronization
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

play_pause_sync_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎵 MASTER AUDIO PLAY/PAUSE SYNC & CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.getActiveAudioPlayer = function() {
  if (window.coreAudioElement && window.coreAudioElement.src) return window.coreAudioElement;
  if (typeof audioPlayerObj !== 'undefined' && audioPlayerObj && audioPlayerObj.src) return audioPlayerObj;
  if (window.currentAudioPlayer && window.currentAudioPlayer.src) return window.currentAudioPlayer;
  if (window.radioAudioElement && window.isLiveRadioPlaying) return window.radioAudioElement;
  return window.coreAudioElement || (typeof audioPlayerObj !== 'undefined' ? audioPlayerObj : null);
};

window.updateMasterAudioPlayState = function(isPlaying) {
  if (typeof isAudioPlaying !== 'undefined') isAudioPlaying = isPlaying;
  if (window.MediaRouter) window.MediaRouter.isPlaying = isPlaying;

  // 1. Update Full-Screen Player Main Play/Pause Button
  const playBtn = document.getElementById('glass-modal-play-btn');
  if (playBtn) {
    playBtn.innerHTML = isPlaying 
      ? '<span id="glass-modal-play-icon" style="font-size:1.6rem; font-weight:900; line-height:1; display:flex; align-items:center; justify-content:center;">❚❚</span>'
      : '<span id="glass-modal-play-icon" style="font-size:1.6rem; font-weight:900; line-height:1; margin-left:3px; display:flex; align-items:center; justify-content:center;">▶</span>';
    playBtn.title = isPlaying ? "पॉज करें (Pause)" : "प्ले करें (Play)";
  }

  // 2. Update Mini Player Play/Pause Button
  const miniPlayBtn = document.getElementById('mini-player-play-btn');
  if (miniPlayBtn) {
    miniPlayBtn.innerHTML = isPlaying ? '❚❚' : '▶';
  }

  // 3. Rotating artwork effect if playing
  const mImg = document.getElementById('glass-modal-img');
  if (mImg) {
    if (isPlaying) mImg.classList.add('playing');
    else mImg.classList.remove('playing');
  }
};

window.togglePlayKatha = function() {
  const audio = window.getActiveAudioPlayer();

  if (!audio) {
    if (typeof playKatha === 'function') {
      playKatha(typeof currentKathaIdx !== 'undefined' ? currentKathaIdx : 0);
      window.updateMasterAudioPlayState(true);
    }
    return;
  }

  if (audio.paused) {
    const playPromise = audio.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        window.updateMasterAudioPlayState(true);
      }).catch(err => {
        console.warn("Play blocked:", err);
        window.updateMasterAudioPlayState(true);
      });
    } else {
      window.updateMasterAudioPlayState(true);
    }
  } else {
    audio.pause();
    window.updateMasterAudioPlayState(false);
  }
};

// Global Audio Event Hook to ensure UI is NEVER out of sync!
setInterval(function() {
  const audio = window.getActiveAudioPlayer();
  if (audio) {
    const isPlaying = !audio.paused && !audio.ended && audio.currentTime > 0;
    const playBtn = document.getElementById('glass-modal-play-btn');
    if (playBtn) {
      const isShowingPause = playBtn.innerHTML.includes('❚❚');
      if (isPlaying && !isShowingPause) {
        window.updateMasterAudioPlayState(true);
      } else if (!isPlaying && isShowingPause) {
        window.updateMasterAudioPlayState(false);
      }
    }
  }
}, 300);
"""

js += "\n\n" + play_pause_sync_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Fixed 3: Synchronized Play/Pause Button UI (▶ on Pause, ❚❚ on Play)")

# Bump cache buster in index.html
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Successfully applied all 3 fixes and bumped cache buster to {ts}")
