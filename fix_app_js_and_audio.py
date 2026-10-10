import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Fix Syntax Error in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Fix unquoted showToast
app_js = app_js.replace(
    "showToast(🙏 स्वागतम्, ! (Streak:  दिन 🔥));",
    "showToast(`🙏 स्वागतम्, ${user.name || 'भक्त'}! (Streak: ${user.preferences?.dailyStreak || 1} दिन 🔥)`);"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("✓ Fixed syntax error in app.js")

# 2. Update index.html for Video Sound and Tap-to-Unmute overlay
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_video_overlay = """  <!-- 🎬 FULLSCREEN APP STARTUP INTRO CINEMATIC VIDEO 🎬 -->
  <div id="app-intro-video-overlay" style="position:fixed; inset:0; z-index:999999; background:#000; display:flex; align-items:center; justify-content:center; overflow:hidden; transition:opacity 0.6s ease;">
    <video id="app-intro-video" src="assets/videos/app_intro_cinematic.mp4" playsinline autoplay muted style="width:100%; height:100%; object-fit:cover;"></video>
    
    <!-- Top Controls: Sound Toggle & Skip Button -->
    <div style="position:absolute; top:20px; right:16px; z-index:10; display:flex; align-items:center; gap:8px;">
      <button onclick="toggleIntroVideoSound()" id="intro-video-sound-btn" style="background:rgba(10,2,18,0.65); border:1.2px solid rgba(248,200,59,0.5); color:#FDE68A; padding:6px 14px; border-radius:20px; font-size:0.75rem; font-weight:800; cursor:pointer; backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); box-shadow:0 4px 15px rgba(0,0,0,0.4);">
        🔇 ध्वनि चालू करें
      </button>
      <button onclick="skipIntroVideo()" style="background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; padding:7px 18px; border-radius:20px; font-size:0.82rem; font-weight:900; cursor:pointer; box-shadow:0 0 18px rgba(248,200,59,0.6); transition:transform 0.15s ease;">
        छोड़ें (Skip) ❯
      </button>
    </div>
  </div>"""

new_video_overlay = """  <!-- 🎬 FULLSCREEN APP STARTUP INTRO CINEMATIC VIDEO 🎬 -->
  <div id="app-intro-video-overlay" onclick="enableIntroVideoAudioOnTouch(event)" style="position:fixed; inset:0; z-index:999999; background:#000; display:flex; align-items:center; justify-content:center; overflow:hidden; transition:opacity 0.5s ease; cursor:pointer;">
    <video id="app-intro-video" src="assets/videos/app_intro_cinematic.mp4" playsinline autoplay muted style="width:100%; height:100%; object-fit:cover;"></video>
    
    <!-- Floating Center Tap-to-Unmute Prompt -->
    <div id="intro-sound-prompt-pill" onclick="toggleIntroVideoSound(event)" style="position:absolute; bottom:40px; left:50%; transform:translateX(-50%); z-index:15; background:linear-gradient(135deg, rgba(248,200,59,0.95), rgba(217,119,6,0.95)); border:2px solid #FEF3C7; color:#1A0B2E; padding:10px 22px; border-radius:30px; font-size:0.88rem; font-weight:900; box-shadow:0 0 30px rgba(248,200,59,0.9), 0 4px 20px rgba(0,0,0,0.6); display:flex; align-items:center; gap:8px; animation:pulseGlow 1.8s infinite; cursor:pointer;">
      <span style="font-size:1.2rem;">🔊</span>
      <span>ध्वनि चालू करने हेतु स्पर्श करें (Tap For Sound)</span>
    </div>

    <!-- Top Controls: Sound Toggle & Skip Button -->
    <div style="position:absolute; top:20px; right:16px; z-index:20; display:flex; align-items:center; gap:8px;">
      <button onclick="toggleIntroVideoSound(event)" id="intro-video-sound-btn" style="background:rgba(10,2,18,0.75); border:1.5px solid #F8C83B; color:#FDE68A; padding:7px 15px; border-radius:20px; font-size:0.78rem; font-weight:900; cursor:pointer; backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); box-shadow:0 4px 15px rgba(0,0,0,0.5);">
        🔇 ध्वनि चालू करें
      </button>
      <button onclick="skipIntroVideo(event)" style="background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; padding:8px 20px; border-radius:20px; font-size:0.85rem; font-weight:900; cursor:pointer; box-shadow:0 0 20px rgba(248,200,59,0.7); transition:transform 0.15s ease;">
        छोड़ें (Skip) ❯
      </button>
    </div>
  </div>"""

if old_video_overlay in html:
    html = html.replace(old_video_overlay, new_video_overlay)
    print("✓ Updated video overlay in index.html with interactive tap-to-unmute")
else:
    # Regex replacement if exact match differs
    html = re.sub(r'<!-- 🎬 FULLSCREEN APP STARTUP INTRO CINEMATIC VIDEO 🎬 -->[\s\S]*?<\/div>\s*<\/div>', new_video_overlay, html)
    print("✓ Replaced video overlay via regex")

# Bump cache busters
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)
html = re.sub(r'app_intro_cinematic\.mp4(\?v=\d+)?', f'app_intro_cinematic.mp4?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add audio gesture handlers in app.js
audio_gesture_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🔊 INTRO VIDEO AUDIO GESTURE & LIFECYCLE CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.enableIntroVideoAudioOnTouch = function(event) {
  const video = document.getElementById('app-intro-video');
  const btn = document.getElementById('intro-video-sound-btn');
  const promptPill = document.getElementById('intro-sound-prompt-pill');

  if (!video) return;

  // If clicked directly on the Skip button, do not intercept
  if (event && event.target && event.target.closest && event.target.closest('button') && event.target.closest('button').textContent.includes('Skip')) {
    return;
  }

  video.muted = false;
  video.volume = 1.0;

  if (btn) {
    btn.innerHTML = '🔊 ध्वनि चालू है';
    btn.style.borderColor = '#10B981';
    btn.style.color = '#86EFAC';
  }

  if (promptPill) {
    promptPill.style.display = 'none';
  }
};

window.toggleIntroVideoSound = function(event) {
  if (event) event.stopPropagation();
  const video = document.getElementById('app-intro-video');
  const btn = document.getElementById('intro-video-sound-btn');
  const promptPill = document.getElementById('intro-sound-prompt-pill');
  if (!video) return;

  video.muted = !video.muted;
  if (!video.muted) video.volume = 1.0;

  if (btn) {
    btn.innerHTML = video.muted ? '🔇 ध्वनि चालू करें' : '🔊 ध्वनि चालू है';
    btn.style.borderColor = video.muted ? '#F8C83B' : '#10B981';
    btn.style.color = video.muted ? '#FDE68A' : '#86EFAC';
  }

  if (promptPill) {
    promptPill.style.display = video.muted ? 'flex' : 'none';
  }
};

window.skipIntroVideo = function(event) {
  if (event) event.stopPropagation();
  const overlay = document.getElementById('app-intro-video-overlay');
  const video = document.getElementById('app-intro-video');

  if (video) {
    try { video.pause(); } catch(e) {}
  }

  if (overlay) {
    overlay.style.opacity = '0';
    overlay.style.pointerEvents = 'none';
    setTimeout(() => {
      overlay.style.display = 'none';
    }, 400);
  }

  // Guaranteed open Login Modal
  setTimeout(() => {
    window.openAuthModal();
  }, 250);
};

window.openAuthModal = function() {
  const modal = document.getElementById('auth-modal');
  if (modal) {
    modal.style.display = 'flex';
    modal.classList.remove('hidden');
  }
};

window.closeAuthModal = function() {
  const modal = document.getElementById('auth-modal');
  if (modal) modal.style.display = 'none';
};
"""

with open('app.js', 'r', encoding='utf-8') as f:
    cur_js = f.read()

# Replace or append audio gesture
if 'enableIntroVideoAudioOnTouch' not in cur_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(audio_gesture_js)
    print("✓ Added Audio Gesture & Guaranteed Login Opener to app.js")
else:
    print("Audio gesture already in app.js")

print(f"✓ Fix applied and synchronized (v={ts})")
