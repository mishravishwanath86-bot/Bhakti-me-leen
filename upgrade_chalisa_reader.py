import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', encoding='utf-8') as f:
    app_js = f.read()

target_start = 'window.readChalisaItemDirect = function(deityKey, idx) {'
pos = app_js.find(target_start)
if pos == -1:
    print("ERROR: could not find window.readChalisaItemDirect in app.js")
    sys.exit(1)

# Find the end of window.readChalisaItemDirect, which ends before "// Direct audio/video player"
end_marker = '// Direct audio/video player'
end_pos = app_js.find(end_marker, pos)
if end_pos == -1:
    print("ERROR: could not find end_marker in app.js")
    sys.exit(1)

new_func = """window.switchChalisaReaderTab = function(tabName) {
  document.querySelectorAll('.chalisa-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabName) {
      btn.style.background = 'linear-gradient(135deg, #F59E0B, #D97706)';
      btn.style.color = '#000000';
      btn.style.fontWeight = '900';
      btn.style.border = '1.5px solid #B45309';
      btn.style.boxShadow = '0 4px 12px rgba(217,119,6,0.35)';
    } else {
      btn.style.background = '#FFFFFF';
      btn.style.color = '#000000';
      btn.style.fontWeight = '700';
      btn.style.border = '1.5px solid #D1D5DB';
      btn.style.boxShadow = '0 2px 6px rgba(0,0,0,0.06)';
    }
  });
  document.querySelectorAll('.chalisa-tab-pane').forEach(pane => {
    pane.style.display = (pane.id === 'chalisa-pane-' + tabName) ? 'block' : 'none';
  });
};

window.readChalisaItemDirect = function(deityKey, idx, initialMode) {
  const coll = window.CHALISA_COLLECTIONS ? window.CHALISA_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) {
    console.warn("Chalisa item not found:", deityKey, idx);
    return;
  }
  const item = coll.items[idx];
  
  if (typeof window.closeChalisaOptionsModal === 'function') {
    window.closeChalisaOptionsModal();
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title');
  if (titleEl) {
    titleEl.textContent = item.title || coll.title;
    titleEl.style.color = '#000000';
  }

  // 2. Set Deity Image & Audio Titles
  const deityImg = document.getElementById('reader-deity-img');
  if (deityImg) {
    deityImg.src = item.thumb || coll.img || coll.fallbackImg || 'assets/gallery/bal_hanuman.jpg';
    deityImg.onerror = function() { this.src = coll.fallbackImg || 'assets/app_logo.jpg'; };
  }

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) {
    aTitleEl.textContent = item.hi_line || item.title;
    aTitleEl.style.color = '#000000';
  }

  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) {
    aSubEl.textContent = `${coll.deity || 'संकटमोचन श्री हनुमान जी'} • ${item.sub || 'पावन नित्य चालीसा'}`;
    aSubEl.style.color = '#374151';
  }

  // 3. Set Back Button Target
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.onclick = function(e) {
      if (e && typeof e.preventDefault === 'function') e.preventDefault();
      if (e && typeof e.stopPropagation === 'function') e.stopPropagation();
      window.handleReaderBack(e);
    };
  }

  // 4. Video Player handling
  const ytContainer = document.getElementById('reader-youtube-container');
  if (ytContainer) {
    if (initialMode === 'video' && item.video_id) {
      ytContainer.style.display = 'block';
      ytContainer.innerHTML = `<iframe width="100%" height="220" src="https://www.youtube.com/embed/${item.video_id}?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:12px; margin-bottom:12px;"></iframe>`;
    } else {
      ytContainer.style.display = 'none';
      ytContainer.innerHTML = '';
    }
  }

  // 5. Render Full Drik Panchang Scripture & Meaning Tabs with Deep Black Text
  const readerContent = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
  if (readerContent) {
    const hasMeaning = !!item.meaning;
    const hasVidhi = !!item.vidhi;
    const hasSig = !!item.significance;
    const hasEn = !!item.english_lyrics;

    readerContent.innerHTML = `
      <div class="pure-reader-wrapper" style="padding:0.6rem 0 3rem; text-align:center; color:#000000;">
        
        <!-- Header Badge -->
        <div style="font-size:0.85rem; color:#78350F; font-weight:800; margin-bottom:0.6rem; background:rgba(248, 200, 59, 0.25); display:inline-block; padding:5px 16px; border-radius:16px; border:1.5px solid rgba(217, 119, 6, 0.4);">
          🪔 ${coll.deity || 'संकटमोचन श्री हनुमान जी'} • ${item.sub || 'Drik Panchang Verified'}
        </div>

        <!-- Main Title -->
        <h1 style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.6rem; color:#000000; font-weight:900; margin:0.4rem 0 1.2rem; text-shadow:none; letter-spacing:0.3px;">
          ॥ ${item.hi_line || item.title} ॥
        </h1>

        <!-- Navigation Tabs with High Contrast Black Text -->
        <div style="display:flex; gap:8px; overflow-x:auto; padding:0.4rem 0.6rem 1.2rem; margin-bottom:1rem; justify-content:center; flex-wrap:wrap; scrollbar-width:none;">
          <button class="chalisa-tab-btn active" data-tab="lyrics" onclick="window.switchChalisaReaderTab('lyrics')" style="padding:8px 16px; border-radius:18px; font-size:0.82rem; white-space:nowrap; cursor:pointer; background:linear-gradient(135deg, #F59E0B, #D97706); color:#000000; font-weight:900; border:1.5px solid #B45309; box-shadow:0 4px 12px rgba(217,119,6,0.35); transition:all 0.2s ease;">
            📜 पावन पाठ
          </button>
          ${hasMeaning ? `
          <button class="chalisa-tab-btn" data-tab="meaning" onclick="window.switchChalisaReaderTab('meaning')" style="padding:8px 16px; border-radius:18px; font-size:0.82rem; white-space:nowrap; cursor:pointer; background:#FFFFFF; color:#000000; font-weight:700; border:1.5px solid #D1D5DB; box-shadow:0 2px 6px rgba(0,0,0,0.06); transition:all 0.2s ease;">
            📖 सम्पूर्ण भावार्थ
          </button>` : ''}
          ${hasVidhi ? `
          <button class="chalisa-tab-btn" data-tab="vidhi" onclick="window.switchChalisaReaderTab('vidhi')" style="padding:8px 16px; border-radius:18px; font-size:0.82rem; white-space:nowrap; cursor:pointer; background:#FFFFFF; color:#000000; font-weight:700; border:1.5px solid #D1D5DB; box-shadow:0 2px 6px rgba(0,0,0,0.06); transition:all 0.2s ease;">
            🪔 पाठ विधि व नियम
          </button>` : ''}
          ${hasSig ? `
          <button class="chalisa-tab-btn" data-tab="sig" onclick="window.switchChalisaReaderTab('sig')" style="padding:8px 16px; border-radius:18px; font-size:0.82rem; white-space:nowrap; cursor:pointer; background:#FFFFFF; color:#000000; font-weight:700; border:1.5px solid #D1D5DB; box-shadow:0 2px 6px rgba(0,0,0,0.06); transition:all 0.2s ease;">
            ✨ महत्त्व व फलश्रुति
          </button>` : ''}
          ${hasEn ? `
          <button class="chalisa-tab-btn" data-tab="en" onclick="window.switchChalisaReaderTab('en')" style="padding:8px 16px; border-radius:18px; font-size:0.82rem; white-space:nowrap; cursor:pointer; background:#FFFFFF; color:#000000; font-weight:700; border:1.5px solid #D1D5DB; box-shadow:0 2px 6px rgba(0,0,0,0.06); transition:all 0.2s ease;">
            🔤 English Lyrics
          </button>` : ''}
        </div>

        <!-- Tab 1: Lyrics Pane (Deep Black Text) -->
        <div id="chalisa-pane-lyrics" class="chalisa-tab-pane" style="display:block;">
          <div style="background:#FFFFFF; border:1.5px solid #E5E7EB; border-radius:24px; padding:2rem 1.4rem; max-width:680px; margin:0 auto; box-shadow:0 10px 30px rgba(0,0,0,0.08);">
            <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.16rem; line-height:2.3; color:#000000; font-weight:700; white-space:pre-line; text-shadow:none;">
${item.content || item.text}
            </div>
          </div>
        </div>

        <!-- Tab 2: Meaning Pane (Deep Black Text) -->
        ${hasMeaning ? `
        <div id="chalisa-pane-meaning" class="chalisa-tab-pane" style="display:none;">
          <div style="background:#FFFFFF; border:1.5px solid #E5E7EB; border-radius:24px; padding:2rem 1.4rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 10px 30px rgba(0,0,0,0.08);">
            <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.05rem; line-height:2.1; color:#000000; font-weight:600; white-space:pre-line; text-shadow:none;">
${item.meaning}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 3: Vidhi Pane (Deep Black Text) -->
        ${hasVidhi ? `
        <div id="chalisa-pane-vidhi" class="chalisa-tab-pane" style="display:none;">
          <div style="background:#FFFFFF; border:1.5px solid #E5E7EB; border-radius:24px; padding:2rem 1.4rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 10px 30px rgba(0,0,0,0.08);">
            <div style="font-family:'Inter', sans-serif; font-size:1.02rem; line-height:2.1; color:#000000; font-weight:600; white-space:pre-line; text-shadow:none;">
${item.vidhi}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 4: Significance Pane (Deep Black Text) -->
        ${hasSig ? `
        <div id="chalisa-pane-sig" class="chalisa-tab-pane" style="display:none;">
          <div style="background:#FFFFFF; border:1.5px solid #E5E7EB; border-radius:24px; padding:2rem 1.4rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 10px 30px rgba(0,0,0,0.08);">
            <div style="font-family:'Inter', sans-serif; font-size:1.02rem; line-height:2.1; color:#000000; font-weight:600; white-space:pre-line; text-shadow:none;">
${item.significance}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 5: English Lyrics Pane (Deep Black Text) -->
        ${hasEn ? `
        <div id="chalisa-pane-en" class="chalisa-tab-pane" style="display:none;">
          <div style="background:#FFFFFF; border:1.5px solid #E5E7EB; border-radius:24px; padding:2rem 1.4rem; max-width:680px; margin:0 auto; box-shadow:0 10px 30px rgba(0,0,0,0.08);">
            <div style="font-family:'Inter', sans-serif; font-size:1.1rem; line-height:2.3; color:#000000; font-weight:700; white-space:pre-line; text-shadow:none;">
${item.english_lyrics}
            </div>
          </div>
        </div>` : ''}

        <!-- Drik Panchang Verified Source Link Card -->
        ${item.drik_url ? `
        <div style="max-width:680px; margin:1.5rem auto 0; padding:1rem; border-radius:18px; background:linear-gradient(135deg, #FEF3C7, #FDE68A); border:1.5px solid #F59E0B; text-align:center; box-shadow:0 4px 15px rgba(245,158,11,0.15);">
          <div style="font-size:0.85rem; font-weight:800; color:#92400E; margin-bottom:4px;">
            🌐 द्रिक पञ्चाङ्ग (Drik Panchang) प्रामाणिक स्रोत
          </div>
          <div style="font-size:0.75rem; color:#78350F; margin-bottom:10px;">
            यह पावन पाठ, भावार्थ व विधि द्रिक पञ्चाङ्ग के मूल शास्त्रोक्त संदर्भों द्वारा सत्यापित है।
          </div>
          <a href="${item.drik_url}" target="_blank" rel="noopener noreferrer" style="display:inline-flex; align-items:center; gap:6px; background:#D97706; color:#FFFFFF; text-decoration:none; font-weight:800; font-size:0.82rem; padding:6px 16px; border-radius:14px; box-shadow:0 2px 8px rgba(217,119,6,0.3);">
            <span>🔗 द्रिक पञ्चाङ्ग पर मूल पृष्ठ देखें</span>
          </a>
        </div>` : ''}

        <!-- Interactive Devotional Action Buttons -->
        <div style="margin-top:2rem; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
          <button onclick="triggerFlowerShower()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-weight:900; font-size:0.9rem; padding:10px 22px; border-radius:24px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:flex; align-items:center; gap:8px;">
            <span>🌸</span> पुष्प वर्षा करें
          </button>
          <button onclick="ringBell()" style="background:rgba(248,200,59,0.15); color:#92400E; border:1.5px solid #D97706; font-weight:800; font-size:0.9rem; padding:10px 22px; border-radius:24px; cursor:pointer; display:flex; align-items:center; gap:8px;">
            <span>🔔</span> घंटी बजाएं
          </button>
        </div>

      </div>
    `;
  }

  window.showPage('page-reader');
};

"""

app_js = app_js[:pos] + new_func + app_js[end_pos:]
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Successfully upgraded window.readChalisaItemDirect in app.js!")
