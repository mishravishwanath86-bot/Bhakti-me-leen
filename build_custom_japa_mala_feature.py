import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html for page-mala section & Custom Mantra Modal
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

rich_japa_page_html = """    <!-- 📿 INTERACTIVE DIGITAL JAPA MALA (WITH CUSTOM MANTRA CREATOR) 📿 -->
    <section id="page-mala" class="page">
      <div class="page-header-bar">
        <button class="back-btn" onclick="showPage('page-home')">←</button>
        <h2>📿 डिजिटल नाम जाप माला</h2>
        <div style="display:flex; align-items:center; gap:8px;">
          <button class="katha-search-btn" onclick="openCustomMantraCreatorModal()" title="नया मंत्र जोड़ें (Add Custom Mantra)">✨➕</button>
          <button class="katha-search-btn" onclick="resetJapaMala()" title="माला रीसेट करें">🔄</button>
        </div>
      </div>

      <div style="background:linear-gradient(145deg, #2D1047 0%, #170529 60%, #0B0116 100%); border-radius:26px; padding:1.4rem 1.1rem; margin: 0 0.8rem 1.2rem; border:1.5px solid #F59E0B; text-align:center; box-shadow:0 12px 35px rgba(0,0,0,0.7), 0 0 15px rgba(248,200,59,0.12) inset; position:relative; overflow:hidden;">
        
        <!-- Header Tag & Custom Mantra CTA Button -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.18); border:1px solid #F8C83B; padding:4px 12px; border-radius:14px; font-size:0.75rem; font-weight:900; color:#FDE68A;">
            <span>🕉️</span> <span id="japa-target-bead-tag">108 मनका पावन साधना</span>
          </div>
          <button onclick="openCustomMantraCreatorModal()" style="background:linear-gradient(135deg, #EC4899 0%, #BE185D 100%); color:#FFF; border:none; font-size:0.75rem; font-weight:900; padding:5px 12px; border-radius:12px; cursor:pointer; display:flex; align-items:center; gap:4px; box-shadow:0 3px 10px rgba(236,72,153,0.35);">
            <span>✨</span> + अपना मंत्र जोड़ें
          </button>
        </div>

        <!-- Horizontal Scrolling Quick-Switch Mantra Chips -->
        <div id="japa-mantra-chips-scroll" style="display:flex; align-items:center; gap:8px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none; -webkit-overflow-scrolling:touch;">
          <!-- Dynamically populated via renderJapaMantraChips() -->
        </div>

        <!-- Big Sacred Mantra Display Box -->
        <div style="background:rgba(255,255,255,0.05); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 14px; margin-bottom:14px;">
          <div id="japa-mantra-title" style="font-size:0.85rem; font-weight:900; color:#F8C83B; margin-bottom:4px;">
            🌸 हरे कृष्ण महामंत्र
          </div>
          <div id="japa-mantra-text" style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.15rem; font-weight:700; color:#FFFDF8; line-height:1.5; min-height:2.6rem; display:flex; align-items:center; justify-content:center; text-shadow:0 0 15px rgba(248,200,59,0.3);">
            हरे कृष्ण हरे कृष्ण कृष्ण कृष्ण हरे हरे । हरे राम हरे राम राम राम हरे हरे ॥
          </div>
        </div>

        <!-- Circular 108 Progress Counter (Interactive Mala Ring) -->
        <div class="mala-ring-container" onclick="incrementJapaMala()" style="position:relative; width:220px; height:220px; margin:0 auto 1.2rem; cursor:pointer; user-select:none; -webkit-user-select:none;">
          <svg class="mala-bead-svg" viewBox="0 0 240 240" style="width:100%; height:100%; transform:rotate(-90deg);">
            <defs>
              <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#FDE68A" />
                <stop offset="50%" stop-color="#F8C83B" />
                <stop offset="100%" stop-color="#D97706" />
              </linearGradient>
            </defs>
            <circle cx="120" cy="120" r="100" stroke="rgba(255,255,255,0.1)" stroke-width="12" fill="transparent"></circle>
            <circle id="mala-circle-bar" cx="120" cy="120" r="100" stroke="url(#goldGradient)" stroke-width="12" stroke-linecap="round" fill="transparent" stroke-dasharray="628.3" stroke-dashoffset="628.3" style="transition:stroke-dashoffset 0.15s ease;"></circle>
          </svg>
          <div class="mala-center-count" style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; pointer-events:none;">
            <div class="mala-num" id="mala-count-display" style="font-size:3.2rem; font-weight:900; color:#FFFDF8; line-height:1; font-family:'Tiro Devanagari Hindi', serif; text-shadow:0 0 20px rgba(248,200,59,0.6);">0</div>
            <div class="mala-target" id="mala-target-subtext" style="font-size:0.8rem; font-weight:800; color:#FDE68A; margin-top:4px;">/ 108 मनके</div>
          </div>
        </div>

        <!-- Mala Count & Completed Malas -->
        <div style="display:flex; justify-content:center; gap:12px; margin-bottom:1.2rem;">
          <div style="background:rgba(248,200,59,0.15); border:1.2px solid #F8C83B; border-radius:16px; padding:8px 16px; flex:1; max-width:145px;">
            <span style="font-size:0.75rem; color:#FDE68A; font-weight:800; display:block;">पूर्ण मालाएं:</span>
            <strong id="mala-completed-total" style="font-size:1.3rem; color:#FFFDF8; font-weight:900;">0</strong>
          </div>
          <div style="background:rgba(236,72,153,0.15); border:1.2px solid #F472B6; border-radius:16px; padding:8px 16px; flex:1; max-width:145px;">
            <span style="font-size:0.75rem; color:#FBCFE8; font-weight:800; display:block;">कुल जाप संख्या:</span>
            <strong id="mala-total-chants" style="font-size:1.3rem; color:#FFFDF8; font-weight:900;">0</strong>
          </div>
        </div>

        <!-- Giant Chanting Tap Button -->
        <button id="japa-giant-tap-btn" onclick="incrementJapaMala()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; font-weight:900; font-size:1.15rem; padding:15px 0; border-radius:24px; border:none; cursor:pointer; box-shadow:0 6px 25px rgba(248,200,59,0.5); width:100%; max-width:330px; transition:transform 0.08s ease; display:flex; align-items:center; justify-content:center; gap:8px; margin:0 auto;" onmousedown="this.style.transform='scale(0.95)'" onmouseup="this.style.transform='scale(1)'">
          <span style="font-size:1.35rem;">📿</span> <span>जाप करें (Tap to Chant)</span>
        </button>
      </div>
      <div style="height:6rem"></div>
    </section>

    <!-- ✨ CUSTOM MANTRA CREATOR MODAL ✨ -->
    <div id="custom-mantra-creator-modal" style="display:none; position:fixed; inset:0; z-index:100090; background:rgba(10,2,18,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
      <div style="width:100%; max-width:390px; background:linear-gradient(160deg, #2D1047 0%, #1A052E 60%, #0F021B 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.6rem 1.4rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.9); position:relative; animation:fadeInUp 0.25s ease;">
        
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="font-size:1.15rem; font-weight:900; color:#F8C83B; display:flex; align-items:center; gap:6px;">
            <span>✨</span> अपना व्यक्तिगत मंत्र जोड़ें
          </div>
          <button onclick="closeCustomMantraCreatorModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:30px; height:30px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>

        <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 14px 0; line-height:1.4;">
          अपना इष्ट मंत्र, गुरु मंत्र या पावन नाम दर्ज करें और माला जाप आरंभ करें:
        </p>

        <!-- Input 1: Title / Name -->
        <div style="margin-bottom:12px;">
          <label style="font-size:0.78rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            मंत्र / नाम शीर्षक (Short Title):
          </label>
          <input type="text" id="custom-mantra-title-input" placeholder="उदा. राधे राधे, श्री सीताराम, गुरु मंत्र" style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); border-radius:14px; padding:10px 14px; color:#FFFDF8; font-size:0.9rem; font-weight:700; outline:none; box-sizing:border-box;">
        </div>

        <!-- Input 2: Full Mantra Text -->
        <div style="margin-bottom:12px;">
          <label style="font-size:0.78rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            सम्पूर्ण मंत्र पाठ (Full Mantra Text):
          </label>
          <textarea id="custom-mantra-text-input" rows="3" placeholder="उदा. ॥ श्री राधा वल्लभ विजयते नमः ॥" style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); border-radius:14px; padding:10px 14px; color:#FFFDF8; font-size:0.9rem; font-weight:700; outline:none; box-sizing:border-box; resize:none; font-family:'Tiro Devanagari Hindi', serif;"></textarea>
        </div>

        <!-- Input 3: Bead Count Selector -->
        <div style="margin-bottom:14px;">
          <label style="font-size:0.78rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:6px;">
            मनका संख्या लक्ष्य (Beads Target):
          </label>
          <div style="display:flex; gap:6px;">
            <button type="button" onclick="selectCustomBeadTarget(108, this)" class="custom-bead-target-btn active" style="flex:1; padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; text-align:center;">
              108 मनके ⭐
            </button>
            <button type="button" onclick="selectCustomBeadTarget(54, this)" class="custom-bead-target-btn" style="flex:1; padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
              54 मनके
            </button>
            <button type="button" onclick="selectCustomBeadTarget(27, this)" class="custom-bead-target-btn" style="flex:1; padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
              27 मनके
            </button>
            <button type="button" onclick="selectCustomBeadTarget(1008, this)" class="custom-bead-target-btn" style="flex:1; padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
              1008
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button onclick="saveCustomMantraAndStart()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:flex; align-items:center; justify-content:center; gap:6px;">
          <span>💾</span> सहेजें और जाप शुरू करें ➔
        </button>

      </div>
    </div>
"""

# Replace in index.html
s_mala = html.find('<!-- 📿 INTERACTIVE DIGITAL JAPA MALA')
if s_mala != -1:
    e_mala = html.find('<!-- 🪔 VIRTUAL AARTI & TEMPLE DARSHAN STAGE', s_mala)
    html = html[:s_mala] + rich_japa_page_html + "\n\n    " + html[e_mala:]

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with Custom Mantra Creator Modal & Quick-Switch Chips (v={ts})")

# 2. Update app.js with Full Custom Mantra Engine
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

japa_mala_engine_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 📿 DIGITAL NAAM JAAP MALA & CUSTOM MANTRA ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.selectedCustomBeadTarget = 108;
window.currentMalaTarget = 108;
window.currentMalaCount = 0;

window.DEFAULT_PRESET_MANTRAS = [
  { id: 'hare_krishna', name: '🌸 हरे कृष्ण', text: 'हरे कृष्ण हरे कृष्ण कृष्ण कृष्ण हरे हरे । हरे राम हरे राम राम राम हरे हरे ॥', target: 108, color: '#EC4899' },
  { id: 'om_namah_shivaya', name: '🔱 ॐ नमः शिवाय', text: '॥ ॐ नमः शिवाय ॥', target: 108, color: '#3B82F6' },
  { id: 'shree_ram', name: '🚩 श्री राम', text: '॥ श्री राम जय राम जय जय राम ॥', target: 108, color: '#F97316' },
  { id: 'ganesh_mantra', name: '🐘 ॐ गं गणपतये', text: '॥ ॐ गं गणपतये नमः ॥', target: 108, color: '#EF4444' },
  { id: 'gayatri_mantra', name: '🪔 गायत्री महामंत्र', text: '॥ ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात् ॥', target: 108, color: '#F59E0B' },
  { id: 'mahamrityunjaya', name: '🕉️ महामृत्युंजय', text: '॥ ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय माऽमृतात् ॥', target: 108, color: '#8B5CF6' },
  { id: 'radha_krishna', name: '🌺 राधे राधे', text: '॥ श्री राधा वल्लभ विजयते नमः ॥', target: 108, color: '#F472B6' }
];

window.activeMantra = window.DEFAULT_PRESET_MANTRAS[0];

// Load Custom Mantras from LocalStorage
window.getStoredCustomMantras = function() {
  try {
    const raw = localStorage.getItem('sanatan_custom_mantras');
    return raw ? JSON.parse(raw) : [];
  } catch(e) {
    return [];
  }
};

window.saveStoredCustomMantras = function(list) {
  try {
    localStorage.setItem('sanatan_custom_mantras', JSON.stringify(list));
  } catch(e) {}
};

// Render Chips Strip
window.renderJapaMantraChips = function() {
  const container = document.getElementById('japa-mantra-chips-scroll');
  if (!container) return;

  const customList = window.getStoredCustomMantras();
  const allMantras = [...window.DEFAULT_PRESET_MANTRAS, ...customList];

  let html = '';
  allMantras.forEach((m) => {
    const isActive = m.id === window.activeMantra.id;
    const bg = isActive ? 'linear-gradient(135deg, #F8C83B, #D97706)' : 'rgba(255,255,255,0.08)';
    const color = isActive ? '#1A0B2E' : '#CBD5E1';
    const border = isActive ? 'none' : '1px solid rgba(255,255,255,0.15)';
    const shadow = isActive ? '0 0 12px rgba(248,200,59,0.45)' : 'none';

    html += `
      <div style="display:flex; align-items:center; background:${bg}; color:${color}; border:${border}; border-radius:14px; padding:6px 12px; font-size:0.78rem; font-weight:800; cursor:pointer; white-space:nowrap; box-shadow:${shadow}; flex-shrink:0; transition:all 0.15s ease;" onclick="selectJapaMantraById('${m.id}')">
        <span>${m.name}</span>
        ${m.isCustom ? `<span onclick="event.stopPropagation(); deleteCustomMantra('${m.id}')" title="हटाएं" style="margin-left:6px; font-size:0.75rem; opacity:0.8; padding:0 3px; border-radius:4px; background:rgba(0,0,0,0.2);">✕</span>` : ''}
      </div>
    `;
  });

  // Add + Create Button chip
  html += `
    <div onclick="openCustomMantraCreatorModal()" style="display:flex; align-items:center; gap:4px; background:rgba(236,72,153,0.2); color:#FBCFE8; border:1px dashed #F472B6; border-radius:14px; padding:6px 12px; font-size:0.78rem; font-weight:800; cursor:pointer; white-space:nowrap; flex-shrink:0;">
      <span>➕</span> नया मंत्र जोड़ें
    </div>
  `;

  container.innerHTML = html;
};

window.selectJapaMantraById = function(id) {
  const customList = window.getStoredCustomMantras();
  const allMantras = [...window.DEFAULT_PRESET_MANTRAS, ...customList];
  const found = allMantras.find(m => m.id === id);

  if (found) {
    window.activeMantra = found;
    window.currentMalaTarget = found.target || 108;
    
    // Update Display Box
    const titleEl = document.getElementById('japa-mantra-title');
    const textEl = document.getElementById('japa-mantra-text');
    const tagEl = document.getElementById('japa-target-bead-tag');
    const subtextEl = document.getElementById('mala-target-subtext');

    if (titleEl) titleEl.textContent = found.name;
    if (textEl) textEl.textContent = found.text;
    if (tagEl) tagEl.textContent = `${window.currentMalaTarget} मनका पावन साधना`;
    if (subtextEl) subtextEl.textContent = `/ ${window.currentMalaTarget} मनके`;

    window.renderJapaMantraChips();
    window.updateMalaCircleProgress();

    if (typeof showToast === 'function') {
      showToast(`📿 चयनित: ${found.name}`);
    }
  }
};

window.incrementJapaMala = function() {
  window.currentMalaCount++;

  // Haptic feedback
  if (navigator.vibrate) navigator.vibrate(25);

  // Bead Click Sound
  if (typeof playSoundEffect === 'function') {
    playSoundEffect('correct');
  }

  // Update Total Chants
  let totalChants = parseInt(localStorage.getItem('sanatan_total_japa_chants') || '0');
  totalChants++;
  localStorage.setItem('sanatan_total_japa_chants', totalChants.toString());

  // Update UI Displays
  const countEl = document.getElementById('mala-count-display');
  if (countEl) countEl.textContent = window.currentMalaCount;

  const totalEl = document.getElementById('mala-total-chants');
  if (totalEl) totalEl.textContent = totalChants;

  window.updateMalaCircleProgress();

  // Check 1 Mala Completion (108 or custom target)
  if (window.currentMalaCount >= window.currentMalaTarget) {
    window.currentMalaCount = 0;
    if (countEl) countEl.textContent = '0';
    window.updateMalaCircleProgress();

    let completedMalas = parseInt(localStorage.getItem('sanatan_completed_malas') || '0');
    completedMalas++;
    localStorage.setItem('sanatan_completed_malas', completedMalas.toString());

    const malTotEl = document.getElementById('mala-completed-total');
    if (malTotEl) malTotEl.textContent = completedMalas;

    // Victory Celebration
    if (typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
    }
    if (typeof playSoundEffect === 'function') {
      playSoundEffect('victory');
    }

    if (typeof showToast === 'function') {
      showToast(`📿 पावन ${completedMalas}वीं माला पूर्ण हुई! प्रभु कृपा बरसे (+10 साधना अंक)`);
    }
  }
};

window.updateMalaCircleProgress = function() {
  const circle = document.getElementById('mala-circle-bar');
  if (circle) {
    const circumference = 2 * Math.PI * 100; // 628.3
    const progress = Math.min(1, window.currentMalaCount / window.currentMalaTarget);
    const offset = circumference - (progress * circumference);
    circle.style.strokeDashoffset = offset;
  }
};

window.resetJapaMala = function() {
  window.currentMalaCount = 0;
  const countEl = document.getElementById('mala-count-display');
  if (countEl) countEl.textContent = '0';
  window.updateMalaCircleProgress();
  if (typeof showToast === 'function') {
    showToast('🔄 माला मनका 0 पर रीसेट किया गया');
  }
};

// Modal Handlers
window.openCustomMantraCreatorModal = function() {
  const modal = document.getElementById('custom-mantra-creator-modal');
  if (modal) modal.style.display = 'flex';
  const titleInp = document.getElementById('custom-mantra-title-input');
  if (titleInp) titleInp.focus();
};

window.closeCustomMantraCreatorModal = function() {
  const modal = document.getElementById('custom-mantra-creator-modal');
  if (modal) modal.style.display = 'none';
};

window.selectCustomBeadTarget = function(target, btnEl) {
  window.selectedCustomBeadTarget = target;
  document.querySelectorAll('.custom-bead-target-btn').forEach(b => {
    b.classList.remove('active');
    b.style.background = 'rgba(255,255,255,0.08)';
    b.style.color = '#CBD5E1';
    b.style.border = '1px solid rgba(255,255,255,0.15)';
  });

  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
  }
};

window.saveCustomMantraAndStart = function() {
  const titleInp = document.getElementById('custom-mantra-title-input');
  const textInp = document.getElementById('custom-mantra-text-input');

  const title = (titleInp ? titleInp.value : '').trim();
  const text = (textInp ? textInp.value : '').trim();

  if (!title) {
    if (typeof showToast === 'function') showToast('⚠️ कृपया मंत्र का नाम / शीर्षक दर्ज करें');
    return;
  }

  const customObj = {
    id: 'custom_' + Date.now(),
    name: '✨ ' + title,
    text: text || title,
    target: window.selectedCustomBeadTarget || 108,
    isCustom: true,
    color: '#F8C83B'
  };

  const list = window.getStoredCustomMantras();
  list.push(customObj);
  window.saveStoredCustomMantras(list);

  // Clear inputs & close
  if (titleInp) titleInp.value = '';
  if (textInp) textInp.value = '';
  window.closeCustomMantraCreatorModal();

  // Select newly created custom mantra & start chanting!
  window.selectJapaMantraById(customObj.id);

  if (typeof showToast === 'function') {
    showToast(`✨ आपका नया मंत्र '${title}' सहेजा गया! जाप आरंभ करें 📿`);
  }
};

window.deleteCustomMantra = function(id) {
  let list = window.getStoredCustomMantras();
  list = list.filter(m => m.id !== id);
  window.saveStoredCustomMantras(list);

  if (window.activeMantra.id === id) {
    window.selectJapaMantraById(window.DEFAULT_PRESET_MANTRAS[0].id);
  } else {
    window.renderJapaMantraChips();
  }

  if (typeof showToast === 'function') {
    showToast('🗑️ कस्टम मंत्र हटाया गया');
  }
};

// Initialize Mala Page on startup
document.addEventListener('DOMContentLoaded', function() {
  window.renderJapaMantraChips();
  const malTotEl = document.getElementById('mala-completed-total');
  if (malTotEl) {
    malTotEl.textContent = localStorage.getItem('sanatan_completed_malas') || '0';
  }
  const totEl = document.getElementById('mala-total-chants');
  if (totEl) {
    totEl.textContent = localStorage.getItem('sanatan_total_japa_chants') || '0';
  }
});
"""

# Replace in app.js
if 'window.incrementJapaMala' in js:
    js = js[:js.find('window.incrementJapaMala')] + japa_mala_engine_js + "\n\n" + js[js.find('window.incrementJapaMala') + 120:]
else:
    js += "\n\n" + japa_mala_engine_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"✓ Updated app.js with Digital Naam Jaap Mala Engine & Custom Mantra Creator (v={ts})")
