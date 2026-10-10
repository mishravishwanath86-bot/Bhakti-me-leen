import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Early script defining all video handlers in <head> BEFORE <body>
early_video_script = """
  <!-- 🎬 EARLY SCRIPT: DEFINES INTRO VIDEO & AUTH MODAL HANDLERS BEFORE DOM PARSING 🎬 -->
  <script>
    window.hasIntroVideoSkipped = false;

    window.checkVideoEndProgress = function(video) {
      if (window.hasIntroVideoSkipped) return;
      if (video && video.duration && !isNaN(video.duration)) {
        if (video.currentTime >= (video.duration - 0.35)) {
          window.skipIntroVideo();
        }
      }
    };

    window.enableIntroVideoAudioOnTouch = function(event) {
      const video = document.getElementById('app-intro-video');
      const btn = document.getElementById('intro-video-sound-btn');
      const promptPill = document.getElementById('intro-sound-prompt-pill');
      if (!video) return;

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

      // Immediately Open Smart Vedic Auth Modal
      setTimeout(() => {
        window.openAuthModal();
      }, 50);
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

    window.closeAuthModal = function() {
      const modal = document.getElementById('auth-modal');
      if (modal) modal.style.display = 'none';
    };
  </script>
"""

# Insert early script right before </head>
if 'EARLY SCRIPT: DEFINES INTRO VIDEO & AUTH MODAL HANDLERS' not in html:
    html = html.replace('</head>', early_video_script + '\n</head>')
    print("✓ Injected Early Video & Auth Opener Script into <head> of index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)
html = re.sub(r'app_intro_cinematic\.mp4(\?v=\d+)?', f'app_intro_cinematic.mp4?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ index.html saved with Early Script in <head> (v={ts})")
