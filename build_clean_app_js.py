import json
import re
import sys

# 1. Load the full base app.js from the clean 26k line backup
with open('app.js.bak_aarti_ui_1789877632', 'r', encoding='utf-8') as f:
    js = f.read()

print(f"Loaded base backup app.js: {len(js)} bytes, {js.count(chr(10))} lines")

# 2. Ensure HINDU_VRATS is exposed
if "window.HINDU_VRATS = HINDU_VRATS;" not in js:
    js = js.replace("const HINDU_VRATS = [", "const HINDU_VRATS = [\n", 1)
    # Find closing of HINDU_VRATS = [...]
    v_start = js.find("const HINDU_VRATS = [")
    v_end = js.find("];", v_start) + 2
    js = js[:v_end] + "\nwindow.HINDU_VRATS = HINDU_VRATS;\n" + js[v_end:]
    print("Exposed window.HINDU_VRATS")

# 3. Ensure initVratAllPage is present
if "function initVratAllPage()" not in js:
    vrat_all_code = '''
// ══════════════════════════════════════════════════════════════════════════════
// 🕉️ HINDU VRATS ALL PAGE CONTROLLER (IMAGE 2 FULL PAGE)
// ══════════════════════════════════════════════════════════════════════════════
window._vratCurrentFilter = 'all';

window.initVratAllPage = function(filterCategory) {
  if (filterCategory !== undefined) window._vratCurrentFilter = filterCategory;
  const container = document.getElementById('vrats-all-cards-container');
  const tabsContainer = document.getElementById('vrats-all-filter-tabs');
  const countBadge = document.getElementById('vrats-all-count-badge');
  if (!container) return;

  const allVrats = window.HINDU_VRATS || [];
  
  const categories = [
    ['all', `✨ सभी (${allVrats.length})`],
    ['monthly', '🌙 मासिक व्रत'],
    ['quarterly', '⭐ पावन उपवास'],
    ['special', '🔱 विशेष साधना']
  ];

  if (tabsContainer && tabsContainer.children.length === 0) {
    tabsContainer.innerHTML = categories.map(([k, label]) => `
      <button class="drik-page-chip ${k === window._vratCurrentFilter ? 'active' : ''}" data-cat="${k}" onclick="window.initVratAllPage('${k}')">
        ${label}
      </button>
    `).join('');
  } else if (tabsContainer) {
    tabsContainer.querySelectorAll('.drik-page-chip').forEach(btn => {
      if (btn.getAttribute('data-cat') === window._vratCurrentFilter) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  const filter = window._vratCurrentFilter;
  let filtered = allVrats;
  if (filter === 'monthly') {
    filtered = allVrats.filter(v => v.name.includes('एकादशी') || v.name.includes('प्रदोष') || v.name.includes('चतुर्थी') || v.name.includes('शिवरात्रि') || v.name.includes('पूर्णिमा') || v.name.includes('अमावस्या'));
  } else if (filter === 'quarterly') {
    filtered = allVrats.filter(v => v.name.includes('षष्ठी') || v.name.includes('सप्तमी') || v.name.includes('अष्टमी') || v.name.includes('नवमी') || v.name.includes('रोहिणी') || v.name.includes('सोमवार') || v.name.includes('बृहस्पति'));
  } else if (filter === 'special') {
    filtered = allVrats.filter(v => !v.name.includes('एकादशी') && !v.name.includes('प्रदोष') && !v.name.includes('चतुर्थी'));
  }

  if (countBadge) countBadge.textContent = `${filtered.length} व्रत`;

  container.innerHTML = filtered.map(v => {
    let clickAttr = '';
    if (v.isDynamic) {
      clickAttr = `onclick="openVratPage('${v.page}')"`;
    } else if (v.page) {
      clickAttr = `onclick="showPage('${v.page}')"`;
    }
    return `
      <button class="vrat-card" ${clickAttr} style="min-height:115px; padding:1rem 0.5rem; text-align:center;">
        <div class="vrat-img-wrap" style="width:58px; height:58px; margin-bottom:0.5rem;">
          <img class="vrat-icon-img" src="${v.img}" alt="${v.name}" onerror="this.src='assets/app_logo.jpg'">
        </div>
        <div class="vrat-name" style="font-size:0.88rem; font-weight:800; line-height:1.25;">${v.name}</div>
      </button>
    `;
  }).join('');
};
'''
    js += "\n\n" + vrat_all_code.strip() + "\n"
    print("Injected initVratAllPage")

# 4. Load full drik_ganesh_1 data from final_granular_aarti_collections.json
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    colls = json.load(f)

ganesh_item = colls['ganesh']['items'][0]
ganesh_item_json = json.dumps(ganesh_item, ensure_ascii=False, indent=8)

# Find drik_ganesh_1 in AARTI_COLLECTIONS in js
idx_drik1 = js.find('"id": "drik_ganesh_1"')
if idx_drik1 != -1:
    obj_start = js.rfind('{', 0, idx_drik1)
    idx_drik2 = js.find('"id": "drik_ganesh_2"', idx_drik1)
    obj_end = js.rfind('}', 0, idx_drik2) + 1
    js = js[:obj_start] + ganesh_item_json + js[obj_end:]
    print("Updated drik_ganesh_1 in AARTI_COLLECTIONS with complete Drik Panchang data")
else:
    print("WARNING: drik_ganesh_1 not found in js!")

# 5. Inject complete reader & player controllers
reader_controllers = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 DRIK PANCHANG VERIFIED AARTI ITEM READER & PLAYER CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════

window.switchAartiReaderTab = function(tabName) {
  document.querySelectorAll('.aarti-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabName) {
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.color = '#1A0B2E';
      btn.style.fontWeight = '900';
      btn.style.border = 'none';
      btn.style.boxShadow = '0 2px 10px rgba(248,200,59,0.4)';
    } else {
      btn.style.background = 'rgba(255,255,255,0.08)';
      btn.style.color = '#FDE68A';
      btn.style.fontWeight = '700';
      btn.style.border = '1px solid rgba(248,200,59,0.3)';
      btn.style.boxShadow = 'none';
    }
  });

  document.querySelectorAll('.aarti-tab-pane').forEach(pane => {
    pane.style.display = (pane.id === 'aarti-pane-' + tabName) ? 'block' : 'none';
  });
};

window.readAartiItemDirect = function(deityKey, idx, initialMode) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) {
    console.warn("Aarti item not found:", deityKey, idx);
    return;
  }
  const item = coll.items[idx];

  // Close options modal if open
  const modal = document.getElementById('aarti-options-modal');
  if (modal) {
    modal.classList.remove('active');
    modal.style.display = 'none';
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title');
  if (titleEl) titleEl.textContent = item.title || coll.title;

  // 2. Set Deity Image & Audio Titles
  const deityImg = document.getElementById('reader-deity-img');
  if (deityImg) {
    deityImg.src = item.thumb || coll.img || coll.fallbackImg || 'assets/deity_ganesh.jpg';
    deityImg.onerror = function() { this.src = coll.fallbackImg || 'assets/deity_ganesh.jpg'; };
  }

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) aTitleEl.textContent = item.hi_line || item.title;

  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) aSubEl.textContent = `${coll.deity || 'सनातन'} • ${item.sub || 'Drik Panchang Verified'}`;

  // 3. Set Back Button Target
  window.readerBackPage = (typeof currentPage !== 'undefined' && currentPage !== 'page-reader') ? currentPage : 'page-home';
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.onclick = () => window.showPage(window.readerBackPage || 'page-home');
  }

  // 4. Render Video Container if available
  const ytContainer = document.getElementById('reader-youtube-container');
  if (ytContainer) {
    if (item.video_id) {
      ytContainer.style.display = 'block';
      ytContainer.innerHTML = `
        <div style="max-width:680px; margin:0 auto 1.2rem; border-radius:18px; overflow:hidden; border:1.5px solid rgba(248,200,59,0.45); box-shadow:0 8px 25px rgba(0,0,0,0.6); position:relative; background:#000;">
          <iframe width="100%" height="220" src="https://www.youtube.com/embed/${item.video_id}?autoplay=0&rel=0" title="${item.title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="display:block; width:100%; border:none;"></iframe>
          <div style="padding:6px 12px; background:rgba(26,11,46,0.95); font-size:0.75rem; color:#FDE68A; display:flex; align-items:center; justify-content:space-between;">
            <span>🎬 Drik Panchang Official Aarti Video</span>
            <span style="color:#FBCFE8; font-size:0.7rem;">अनुराधा पौडवाल • टी-सीरीज़</span>
          </div>
        </div>
      `;
    } else {
      ytContainer.style.display = 'none';
      ytContainer.innerHTML = '';
    }
  }

  // 5. Render Full Drik Panchang Scripture & Meaning Tabs
  const readerContent = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
  if (readerContent) {
    const hasMeaning = !!item.meaning;
    const hasVidhi = !!item.vidhi;
    const hasSig = !!item.significance;
    const hasEn = !!item.english_lyrics;

    readerContent.innerHTML = `
      <div class="pure-reader-wrapper" style="padding:0.8rem 0 3rem; text-align:center;">
        
        <!-- Header Badge -->
        <div style="font-size:0.82rem; color:#FDE68A; font-weight:800; margin-bottom:0.5rem; background:rgba(248,200,59,0.18); display:inline-flex; align-items:center; gap:6px; padding:5px 16px; border-radius:16px; border:1.2px solid rgba(248,200,59,0.45); box-shadow:0 0 12px rgba(248,200,59,0.25);">
          <span>🪔</span> ${coll.deity} • ${item.source || 'द्रिक पञ्चाङ्ग प्रमाणिक'}
        </div>

        <h1 style="font-size:1.4rem; color:#FFFDF8; font-weight:900; margin:0.4rem 0 1rem; text-shadow:0 2px 8px rgba(0,0,0,0.8);">
          ॥ ${item.hi_line || item.title} ॥
        </h1>

        <!-- Navigation Tabs -->
        <div style="display:flex; gap:8px; overflow-x:auto; padding:0.4rem 0.6rem 1rem; margin-bottom:1rem; justify-content:center; flex-wrap:wrap; scrollbar-width:none;">
          <button class="aarti-tab-btn active" data-tab="lyrics" onclick="window.switchAartiReaderTab('lyrics')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; border:none; box-shadow:0 2px 10px rgba(248,200,59,0.4); transition:all 0.2s ease;">
            📜 आरती पाठ
          </button>
          ${hasMeaning ? `
          <button class="aarti-tab-btn" data-tab="meaning" onclick="window.switchAartiReaderTab('meaning')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            🌺 सम्पूर्ण भावार्थ
          </button>` : ''}
          ${hasVidhi ? `
          <button class="aarti-tab-btn" data-tab="vidhi" onclick="window.switchAartiReaderTab('vidhi')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            🪔 आरती विधि व नियम
          </button>` : ''}
          ${hasSig ? `
          <button class="aarti-tab-btn" data-tab="sig" onclick="window.switchAartiReaderTab('sig')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            ✨ महत्त्व व फलश्रुति
          </button>` : ''}
          ${hasEn ? `
          <button class="aarti-tab-btn" data-tab="en" onclick="window.switchAartiReaderTab('en')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            🔤 English
          </button>` : ''}
        </div>

        <!-- Tab 1: Lyrics Pane -->
        <div id="aarti-pane-lyrics" class="aarti-tab-pane" style="display:block;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1rem; max-width:680px; margin:0 auto; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Tiro Devanagari Hindi', 'Georgia', serif; font-size:1.22rem; line-height:2.3; color:#FFFDF8; font-weight:700; white-space:pre-line; text-shadow:0 1px 4px rgba(0,0,0,0.8);">
${item.content}
            </div>
          </div>
        </div>

        <!-- Tab 2: Meaning Pane -->
        ${hasMeaning ? `
        <div id="aarti-pane-meaning" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1.2rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:0.95rem; line-height:1.9; color:#FEF3C7; font-weight:500; white-space:pre-line;">
${item.meaning}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 3: Vidhi Pane -->
        ${hasVidhi ? `
        <div id="aarti-pane-vidhi" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1.2rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:0.95rem; line-height:1.9; color:#FEF3C7; font-weight:500; white-space:pre-line;">
${item.vidhi}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 4: Significance Pane -->
        ${hasSig ? `
        <div id="aarti-pane-sig" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1.2rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:0.95rem; line-height:1.9; color:#FEF3C7; font-weight:500; white-space:pre-line;">
${item.significance}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 5: English Lyrics Pane -->
        ${hasEn ? `
        <div id="aarti-pane-en" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1rem; max-width:680px; margin:0 auto; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:1.05rem; line-height:2.1; color:#FFFDF8; font-weight:600; white-space:pre-line;">
${item.english_lyrics}
            </div>
          </div>
        </div>` : ''}

        <!-- Drik Panchang Verified Source Link Card -->
        ${item.drik_url ? `
        <div style="max-width:680px; margin:1.5rem auto 0; background:linear-gradient(135deg, rgba(217,119,6,0.18), rgba(120,53,15,0.22)); border:1.2px solid rgba(248,200,59,0.35); border-radius:16px; padding:1rem 1.2rem; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div style="text-align:left;">
            <div style="color:#FDE68A; font-size:0.85rem; font-weight:800; display:flex; align-items:center; gap:6px;">
              <span>🌐</span> द्रिक पञ्चाङ्ग प्रमाणिक संदर्भ (Drik Panchang Verified)
            </div>
            <div style="color:#FBCFE8; font-size:0.75rem; margin-top:2px;">
              शास्त्रीय पाठ, गीतिकाव्य व वीडियो स्रोत
            </div>
          </div>
          <a href="${item.drik_url}" target="_blank" rel="noopener" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; text-decoration:none; font-weight:900; font-size:0.75rem; padding:6px 14px; border-radius:12px; display:inline-flex; align-items:center; gap:4px; box-shadow:0 2px 8px rgba(0,0,0,0.3);">
            द्रिक पञ्चाङ्ग पर देखें ↗
          </a>
        </div>` : ''}

        <!-- Interactive Action Buttons -->
        <div style="margin-top:1.8rem; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
          <button onclick="triggerFlowerShower()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-weight:900; font-size:0.88rem; padding:10px 20px; border-radius:24px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:inline-flex; align-items:center; gap:6px;">
            🌸 पुष्प वर्षा करें
          </button>
          <button onclick="ringBell()" style="background:rgba(255,255,255,0.08); color:#FDE68A; border:1.5px solid rgba(248,200,59,0.35); font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:24px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            🔔 मन्दिर घंटी
          </button>
          <button onclick="shareDivineCard()" style="background:rgba(26,11,46,0.3); color:#FEF3C7; border:1.5px solid rgba(255,255,255,0.2); font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:24px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            📤 शेयर करें
          </button>
        </div>

      </div>
    `;
  }

  // 6. Open Reader Page
  window.showPage('page-reader');
  window.scrollTo(0, 0);
};

window.playAartiItemDirect = function(deityKey, idx) {
  // Directly launch reader in audio mode
  window.readAartiItemDirect(deityKey, idx, 'audio');
  
  if (typeof toggleReaderAudioPlay === 'function') {
    toggleReaderAudioPlay();
  }
};
"""

js += "\n\n" + reader_controllers.strip() + "\n"

# 6. Ensure showPage hook for page-aarti
if "['all', '✨ सभी (86)']" in js:
    js = js.replace("['all', '✨ सभी (86)']", "['all', '✨ सभी (118)']", 1)

show_page_hook = """  if(id === 'page-aarti' && typeof window.renderFullDrikAartiPage === 'function') {
    window.renderFullDrikAartiPage('all', '');
  }
"""
if "if(!$(id)) return;" in js and "if(id === 'page-aarti'" not in js:
    js = js.replace("if(!$(id)) return;", "if(!$(id)) return;\n" + show_page_hook, 1)

# Write out the clean app.js
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"Successfully generated clean app.js: {len(js)} bytes, {js.count(chr(10))} lines")
