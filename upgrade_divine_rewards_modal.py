import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("UPGRADING DAIVIYA UPHAAR PURASKAR (DIVINE REWARDS) MODAL")
print("=" * 80)

# 1. Add #divine-gift-modal to index.html before </body>
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

divine_gift_modal_html = """  <!-- ═════════════════════════════════════════════════════════════════
       🎁 DAIVIYA UPHAAR PURASKAR (DIVINE REWARDS) LUXURY MODAL 🎁
       ═════════════════════════════════════════════════════════════════ -->
  <div id="divine-gift-modal" style="display:none; position:fixed; inset:0; z-index:100040; background:rgba(10,2,18,0.95); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div class="divine-chest-modal-card" style="width:100%; max-width:420px; background:linear-gradient(160deg, #380E57 0%, #1A0429 60%, #0D0117 100%); border:2px solid rgba(248,200,59,0.5); border-radius:32px; padding:1.8rem 1.4rem; box-shadow:0 25px 70px rgba(0,0,0,0.9); position:relative; text-align:center; margin:auto 0;">
      
      <!-- Close Button -->
      <button onclick="closeDivineGiftModal()" style="position:absolute; top:14px; right:14px; background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:background 0.2s;">✕</button>

      <!-- Header -->
      <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; background:rgba(248,200,59,0.2); border:1px solid rgba(248,200,59,0.4); padding:3px 12px; border-radius:12px; display:inline-flex; align-items:center; gap:6px; margin-bottom:8px;">
        <span>✨</span> नित्य साधना फल
      </div>
      <h2 style="font-size:1.3rem; font-weight:900; color:#FFFDF8; margin:0 0 4px 0; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>🎁</span> दैवीय उपहार पुरस्कार
      </h2>
      <p style="font-size:0.8rem; color:#FBCFE8; margin:0 0 16px 0;">
        आपकी नित्य भक्ति व साधना से प्रसन्न होकर देव कृपा प्रकट हुई है!
      </p>

      <!-- Stage 1: Mystery Chest View (Before Opening) -->
      <div id="gift-chest-stage" style="display:flex; flex-direction:column; align-items:center; padding:1.5rem 0;">
        <div id="mystery-chest-box" style="position:relative; width:120px; height:120px; border-radius:28px; background:radial-gradient(circle, #F59E0B 0%, #B45309 70%, #78350F 100%); border:3px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:3.8rem; box-shadow:0 0 40px rgba(245,158,11,0.55), inset 0 0 20px rgba(0,0,0,0.4); cursor:pointer; transition:transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);" onclick="openMysteryChestAnimation()">
          <span id="chest-icon" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.5));">🎁</span>
          <div style="position:absolute; inset:-8px; border-radius:36px; border:2px dashed rgba(248,200,59,0.4); animation:spinSlow 12s linear infinite;"></div>
        </div>

        <p style="font-size:0.82rem; font-weight:700; color:#FDE68A; margin:16px 0 18px 0;">
          👇 कलश / उपहार पेटिका पर स्पर्श करें
        </p>

        <button onclick="openMysteryChestAnimation()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 30px; border-radius:20px; cursor:pointer; box-shadow:0 6px 20px rgba(248,200,59,0.45); display:inline-flex; align-items:center; gap:8px;">
          <span>✨</span> उपहार खोलें ❯
        </button>
      </div>

      <!-- Stage 2: Revealed Rewards View (After Opening) -->
      <div id="gift-reward-stage" style="display:none; flex-direction:column; gap:12px; text-align:left; animation:fadeInUp 0.4s ease forwards;">
        
        <!-- Punya Coins Badge -->
        <div style="background:linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(217,119,6,0.1) 100%); border:1.5px solid #F59E0B; border-radius:18px; padding:10px 14px; display:flex; align-items:center; justify-content:space-between;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.6rem;">🪙</span>
            <div>
              <div style="font-size:0.88rem; font-weight:900; color:#FDE68A;">+25 पुण्य सिक्के प्राप्त हुए!</div>
              <div style="font-size:0.72rem; color:#CBD5E1;">डिजिटल भक्ति वॉलेट में जमा किए गए</div>
            </div>
          </div>
          <span id="wallet-balance-badge" style="font-size:0.82rem; font-weight:900; background:#F59E0B; color:#1A0B2E; padding:4px 10px; border-radius:12px;">
            कुल: 125 🪙
          </span>
        </div>

        <!-- 4K Wallpaper Download Card -->
        <div style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:12px; display:flex; align-items:center; gap:12px;">
          <img id="reward-wallpaper-img" src="assets/gallery/bal_ganesha.jpg" alt="4K Wallpaper" style="width:65px; height:65px; border-radius:14px; object-fit:cover; border:1.5px solid #FDE68A; flex-shrink:0;" />
          <div style="flex:1;">
            <div id="reward-wallpaper-title" style="font-size:0.88rem; font-weight:900; color:#FFFDF8; margin-bottom:2px;">
              🖼️ 4K दिव्य देव वॉलपेपर
            </div>
            <div style="font-size:0.72rem; color:#FDE68A; margin-bottom:6px;">मोबाइल लॉकस्क्रीन हेतु सिद्ध स्वरूप</div>
            <a id="reward-wallpaper-btn" href="assets/gallery/bal_ganesha.jpg" download="Bhakti_Divine_4K_Wallpaper.jpg" style="background:linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%); color:#FFF; text-decoration:none; font-size:0.75rem; font-weight:800; padding:4px 12px; border-radius:10px; display:inline-flex; align-items:center; gap:4px;">
              <span>📥</span> डाउनलोड 4K
            </a>
          </div>
        </div>

        <!-- Divine Ringtone / Shankh Audio Download -->
        <div style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:12px; display:flex; align-items:center; justify-content:space-between;">
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="width:42px; height:42px; border-radius:12px; background:rgba(248,200,59,0.2); border:1px solid rgba(248,200,59,0.4); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              🎵
            </div>
            <div>
              <div id="reward-audio-title" style="font-size:0.85rem; font-weight:900; color:#FFFDF8;">पावन शंख व आरती रिंगटोन</div>
              <div style="font-size:0.72rem; color:#CBD5E1;">30s सिद्ध ध्यान ध्वनि (MP3)</div>
            </div>
          </div>
          <a id="reward-audio-btn" href="assets/audio/shree_ganesh_aarti.mp3" download="Bhakti_Divine_Ringtone.mp3" style="background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; text-decoration:none; font-size:0.75rem; font-weight:800; padding:6px 12px; border-radius:12px; display:inline-flex; align-items:center; gap:4px;">
            <span>📥</span> MP3
          </a>
        </div>

        <!-- Personalized Sanskrit Blessing Card with WhatsApp Share -->
        <div style="background:linear-gradient(145deg, #240C44 0%, #150529 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:20px; padding:14px; text-align:center;">
          <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-bottom:4px;">
            📜 व्यक्तिगत दिव्य आशीर्वाद पत्र
          </div>
          <div id="reward-blessing-name" style="font-size:1rem; font-weight:900; color:#FFFDF8; margin-bottom:6px;">
            प्रिय भक्त जन हेतु
          </div>
          <div id="reward-blessing-shlok" style="font-family:'Tiro Devanagari Hindi', serif; font-size:0.92rem; font-weight:700; color:#FDE68A; line-height:1.5; margin-bottom:6px;">
            ॥ सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते ॥
          </div>
          <p id="reward-blessing-meaning" style="font-size:0.75rem; color:#CBD5E1; margin:0 0 10px 0; line-height:1.4;">
            माँ भगवती आपके समस्त मनोरथ सिद्ध करें और घर में अखंड सुख-शांति व समृद्धि का वास हो।
          </p>

          <button onclick="shareBlessingCardWhatsApp()" style="width:100%; background:linear-gradient(135deg, #10B981 0%, #059669 100%); color:#FFF; border:none; font-size:0.82rem; font-weight:900; padding:8px 0; border-radius:14px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px; box-shadow:0 4px 15px rgba(16,185,129,0.35);">
            <span>📲</span> WhatsApp पर आशीर्वाद शेयर करें
          </button>
        </div>

        <!-- Reset / Claim Again Button -->
        <button onclick="claimDivineRewardDone()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.9rem; font-weight:900; padding:11px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); text-align:center;">
          ✓ आशीर्वाद ग्रहण किया (पूर्ण)
        </button>

      </div>

    </div>
  </div>"""

if 'id="divine-gift-modal"' not in html:
    pos_body = html.find('</body>')
    html = html[:pos_body] + divine_gift_modal_html + "\n\n" + html[pos_body:]
    print("✓ Injected #divine-gift-modal into index.html")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Updated index.html")

# 2. Append Javascript Logic in app.js
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

divine_rewards_upgraded_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎁 DAIVIYA UPHAAR PURASKAR (DIVINE REWARDS) CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════

window.DIVINE_WALLPAPERS = [
  { title: 'बाल गणेश 4K वॉलपेपर', img: 'assets/gallery/bal_ganesha.jpg' },
  { title: 'बाल हनुमान 4K वॉलपेपर', img: 'assets/gallery/bal_hanuman.jpg' },
  { title: 'दिव्य श्री कृष्ण 4K वॉलपेपर', img: 'assets/gallery/bal_krishna.jpg' },
  { title: 'देवाधिदेव महादेव 4K वॉलपेपर', img: 'assets/gallery/bal_shiva.jpg' },
  { title: 'माँ महालक्ष्मी 4K वॉलपेपर', img: 'assets/gallery/bal_lakshmi.jpg' },
  { title: 'माँ जगदम्बे 4K वॉलपेपर', img: 'assets/gallery/bal_durga.jpg' }
];

window.DIVINE_BLESSINGS = [
  {
    shlok: '॥ सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते ॥',
    meaning: 'माँ भगवती आपके समस्त मनोरथ सिद्ध करें और घर में अखंड सुख-शांति व समृद्धि का वास हो।'
  },
  {
    shlok: '॥ ॐ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥',
    meaning: 'प्रथम पूज्य श्री गणेश जी आपके जीवन के सभी विघ्न दूर कर हर कार्य में शुभता प्रदान करें।'
  },
  {
    shlok: '॥ मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम्। वातात्मजं वानरयूथमुख्यं श्रीरामदूतं शरणं प्रपद्ये ॥',
    meaning: 'पवनपुत्र श्री हनुमान जी आपको असीम बल, तेज, आरोग्य और भयमुक्ति का आशीर्वाद प्रदान करें।'
  },
  {
    shlok: '॥ ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान् मृत्योर्मुक्षीय मामृतात् ॥',
    meaning: 'महादेव शिव शम्भू आपके परिवार को दीर्घायु, आरोग्य और समस्त संकटों से रक्षा प्रदान करें।'
  }
];

window.claimDivineGift = function() {
  const modal = document.getElementById('divine-gift-modal');
  const chestStage = document.getElementById('gift-chest-stage');
  const rewardStage = document.getElementById('gift-reward-stage');
  
  if (chestStage) chestStage.style.display = 'flex';
  if (rewardStage) rewardStage.style.display = 'none';

  if (modal) {
    modal.style.display = 'flex';
    if (navigator.vibrate) navigator.vibrate(40);
  }
};

window.closeDivineGiftModal = function() {
  const modal = document.getElementById('divine-gift-modal');
  if (modal) modal.style.display = 'none';
};

window.openMysteryChestAnimation = function() {
  const chest = document.getElementById('mystery-chest-box');
  const chestIcon = document.getElementById('chest-icon');

  if (chest) {
    chest.style.transform = 'scale(1.3) rotate(15deg)';
    setTimeout(() => { chest.style.transform = 'scale(0.85) rotate(-15deg)'; }, 150);
    setTimeout(() => { chest.style.transform = 'scale(1.4) rotate(0deg)'; }, 300);
  }

  if (chestIcon) {
    chestIcon.textContent = '✨';
  }

  if (typeof triggerFlowerShower === 'function') {
    triggerFlowerShower();
  }

  if (navigator.vibrate) navigator.vibrate([60, 40, 100]);

  // Update Punya Coins
  let currentCoins = parseInt(localStorage.getItem('bhakti_punya_coins') || '100');
  currentCoins += 25;
  localStorage.setItem('bhakti_punya_coins', currentCoins.toString());

  const walletBadge = document.getElementById('wallet-balance-badge');
  if (walletBadge) walletBadge.textContent = `कुल: ${currentCoins} 🪙`;

  // Pick Random Wallpaper
  const randWp = window.DIVINE_WALLPAPERS[Math.floor(Math.random() * window.DIVINE_WALLPAPERS.length)];
  const wpImg = document.getElementById('reward-wallpaper-img');
  const wpTitle = document.getElementById('reward-wallpaper-title');
  const wpBtn = document.getElementById('reward-wallpaper-btn');
  if (wpImg) wpImg.src = randWp.img;
  if (wpTitle) wpTitle.textContent = `🖼️ ${randWp.title}`;
  if (wpBtn) {
    wpBtn.href = randWp.img;
    wpBtn.download = `${randWp.title}.jpg`;
  }

  // Pick Random Blessing
  const randBl = window.DIVINE_BLESSINGS[Math.floor(Math.random() * window.DIVINE_BLESSINGS.length)];
  const blShlok = document.getElementById('reward-blessing-shlok');
  const blMeaning = document.getElementById('reward-blessing-meaning');
  if (blShlok) blShlok.textContent = randBl.shlok;
  if (blMeaning) blMeaning.textContent = randBl.meaning;

  setTimeout(() => {
    const chestStage = document.getElementById('gift-chest-stage');
    const rewardStage = document.getElementById('gift-reward-stage');
    if (chestStage) chestStage.style.display = 'none';
    if (rewardStage) rewardStage.style.display = 'flex';
  }, 600);
};

window.shareBlessingCardWhatsApp = function() {
  const shlok = document.getElementById('reward-blessing-shlok')?.textContent || '';
  const meaning = document.getElementById('reward-blessing-meaning')?.textContent || '';
  const text = `🌸 पावन दैवीय आशीर्वाद पत्र 🌸\\n\\n${shlok}\\n\\n📖 भावार्थ: ${meaning}\\n\\n🙏 भक्ति में लीन ऐप: http://localhost:8000`;
  
  if (navigator.share) {
    navigator.share({ title: 'पावन दैवीय आशीर्वाद पत्र', text: text }).catch(() => {});
  } else {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  }
};

window.claimDivineRewardDone = function() {
  window.closeDivineGiftModal();
  if (typeof showToast === 'function') {
    showToast('🙏 दिव्य पुरस्कार व आशीर्वाद ग्रहण किया गया!');
  }
};
"""

js += "\n\n" + divine_rewards_upgraded_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected upgraded Divine Rewards handlers into app.js")

print("=" * 80)
print("DIVINE REWARDS UPGRADE COMPLETED SUCCESSFULLY")
print("=" * 80)
