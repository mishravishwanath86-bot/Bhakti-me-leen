import sys, re, time, json, sqlite3

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🪔 IMPLEMENTING COMPLETE AARTI STAGE SOUND & INTERACTION ENGINE")
print("======================================================================")

# 1. Fetch curated Aarti items from database
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
        'deity': r[1] or 'general',
        'title': r[2],
        'desc': r[3] or 'पावन वैदिक नित्य महाआरती',
        'audio': r[4] or 'assets/audio/bhajan_achyutam_keshavam.mp3',
        'thumb': r[5] or 'assets/gallery/bal_ganesha_little.jpg'
    })
conn.close()

print(f"✓ Loaded {len(aarti_db_items)} curated Aarti items from DB")

aarti_dataset_json = json.dumps(aarti_db_items, ensure_ascii=False)

# 2. Append CSS animations for Aarti stage in styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

aarti_stage_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🪔 VIRTUAL DIVINE AARTI STAGE & FLOWER SHOWER ANIMATIONS
   ══════════════════════════════════════════════════════════════════════════════ */

@keyframes spinDisc {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes spinDiscReverse {
  0% { transform: rotate(360deg); }
  100% { transform: rotate(0deg); }
}

@keyframes bellSwing {
  0% { transform: rotate(0deg); }
  20% { transform: rotate(18deg); }
  40% { transform: rotate(-18deg); }
  60% { transform: rotate(12deg); }
  80% { transform: rotate(-8deg); }
  100% { transform: rotate(0deg); }
}

@keyframes conchPulse {
  0% { transform: scale(1); filter: drop-shadow(0 0 5px #F472B6); }
  50% { transform: scale(1.15) rotate(-5deg); filter: drop-shadow(0 0 20px #EC4899); }
  100% { transform: scale(1); filter: drop-shadow(0 0 5px #F472B6); }
}

@keyframes fallingPetal {
  0% {
    opacity: 1;
    transform: translate3d(0, -20px, 0) rotate(0deg) scale(0.8);
  }
  70% {
    opacity: 0.9;
  }
  100% {
    opacity: 0;
    transform: translate3d(var(--drift-x, 40px), 100vh, 0) rotate(var(--rot, 360deg)) scale(1.2);
  }
}
"""

if 'VIRTUAL DIVINE AARTI STAGE & FLOWER SHOWER ANIMATIONS' in css:
    css = re.sub(r'/\* ══════════════════════════════════════════════════════════════════════════════\s*🪔 VIRTUAL DIVINE AARTI STAGE & FLOWER SHOWER ANIMATIONS[\s\S]*', '', css)

css += '\n\n' + aarti_stage_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Appended Aarti Stage CSS & Animations to styles.css")

# 3. Add complete Audio Synthesizer, Bell, Conch, Flower Shower & Aarti Stage Controller in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

aarti_complete_js = f"""
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 SACRED AUDIO SYNTHESIZER: TEMPLE BELL, SHANKH & FLOWER SHOWER ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.spiritualAudioCtx = null;

window.getSpiritualAudioContext = function() {{
  if (!window.spiritualAudioCtx) {{
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {{
      window.spiritualAudioCtx = new AudioCtx();
    }}
  }}
  if (window.spiritualAudioCtx && window.spiritualAudioCtx.state === 'suspended') {{
    window.spiritualAudioCtx.resume();
  }}
  return window.spiritualAudioCtx;
}};

// 1. Realistic Resonant Temple Bell Synthesizer (पावन घंटा नाद)
window.playBellSound = function() {{
  try {{
    const ctx = window.getSpiritualAudioContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    
    // Fundamental & Harmonics of a resonant brass temple bell
    const harmonics = [
      {{ freq: 1046.5, gain: 0.5, decay: 2.8 }}, // C6
      {{ freq: 2093.0, gain: 0.35, decay: 2.2 }}, // C7
      {{ freq: 2793.8, gain: 0.25, decay: 1.8 }}, // F7
      {{ freq: 4186.0, gain: 0.18, decay: 1.4 }}, // C8
      {{ freq: 5587.6, gain: 0.10, decay: 0.9 }}  // F8
    ];

    const masterGain = ctx.createGain();
    masterGain.gain.setValueAtTime(0.7, now);
    masterGain.connect(ctx.destination);

    harmonics.forEach(h => {{
      const osc = ctx.createOscillator();
      const g = ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(h.freq, now);

      g.gain.setValueAtTime(h.gain, now);
      g.gain.exponentialRampToValueAtTime(0.0001, now + h.decay);

      osc.connect(g);
      g.connect(masterGain);

      osc.start(now);
      osc.stop(now + h.decay + 0.1);
    }});
  }} catch(e) {{
    console.error('Bell sound error:', e);
  }}
}};

// 2. Powerful Deep Sacred Conch Shell Synthesizer (दिव्य शंखनाद)
window.playConchSound = function() {{
  try {{
    const ctx = window.getSpiritualAudioContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    const duration = 3.2;

    const masterGain = ctx.createGain();
    masterGain.gain.setValueAtTime(0.001, now);
    masterGain.gain.linearRampToValueAtTime(0.65, now + 0.6); // Swell
    masterGain.gain.exponentialRampToValueAtTime(0.0001, now + duration);
    masterGain.connect(ctx.destination);

    // Resonant Lowpass Filter for natural hollow horn resonance
    const filter = ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(450, now);
    filter.frequency.linearRampToValueAtTime(750, now + 0.5);
    filter.frequency.exponentialRampToValueAtTime(300, now + duration);
    filter.Q.setValueAtTime(4.5, now);
    filter.connect(masterGain);

    // Detuned rich harmonic stack
    const freqs = [220, 222, 440, 660, 880];
    freqs.forEach((f, idx) => {{
      const osc = ctx.createOscillator();
      osc.type = idx % 2 === 0 ? 'sawtooth' : 'triangle';
      
      // Pitch bend upwards at start (natural horn blowing technique)
      osc.frequency.setValueAtTime(f * 0.92, now);
      osc.frequency.linearRampToValueAtTime(f * 1.02, now + 0.4);
      osc.frequency.linearRampToValueAtTime(f, now + 0.8);

      const oscGain = ctx.createGain();
      oscGain.gain.setValueAtTime(1.0 / (idx + 1.2), now);

      osc.connect(oscGain);
      oscGain.connect(filter);

      osc.start(now);
      osc.stop(now + duration + 0.1);
    }});
  }} catch(e) {{
    console.error('Conch sound error:', e);
  }}
}};

// 3. Bell Ring Action Button Controller
window.ringTempleBell = function() {{
  if (typeof window.duckRadioAudio === 'function') window.duckRadioAudio(3000);
  window.playBellSound();

  const bellBtn = event && event.target ? event.target.closest('button') : null;
  if (bellBtn) {{
    bellBtn.style.animation = 'bellSwing 0.8s ease';
    setTimeout(() => {{ bellBtn.style.animation = ''; }}, 850);
  }}

  if (navigator.vibrate) navigator.vibrate([40, 60, 40]);
  if (typeof showToast === 'function') {{
    showToast('🔔 पावन घंटा नाद... ॐ नमः शिवाय!');
  }}
}};

// 4. Conch Blow Action Button Controller
window.blowTempleConch = function() {{
  if (typeof window.duckRadioAudio === 'function') window.duckRadioAudio(4000);
  window.playConchSound();

  const conchBtn = event && event.target ? event.target.closest('button') : null;
  if (conchBtn) {{
    conchBtn.style.animation = 'conchPulse 1.2s ease';
    setTimeout(() => {{ conchBtn.style.animation = ''; }}, 1250);
  }}

  if (navigator.vibrate) navigator.vibrate([80, 50, 120]);
  if (typeof showToast === 'function') {{
    showToast('🐚 पावन शंखनाद... जय श्री राम!');
  }}
}};

// 5. Flower Shower (पुष्प वर्षा) Cascading Particle System
window.triggerFlowerShower = function() {{
  try {{
    // Play floral chime harp sparkle
    const ctx = window.getSpiritualAudioContext();
    if (ctx) {{
      const now = ctx.currentTime;
      const chimeFreqs = [523.25, 659.25, 783.99, 1046.50, 1318.51, 1567.98];
      chimeFreqs.forEach((cf, i) => {{
        const osc = ctx.createOscillator();
        const g = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(cf, now + (i * 0.06));
        g.gain.setValueAtTime(0.18, now + (i * 0.06));
        g.gain.exponentialRampToValueAtTime(0.0001, now + (i * 0.06) + 0.6);
        osc.connect(g);
        g.connect(ctx.destination);
        osc.start(now + (i * 0.06));
        osc.stop(now + (i * 0.06) + 0.7);
      }});
    }}
  }} catch(e) {{}}

  let container = document.getElementById('flower-shower-container');
  if (!container) {{
    container = document.createElement('div');
    container.id = 'flower-shower-container';
    container.style.cssText = 'position:fixed; inset:0; pointer-events:none; z-index:999990; overflow:hidden;';
    document.body.appendChild(container);
  }}

  const petals = ['🌹', '🌸', '🌺', '🪷', '🌼', '🏵️', '✨', '💐'];
  const count = 36;

  for (let i = 0; i < count; i++) {{
    setTimeout(() => {{
      const petal = document.createElement('div');
      const char = petals[Math.floor(Math.random() * petals.length)];
      const startX = Math.random() * 96; // vw
      const size = 18 + Math.random() * 22; // px
      const dur = 2.2 + Math.random() * 2.0; // sec
      const drift = -80 + Math.random() * 160; // px
      const rot = 180 + Math.random() * 540; // deg

      petal.style.cssText = `
        position: absolute;
        top: -30px;
        left: ${{startX}}vw;
        font-size: ${{size}}px;
        filter: drop-shadow(0 0 8px rgba(248,200,59,0.7));
        animation: fallingPetal ${{dur}}s ease-out forwards;
        --drift-x: ${{drift}}px;
        --rot: ${{rot}}deg;
      `;
      petal.textContent = char;

      container.appendChild(petal);

      setTimeout(() => {{
        if (petal.parentNode) petal.parentNode.removeChild(petal);
      }}, dur * 1000 + 200);
    }}, i * 45);
  }}

  if (navigator.vibrate) navigator.vibrate([30, 40, 50]);
  if (typeof showToast === 'function') {{
    showToast('🌸 प्रभु चरणों में पावन पुष्प वर्षा!');
  }}
}};

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
  if (typeof window.playUserUploadedBhajan === 'function') {{
    window.playUserUploadedBhajan({{
      title: item.title,
      sub: item.desc,
      src: item.audio
    }});
  }} else {{
    let audio = document.getElementById('core-app-audio');
    if (!audio) {{
      audio = new Audio();
      audio.id = 'core-app-audio';
      document.body.appendChild(audio);
    }}
    audio.src = item.audio;
    audio.play().catch(e => console.log('Audio autoplay prevented:', e));
  }}

  if (typeof window.triggerFlowerShower === 'function') window.triggerFlowerShower();

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

window.openAartiReader = function(aartiId) {{
  const item = window.DIVINE_AARTI_DATASET.find(x => x.id === aartiId);
  if (!item) return;

  if (typeof window.openContentItemReader === 'function') {{
    window.openContentItemReader(aartiId);
  }} else if (typeof window.showPage === 'function') {{
    window.playAartiItemDirect(aartiId);
  }}
}};

// Initialize Aarti Stage Cards on page load
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => window.renderAartiStageCards('all'));
}} else {{
  window.renderAartiStageCards('all');
}}
"""

# Replace in app.js
if 'SACRED AUDIO SYNTHESIZER: TEMPLE BELL, SHANKH & FLOWER SHOWER ENGINE' in app_js:
    app_js = re.sub(r'// ══════════════════════════════════════════════════════════════════════════════\s*// 🪔 SACRED AUDIO SYNTHESIZER[\s\S]*', '', app_js)

app_js += '\n\n' + aarti_complete_js

ts = int(time.time())
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("✓ Updated app.js with complete Aarti Stage & Sound Synthesizer Engine")

# Update index.html cache busters
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Updated index.html cache buster")
print("✓ Aarti Stage Sound & Interaction Engine fully synchronized!")
