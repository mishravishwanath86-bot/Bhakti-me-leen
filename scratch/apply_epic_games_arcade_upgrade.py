import os
import sys
import shutil
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
ENGINE_FILE = os.path.join(BASE_DIR, "epic_games_engine.js")
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")
SYNC_FILE = os.path.join(BASE_DIR, "sync_assets.py")

VIDEO_SOURCE = r"C:\Users\vishw\OneDrive\Videos\gemini_generated_video_25353670.mp4"

print("=== 1. Ensuring Video Assets Are Present ===")
os.makedirs(os.path.join(BASE_DIR, "assets", "games"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "assets", "videos"), exist_ok=True)

dst_games_vid = os.path.join(BASE_DIR, "assets", "games", "epic_games_intro.mp4")
dst_videos_vid = os.path.join(BASE_DIR, "assets", "videos", "epic_games_intro.mp4")

if os.path.exists(VIDEO_SOURCE):
    shutil.copy2(VIDEO_SOURCE, dst_games_vid)
    shutil.copy2(VIDEO_SOURCE, dst_videos_vid)
    print(f"✓ Copied video to assets/games/epic_games_intro.mp4 ({os.path.getsize(dst_games_vid)} bytes)")
    print(f"✓ Copied video to assets/videos/epic_games_intro.mp4 ({os.path.getsize(dst_videos_vid)} bytes)")
else:
    print("⚠ Video source not found at specified OneDrive path, using existing copied files.")

print("\n=== 2. Updating sync_assets.py to Include assets/videos ===")
with open(SYNC_FILE, "r", encoding="utf-8") as f:
    sync_code = f.read()

if '"assets/videos"' not in sync_code:
    sync_code = sync_code.replace(
        '"assets/games",',
        '"assets/games",\n    "assets/videos",'
    )
    with open(SYNC_FILE, "w", encoding="utf-8") as f:
        f.write(sync_code)
    print("✓ Added assets/videos to sync_assets.py")
else:
    print("✓ assets/videos already in sync_assets.py")

print("\n=== 3. Updating index.html (Arcade Showcase Banner & Video Modal) ===")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the old home-epic-games-banner
banner_start = html.find('<!-- 🎮 EPIC GAMES HOME BANNER')
if banner_start == -1:
    banner_start = html.find('<div class="home-epic-games-banner')

banner_end = html.find('<!-- ══════════ 🧩 DIVINE BHAKTI JIGSAW PUZZLE GAME MODULE', banner_start)
if banner_end == -1:
    banner_end = html.find('<!-- ══════════ 🎮 EPIC GAMES HUB', banner_start)

if banner_start != -1 and banner_end != -1:
    # Also capture preceding </section> or whatever boundary
    old_banner_chunk = html[banner_start:banner_end]
else:
    print("Could not find exact boundaries for banner, will use regex...")
    old_banner_chunk = None

new_banner_html = """<!-- 🎮 EPIC GAMES HOME BANNER (दिव्य भक्ति क्रीड़ा स्थल - ७ अनोखे भक्ति खेल) 🎮 -->
      <div class="home-epic-games-banner home-promo-banner-card" onclick="triggerEpicGamesLaunchWithVideo('page-epic-games')">
        <!-- Top Arcade Header Badge Row -->
        <div class="home-epic-banner-top">
          <div class="home-epic-banner-badge">
            <span class="live-pulse-dot"></span>
            <span>🔴 लाइव गेमिंग ज़ोन • ७ पावन खेल</span>
          </div>
          <div class="home-epic-banner-coins">
            <span class="coin-bounce">🪙</span>
            <span>1,000+ कॉइन्स • दैनिक रिवॉर्ड</span>
          </div>
        </div>

        <!-- Hero Game Showcase Section -->
        <div class="home-epic-banner-main">
          <!-- 3D Mascot Avatar with Bal Ganesha Gaming Visual -->
          <div class="home-epic-mascot-wrap">
            <img src="assets/games/mascot_bal_ganesha.jpg" alt="Bal Ganesha Gaming Mascot" class="home-epic-mascot-img">
            <span class="home-epic-mascot-badge">🎮 3D</span>
          </div>
          <div class="home-epic-banner-titles">
            <div class="home-epic-banner-h">
              <span class="home-epic-title-gradient">दिव्य भक्ति क्रीड़ा स्थल</span>
            </div>
            <div class="home-epic-banner-sub">Sanatan Epic Games • ७ अद्वितीय आध्यात्मिक खेल</div>
            <div class="home-epic-banner-status">
              <span class="status-star">⭐</span>
              <span>सभी स्तर अनलॉक • १००% ऑफलाइन निःशुल्क</span>
            </div>
          </div>
        </div>

        <!-- 🕹️ Visual Interactive Mini-Game Showcase Rail (Shows REAL games inside!) -->
        <div class="home-epic-games-rail-wrap">
          <div class="home-epic-rail-header">
            <span class="rail-header-title">🎮 उपलब्ध भक्ति खेल (चुनें व खेलें):</span>
            <span class="rail-header-hint">स्लाइड करें ❯</span>
          </div>
          <div class="home-epic-games-rail" onclick="event.stopPropagation()">
            <!-- Mini Card 1: Swipe Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openSwipeGame('cat_1_ramayana'); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/cards/ram.jpg" alt="Swipe" class="mini-card-thumb">
                <span class="mini-card-tag tag-purple">🏹 स्वाइप</span>
              </div>
              <div class="mini-card-title">रामायण स्वाइप</div>
              <div class="mini-card-sub">अयोध्या या लंका</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>

            <!-- Mini Card 2: Jigsaw Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openJigsawGame(); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/deity_ganesh.jpg" alt="Jigsaw" class="mini-card-thumb">
                <span class="mini-card-tag tag-cyan">🧩 जिग्सॉ</span>
              </div>
              <div class="mini-card-title">दिव्य जिग्सॉ</div>
              <div class="mini-card-sub">५० पावन स्तर</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>

            <!-- Mini Card 3: Card Match Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openMatchGame(); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/deity_krishna.jpg" alt="Match" class="mini-card-thumb">
                <span class="mini-card-tag tag-orange">🎴 कार्ड मैच</span>
              </div>
              <div class="mini-card-title">स्मृति चक्र</div>
              <div class="mini-card-sub">३० स्तर मेमोरी</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>

            <!-- Mini Card 4: Phool Arpan Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openPhoolArpanGame(); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/games/cover_phool_arpan.jpg" alt="Arpan" class="mini-card-thumb">
                <span class="mini-card-tag tag-amber">🌸 अर्पण</span>
              </div>
              <div class="mini-card-title">पुष्प अर्पण</div>
              <div class="mini-card-sub">स्वर्ण थाली भेंट</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>

            <!-- Mini Card 5: Aarti Puzzle Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openAartiGame(); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/aarti.jpg" alt="Aarti" class="mini-card-thumb">
                <span class="mini-card-tag tag-gold">🪔 आरती पहेली</span>
              </div>
              <div class="mini-card-title">आरती पहेली</div>
              <div class="mini-card-sub">पंक्तियाँ सजाएँ</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>

            <!-- Mini Card 6: Mantra Puzzle Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openMantraGame(); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/deity_shiva.jpg" alt="Mantra" class="mini-card-thumb">
                <span class="mini-card-tag tag-purple">🕉️ मन्त्र पहेली</span>
              </div>
              <div class="mini-card-title">मन्त्र पहेली</div>
              <div class="mini-card-sub">वैदिक श्लोक</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>

            <!-- Mini Card 7: PadaBandham Game -->
            <div class="home-epic-mini-card" onclick="triggerEpicGamesLaunchWithVideo(null, function(){ openPadabandhamGame(); })">
              <div class="mini-card-thumb-wrap">
                <img src="assets/deity_hanuman.jpg" alt="Word" class="mini-card-thumb">
                <span class="mini-card-tag tag-yellow">🔤 पदबन्धम</span>
              </div>
              <div class="mini-card-title">शब्द पहेली</div>
              <div class="mini-card-sub">शास्त्र शब्द खोज</div>
              <div class="mini-card-play-action">▶ खेलें</div>
            </div>
          </div>
        </div>

        <!-- Banner Footer Row -->
        <div class="home-epic-banner-footer">
          <div class="home-epic-features-text">
            <span>⚡ १००% ऑफलाइन</span>
            <span class="feature-dot">•</span>
            <span>🛡️ बिना विज्ञापन</span>
            <span class="feature-dot">•</span>
            <span>🎁 दैनिक पुरस्कार</span>
          </div>
          <button class="home-epic-cta-btn" onclick="event.stopPropagation(); triggerEpicGamesLaunchWithVideo('page-epic-games');">
            <span class="cta-sparkle">✨</span>
            <span class="cta-text">खेलें (Play Arena)</span>
            <span class="cta-arrow">❯</span>
          </button>
        </div>
      </div>
"""

video_modal_html = """<!-- ══════════ 🎬 CINEMATIC EPIC GAMES INTRO VIDEO MODAL ══════════ -->
    <div id="epic-games-video-modal" class="epic-games-video-modal" style="display:none;">
      <div class="epic-video-overlay-backdrop"></div>
      <div class="epic-video-shell">
        <!-- Floating Cinematic Header -->
        <div class="epic-video-topbar">
          <div class="epic-video-brand">
            <span class="epic-video-brand-icon">🎮</span>
            <span class="epic-video-brand-text">दिव्य भक्ति क्रीड़ा स्थल</span>
          </div>
          <button type="button" class="epic-video-skip-pill" onclick="skipEpicGamesIntroVideo()" title="Skip Video">
            <span>खेल शुरू करें (Skip)</span>
            <span class="skip-arrow">❯❯</span>
          </button>
        </div>

        <!-- Video Player Wrapper -->
        <div class="epic-video-player-wrap">
          <video id="epic-games-intro-video" 
                 playsinline 
                 webkit-playsinline 
                 preload="auto"
                 src="assets/games/epic_games_intro.mp4">
          </video>
          <div id="epic-video-loader" class="epic-video-loader" style="display:none;">
            <div class="epic-loader-spin"></div>
            <div class="epic-loader-text">शुभ आरंभ...</div>
          </div>
        </div>

        <!-- Bottom Status Hint -->
        <div class="epic-video-bottom-hint">
          <span>✨ वीडियो समाप्त होते ही खेल प्रारंभ होगा</span>
        </div>
      </div>
    </div>
"""

if old_banner_chunk:
    html = html.replace(old_banner_chunk, new_banner_html)
    print("✓ Replaced home-epic-games-banner with new Arcade Showcase")
else:
    # Use regex
    banner_regex = re.compile(r'<div class="home-epic-games-banner[\s\S]*?</div>\s*</div>\s*(?=<!-- ══════════ (?:🧩|🎮))', re.MULTILINE)
    html = banner_regex.sub(new_banner_html, html, count=1)
    print("✓ Replaced home-epic-games-banner using regex")

# Add video modal if not already added
if 'id="epic-games-video-modal"' not in html:
    hub_pos = html.find('id="page-epic-games"')
    if hub_pos != -1:
        sec_start = html.rfind('<section', 0, hub_pos)
        html = html[:sec_start] + video_modal_html + "\n    " + html[sec_start:]
        print("✓ Inserted #epic-games-video-modal before #page-epic-games in index.html")
    else:
        # Append before closing body
        html = html.replace("</body>", video_modal_html + "\n</body>")
        print("✓ Appended #epic-games-video-modal before </body>")
else:
    print("✓ #epic-games-video-modal already present in index.html")

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Saved index.html")

print("\n=== 4. Updating epic_games_engine.js with Video Intro Launch Logic ===")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine_code = f.read()

video_js_logic = """
/* ══════════════════════════════════════════════════════════════════════════════
   🎬 CINEMATIC EPIC GAMES INTRO VIDEO CONTROLLER
   ══════════════════════════════════════════════════════════════════════════════ */
var pendingGameDestination = 'page-epic-games';
var pendingGameCallback = null;

function triggerEpicGamesLaunchWithVideo(destination, callback) {
  pendingGameDestination = destination || 'page-epic-games';
  pendingGameCallback = (typeof callback === 'function') ? callback : null;

  var modal = document.getElementById('epic-games-video-modal');
  var video = document.getElementById('epic-games-intro-video');

  if (!modal || !video) {
    proceedToTargetGame();
    return;
  }

  // Attempt to pause any ambient audio
  if (typeof pauseAllAudio === 'function') {
    try { pauseAllAudio(); } catch (e) {}
  }
  if (typeof pauseMusic === 'function') {
    try { pauseMusic(); } catch (e) {}
  }

  modal.style.display = 'flex';
  // Trigger animation next frame
  requestAnimationFrame(function() {
    modal.classList.add('active');
  });

  // Video completion listener: automatically open game when finished
  video.onended = function() {
    closeVideoAndOpenGame();
  };

  // Error fallback: proceed directly if video fails to play
  video.onerror = function() {
    console.warn('Intro video error, proceeding directly to game.');
    closeVideoAndOpenGame();
  };

  // Play video
  try {
    video.currentTime = 0;
    var playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise.catch(function(err) {
        console.warn('Autoplay error / user interaction required:', err);
      });
    }
  } catch (err) {
    console.warn('Video play exception:', err);
  }
}

function skipEpicGamesIntroVideo() {
  closeVideoAndOpenGame();
}

function closeVideoAndOpenGame() {
  var modal = document.getElementById('epic-games-video-modal');
  var video = document.getElementById('epic-games-intro-video');

  if (video) {
    try {
      video.pause();
      video.onended = null;
      video.onerror = null;
    } catch (e) {}
  }

  if (modal) {
    modal.classList.remove('active');
    setTimeout(function() {
      modal.style.display = 'none';
    }, 280);
  }

  proceedToTargetGame();
}

function proceedToTargetGame() {
  if (pendingGameCallback) {
    var cb = pendingGameCallback;
    pendingGameCallback = null;
    cb();
  } else if (pendingGameDestination) {
    var dest = pendingGameDestination;
    pendingGameDestination = 'page-epic-games';
    if (typeof showPage === 'function') {
      showPage(dest);
    }
  }
}

// Expose globally on window
window.triggerEpicGamesLaunchWithVideo = triggerEpicGamesLaunchWithVideo;
window.skipEpicGamesIntroVideo = skipEpicGamesIntroVideo;
window.closeVideoAndOpenGame = closeVideoAndOpenGame;
"""

if "triggerEpicGamesLaunchWithVideo" not in engine_code:
    engine_code += "\n" + video_js_logic
    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write(engine_code)
    print("✓ Added Video Controller to epic_games_engine.js")
else:
    print("✓ triggerEpicGamesLaunchWithVideo already in epic_games_engine.js")

print("\n=== 5. Updating epic_games.css with Arcade Banner & Video Modal Styles ===")
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css_code = f.read()

arcade_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🎮 UPGRADED DIVYA BHAKTI KRIDA STHAL (ARCADE GAMING HUB BANNER)
   ══════════════════════════════════════════════════════════════════════════════ */
.home-epic-games-banner {
  margin: 0.6rem 1rem 1.6rem !important;
  background: radial-gradient(circle at 90% 10%, rgba(245, 158, 11, 0.28) 0%, transparent 55%),
              radial-gradient(circle at 10% 90%, rgba(124, 58, 237, 0.25) 0%, transparent 50%),
              linear-gradient(135deg, #1C0830 0%, #0F041D 45%, #250A3E 100%) !important;
  border: 2px solid #F59E0B !important;
  border-radius: 26px !important;
  padding: 1.2rem !important;
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.75), 0 0 28px rgba(245, 158, 11, 0.25) inset !important;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  user-select: none;
}

.home-epic-games-banner:active {
  transform: scale(0.99);
}

/* Pulsing live dot */
.live-pulse-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #EF4444;
  box-shadow: 0 0 8px #EF4444;
  animation: liveDotPulse 1.4s infinite ease-in-out;
}

@keyframes liveDotPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.35); opacity: 0.6; }
}

.coin-bounce {
  display: inline-block;
  animation: coinBounce 2s infinite ease-in-out;
}

@keyframes coinBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-2.5px); }
}

/* Mascot Avatar Wrap */
.home-epic-mascot-wrap {
  position: relative;
  width: 68px;
  height: 68px;
  border-radius: 20px;
  border: 2px solid #F59E0B;
  box-shadow: 0 6px 18px rgba(245, 158, 11, 0.45), 0 0 12px rgba(245, 158, 11, 0.3) inset;
  flex-shrink: 0;
  overflow: visible;
  background: #2D0B40;
}

.home-epic-mascot-img {
  width: 100%;
  height: 100%;
  border-radius: 18px;
  object-fit: cover;
  display: block;
}

.home-epic-mascot-badge {
  position: absolute;
  bottom: -4px;
  right: -6px;
  background: linear-gradient(135deg, #F59E0B, #DC2626);
  color: #FFF;
  font-size: 0.58rem;
  font-weight: 900;
  padding: 2px 5px;
  border-radius: 6px;
  border: 1px solid #FEF08A;
  box-shadow: 0 2px 6px rgba(0,0,0,0.5);
  letter-spacing: 0.5px;
}

.home-epic-title-gradient {
  background: linear-gradient(135deg, #FFFBEB 0%, #FDE68A 45%, #F59E0B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 1.25rem;
  font-weight: 900;
  letter-spacing: 0.4px;
}

.home-epic-banner-status {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.7rem;
  font-weight: 800;
  color: #86EFAC;
  margin-top: 3px;
}

.status-star {
  font-size: 0.75rem;
  color: #FBBF24;
}

/* 🕹️ Horizontal Mini Game Preview Rail */
.home-epic-games-rail-wrap {
  margin: 12px 0 10px;
  width: 100%;
}

.home-epic-rail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 7px;
  padding: 0 2px;
}

.rail-header-title {
  font-size: 0.74rem;
  font-weight: 800;
  color: #E9D5FF;
}

.rail-header-hint {
  font-size: 0.65rem;
  font-weight: 700;
  color: #F59E0B;
  opacity: 0.9;
}

.home-epic-games-rail {
  display: flex;
  gap: 10px;
  overflow-x: auto;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  padding: 4px 2px 8px;
  scrollbar-width: none;
}

.home-epic-games-rail::-webkit-scrollbar {
  display: none;
}

.home-epic-mini-card {
  flex: 0 0 100px;
  background: rgba(255, 255, 255, 0.06);
  border: 1.4px solid rgba(245, 158, 11, 0.4);
  border-radius: 14px;
  padding: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  position: relative;
  overflow: hidden;
}

.home-epic-mini-card:active {
  transform: scale(0.95);
  border-color: #F59E0B;
}

.mini-card-thumb-wrap {
  width: 100%;
  height: 64px;
  border-radius: 10px;
  position: relative;
  overflow: hidden;
  margin-bottom: 5px;
}

.mini-card-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.mini-card-tag {
  position: absolute;
  top: 3px;
  left: 3px;
  font-size: 0.52rem;
  font-weight: 900;
  color: #FFF;
  padding: 1px 5px;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.6);
  line-height: 1.1;
}

.tag-purple { background: linear-gradient(135deg, #7C3AED, #9333EA); }
.tag-cyan { background: linear-gradient(135deg, #0891B2, #0284C7); }
.tag-orange { background: linear-gradient(135deg, #EA580C, #C2410C); }
.tag-amber { background: linear-gradient(135deg, #D97706, #B45309); }
.tag-gold { background: linear-gradient(135deg, #B45309, #78350F); border: 0.8px solid #FDE68A; }
.tag-yellow { background: linear-gradient(135deg, #CA8A04, #A16207); }

.mini-card-title {
  font-size: 0.72rem;
  font-weight: 900;
  color: #FFFDF8;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  line-height: 1.2;
}

.mini-card-sub {
  font-size: 0.58rem;
  color: #D8B4FE;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  margin-top: 1px;
}

.mini-card-play-action {
  margin-top: 4px;
  width: 100%;
  background: linear-gradient(135deg, #F59E0B, #D97706);
  color: #1A0B2E;
  font-size: 0.62rem;
  font-weight: 900;
  padding: 2px 0;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(245, 158, 11, 0.4);
}

/* 3D Glowing CTA Button */
.home-epic-cta-btn {
  background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 40%, #D97706 100%) !important;
  color: #1A0B2E !important;
  font-size: 0.85rem !important;
  font-weight: 900 !important;
  padding: 8px 18px !important;
  border-radius: 18px !important;
  border: 1.5px solid #FFFBEB !important;
  box-shadow: 0 4px 18px rgba(245, 158, 11, 0.6), 0 0 10px rgba(254, 240, 138, 0.5) inset !important;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  animation: ctaGlowPulse 2.5s infinite ease-in-out;
}

@keyframes ctaGlowPulse {
  0%, 100% { box-shadow: 0 4px 18px rgba(245, 158, 11, 0.6), 0 0 8px rgba(254, 240, 138, 0.4) inset; }
  50% { box-shadow: 0 6px 26px rgba(245, 158, 11, 0.9), 0 0 16px rgba(254, 240, 138, 0.8) inset; }
}

.home-epic-cta-btn:active {
  transform: scale(0.94);
}

.feature-dot {
  opacity: 0.4;
  margin: 0 1px;
}

/* ══════════════════════════════════════════════════════════════════════════════
   🎬 FULLSCREEN CINEMATIC INTRO VIDEO MODAL
   ══════════════════════════════════════════════════════════════════════════════ */
.epic-games-video-modal {
  position: fixed;
  inset: 0;
  z-index: 55000;
  background: #000000;
  display: none;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.28s ease;
  user-select: none;
}

.epic-games-video-modal.active {
  opacity: 1;
}

.epic-video-overlay-backdrop {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle, rgba(20, 10, 30, 0.7) 0%, #000 100%);
  pointer-events: none;
}

.epic-video-shell {
  position: relative;
  width: 100%;
  height: 100%;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

.epic-video-topbar {
  position: absolute;
  top: 14px;
  left: 14px;
  right: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 10;
  pointer-events: auto;
}

.epic-video-brand {
  display: flex;
  align-items: center;
  gap: 7px;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(10px);
  border: 1.2px solid rgba(245, 158, 11, 0.5);
  border-radius: 20px;
  padding: 5px 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5);
}

.epic-video-brand-icon {
  font-size: 1rem;
}

.epic-video-brand-text {
  font-size: 0.8rem;
  font-weight: 900;
  color: #FFFDF8;
  letter-spacing: 0.3px;
}

.epic-video-skip-pill {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.95), rgba(217, 119, 6, 0.95));
  border: 1.5px solid #FEF08A;
  border-radius: 20px;
  color: #1A0B2E;
  font-size: 0.76rem;
  font-weight: 900;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.5);
  transition: transform 0.15s ease;
}

.epic-video-skip-pill:active {
  transform: scale(0.94);
}

.epic-video-player-wrap {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000;
  position: relative;
}

#epic-games-intro-video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: #000;
}

.epic-video-bottom-hint {
  position: absolute;
  bottom: 22px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.68);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(245, 158, 11, 0.35);
  border-radius: 16px;
  padding: 5px 16px;
  font-size: 0.72rem;
  font-weight: 800;
  color: #FDE68A;
  z-index: 10;
  white-space: nowrap;
  pointer-events: none;
  box-shadow: 0 4px 12px rgba(0,0,0,0.6);
}
"""

if ".epic-games-video-modal" not in css_code:
    css_code += "\n" + arcade_css
    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(css_code)
    print("✓ Added Arcade Banner and Video Modal styles to epic_games.css")
else:
    print("✓ Arcade styles already present in epic_games.css")

print("\n=== All Upgrades Completed Successfully ===")
