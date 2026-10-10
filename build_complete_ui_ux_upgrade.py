import re, sys, os, shutil
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"
GALLERY_DIR = BASE_DIR / "assets" / "gallery"
GALLERY_DIR.mkdir(parents=True, exist_ok=True)
brain_dir = Path(r"C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9")

print("=" * 80)
print("BUILDING COMPLETE UI/UX UPGRADE: AUDIO LIB, PROFILE, AARTIS, GALLERY")
print("=" * 80)

# 1. Copy generated images
img_copies = {
    'bal_radha_krishna': 'bal_radha_krishna.jpg',
    'bal_vishnu': 'bal_vishnu.jpg',
    'divya_vishnu': 'divya_vishnu.jpg',
    'divya_lakshmi': 'divya_lakshmi.jpg',
    'divya_radha': 'divya_radha.jpg',
}

for prefix, dest_name in img_copies.items():
    matches = list(brain_dir.glob(f"{prefix}_*.jpg"))
    if matches:
        latest = sorted(matches, key=os.path.getmtime, reverse=True)[0]
        dest = GALLERY_DIR / dest_name
        shutil.copyfile(latest, dest)
        print(f"✓ Copied {latest.name} -> assets/gallery/{dest_name}")

# 2. Read app.js and update Gallery image paths
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Update image paths in BAL_ROOP_GALLERY and DIVYA_ROOP_GALLERY
js = js.replace("'assets/gallery/bal_vishnu.jpg'", "'assets/gallery/bal_vishnu.jpg'")
js = js.replace("id: 'bal-vishnu',\n    nameHi: 'बाल विष्णु',\n    nameEn: 'Little Bal Vishnu',\n    category: 'tridev',\n    mantra: '॥ ॐ नमो भगवते वासुदेवाय ॥',\n    img: 'assets/deity_vishnu.jpg'", "id: 'bal-vishnu',\n    nameHi: 'बाल विष्णु',\n    nameEn: 'Little Bal Vishnu',\n    category: 'tridev',\n    mantra: '॥ ॐ नमो भगवते वासुदेवाय ॥',\n    img: 'assets/gallery/bal_vishnu.jpg'")
js = js.replace("id: 'bal-radha',\n    nameHi: 'बाल राधा',\n    nameEn: 'Little Devi Radha',\n    category: 'devi',\n    mantra: '॥ ॐ श्री राधे ॥',\n    img: 'assets/deity_radha.jpg'", "id: 'bal-radha',\n    nameHi: 'बाल राधा-कृष्ण',\n    nameEn: 'Little Radha Krishna',\n    category: 'devi',\n    mantra: '॥ ॐ श्री राधे कृष्णाय नमः ॥',\n    img: 'assets/gallery/bal_radha_krishna.jpg'")

js = js.replace("id: 'divya-vishnu',\n    nameHi: 'भगवान श्री विष्णु',\n    nameEn: 'Lord Vishnu',\n    category: 'tridev',\n    mantra: '॥ शान्ताकारं भुजगशयनं पद्मनाभं सुरेशं विश्वाधारं गगनसदृशं मेघवर्णं शुभाङ्गम् ॥',\n    img: 'assets/deity_vishnu.jpg'", "id: 'divya-vishnu',\n    nameHi: 'भगवान श्री विष्णु',\n    nameEn: 'Lord Vishnu',\n    category: 'tridev',\n    mantra: '॥ शान्ताकारं भुजगशयनं पद्मनाभं सुरेशं विश्वाधारं गगनसदृशं मेघवर्णं शुभाङ्गम् ॥',\n    img: 'assets/gallery/divya_vishnu.jpg'")
js = js.replace("id: 'divya-lakshmi',\n    nameHi: 'माँ लक्ष्मी',\n    nameEn: 'Goddess Lakshmi',\n    category: 'devi',\n    mantra: '॥ ॐ श्रीं ह्रीं क्लीं श्री सिद्ध लक्ष्म्यै नमः ॥',\n    img: 'assets/deity_lakshmi.jpg'", "id: 'divya-lakshmi',\n    nameHi: 'माँ लक्ष्मी',\n    nameEn: 'Goddess Lakshmi',\n    category: 'devi',\n    mantra: '॥ ॐ श्रीं ह्रीं क्लीं श्री सिद्ध लक्ष्म्यै नमः ॥',\n    img: 'assets/gallery/divya_lakshmi.jpg'")
js = js.replace("id: 'divya-radha',\n    nameHi: 'श्री राधारानी',\n    nameEn: 'Goddess Radha',\n    category: 'devi',\n    mantra: '॥ तप्तकाञ्चनगौराङ्गि राधे वृन्दावनेश्वरि । वृषभानुसुते देवि प्रणमामि हरिप्रिये ॥',\n    img: 'assets/deity_radha.jpg'", "id: 'divya-radha',\n    nameHi: 'श्री राधारानी',\n    nameEn: 'Goddess Radha',\n    category: 'devi',\n    mantra: '॥ तप्तकाञ्चनगौराङ्गि राधे वृन्दावनेश्वरि । वृषभानुसुते देवि प्रणमामि हरिप्रिये ॥',\n    img: 'assets/gallery/divya_radha.jpg'")

# 3. Explicitly define openAartiCollectionModal on window with bulletproof display
aarti_modal_fix_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 GUARANTEED BULLETPROOF AARTI COLLECTION MODAL CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.openAartiCollectionModal = function(deityKey) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll) {
    console.warn('Aarti collection not found:', deityKey);
    return;
  }

  const modal = document.getElementById('aarti-options-modal');
  if (!modal) return;

  const titleEl = document.getElementById('aarti-modal-title');
  const deityEl = document.getElementById('aarti-modal-deity');
  const mantraEl = document.getElementById('aarti-modal-mantra');
  const imgEl = document.getElementById('aarti-modal-img');
  const listContainer = document.getElementById('aarti-modal-list');

  if (titleEl) titleEl.textContent = coll.title;
  if (deityEl) deityEl.textContent = coll.deity;
  if (mantraEl) mantraEl.textContent = coll.mantra;
  
  if (imgEl) {
    imgEl.src = coll.img;
    imgEl.onerror = function() { this.src = coll.fallbackImg; };
  }

  if (listContainer) {
    listContainer.innerHTML = coll.items.map((item, idx) => `
      <div class="aarti-opt-card" onclick="window.readAartiItemDirect('${deityKey}', ${idx})">
        <div class="aarti-opt-index">0${idx+1}</div>
        <div class="aarti-opt-info">
          <div class="aarti-opt-title">${item.title}</div>
          <div class="aarti-opt-sub">${item.sub}</div>
        </div>
        <div class="aarti-opt-actions">
          <button class="aarti-opt-read-btn" onclick="event.stopPropagation(); window.readAartiItemDirect('${deityKey}', ${idx})" title="पाठ पढ़ें">
            📖 पढ़ें
          </button>
          <button class="aarti-opt-play-btn" onclick="event.stopPropagation(); window.playAartiItemDirect('${deityKey}', ${idx})" title="आरती सुनें">
            ▶
          </button>
        </div>
      </div>
    `).join('');
  }

  modal.classList.remove('hidden');
  modal.classList.add('active');
  modal.style.display = 'flex';
  modal.style.opacity = '1';
  modal.style.pointerEvents = 'auto';

  if (navigator.vibrate) navigator.vibrate(30);
};

window.closeAartiOptionsModal = function() {
  const modal = document.getElementById('aarti-options-modal');
  if (modal) {
    modal.classList.remove('active');
    modal.style.display = 'none';
    modal.style.pointerEvents = 'none';
  }
};

window.readAartiItemDirect = function(deityKey, idx) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items[idx]) return;
  const item = coll.items[idx];
  
  window.closeAartiOptionsModal();

  // Load into Reader
  const readerTitle = document.getElementById('reader-title');
  const readerContent = document.getElementById('reader-content');
  if (readerTitle) readerTitle.textContent = item.title;
  if (readerContent) {
    readerContent.innerHTML = `
      <div style="text-align:center; padding:1rem 0;">
        <div style="font-size:1.15rem; color:#D97706; font-weight:800; margin-bottom:0.5rem;">${coll.deity}</div>
        <div style="font-size:0.9rem; color:#78350F; font-weight:600; margin-bottom:1.5rem;">${coll.mantra}</div>
        <div style="white-space:pre-line; text-align:center; line-height:2.2; font-size:1.15rem; color:#1A0B2E; font-weight:700; font-family:'Tiro Devanagari Hindi', serif;">${item.content}</div>
      </div>
    `;
  }
  window.showPage('page-reader');
};

window.playAartiItemDirect = function(deityKey, idx) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items[idx]) return;
  const item = coll.items[idx];
  
  window.closeAartiOptionsModal();

  const record = {
    title: item.title,
    deity_id: deityKey,
    deity_name_hi: coll.deity,
    content_type: 'aarti',
    audio_url: item.audio_url,
    content: item.content
  };

  if (window.MediaRouter) {
    window.MediaRouter.playRecord(record);
  }
};
"""

js += "\n" + aarti_modal_fix_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected guaranteed Aarti modal controller in app.js")

# 4. Classic Profile Page UI & Audio Library UI in styles.css
classic_styles_css = """
/* ══════════════════════════════════════════════════════════════════
   👑 CLASSIC ROYAL VEDIC AUDIO LIBRARY & PROFILE PAGE STYLING
   ══════════════════════════════════════════════════════════════════ */

/* Classic Audio Library */
.katha-hero-royal {
  background: linear-gradient(135deg, #1C0A35 0%, #3B1259 50%, #150628 100%);
  border: 1.5px solid rgba(248, 200, 59, 0.4);
  border-radius: 24px;
  padding: 1.4rem;
  margin: 1rem 1.2rem 1.2rem;
  color: #FFFDF8;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.katha-hero-royal::after {
  content: '';
  position: absolute;
  top: -50%; right: -20%;
  width: 250px; height: 250px;
  background: radial-gradient(circle, rgba(248, 200, 59, 0.2) 0%, transparent 70%);
  pointer-events: none;
}

.katha-filter-chips {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 0.4rem 1.2rem 1rem;
  scrollbar-width: none;
}

.katha-filter-chips::-webkit-scrollbar { display: none; }

.katha-chip {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.3);
  color: #FDE68A;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}

.katha-chip.active, .katha-chip:hover {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  border-color: #F8C83B;
  box-shadow: 0 4px 12px rgba(248, 200, 59, 0.4);
}

/* Classic Profile Styling */
.profile-royal-card {
  background: linear-gradient(145deg, #240C42 0%, #150628 100%);
  border: 1.5px solid rgba(248, 200, 59, 0.4);
  border-radius: 28px;
  padding: 1.6rem 1.4rem;
  margin: 1rem 1.2rem 1.4rem;
  text-align: center;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
  position: relative;
  overflow: hidden;
}

.profile-avatar-wrap {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  margin: 0 auto 0.8rem;
  padding: 4px;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  box-shadow: 0 0 25px rgba(248, 200, 59, 0.4);
}

.profile-avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  background: #1A0B2E;
}

.profile-name-title {
  font-size: 1.35rem;
  font-weight: 900;
  color: #FFFDF8;
  margin-bottom: 2px;
}

.profile-status-badge {
  display: inline-block;
  background: rgba(248, 200, 59, 0.15);
  border: 1px solid rgba(248, 200, 59, 0.4);
  color: #FDE68A;
  font-size: 0.76rem;
  font-weight: 800;
  padding: 3px 12px;
  border-radius: 12px;
  margin-bottom: 1rem;
}

.profile-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(248, 200, 59, 0.2);
}

.profile-stat-box {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 10px 6px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.profile-stat-val {
  font-size: 1.25rem;
  font-weight: 900;
  color: #F8C83B;
}

.profile-stat-lbl {
  font-size: 0.72rem;
  color: #E2E8F0;
  font-weight: 600;
}

.profile-menu-section {
  margin: 0 1.2rem 1.4rem;
}

.profile-menu-item {
  background: linear-gradient(135deg, rgba(32, 12, 60, 0.85) 0%, rgba(18, 6, 36, 0.95) 100%);
  border: 1px solid rgba(248, 200, 59, 0.25);
  border-radius: 20px;
  padding: 14px 16px;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  transition: all 0.2s ease;
}

.profile-menu-item:hover {
  transform: translateX(4px);
  border-color: rgba(248, 200, 59, 0.6);
}

.profile-menu-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: rgba(248, 200, 59, 0.15);
  border: 1px solid rgba(248, 200, 59, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.profile-menu-text {
  flex: 1;
}

.profile-menu-title {
  font-size: 0.96rem;
  font-weight: 800;
  color: #FFFDF8;
}

.profile-menu-sub {
  font-size: 0.75rem;
  color: #94A3B8;
  font-weight: 600;
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + classic_styles_css)
print("✓ Appended Classic Audio Library & Profile CSS to styles.css")

# 5. Replace #page-profile content in index.html with the classic royal UI
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

profile_section_new = """    <!-- PROFILE PAGE (CLASSIC ROYAL VEDIC UI) 👤 -->
    <section id="page-profile" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2 data-i18n="nav_profile">प्रोफ़ाइल</h2>
      </div>

      <!-- Royal Profile Card -->
      <div class="profile-royal-card">
        <div class="profile-avatar-wrap">
          <img src="assets/gallery/bal_ganesha.jpg" id="prof-user-avatar" class="profile-avatar-img" alt="User Avatar" />
        </div>
        <div class="profile-name-title" id="prof-user-name">भक्त जन</div>
        <div class="profile-status-badge">✨ दैनिक वैदिक साधक</div>
        
        <div>
          <button onclick="openAuthModal()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-weight:900; font-size:0.85rem; padding:8px 20px; border-radius:20px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.35);">
            🔑 खाता बदलें / लॉगिन करें
          </button>
        </div>

        <div class="profile-stats-grid">
          <div class="profile-stat-box">
            <div class="profile-stat-val" id="prof-stat-jaap">108</div>
            <div class="profile-stat-lbl">जाप संख्या</div>
          </div>
          <div class="profile-stat-box">
            <div class="profile-stat-val" id="prof-stat-streak">7 दिन</div>
            <div class="profile-stat-lbl">साधना स्ट्रीक</div>
          </div>
          <div class="profile-stat-box">
            <div class="profile-stat-val" id="prof-stat-favs">12</div>
            <div class="profile-stat-lbl">पसंदीदा</div>
          </div>
        </div>
      </div>

      <!-- Settings & Tools Menu -->
      <div class="profile-menu-section">
        <h3 style="font-size:1rem; font-weight:900; color:#1A0B2E; margin:0 0 10px 4px; display:flex; align-items:center; gap:6px;">
          <span>⚙️</span> आध्यात्मिक सेटिंग्स व सुविधाएं
        </h3>

        <!-- Language Selector -->
        <div class="profile-menu-item" onclick="showPage('page-settings')">
          <div class="profile-menu-icon">🌐</div>
          <div class="profile-menu-text">
            <div class="profile-menu-title">ऐप भाषा (Language)</div>
            <div class="profile-menu-sub">हिन्दी / English / संस्कृत</div>
          </div>
          <div style="color:#FDE68A; font-weight:800; font-size:0.9rem;">❯</div>
        </div>

        <!-- Onboarding Tour Replay -->
        <div class="profile-menu-item" onclick="replayOnboarding()">
          <div class="profile-menu-icon">🔄</div>
          <div class="profile-menu-text">
            <div class="profile-menu-title">ऐप स्वागत यात्रा (Tour)</div>
            <div class="profile-menu-sub">5-स्लाइड वाली भक्ति यात्रा दोबारा देखें</div>
          </div>
          <div style="color:#FDE68A; font-weight:800; font-size:0.9rem;">❯</div>
        </div>

        <!-- Japa Mala Settings -->
        <div class="profile-menu-item" onclick="showPage('page-mala')">
          <div class="profile-menu-icon">📿</div>
          <div class="profile-menu-text">
            <div class="profile-menu-title">डिजिटल जाप माला</div>
            <div class="profile-menu-sub">108x मणके, कम्पन व शंख ध्वनि</div>
          </div>
          <div style="color:#FDE68A; font-weight:800; font-size:0.9rem;">❯</div>
        </div>

        <!-- Share App -->
        <div class="profile-menu-item" onclick="shareDivineCard()">
          <div class="profile-menu-icon">📤</div>
          <div class="profile-menu-text">
            <div class="profile-menu-title">मित्रों को शेयर करें</div>
            <div class="profile-menu-sub">सनातन धर्म का पावन प्रचार करें</div>
          </div>
          <div style="color:#FDE68A; font-weight:800; font-size:0.9rem;">❯</div>
        </div>

        <!-- Rate Modal -->
        <div class="profile-menu-item" onclick="document.getElementById('rate-modal').classList.remove('hidden'); document.getElementById('rate-modal').style.display='flex';">
          <div class="profile-menu-icon">⭐</div>
          <div class="profile-menu-text">
            <div class="profile-menu-title">ऐप को 5 स्टार रेटिंग दें</div>
            <div class="profile-menu-sub">अपना अमूल्य आशीर्वाद एवं सुझाव दें</div>
          </div>
          <div style="color:#FDE68A; font-weight:800; font-size:0.9rem;">❯</div>
        </div>

        <!-- Logout / Guest Reset -->
        <div class="profile-menu-item" onclick="handleLogout()">
          <div class="profile-menu-icon" style="background:rgba(239,68,68,0.2); border-color:rgba(239,68,68,0.4);">🚪</div>
          <div class="profile-menu-text">
            <div class="profile-menu-title" style="color:#FCA5A5;">लॉग आउट (Log Out)</div>
            <div class="profile-menu-sub">खाता रीसेट करें अथवा नया लॉगिन करें</div>
          </div>
          <div style="color:#FCA5A5; font-weight:800; font-size:0.9rem;">❯</div>
        </div>
      </div>
    </section>"""

# Replace page-profile in index.html
pos_prof = html.find('id="page-profile"')
if pos_prof != -1:
    pos_sec_start = html.rfind('<section', 0, pos_prof)
    pos_sec_end = html.find('</section>', pos_prof) + 10
    html = html[:pos_sec_start] + profile_section_new + html[pos_sec_end:]
    print("✓ Replaced #page-profile with Classic Royal Vedic UI in index.html")

# 6. Ensure direct onclick handlers on Home Aarti Cards
home_aarti_replacement = """        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
          
          <!-- Ganesh Aarti Card -->
          <div onclick="window.openAartiCollectionModal('ganesh')" style="background:linear-gradient(145deg, #2A0D4E 0%, #150628 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:20px; padding:1rem; cursor:pointer; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.4); position:relative; overflow:hidden;">
            <div style="position:absolute; top:6px; right:8px; font-size:0.68rem; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:2px 6px; border-radius:8px; font-weight:800;">3 आरतियां</div>
            <img src="assets/gallery/bal_ganesha.jpg" onerror="this.src='assets/deity_ganesh.jpg'" style="width:65px; height:65px; border-radius:50%; object-fit:cover; border:2px solid #F8C83B; margin-bottom:8px; box-shadow:0 0 15px rgba(248,200,59,0.3);" />
            <div style="color:#FFFDF8; font-weight:900; font-size:0.95rem; margin-bottom:2px;">श्री गणेश आरती</div>
            <div style="color:#FBCFE8; font-size:0.72rem; margin-bottom:8px;">जय गणेश • विनायक • गणपति सेवा</div>
            <button onclick="event.stopPropagation(); window.openAartiCollectionModal('ganesh')" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:5px 14px; border-radius:12px; border:none; cursor:pointer; width:100%;">आरती चुनें ❯</button>
          </div>

          <!-- Hanuman Aarti Card -->
          <div onclick="window.openAartiCollectionModal('hanuman')" style="background:linear-gradient(145deg, #2A0D4E 0%, #150628 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:20px; padding:1rem; cursor:pointer; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.4); position:relative; overflow:hidden;">
            <div style="position:absolute; top:6px; right:8px; font-size:0.68rem; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:2px 6px; border-radius:8px; font-weight:800;">3 आरतियां</div>
            <img src="assets/gallery/bal_hanuman.jpg" onerror="this.src='assets/deity_hanuman.jpg'" style="width:65px; height:65px; border-radius:50%; object-fit:cover; border:2px solid #F8C83B; margin-bottom:8px; box-shadow:0 0 15px rgba(248,200,59,0.3);" />
            <div style="color:#FFFDF8; font-weight:900; font-size:0.95rem; margin-bottom:2px;">श्री हनुमान आरती</div>
            <div style="color:#FBCFE8; font-size:0.72rem; margin-bottom:8px;">हनुमान लला • बालाजी • पवनसुत</div>
            <button onclick="event.stopPropagation(); window.openAartiCollectionModal('hanuman')" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:5px 14px; border-radius:12px; border:none; cursor:pointer; width:100%;">आरती चुनें ❯</button>
          </div>

        </div>"""

pos_cards = html.find('<!-- 🪔 NITYA AARTI COLLECTION CARDS (GANESH & HANUMAN) 🪔 -->')
if pos_cards != -1:
    pos_grid = html.find('<div style="display:grid; grid-template-columns:1fr 1fr;', pos_cards)
    pos_grid_end = html.find('</div>\n      </div>', pos_grid)
    html = html[:pos_grid] + home_aarti_replacement + html[pos_grid_end+7:]
    print("✓ Updated Home Page Ganesh & Hanuman Aarti cards with explicit window.openAartiCollectionModal")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated index.html with new cache buster ?v={ts}")

print("=" * 80)
print("ALL UPGRADES COMPLETE & INTEGRATED")
print("=" * 80)
