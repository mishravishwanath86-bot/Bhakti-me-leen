import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

json_str = json.dumps(chalisa_data, ensure_ascii=False, indent=2)

js_template = """
// ══════════════════════════════════════════════════════════════════════════════
// 📜 DRIK PANCHANG COMPLETE CHALISA ENGINE (54 CHALISAS POINT-WISE SET)
// ══════════════════════════════════════════════════════════════════════════════

window.CHALISA_COLLECTIONS = __JSON_DATA__;

// 1. Render Chalisa Card HTML (Matching Image 1 Aarti Style)
window.renderDrikChalisaCardHtml = function(item, catKey, coll, idx) {
  const thumb = item.thumb || coll.img || 'assets/gallery/bal_ganesha_little.jpg';
  const fallback = coll.fallbackImg || 'assets/deity_ganesh.jpg';
  
  return `
    <div class="drik-image1-card" onclick="window.readChalisaItemDirect('${catKey}', ${idx})">
      <img src="${thumb}" onerror="this.src='${fallback}';" alt="${item.title}" class="drik-card-thumb" />
      <div style="flex:1; min-width:0;">
        <div class="drik-card-title-en" title="${item.title}">${item.title}</div>
        <div class="drik-card-sub-en" title="${item.en_line}">${item.en_line}</div>
        <div class="drik-card-title-hi" onclick="event.stopPropagation(); window.readChalisaItemDirect('${catKey}', ${idx})" title="${item.hi_line}">${item.hi_line}</div>
        <div style="display:flex; align-items:center; gap:8px;">
          ${item.audio_url ? `
          <button class="drik-card-play-btn" onclick="event.stopPropagation(); window.playChalisaItemDirect('${catKey}', ${idx})" title="चालीसा सुनें">
            <span>▶</span> चालीसा सुनें
          </button>` : ''}
          <button class="drik-card-read-btn" onclick="event.stopPropagation(); window.readChalisaItemDirect('${catKey}', ${idx})" title="पाठ व भावार्थ पढ़ें">
            <span>📖</span> पाठ पढ़ें
          </button>
        </div>
      </div>
    </div>
  `;
};

// 2. Updated Chalisa Collection Modal Controller
window._chalisaActiveModalDeity = null;
window._chalisaOriginPage = 'page-home';

window.openChalisaCollectionModal = function(deityKey) {
  const coll = window.CHALISA_COLLECTIONS ? window.CHALISA_COLLECTIONS[deityKey] : null;
  if (!coll) {
    console.warn('Chalisa collection not found:', deityKey);
    return;
  }

  window._chalisaActiveModalDeity = deityKey;
  const activeOrigin = (window.currentPage && window.currentPage !== 'page-reader') 
    ? window.currentPage 
    : ((typeof currentPage !== 'undefined' && currentPage !== 'page-reader') ? currentPage : 'page-home');
  window._chalisaOriginPage = activeOrigin;

  const modal = document.getElementById('chalisa-options-modal');
  if (!modal) return;

  const titleEl = document.getElementById('chalisa-modal-title');
  const deityEl = document.getElementById('chalisa-modal-deity');
  const mantraEl = document.getElementById('chalisa-modal-mantra');
  const imgEl = document.getElementById('chalisa-modal-img');
  const listContainer = document.getElementById('chalisa-modal-list');

  if (titleEl) titleEl.textContent = `${coll.title_en || coll.title} | ${coll.title}`;
  if (deityEl) deityEl.textContent = coll.deity;
  if (mantraEl) mantraEl.textContent = coll.mantra;
  
  if (imgEl) {
    imgEl.src = coll.img;
    imgEl.onerror = function() { this.src = coll.fallbackImg; };
  }

  // Deity quick switch pills inside modal
  const deitiesList = [
    ['hanuman', 'हनुमान'], ['ganesh', 'गणेश'], ['shiva', 'शिव'], ['krishna', 'कृष्ण'],
    ['rama', 'राम'], ['durga', 'दुर्गा'], ['lakshmi', 'लक्ष्मी'], ['saraswati', 'सरस्वती'],
    ['surya', 'सूर्य'], ['shani', 'शनि'], ['khatushyam', 'श्याम'], ['ganga', 'गंगा'],
    ['bhairav', 'भैरव'], ['gayatri', 'गायत्री'], ['radha', 'राधा'], ['vishnu', 'विष्णु'],
    ['devi', 'देवी माँ'], ['sants', 'सन्त-गीता']
  ];

  const switchPillsHtml = `
    <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
      ${deitiesList.map(([k, label]) => `
        <button onclick="window.openChalisaCollectionModal('${k}')" style="padding:4px 10px; border-radius:12px; border:1px solid rgba(248,200,59,0.3); font-size:0.75rem; font-weight:800; cursor:pointer; white-space:nowrap; background:${k === deityKey ? 'linear-gradient(135deg, #F8C83B, #D97706)' : 'rgba(255,255,255,0.06)'}; color:${k === deityKey ? '#1A0B2E' : '#FDE68A'};">
          ${label}
        </button>
      `).join('')}
    </div>
  `;

  if (listContainer) {
    listContainer.innerHTML = switchPillsHtml + `
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px;">
        ${coll.items.map((item, idx) => window.renderDrikChalisaCardHtml(item, deityKey, coll, idx)).join('')}
      </div>
    `;
  }

  modal.classList.remove('hidden');
  modal.classList.add('active');
  modal.style.display = 'flex';
  modal.style.opacity = '1';
  modal.style.pointerEvents = 'auto';

  if (navigator.vibrate) navigator.vibrate(30);
};

window.closeChalisaOptionsModal = function() {
  const modal = document.getElementById('chalisa-options-modal');
  if (modal) {
    modal.classList.remove('active');
    modal.classList.add('hidden');
    modal.style.display = 'none';
    modal.style.opacity = '0';
    modal.style.pointerEvents = 'none';
  }
};

// Direct item reader
window.readChalisaItemDirect = function(deityKey, idx) {
  const coll = window.CHALISA_COLLECTIONS ? window.CHALISA_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) return;

  const item = coll.items[idx];
  window.closeChalisaOptionsModal();

  const readerObj = {
    title: item.title,
    deity: coll.deity,
    mantra: coll.mantra,
    text: item.content,
    meaning: item.meaning,
    audio_url: item.audio_url,
    video_id: item.video_id,
    thumb: item.thumb || coll.img,
    img: coll.img,
    source: item.source || 'Drik Panchang Verified',
    drik_url: item.drik_url
  };

  if (typeof openReader === 'function') {
    openReader(readerObj, 'page-chalisa');
  }
};

// Direct audio/video player
window.playChalisaItemDirect = function(deityKey, idx) {
  const coll = window.CHALISA_COLLECTIONS ? window.CHALISA_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) return;

  const item = coll.items[idx];
  if (item.video_id && typeof playYouTubeAudio === 'function') {
    playYouTubeAudio(item.video_id, item.title, coll.deity);
  } else if (item.audio_url && typeof playAudioUrl === 'function') {
    playAudioUrl(item.audio_url, item.title, coll.deity);
  } else {
    window.readChalisaItemDirect(deityKey, idx);
  }
};

// 3. Render Full DrikPanchang Chalisa Page (page-chalisa)
window._drikChalisaCurrentFilter = 'all';
window._drikChalisaCurrentSearch = '';

window.renderFullDrikChalisaPage = function(filterCategory, searchQuery) {
  if (filterCategory !== undefined) window._drikChalisaCurrentFilter = filterCategory;
  if (searchQuery !== undefined) window._drikChalisaCurrentSearch = searchQuery.toLowerCase().trim();

  const container = document.getElementById('drik-chalisa-cards-container');
  const pillsContainer = document.getElementById('drik-chalisa-page-pills');
  if (!container) return;

  const categories = [
    ['all', '✨ सभी (54)'],
    ['devtas', '🔱 देवताओं की चालीसा (22)'],
    ['devis', '🌸 देवियों की चालीसा (21)'],
    ['sants', '🧘‍♂️ सन्तों की चालीसा (9)'],
    ['other', '📜 अन्य चालीसा (2)']
  ];

  if (pillsContainer && pillsContainer.children.length === 0) {
    pillsContainer.innerHTML = categories.map(([k, label]) => `
      <button class="drik-page-chip ${k === window._drikChalisaCurrentFilter ? 'active' : ''}" data-cat="${k}" onclick="window.renderFullDrikChalisaPage('${k}', window._drikChalisaCurrentSearch)">
        ${label}
      </button>
    `).join('');
  } else if (pillsContainer) {
    pillsContainer.querySelectorAll('.drik-page-chip').forEach(btn => {
      if (btn.getAttribute('data-cat') === window._drikChalisaCurrentFilter) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  let html = '';
  const search = window._drikChalisaCurrentSearch;
  const filter = window._drikChalisaCurrentFilter;

  // Iterate over all collections and group/filter
  Object.keys(window.CHALISA_COLLECTIONS).forEach(catKey => {
    const coll = window.CHALISA_COLLECTIONS[catKey];
    if (!coll) return;

    let items = coll.items;
    
    // Filter by section
    if (filter === 'devtas') {
      items = items.filter(i => i.section === 'देवताओं की चालीसा');
    } else if (filter === 'devis') {
      items = items.filter(i => i.section === 'देवियों की चालीसा');
    } else if (filter === 'sants') {
      items = items.filter(i => i.section === 'सन्तों की चालीसा');
    } else if (filter === 'other') {
      items = items.filter(i => i.section === 'अन्य चालीसा');
    }

    // Filter by search
    if (search) {
      items = items.filter(i => 
        i.title.toLowerCase().includes(search) || 
        i.en_line.toLowerCase().includes(search) || 
        i.hi_line.includes(search) ||
        coll.title.includes(search) ||
        coll.deity.includes(search)
      );
    }

    if (items.length === 0) return;

    html += `
      <div class="drik-category-block" style="margin-bottom:1.2rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px; border-bottom:1px solid rgba(248,200,59,0.2); padding-bottom:4px;">
          <div style="font-size:0.95rem; font-weight:900; color:#FDE68A; display:flex; align-items:center; gap:6px;">
            <span>🪔</span> ${coll.title}
          </div>
          <span style="font-size:0.75rem; color:#CBD5E1; background:rgba(255,255,255,0.08); padding:2px 8px; border-radius:10px;">
            ${items.length} चालीसा
          </span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:10px;">
          ${items.map(item => {
            const realIdx = coll.items.findIndex(it => it.id === item.id);
            return window.renderDrikChalisaCardHtml(item, catKey, coll, realIdx >= 0 ? realIdx : 0);
          }).join('')}
        </div>
      </div>
    `;
  });

  if (!html) {
    container.innerHTML = `
      <div style="text-align:center; padding:3rem 1rem; color:#94A3B8;">
        <div style="font-size:2.5rem; margin-bottom:10px;">🔍</div>
        <div style="font-size:1.1rem; font-weight:700; color:#FFFDF8;">कोई चालीसा नहीं मिली</div>
        <div style="font-size:0.85rem; margin-top:4px;">कृपया अन्य शब्द लिखकर खोजें</div>
      </div>
    `;
  } else {
    container.innerHTML = html;
  }
};
"""

final_js = js_template.replace("__JSON_DATA__", json_str)

with open('chalisa_engine.js', 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Generated chalisa_engine.js successfully!")
