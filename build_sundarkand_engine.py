import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('drik_sundarkand_dohas.json', 'r', encoding='utf-8') as f:
    sundarkand_data = json.load(f)

json_str = json.dumps(sundarkand_data, ensure_ascii=False, indent=2)

js_header = """// ══════════════════════════════════════════════════════════════════════════════
// 🏹 DRIK PANCHANG SUNDARKAND DOHA ENGINE (सम्पूर्ण ६० दोहा-वार पाठ व भावार्थ)
// ══════════════════════════════════════════════════════════════════════════════

window.SUNDARKAND_DATA = """

js_body = """;

// State variables
window._sundarkandCurrentDoha = 1;
window._sundarkandActiveChapter = 1;
window._sundarkandOriginPage = 'page-home';
window._sundarkandFilter = 'all';
window._sundarkandSearch = '';
window._sundarkandAudio = null;
window._sundarkandAudioPlaying = false;

// Audio Management
window.toggleSundarkandAudio = function(forcePlay) {
  if (!window._sundarkandAudio) {
    window._sundarkandAudio = new Audio(window.SUNDARKAND_DATA.audio_source || 'assets/audio/katha_rajan_sundarkand.mp3');
    window._sundarkandAudio.addEventListener('ended', function() {
      window._sundarkandAudioPlaying = false;
      window.updateSundarkandAudioUI();
    });
    window._sundarkandAudio.addEventListener('pause', function() {
      window._sundarkandAudioPlaying = false;
      window.updateSundarkandAudioUI();
    });
    window._sundarkandAudio.addEventListener('play', function() {
      window._sundarkandAudioPlaying = true;
      window.updateSundarkandAudioUI();
    });
  }

  if (forcePlay === true || (!window._sundarkandAudioPlaying && forcePlay !== false)) {
    window._sundarkandAudio.play().then(() => {
      window._sundarkandAudioPlaying = true;
      window.updateSundarkandAudioUI();
    }).catch(e => console.warn('Audio play error:', e));
  } else {
    window._sundarkandAudio.pause();
    window._sundarkandAudioPlaying = false;
    window.updateSundarkandAudioUI();
  }
};

window.updateSundarkandAudioUI = function() {
  const isPlaying = window._sundarkandAudioPlaying;
  const btns = document.querySelectorAll('.sundarkand-audio-btn, #sundarkand-reader-audio-btn');
  btns.forEach(btn => {
    if (isPlaying) {
      btn.innerHTML = '<span>⏸</span> पाठ रोकें';
      btn.style.background = 'linear-gradient(135deg, #10B981, #059669)';
      btn.style.color = '#FFFDF8';
    } else {
      btn.innerHTML = '<span>▶</span> पाठ सुनें';
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.color = '#1A0B2E';
    }
  });

  const wave = document.getElementById('sundarkand-audio-wave');
  if (wave) {
    wave.style.display = isPlaying ? 'inline-flex' : 'none';
  }
};

// 1. Open Chapter / Sopan Selection Modal
window.openSundarkandChapterModal = function(chapterId) {
  chapterId = parseInt(chapterId, 10) || 1;
  window._sundarkandActiveChapter = chapterId;

  const data = window.SUNDARKAND_DATA;
  if (!data) return;

  const chap = data.chapters.find(c => c.id === chapterId);
  if (!chap) return;

  const activeOrigin = (window.currentPage && window.currentPage !== 'page-reader') 
    ? window.currentPage 
    : ((typeof currentPage !== 'undefined' && currentPage !== 'page-reader') ? currentPage : 'page-home');
  window._sundarkandOriginPage = activeOrigin;

  const modal = document.getElementById('sundarkand-options-modal');
  if (!modal) return;

  const titleEl = document.getElementById('sundarkand-modal-title');
  const chapTitleEl = document.getElementById('sundarkand-modal-chap-title');
  const rangeEl = document.getElementById('sundarkand-modal-range');
  const descEl = document.getElementById('sundarkand-modal-desc');
  const imgEl = document.getElementById('sundarkand-modal-img');
  const listContainer = document.getElementById('sundarkand-modal-list');

  if (titleEl) titleEl.textContent = `॥ सुन्दरकाण्ड सोपान ${chap.id} ॥`;
  if (chapTitleEl) chapTitleEl.textContent = chap.title;
  if (rangeEl) rangeEl.textContent = `॥ ${chap.doha_range} • कुल ${chap.count} दोहे ॥`;
  if (descEl) descEl.textContent = chap.desc;

  if (imgEl) {
    imgEl.src = chap.thumb;
    imgEl.onerror = function() { this.src = 'assets/gallery/bal_hanuman.jpg'; };
  }

  // 10 Chapter Switch Pills (Non-shrinking, smoothly scrollable, auto-centering)
  const switchPillsHtml = `
    <div class="sundarkand-pills-sticky-wrap">
      <div class="sundarkand-pills-scroller" id="sundarkand-pills-bar">
        ${data.chapters.map(c => `
          <button class="sundarkand-sopan-pill ${c.id === chapterId ? 'active' : ''}" 
                  onclick="window.openSundarkandChapterModal(${c.id})"
                  data-chap="${c.id}"
                  title="${c.title}">
            <span class="sopan-pill-icon">${c.id === chapterId ? '🚩' : '•'}</span>
            <span class="sopan-pill-label">सोपान ${c.id}</span>
            <span class="sopan-pill-range">(${c.doha_range.replace('दोहा ', '')})</span>
          </button>
        `).join('')}
      </div>
    </div>
  `;

  // Get Dohas for this chapter
  const chapterDohas = data.dohas.filter(d => d.chapter_id === chapterId);

  const dohasHtml = `
    <div class="sundarkand-dohas-grid">
      ${chapterDohas.map(doha => `
        <div class="sundarkand-doha-card">
          <div>
            <div class="sundarkand-card-header">
              <span class="sundarkand-doha-badge">
                दोहा ${doha.doha_number}
              </span>
              <span class="sundarkand-chaupai-count">
                📜 ${doha.chaupais.length} चौपाइयाँ
              </span>
            </div>
            <div class="sundarkand-card-title">
              ${doha.title}
            </div>
            <div class="sundarkand-quote-box">
              <div class="sundarkand-quote-lines">
                ${doha.doha ? doha.doha.map(line => `<div class="sundarkand-quote-line">${line}</div>`).join('') : ''}
              </div>
            </div>
            <div class="sundarkand-card-meaning">
              <strong style="color:#FDE68A; font-weight:800;">भावार्थ:</strong> ${doha.meaning}
            </div>
          </div>
          <div class="sundarkand-card-actions">
            <button class="sundarkand-card-read-btn" onclick="window.openSundarkandDohaReader(${doha.doha_number})">
              <span>📖</span> दोहा पाठ व भावार्थ ➔
            </button>
            <button class="sundarkand-card-listen-btn" onclick="window.playSundarkandDoha(${doha.doha_number})" title="दोहा ${doha.doha_number} AI पाठ सुनें">
              <span>🔊</span> पाठ
            </button>
          </div>
        </div>
      `).join('')}
    </div>
  `;

  if (listContainer) {
    listContainer.innerHTML = switchPillsHtml + dohasHtml;
  }

  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';

  setTimeout(() => {
    if (typeof document !== 'undefined' && typeof document.querySelector === 'function') {
      const activePill = document.querySelector('#sundarkand-pills-bar .sundarkand-sopan-pill.active');
      if (activePill && typeof activePill.scrollIntoView === 'function') {
        activePill.scrollIntoView({ inline: 'center', behavior: 'smooth', block: 'nearest' });
      }
    }
  }, 40);

  if (typeof window.updateSundarkandAudioUI === 'function') {
    window.updateSundarkandAudioUI();
  }
};

window.closeSundarkandChapterModal = function() {
  const modal = document.getElementById('sundarkand-options-modal');
  if (modal) modal.style.display = 'none';
  document.body.style.overflow = '';
};

// 2. Dedicated Interactive Doha Reader (दोहा-वार पावन पाठ व भावार्थ)
window.openSundarkandDohaReader = function(dohaNum) {
  dohaNum = parseInt(dohaNum, 10) || 1;
  if (dohaNum < 1) dohaNum = 1;
  if (dohaNum > 60) dohaNum = 60;
  window._sundarkandCurrentDoha = dohaNum;

  const data = window.SUNDARKAND_DATA;
  if (!data) return;

  const doha = data.dohas.find(d => d.doha_number === dohaNum);
  if (!doha) return;

  // Close chapter modal if open
  window.closeSundarkandChapterModal();

  const readerModal = document.getElementById('sundarkand-reader-modal');
  if (!readerModal) return;

  // Header Elements
  const counterEl = document.getElementById('sundarkand-reader-counter');
  const sopanBadgeEl = document.getElementById('sundarkand-reader-sopan-badge');
  const dohaTitleEl = document.getElementById('sundarkand-reader-doha-title');
  const contentEl = document.getElementById('sundarkand-reader-content');
  const prevBtn = document.getElementById('sundarkand-reader-prev-btn');
  const nextBtn = document.getElementById('sundarkand-reader-next-btn');

  if (counterEl) counterEl.textContent = `दोहा ${dohaNum} / 60`;
  if (sopanBadgeEl) sopanBadgeEl.textContent = doha.chapter_range;
  if (dohaTitleEl) dohaTitleEl.textContent = `दोहा ${dohaNum}: ${doha.title}`;

  // Prev / Next button states
  if (prevBtn) {
    prevBtn.disabled = dohaNum <= 1;
    prevBtn.style.opacity = dohaNum <= 1 ? '0.35' : '1';
    prevBtn.onclick = function() { window.openSundarkandDohaReader(dohaNum - 1); };
  }
  if (nextBtn) {
    nextBtn.disabled = dohaNum >= 60;
    nextBtn.style.opacity = dohaNum >= 60 ? '0.35' : '1';
    nextBtn.onclick = function() { window.openSundarkandDohaReader(dohaNum + 1); };
  }

  // Build Reader Content
  let html = '';

  // 1. Shloka (If Doha 1)
  if (doha.shloka && doha.shloka.length > 0) {
    html += `
      <div style="background:rgba(248,200,59,0.06); border:1.5px solid rgba(248,200,59,0.3); border-radius:18px; padding:16px; margin-bottom:18px; text-align:center;">
        <div style="color:#F59E0B; font-weight:900; font-size:1rem; margin-bottom:8px; display:flex; align-items:center; justify-content:center; gap:6px;">
          <span>🕉️</span> ॥ मंगलाचरण श्लोक ॥
        </div>
        <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.02rem; color:#FEF3C7; line-height:1.7; white-space:pre-line;">
          ${doha.shloka.join('\\n')}
        </div>
      </div>
    `;
  }

  // 2. Chaupais (चौपाइयाँ)
  if (doha.chaupais && doha.chaupais.length > 0) {
    html += `
      <div style="margin-bottom:18px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; border-bottom:1px solid rgba(248,200,59,0.2); padding-bottom:4px;">
          <div style="color:#FDE68A; font-weight:900; font-size:0.95rem; display:flex; align-items:center; gap:6px;">
            <span>॥</span> चौपाई <span>॥</span>
          </div>
          <span style="font-size:0.75rem; color:#CBD5E1; background:rgba(255,255,255,0.08); padding:2px 8px; border-radius:10px;">
            ${doha.chaupais.length} पंक्तियाँ
          </span>
        </div>
        <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.05rem; color:#FFFDF8; line-height:1.8; padding:4px 8px;">
          ${doha.chaupais.map(line => `<div style="margin-bottom:6px; letter-spacing:0.2px;">${line}</div>`).join('')}
        </div>
      </div>
    `;
  }

  // 3. Chhand (If present)
  if (doha.chhand && doha.chhand.length > 0) {
    html += `
      <div style="background:rgba(251,191,36,0.06); border:1.5px solid rgba(251,191,36,0.3); border-radius:18px; padding:16px; margin-bottom:18px;">
        <div style="color:#F59E0B; font-weight:900; font-size:0.95rem; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
          <span>🎶</span> ॥ छन्द ॥
        </div>
        <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.02rem; color:#FEF3C7; line-height:1.75;">
          ${doha.chhand.map(line => `<div style="margin-bottom:4px;">${line}</div>`).join('')}
        </div>
      </div>
    `;
  }

  // 4. Doha (Golden Highlight Card)
  if (doha.doha && doha.doha.length > 0) {
    html += `
      <div style="background:linear-gradient(135deg, rgba(248,200,59,0.15) 0%, rgba(217,119,6,0.2) 100%); border:2px solid #F59E0B; border-radius:20px; padding:18px; margin-bottom:20px; text-align:center; box-shadow:0 0 25px rgba(248,200,59,0.25);">
        <div style="color:#FDE68A; font-weight:900; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">
          ॥ दोहा ${dohaNum} ॥
        </div>
        <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.15rem; font-weight:700; color:#FFFDF8; line-height:1.8; text-shadow:0 0 12px rgba(248,200,59,0.4);">
          ${doha.doha.join('<br>')}
        </div>
      </div>
    `;
  }

  // 5. Hindi Meaning (भावार्थ)
  if (doha.meaning) {
    html += `
      <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.2); border-radius:18px; padding:16px 18px; margin-bottom:20px;">
        <div style="color:#F59E0B; font-weight:900; font-size:0.95rem; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
          <span>💡</span> ॥ पावन हिन्दी भावार्थ ॥
        </div>
        <div style="font-size:0.92rem; color:#E2E8F0; line-height:1.75; text-align:justify;">
          ${doha.meaning}
        </div>
      </div>
    `;
  }

  // 6. Footer / Verification badge
  html += `
    <div style="text-align:center; padding:12px; border-top:1px dashed rgba(248,200,59,0.25); color:#94A3B8; font-size:0.75rem;">
      द्रिक पञ्चाङ्ग प्रमाणिक श्री रामचरितमानस सुन्दरकाण्ड पाठ (Drik Panchang Verified)
    </div>
  `;

  if (contentEl) {
    contentEl.innerHTML = html;
    contentEl.scrollTop = 0;
  }

  readerModal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
};

window.closeSundarkandDohaReader = function() {
  const readerModal = document.getElementById('sundarkand-reader-modal');
  if (readerModal) readerModal.style.display = 'none';
  document.body.style.overflow = '';
};

// 3. Quick Doha Jumper (दोहा चयन 1 से 60)
window.openSundarkandJumperModal = function() {
  const modal = document.getElementById('sundarkand-jumper-modal');
  if (!modal) return;

  const listEl = document.getElementById('sundarkand-jumper-list');
  if (listEl) {
    const cur = window._sundarkandCurrentDoha || 1;
    let buttonsHtml = '';
    for (let i = 1; i <= 60; i++) {
      const isCur = i === cur;
      buttonsHtml += `
        <button onclick="window.closeSundarkandJumperModal(); window.openSundarkandDohaReader(${i});" style="width:48px; height:48px; border-radius:12px; border:1.5px solid ${isCur ? '#F8C83B' : 'rgba(248,200,59,0.25)'}; background:${isCur ? 'linear-gradient(135deg, #F8C83B, #D97706)' : 'rgba(255,255,255,0.06)'}; color:${isCur ? '#1A0B2E' : '#FFFDF8'}; font-weight:900; font-size:0.95rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:${isCur ? '0 0 12px rgba(248,200,59,0.5)' : 'none'};">
          ${i}
        </button>
      `;
    }
    listEl.innerHTML = buttonsHtml;
  }

  modal.style.display = 'flex';
};

window.closeSundarkandJumperModal = function() {
  const modal = document.getElementById('sundarkand-jumper-modal');
  if (modal) modal.style.display = 'none';
};

// 4. Full Page Renderer (page-sundarkand)
window.renderFullSundarkandPage = function(filterCategory, searchQuery) {
  if (filterCategory !== undefined) window._sundarkandFilter = filterCategory;
  if (searchQuery !== undefined) window._sundarkandSearch = searchQuery.toLowerCase().trim();

  const container = document.getElementById('drik-sundarkand-cards-container');
  const pillsContainer = document.getElementById('drik-sundarkand-page-pills');
  if (!container) return;

  const filters = [
    ['all', '✨ सभी (60 दोहे)'],
    ['sopan-1-2', '🚩 सोपान 1-2 (1-12)'],
    ['sopan-3-4', '🚩 सोपान 3-4 (13-24)'],
    ['sopan-5-6', '🚩 सोपान 5-6 (25-36)'],
    ['sopan-7-8', '🚩 सोपान 7-8 (37-48)'],
    ['sopan-9-10', '🚩 सोपान 9-10 (49-60)']
  ];

  if (pillsContainer && pillsContainer.children.length === 0) {
    pillsContainer.innerHTML = filters.map(([k, label]) => `
      <button class="drik-page-chip ${k === window._sundarkandFilter ? 'active' : ''}" data-cat="${k}" onclick="window.renderFullSundarkandPage('${k}', window._sundarkandSearch)" style="padding:6px 14px; border-radius:16px; border:1px solid rgba(248,200,59,0.3); font-size:0.8rem; font-weight:800; cursor:pointer; white-space:nowrap; background:${k === window._sundarkandFilter ? 'linear-gradient(135deg, #F8C83B, #D97706)' : 'rgba(255,255,255,0.06)'}; color:${k === window._sundarkandFilter ? '#1A0B2E' : '#FDE68A'};">
        ${label}
      </button>
    `).join('');
  } else if (pillsContainer) {
    pillsContainer.querySelectorAll('.drik-page-chip').forEach(btn => {
      const k = btn.getAttribute('data-cat');
      if (k === window._sundarkandFilter) {
        btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
        btn.style.color = '#1A0B2E';
      } else {
        btn.style.background = 'rgba(255,255,255,0.06)';
        btn.style.color = '#FDE68A';
      }
    });
  }

  const data = window.SUNDARKAND_DATA;
  if (!data) return;

  const search = window._sundarkandSearch;
  const filter = window._sundarkandFilter;

  // Filter dohas
  let filteredDohas = data.dohas;

  if (filter === 'sopan-1-2') filteredDohas = filteredDohas.filter(d => d.chapter_id === 1 || d.chapter_id === 2);
  else if (filter === 'sopan-3-4') filteredDohas = filteredDohas.filter(d => d.chapter_id === 3 || d.chapter_id === 4);
  else if (filter === 'sopan-5-6') filteredDohas = filteredDohas.filter(d => d.chapter_id === 5 || d.chapter_id === 6);
  else if (filter === 'sopan-7-8') filteredDohas = filteredDohas.filter(d => d.chapter_id === 7 || d.chapter_id === 8);
  else if (filter === 'sopan-9-10') filteredDohas = filteredDohas.filter(d => d.chapter_id === 9 || d.chapter_id === 10);

  if (search) {
    filteredDohas = filteredDohas.filter(d => 
      d.doha_number.toString() === search ||
      `दोहा ${d.doha_number}`.includes(search) ||
      d.title.toLowerCase().includes(search) ||
      d.meaning.toLowerCase().includes(search) ||
      (d.doha && d.doha.join(' ').toLowerCase().includes(search)) ||
      (d.chaupais && d.chaupais.join(' ').toLowerCase().includes(search)) ||
      d.chapter_title.toLowerCase().includes(search)
    );
  }

  if (filteredDohas.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:3rem 1rem; color:#94A3B8;">
        <div style="font-size:2.5rem; margin-bottom:10px;">🔍</div>
        <div style="font-size:1.1rem; font-weight:700; color:#FFFDF8;">कोई दोहा नहीं मिला</div>
        <div style="font-size:0.85rem; margin-top:4px;">कृपया दोहा संख्या (1-60) अथवा अन्य शब्द लिखकर खोजें</div>
      </div>
    `;
    return;
  }

  // Group by chapter
  const grouped = {};
  filteredDohas.forEach(d => {
    if (!grouped[d.chapter_id]) grouped[d.chapter_id] = [];
    grouped[d.chapter_id].push(d);
  });

  let html = '';
  Object.keys(grouped).forEach(chapIdStr => {
    const cId = parseInt(chapIdStr, 10);
    const chap = data.chapters.find(c => c.id === cId);
    const dohasInChap = grouped[chapIdStr];

    html += `
      <div style="background:linear-gradient(135deg, rgba(31,7,56,0.7) 0%, rgba(59,18,89,0.5) 100%); border:1.5px solid rgba(248,200,59,0.3); border-radius:22px; padding:1.2rem; margin-bottom:1.2rem; box-shadow:0 6px 20px rgba(0,0,0,0.35);">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; border-bottom:1px solid rgba(248,200,59,0.25); padding-bottom:8px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <img src="${chap ? chap.thumb : 'assets/gallery/bal_hanuman.jpg'}" style="width:36px; height:36px; border-radius:50%; object-fit:cover; border:1.5px solid #F8C83B;" alt="thumb" />
            <div>
              <div style="font-size:1rem; font-weight:900; color:#FFFDF8;">${chap ? chap.title : 'सोपान ' + cId}</div>
              <div style="font-size:0.75rem; color:#FDE68A;">॥ ${chap ? chap.doha_range : ''} ॥</div>
            </div>
          </div>
          <button onclick="window.openSundarkandChapterModal(${cId})" style="background:rgba(248,200,59,0.15); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; padding:4px 10px; border-radius:12px; font-size:0.75rem; font-weight:800; cursor:pointer;">
            सोपान देखें ❯
          </button>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:10px;">
          ${dohasInChap.map(doha => `
            <div onclick="window.openSundarkandDohaReader(${doha.doha_number})" style="background:rgba(255,255,255,0.04); border:1px solid rgba(248,200,59,0.2); border-radius:16px; padding:10px 12px; cursor:pointer; transition:transform 0.15s ease;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
              <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:4px;">
                <span style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.68rem; font-weight:900; padding:2px 6px; border-radius:8px;">
                  #${doha.doha_number} दोहा
                </span>
                <span style="font-size:0.72rem; color:#FDE68A; opacity:0.8;">
                  ${doha.chaupais.length} चौपाई
                </span>
              </div>
              <div style="font-size:0.88rem; font-weight:800; color:#FFFDF8; margin-bottom:4px; line-height:1.35;">
                ${doha.title}
              </div>
              <div style="font-size:0.78rem; color:#FDE68A; font-family:'Tiro Devanagari Hindi', serif; line-height:1.35; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; opacity:0.9;">
                ${doha.doha ? doha.doha[0] : ''}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
};

// Auto-hook into showPage when window loads
document.addEventListener('DOMContentLoaded', function() {
  if (window.showPage) {
    const origShowPage = window.showPage;
    window.showPage = function(pageId) {
      origShowPage(pageId);
      if (pageId === 'page-sundarkand' && typeof window.renderFullSundarkandPage === 'function') {
        setTimeout(() => window.renderFullSundarkandPage('all', ''), 30);
      }
    };
  }
});
"""

with open('sundarkand_engine.js', 'w', encoding='utf-8') as f:
    f.write(js_header + json_str + js_body)

print("SUCCESS: sundarkand_engine.js compiled successfully!")
