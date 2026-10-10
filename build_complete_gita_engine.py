import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read compiled bhagavad_gita_chapters.json
with open('bhagavad_gita_chapters.json', 'r', encoding='utf-8') as f:
    gita_data = json.load(f)

json_str = json.dumps(gita_data, ensure_ascii=False)

engine_js = f"""// ══════════════════════════════════════════════════════════════════════════════
// 📖 BHAGAVAD GITA CHAPTER ENGINE (श्रीमद्भगवद्गीता सम्पूर्ण १८ अध्याय • ७०१ श्लोक)
// BhagavadGita.com Verified Chapter View & Verse-by-Verse Reader
// ══════════════════════════════════════════════════════════════════════════════

window.GITA_DATA = {json_str};

// State
window._gitaFilter = 'all';
window._gitaSearchQuery = '';
window._currentGitaChapter = 1;
window._gitaAudioInstance = null;
window._gitaVerseAudioInstance = null;
window._currentPlayingVerseBtn = null;

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {{
  if (typeof window.renderFullGitaPage === 'function') {{
    window.renderFullGitaPage('all', '');
  }}
}});

// ══════════════════════════════════════════════════════════════════════════════
// 1. CHAPTER OPTIONS OVERVIEW MODAL
// ══════════════════════════════════════════════════════════════════════════════

window.openGitaChapterModal = function(chapNum) {{
  chapNum = parseInt(chapNum, 10);
  if (!window.GITA_DATA || !window.GITA_DATA.chapters) return;
  const chap = window.GITA_DATA.chapters.find(c => c.chapter_number === chapNum);
  if (!chap) return;

  window._currentGitaChapter = chapNum;

  const modal = document.getElementById('gita-chapter-options-modal');
  const imgEl = document.getElementById('gita-modal-img');
  const nameEl = document.getElementById('gita-modal-chap-name');
  const versesEl = document.getElementById('gita-modal-verses');
  const descEl = document.getElementById('gita-modal-desc');
  const listEl = document.getElementById('gita-modal-list');

  if (imgEl) imgEl.src = chap.thumb || 'assets/gallery/gita_upadesh_card.jpg';
  if (nameEl) nameEl.textContent = `अध्याय ${{chapNum}}: ${{chap.name}} (${{chap.name_transliterated}})`;
  if (versesEl) versesEl.textContent = `॥ ${{chap.verses_count}} श्लोक • ${{chap.yoga_group}} • ${{chap.section}} ॥`;
  if (descEl) descEl.textContent = chap.summary ? (chap.summary.length > 250 ? chap.summary.substring(0, 250) + '...' : chap.summary) : '';

  if (listEl) {{
    listEl.innerHTML = `
      <!-- Action Primary: Open Full Chapter Reader -->
      <div style="background:linear-gradient(135deg, rgba(248,200,59,0.18) 0%, rgba(217,119,6,0.25) 100%); border:1.8px solid #F8C83B; border-radius:18px; padding:14px 16px; margin-bottom:12px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.2);" onclick="window.closeGitaChapterModal(); window.openGitaChapterReader(${{chapNum}});">
        <div style="display:flex; align-items:center; gap:12px;">
          <div style="width:42px; height:42px; border-radius:50%; background:linear-gradient(135deg,#F8C83B,#D97706); display:flex; align-items:center; justify-content:center; color:#1A0B2E; font-size:1.3rem; font-weight:900;">
            📖
          </div>
          <div>
            <div style="color:#FFFDF8; font-weight:900; font-size:0.95rem;">सम्पूर्ण अध्याय पाठ पढ़ें</div>
            <div style="color:#FDE68A; font-size:0.75rem;">कुल ${{chap.verses_count}} श्लोक, शब्दार्थ एवं पावन भावार्थ (bhagavadgita.com)</div>
          </div>
        </div>
        <div style="background:#F8C83B; color:#1A0B2E; font-weight:900; font-size:0.8rem; padding:6px 12px; border-radius:12px;">
          पढ़ें ❯
        </div>
      </div>

      <!-- Action Secondary: Listen to Sankirtan -->
      <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(248,200,59,0.3); border-radius:16px; padding:12px 14px; margin-bottom:12px; display:flex; align-items:center; justify-content:space-between; cursor:pointer;" onclick="window.toggleGitaAudio()">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:1.2rem;">🦚</span>
          <span style="color:#FFFDF8; font-size:0.85rem; font-weight:700;">गीता अमृत संकीर्तन सुनें</span>
        </div>
        <span style="color:#FDE68A; font-size:0.75rem;">▶ चलाएं</span>
      </div>

      <!-- Quick Verse Jumper preview -->
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(248,200,59,0.2); border-radius:16px; padding:12px; margin-bottom:12px;">
        <div style="font-size:0.78rem; color:#FDE68A; font-weight:800; margin-bottom:8px;">श्लोक त्वरित चयन (१ से ${{chap.verses_count}}):</div>
        <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:4px; scrollbar-width:none;">
          ${{Array.from({{length: Math.min(chap.verses_count, 15)}}, (_, i) => i + 1).map(v => `
            <button onclick="window.closeGitaChapterModal(); window.openGitaChapterReader(${{chapNum}}, ${{v}});" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; padding:4px 8px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer; flex-shrink:0;">
              ${{v}}
            </button>
          `).join('')}}
          ${{chap.verses_count > 15 ? `<button onclick="window.closeGitaChapterModal(); window.openGitaChapterReader(${{chapNum}});" style="background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:4px 8px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer; flex-shrink:0;">+${{chap.verses_count - 15}} और</button>` : ''}}
        </div>
      </div>
    `;
  }}

  if (modal) {{
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }}
}};

window.closeGitaChapterModal = function() {{
  const modal = document.getElementById('gita-chapter-options-modal');
  if (modal) {{
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }}
}};

// ══════════════════════════════════════════════════════════════════════════════
// 2. DEDICATED CHAPTER VIEW READER (BHAGAVADGITA.COM VERIFIED)
// ══════════════════════════════════════════════════════════════════════════════

window.openGitaChapterReader = function(chapNum, targetVerse) {{
  chapNum = parseInt(chapNum, 10);
  if (!window.GITA_DATA || !window.GITA_DATA.chapters) return;
  const chap = window.GITA_DATA.chapters.find(c => c.chapter_number === chapNum);
  if (!chap) return;

  window._currentGitaChapter = chapNum;

  const readerModal = document.getElementById('gita-chapter-reader-modal');
  const counterEl = document.getElementById('gita-reader-counter');
  const sectionBadgeEl = document.getElementById('gita-reader-section-badge');
  const contentEl = document.getElementById('gita-reader-content');
  const prevBtn = document.getElementById('gita-reader-prev-btn');
  const nextBtn = document.getElementById('gita-reader-next-btn');

  if (counterEl) counterEl.textContent = `अध्याय ${{chapNum}} / 18`;
  if (sectionBadgeEl) sectionBadgeEl.textContent = `${{chap.verses_count}} श्लोक • ${{chap.name}}`;

  // Prev / Next button states
  if (prevBtn) {{
    prevBtn.disabled = chapNum <= 1;
    prevBtn.style.opacity = chapNum <= 1 ? '0.35' : '1';
    prevBtn.onclick = function() {{ window.openGitaChapterReader(chapNum - 1); }};
  }}
  if (nextBtn) {{
    nextBtn.disabled = chapNum >= 18;
    nextBtn.style.opacity = chapNum >= 18 ? '0.35' : '1';
    nextBtn.onclick = function() {{ window.openGitaChapterReader(chapNum + 1); }};
  }}

  // Build Reader DOM
  const verses = chap.verses || [];

  let html = `
    <!-- Chapter Hero Card -->
    <div style="background:linear-gradient(135deg, rgba(31,7,56,0.9) 0%, rgba(59,18,89,0.75) 100%); border:1.8px solid rgba(248,200,59,0.45); border-radius:24px; padding:18px; margin-bottom:18px; text-align:center; box-shadow:0 8px 30px rgba(0,0,0,0.5);">
      <img src="${{chap.thumb || 'assets/gallery/gita_upadesh_card.jpg'}}" style="width:105px; height:105px; border-radius:50%; object-fit:cover; border:3px solid #F8C83B; margin-bottom:10px; box-shadow:0 0 20px rgba(248,200,59,0.4);" alt="Gita Upadesh" />
      <div style="font-size:1.35rem; font-weight:900; color:#FFFDF8; margin-bottom:4px; font-family:'Tiro Devanagari Hindi', serif;">
        ॥ श्रीमद्भगवद्गीता • अध्याय ${{chapNum}} ॥
      </div>
      <div style="font-size:1.15rem; font-weight:800; color:#FDE68A; margin-bottom:6px;">
        ${{chap.name}}
      </div>
      <div style="font-size:0.85rem; color:#CBD5E1; font-style:italic; margin-bottom:8px;">
        ${{chap.name_transliterated}} • ${{chap.name_english}}
      </div>
      <div style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;">
        <span style="background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:3px 10px; border-radius:10px;">
          ${{chap.verses_count}} श्लोक
        </span>
        <span style="background:rgba(255,255,255,0.08); color:#FDE68A; font-size:0.75rem; font-weight:700; padding:3px 10px; border-radius:10px; border:1px solid rgba(248,200,59,0.3);">
          ${{chap.section}}
        </span>
        <span style="background:rgba(255,255,255,0.08); color:#CBD5E1; font-size:0.75rem; font-weight:700; padding:3px 10px; border-radius:10px;">
          ${{chap.yoga_group}}
        </span>
      </div>
    </div>

    <!-- Chapter View Mode Switcher -->
    <div style="display:flex; gap:6px; margin-bottom:16px; background:rgba(255,255,255,0.05); padding:4px; border-radius:14px; border:1px solid rgba(248,200,59,0.25);">
      <button id="gita-tab-btn-verses" onclick="window.switchGitaReaderTab('verses')" style="flex:1; padding:8px 6px; border:none; border-radius:10px; background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; font-weight:900; font-size:0.78rem; cursor:pointer;">
        📜 सम्पूर्ण श्लोक (${{chap.verses_count}})
      </button>
      <button id="gita-tab-btn-intro" onclick="window.switchGitaReaderTab('intro')" style="flex:1; padding:8px 6px; border:none; border-radius:10px; background:transparent; color:#FDE68A; font-weight:800; font-size:0.78rem; cursor:pointer;">
        📖 विस्तृत अध्याय परिचय
      </button>
      <button id="gita-tab-btn-keys" onclick="window.switchGitaReaderTab('keys')" style="flex:1; padding:8px 6px; border:none; border-radius:10px; background:transparent; color:#FDE68A; font-weight:800; font-size:0.78rem; cursor:pointer;">
        💎 प्रमुख सूत्र श्लोक
      </button>
    </div>

    <!-- TAB 1: ALL VERSES (DEFAULT) -->
    <div id="gita-tab-content-verses">
      <!-- Search Verse Input & Jump Pills -->
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(248,200,59,0.25); border-radius:18px; padding:12px; margin-bottom:16px;">
        <div style="position:relative; margin-bottom:10px;">
          <input type="text" id="gita-verse-search" placeholder="🔍 श्लोक संख्या खोजें (जैसे: 1, 22, 47) अथवा शब्द..." oninput="window.filterGitaVerses(this.value)" style="width:100%; background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.3); border-radius:12px; padding:8px 12px 8px 34px; color:#FFFDF8; font-size:0.85rem; outline:none; box-sizing:border-box;" />
          <span style="position:absolute; left:10px; top:50%; transform:translateY(-50%); opacity:0.6; font-size:0.9rem;">🔍</span>
        </div>
        
        <div style="font-size:0.72rem; color:#FDE68A; font-weight:800; margin-bottom:6px;">श्लोक संख्या पर स्पर्श करें और सीधे उस श्लोक पर पहुंचें:</div>
        <div style="display:flex; gap:5px; overflow-x:auto; padding-bottom:4px; scrollbar-width:none;">
          ${{verses.map(v => `
            <a href="#gita-verse-${{chapNum}}-${{v.verse_number}}" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; padding:4px 8px; border-radius:8px; font-size:0.75rem; font-weight:800; text-decoration:none; flex-shrink:0; cursor:pointer;">
              ${{v.verse_number}}
            </a>
          `).join('')}}
        </div>
      </div>

      <!-- Verse Cards List -->
      <div id="gita-verses-list" style="display:flex; flex-direction:column; gap:14px;">
        ${{verses.map(v => `
          <div class="gita-verse-card" id="gita-verse-${{chapNum}}-${{v.verse_number}}" data-verse-num="${{v.verse_number}}" data-verse-text="${{encodeURIComponent(v.sanskrit + ' ' + v.hindi + ' ' + v.english)}}" style="background:linear-gradient(145deg, rgba(31,7,56,0.6) 0%, rgba(20,5,38,0.7) 100%); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:16px; box-shadow:0 6px 20px rgba(0,0,0,0.35);">
            
            <!-- Verse Header -->
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; border-bottom:1px solid rgba(248,200,59,0.2); padding-bottom:8px;">
              <span style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.78rem; font-weight:900; padding:3px 10px; border-radius:10px; display:flex; align-items:center; gap:4px;">
                <span>॥</span> श्लोक ${{chapNum}}.${{v.verse_number}} <span>॥</span>
              </span>
              
              <div style="display:flex; align-items:center; gap:6px;">
                <button class="verse-audio-btn" data-audio="${{v.audio_url}}" onclick="window.playVerseAudio('${{v.audio_url}}', this)" title="श्लोक उच्चारण सुनें" style="background:rgba(248,200,59,0.15); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; padding:4px 8px; border-radius:8px; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:4px;">
                  <span>▶</span> सुनें
                </button>
                <button onclick="triggerFlowerShower()" title="पुष्प वर्षा" style="background:rgba(255,255,255,0.08); border:none; color:#FDE68A; width:28px; height:28px; border-radius:50%; font-size:0.85rem; cursor:pointer;">
                  🌸
                </button>
              </div>
            </div>

            <!-- Sanskrit Verse -->
            <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.15rem; color:#FFFDF8; line-height:1.75; margin-bottom:10px; text-align:center; font-weight:700; text-shadow:0 0 10px rgba(248,200,59,0.2);">
              ${{v.sanskrit ? v.sanskrit.replace(/\\n/g, '<br>') : ''}}
            </div>

            <!-- Transliteration -->
            <div style="font-size:0.82rem; color:#FDE68A; font-style:italic; line-height:1.55; margin-bottom:12px; text-align:center; opacity:0.85;">
              ${{v.transliteration ? v.transliteration.replace(/\\n/g, '<br>') : ''}}
            </div>

            <!-- Hindi Translation (Swami Ramsukhdas / bhagavadgita.com) -->
            <div style="background:linear-gradient(135deg, rgba(248,200,59,0.08) 0%, rgba(217,119,6,0.12) 100%); border-left:3px solid #F8C83B; border-radius:10px; padding:10px 14px; margin-bottom:8px; font-size:0.88rem; color:#FEF3C7; line-height:1.65;">
              <strong style="color:#F8C83B;">हिन्दी भावार्थ:</strong> ${{v.hindi}}
            </div>

            <!-- Expandable Word Meanings & English -->
            ${{v.word_meanings || v.english ? `
              <details style="margin-top:8px; cursor:pointer;">
                <summary style="font-size:0.75rem; color:#CBD5E1; outline:none; user-select:none; font-weight:700;">
                  🔍 शब्दार्थ एवं English Translation देखें ❯
                </summary>
                <div style="margin-top:8px; padding-top:8px; border-top:1px dashed rgba(248,200,59,0.2); font-size:0.78rem; color:#CBD5E1; line-height:1.55;">
                  ${{v.word_meanings ? `
                    <div style="margin-bottom:6px;">
                      <strong style="color:#FDE68A;">शब्दार्थ:</strong> ${{v.word_meanings}}
                    </div>
                  ` : ''}}
                  ${{v.english ? `
                    <div>
                      <strong style="color:#FDE68A;">English:</strong> ${{v.english}}
                    </div>
                  ` : ''}}
                </div>
              </details>
            ` : ''}}

          </div>
        `).join('')}}
      </div>
    </div>

    <!-- TAB 2: DETAILED CHAPTER OVERVIEW -->
    <div id="gita-tab-content-intro" style="display:none;">
      <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:18px; margin-bottom:16px;">
        <div style="color:#F8C83B; font-weight:900; font-size:1.05rem; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
          <span>📜</span> ॥ विस्तृत अध्याय सारांश एवं पृष्ठभूमि (bhagavadgita.com) ॥
        </div>
        <div style="font-size:0.92rem; color:#E2E8F0; line-height:1.85; text-align:justify; white-space:pre-line;">
          ${{chap.summary}}
        </div>
      </div>

      <!-- Life Lessons Box -->
      ${{chap.life_lesson ? `
        <div style="background:linear-gradient(135deg, rgba(16,185,129,0.15) 0%, rgba(5,150,105,0.2) 100%); border:1.5px solid rgba(16,185,129,0.4); border-radius:20px; padding:16px 18px; margin-bottom:16px;">
          <div style="color:#34D399; font-weight:900; font-size:0.95rem; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
            <span>💡</span> ॥ आधुनिक जीवन हेतु गीता की पावन शिक्षा ॥
          </div>
          <div style="font-size:0.9rem; color:#ECFDF5; line-height:1.65;">
            ${{chap.life_lesson}}
          </div>
        </div>
      ` : ''}}
    </div>

    <!-- TAB 3: KEY SHLOKAS -->
    <div id="gita-tab-content-keys" style="display:none;">
      <div style="color:#FDE68A; font-weight:900; font-size:1rem; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
        <span>🪔</span> ॥ इस अध्याय के प्रमुख महावाक्य व सूत्र श्लोक ॥
      </div>
      ${{(chap.key_shlokas || []).map(ks => `
        <div style="background:linear-gradient(135deg, rgba(248,200,59,0.12) 0%, rgba(217,119,6,0.18) 100%); border:1.5px solid #F59E0B; border-radius:18px; padding:16px; margin-bottom:14px; box-shadow:0 4px 15px rgba(0,0,0,0.3);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <span style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:2px 8px; border-radius:8px;">
              श्लोक ${{ks.verse_num}}
            </span>
          </div>
          <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.1rem; color:#FFFDF8; line-height:1.7; margin-bottom:8px; text-align:center; font-weight:700;">
            ${{ks.sanskrit ? ks.sanskrit.replace(/\\n/g, '<br>') : ''}}
          </div>
          <div style="font-size:0.8rem; color:#FDE68A; font-style:italic; line-height:1.5; margin-bottom:8px; text-align:center; opacity:0.85;">
            ${{ks.transliteration ? ks.transliteration.replace(/\\n/g, ' / ') : ''}}
          </div>
          <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:10px 14px; font-size:0.88rem; color:#FEF3C7; line-height:1.6;">
            <strong>भावार्थ:</strong> ${{ks.meaning}}
          </div>
        </div>
      `).join('')}}
    </div>

    <!-- Attribution -->
    <div style="text-align:center; padding:16px; border-top:1px dashed rgba(248,200,59,0.25); color:#94A3B8; font-size:0.75rem; margin-top:20px;">
      प्रामाणिक स्रोत: https://bhagavadgita.com/chapter/${{chapNum}} (श्रीमद्भगवद्गीता सम्पूर्ण अध्याय पाठ)
    </div>
  `;

  if (contentEl) {{
    contentEl.innerHTML = html;
    contentEl.scrollTop = 0;
  }}

  if (readerModal) {{
    readerModal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }}

  // Jump to target verse if requested
  if (targetVerse) {{
    setTimeout(function() {{
      const targetCard = document.getElementById(`gita-verse-${{chapNum}}-${{targetVerse}}`);
      if (targetCard && contentEl) {{
        targetCard.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        targetCard.style.borderColor = '#F8C83B';
        targetCard.style.boxShadow = '0 0 25px rgba(248,200,59,0.6)';
      }}
    }}, 200);
  }}
}};

window.closeGitaChapterReader = function() {{
  const readerModal = document.getElementById('gita-chapter-reader-modal');
  if (readerModal) {{
    readerModal.style.display = 'none';
    document.body.style.overflow = '';
  }}
  if (window._gitaVerseAudioInstance) {{
    window._gitaVerseAudioInstance.pause();
    window._gitaVerseAudioInstance = null;
  }}
  if (window._currentPlayingVerseBtn) {{
    window._currentPlayingVerseBtn.innerHTML = '<span>▶</span> सुनें';
    window._currentPlayingVerseBtn = null;
  }}
}};

// Switch tabs inside chapter reader
window.switchGitaReaderTab = function(tabName) {{
  const tVerses = document.getElementById('gita-tab-content-verses');
  const tIntro = document.getElementById('gita-tab-content-intro');
  const tKeys = document.getElementById('gita-tab-content-keys');

  const bVerses = document.getElementById('gita-tab-btn-verses');
  const bIntro = document.getElementById('gita-tab-btn-intro');
  const bKeys = document.getElementById('gita-tab-btn-keys');

  if (!tVerses || !tIntro || !tKeys) return;

  tVerses.style.display = tabName === 'verses' ? 'block' : 'none';
  tIntro.style.display = tabName === 'intro' ? 'block' : 'none';
  tKeys.style.display = tabName === 'keys' ? 'block' : 'none';

  if (bVerses) {{
    bVerses.style.background = tabName === 'verses' ? 'linear-gradient(135deg,#F8C83B,#D97706)' : 'transparent';
    bVerses.style.color = tabName === 'verses' ? '#1A0B2E' : '#FDE68A';
  }}
  if (bIntro) {{
    bIntro.style.background = tabName === 'intro' ? 'linear-gradient(135deg,#F8C83B,#D97706)' : 'transparent';
    bIntro.style.color = tabName === 'intro' ? '#1A0B2E' : '#FDE68A';
  }}
  if (bKeys) {{
    bKeys.style.background = tabName === 'keys' ? 'linear-gradient(135deg,#F8C83B,#D97706)' : 'transparent';
    bKeys.style.color = tabName === 'keys' ? '#1A0B2E' : '#FDE68A';
  }}
}};

// Live filter verses inside reader
window.filterGitaVerses = function(query) {{
  query = (query || '').trim().toLowerCase();
  const cards = document.querySelectorAll('.gita-verse-card');
  cards.forEach(card => {{
    if (!query) {{
      card.style.display = 'block';
      return;
    }}
    const vNum = card.dataset.verseNum || '';
    const text = decodeURIComponent(card.dataset.verseText || '').toLowerCase();
    if (vNum === query || text.includes(query)) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}};

// Play audio recitation for a specific verse
window.playVerseAudio = function(audioUrl, btnEl) {{
  if (!audioUrl) return;

  if (window._gitaVerseAudioInstance && !window._gitaVerseAudioInstance.paused && window._currentPlayingVerseBtn === btnEl) {{
    window._gitaVerseAudioInstance.pause();
    btnEl.innerHTML = '<span>▶</span> सुनें';
    return;
  }}

  if (window._gitaVerseAudioInstance) {{
    window._gitaVerseAudioInstance.pause();
  }}
  if (window._currentPlayingVerseBtn) {{
    window._currentPlayingVerseBtn.innerHTML = '<span>▶</span> सुनें';
  }}

  btnEl.innerHTML = '<span>⏳</span>...';
  const audio = new Audio(audioUrl);
  window._gitaVerseAudioInstance = audio;
  window._currentPlayingVerseBtn = btnEl;

  audio.play().then(() => {{
    btnEl.innerHTML = '<span>⏸</span> विराम';
  }}).catch(() => {{
    btnEl.innerHTML = '<span>▶</span> सुनें';
  }});

  audio.onended = function() {{
    btnEl.innerHTML = '<span>▶</span> सुनें';
    window._currentPlayingVerseBtn = null;
  }};
}};

// ══════════════════════════════════════════════════════════════════════════════
// 3. CHAPTER JUMPER MODAL
// ══════════════════════════════════════════════════════════════════════════════

window.openGitaJumperModal = function() {{
  const modal = document.getElementById('gita-jumper-modal');
  const listEl = document.getElementById('gita-jumper-list');
  if (!modal || !listEl || !window.GITA_DATA || !window.GITA_DATA.chapters) return;

  listEl.innerHTML = window.GITA_DATA.chapters.map(chap => `
    <div onclick="window.closeGitaJumperModal(); window.openGitaChapterReader(${{chap.chapter_number}});" style="background:linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(248,200,59,0.08) 100%); border:1px solid rgba(248,200,59,0.3); border-radius:14px; padding:10px 14px; display:flex; align-items:center; justify-content:space-between; cursor:pointer;">
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="width:28px; height:28px; border-radius:50%; background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; font-weight:900; font-size:0.75rem; display:flex; align-items:center; justify-content:center;">
          ${{chap.chapter_number}}
        </span>
        <div>
          <div style="color:#FFFDF8; font-weight:800; font-size:0.88rem;">${{chap.name}}</div>
          <div style="color:#FDE68A; font-size:0.72rem;">${{chap.name_transliterated}}</div>
        </div>
      </div>
      <span style="color:#FDE68A; font-size:0.72rem; background:rgba(248,200,59,0.18); padding:2px 8px; border-radius:8px; font-weight:700;">
        ${{chap.verses_count}} श्लोक
      </span>
    </div>
  `).join('');

  modal.style.display = 'flex';
}};

window.closeGitaJumperModal = function() {{
  const modal = document.getElementById('gita-jumper-modal');
  if (modal) modal.style.display = 'none';
}};

// ══════════════════════════════════════════════════════════════════════════════
// 4. FULL PAGE RENDERER (PAGE-GITA)
// ══════════════════════════════════════════════════════════════════════════════

window.renderFullGitaPage = function(filterSection, searchQuery) {{
  window._gitaFilter = filterSection || 'all';
  window._gitaSearchQuery = searchQuery || '';

  const container = document.getElementById('drik-gita-cards-container');
  const pillsContainer = document.getElementById('drik-gita-page-pills');
  if (!container || !window.GITA_DATA || !window.GITA_DATA.chapters) return;

  // Render Filter Pills if not already built
  if (pillsContainer && pillsContainer.children.length === 0) {{
    const pillDefs = [
      {{ id: 'all', label: 'सभी १८ अध्याय (701 श्लोक)', icon: '📖' }},
      {{ id: 'karma', label: 'कर्म षट्क (अध्याय १-६)', icon: '🏹' }},
      {{ id: 'bhakti', label: 'भक्ति षट्क (अध्याय ७-१२)', icon: '🦚' }},
      {{ id: 'jnana', label: 'ज्ञान षट्क (अध्याय १३-१८)', icon: '🕉️' }}
    ];

    pillsContainer.innerHTML = pillDefs.map(pd => `
      <button class="gita-pill-btn" data-filter="${{pd.id}}" onclick="window.renderFullGitaPage('${{pd.id}}', document.getElementById('drik-gita-search-input') ? document.getElementById('drik-gita-search-input').value : '')" style="white-space:nowrap; padding:6px 14px; border-radius:18px; font-size:0.8rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:5px; border:1px solid rgba(248,200,59,0.3); background:${{pd.id === 'all' ? 'linear-gradient(135deg,#F8C83B,#D97706)' : 'rgba(255,255,255,0.06)'}}; color:${{pd.id === 'all' ? '#1A0B2E' : '#FFFDF8'}};">
        <span>${{pd.icon}}</span> ${{pd.label}}
      </button>
    `).join('');
  }}

  // Update active pill styling
  if (pillsContainer) {{
    pillsContainer.querySelectorAll('.gita-pill-btn').forEach(b => {{
      const isActive = b.dataset.filter === window._gitaFilter;
      b.style.background = isActive ? 'linear-gradient(135deg,#F8C83B,#D97706)' : 'rgba(255,255,255,0.06)';
      b.style.color = isActive ? '#1A0B2E' : '#FFFDF8';
    }});
  }}

  // Filter Chapters
  let chapters = window.GITA_DATA.chapters;

  if (window._gitaFilter === 'karma') {{
    chapters = chapters.filter(c => c.chapter_number >= 1 && c.chapter_number <= 6);
  }} else if (window._gitaFilter === 'bhakti') {{
    chapters = chapters.filter(c => c.chapter_number >= 7 && c.chapter_number <= 12);
  }} else if (window._gitaFilter === 'jnana') {{
    chapters = chapters.filter(c => c.chapter_number >= 13 && c.chapter_number <= 18);
  }}

  const q = window._gitaSearchQuery.trim().toLowerCase();
  if (q) {{
    chapters = chapters.filter(c => {{
      return c.chapter_number.toString() === q ||
             c.name.toLowerCase().includes(q) ||
             c.name_transliterated.toLowerCase().includes(q) ||
             c.name_english.toLowerCase().includes(q) ||
             c.summary.toLowerCase().includes(q);
    }});
  }}

  if (chapters.length === 0) {{
    container.innerHTML = `
      <div style="text-align:center; padding:3rem 1rem; color:#CBD5E1;">
        <div style="font-size:2.5rem; margin-bottom:10px;">🔍</div>
        <div style="font-size:1rem; font-weight:800; color:#FFFDF8;">कोई अध्याय नहीं मिला</div>
        <div style="font-size:0.8rem; margin-top:4px;">कृपया अन्य नाम या अध्याय संख्या से खोजें।</div>
      </div>
    `;
    return;
  }}

  container.innerHTML = chapters.map(chap => `
    <div class="gita-chapter-card" onclick="window.openGitaChapterReader(${{chap.chapter_number}})" style="background:linear-gradient(135deg, rgba(31,7,56,0.7) 0%, rgba(20,5,38,0.85) 100%); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:14px; display:flex; gap:14px; cursor:pointer; transition:all 0.25s ease; box-shadow:0 4px 15px rgba(0,0,0,0.3);">
      
      <!-- Thumbnail -->
      <div style="position:relative; width:82px; height:82px; flex-shrink:0; border-radius:16px; overflow:hidden; border:1.8px solid #F8C83B;">
        <img src="${{chap.thumb || 'assets/gallery/gita_upadesh_card.jpg'}}" alt="${{chap.name}}" style="width:100%; height:100%; object-fit:cover;" onerror="this.src='assets/gallery/bal_krishna.jpg';" />
        <span style="position:absolute; bottom:3px; right:3px; background:rgba(0,0,0,0.75); color:#FDE68A; font-size:0.65rem; font-weight:900; padding:1px 5px; border-radius:6px; border:0.8px solid #F8C83B;">
          अ.${{chap.chapter_number}}
        </span>
      </div>

      <!-- Details -->
      <div style="flex:1; min-width:0; display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:6px;">
            <div style="font-size:1.05rem; font-weight:900; color:#FFFDF8; font-family:'Tiro Devanagari Hindi', serif; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
              अध्याय ${{chap.chapter_number}}: ${{chap.name}}
            </div>
            <span style="background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; font-size:0.7rem; font-weight:900; padding:2px 7px; border-radius:8px; flex-shrink:0;">
              ${{chap.verses_count}} श्लोक
            </span>
          </div>

          <div style="font-size:0.78rem; color:#FDE68A; margin-bottom:4px; font-weight:700;">
            ${{chap.name_transliterated}} • ${{chap.yoga_group}}
          </div>

          <div style="font-size:0.75rem; color:#CBD5E1; line-height:1.45; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; text-overflow:ellipsis;">
            ${{chap.summary ? chap.summary.substring(0, 160) + '...' : ''}}
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; border-top:1px dashed rgba(248,200,59,0.2); pt:6px;">
          <span style="font-size:0.7rem; color:#94A3B8;">${{chap.section}}</span>
          <span style="color:#F8C83B; font-size:0.75rem; font-weight:900; display:flex; align-items:center; gap:2px;">
            सम्पूर्ण पाठ ❯
          </span>
        </div>
      </div>

    </div>
  `).join('');
}};

// ══════════════════════════════════════════════════════════════════════════════
// 5. AUDIO CHANTING CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.toggleGitaAudio = function() {{
  const audioBtns = document.querySelectorAll('.gita-audio-btn');

  if (!window._gitaAudioInstance) {{
    const audioSrc = (window.GITA_DATA && window.GITA_DATA.audio_source) ? window.GITA_DATA.audio_source : 'assets/audio/bhajan_achyutam_keshavam.mp3';
    window._gitaAudioInstance = new Audio(audioSrc);
    window._gitaAudioInstance.loop = true;
  }}

  const audio = window._gitaAudioInstance;

  if (audio.paused) {{
    audio.play().then(() => {{
      audioBtns.forEach(b => {{
        b.innerHTML = '<span>⏸</span> संकीर्तन रोकें';
        b.style.background = 'linear-gradient(135deg, #10B981, #059669)';
        b.style.color = '#FFFDF8';
      }});
    }}).catch(err => {{
      console.warn("Audio autoplay blocked or failed:", err);
    }});
  }} else {{
    audio.pause();
    audioBtns.forEach(b => {{
      b.innerHTML = '<span>▶</span> संकीर्तन सुनें';
      b.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      b.style.color = '#1A0B2E';
    }});
  }}
}};
"""

with open('gita_engine.js', 'w', encoding='utf-8') as f:
    f.write(engine_js)

print("Saved gita_engine.js successfully! Size:", len(engine_js))
