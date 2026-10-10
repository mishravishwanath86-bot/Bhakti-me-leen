import shutil, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# Backup index.html and app.js
shutil.copyfile('index.html', 'index.html.bak')
shutil.copyfile('app.js', 'app.js.bak')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 1. Generate the Home page Chalisa grid HTML
from generate_home_chalisa_grid import full_grid_html

home_chalisa_widget = f'''
      <!-- 📜 NITYA CHALISA COLLECTION PREVIEW (18 DEITY POINTS) 📜 -->
      <div style="margin: 0 1.2rem 1.4rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.8rem;">
          <h2 style="font-size:1.1rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.35rem; filter:drop-shadow(0 0 8px #F59E0B);">📜</span>
            <span>नित्य पावन चालीसा संग्रह</span>
          </h2>
          <button class="see-all-toggle-btn" onclick="showPage('page-chalisa'); if(window.renderFullDrikChalisaPage) window.renderFullDrikChalisaPage('all', '');" style="background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; border:none; font-size:0.78rem; font-weight:900; padding:6px 14px; border-radius:14px; cursor:pointer; box-shadow:0 2px 10px rgba(248,200,59,0.35); display:flex; align-items:center; gap:4px;">सभी देखें (18 देव • 54 चालीसा) ❯</button>
        </div>

        <!-- 18-Deity Point-wise Preview Grid -->
        <div class="aarti-preview-grid" id="home-nitya-chalisa-grid">
{full_grid_html}
        </div>
      </div>
'''

# Insert home_chalisa_widget right after Nitya Aarti Collection Preview in index.html
# Look for: <!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->
banner_marker = '<!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->'
banner_idx = html.find(banner_marker)
if banner_idx == -1:
    print("ERROR: banner_marker not found in index.html")
    sys.exit(1)

html = html[:banner_idx] + home_chalisa_widget + "\n      " + html[banner_idx:]
print("Added home_chalisa_widget to index.html successfully!")

# 2. Add chalisa-options-modal right after aarti-options-modal in index.html
modal_end_marker = 'id="aarti-options-modal"'
m_idx = html.find(modal_end_marker)
# find closing </div> of aarti-options-modal
m_close_idx = html.find('</div>\n  </div>', m_idx)
if m_close_idx == -1:
    print("ERROR: could not find aarti modal close")
    sys.exit(1)

m_insert_pos = m_close_idx + len('</div>\n  </div>')

chalisa_modal_html = '''

  <!-- ══════════════════════════════════════════════════════════════════════════════
       📜 DEDICATED CHALISA COLLECTION MODAL (IMAGE 1 EXACT DRIK EXPERIENCE)
       ══════════════════════════════════════════════════════════════════════════════ -->
  <div id="chalisa-options-modal" class="aarti-options-modal" style="display:none;" onclick="if(event.target === this && typeof window.closeChalisaOptionsModal === 'function') window.closeChalisaOptionsModal();">
    <div class="aarti-modal-content">
      
      <!-- Top Bar -->
      <div class="glass-player-topbar" style="margin-bottom:1rem;">
        <button class="glass-topbar-btn" onclick="if(typeof window.closeChalisaOptionsModal === 'function') window.closeChalisaOptionsModal();" title="बंद करें / मुख्य पृष्ठ">✕</button>
        <div id="chalisa-modal-title" style="font-size:1.05rem; font-weight:900; color:#FDE68A;">॥ चालीसा संग्रह ॥</div>
        <button class="glass-topbar-btn" onclick="triggerFlowerShower()">🌸</button>
      </div>

      <!-- Deity Header Card -->
      <div style="background:linear-gradient(135deg, #1F0738 0%, #3B1259 50%, #150628 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:22px; padding:1.2rem; margin-bottom:1.2rem; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.5);">
        <img id="chalisa-modal-img" src="assets/gallery/bal_hanuman.jpg" style="width:75px; height:75px; border-radius:50%; object-fit:cover; border:2.5px solid #F8C83B; margin-bottom:8px; box-shadow:0 0 15px rgba(248,200,59,0.4);" alt="Deity" />
        <div id="chalisa-modal-deity" style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin-bottom:4px;">श्री हनुमान जी</div>
        <div id="chalisa-modal-mantra" style="font-size:0.8rem; color:#FDE68A; font-weight:700;">॥ ॐ हं हनुमते नमः ॥</div>
      </div>

      <!-- Dynamic Items Container with Switch Pills -->
      <div id="chalisa-modal-list"></div>

    </div>
  </div>'''

html = html[:m_insert_pos] + chalisa_modal_html + html[m_insert_pos:]
print("Added chalisa-options-modal to index.html successfully!")

# 3. Upgrade page-chalisa in index.html
old_page_chalisa = '''<section id="page-chalisa" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>चालीसा</h2>
      </div>
      <div class="deity-grid" id="chalisa-deity-grid"></div>
    </section>'''

new_page_chalisa = '''<section id="page-chalisa" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>चालीसा संग्रह</h2>
        <span style="font-size:0.75rem; background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; padding:3px 10px; border-radius:12px; font-weight:900;">54 चालीसा</span>
      </div>

      <!-- Search & Category Filters -->
      <div style="padding: 0 1.2rem 0.8rem;">
        <div style="position:relative; margin-bottom:0.8rem;">
          <input type="text" id="drik-chalisa-search-input" placeholder="🔍 चालीसा अथवा देव नाम खोजें..." oninput="window.renderFullDrikChalisaPage(window._drikChalisaCurrentFilter, this.value)" style="width:100%; background:rgba(255,255,255,0.06); border:1.5px solid rgba(248,200,59,0.3); border-radius:16px; padding:10px 14px 10px 38px; color:#FFFDF8; font-size:0.9rem; outline:none; box-sizing:border-box;" />
          <span style="position:absolute; left:12px; top:50%; transform:translateY(-50%); font-size:1rem; opacity:0.6;">🔍</span>
        </div>
        
        <div id="drik-chalisa-page-pills" style="display:flex; gap:6px; overflow-x:auto; padding-bottom:4px; scrollbar-width:none;"></div>
      </div>

      <!-- Dynamic Cards Container -->
      <div id="drik-chalisa-cards-container" style="padding: 0 1.2rem 1.5rem; display:flex; flex-direction:column; gap:12px;"></div>
    </section>'''

if old_page_chalisa in html:
    html = html.replace(old_page_chalisa, new_page_chalisa)
    print("Upgraded page-chalisa in index.html successfully!")
else:
    print("Warning: old_page_chalisa not directly matched, trying regex")
    html = re.sub(r'<section id="page-chalisa"[^>]*>.*?</section>', new_page_chalisa, html, flags=re.DOTALL)
    print("Upgraded page-chalisa via regex!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved index.html successfully!")

# 4. Integrate chalisa_engine.js into app.js
with open('chalisa_engine.js', encoding='utf-8') as f:
    chalisa_engine_code = f.read()

with open('app.js', encoding='utf-8') as f:
    app_js = f.read()

# Add call in switchPage for page-chalisa:
old_switch_target = "if(id === 'page-aarti' && typeof window.renderFullDrikAartiPage === 'function') {"
new_switch_target = """if(id === 'page-chalisa' && typeof window.renderFullDrikChalisaPage === 'function') {
    window.renderFullDrikChalisaPage('all', '');
  }

  if(id === 'page-aarti' && typeof window.renderFullDrikAartiPage === 'function') {"""

if old_switch_target in app_js:
    app_js = app_js.replace(old_switch_target, new_switch_target, 1)
    print("Added switchPage handler for page-chalisa!")

# Append chalisa_engine_code to app.js
app_js += "\n\n" + chalisa_engine_code

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Saved app.js successfully!")
