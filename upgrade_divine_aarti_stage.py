import sys, re, time, json, sqlite3

sys.stdout.reconfigure(encoding='utf-8')

# 1. Fetch top curated Aarti items across deities from database
conn = sqlite3.connect('db/bhakti.db')
cur = conn.cursor()
cur.execute("""
    SELECT id, deity_id, title, short_description, audio_url, thumbnail 
    FROM content_items 
    WHERE category_id='aarti' OR content_type='aarti' OR title LIKE '%आरती%'
    ORDER BY is_popular DESC, play_count DESC
    LIMIT 60
""")
aarti_db_items = []
for r in cur.fetchall():
    aarti_db_items.append({
        'id': r[0],
        'deity': r[1],
        'title': r[2],
        'desc': r[3] or 'पावन वैदिक नित्य महाआरती',
        'audio': r[4] or 'assets/audio/bhajan_achyutam_keshavam.mp3',
        'thumb': r[5] or 'assets/gallery/bal_ganesha_little.jpg'
    })
conn.close()

print(f"✓ Loaded {len(aarti_db_items)} curated Aarti items from DB")

# 2. Rich Aarti Stage HTML
rich_aarti_stage_html = """    <!-- ═════════════════════════════════════════════════════════════════
         🪔 VIRTUAL DIVINE AARTI & SACRED TEMPLE DARSHAN STAGE 🪔
         ═════════════════════════════════════════════════════════════════ -->
    <section id="page-aarti-stage" class="page">
      
      <!-- Top Royal Navigation Header -->
      <div class="page-header-bar">
        <button class="back-btn" onclick="showPage('page-home')">←</button>
        <h2 style="font-size:1.15rem; font-weight:900; color:#FFFDF8;">🪔 दिव्य आरती व मंदिर दर्शन</h2>
        <button class="katha-search-btn" onclick="triggerFlowerShower()" title="पुष्प वर्षा">🌸</button>
      </div>

      <div style="padding: 0 1.1rem 2rem;">

        <!-- 🌟 INTERACTIVE CENTRAL THALI & TEMPLE DARSHAN HERO STAGE 🌟 -->
        <div style="background: radial-gradient(circle at 50% 20%, #3B1259 0%, #1A052E 65%, #0B0116 100%); border: 1.8px solid #F8C83B; border-radius: 26px; padding: 1.5rem 1.2rem; margin-bottom: 1.4rem; text-align: center; box-shadow: 0 15px 40px rgba(0,0,0,0.8), 0 0 20px rgba(248,200,59,0.18) inset; position: relative; overflow: hidden;">
          
          <!-- Top Live Aarti Tag -->
          <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.18); border:1.2px solid #F8C83B; padding:5px 16px; border-radius:20px; font-size:0.78rem; font-weight:900; color:#FDE68A; margin-bottom:0.8rem;">
            <span>🪔</span> अखंड पावन आरती व दिव्य दीपदान
          </div>

          <!-- Current Selected Deity Name -->
          <h3 id="aarti-current-deity-title" style="color:#FFFDF8; font-size:1.35rem; font-weight:900; margin:0 0 4px 0; letter-spacing:0.4px;">
            ॥ श्री गणेश जी की आरती — जय गणेश देवा ॥
          </h3>
          <p id="aarti-current-deity-sub" style="color:#CBD5E1; font-size:0.8rem; margin:0 0 16px 0;">
            दीप प्रज्वलित करें, घंटी-शंख बजाएं और प्रभु के चरणों में नमन करें
          </p>

          <!-- 3D Glowing Rotating Aarti Thali -->
          <div style="position:relative; width:210px; height:210px; margin:0 auto 16px; display:flex; align-items:center; justify-content:center;">
            
            <!-- Rotating Golden Brass Thali Rim -->
            <div id="aarti-thali-disc" style="width:200px; height:200px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #D97706 50%, #78350F 90%, #451A03 100%); border:4.5px solid #FFFDF8; box-shadow:0 0 45px rgba(248,200,59,0.7), inset 0 0 25px rgba(0,0,0,0.6); display:flex; align-items:center; justify-content:center; animation:spinDisc 25s linear infinite; position:relative;">
              
              <!-- Outer 4 Small Decorative Diyas -->
              <span style="position:absolute; top:8px; font-size:1.1rem; filter:drop-shadow(0 0 6px #F59E0B);">🪔</span>
              <span style="position:absolute; bottom:8px; font-size:1.1rem; filter:drop-shadow(0 0 6px #F59E0B);">🪔</span>
              <span style="position:absolute; left:8px; font-size:1.1rem; filter:drop-shadow(0 0 6px #F59E0B);">🪔</span>
              <span style="position:absolute; right:8px; font-size:1.1rem; filter:drop-shadow(0 0 6px #F59E0B);">🪔</span>

              <!-- Central Deity Image Inside Thali -->
              <div style="width:115px; height:115px; border-radius:50%; border:3px solid #FEF3C7; overflow:hidden; box-shadow:0 0 20px rgba(0,0,0,0.8); background:#1E0738;">
                <img id="aarti-thali-deity-img" src="assets/gallery/bal_ganesha_little.jpg" style="width:100%; height:100%; object-fit:cover;" onerror="this.src='assets/gallery/divya_shiva.jpg'" />
              </div>

              <!-- Grand Central Camphor / Diya Flame -->
              <div id="aarti-central-flame" style="position:absolute; top:calc(50% - 24px); left:calc(50% - 24px); width:48px; height:48px; pointer-events:none; display:flex; align-items:center; justify-content:center; font-size:2.2rem; filter:drop-shadow(0 0 16px #F59E0B); animation:pulseGlow 1.5s infinite;">
                🪔
              </div>
            </div>
          </div>

          <!-- Interactive Temple Instruments & Seva Action Buttons -->
          <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap; margin-bottom:14px;">
            
            <button onclick="ringTempleBell()" style="background:rgba(248,200,59,0.18); border:1.5px solid #F8C83B; color:#FDE68A; font-weight:800; font-size:0.82rem; padding:8px 14px; border-radius:18px; cursor:pointer; display:inline-flex; align-items:center; gap:5px; box-shadow:0 0 10px rgba(248,200,59,0.25);">
              <span>🔔</span> घंटी बजाएं
            </button>
            
            <button onclick="blowTempleConch()" style="background:rgba(236,72,153,0.18); border:1.5px solid #F472B6; color:#FBCFE8; font-weight:800; font-size:0.82rem; padding:8px 14px; border-radius:18px; cursor:pointer; display:inline-flex; align-items:center; gap:5px; box-shadow:0 0 10px rgba(236,72,153,0.25);">
              <span>🐚</span> शंख ध्वनि
            </button>
            
            <button onclick="triggerFlowerShower()" style="background:rgba(16,185,129,0.18); border:1.5px solid #34D399; color:#A7F3D0; font-weight:800; font-size:0.82rem; padding:8px 14px; border-radius:18px; cursor:pointer; display:inline-flex; align-items:center; gap:5px; box-shadow:0 0 10px rgba(16,185,129,0.25);">
              <span>🌸</span> पुष्प वर्षा
            </button>
            
            <button onclick="toggleThaliRotationSpeed()" id="aarti-speed-btn" style="background:rgba(139,92,246,0.18); border:1.5px solid #A78BFA; color:#DDD6FE; font-weight:800; font-size:0.82rem; padding:8px 14px; border-radius:18px; cursor:pointer; display:inline-flex; align-items:center; gap:5px;">
              <span>🔄</span> आरती घुमाएं
            </button>
          </div>

          <!-- Direct Play Aarti / Start 3D Mandir Buttons -->
          <div style="display:flex; flex-direction:column; gap:8px;">
            <button onclick="playCurrentSelectedAarti()" id="aarti-play-now-btn" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; font-weight:900; font-size:0.95rem; padding:11px 0; border-radius:18px; border:none; cursor:pointer; box-shadow:0 4px 18px rgba(248,200,59,0.45); display:flex; align-items:center; justify-content:center; gap:6px;">
              <span>▶</span> पावन महाआरती सुनें
            </button>

            <button onclick="start3DMandirParikramaFlow()" style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); color:#FDE68A; font-weight:800; font-size:0.85rem; padding:10px 0; border-radius:18px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px;">
              <span>🏛️</span> 3D भव्य मंदिर में प्रवेश करें (360° परिक्रमा) ➔
            </button>
          </div>

        </div>

        <!-- 🌺 SELECT DEITY FILTER CHIPS 🌺 -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div style="font-size:0.98rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
            <span>🪔</span> सम्पूर्ण दिव्य आरती संग्रह (60+ महाआरती)
          </div>
        </div>

        <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
          <button onclick="filterAartiCategory('all', this)" class="aarti-cat-pill active" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; white-space:nowrap;">
            ✨ सभी (All)
          </button>
          <button onclick="filterAartiCategory('ganesh', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🌺 श्री गणेश
          </button>
          <button onclick="filterAartiCategory('shiva', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🔱 भगवान शिव
          </button>
          <button onclick="filterAartiCategory('hanuman', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🚩 हनुमान जी
          </button>
          <button onclick="filterAartiCategory('ram', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🏹 श्री राम
          </button>
          <button onclick="filterAartiCategory('krishna', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🪷 श्री कृष्ण
          </button>
          <button onclick="filterAartiCategory('durga', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🌺 माँ दुर्गा
          </button>
          <button onclick="filterAartiCategory('laxmi', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            🪷 माँ लक्ष्मी
          </button>
          <button onclick="filterAartiCategory('vishnu', this)" class="aarti-cat-pill" style="padding:6px 14px; border-radius:14px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">
            ☸️ श्री विष्णु
          </button>
        </div>

        <!-- 📜 DYNAMIC AARTI CARDS CONTAINER 📜 -->
        <div id="aarti-stage-cards-grid" style="display:flex; flex-direction:column; gap:10px;">
          <!-- Rendered dynamically by JavaScript -->
        </div>

      </div>
      <div style="height:6rem"></div>
    </section>"""

# 3. Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_pos = html.find('<!-- 🪔 VIRTUAL AARTI & TEMPLE DARSHAN STAGE 🪔 -->')
if s_pos == -1:
    s_pos = html.find('<section id="page-aarti-stage"')

e_pos = html.find('<!-- ═════════════════════════════════════════════════════════════════\n         🖼️ DIVINE GALLERY', s_pos)
if e_pos == -1:
    e_pos = html.find('<section id="page-gallery"', s_pos)

if s_pos != -1 and e_pos != -1:
    html = html[:s_pos] + rich_aarti_stage_html + "\n\n    " + html[e_pos:]
    print("✓ Successfully upgraded #page-aarti-stage in index.html")
else:
    print("Regex replace for #page-aarti-stage")
    html = re.sub(r'<section id="page-aarti-stage" class="page">[\s\S]*?<\/section>', rich_aarti_stage_html, html)
    print("✓ Replaced via Regex")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 4. Add Dynamic Aarti Stage JavaScript Engine in app.js
aarti_dataset_json = json.dumps(aarti_db_items, ensure_ascii=False)

aarti_stage_js = f"""
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 DYNAMIC VIRTUAL AARTI & TEMPLE DARSHAN STAGE ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.DIVINE_AARTI_DATASET = {aarti_dataset_json};

window.currentSelectedAartiItem = window.DIVINE_AARTI_DATASET[0] || null;
window.isThaliFastRotating = false;

window.renderAartiStageCards = function(filterDeity = 'all') {{
  const grid = document.getElementById('aarti-stage-cards-grid');
  if (!grid) return;

  grid.innerHTML = '';

  const items = window.DIVINE_AARTI_DATASET.filter(item => {{
    if (filterDeity === 'all') return true;
    return item.deity.toLowerCase().includes(filterDeity.toLowerCase()) || 
           item.title.toLowerCase().includes(filterDeity.toLowerCase());
  }});

  if (items.length === 0) {{
    grid.innerHTML = '<div style="text-align:center; padding:2rem; color:#CBD5E1; font-size:0.88rem;">इस श्रेणी में आरती उपलब्ध नहीं है।</div>';
    return;
  }}

  items.forEach(item => {{
    const card = document.createElement('div');
    card.style.cssText = 'background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:20px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.3); transition:all 0.2s ease;';

    card.innerHTML = `
      <div onclick="selectAartiForStage('${{item.id}}')" style="display:flex; align-items:center; gap:12px; flex:1; cursor:pointer;">
        <div style="width:48px; height:48px; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); padding:2px; flex-shrink:0; box-shadow:0 0 12px rgba(248,200,59,0.35);">
          <img src="${{item.thumb}}" style="width:100%; height:100%; border-radius:12px; object-fit:cover;" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" />
        </div>
        <div style="flex:1;">
          <div style="font-size:0.92rem; font-weight:900; color:#FFFDF8; line-height:1.3;">
            ${{item.title}}
          </div>
          <div style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-top:2px;">
            ${{item.desc}}
          </div>
        </div>
      </div>

      <div style="display:flex; align-items:center; gap:6px;">
        <button onclick="playAartiItemDirect('${{item.id}}')" title="आरती सुनें" style="width:38px; height:38px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; font-size:1rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 12px rgba(248,200,59,0.4);">
          ▶
        </button>
        <button onclick="openAartiReader('${{item.id}}')" title="आरती पढ़ें" style="width:38px; height:38px; border-radius:50%; background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          📖
        </button>
      </div>
    `;

    grid.appendChild(card);
  }});
}};

window.selectAartiForStage = function(aartiId) {{
  const item = window.DIVINE_AARTI_DATASET.find(x => x.id === aartiId);
  if (!item) return;

  window.currentSelectedAartiItem = item;

  const titleEl = document.getElementById('aarti-current-deity-title');
  const subEl = document.getElementById('aarti-current-deity-sub');
  const imgEl = document.getElementById('aarti-thali-deity-img');

  if (titleEl) titleEl.textContent = `॥ ${{item.title}} ॥`;
  if (subEl) subEl.textContent = `${{item.desc}} — दीपदान व नमन करें`;
  if (imgEl) imgEl.src = item.thumb;

  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof showToast === 'function') showToast(`🪔 ${{item.title}} थाली में स्थापित!`);
}};

window.playCurrentSelectedAarti = function() {{
  if (!window.currentSelectedAartiItem) {{
    window.currentSelectedAartiItem = window.DIVINE_AARTI_DATASET[0];
  }}
  if (window.currentSelectedAartiItem) {{
    window.playAartiItemDirect(window.currentSelectedAartiItem.id);
  }}
}};

window.playAartiItemDirect = function(aartiId) {{
  const item = window.DIVINE_AARTI_DATASET.find(x => x.id === aartiId);
  if (!item) return;

  window.selectAartiForStage(aartiId);

  // Play audio using global audio player
  if (typeof window.playTrack === 'function') {{
    window.playTrack({{
      id: item.id,
      title: item.title,
      deity: item.deity,
      sub: item.desc,
      img: item.thumb,
      src: item.audio
    }});
  }} else {{
    if (!window.aartiAudioObj) window.aartiAudioObj = new Audio();
    window.aartiAudioObj.src = item.audio;
    window.aartiAudioObj.play().catch(() => {{}});
  }}

  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');

  if (typeof showToast === 'function') {{
    showToast(`🪔 पावन आरती गायन: ${{item.title}}`);
  }}
}};

window.filterAartiCategory = function(catKey, btnEl) {{
  document.querySelectorAll('.aarti-cat-pill').forEach(b => {{
    b.classList.remove('active');
    b.style.background = 'rgba(255,255,255,0.08)';
    b.style.color = '#CBD5E1';
    b.style.border = '1px solid rgba(255,255,255,0.15)';
  }});

  if (btnEl) {{
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
  }}

  window.renderAartiStageCards(catKey);
}};

window.toggleThaliRotationSpeed = function() {{
  const thali = document.getElementById('aarti-thali-disc');
  const btn = document.getElementById('aarti-speed-btn');
  if (!thali) return;

  window.isThaliFastRotating = !window.isThaliFastRotating;

  if (window.isThaliFastRotating) {{
    thali.style.animation = 'spinDisc 6s linear infinite';
    if (btn) btn.innerHTML = '<span>⚡</span> तीव्र आरती';
    if (typeof showToast === 'function') showToast('⚡ महाआरती परिक्रमा तीव्र हुई!');
  }} else {{
    thali.style.animation = 'spinDisc 25s linear infinite';
    if (btn) btn.innerHTML = '<span>🔄</span> आरती घुमाएं';
    if (typeof showToast === 'function') showToast('🔄 सामान्य आरती परिक्रमा गति');
  }}

  if (navigator.vibrate) navigator.vibrate(30);
}};

// Initialize Aarti Stage Cards when page loads
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => window.renderAartiStageCards('all'));
}} else {{
  window.renderAartiStageCards('all');
}}
"""

with open('app.js', 'r', encoding='utf-8') as f:
    cur_js = f.read()

# Replace or append in app.js
if 'DYNAMIC VIRTUAL AARTI & TEMPLE DARSHAN STAGE ENGINE' not in cur_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(aarti_stage_js)
    print("✓ Added Dynamic Aarti Stage Engine to app.js")
else:
    s_block = cur_js.find('// 🪔 DYNAMIC VIRTUAL AARTI')
    cur_js = cur_js[:s_block] + aarti_stage_js
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(cur_js)
    print("✓ Updated Dynamic Aarti Stage Engine in app.js")

print(f"✓ Aarti Stage fully synchronized and live (v={ts})")
