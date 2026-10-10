import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html video tag with inline onended and ontimeupdate
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_video_tag = '<video id="app-intro-video" src="assets/videos/app_intro_cinematic.mp4'
new_video_tag = '<video id="app-intro-video" onended="skipIntroVideo(event)" ontimeupdate="checkVideoEndProgress(this)" src="assets/videos/app_intro_cinematic.mp4'

if old_video_tag in html:
    html = html.replace(old_video_tag, new_video_tag)
    print("✓ Added inline onended & ontimeupdate to video tag in index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)
html = re.sub(r'app_intro_cinematic\.mp4(\?v=\d+)?', f'app_intro_cinematic.mp4?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update app.js with ultra-robust multi-layer video lifecycle & auto auth opener
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

video_lifecycle_engine = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎬 ULTRA-ROBUST VIDEO END DETECTOR & AUTOMATIC AUTH MODAL OPENER
// ══════════════════════════════════════════════════════════════════════════════

window.hasIntroVideoSkipped = false;

window.checkVideoEndProgress = function(video) {
  if (window.hasIntroVideoSkipped) return;
  if (video && video.duration && !isNaN(video.duration)) {
    // If within 0.35s of end, immediately transition to login
    if (video.currentTime >= (video.duration - 0.35)) {
      window.skipIntroVideo();
    }
  }
};

window.initIntroVideo = function() {
  const overlay = document.getElementById('app-intro-video-overlay');
  const video = document.getElementById('app-intro-video');
  if (!overlay || !video) return;

  window.hasIntroVideoSkipped = false;

  // Listeners
  video.addEventListener('ended', function() {
    window.skipIntroVideo();
  });

  video.addEventListener('timeupdate', function() {
    window.checkVideoEndProgress(video);
  });

  video.addEventListener('loadedmetadata', function() {
    if (video.duration && !isNaN(video.duration)) {
      // Safety fallback timer matching video duration + 0.5s
      setTimeout(() => {
        if (!window.hasIntroVideoSkipped) {
          window.skipIntroVideo();
        }
      }, (video.duration + 0.5) * 1000);
    }
  });

  // Attempt auto-play
  video.play().catch(err => {
    console.log("Autoplay waiting for touch gesture:", err);
  });
};

window.skipIntroVideo = function(event) {
  if (event) {
    event.stopPropagation();
    if (event.preventDefault) event.preventDefault();
  }

  if (window.hasIntroVideoSkipped) return;
  window.hasIntroVideoSkipped = true;

  const overlay = document.getElementById('app-intro-video-overlay');
  const video = document.getElementById('app-intro-video');
  const splash = document.getElementById('splash-screen');

  if (video) {
    try { video.pause(); } catch(e) {}
  }

  if (splash) {
    splash.style.display = 'none';
    splash.classList.add('hidden');
  }

  if (overlay) {
    overlay.style.transition = 'opacity 0.35s ease';
    overlay.style.opacity = '0';
    overlay.style.pointerEvents = 'none';
    setTimeout(() => {
      overlay.style.display = 'none';
      if (overlay.parentNode) {
        overlay.parentNode.removeChild(overlay);
      }
    }, 350);
  }

  // Guaranteed direct opening of Smart Vedic Auth Modal
  setTimeout(() => {
    window.openAuthModal();
  }, 100);
};

window.openAuthModal = function() {
  const modal = document.getElementById('auth-modal');
  if (modal) {
    modal.style.display = 'flex';
    modal.style.opacity = '1';
    modal.style.pointerEvents = 'auto';
    modal.classList.remove('hidden');
  }
};
"""

# Append / update in app.js
app_js += "\n" + video_lifecycle_engine

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print(f"✓ Applied Multi-layer Video End Detector & Auto Auth Opener (v={ts})")
