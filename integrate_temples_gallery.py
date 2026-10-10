import re, sys, os, json, shutil
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
print("INTEGRATING INDIA & WORLD TEMPLES INTO DIVINE GALLERY")
print("=" * 80)

# 1. Copy generated temple images
for prefix, dest_name in [
    ('temple_mahakaleshwar', 'temple_mahakaleshwar.jpg'),
    ('temple_kashi', 'temple_kashi.jpg'),
    ('temple_angkor_wat', 'temple_angkor_wat.jpg')
]:
    matches = list(brain_dir.glob(f"{prefix}_*.jpg"))
    if matches:
        latest = sorted(matches, key=os.path.getmtime, reverse=True)[0]
        dest = GALLERY_DIR / dest_name
        shutil.copyfile(latest, dest)
        print(f"✓ Copied {latest.name} -> assets/gallery/{dest_name}")

# 2. Parse raw text and extract unique India and World temples
import parse_temples_data

india_temples = parse_temples_data.india_temples
world_temples = parse_temples_data.world_temples

# Assign custom images to key temples
for t in india_temples:
    if 'महाकालेश्वर' in t['nameHi']:
        t['img'] = 'assets/gallery/temple_mahakaleshwar.jpg'
    elif 'काशी विश्वनाथ' in t['nameHi']:
        t['img'] = 'assets/gallery/temple_kashi.jpg'
    elif 'सोमनाथ' in t['nameHi']:
        t['img'] = 'assets/gallery/temple_kashi.jpg'
    elif 'जगन्नाथ' in t['nameHi']:
        t['img'] = 'assets/gallery/bal_vishnu.jpg'
    elif 'तिरुपति' in t['nameHi'] or 'बालाजी' in t['nameHi']:
        t['img'] = 'assets/gallery/divya_vishnu.jpg'
    elif 'मीनाक्षी' in t['nameHi']:
        t['img'] = 'assets/gallery/divya_lakshmi.jpg'
    elif 'सिद्धिविनायक' in t['nameHi']:
        t['img'] = 'assets/gallery/divya_ganesha.jpg'
    else:
        t['img'] = 'assets/panchang_book.jpg'

for t in world_temples:
    if 'अंकोरवाट' in t['nameHi']:
        t['img'] = 'assets/gallery/temple_angkor_wat.jpg'
    elif 'पशुपतिनाथ' in t['nameHi']:
        t['img'] = 'assets/gallery/divya_shiva.jpg'
    elif 'प्रम्बानन' in t['nameHi']:
        t['img'] = 'assets/gallery/divya_shiva.jpg'
    elif 'बाटू' in t['nameHi']:
        t['img'] = 'assets/gallery/divya_hanuman.jpg'
    else:
        t['img'] = 'assets/panchang_book.jpg'

print(f"India temples: {len(india_temples)}, World temples: {len(world_temples)}")

# 3. Add to app.js
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

temples_js = f"""
// ══════════════════════════════════════════════════════════════════════════════
// 🚩 SACRED TEMPLES OF INDIA & WORLDWIDE HINDU SANCTUARIES
// ══════════════════════════════════════════════════════════════════════════════

window.INDIA_TEMPLES_GALLERY = {json.dumps(india_temples, ensure_ascii=False, indent=2)};

window.WORLD_TEMPLES_GALLERY = {json.dumps(world_temples, ensure_ascii=False, indent=2)};
"""

# Enhanced renderDivineGallery with India & World Temple tabs
render_gallery_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🖼️ ENHANCED 4-TAB DIVINE GALLERY (BAL ROOP, DIVYA ROOP, INDIA & WORLD TEMPLES)
// ══════════════════════════════════════════════════════════════════════════════

window.currentGalleryTab = 'bal';
window.currentGalleryCategory = 'all';
window.currentGallerySearch = '';

window.switchGalleryTab = function(tab) {
  window.currentGalleryTab = tab;
  document.querySelectorAll('.gal-tab-pill').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tab);
  });
  window.renderDivineGallery();
};

window.filterGalleryCategory = function(cat) {
  window.currentGalleryCategory = cat;
  document.querySelectorAll('.gal-cat-chip').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.cat === cat);
  });
  window.renderDivineGallery();
};

window.renderDivineGallery = function() {
  const container = document.getElementById('gallery-grid-container');
  const countEl = document.getElementById('gallery-count-badge');
  const catChipsWrap = document.getElementById('gallery-category-chips');
  
  if (!container) return;

  let dataset = [];
  let tabName = '';

  if (window.currentGalleryTab === 'bal') {
    dataset = window.BAL_ROOP_GALLERY || [];
    tabName = 'बाल रूप';
    if (catChipsWrap) catChipsWrap.style.display = 'flex';
  } else if (window.currentGalleryTab === 'divya') {
    dataset = window.DIVYA_ROOP_GALLERY || [];
    tabName = 'दिव्य रूप';
    if (catChipsWrap) catChipsWrap.style.display = 'flex';
  } else if (window.currentGalleryTab === 'india') {
    dataset = window.INDIA_TEMPLES_GALLERY || [];
    tabName = 'भारत के प्रमुख मंदिर';
    if (catChipsWrap) catChipsWrap.style.display = 'none';
  } else if (window.currentGalleryTab === 'world') {
    dataset = window.WORLD_TEMPLES_GALLERY || [];
    tabName = 'विश्व के प्रमुख मंदिर';
    if (catChipsWrap) catChipsWrap.style.display = 'none';
  }

  // Filter by search
  const q = (window.currentGallerySearch || '').toLowerCase().trim();
  let filtered = dataset.filter(item => {
    const matchCat = (window.currentGalleryTab === 'india' || window.currentGalleryTab === 'world' || window.currentGalleryCategory === 'all' || item.category === window.currentGalleryCategory);
    const matchQuery = !q || (item.nameHi && item.nameHi.toLowerCase().includes(q)) || 
                             (item.nameEn && item.nameEn.toLowerCase().includes(q)) ||
                             (item.location && item.location.toLowerCase().includes(q)) ||
                             (item.famous && item.famous.toLowerCase().includes(q));
    return matchCat && matchQuery;
  });

  if (countEl) {
    countEl.textContent = `${filtered.length} ${tabName}`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column:1/-1; text-align:center; padding:3rem 1rem; color:#FDE68A;">
        <div style="font-size:2.5rem; margin-bottom:0.5rem;">🔍</div>
        <div style="font-size:1.1rem; font-weight:800;">कोई परिणाम नहीं मिला</div>
        <div style="font-size:0.85rem; color:#94A3B8;">कृपया दूसरा शब्द खोजें अथवा फ़िल्टर बदलें</div>
      </div>
    `;
    return;
  }

  // Render Temples vs Deities
  if (window.currentGalleryTab === 'india' || window.currentGalleryTab === 'world') {
    container.innerHTML = filtered.map((t, idx) => `
      <div class="temple-card-royal" onclick="window.openTempleLightbox('${window.currentGalleryTab}', '${t.id}')">
        <div class="temple-card-img-wrap">
          <img src="${t.img}" class="temple-card-img" alt="${t.nameHi}" onerror="this.src='assets/panchang_book.jpg'" />
          <div class="temple-card-num">#${idx+1}</div>
        </div>
        <div class="temple-card-body">
          <div class="temple-card-title">${t.nameHi}</div>
          <div class="temple-card-sub">${t.nameEn}</div>
          <div class="temple-card-loc">📍 ${t.location}</div>
          <div class="temple-card-famous">✨ ${t.famous}</div>
          ${t.food ? `<div class="temple-card-food">🍯 <b>प्रसाद:</b> ${t.food}</div>` : ''}
          <div class="temple-card-actions">
            <a href="${t.mapUrl}" target="_blank" onclick="event.stopPropagation();" class="temple-map-btn">
              📍 Google Map
            </a>
            <button class="temple-darshan-btn" onclick="event.stopPropagation(); window.openTempleLightbox('${window.currentGalleryTab}', '${t.id}')">
              🪔 दर्शन
            </button>
          </div>
        </div>
      </div>
    `).join('');
  } else {
    // Deity cards
    container.innerHTML = filtered.map(d => `
      <div class="gal-card" onclick="window.openGalleryLightbox('${d.id}')">
        <div class="gal-card-img-wrap">
          <img src="${d.img}" class="gal-card-img" alt="${d.nameHi}" onerror="this.src='${d.fallbackImg}'" />
          <div class="gal-card-badge">${d.category ? d.category.toUpperCase() : 'DIVINE'}</div>
        </div>
        <div class="gal-card-info">
          <div class="gal-card-title">${d.nameHi}</div>
          <div class="gal-card-sub">${d.nameEn}</div>
          <div class="gal-card-mantra">${d.mantra || '॥ ॐ नमः शिवाय ॥'}</div>
          <button class="gal-card-btn" onclick="event.stopPropagation(); window.openGalleryLightbox('${d.id}')">
            🪔 दर्शन करें ❯
          </button>
        </div>
      </div>
    `).join('');
  }
};

window.openTempleLightbox = function(tab, templeId) {
  const dataset = tab === 'india' ? window.INDIA_TEMPLES_GALLERY : window.WORLD_TEMPLES_GALLERY;
  const temple = dataset.find(t => t.id === templeId);
  if (!temple) return;

  const modal = document.getElementById('gallery-lightbox-modal');
  const imgEl = document.getElementById('lightbox-img');
  const titleEl = document.getElementById('lightbox-title');
  const subEl = document.getElementById('lightbox-sub');
  const mantraEl = document.getElementById('lightbox-mantra');

  if (titleEl) titleEl.textContent = temple.nameHi;
  if (subEl) subEl.textContent = `${temple.nameEn} • 📍 ${temple.location}`;
  if (mantraEl) {
    mantraEl.innerHTML = `
      <div style="font-size:0.95rem; color:#FFFDF8; margin-bottom:8px; line-height:1.6;">${temple.famous}</div>
      ${temple.food ? `<div style="font-size:0.85rem; color:#FDE68A; margin-bottom:12px; background:rgba(248,200,59,0.15); padding:6px 12px; border-radius:12px; border:1px solid rgba(248,200,59,0.3);">🍯 <b>प्रसिद्ध भोजन व महाप्रसाद:</b> ${temple.food}</div>` : ''}
      <a href="${temple.mapUrl}" target="_blank" style="display:inline-block; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; padding:8px 18px; border-radius:20px; text-decoration:none; box-shadow:0 4px 15px rgba(248,200,59,0.4);">
        📍 Google Maps पर लोकेशन देखें
      </a>
    `;
  }
  if (imgEl) {
    imgEl.src = temple.img;
    imgEl.onerror = function() { this.src = 'assets/panchang_book.jpg'; };
  }

  if (modal) {
    modal.classList.remove('hidden');
    modal.style.display = 'flex';
  }
};
"""

js += "\n\n" + temples_js.strip() + "\n\n" + render_gallery_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected Temples dataset and 4-Tab Gallery Renderer into app.js")

# 4. Add Temple Card CSS into styles.css
temple_card_css = """
/* ══════════════════════════════════════════════════════════════════
   🚩 TEMPLE CARDS STYLING (INDIA & WORLD TEMPLES)
   ══════════════════════════════════════════════════════════════════ */

.temple-card-royal {
  background: linear-gradient(145deg, #1E0A38 0%, #110424 100%);
  border: 1.5px solid rgba(248, 200, 59, 0.35);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.45);
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
  cursor: pointer;
}

.temple-card-royal:hover {
  transform: translateY(-4px);
  border-color: rgba(248, 200, 59, 0.7);
  box-shadow: 0 12px 30px rgba(248, 200, 59, 0.25);
}

.temple-card-img-wrap {
  width: 100%;
  height: 160px;
  position: relative;
  overflow: hidden;
}

.temple-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.temple-card-royal:hover .temple-card-img {
  transform: scale(1.06);
}

.temple-card-num {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(9, 5, 20, 0.85);
  border: 1px solid #F8C83B;
  color: #FDE68A;
  font-size: 0.75rem;
  font-weight: 900;
  padding: 3px 8px;
  border-radius: 10px;
}

.temple-card-body {
  padding: 1.1rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.temple-card-title {
  font-size: 1.12rem;
  font-weight: 900;
  color: #FFFDF8;
  margin-bottom: 2px;
}

.temple-card-sub {
  font-size: 0.78rem;
  color: #C084FC;
  font-weight: 600;
  margin-bottom: 8px;
}

.temple-card-loc {
  font-size: 0.8rem;
  color: #93C5FD;
  font-weight: 700;
  margin-bottom: 6px;
}

.temple-card-famous {
  font-size: 0.82rem;
  color: #E2E8F0;
  line-height: 1.5;
  margin-bottom: 8px;
  flex: 1;
}

.temple-card-food {
  font-size: 0.78rem;
  color: #FDE68A;
  background: rgba(248, 200, 59, 0.12);
  border: 1px solid rgba(248, 200, 59, 0.25);
  padding: 5px 10px;
  border-radius: 10px;
  margin-bottom: 12px;
}

.temple-card-actions {
  display: flex;
  gap: 8px;
  margin-top: auto;
}

.temple-map-btn {
  flex: 1;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.35);
  color: #FDE68A;
  padding: 7px 10px;
  border-radius: 14px;
  font-size: 0.76rem;
  font-weight: 800;
  text-align: center;
  text-decoration: none;
  transition: all 0.2s ease;
}

.temple-map-btn:hover {
  background: rgba(248, 200, 59, 0.25);
  color: #FFF;
}

.temple-darshan-btn {
  flex: 1;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  border: none;
  padding: 7px 12px;
  border-radius: 14px;
  font-size: 0.78rem;
  font-weight: 900;
  cursor: pointer;
  box-shadow: 0 3px 12px rgba(248, 200, 59, 0.35);
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + temple_card_css)
print("✓ Appended Temple Card CSS to styles.css")

# 5. Update #page-gallery in index.html with 4 Luxury Tabs
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

gallery_section_new = """    <!-- 🖼️ DIVINE DARSHAN & SACRED TEMPLES GALLERY 🖼️ -->
    <section id="page-gallery" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>दिव्य दर्शन व तीर्थ गैलरी</h2>
      </div>

      <!-- 4 Luxury Tabs: Bal Roop, Divya Roop, India Temples, World Temples -->
      <div class="gal-tabs-bar" style="display:flex; gap:8px; overflow-x:auto; padding:0.8rem 1.2rem; scrollbar-width:none;">
        <button class="gal-tab-pill active" data-tab="bal" onclick="switchGalleryTab('bal')">
          👶 बाल रूप (60)
        </button>
        <button class="gal-tab-pill" data-tab="divya" onclick="switchGalleryTab('divya')">
          🕉️ दिव्य रूप (60)
        </button>
        <button class="gal-tab-pill" data-tab="india" onclick="switchGalleryTab('india')">
          🇮🇳 भारत के प्रमुख मंदिर (69)
        </button>
        <button class="gal-tab-pill" data-tab="world" onclick="switchGalleryTab('world')">
          🌍 विश्व के प्रमुख मंदिर (32)
        </button>
      </div>

      <!-- Search & Info Bar -->
      <div style="padding:0 1.2rem 0.6rem; display:flex; align-items:center; justify-content:space-between; gap:10px;">
        <div style="flex:1; position:relative;">
          <input type="text" id="gallery-search-input" placeholder="🔍 नाम, स्थान अथवा विशेषता खोजें..." oninput="window.currentGallerySearch=this.value; renderDivineGallery();" style="width:100%; background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); border-radius:18px; padding:9px 16px; color:#FFF; font-size:0.88rem; outline:none;" />
        </div>
        <div id="gallery-count-badge" style="font-size:0.78rem; font-weight:800; color:#FDE68A; background:rgba(248,200,59,0.15); border:1px solid rgba(248,200,59,0.4); padding:6px 12px; border-radius:14px; white-space:nowrap;">
          लोड हो रहा है...
        </div>
      </div>

      <!-- Category Filter Chips (For Deity Gallery) -->
      <div id="gallery-category-chips" class="gal-cat-chips" style="display:flex; gap:8px; overflow-x:auto; padding:0.2rem 1.2rem 1rem; scrollbar-width:none;">
        <button class="gal-cat-chip active" data-cat="all" onclick="filterGalleryCategory('all')">समस्त देव</button>
        <button class="gal-cat-chip" data-cat="tridev" onclick="filterGalleryCategory('tridev')">त्रिदेव व अवतार</button>
        <button class="gal-cat-chip" data-cat="devi" onclick="filterGalleryCategory('devi')">माँ भगवती</button>
        <button class="gal-cat-chip" data-cat="vedic" onclick="filterGalleryCategory('vedic')">वैदिक देव</button>
        <button class="gal-cat-chip" data-cat="navagraha" onclick="filterGalleryCategory('navagraha')">नवग्रह</button>
        <button class="gal-cat-chip" data-cat="bhakt" onclick="filterGalleryCategory('bhakt')">परम भक्त व नदियां</button>
      </div>

      <!-- Dynamic Cards Grid -->
      <div id="gallery-grid-container" class="gal-grid" style="padding:0 1.2rem 2.5rem; display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:16px;">
        <!-- Injected dynamically via renderDivineGallery() -->
      </div>
    </section>"""

# Replace #page-gallery
pos_gal = html.find('id="page-gallery"')
if pos_gal != -1:
    pos_start = html.rfind('<section', 0, pos_gal)
    pos_end = html.find('</section>', pos_gal) + 10
    html = html[:pos_start] + gallery_section_new + html[pos_end:]
    print("✓ Replaced #page-gallery with 4-Tab Gallery in index.html")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated index.html with new cache buster ?v={ts}")

print("=" * 80)
print("TEMPLES INTEGRATION COMPLETE")
print("=" * 80)
