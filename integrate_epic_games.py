import shutil
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

backup_file = "index.html.bak_before_epic_games"
shutil.copyfile("index.html", backup_file)
print(f"Created backup at {backup_file}")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add epic_games.css into <head>
css_link = '  <link rel="stylesheet" href="epic_games.css">\n'
if 'href="epic_games.css"' not in html:
    head_end = html.find('</head>')
    html = html[:head_end] + css_link + html[head_end:]
    print("Added epic_games.css into <head>")

# 2. Add Home Page Epic Games Banner right before </section> of page-home
home_banner_html = """
      <!-- 🎮 EPIC GAMES HOME BANNER (महाकाव्य भक्ति गेम्स हब) 🎮 -->
      <div class="home-epic-games-banner home-promo-banner-card" onclick="showPage('page-epic-games')">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div style="display:flex; align-items:center; gap:14px;">
            <div style="font-size:2.4rem; filter:drop-shadow(0 0 12px #F59E0B); animation: pulse 2s infinite;">🎮</div>
            <div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="color:#FFFDF8; font-size:1.15rem; font-weight:900;">एपिक गेम्स (Epic Games)</span>
                <span style="background:rgba(245,158,11,0.25); border:1px solid #F59E0B; color:#FDE68A; font-size:0.72rem; font-weight:800; padding:2px 8px; border-radius:10px;">४ दिव्य खेल</span>
              </div>
              <div style="color:#E9D5FF; font-size:0.8rem; margin-top:3px;">स्वाइप, स्मृति मिलान, पहेली व शब्द ग्रिड ❯</div>
            </div>
          </div>
          <button style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-weight:900; font-size:0.85rem; padding:8px 18px; border-radius:16px; box-shadow:0 4px 15px rgba(248,200,59,0.4); cursor:pointer;">खेलें ❯</button>
        </div>
      </div>
"""

page_home_end = html.find('</section>', html.find('id="page-home"'))
if 'home-epic-games-banner' not in html:
    html = html[:page_home_end] + home_banner_html + html[page_home_end:]
    print("Added Epic Games banner to page-home")

# 3. Add Epic Games Hub Page and All Game Arenas right after </section> of page-home
page_home_end_after = html.find('</section>', html.find('id="page-home"')) + len('</section>')

epic_games_hub_and_modals = """

    <!-- ══════════ 🎮 EPIC GAMES HUB (Exact WhatsApp Video Frame 0 Style) ══════════ -->
    <section id="page-epic-games" class="page" style="display:none; padding-bottom:90px; background:#F5EFE6; min-height:100vh;">
      <!-- Sticky Header -->
      <div class="epic-hub-header">
        <div style="display:flex; align-items:center; gap:12px;">
          <button class="back-btn" data-back="page-home" onclick="showPage('page-home')" style="background:none; border:none; font-size:1.5rem; font-weight:900; color:#2D1400; cursor:pointer;">←</button>
          <h2 style="margin:0; font-size:1.25rem; font-weight:900; color:#2D1400;">Epic Games</h2>
        </div>
        <div style="display:flex; align-items:center; gap:10px;">
          <div style="background:#FFFBF0; border:1.5px solid #F59E0B; border-radius:18px; padding:3px 12px; display:flex; align-items:center; gap:6px; font-weight:900; font-size:0.9rem; color:#2D1400; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            <span>🪙</span>
            <span class="epic-coins-val">1K</span>
          </div>
        </div>
      </div>

      <!-- 2x2 Grid matching frame_000_0s.jpg -->
      <div class="epic-games-grid">
        <!-- 1. Match -->
        <div class="epic-game-menu-card" onclick="openMatchGame()">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-memory">Memory</span>
            <img src="assets/games/cover_match.jpg" alt="Match" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          </div>
          <div class="epic-card-title">Match</div>
          <div class="epic-card-subtitle">Find and match the same card</div>
          <button class="epic-card-play-btn btn-purple">🎮 Play</button>
        </div>

        <!-- 2. Swipe (The exact WhatsApp video game!) -->
        <div class="epic-game-menu-card" onclick="openSwipeGame('ayodhya_mithila')">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-story">Story</span>
            <img src="assets/games/cover_swipe.jpg" alt="Swipe" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          </div>
          <div class="epic-card-title">Swipe</div>
          <div class="epic-card-subtitle">Swipe to the right team</div>
          <button class="epic-card-play-btn btn-blue">🎮 Play</button>
        </div>

        <!-- 3. JigSaw -->
        <div class="epic-game-menu-card" onclick="openJigsawGame()">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-puzzle">Puzzle</span>
            <img src="assets/games/cover_jigsaw.jpg" alt="JigSaw" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          </div>
          <div class="epic-card-title">JigSaw</div>
          <div class="epic-card-subtitle">Shape the epic characters/scenes</div>
          <button class="epic-card-play-btn btn-cyan">🎮 Play</button>
        </div>

        <!-- 4. PadaBandham -->
        <div class="epic-game-menu-card" onclick="openPadabandhamGame()">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-word">Word</span>
            <img src="assets/games/cover_padabandham.jpg" alt="PadaBandham" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          </div>
          <div class="epic-card-title">PadaBandham</div>
          <div class="epic-card-subtitle">Find the epic word</div>
          <button class="epic-card-play-btn btn-gold">🎮 Play</button>
        </div>
      </div>
    </section>

    <!-- ══════════ 🏹 SWIPE GAME ARENA (The Exact Video Screen) ══════════ -->
    <div id="swipe-arena" class="swipe-game-arena">
      <!-- Top Bar -->
      <div class="swipe-top-bar">
        <button class="swipe-close-btn" onclick="closeSwipeGame()">✕</button>
        <div class="swipe-cat-dropdown" onclick="newSwipeGame()">
          <span id="swipe-cat-title">श्रेणियाँ</span> <span>∨</span>
        </div>
        <div class="swipe-header-actions">
          <button class="swipe-lang-btn">A <span style="font-size:0.75rem;">अ</span></button>
          <button class="swipe-settings-btn">⚙️</button>
        </div>
      </div>

      <!-- Coin Banner -->
      <div class="swipe-coin-banner">
        <span class="swipe-coin-icon">🪙</span>
        <span class="swipe-coin-amount epic-coins-val">1K</span>
      </div>

      <!-- Dynamic Instruction -->
      <div class="swipe-instruction-text" id="swipe-instruction">अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें</div>

      <!-- 3D Card Deck Stage -->
      <div class="swipe-card-deck-stage" id="swipe-card-deck">
        <!-- Injected dynamically by epic_games_engine.js -->
      </div>

      <!-- Quick Desktop Swipe Buttons (Accessibility) -->
      <div style="display:flex; gap:16px; margin-bottom:4px; z-index:10;">
        <button onclick="swipeCardManual('left')" style="background:rgba(124,58,237,0.88); color:#FFF; border:1.5px solid #F59E0B; border-radius:14px; padding:6px 14px; font-weight:900; font-size:0.8rem; cursor:pointer; box-shadow:0 3px 10px rgba(0,0,0,0.3);">⟵ बाएँ (अयोध्या)</button>
        <button onclick="swipeCardManual('right')" style="background:rgba(220,38,38,0.88); color:#FFF; border:1.5px solid #F59E0B; border-radius:14px; padding:6px 14px; font-weight:900; font-size:0.8rem; cursor:pointer; box-shadow:0 3px 10px rgba(0,0,0,0.3);">दाएँ (मिथिला) ⟶</button>
      </div>

      <!-- Two Bottom Shrines/Portals -->
      <div class="swipe-portals-container">
        <!-- Left Portal (Ayodhya) -->
        <div class="swipe-portal-shrine" id="swipe-portal-left" onclick="swipeCardManual('left')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/games/portal_ayodhya.jpg" alt="अयोध्या" class="swipe-portal-bg">
            <div class="swipe-portal-score-badge score-ayodhya" id="swipe-left-score">0</div>
          </div>
          <div class="swipe-portal-label" id="swipe-left-portal-label">अयोध्या</div>
        </div>

        <!-- Right Portal (Mithila) -->
        <div class="swipe-portal-shrine" id="swipe-portal-right" onclick="swipeCardManual('right')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/games/portal_mithila.jpg" alt="मिथिला" class="swipe-portal-bg">
            <div class="swipe-portal-score-badge score-mithila" id="swipe-right-score">0</div>
          </div>
          <div class="swipe-portal-label" id="swipe-right-portal-label">मिथिला</div>
        </div>
      </div>
    </div>

    <!-- ══════════ 📜 CHARACTER REVIEW ARENA (frame_018_71s.jpg) ══════════ -->
    <div id="swipe-review-arena" class="swipe-review-arena">
      <!-- Top Bar -->
      <div class="swipe-review-top-bar">
        <button class="swipe-close-btn" onclick="closeSwipeReview()">✕</button>
        <div class="swipe-review-back-circle" onclick="closeSwipeReview()">←</div>
        <div class="swipe-cat-dropdown">
          <span>श्रेणियाँ</span> <span>∨</span>
        </div>
        <div class="swipe-header-actions">
          <button class="swipe-lang-btn">A <span style="font-size:0.75rem;">अ</span></button>
          <button class="swipe-settings-btn">⚙️</button>
        </div>
      </div>

      <!-- Coin Banner -->
      <div class="swipe-coin-banner" style="margin-top:0;">
        <span class="swipe-coin-icon">🪙</span>
        <span class="swipe-coin-amount epic-coins-val">1K</span>
      </div>

      <!-- Center Detailed Card Container -->
      <div id="swipe-review-card-container">
        <!-- Rendered by epic_games_engine.js -->
      </div>

      <!-- Bottom Token Rail: "देखने के लिए टैप करें" -->
      <div class="swipe-review-bottom-rail">
        <div class="swipe-review-rail-heading">देखने के लिए टैप करें</div>
        <div class="swipe-tokens-scroll-wrap" id="swipe-review-tokens-rail">
          <!-- Populated dynamically with tokens & checkmarks -->
        </div>
      </div>
    </div>

    <!-- ══════════ 🏆 SWIPE RESULT / TRY AGAIN MODAL (frame_84s.jpg) ══════════ -->
    <div id="swipe-result-modal" class="swipe-result-modal-overlay">
      <div class="swipe-result-box">
        <div class="swipe-result-ribbon" id="swipe-result-ribbon-text">शानदार विजय!</div>
        <div class="swipe-result-stats" id="swipe-result-score-text">आपने पूरे किए 10/12 पात्र</div>
        <div class="swipe-result-score-chip">
          <span>🔄</span>
          <span id="swipe-result-streak-count">10</span>
        </div>
        <div class="swipe-result-heading" id="swipe-result-heading">बढ़िया प्रयास!</div>
        <div class="swipe-result-message" id="swipe-result-message">कुछ पात्रों को एक और कोशिश चाहिए</div>
        
        <div class="swipe-result-btns-row">
          <button class="btn-learn-lore" onclick="showCharacterReviewScreen(); hideSwipeResultModal();">📖 जानें</button>
          <button class="btn-retry-round" onclick="retrySwipeRound()">🔄 फिर से</button>
        </div>
        <button class="swipe-result-new-game-btn" onclick="newSwipeGame()">▶ नया खेल</button>
        <a class="swipe-result-home-link" onclick="hideSwipeResultModal(); closeSwipeGame(); showPage('page-epic-games');">होम पर वापस</a>
      </div>
    </div>

    <!-- ══════════ 🎴 1. MATCH GAME MODAL ══════════ -->
    <div id="match-game-modal" class="modal-overlay" style="display:none; z-index:35000; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); position:fixed; inset:0; align-items:center; justify-content:center; padding:16px;">
      <div style="background:#FFFDF8; border:3px solid #F59E0B; border-radius:24px; width:100%; max-width:420px; padding:20px; position:relative; box-shadow:0 12px 35px rgba(0,0,0,0.6);">
        <button onclick="closeMatchGame()" style="position:absolute; top:12px; right:14px; background:none; border:none; font-size:1.5rem; font-weight:900; color:#2D1400; cursor:pointer;">✕</button>
        <div style="font-size:1.25rem; font-weight:900; color:#2D1400; text-align:center; margin-bottom:4px;">दिव्य स्मृति कार्ड (Match)</div>
        <div style="font-size:0.8rem; color:#786C5E; text-align:center; margin-bottom:12px;">समान दिव्य प्रतीकों के जोड़े खोजें • चालें: <strong id="match-moves-count" style="color:#D97706;">0</strong></div>
        
        <div id="match-cards-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px; margin-bottom:16px;">
          <!-- 12 cards injected here -->
        </div>

        <button onclick="initMatchGame()" style="width:100%; background:linear-gradient(135deg, #8B5CF6, #6D28D9); color:#FFF; border:none; padding:10px 0; border-radius:14px; font-weight:900; cursor:pointer;">🔄 पुनः प्रारम्भ करें</button>
      </div>
    </div>

    <!-- ══════════ 🧩 2. JIGSAW PUZZLE MODAL ══════════ -->
    <div id="jigsaw-game-modal" class="modal-overlay" style="display:none; z-index:35000; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); position:fixed; inset:0; align-items:center; justify-content:center; padding:16px;">
      <div style="background:#FFFDF8; border:3px solid #F59E0B; border-radius:24px; width:100%; max-width:400px; padding:20px; position:relative; box-shadow:0 12px 35px rgba(0,0,0,0.6);">
        <button onclick="closeJigsawGame()" style="position:absolute; top:12px; right:14px; background:none; border:none; font-size:1.5rem; font-weight:900; color:#2D1400; cursor:pointer;">✕</button>
        <div style="font-size:1.25rem; font-weight:900; color:#2D1400; text-align:center; margin-bottom:4px;">श्री राम पौराणिक पहेली (JigSaw)</div>
        <div style="font-size:0.8rem; color:#786C5E; text-align:center; margin-bottom:12px;">खण्डों को क्रम में जमाएँ (1 से 8) • चालें: <strong id="jigsaw-moves-count" style="color:#0891B2;">0</strong></div>
        
        <div id="jigsaw-grid" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; width:270px; height:270px; margin:0 auto 16px; background:#FDE68A; padding:8px; border-radius:18px;">
          <!-- 3x3 tiles injected here -->
        </div>

        <button onclick="initJigsawGame()" style="width:100%; background:linear-gradient(135deg, #06B6D4, #0891B2); color:#FFF; border:none; padding:10px 0; border-radius:14px; font-weight:900; cursor:pointer;">🔄 पुनः क्रमबद्ध करें</button>
      </div>
    </div>

    <!-- ══════════ 📖 3. PADABANDHAM WORD GRID MODAL ══════════ -->
    <div id="padabandham-game-modal" class="modal-overlay" style="display:none; z-index:35000; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); position:fixed; inset:0; align-items:center; justify-content:center; padding:16px;">
      <div style="background:#FFFDF8; border:3px solid #F59E0B; border-radius:24px; width:100%; max-width:420px; padding:20px; position:relative; box-shadow:0 12px 35px rgba(0,0,0,0.6);">
        <button onclick="closePadabandhamGame()" style="position:absolute; top:12px; right:14px; background:none; border:none; font-size:1.5rem; font-weight:900; color:#2D1400; cursor:pointer;">✕</button>
        <div style="font-size:1.25rem; font-weight:900; color:#2D1400; text-align:center; margin-bottom:4px;">पदबन्धम् (PadaBandham)</div>
        <div style="font-size:0.8rem; color:#786C5E; text-align:center; margin-bottom:12px;">रामायण व महाभारत के पवित्र नाम खोजें</div>
        
        <div id="padabandham-word-list" style="display:flex; flex-wrap:wrap; gap:8px; justify-content:center; margin-bottom:16px;">
          <!-- Words list injected here -->
        </div>

        <div style="background:#FEF3C7; border:1.5px solid #F59E0B; border-radius:18px; padding:14px; text-align:center; font-size:0.95rem; font-weight:800; color:#2D1400; line-height:1.5; margin-bottom:16px;">
          🚩 <strong>रामायण - महाभारत शब्द संज्ञान</strong><br>
          <span style="font-size:0.82rem; color:#5A4A3B;">शब्दों को पहचानें और दिव्य ज्ञान संकलित करें।</span>
        </div>

        <button onclick="alert('🎉 शब्द ग्रिड संज्ञान पूर्ण! +100 🪙');" style="width:100%; background:linear-gradient(135deg, #D97706, #B45309); color:#FFF; border:none; padding:10px 0; border-radius:14px; font-weight:900; cursor:pointer;">✅ संज्ञान पूर्ण करें</button>
      </div>
    </div>
"""

if 'id="page-epic-games"' not in html:
    html = html[:page_home_end_after] + epic_games_hub_and_modals + html[page_home_end_after:]
    print("Added page-epic-games and all game arena modals")

# 4. Add epic_games_engine.js before </body>
script_tag = '  <script src="epic_games_engine.js"></script>\n'
if 'src="epic_games_engine.js"' not in html:
    body_end = html.rfind('</body>')
    html = html[:body_end] + script_tag + html[body_end:]
    print("Added epic_games_engine.js before </body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html successfully updated with Epic Games Hub, Swipe Game, and 3 Related Games!")
