import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("OVERHAULING DIVINE GALLERY (PAGE-GALLERY) UI/UX TO ROYAL VEDIC LUXURY")
print("=" * 80)

# 1. Update index.html page-gallery header and elements
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

clean_gallery_header_html = """    <!-- ═════════════════════════════════════════════════════════════════
         🖼️ ROYAL DIVINE GALLERY & SACRED TEMPLES PILGRIMAGE 🖼️
         ═════════════════════════════════════════════════════════════════ -->
    <section id="page-gallery" class="page">
      
      <!-- Top Royal Header Bar -->
      <div class="gallery-topbar">
        <button class="gallery-back-btn" onclick="showPage('page-home')">❮</button>
        <h2 class="gallery-heading">॥ दिव्य दर्शन व तीर्थ गैलरी ॥</h2>
        <button class="gallery-action-btn" onclick="triggerFlowerShower()" title="पुष्प वर्षा">🌸</button>
      </div>

      <!-- 4 Luxury Pill Tabs -->
      <div class="gal-tabs-bar">
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

      <!-- Luxury Search & Counter Row -->
      <div class="gallery-search-row">
        <div class="gallery-search-input-box">
          <span class="gallery-search-icon">🔍</span>
          <input type="text" id="gallery-search-input" class="gallery-search-field" placeholder="नाम, स्थान अथवा विशेषता खोजें..." oninput="window.currentGallerySearch=this.value; renderDivineGallery();" />
        </div>
        <div id="gallery-count-badge" class="gallery-counter-badge">
          60 स्वरूप
        </div>
      </div>

      <!-- Subcategory Filter Chips -->
      <div id="gallery-category-chips" class="gal-cat-chips">
        <button class="gal-cat-chip active" data-cat="all" onclick="filterGalleryCategory('all')">✨ समस्त स्वरूप</button>
        <button class="gal-cat-chip" data-cat="tridev" onclick="filterGalleryCategory('tridev')">🔱 त्रिदेव व अवतार</button>
        <button class="gal-cat-chip" data-cat="devi" onclick="filterGalleryCategory('devi')">🌺 माँ भगवती</button>
        <button class="gal-cat-chip" data-cat="vedic" onclick="filterGalleryCategory('vedic')">☀️ वैदिक देव</button>
        <button class="gal-cat-chip" data-cat="navgraha" onclick="filterGalleryCategory('navgraha')">🪐 नवग्रह</button>
        <button class="gal-cat-chip" data-cat="bhakt" onclick="filterGalleryCategory('bhakt')">🚩 परम भक्त व नदियां</button>
      </div>

      <!-- Main Divine Gallery Grid -->
      <div id="gallery-grid-container" class="gallery-cards-grid">
        <!-- Rendered dynamically via renderDivineGallery() -->
      </div>

    </section>"""

pos_gal = html.find('id="page-gallery"')
if pos_gal != -1:
    pos_end_sec = html.find('</section>', pos_gal) + 10
    html = html[:pos_gal-10] + clean_gallery_header_html[7:] + html[pos_end_sec:]
    print("✓ Replaced page-gallery markup in index.html")

# 2. Append Royal Vedic Gallery CSS in styles.css
gallery_luxury_css = """
/* ══════════════════════════════════════════════════════════════════
   🏛️ ULTRA-LUXURY ROYAL VEDIC GALLERY STYLES (#PAGE-GALLERY)
   ══════════════════════════════════════════════════════════════════ */

#page-gallery {
  background: radial-gradient(circle at 50% 10%, #250B40 0%, #120422 55%, #080112 100%) !important;
  color: #FFFDF8 !important;
  min-height: 100vh !important;
  padding-bottom: 90px !important;
}

/* Topbar */
.gallery-topbar {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 1rem 1.2rem 0.8rem !important;
  background: linear-gradient(180deg, rgba(35, 10, 60, 0.9) 0%, rgba(18, 4, 34, 0.4) 100%) !important;
  border-bottom: 1px solid rgba(248, 200, 59, 0.25) !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 100 !important;
  backdrop-filter: blur(20px) !important;
}

.gallery-back-btn, .gallery-action-btn {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  color: #FDE68A !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 50% !important;
  font-size: 1.1rem !important;
  font-weight: 900 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.gallery-back-btn:active, .gallery-action-btn:active {
  transform: scale(0.92) !important;
  background: rgba(248, 200, 59, 0.25) !important;
}

.gallery-heading {
  font-size: 1.12rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  letter-spacing: 0.5px !important;
  text-shadow: 0 0 15px rgba(248, 200, 59, 0.4) !important;
  margin: 0 !important;
}

/* 4 Main Tabs Bar */
.gal-tabs-bar {
  display: flex !important;
  gap: 10px !important;
  overflow-x: auto !important;
  padding: 1rem 1.2rem 0.6rem !important;
  scrollbar-width: none !important;
}

.gal-tabs-bar::-webkit-scrollbar {
  display: none !important;
}

.gal-tab-pill {
  flex-shrink: 0 !important;
  background: rgba(255, 255, 255, 0.07) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.3) !important;
  color: #FDE68A !important;
  font-size: 0.88rem !important;
  font-weight: 800 !important;
  padding: 10px 18px !important;
  border-radius: 22px !important;
  cursor: pointer !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
  white-space: nowrap !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;
}

.gal-tab-pill:hover {
  background: rgba(255, 255, 255, 0.12) !important;
  border-color: rgba(248, 200, 59, 0.6) !important;
  color: #FFF !important;
}

.gal-tab-pill.active {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%) !important;
  color: #1A0B2E !important;
  font-weight: 900 !important;
  border-color: #FEF3C7 !important;
  box-shadow: 0 6px 20px rgba(248, 200, 59, 0.45) !important;
  transform: translateY(-2px) !important;
}

/* Search and Counter Row */
.gallery-search-row {
  padding: 0.4rem 1.2rem 0.8rem !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
}

.gallery-search-input-box {
  flex: 1 !important;
  position: relative !important;
  display: flex !important;
  align-items: center !important;
}

.gallery-search-icon {
  position: absolute !important;
  left: 14px !important;
  font-size: 1rem !important;
  color: #FDE68A !important;
  pointer-events: none !important;
}

.gallery-search-field {
  width: 100% !important;
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  border-radius: 20px !important;
  padding: 11px 16px 11px 42px !important;
  color: #FFFDF8 !important;
  font-size: 0.9rem !important;
  outline: none !important;
  transition: all 0.2s ease !important;
  box-sizing: border-box !important;
}

.gallery-search-field:focus {
  border-color: #F8C83B !important;
  background: rgba(255, 255, 255, 0.12) !important;
  box-shadow: 0 0 15px rgba(248, 200, 59, 0.35) !important;
}

.gallery-search-field::placeholder {
  color: #94A3B8 !important;
}

.gallery-counter-badge {
  font-size: 0.8rem !important;
  font-weight: 900 !important;
  color: #1A0B2E !important;
  background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 100%) !important;
  border: 1px solid #FEF3C7 !important;
  padding: 10px 16px !important;
  border-radius: 18px !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.35) !important;
}

/* Category Filter Chips */
.gal-cat-chips {
  display: flex !important;
  gap: 8px !important;
  overflow-x: auto !important;
  padding: 0 1.2rem 1.1rem !important;
  scrollbar-width: none !important;
}

.gal-cat-chips::-webkit-scrollbar {
  display: none !important;
}

.gal-cat-chip {
  flex-shrink: 0 !important;
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.18) !important;
  color: #CBD5E1 !important;
  font-size: 0.8rem !important;
  font-weight: 700 !important;
  padding: 6px 14px !important;
  border-radius: 16px !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  white-space: nowrap !important;
}

.gal-cat-chip:hover {
  background: rgba(255, 255, 255, 0.12) !important;
  color: #FFF !important;
  border-color: rgba(248, 200, 59, 0.4) !important;
}

.gal-cat-chip.active {
  background: rgba(248, 200, 59, 0.25) !important;
  border-color: #F8C83B !important;
  color: #FFFDF8 !important;
  font-weight: 800 !important;
  box-shadow: 0 2px 10px rgba(248, 200, 59, 0.3) !important;
}

/* Gallery Cards Grid */
.gallery-cards-grid {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 14px !important;
  padding: 0 1.2rem 2rem !important;
}

@media (max-width: 380px) {
  .gallery-cards-grid {
    grid-template-columns: 1fr !important;
  }
}

.gallery-card-royal, .temple-card-royal {
  background: linear-gradient(145deg, #240C44 0%, #130426 100%) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  border-radius: 22px !important;
  overflow: hidden !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  cursor: pointer !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.gallery-card-royal:hover, .temple-card-royal:hover {
  transform: translateY(-4px) scale(1.01) !important;
  border-color: rgba(248, 200, 59, 0.8) !important;
  box-shadow: 0 14px 35px rgba(248, 200, 59, 0.3) !important;
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + gallery_luxury_css)
print("✓ Appended Royal Vedic Gallery CSS to styles.css")

# 3. Bump cache buster in index.html
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved updated index.html with new cache buster ?v={ts}")

print("=" * 80)
print("GALLERY UI/UX OVERHAUL COMPLETED SUCCESSFULLY")
print("=" * 80)
