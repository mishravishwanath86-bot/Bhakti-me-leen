import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Fullscreen App Startup Intro Video Overlay right after <body>
intro_video_html = """  <!-- 🎬 FULLSCREEN APP STARTUP INTRO CINEMATIC VIDEO 🎬 -->
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

if 'id="app-intro-video-overlay"' not in html:
    html = html.replace('<body>', '<body>\n\n' + intro_video_html)
    print("✓ Added Fullscreen Intro Video Overlay to index.html")

# 2. Update #onboarding-overlay to start hidden (style="display:none;")
html = html.replace(
    '<div id="onboarding-overlay">',
    '<div id="onboarding-overlay" style="display:none;">'
)

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add Intro Video Controller & Post-Login 5-Slide Onboarding Flow in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

intro_and_onboarding_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎬 CINEMATIC APP STARTUP INTRO VIDEO & POST-LOGIN ONBOARDING CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.isIntroVideoSoundMuted = true;

window.initIntroVideo = function() {
  const overlay = document.getElementById('app-intro-video-overlay');
  const video = document.getElementById('app-intro-video');
  if (!overlay || !video) return;

  // Auto-play video
  video.play().catch(err => {
    console.log("Autoplay waiting for interaction:", err);
  });

  // End video automatically
  video.onended = function() {
    window.skipIntroVideo();
  };
};

window.toggleIntroVideoSound = function() {
  const video = document.getElementById('app-intro-video');
  const btn = document.getElementById('intro-video-sound-btn');
  if (!video) return;

  video.muted = !video.muted;
  window.isIntroVideoSoundMuted = video.muted;

  if (btn) {
    btn.innerHTML = video.muted ? '🔇 ध्वनि चालू करें' : '🔊 ध्वनि चालू है';
    btn.style.borderColor = video.muted ? 'rgba(248,200,59,0.5)' : '#10B981';
  }
};

window.skipIntroVideo = function() {
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
    }, 600);
  }

  // Check authentication status on start
  const isAuth = localStorage.getItem('sanatan_is_authenticated');
  const isGuest = localStorage.getItem('sanatan_is_guest');

  if (!isAuth && !isGuest) {
    // Open Smart Vedic Auth Modal for unauthenticated user
    setTimeout(() => {
      window.openAuthModal();
    }, 300);
  }
};

// 🌟 Post-Login: Trigger 5-Slide Onboarding Carousel if not completed
window.checkAndTriggerPostLoginOnboarding = function() {
  const isCompleted = localStorage.getItem('sanatan_onboarding_completed');
  const onboardingOverlay = document.getElementById('onboarding-overlay');

  if (!isCompleted && onboardingOverlay) {
    onboardingOverlay.style.display = 'block';
    window.currentOnboardingSlide = 0;
    window.updateOnboardingSlide(0);
  } else {
    // If onboarding already done, trigger Step 2: Deity Selection
    const deityModal = document.getElementById('deity-onboarding-modal');
    const primaryDeity = localStorage.getItem('sanatan_primary_deity');
    if (!primaryDeity && deityModal) {
      deityModal.style.display = 'flex';
    }
  }
};

// Hook finishOnboarding to transition to Deity Selection Onboarding
const origFinishOnboarding = window.finishOnboarding;
window.finishOnboarding = function() {
  const overlay = document.getElementById('onboarding-overlay');
  if (overlay) overlay.style.display = 'none';

  localStorage.setItem('sanatan_onboarding_completed', 'true');

  // Trigger Step 2: Deity Selection
  const deityModal = document.getElementById('deity-onboarding-modal');
  if (deityModal) {
    deityModal.style.display = 'flex';
  } else {
    if (typeof showToast === 'function') showToast('🚩 स्वागतम्! दिव्य यात्रा आरंभ हुई');
  }
};

// Start Intro Video immediately on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.initIntroVideo);
} else {
  window.initIntroVideo();
}
"""

if 'CINEMATIC APP STARTUP INTRO VIDEO' not in app_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(intro_and_onboarding_js)
    print("✓ Added Intro Video & Post-Login Onboarding Controller to app.js")
else:
    print("Intro Video Controller already present in app.js")

# Update onSuccessfulAuthentication in app.js to trigger checkAndTriggerPostLoginOnboarding
app_js = app_js.replace(
    "// Open Step 2: Deity Selection Onboarding\n  const deityModal = document.getElementById('deity-onboarding-modal');\n  if (deityModal) {\n    deityModal.style.display = 'flex';\n  }",
    "// Trigger 5-Slide Carousel first, then Deity Selection Onboarding\n  window.checkAndTriggerPostLoginOnboarding();"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print(f"✓ Video and Onboarding sequence fully configured and live (v={ts})")
