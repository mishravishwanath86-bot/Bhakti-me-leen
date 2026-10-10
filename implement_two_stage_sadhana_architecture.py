import re, time, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🪔 IMPLEMENTING TWO-STAGE SADHANA ARCHITECTURE")
print("======================================================================")

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the long sadhana-hub-container on home screen with the compact trigger card
sadhana_section_pattern = r'<!-- 🧘 NITYA SADHANA & WEEKLY STREAK TRACKER 🧘 -->[\s\S]*?<!-- 🎁 DIVINE REWARD GIFT CHEST CARD -->'

compact_home_card = """<!-- 🪔 STAGE 1: COMPACT LIVE SADHANA TRIGGER WIDGET 🪔 -->
      <div id="sadhana-home-compact-card" onclick="openFullSadhanaControlModal()" style="margin: 0 1.2rem 1.4rem; background: radial-gradient(circle at 80% 20%, rgba(61, 16, 96, 0.9) 0%, rgba(26, 11, 46, 0.88) 60%, rgba(13, 2, 26, 0.95) 100%); border: 1.5px solid #F59E0B; border-radius: 24px; padding: 1.2rem 1.3rem; box-shadow: 0 10px 35px rgba(0,0,0,0.7), 0 0 20px rgba(245,158,11,0.15) inset; cursor: pointer; position: relative; overflow: hidden; transition: transform 0.2s ease, box-shadow 0.2s ease;">
        
        <!-- Subtle Glow Accent Orb -->
        <div style="position:absolute; top:-25px; right:-25px; width:110px; height:110px; border-radius:50%; background:radial-gradient(circle, rgba(245,158,11,0.3) 0%, transparent 70%); pointer-events:none;"></div>

        <!-- Header: Title & Streak Badge -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div style="font-size:1.05rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.35rem; filter:drop-shadow(0 0 8px #F59E0B);">🪔</span>
            <span>दैनिक साधना संज्ञान</span>
          </div>
          <div id="sadhana-home-streak-badge" style="font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, rgba(245,158,11,0.25) 0%, rgba(217,119,6,0.15) 100%); border:1.2px solid #F59E0B; color:#FDE68A; padding:3px 10px; border-radius:12px; box-shadow:0 0 10px rgba(245,158,11,0.3);">
            🔥 21 दिन स्ट्रीक
          </div>
        </div>

        <!-- Metric Row 1: Daily Visit Counter -->
        <div style="display:flex; align-items:center; gap:6px; font-size:0.8rem; color:#CBD5E1; margin-bottom:6px;">
          <span style="font-size:0.95rem;">👁️</span>
          <span>आज का पावन प्रवेश:</span>
          <strong id="sadhana-home-visit-count" style="color:#FFFDF8; font-weight:900;">3 बार</strong>
          <span style="font-size:0.7rem; color:#94A3B8;">(Visit Counter)</span>
        </div>

        <!-- Metric Row 2: Shield Vault & Punya Summary -->
        <div style="display:flex; align-items:center; gap:6px; font-size:0.8rem; color:#CBD5E1; margin-bottom:12px;">
          <span style="font-size:0.95rem;">🛡️</span>
          <span>संकल्प रक्षा कवच:</span>
          <strong id="sadhana-home-shield-summary" style="color:#FDE68A; font-weight:900;">1 सक्रिय</strong>
          <span style="color:#64748B;">•</span>
          <span>संचित पुण्य:</span>
          <strong id="sadhana-home-punya-summary" style="color:#F8C83B; font-weight:900;">1,450</strong>
        </div>

        <!-- Interactive Action CTA Button -->
        <button onclick="openFullSadhanaControlModal(); event.stopPropagation();" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.85rem; font-weight:900; padding:10px 0; border-radius:14px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.35); display:flex; align-items:center; justify-content:center; gap:6px; transition:transform 0.15s ease;">
          <span>साधना नियंत्रण कक्ष खोलें (विस्तार से देखें)</span> ➔
        </button>

      </div>

      <!-- 🎁 DIVINE REWARD GIFT CHEST CARD -->"""

if re.search(sadhana_section_pattern, html):
    html = re.sub(sadhana_section_pattern, compact_home_card, html, count=1)
    print("✓ Successfully replaced long sadhana section on Home screen with Compact Trigger Widget!")
else:
    print("⚠️ Pattern match failed, looking for specific container...")

# Insert Stage 2 Full-Screen Sadhana Control Modal right before other modals
stage_2_fullscreen_modal = """
  <!-- ═══════════════════════════════════════════════════════════════════════════
       🪔 STAGE 2: FULL-SCREEN "दैनिक साधना नियंत्रण कक्ष" (MODAL / PAGE) 🪔
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="full-sadhana-control-modal" style="display:none; position:fixed; inset:0; z-index:100150; background:rgba(7,1,16,0.96); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); flex-direction:column; overflow-y:auto; padding:0; animation:fadeInUp 0.3s ease;">
    
    <!-- Top Sticky Header Bar -->
    <div style="position:sticky; top:0; z-index:40; padding:14px 16px; background:linear-gradient(180deg, #1D0733 0%, rgba(13,2,26,0.95) 100%); border-bottom:1.5px solid rgba(248,200,59,0.35); display:flex; align-items:center; justify-content:space-between; backdrop-filter:blur(15px); -webkit-backdrop-filter:blur(15px);">
      <button onclick="closeFullSadhanaControlModal()" style="background:rgba(255,255,255,0.12); border:1.2px solid rgba(248,200,59,0.4); color:#FDE68A; padding:5px 12px; border-radius:12px; font-size:0.78rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:4px;">
        ✕ वापस जाएं
      </button>

      <div style="font-size:0.95rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
        <span style="font-size:1.2rem;">🪔</span>
        <span>संपूर्ण दैनिक साधना व संकल्प</span>
      </div>

      <div id="modal-sadhana-streak-badge" style="font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; padding:4px 10px; border-radius:12px; box-shadow:0 0 10px rgba(248,200,59,0.4);">
        🔥 21 दिन स्ट्रीक
      </div>
    </div>

    <!-- Scrollable Modal Content Container -->
    <div style="padding:16px; max-width:480px; margin:0 auto; width:100%; box-sizing:border-box;">

      <!-- Today's Visit Summary Banner -->
      <div style="background:linear-gradient(135deg, rgba(245,158,11,0.15) 0%, rgba(147,51,234,0.15) 100%); border:1.2px solid rgba(248,200,59,0.35); border-radius:18px; padding:12px 14px; margin-bottom:16px; display:flex; align-items:center; gap:10px;">
        <div style="font-size:2rem; filter:drop-shadow(0 0 8px #F59E0B);">👁️</div>
        <div>
          <div style="font-size:0.85rem; font-weight:900; color:#FFFDF8;" id="modal-visit-summary-text">
            आज आपने <strong style="color:#FDE68A;">3 बार</strong> प्रभु दर्शन व साधना हेतु प्रवेश किया है
          </div>
          <div style="font-size:0.72rem; color:#CBD5E1; margin-top:2px;">
            ✨ मन शांत, एकाग्र एवं प्रभु चरणों में समर्पित है
          </div>
        </div>
      </div>

      <!-- Weekly Day Strip inside Modal -->
      <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(248,200,59,0.25); border-radius:18px; padding:10px 12px; margin-bottom:16px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
          <span style="font-size:0.75rem; font-weight:800; color:#CBD5E1;">साप्ताहिक साधना नियम:</span>
          <span style="font-size:0.72rem; font-weight:800; color:#FDE68A;">आज 5/7 पूर्ण ✓</span>
        </div>
        <div class="weekly-day-strip">
          <div class="day-dot done" onclick="toggleDayDone(0)"><span>सोम</span><span class="dot-check">✓</span></div>
          <div class="day-dot done" onclick="toggleDayDone(1)"><span>मंगल</span><span class="dot-check">✓</span></div>
          <div class="day-dot done" onclick="toggleDayDone(2)"><span>बुध</span><span class="dot-check">✓</span></div>
          <div class="day-dot done" onclick="toggleDayDone(3)"><span>गुरु</span><span class="dot-check">✓</span></div>
          <div class="day-dot active-today" onclick="toggleDayDone(4)"><span>शुक्र</span><span class="dot-check">●</span></div>
          <div class="day-dot" onclick="toggleDayDone(5)"><span>शनि</span><span class="dot-check">○</span></div>
          <div class="day-dot" onclick="toggleDayDone(6)"><span>रवि</span><span class="dot-check">○</span></div>
        </div>
      </div>

      <!-- MODULE A: "साधना स्ट्रीक व पुण्य रक्षा" (Streak Shields & Vedic Rewards) -->
      <div id="modal-sadhana-streak-shield-vault" style="background:linear-gradient(145deg, #2D1047 0%, #17042B 60%, #0D021A 100%); border:1.5px solid #F59E0B; border-radius:22px; padding:14px; box-shadow:0 8px 25px rgba(0,0,0,0.6), inset 0 0 15px rgba(248,200,59,0.12); margin-bottom:16px; position:relative; overflow:hidden;">
        
        <div style="position:absolute; top:-20px; right:-20px; width:90px; height:90px; border-radius:50%; background:radial-gradient(circle, rgba(245,158,11,0.25) 0%, transparent 70%); pointer-events:none;"></div>

        <!-- Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
          <div style="display:flex; align-items:center; gap:6px; font-size:0.95rem; font-weight:900; color:#FFFDF8;">
            <span style="font-size:1.2rem; filter:drop-shadow(0 0 6px #F59E0B);">🛡️</span>
            <span>साधना स्ट्रीक व पुण्य रक्षा</span>
          </div>
          <button onclick="openVedicRanksModal()" style="background:rgba(248,200,59,0.18); border:1px solid #F8C83B; color:#FDE68A; font-size:0.7rem; font-weight:800; padding:3px 8px; border-radius:10px; cursor:pointer; display:flex; align-items:center; gap:3px;">
            <span>🏆</span> पदवियां ❯
          </button>
        </div>

        <!-- Vault Metrics Row -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px; background:rgba(0,0,0,0.3); border-radius:14px; padding:8px 12px;">
          <div>
            <div style="font-size:0.68rem; color:#CBD5E1;">🌟 संचित पुण्य अंक</div>
            <div id="sadhana-punya-points-text" style="font-size:1.1rem; font-weight:900; color:#F8C83B; letter-spacing:0.5px;">1,450 अंक</div>
          </div>
          <div id="sadhana-active-shield-badge" style="font-size:0.75rem; font-weight:900; background:rgba(245,158,11,0.2); border:1px solid #F59E0B; color:#FDE68A; padding:4px 10px; border-radius:12px; box-shadow:0 0 10px rgba(245,158,11,0.3);">
            🛡️ 1 सक्रिय कवच
          </div>
        </div>

        <!-- Vedic Rank Badge & Protection Note -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px; font-size:0.75rem;">
          <div style="color:#CBD5E1;">
            वर्तमान पदवी: <strong id="sadhana-vedic-rank-text" style="color:#FFFDF8; font-weight:900;">🔱 'तपस्वी' (Level 2)</strong>
          </div>
          <div style="color:#FDE68A; font-size:0.68rem; cursor:pointer;" onclick="openVedicRanksModal()">
            अगली: 'सिद्ध साधक' ❯
          </div>
        </div>

        <div style="font-size:0.7rem; color:#94A3B8; margin-bottom:10px; line-height:1.3; font-style:italic;">
          "यदि किसी दिन नियम छूटे, तो यह कवच स्वतः 1 दिन की स्ट्रीक बचाएगा।"
        </div>

        <!-- Add Shield Button -->
        <button onclick="buyStreakShield()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.82rem; font-weight:900; padding:10px 0; border-radius:14px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.35); display:flex; align-items:center; justify-content:center; gap:6px;">
          <span>🛡️</span> +500 पुण्य अंक से नया कवच जोड़ें
        </button>
      </div>


      <!-- MODULE B: "सामूहिक साधना मंडल" (Family & Sangha Collective Circle) -->
      <div id="modal-sadhana-collective-sangha-card" style="background:linear-gradient(145deg, #1F0738 0%, #3D0E54 60%, #150328 100%); border:1.5px solid #F8C83B; border-radius:22px; padding:14px; box-shadow:0 8px 25px rgba(0,0,0,0.6), inset 0 0 15px rgba(248,200,59,0.12); margin-bottom:16px;">
        
        <!-- Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
          <div style="display:flex; align-items:center; gap:6px; font-size:0.95rem; font-weight:900; color:#FFFDF8;">
            <span style="font-size:1.2rem;">👥</span>
            <span>सामूहिक साधना मंडल</span>
          </div>
          <button onclick="openCreateJoinSanghaModal()" style="background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:0.68rem; font-weight:800; padding:3px 8px; border-radius:10px; cursor:pointer;">
            मंडल बदलें ❯
          </button>
        </div>

        <!-- Active Circle Title -->
        <div id="sangha-circle-title" style="font-size:0.85rem; font-weight:900; color:#FDE68A; margin-bottom:8px; line-height:1.3;">
          🕉️ महामृत्युंजय 1 लाख महा-अनुष्ठान (मिश्रा परिवार)
        </div>

        <!-- Target Progress Bar -->
        <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:8px 10px; margin-bottom:10px;">
          <div style="display:flex; align-items:center; justify-content:space-between; font-size:0.75rem; margin-bottom:6px;">
            <span style="color:#CBD5E1;">📊 कुल सामूहिक प्रगति:</span>
            <span style="font-weight:900; color:#FFFDF8;">
              <span id="sangha-progress-text" style="color:#F8C83B;">68,400 / 100,000 जप</span>
              <span id="sangha-progress-pct" style="color:#FDE68A;">(68.4%)</span>
            </span>
          </div>
          <div style="width:100%; height:8px; background:rgba(255,255,255,0.1); border-radius:10px; overflow:hidden; border:1px solid rgba(248,200,59,0.3);">
            <div id="sangha-progress-bar-fill" style="width:68.4%; height:100%; background:linear-gradient(90deg, #10B981, #F8C83B, #FF512F); border-radius:10px; transition:width 0.4s ease; box-shadow:0 0 10px rgba(248,200,59,0.7);"></div>
          </div>
        </div>

        <!-- Top Contributors (Leaderboard) -->
        <div style="margin-bottom:10px;">
          <div style="font-size:0.75rem; font-weight:900; color:#CBD5E1; margin-bottom:6px; display:flex; align-items:center; gap:4px;">
            <span>👑</span> शीर्ष साधक (Live Contributors):
          </div>
          <div id="sangha-contributors-list" style="display:flex; flex-direction:column; gap:5px;">
            <!-- Filled dynamically by JS -->
          </div>
        </div>

        <!-- Action Buttons: Dedicate Jap & Add Member -->
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:10px;">
          <button onclick="openDedicateJapModal()" style="background:linear-gradient(135deg, #FF8C00 0%, #FF512F 100%); color:#FFF; border:none; font-size:0.78rem; font-weight:900; padding:9px 0; border-radius:12px; cursor:pointer; box-shadow:0 4px 12px rgba(255,81,47,0.4); display:flex; align-items:center; justify-content:center; gap:4px;">
            <span>📿</span> आज के जप समर्पित करें
          </button>
          <button onclick="openAddMemberModal()" style="background:rgba(255,255,255,0.1); border:1.2px solid #F8C83B; color:#FDE68A; font-size:0.78rem; font-weight:900; padding:9px 0; border-radius:12px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:4px;">
            <span>➕</span> सदस्य जोड़ें
          </button>
        </div>

        <!-- Live Feed & Nudge Strip -->
        <div style="background:rgba(0,0,0,0.25); border-radius:10px; padding:6px 10px; margin-bottom:10px;">
          <div id="sangha-feed-list" style="display:flex; flex-direction:column; gap:3px;">
            <!-- Filled dynamically by JS -->
          </div>
          <div style="display:flex; align-items:center; justify-content:flex-end; margin-top:4px;">
            <button onclick="nudgeSanghaMember('राहुल')" style="background:transparent; border:none; color:#F8C83B; font-size:0.68rem; font-weight:800; cursor:pointer; text-decoration:underline;">
              🔔 राहुल को स्मरण भेजें (Nudge)
            </button>
          </div>
        </div>

      </div>

      <!-- Bottom WhatsApp Share CTA -->
      <button onclick="shareSanghaProgressWhatsApp()" style="width:100%; background:linear-gradient(135deg, #25D366 0%, #128C7E 100%); color:#FFF; border:none; font-size:0.88rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 18px rgba(37,211,102,0.4); display:flex; align-items:center; justify-content:center; gap:8px; margin-bottom:30px;">
        <span>📲</span> WhatsApp पर संपूर्ण साधना प्रगति साझा करें
      </button>

    </div>
  </div>
"""

# Insert Stage 2 modal if not present
if 'id="full-sadhana-control-modal"' not in html:
    html = html.replace('<!-- ═══════════════════════════════════════════════════════════════════════════\n       🏆 VEDIC RANKS & BADGES MODAL', stage_2_fullscreen_modal + '\n\n  <!-- ═══════════════════════════════════════════════════════════════════════════\n       🏆 VEDIC RANKS & BADGES MODAL')
    print("✓ Inserted Stage 2 Full-Screen Sadhana Control Modal into index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html updated successfully!")


# 2. Update sadhana_gamification_engine.js with Visit Counter Logic and Modal Controls
with open('sadhana_gamification_engine.js', 'r', encoding='utf-8') as f:
    engine_js = f.read()

visit_tracking_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 👁️ DAILY APP VISIT TRACKING & TWO-STAGE ARCHITECTURE CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════

window.currentDailyVisits = 3;

window.trackDailyAppVisits = function() {
  const today = new Date().toISOString().split('T')[0];
  const lastDate = localStorage.getItem('sanatan_last_visit_date');
  const lastTs = parseInt(localStorage.getItem('sanatan_last_visit_timestamp') || '0');
  let visitCount = parseInt(localStorage.getItem('sanatan_daily_visit_count') || '3');

  const now = Date.now();

  if (lastDate !== today) {
    visitCount = 1;
    localStorage.setItem('sanatan_last_visit_date', today);
    localStorage.setItem('sanatan_daily_visit_count', '1');
    localStorage.setItem('sanatan_last_visit_timestamp', now.toString());
  } else {
    // Increment visit count if session gap > 15 minutes
    if (now - lastTs > 15 * 60 * 1000) {
      visitCount += 1;
      localStorage.setItem('sanatan_daily_visit_count', visitCount.toString());
      localStorage.setItem('sanatan_last_visit_timestamp', now.toString());
    }
  }

  if (visitCount < 1) visitCount = 1;
  window.currentDailyVisits = visitCount;
  window.updateVisitCountUI(visitCount);
};

window.updateVisitCountUI = function(count) {
  count = count || window.currentDailyVisits || 3;
  
  // Update Home Compact Card
  const homeVisitEl = document.getElementById('sadhana-home-visit-count');
  if (homeVisitEl) homeVisitEl.textContent = `${count} बार`;

  // Update Modal Banner
  const modalVisitText = document.getElementById('modal-visit-summary-text');
  if (modalVisitText) {
    modalVisitText.innerHTML = `आज आपने <strong style="color:#FDE68A;">${count} बार</strong> प्रभु दर्शन व साधना हेतु प्रवेश किया है`;
  }
};

window.renderHomeCompactTriggerUI = function() {
  const streakBadge = document.getElementById('sadhana-home-streak-badge');
  const shieldSummary = document.getElementById('sadhana-home-shield-summary');
  const punyaSummary = document.getElementById('sadhana-home-punya-summary');
  const modalStreakBadge = document.getElementById('modal-sadhana-streak-badge');

  const streak = window.SadhanaProfile.current_streak;
  const shields = window.SadhanaProfile.active_shields;
  const points = window.SadhanaProfile.punya_points;

  if (streakBadge) streakBadge.textContent = `🔥 ${streak} दिन स्ट्रीक`;
  if (modalStreakBadge) modalStreakBadge.textContent = `🔥 ${streak} दिन स्ट्रीक`;
  if (shieldSummary) shieldSummary.textContent = `${shields} सक्रिय`;
  if (punyaSummary) punyaSummary.textContent = `${points.toLocaleString('en-IN')}`;
};

window.openFullSadhanaControlModal = function() {
  const modal = document.getElementById('full-sadhana-control-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
  window.renderSadhanaShieldVaultUI();
  window.renderSanghaCircleUI();
  window.updateVisitCountUI();

  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
};

window.closeFullSadhanaControlModal = function() {
  const modal = document.getElementById('full-sadhana-control-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
  window.renderHomeCompactTriggerUI();
};
"""

# Append to sadhana_gamification_engine.js
if 'trackDailyAppVisits' not in engine_js:
    engine_js += '\n' + visit_tracking_code
    print("✓ Added visit tracking and modal controllers to sadhana_gamification_engine.js")

# In initSadhanaGamificationEngine, ensure trackDailyAppVisits and renderHomeCompactTriggerUI are called
init_hook = """  // Track Daily Visits
  window.trackDailyAppVisits();
  window.renderHomeCompactTriggerUI();"""

if 'window.trackDailyAppVisits();' not in engine_js:
    engine_js = engine_js.replace("window.renderSanghaCircleUI();", "window.renderSanghaCircleUI();\n" + init_hook)
    print("✓ Hooked trackDailyAppVisits into engine init")

# In renderSadhanaShieldVaultUI and renderSanghaCircleUI, also call renderHomeCompactTriggerUI
if 'window.renderHomeCompactTriggerUI();' not in engine_js.split('renderSadhanaShieldVaultUI')[1].split('}')[0]:
    engine_js = engine_js.replace("pointsEl.textContent = `${window.SadhanaProfile.punya_points.toLocaleString('en-IN')} अंक`;", "pointsEl.textContent = `${window.SadhanaProfile.punya_points.toLocaleString('en-IN')} अंक`;\n  window.renderHomeCompactTriggerUI();")

with open('sadhana_gamification_engine.js', 'w', encoding='utf-8') as f:
    f.write(engine_js)

print("✓ sadhana_gamification_engine.js updated successfully!")
