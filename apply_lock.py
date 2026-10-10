import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

print("Applying Locked state to Epic Games...")

# 1. Update epic_games.css
lock_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🔒 EPIC GAMES LOCKED STATE STYLES (अभी लॉक है)
   ══════════════════════════════════════════════════════════════════════════════ */
.btn-locked {
  background: linear-gradient(135deg, #4B5563, #374151) !important;
  color: #E5E7EB !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  box-shadow: none !important;
  cursor: pointer !important;
}

.epic-card-lock-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(17, 24, 39, 0.88);
  backdrop-filter: blur(8px);
  border: 1px solid #F59E0B;
  color: #FDE68A;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 4px;
  z-index: 5;
  box-shadow: 0 4px 10px rgba(0,0,0,0.4);
}

.epic-game-menu-card.is-locked .epic-card-cover-img {
  filter: grayscale(35%) brightness(0.72);
}

.epic-card-lock-watermark {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(15, 10, 25, 0.45);
  backdrop-filter: blur(1.5px);
  z-index: 4;
  pointer-events: none;
  border-radius: 16px 16px 0 0;
}

.epic-card-lock-watermark .lock-icon-lg {
  font-size: 2.2rem;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.6));
  animation: lockPulse 2.5s infinite ease-in-out;
}

.epic-card-lock-watermark .lock-label-sm {
  color: #FDE68A;
  font-size: 0.72rem;
  font-weight: 900;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  margin-top: 4px;
  background: rgba(0,0,0,0.65);
  padding: 2px 8px;
  border-radius: 8px;
  border: 1px solid rgba(245,158,11,0.4);
}

@keyframes lockPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.08); }
}

/* Modal Overlay for Lock Announcement */
.epic-locked-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 50000;
  background: rgba(10, 6, 20, 0.85);
  backdrop-filter: blur(12px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
  animation: fadeIn 0.25s ease-out;
}

.epic-locked-modal-box {
  background: linear-gradient(145deg, #1F1530 0%, #120A20 100%);
  border: 2px solid #F59E0B;
  border-radius: 26px;
  padding: 28px 22px 24px;
  max-width: 360px;
  width: 100%;
  text-align: center;
  box-shadow: 0 20px 50px rgba(0,0,0,0.7), 0 0 35px rgba(245,158,11,0.25);
  position: relative;
}

.epic-locked-icon-orb {
  width: 76px;
  height: 76px;
  margin: 0 auto 16px;
  background: radial-gradient(circle, #FDE68A 0%, #D97706 60%, #78350F 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.4rem;
  box-shadow: 0 10px 25px rgba(217, 119, 6, 0.5), inset 0 2px 4px rgba(255,255,255,0.8);
  animation: lockPulse 2s infinite ease-in-out;
}

.epic-locked-status-chip {
  display: inline-block;
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid #EF4444;
  color: #FCA5A5;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 3px 12px;
  border-radius: 12px;
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}

.epic-locked-modal-title {
  color: #FFFDF8;
  font-size: 1.3rem;
  font-weight: 900;
  margin-bottom: 8px;
}

.epic-locked-modal-desc {
  color: #D8B4FE;
  font-size: 0.88rem;
  line-height: 1.5;
  margin-bottom: 20px;
}

.epic-locked-btn-ok {
  width: 100%;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  border: none;
  border-radius: 16px;
  padding: 12px 0;
  font-weight: 900;
  font-size: 0.95rem;
  cursor: pointer;
  box-shadow: 0 6px 20px rgba(248, 200, 59, 0.4);
  transition: transform 0.15s ease;
}

.epic-locked-btn-ok:active {
  transform: scale(0.97);
}

.epic-locked-toast {
  position: fixed;
  bottom: 84px;
  left: 50%;
  transform: translateX(-50%) translateY(30px);
  background: rgba(17, 24, 39, 0.95);
  border: 1.5px solid #F59E0B;
  color: #FFFDF8;
  padding: 10px 18px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.5);
  z-index: 60000;
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.epic-locked-toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
  pointer-events: auto;
}
"""

with open('epic_games.css', 'a', encoding='utf-8') as f:
    f.write(lock_css)
print("Added lock styles to epic_games.css")

# 2. Update epic_games_engine.js with lock logic
lock_js_additions = """
/* ══════════════════════════════════════════════════════════════════════════════
   🔒 EPIC GAMES LOCK / UNLOCK ENGINE LOGIC
   ══════════════════════════════════════════════════════════════════════════════ */
window.IS_EPIC_GAMES_LOCKED = true;

window.showEpicGameLockedNotice = function(e) {
  if (e && e.stopPropagation) e.stopPropagation();
  var modal = document.getElementById('epic-locked-modal');
  if (modal) {
    modal.style.display = 'flex';
  } else {
    showEpicLockedToast('🔒 एपिक गेम्स अभी लॉक है! शीघ्र आ रहा है।');
  }
};

window.closeEpicLockedModal = function() {
  var modal = document.getElementById('epic-locked-modal');
  if (modal) modal.style.display = 'none';
};

window.showEpicLockedToast = function(msg) {
  var toast = document.getElementById('epic-locked-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'epic-locked-toast';
    toast.className = 'epic-locked-toast';
    document.body.appendChild(toast);
  }
  toast.innerHTML = '<span>🔒</span> <span>' + (msg || 'यह खेल अभी लॉक है! शीघ्र आ रहा है।') + '</span>';
  toast.classList.add('show');
  setTimeout(function() {
    toast.classList.remove('show');
  }, 2800);
};

// Hook open methods to enforce lock
var _origOpenSwipe = window.openSwipeGame;
window.openSwipeGame = function(theme) {
  if (window.IS_EPIC_GAMES_LOCKED) {
    window.showEpicGameLockedNotice();
    return;
  }
  if (_origOpenSwipe) _origOpenSwipe(theme);
};

var _origOpenMatch = window.openMatchGame;
window.openMatchGame = function() {
  if (window.IS_EPIC_GAMES_LOCKED) {
    window.showEpicGameLockedNotice();
    return;
  }
  if (_origOpenMatch) _origOpenMatch();
};

var _origOpenJigsaw = window.openJigsawGame;
window.openJigsawGame = function() {
  if (window.IS_EPIC_GAMES_LOCKED) {
    window.showEpicGameLockedNotice();
    return;
  }
  if (_origOpenJigsaw) _origOpenJigsaw();
};

var _origOpenPada = window.openPadabandhamGame;
window.openPadabandhamGame = function() {
  if (window.IS_EPIC_GAMES_LOCKED) {
    window.showEpicGameLockedNotice();
    return;
  }
  if (_origOpenPada) _origOpenPada();
};

window.unlockEpicGames = function() {
  window.IS_EPIC_GAMES_LOCKED = false;
  document.querySelectorAll('.epic-game-menu-card').forEach(function(card) {
    card.classList.remove('is-locked');
  });
  document.querySelectorAll('.epic-card-play-btn').forEach(function(btn) {
    btn.classList.remove('btn-locked');
    btn.innerHTML = '🎮 Play';
  });
  var bannerBtn = document.querySelector('.home-epic-games-banner button');
  if (bannerBtn) {
    bannerBtn.innerHTML = 'खेलें ❯';
    bannerBtn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
  }
  alert('🔓 Epic Games Unlocked!');
};
"""

with open('epic_games_engine.js', 'a', encoding='utf-8') as f:
    f.write(lock_js_additions)
print("Added lock engine logic to epic_games_engine.js")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Home Page Banner with Locked version
old_banner_start = html.find('<!-- 🎮 EPIC GAMES HOME BANNER')
old_banner_end = html.find('</div>\n      </div>', old_banner_start) + len('</div>\n      </div>')

new_locked_banner = """<!-- 🎮 EPIC GAMES HOME BANNER (LOCKED / सुरक्षित - अभी लॉक है) 🎮 -->
      <div class="home-epic-games-banner home-promo-banner-card" onclick="showEpicGameLockedNotice(event)" style="opacity: 0.95; border: 1.5px solid rgba(245,158,11,0.6); background: linear-gradient(135deg, rgba(35, 20, 60, 0.94), rgba(20, 10, 35, 0.98)); cursor: pointer; box-shadow: 0 8px 25px rgba(0,0,0,0.5);">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div style="display:flex; align-items:center; gap:14px;">
            <div style="position:relative;">
              <div style="font-size:2.4rem; filter:drop-shadow(0 0 10px rgba(245,158,11,0.4)); opacity:0.85;">🎮</div>
              <div style="position:absolute; bottom:-3px; right:-5px; background:#EF4444; color:#FFF; font-size:0.85rem; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center; box-shadow:0 2px 6px rgba(0,0,0,0.5); border:1.5px solid #FFF;">🔒</div>
            </div>
            <div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="color:#FFFDF8; font-size:1.15rem; font-weight:900;">एपिक गेम्स (Epic Games)</span>
                <span style="background:rgba(239,68,68,0.25); border:1px solid #EF4444; color:#FCA5A5; font-size:0.72rem; font-weight:800; padding:2px 8px; border-radius:10px;">🔒 अभी लॉक है</span>
              </div>
              <div style="color:#E9D5FF; font-size:0.8rem; margin-top:3px;">शीघ्र ही अनलॉक होगा • ४ दिव्य महाकाव्य खेल ❯</div>
            </div>
          </div>
          <button style="background:rgba(255,255,255,0.12); color:#FDE68A; border:1px solid rgba(245,158,11,0.4); font-weight:900; font-size:0.82rem; padding:8px 16px; border-radius:16px; display:flex; align-items:center; gap:6px; cursor:pointer; box-shadow:none;">🔒 लॉक</button>
        </div>
      </div>"""

if old_banner_start != -1 and old_banner_end != -1:
    html = html[:old_banner_start] + new_locked_banner + html[old_banner_end:]
    print("Replaced Home banner with Locked banner")

# Update 2x2 grid in page-epic-games to show Locked on every card
old_grid_start = html.find('<div class="epic-games-grid">')
old_grid_end = html.find('</section>', old_grid_start)

new_locked_grid = """<div class="epic-games-grid">
        <!-- 1. Match -->
        <div class="epic-game-menu-card is-locked" onclick="showEpicGameLockedNotice(event)">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-memory">Memory</span>
            <div class="epic-card-lock-badge">🔒 लॉक</div>
            <img src="assets/games/cover_match.jpg" alt="Match" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="epic-card-lock-watermark">
              <span class="lock-icon-lg">🔒</span>
              <span class="lock-label-sm">शीघ्र आ रहा है</span>
            </div>
          </div>
          <div class="epic-card-title">Match</div>
          <div class="epic-card-subtitle">Find and match the same card</div>
          <button class="epic-card-play-btn btn-locked">🔒 Locked</button>
        </div>

        <!-- 2. Swipe -->
        <div class="epic-game-menu-card is-locked" onclick="showEpicGameLockedNotice(event)">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-story">Story</span>
            <div class="epic-card-lock-badge">🔒 लॉक</div>
            <img src="assets/games/cover_swipe.jpg" alt="Swipe" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="epic-card-lock-watermark">
              <span class="lock-icon-lg">🔒</span>
              <span class="lock-label-sm">शीघ्र आ रहा है</span>
            </div>
          </div>
          <div class="epic-card-title">Swipe</div>
          <div class="epic-card-subtitle">Swipe to the right team</div>
          <button class="epic-card-play-btn btn-locked">🔒 Locked</button>
        </div>

        <!-- 3. JigSaw -->
        <div class="epic-game-menu-card is-locked" onclick="showEpicGameLockedNotice(event)">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-puzzle">Puzzle</span>
            <div class="epic-card-lock-badge">🔒 लॉक</div>
            <img src="assets/games/cover_jigsaw.jpg" alt="JigSaw" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="epic-card-lock-watermark">
              <span class="lock-icon-lg">🔒</span>
              <span class="lock-label-sm">शीघ्र आ रहा है</span>
            </div>
          </div>
          <div class="epic-card-title">JigSaw</div>
          <div class="epic-card-subtitle">Shape the epic characters/scenes</div>
          <button class="epic-card-play-btn btn-locked">🔒 Locked</button>
        </div>

        <!-- 4. PadaBandham -->
        <div class="epic-game-menu-card is-locked" onclick="showEpicGameLockedNotice(event)">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-word">Word</span>
            <div class="epic-card-lock-badge">🔒 लॉक</div>
            <img src="assets/games/cover_padabandham.jpg" alt="PadaBandham" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="epic-card-lock-watermark">
              <span class="lock-icon-lg">🔒</span>
              <span class="lock-label-sm">शीघ्र आ रहा है</span>
            </div>
          </div>
          <div class="epic-card-title">PadaBandham</div>
          <div class="epic-card-subtitle">Find the epic word</div>
          <button class="epic-card-play-btn btn-locked">🔒 Locked</button>
        </div>
      </div>
"""

if old_grid_start != -1 and old_grid_end != -1:
    html = html[:old_grid_start] + new_locked_grid + html[old_grid_end:]
    print("Replaced Games Grid with Locked cards")

# Add the Locked Modal popup to index.html if not already present
locked_modal_html = """
    <!-- ══════════ 🔒 EPIC GAMES LOCKED NOTICE MODAL ══════════ -->
    <div id="epic-locked-modal" class="epic-locked-modal-overlay" onclick="closeEpicLockedModal()">
      <div class="epic-locked-modal-box" onclick="event.stopPropagation()">
        <div class="epic-locked-icon-orb">🔒</div>
        <div class="epic-locked-status-chip">सुरक्षित • COMING SOON</div>
        <div class="epic-locked-modal-title">एपिक गेम्स अभी लॉक है</div>
        <div class="epic-locked-modal-desc">
          यह विशेष भक्ति गेमिंग अनुभव वर्तमान में सुरक्षित व तैयार किया गया है। आगामी संस्करण में यह सभी भक्तों के लिए अनलॉक कर दिया जाएगा।
        </div>
        <button class="epic-locked-btn-ok" onclick="closeEpicLockedModal()">समझ गया (ठीक है)</button>
      </div>
    </div>
"""

if 'id="epic-locked-modal"' not in html:
    arena_idx = html.find('id="swipe-arena"')
    if arena_idx != -1:
        parent_div = html.rfind('<div', 0, arena_idx)
        html = html[:parent_div] + locked_modal_html + html[parent_div:]
        print("Added epic-locked-modal to index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully with Locked state!")
