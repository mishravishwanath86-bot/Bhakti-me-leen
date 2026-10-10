import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update styles.css
with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

old_desktop_margin = """.today-panchang-card, .tpc-card,
  .muhurat-home-card, .sadhana-home-compact-card {
    margin: 0 24px !important;
  }"""

new_desktop_margin = """.today-panchang-card, .tpc-card,
  .muhurat-home-card, .sadhana-home-compact-card,
  #sadhana-home-compact-card, .home-promo-banner-card {
    margin: 0 24px 1.8rem !important;
  }"""

if old_desktop_margin in css:
    css = css.replace(old_desktop_margin, new_desktop_margin)
    print("✓ Updated styles.css desktop media query margin rule!")
else:
    print("WARNING: Exact match for old_desktop_margin not found, checking regex...")
    import re
    css = re.sub(
        r'\.today-panchang-card,\s*\.tpc-card,\s*\.muhurat-home-card,\s*\.sadhana-home-compact-card\s*\{\s*margin:\s*0\s+24px\s*!important;\s*\}',
        new_desktop_margin,
        css
    )
    print("✓ Regex updated styles.css desktop media query margin rule!")

# Add specific spacing rule to end of styles.css to ensure universal padding and gap
promo_rule = """
/* ══ HOME INTERMEDIATE PROMO & UTILITY CARDS (BALANCED GAP & BREATHING ROOM) ══ */
.home-promo-banner-card,
#sadhana-home-compact-card,
.today-panchang-card {
  margin-bottom: 1.8rem !important;
  box-sizing: border-box !important;
}

.home-promo-banner-card:hover,
#sadhana-home-compact-card:hover,
.today-panchang-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.5), 0 0 15px rgba(248,200,59,0.15) !important;
}
"""
if '/* ══ HOME INTERMEDIATE PROMO & UTILITY CARDS' not in css:
    css += promo_rule
    print("✓ Appended promo & utility cards spacing rules to styles.css!")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Find the block from BHAKTI AMRIT KALASH to HINDU VRATS
block_pat = r'(<!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->.*?)(<!-- 🕉️ HINDU VRATS & UPAVAS -->)'
block_m = re.search(block_pat, html, re.DOTALL)
if not block_m:
    print("ERROR: Could not locate promo block in index.html")
    sys.exit(1)

new_block = '''<!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->
      <div class="home-promo-banner-card" style="margin: 1.6rem 1.2rem 1.8rem;" onclick="showPage('page-jar')">
        <div style="background: linear-gradient(135deg, #2D104E 0%, #4A154B 100%); border: 1.5px solid #FCD34D; border-radius: 20px; padding: 1.1rem 1.3rem; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 24px rgba(0,0,0,0.35); cursor: pointer; transition: transform 0.2s ease;">
          <div style="display:flex; align-items:center; gap: 1rem;">
            <div style="font-size: 2.2rem; filter: drop-shadow(0 0 10px #F59E0B);">🏺</div>
            <div>
              <div style="color:#FDE68A; font-weight:900; font-size:1.05rem; margin-bottom:2px;">भक्ति अमृत कलश</div>
              <div style="color:#FBCFE8; font-size:0.82rem;">अपनी मनोदशा चुनें और दिव्य श्लोक पाएं ❯</div>
            </div>
          </div>
          <span style="background: linear-gradient(135deg, #FDE68A, #F59E0B); color: #4A1030; font-weight: 900; font-size: 0.8rem; padding: 6px 14px; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.3);">खोलें</span>
        </div>
      </div>

      <!-- 📅 DAILY LIVE VEDIC PANCHANG CARD 📅 -->
      <div class="today-panchang-card home-promo-banner-card" onclick="showPage('page-panchang')" style="margin: 0 1.2rem 1.8rem;">
        <div class="tpc-header">
          <span class="tpc-badge">दैनिक पंचांग</span>
          <span class="tpc-date" id="home-today-date">आज</span>
        </div>
        <div class="tpc-body">
          <div class="tpc-row">
            <span class="tpc-lbl">तिथि:</span>
            <span class="tpc-val" id="home-tithi">लोड हो रहा है...</span>
          </div>
          <div class="tpc-row">
            <span class="tpc-lbl">नक्षत्र:</span>
            <span class="tpc-val" id="home-nakshatra">लोड हो रहा है...</span>
          </div>
          <div class="tpc-sun-row">
            <span>🌅 <span id="home-sunrise">06:00 AM</span></span>
            <span>🌇 <span id="home-sunset">06:30 PM</span></span>
          </div>
        </div>
      </div>

      <!-- 🪔 STAGE 1: COMPACT LIVE SADHANA TRIGGER WIDGET 🪔 -->
      <div id="sadhana-home-compact-card" class="sadhana-home-compact-card home-promo-banner-card" onclick="openFullSadhanaControlModal()" style="margin: 0 1.2rem 1.8rem; background: radial-gradient(circle at 80% 20%, rgba(61, 16, 96, 0.9) 0%, rgba(26, 11, 46, 0.88) 60%, rgba(13, 2, 26, 0.95) 100%); border: 1.5px solid #F59E0B; border-radius: 24px; padding: 1.2rem 1.3rem; box-shadow: 0 10px 35px rgba(0,0,0,0.7), 0 0 20px rgba(245,158,11,0.15) inset; cursor: pointer; position: relative; overflow: hidden; transition: transform 0.2s ease, box-shadow 0.2s ease;">
        
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

      <!-- 🎁 DIVINE REWARD GIFT CHEST CARD -->
      <div class="home-promo-banner-card" style="margin: 0 1.2rem 2.2rem;" onclick="claimDivineGift()">
        <div style="background: linear-gradient(135deg, #BE185D 0%, #831843 100%); border: 1.5px solid #FDE68A; border-radius: 20px; padding: 1rem 1.3rem; display: flex; align-items: center; justify-content: space-between; cursor: pointer; box-shadow: 0 6px 20px rgba(190, 24, 93, 0.35); transition: transform 0.2s ease;">
          <div style="display: flex; align-items: center; gap: 0.9rem;">
            <div style="font-size: 2.2rem; filter: drop-shadow(0 0 10px #F59E0B);">🎁</div>
            <div>
              <div style="color: #FDE68A; font-weight: 900; font-size: 1.02rem;">दैवीय उपहार पुरस्कार</div>
              <div style="color: #FBCFE8; font-size: 0.8rem;" id="gift-progress-subtitle">3/3 साधना पूर्ण! उपहार खोलें ❯</div>
            </div>
          </div>
          <button style="background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color: #1E1B18; font-weight: 900; font-size: 0.8rem; border: none; padding: 7px 16px; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.3); cursor:pointer;">खोलें</button>
        </div>
      </div>

      '''

html = html[:block_m.start(1)] + new_block + html[block_m.start(2):]

# Also ensure Hindu Vrats section header has good top breathing room
html = re.sub(
    r'(<!-- 🕉️ HINDU VRATS & UPAVAS -->\s*<div class="home-grid-header)"',
    r'\1" style="margin-top: 2rem !important;"',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Updated index.html with luxurious spacing and margins!")
