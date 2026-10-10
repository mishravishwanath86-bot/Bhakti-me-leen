import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    colls = json.load(f)

json_str = json.dumps(colls, ensure_ascii=False, indent=2)

addon_code = f"""
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 DRIK PANCHANG COMPLETE AARTI ENGINE (EXACT IMAGE 1 REPLICA & ALL DEITY POINTS)
// ══════════════════════════════════════════════════════════════════════════════

window.AARTI_COLLECTIONS = {json_str};

// 1. Image 1 Card HTML Generator
window.renderDrikImage1CardHtml = function(item, catKey, coll, idx) {{
  const thumb = item.thumb || coll.img || 'assets/gallery/bal_krishna_little.jpg';
  const fallback = coll.fallbackImg || 'assets/deity_krishna.jpg';
  return `
    <div class="drik-image1-card" onclick="window.readAartiItemDirect('${{catKey}}', ${{idx}})">
      <img src="${{thumb}}" onerror="this.src='${{fallback}}';" alt="${{item.title}}" class="drik-card-thumb" />
      <div style="flex:1; min-width:0;">
        <div class="drik-card-title-en" title="${{item.title}}">${{item.title}}</div>
        <div class="drik-card-sub-en" title="${{item.en_line}}">${{item.en_line}}</div>
        <div class="drik-card-title-hi" onclick="event.stopPropagation(); window.readAartiItemDirect('${{catKey}}', ${{idx}})" title="${{item.hi_line}}">${{item.hi_line}}</div>
        <div style="display:flex; align-items:center; gap:8px;">
          <button class="drik-card-play-btn" onclick="event.stopPropagation(); window.playAartiItemDirect('${{catKey}}', ${{idx}})" title="आरती सुनें">
            <span>▶</span> आरती सुनें
          </button>
          <button class="drik-card-read-btn" onclick="event.stopPropagation(); window.readAartiItemDirect('${{catKey}}', ${{idx}})" title="पाठ व भावार्थ पढ़ें">
            <span>📖</span> पाठ पढ़ें
          </button>
        </div>
      </div>
    </div>
  `;
}};

// 2. Updated Aarti Collection Modal Controller
window.openAartiCollectionModal = function(deityKey) {{
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll) {{
    console.warn('Aarti collection not found:', deityKey);
    return;
  }}

  const modal = document.getElementById('aarti-options-modal');
  if (!modal) return;

  const titleEl = document.getElementById('aarti-modal-title');
  const deityEl = document.getElementById('aarti-modal-deity');
  const mantraEl = document.getElementById('aarti-modal-mantra');
  const imgEl = document.getElementById('aarti-modal-img');
  const listContainer = document.getElementById('aarti-modal-list');

  if (titleEl) titleEl.textContent = `${{coll.title_en || coll.title}} | ${{coll.title}}`;
  if (deityEl) deityEl.textContent = coll.deity;
  if (mantraEl) mantraEl.textContent = coll.mantra;
  
  if (imgEl) {{
    imgEl.src = coll.img;
    imgEl.onerror = function() {{ this.src = coll.fallbackImg; }};
  }}

  // Deity quick switch pills inside modal
  const deitiesList = [
    ['ganesh', 'गणेश'], ['hanuman', 'हनुमान'], ['krishna', 'कृष्ण'], ['rama', 'राम'],
    ['shiva', 'शिव'], ['narayana', 'नारायण'], ['durga', 'दुर्गा'], ['lakshmi', 'लक्ष्मी'],
    ['saraswati', 'सरस्वती'], ['surya', 'सूर्य'], ['shanidev', 'शनि'], ['khatushyam', 'श्याम'],
    ['ganga', 'गंगा'], ['bhairav', 'भैरव'], ['gayatri', 'गायत्री'], ['sants', 'सन्त'], ['gita', 'गीता']
  ];

  const switchPillsHtml = `
    <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
      ${{deitiesList.map(([k, label]) => `
        <button onclick="window.openAartiCollectionModal('${{k}}')" style="padding:4px 10px; border-radius:12px; font-size:0.72rem; white-space:nowrap; cursor:pointer; ${{k === deityKey ? 'background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; border:none;' : 'background:rgba(255,255,255,0.08); color:#FDE68A; border:1px solid rgba(248,200,59,0.3);'}}">
          ${{label}}
        </button>
      `).join('')}}
    </div>
  `;

  if (listContainer) {{
    listContainer.innerHTML = switchPillsHtml + `
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px;">
        ${{coll.items.map((item, idx) => window.renderDrikImage1CardHtml(item, deityKey, coll, idx)).join('')}}
      </div>
    `;
  }}

  modal.classList.remove('hidden');
  modal.classList.add('active');
  modal.style.display = 'flex';
  modal.style.opacity = '1';
  modal.style.pointerEvents = 'auto';

  if (navigator.vibrate) navigator.vibrate(30);
}};

// 3. Home Page Aarti Deities Filter Pills
window.filterHomeAartiDeities = function(catKey) {{
  const pills = document.querySelectorAll('.home-aarti-filter-chip');
  pills.forEach(p => {{
    if (p.getAttribute('data-cat') === catKey) {{
      p.classList.add('active');
      p.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      p.style.color = '#1A0B2E';
      p.style.fontWeight = '900';
      p.style.border = 'none';
    }} else {{
      p.classList.remove('active');
      p.style.background = 'rgba(255,255,255,0.06)';
      p.style.color = '#FDE68A';
      p.style.fontWeight = '700';
      p.style.border = '1px solid rgba(248,200,59,0.25)';
    }}
  }});

  const cards = document.querySelectorAll('.home-aarti-card');
  cards.forEach(c => {{
    if (catKey === 'all' || c.getAttribute('data-cat') === catKey) {{
      c.style.display = 'block';
    }} else {{
      c.style.display = 'none';
    }}
  }});
}};

// 4. Render Complete DrikPanchang Aarti Page (page-aarti)
window._drikCurrentFilter = 'all';
window._drikCurrentSearch = '';

window.renderFullDrikAartiPage = function(filterCategory, searchQuery) {{
  if (filterCategory !== undefined) window._drikCurrentFilter = filterCategory;
  if (searchQuery !== undefined) window._drikCurrentSearch = searchQuery.toLowerCase().trim();

  const container = document.getElementById('drik-aarti-cards-container');
  const pillsContainer = document.getElementById('drik-aarti-page-pills');
  if (!container) return;

  const categories = [
    ['all', '✨ सभी (86)'],
    ['krishna', '🪷 श्री कृष्ण (7)'],
    ['rama', '🏹 श्री राम (6)'],
    ['shiva', '🔱 भगवान शिव (5)'],
    ['ganesh', '🌺 श्री गणेश (3)'],
    ['hanuman', '🚩 श्री हनुमान (3)'],
    ['narayana', '☸️ श्री नारायण (5)'],
    ['durga', '🌸 माँ दुर्गा (5)'],
    ['lakshmi', '🪷 माँ लक्ष्मी (4)'],
    ['saraswati', '🦢 माँ सरस्वती (2)'],
    ['surya', '☀️ श्री सूर्य (3)'],
    ['shanidev', '⚖️ शनिदेव (1)'],
    ['khatushyam', '🦚 खाटू श्याम (1)'],
    ['ganga', '🌊 माँ गंगा (4)'],
    ['bhairav', '🔱 भैरव बाबा (2)'],
    ['gayatri', '🌿 गायत्री व तुलसी (4)'],
    ['radha', '🌸 राधा रानी (2)'],
    ['sants', '🧘‍♂️ सन्त व गुरु (9)'],
    ['gita', '📜 रामायण व गीता (9)']
  ];

  // Render pills if needed
  if (pillsContainer && pillsContainer.children.length === 0) {{
    pillsContainer.innerHTML = categories.map(([k, label]) => `
      <button class="drik-page-chip ${{k === window._drikCurrentFilter ? 'active' : ''}}" data-cat="${{k}}" onclick="window.renderFullDrikAartiPage('${{k}}', window._drikCurrentSearch)">
        ${{label}}
      </button>
    `).join('');
  }} else if (pillsContainer) {{
    pillsContainer.querySelectorAll('.drik-page-chip').forEach(btn => {{
      if (btn.getAttribute('data-cat') === window._drikCurrentFilter) {{
        btn.classList.add('active');
      }} else {{
        btn.classList.remove('active');
      }}
    }});
  }}

  let html = '';
  const search = window._drikCurrentSearch;
  const filter = window._drikCurrentFilter;

  // Filter categories to show
  const catsToShow = filter === 'all' 
    ? Object.keys(window.AARTI_COLLECTIONS).filter(k => k !== 'gods' && k !== 'goddesses')
    : [filter];

  let totalMatched = 0;

  catsToShow.forEach(catKey => {{
    const coll = window.AARTI_COLLECTIONS[catKey];
    if (!coll) return;

    let items = coll.items;
    if (search) {{
      items = items.filter(i => 
        i.title.toLowerCase().includes(search) || 
        i.en_line.toLowerCase().includes(search) || 
        i.hi_line.includes(search) ||
        coll.title.includes(search)
      );
    }}

    if (items.length === 0) return;
    totalMatched += items.length;

    html += `
      <div style="margin-bottom:1.6rem;">
        <!-- Category Section Header (Image 1 Theme) -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.75rem; border-bottom:1.5px solid rgba(248,200,59,0.3); padding-bottom:6px;">
          <div style="display:flex; align-items:center; gap:10px;">
            <img src="${{coll.img}}" onerror="this.src='${{coll.fallbackImg}}';" style="width:36px; height:36px; border-radius:50%; object-fit:cover; border:1.5px solid #F8C83B;" />
            <div>
              <div style="font-weight:900; font-size:1.05rem; color:#FDE68A;">${{coll.title_en || coll.title}}</div>
              <div style="font-size:0.75rem; color:#FBCFE8;">${{coll.title}} • ${{coll.mantra}}</div>
            </div>
          </div>
          <span style="font-size:0.72rem; color:#F8C83B; background:rgba(248,200,59,0.15); padding:2px 8px; border-radius:10px; font-weight:800;">${{items.length}} आरतियां</span>
        </div>

        <!-- 2-Column Responsive Image 1 Cards Grid -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px;">
          ${{items.map((item, idx) => window.renderDrikImage1CardHtml(item, catKey, coll, idx)).join('')}}
        </div>
      </div>
    `;
  }});

  if (totalMatched === 0) {{
    html = `
      <div style="text-align:center; padding:3rem 1rem; color:#FDE68A;">
        <div style="font-size:2.5rem; margin-bottom:10px;">🔍</div>
        <div style="font-size:1.1rem; font-weight:800;">कोई आरती नहीं मिली</div>
        <div style="font-size:0.85rem; color:#FBCFE8; margin-top:4px;">कृपया कोई अन्य नाम लिखकर खोजें (उदा. ओंकारा, कुंजबिहारी, जय गणेश)</div>
      </div>
    `;
  }}

  container.innerHTML = html;
}};

// 5. Real-time Search Handler
window._drikSearchTimeout = null;
window.handleDrikAartiSearch = function(val) {{
  clearTimeout(window._drikSearchTimeout);
  window._drikSearchTimeout = setTimeout(() => {{
    window.renderFullDrikAartiPage(undefined, val);
  }}, 200);
}};

// 6. Navigation Interceptor to Auto-Load page-aarti
if (window.showPage) {{
  const origShowPage = window.showPage;
  window.showPage = function(pageId) {{
    origShowPage(pageId);
    if (pageId === 'page-aarti') {{
      window.renderFullDrikAartiPage('all', '');
    }}
  }};
}}
"""

with open('drik_app_addon.js', 'w', encoding='utf-8') as f:
    f.write(addon_code)

print(f"✓ Generated drik_app_addon.js ({len(addon_code)} bytes)")
