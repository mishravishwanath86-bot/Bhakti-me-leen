import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('bhagavad_gita_chapters.json', 'r', encoding='utf-8') as f:
    gita_data = json.load(f)

json_str = json.dumps(gita_data, ensure_ascii=False, indent=2)

js_header = """// ══════════════════════════════════════════════════════════════════════════════
// 📖 BHAGAVAD GITA CHAPTER ENGINE (श्रीमद्भगवद्गीता सम्पूर्ण १८ अध्याय पाठ व भावार्थ)
// ══════════════════════════════════════════════════════════════════════════════

window.GITA_DATA = """

js_body = """;

// State variables
window._gitaCurrentChapter = 1;
window._gitaOriginPage = 'page-home';
window._gitaFilter = 'all';
window._gitaSearch = '';
window._gitaAudio = null;
window._gitaAudioPlaying = false;

// Audio Management
window.toggleGitaAudio = function(forcePlay) {
  if (!window._gitaAudio) {
    window._gitaAudio = new Audio(window.GITA_DATA.audio_source || 'assets/audio/bhajan_achyutam_keshavam.mp3');
    window._gitaAudio.addEventListener('ended', function() {
      window._gitaAudioPlaying = false;
      window.updateGitaAudioUI();
    });
    window._gitaAudio.addEventListener('pause', function() {
      window._gitaAudioPlaying = false;
      window.updateGitaAudioUI();
    });
    window._gitaAudio.addEventListener('play', function() {
      window._gitaAudioPlaying = true;
      window.updateGitaAudioUI();
    });
  }

  if (forcePlay === true || (!window._gitaAudioPlaying && forcePlay !== false)) {
    window._gitaAudio.play().then(() => {
      window._gitaAudioPlaying = true;
      window.updateGitaAudioUI();
    }).catch(e => console.warn('Gita audio play error:', e));
  } else {
    window._gitaAudio.pause();
    window._gitaAudioPlaying = false;
    window.updateGitaAudioUI();
  }
};

window.updateGitaAudioUI = function() {
  const isPlaying = window._gitaAudioPlaying;
  const btns = document.querySelectorAll('.gita-audio-btn, #gita-reader-audio-btn');
  btns.forEach(btn => {
    if (isPlaying) {
      btn.innerHTML = '<span>⏸</span> संकीर्तन रोकें';
      btn.style.background = 'linear-gradient(135deg, #10B981, #059669)';
      btn.style.color = '#FFFDF8';
    } else {
      btn.innerHTML = '<span>▶</span> संकीर्तन सुनें';
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.color = '#1A0B2E';
    }
  });

  const wave = document.getElementById('gita-audio-wave');
  if (wave) {
    wave.style.display = isPlaying ? 'inline-flex' : 'none';
  }
};

// 1. Open Chapter Selection / Overview Modal
window.openGitaChapterModal = function(chapNum) {
  chapNum = parseInt(chapNum, 10) || 1;
  window._gitaCurrentChapter = chapNum;

  const data = window.GITA_DATA;
  if (!data) return;

  const chap = data.chapters.find(c => c.chapter_number === chapNum);
  if (!chap) return;

  const activeOrigin = (window.currentPage && window.currentPage !== 'page-reader') 
    ? window.currentPage 
    : ((typeof currentPage !== 'undefined' && currentPage !== 'page-reader') ? currentPage : 'page-home');
  window._gitaOriginPage = activeOrigin;

  const modal = document.getElementById('gita-chapter-options-modal');
  if (!modal) return;

  const titleEl = document.getElementById('gita-modal-title');
  const chapNameEl = document.getElementById('gita-modal-chap-name');
  const versesEl = document.getElementById('gita-modal-verses');
  const descEl = document.getElementById('gita-modal-desc');
  const imgEl = document.getElementById('gita-modal-img');
  const listContainer = document.getElementById('gita-modal-list');

  if (titleEl) titleEl.textContent = `॥ श्रीमद्भगवद्गीता • अध्याय ${chap.chapter_number} ॥`;
  if (chapNameEl) chapNameEl.textContent = `अध्याय ${chap.chapter_number}: ${chap.name}`;
  if (versesEl) versesEl.textContent = `॥ ${chap.name_transliterated} • ${chap.verses_count} श्लोक • ${chap.yoga_group} ॥`;
  if (descEl) descEl.textContent = chap.summary;

  if (imgEl) {
    imgEl.src = chap.thumb || 'assets/gallery/gita_upadesh_card.jpg';
    imgEl.onerror = function() { this.src = 'assets/gallery/gita_upadesh_card.jpg'; };
  }

  // 18 Chapter Switch Pills
  const switchPillsHtml = `
    <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
      ${data.chapters.map(c => `
        <button onclick="window.openGitaChapterModal(${c.chapter_number})" style="padding:5px 12px; border-radius:14px; border:1px solid rgba(248,200,59,0.35); font-size:0.75rem; font-weight:800; cursor:pointer; white-space:nowrap; background:${c.chapter_number === chapNum ? 'linear-gradient(135deg, #F8C83B, #D97706)' : 'rgba(255,255,255,0.06)'}; color:${c.chapter_number === chapNum ? '#1A0B2E' : '#FDE68A'};">
          अध्याय ${c.chapter_number} (${c.verses_count})
        </button>
      `).join('')}
    </div>
  `;

  // Chapter Content inside modal
  const contentHtml = `
    <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.25); border-radius:18px; padding:14px; box-shadow:0 4px 15px rgba(0,0,0,0.25); margin-bottom:12px;">
      
      <!-- Key Shlokas Box -->
      <div style="margin-bottom:14px;">
        <div style="color:#F59E0B; font-weight:900; font-size:0.95rem; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
          <span>🪔</span> ॥ अध्याय के प्रमुख सूत्र श्लोक ॥
        </div>
        ${chap.key_shlokas.map(ks => `
          <div style="background:rgba(248,200,59,0.08); border-left:3px solid #F59E0B; border-radius:10px; padding:10px 12px; margin-bottom:8px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <span style="font-size:0.72rem; font-weight:800; color:#FDE68A; background:rgba(248,200,59,0.2); padding:2px 6px; border-radius:6px;">
                श्लोक ${ks.verse_num}
              </span>
            </div>
            <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:0.95rem; color:#FFFDF8; line-height:1.5; margin-bottom:4px; font-weight:700;">
              ${ks.sanskrit.replace(/\\n/g, '<br>')}
            </div>
            <div style="font-size:0.8rem; color:#CBD5E1; line-height:1.4;">
              ${ks.meaning}
            </div>
          </div>
        `).join('')}
      </div>

      <!-- Life Lesson Box -->
      <div style="background:linear-gradient(135deg, rgba(248,200,59,0.12) 0%, rgba(217,119,6,0.18) 100%); border:1px solid rgba(248,200,59,0.3); border-radius:12px; padding:10px 12px; margin-bottom:14px;">
        <div style="color:#FDE68A; font-weight:800; font-size:0.85rem; margin-bottom:4px; display:flex; align-items:center; gap:6px;">
          <span>💡</span> गीता जीवन सन्देश
        </div>
        <div style="color:#FFFDF8; font-size:0.82rem; line-height:1.4;">
          ${chap.life_lesson}
        </div>
      </div>

      <!-- Action Buttons -->
      <div style="display:flex; align-items:center; gap:8px;">
        <button onclick="window.openGitaChapterReader(${chap.chapter_number})" style="flex:1; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; padding:10px 14px; border-radius:14px; font-weight:900; font-size:0.85rem; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px; box-shadow:0 3px 10px rgba(248,200,59,0.35);">
          <span>📖</span> सम्पूर्ण अध्याय व श्लोक पढ़ें ❯
        </button>
        <button onclick="window.toggleGitaAudio(true)" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; padding:10px 14px; border-radius:14px; font-size:0.82rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:4px;">
          <span>▶</span> संकीर्तन
        </button>
      </div>
    </div>
  `;

  if (listContainer) {
    listContainer.innerHTML = switchPillsHtml + contentHtml;
  }

  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
};

window.closeGitaChapterModal = function() {
  const modal = document.getElementById('gita-chapter-options-modal');
  if (modal) modal.style.display = 'none';
  document.body.style.overflow = '';
};

// 2. Dedicated Interactive Chapter View Reader (अध्याय-वार पावन पाठ व भावार्थ)
window.openGitaChapterReader = function(chapNum) {
  chapNum = parseInt(chapNum, 10) || 1;
  if (chapNum < 1) chapNum = 1;
  if (chapNum > 18) chapNum = 18;
  window._gitaCurrentChapter = chapNum;

  const data = window.GITA_DATA;
  if (!data) return;

  const chap = data.chapters.find(c => c.chapter_number === chapNum);
  if (!chap) return;

  // Close options modal if open
  window.closeGitaChapterModal();

  const readerModal = document.getElementById('gita-chapter-reader-modal');
  if (!readerModal) return;

  // Header Elements
  const counterEl = document.getElementById('gita-reader-counter');
  const sectionBadgeEl = document.getElementById('gita-reader-section-badge');
  const titleEl = document.getElementById('gita-reader-chapter-title');
  const contentEl = document.getElementById('gita-reader-content');
  const prevBtn = document.getElementById('gita-reader-prev-btn');
  const nextBtn = document.getElementById('gita-reader-next-btn');

  if (counterEl) counterEl.textContent = `अध्याय ${chapNum} / 18`;
  if (sectionBadgeEl) sectionBadgeEl.textContent = `${chap.verses_count} श्लोक • ${chap.yoga_group}`;
  if (titleEl) titleEl.textContent = `अध्याय ${chapNum}: ${chap.name} (${chap.name_transliterated})`;

  // Prev / Next button states
  if (prevBtn) {
    prevBtn.disabled = chapNum <= 1;
    prevBtn.style.opacity = chapNum <= 1 ? '0.35' : '1';
    prevBtn.onclick = function() { window.openGitaChapterReader(chapNum - 1); };
  }
  if (nextBtn) {
    nextBtn.disabled = chapNum >= 18;
    nextBtn.style.opacity = chapNum >= 18 ? '0.35' : '1';
    nextBtn.onclick = function() { window.openGitaChapterReader(chapNum + 1); };
  }

  // Build Reader Content
  let html = `
    <!-- Top Chapter Artwork & Titles -->
    <div style="background:linear-gradient(135deg, rgba(31,7,56,0.85) 0%, rgba(59,18,89,0.7) 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:24px; padding:18px; margin-bottom:20px; text-align:center; box-shadow:0 8px 30px rgba(0,0,0,0.5);">
      <img src="${chap.thumb || 'assets/gallery/gita_upadesh_card.jpg'}" style="width:110px; height:110px; border-radius:50%; object-fit:cover; border:3px solid #F8C83B; margin-bottom:10px; box-shadow:0 0 20px rgba(248,200,59,0.4);" alt="Gita Upadesh" />
      <div style="font-size:1.35rem; font-weight:900; color:#FFFDF8; margin-bottom:4px; font-family:'Tiro Devanagari Hindi', serif;">
        ॥ श्रीमद्भगवद्गीता • अध्याय ${chapNum} ॥
      </div>
      <div style="font-size:1.15rem; font-weight:800; color:#FDE68A; margin-bottom:6px;">
        ${chap.name} (${chap.name_transliterated})
      </div>
      <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;">
        <span style="background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:3px 10px; border-radius:10px;">
          ${chap.verses_count} श्लोक
        </span>
        <span style="background:rgba(255,255,255,0.08); color:#FDE68A; font-size:0.75rem; font-weight:700; padding:3px 10px; border-radius:10px; border:1px solid rgba(248,200,59,0.3);">
          ${chap.section}
        </span>
        <span style="background:rgba(255,255,255,0.08); color:#CBD5E1; font-size:0.75rem; font-weight:700; padding:3px 10px; border-radius:10px;">
          ${chap.yoga_group}
        </span>
      </div>
    </div>

    <!-- Chapter Summary & Overview -->
    <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.25); border-radius:20px; padding:18px; margin-bottom:20px;">
      <div style="color:#F59E0B; font-weight:900; font-size:1rem; margin-bottom:10px; display:flex; align-items:center; gap:8px;">
        <span>📜</span> ॥ विस्तृत अध्याय सारांश एवं महत्त्व ॥
      </div>
      <div style="font-size:0.92rem; color:#E2E8F0; line-height:1.8; text-align:justify;">
        ${chap.summary}
      </div>
    </div>

    <!-- Key Landmark Shlokas -->
    <div style="margin-bottom:22px;">
      <div style="color:#FDE68A; font-weight:900; font-size:1.05rem; margin-bottom:12px; display:flex; align-items:center; gap:8px; border-bottom:1px solid rgba(248,200,59,0.25); padding-bottom:6px;">
        <span>🪔</span> ॥ इस अध्याय के प्रमुख महावाक्य व सूत्र श्लोक ॥
      </div>
      ${chap.key_shlokas.map(ks => `
        <div style="background:linear-gradient(135deg, rgba(248,200,59,0.12) 0%, rgba(217,119,6,0.18) 100%); border:1.5px solid #F59E0B; border-radius:18px; padding:16px; margin-bottom:14px; box-shadow:0 4px 15px rgba(0,0,0,0.3);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <span style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:2px 8px; border-radius:8px;">
              श्लोक ${ks.verse_num}
            </span>
          </div>
          <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.1rem; color:#FFFDF8; line-height:1.7; margin-bottom:8px; text-align:center; font-weight:700;">
            ${ks.sanskrit.replace(/\\n/g, '<br>')}
          </div>
          <div style="font-size:0.8rem; color:#FDE68A; font-style:italic; line-height:1.5; margin-bottom:8px; text-align:center; opacity:0.85;">
            ${ks.transliteration ? ks.transliteration.replace(/\\n/g, ' / ') : ''}
          </div>
          <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:10px 14px; font-size:0.88rem; color:#FEF3C7; line-height:1.6;">
            <strong>भावार्थ:</strong> ${ks.meaning}
          </div>
        </div>
      `).join('')}
    </div>

    <!-- Complete Verse Index (श्लोक सूची) -->
    <div style="background:rgba(255,255,255,0.03); border:1.5px solid rgba(248,200,59,0.2); border-radius:20px; padding:18px; margin-bottom:20px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <div style="color:#FFFDF8; font-weight:900; font-size:0.95rem; display:flex; align-items:center; gap:6px;">
          <span>🔢</span> श्लोक सूची (कुल ${chap.verses_count} श्लोक)
        </div>
        <span style="font-size:0.75rem; color:#CBD5E1;">१ से ${chap.verses_count} श्लोक</span>
      </div>
      <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 10px 0;">इस अध्याय में १ से ${chap.verses_count} तक के पावन श्लोकों का संग्रह:</p>
      <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(64px, 1fr)); gap:6px;">
        ${Array.from({length: chap.verses_count}, (_, i) => i + 1).map(vNum => `
          <button style="padding:6px; border-radius:10px; border:1px solid rgba(248,200,59,0.25); background:rgba(255,255,255,0.05); color:#FDE68A; font-size:0.75rem; font-weight:800; text-align:center;">
            श्लोक ${vNum}
          </button>
        `).join('')}
      </div>
    </div>

    <!-- Life Lessons Box -->
    <div style="background:linear-gradient(135deg, rgba(16,185,129,0.15) 0%, rgba(5,150,105,0.2) 100%); border:1.5px solid rgba(16,185,129,0.4); border-radius:20px; padding:16px 18px; margin-bottom:20px;">
      <div style="color:#34D399; font-weight:900; font-size:0.95rem; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
        <span>💡</span> ॥ आधुनिक जीवन हेतु गीता की पावन शिक्षा ॥
      </div>
      <div style="font-size:0.9rem; color:#ECFDF5; line-height:1.65;">
        ${chap.life_lesson}
      </div>
    </div>

    <!-- Footer Attribution -->
    <div style="text-align:center; padding:12px; border-top:1px dashed rgba(248,200,59,0.25); color:#94A3B8; font-size:0.75rem;">
      स्रोत: https://bhagavadgita.com/ (श्रीमद्भगवद्गीता प्रामाणिक अध्याय पाठ)
    </div>
  `;

  if (contentEl) {
    contentEl.innerHTML = html;
    contentEl.scrollTop = 0;
  }

  readerModal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
};

window.closeGitaChapterReader = function() {
  const readerModal = document.getElementById('gita-chapter-reader-modal');
  if (readerModal) readerModal.style.display = 'none';
  document.body.style.overflow = '';
};

// 3. Quick Chapter Jumper Modal (18 Chapters)
window.openGitaJumperModal = function() {
  const modal = document.getElementById('gita-jumper-modal');
  if (!modal) return;

  const listEl = document.getElementById('gita-jumper-list');
  if (listEl) {
    const cur = window._gitaCurrentChapter || 1;
    const data = window.GITA_DATA;
    listEl.innerHTML = data.chapters.map(c => `
      <div onclick="window.closeGitaJumperModal(); window.openGitaChapterReader(${c.chapter_number});" style="padding:10px 12px; border-radius:14px; border:1.5px solid ${c.chapter_number === cur ? '#F8C83B' : 'rgba(248,200,59,0.25)'}; background:${c.chapter_number === cur ? 'linear-gradient(135deg, rgba(248,200,59,0.25) 0%, rgba(217,119,6,0.3) 100%)' : 'rgba(255,255,255,0.05)'}; cursor:pointer; display:flex; align-items:center; justify-content:space-between; box-shadow:${c.chapter_number === cur ? '0 0 12px rgba(248,200,59,0.4)' : 'none'};">
        <div>
          <div style="font-size:0.85rem; font-weight:900; color:${c.chapter_number === cur ? '#FDE68A' : '#FFFDF8'};">
            अध्याय ${c.chapter_number}: ${c.name}
          </div>
          <div style="font-size:0.72rem; color:#CBD5E1;">
            ${c.name_transliterated} • ${c.verses_count} श्लोक
          </div>
        </div>
        <span style="font-size:0.85rem; color:#FDE68A;">❯</span>
      </div>
    `).join('');
  }

  modal.style.display = 'flex';
};

window.closeGitaJumperModal = function() {
  const modal = document.getElementById('gita-jumper-modal');
  if (modal) modal.style.display = 'none';
};

// 4. Full Page Renderer (page-gita)
window.renderFullGitaPage = function(filterCategory, searchQuery) {
  if (filterCategory !== undefined) window._gitaFilter = filterCategory;
  if (searchQuery !== undefined) window._gitaSearch = searchQuery.toLowerCase().trim();

  const container = document.getElementById('drik-gita-cards-container');
  const pillsContainer = document.getElementById('drik-gita-page-pills');
  if (!container) return;

  const filters = [
    ['all', '✨ सभी (18 अध्याय)'],
    ['karma', '🏹 कर्म षट्क (अध्याय 1-6)'],
    ['bhakti', '🪔 भक्ति षट्क (अध्याय 7-12)'],
    ['jnana', '💡 ज्ञान षट्क (अध्याय 13-18)']
  ];

  if (pillsContainer && pillsContainer.children.length === 0) {
    pillsContainer.innerHTML = filters.map(([k, label]) => `
      <button class="drik-page-chip ${k === window._gitaFilter ? 'active' : ''}" data-cat="${k}" onclick="window.renderFullGitaPage('${k}', window._gitaSearch)" style="padding:6px 14px; border-radius:16px; border:1px solid rgba(248,200,59,0.3); font-size:0.8rem; font-weight:800; cursor:pointer; white-space:nowrap; background:${k === window._gitaFilter ? 'linear-gradient(135deg, #F8C83B, #D97706)' : 'rgba(255,255,255,0.06)'}; color:${k === window._gitaFilter ? '#1A0B2E' : '#FDE68A'};">
        ${label}
      </button>
    `).join('');
  } else if (pillsContainer) {
    pillsContainer.querySelectorAll('.drik-page-chip').forEach(btn => {
      const k = btn.getAttribute('data-cat');
      if (k === window._gitaFilter) {
        btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
        btn.style.color = '#1A0B2E';
      } else {
        btn.style.background = 'rgba(255,255,255,0.06)';
        btn.style.color = '#FDE68A';
      }
    });
  }

  const data = window.GITA_DATA;
  if (!data) return;

  const search = window._gitaSearch;
  const filter = window._gitaFilter;

  // Filter chapters
  let filtered = data.chapters;

  if (filter === 'karma') filtered = filtered.filter(c => c.chapter_number >= 1 && c.chapter_number <= 6);
  else if (filter === 'bhakti') filtered = filtered.filter(c => c.chapter_number >= 7 && c.chapter_number <= 12);
  else if (filter === 'jnana') filtered = filtered.filter(c => c.chapter_number >= 13 && c.chapter_number <= 18);

  if (search) {
    filtered = filtered.filter(c => 
      c.chapter_number.toString() === search ||
      `अध्याय ${c.chapter_number}`.includes(search) ||
      c.name.toLowerCase().includes(search) ||
      c.name_transliterated.toLowerCase().includes(search) ||
      c.summary.toLowerCase().includes(search) ||
      c.yoga_group.toLowerCase().includes(search) ||
      c.life_lesson.toLowerCase().includes(search)
    );
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:3rem 1rem; color:#94A3B8;">
        <div style="font-size:2.5rem; margin-bottom:10px;">🔍</div>
        <div style="font-size:1.1rem; font-weight:700; color:#FFFDF8;">कोई अध्याय नहीं मिला</div>
        <div style="font-size:0.85rem; margin-top:4px;">कृपया अध्याय संख्या (1-18) अथवा विषय लिखकर खोजें</div>
      </div>
    `;
    return;
  }

  let html = `
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:14px;">
      ${filtered.map(chap => `
        <div style="background:linear-gradient(135deg, rgba(31,7,56,0.7) 0%, rgba(59,18,89,0.5) 100%); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:14px; box-shadow:0 6px 20px rgba(0,0,0,0.35); display:flex; flex-direction:column; justify-content:space-between; transition:transform 0.15s ease;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div>
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
              <span style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:3px 8px; border-radius:8px;">
                अध्याय ${chap.chapter_number}
              </span>
              <span style="font-size:0.75rem; color:#FDE68A; background:rgba(248,200,59,0.15); padding:2px 8px; border-radius:8px; font-weight:700;">
                ${chap.verses_count} श्लोक
              </span>
            </div>
            
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
              <img src="${chap.thumb || 'assets/gallery/gita_upadesh_card.jpg'}" style="width:44px; height:44px; border-radius:50%; object-fit:cover; border:1.5px solid #F8C83B;" alt="Gita" />
              <div>
                <div style="font-size:1.02rem; font-weight:900; color:#FFFDF8; line-height:1.3; font-family:'Tiro Devanagari Hindi', serif;">
                  ${chap.name}
                </div>
                <div style="font-size:0.78rem; color:#FDE68A; opacity:0.85;">
                  ${chap.name_transliterated}
                </div>
              </div>
            </div>

            <div style="font-size:0.8rem; color:#CBD5E1; line-height:1.45; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; margin-bottom:12px;">
              ${chap.summary}
            </div>
          </div>

          <div style="display:flex; align-items:center; gap:8px;">
            <button onclick="window.openGitaChapterReader(${chap.chapter_number})" style="flex:1; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; padding:8px 12px; border-radius:12px; font-weight:900; font-size:0.8rem; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:4px; box-shadow:0 2px 8px rgba(248,200,59,0.3);">
              <span>📖</span> अध्याय पढ़ें ❯
            </button>
            <button onclick="window.openGitaChapterModal(${chap.chapter_number})" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; padding:8px 10px; border-radius:12px; font-size:0.8rem; font-weight:800; cursor:pointer;" title="अध्याय सारांश">
              <span>ℹ️</span> सारांश
            </button>
          </div>
        </div>
      `).join('')}
    </div>
  `;

  container.innerHTML = html;
};

// Auto-hook into showPage when window loads
document.addEventListener('DOMContentLoaded', function() {
  if (window.showPage) {
    const origShowPage = window.showPage;
    window.showPage = function(pageId) {
      origShowPage(pageId);
      if (pageId === 'page-gita' && typeof window.renderFullGitaPage === 'function') {
        setTimeout(() => window.renderFullGitaPage('all', ''), 30);
      }
    };
  }
});
"""

with open('gita_engine.js', 'w', encoding='utf-8') as f:
    f.write(js_header + json_str + js_body)

print("SUCCESS: gita_engine.js compiled successfully!")
