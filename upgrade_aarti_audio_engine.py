import sys, re, json, os

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html to add Aarti Live Playback Bar and persistent audio container
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_anchor = '<button onclick="start3DMandirParikramaFlow()"'
pos = html.find(target_anchor)
if pos == -1:
    print("Error: start3DMandirParikramaFlow button not found in index.html")
    sys.exit(1)

btn_end = html.find('</button>', pos) + len('</button>')
div_end = html.find('</div>', btn_end) # end of the hero stage button container

new_playback_bar_html = """
          <!-- 🎵 ACTIVE AARTI PLAYING BAR (NOW PLAYING & CONTROLS) 🎵 -->
          <div id="aarti-live-playback-bar" style="display:none; margin-top:12px; background:linear-gradient(135deg, rgba(248,200,59,0.2) 0%, rgba(217,119,6,0.12) 100%); border:1.5px solid #F8C83B; border-radius:18px; padding:10px 14px; align-items:center; justify-content:space-between; box-shadow:0 0 20px rgba(248,200,59,0.25); animation:pulseGlow 2s infinite;">
            <div style="display:flex; align-items:center; gap:10px; flex:1; min-width:0; text-align:left;">
              <div style="width:10px; height:10px; border-radius:50%; background:#10B981; box-shadow:0 0 10px #10B981; flex-shrink:0;"></div>
              <div style="flex:1; min-width:0;">
                <div style="font-size:0.68rem; color:#FDE68A; font-weight:800; text-transform:uppercase; letter-spacing:0.5px;">🔴 अब बज रहा है (Playing Now)</div>
                <div id="aarti-live-playing-title" style="font-size:0.86rem; font-weight:900; color:#FFFDF8; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">आरती श्री गणेश जी</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:6px; flex-shrink:0;">
              <button onclick="toggleAartiPlayPause()" id="aarti-bar-playpause-btn" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; border-radius:12px; font-size:0.82rem; font-weight:900; padding:6px 12px; cursor:pointer; display:flex; align-items:center; gap:4px;">
                ⏸️ रोकें
              </button>
              <button onclick="openCurrentAartiReader()" title="आरती पाठ पढ़ें" style="background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; border-radius:12px; font-size:0.82rem; padding:6px 10px; cursor:pointer;">
                📖
              </button>
              <button onclick="openGlassPlayer()" title="फुल स्क्रीन प्लेयर खोलें" style="background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; border-radius:12px; font-size:0.82rem; padding:6px 10px; cursor:pointer;">
                🔍
              </button>
            </div>
          </div>

          <!-- Hidden Persistent YouTube Audio Player Container for Aarti Stage -->
          <div id="aarti-stage-youtube-container" style="position:absolute; top:-9999px; left:-9999px; width:1px; height:1px; opacity:0.01; pointer-events:none;"></div>"""

if 'id="aarti-live-playback-bar"' not in html:
    html = html[:div_end + len('</div>')] + new_playback_bar_html + html[div_end + len('</div>'):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Added aarti-live-playback-bar and container to index.html")
else:
    print("aarti-live-playback-bar already in index.html")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Locate DIVINE_AARTI_DATASET and the whole aarti stage engine
target = 'window.DIVINE_AARTI_DATASET = ['
start = js.find('// 🪔 DYNAMIC VIRTUAL AARTI & TEMPLE DARSHAN STAGE ENGINE')
if start == -1:
    start = js.find(target)

end_marker = '// 🌐 GOOGLE 1-TAP & OAUTH LOGIN / SIGN-UP CONTROLLER ENGINE'
end = js.find(end_marker)
if end == -1:
    end = js.find('window.openGoogleAccountPickerModal')
    end = js.rfind('// ══════', 0, end)

print(f"Replacing Aarti Stage engine in app.js from {start} to {end}")

# Load and fix dataset
dataset_match = re.search(r'window\.DIVINE_AARTI_DATASET\s*=\s*(\[.*?\]);', js, re.DOTALL)
items = json.loads(dataset_match.group(1))

# Fix missing files
for item in items:
    if item.get('id') == 'aarti-ram-shri-ramchandra-kripalu':
        item['audio'] = 'assets/audio/katha_ramayana.mp3'
    elif item.get('id') == 'aarti-shiva-karpur-gauram-karunavataram':
        item['audio'] = 'https://www.youtube.com/watch?v=5tZKyk5Bne4'

dataset_json_str = json.dumps(items, ensure_ascii=False)

new_aarti_engine_js = f"""// ══════════════════════════════════════════════════════════════════════════════
// 🪔 DYNAMIC VIRTUAL AARTI & TEMPLE DARSHAN STAGE ENGINE (UNIVERSAL AUDIO)
// ══════════════════════════════════════════════════════════════════════════════

window.DIVINE_AARTI_DATASET = {dataset_json_str};
window.currentSelectedAartiItem = window.DIVINE_AARTI_DATASET[0] || null;
window.isThaliFastRotating = false;
window.isAartiPlaying = false;
window.activeAartiId = null;

// 1. Render Aarti Stage Cards with Play/Pause state and Filters
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
    const isThisActive = window.activeAartiId === item.id && window.isAartiPlaying;
    const card = document.createElement('div');
    card.id = `aarti-card-${{item.id}}`;
    card.style.cssText = `background:rgba(255,255,255,${{isThisActive ? '0.12' : '0.06'}}); border:1.5px solid ${{isThisActive ? '#F8C83B' : 'rgba(248,200,59,0.3)'}}; border-radius:20px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.3); transition:all 0.2s ease;`;

    card.innerHTML = `
      <div onclick="selectAartiForStage('${{item.id}}')" style="display:flex; align-items:center; gap:12px; flex:1; min-width:0; cursor:pointer;">
        <div style="width:48px; height:48px; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); padding:2px; flex-shrink:0; box-shadow:0 0 12px rgba(248,200,59,0.35);">
          <img src="${{item.thumb}}" style="width:100%; height:100%; border-radius:12px; object-fit:cover;" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" />
        </div>
        <div style="flex:1; min-width:0;">
          <div style="font-size:0.92rem; font-weight:900; color:#FFFDF8; line-height:1.3; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
            ${{item.title}}
          </div>
          <div style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
            ${{item.desc}}
          </div>
        </div>
      </div>

      <div style="display:flex; align-items:center; gap:6px; flex-shrink:0;">
        <button id="aarti-play-btn-${{item.id}}" onclick="playAartiItemDirect('${{item.id}}')" title="${{isThisActive ? 'रोकें' : 'आरती सुनें'}}" class="aarti-card-play-btn" style="width:40px; height:40px; border-radius:50%; background:${{isThisActive ? '#10B981' : 'linear-gradient(135deg, #F8C83B, #D97706)'}}; border:none; color:${{isThisActive ? '#FFF' : '#1A0B2E'}}; font-size:1.05rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 12px rgba(248,200,59,0.4); transition:all 0.15s ease;">
          ${{isThisActive ? '⏸️' : '▶'}}
        </button>
        <button onclick="openAartiReader('${{item.id}}')" title="आरती पाठ पढ़ें" style="width:40px; height:40px; border-radius:50%; background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          📖
        </button>
      </div>
    `;

    grid.appendChild(card);
  }});
}};

// 2. Select Aarti to display on the central 3D Aarti Thali
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

  if (navigator.vibrate) navigator.vibrate(25);
}};

// 3. Play or Pause the Currently Selected Aarti from the Hero Stage Button
window.playCurrentSelectedAarti = function() {{
  if (window.isAartiPlaying) {{
    window.toggleAartiPlayPause();
  }} else {{
    const item = window.currentSelectedAartiItem || window.DIVINE_AARTI_DATASET[0];
    if (item) {{
      window.playAartiItemDirect(item.id);
    }}
  }}
}};

// 4. Universal Resilient Aarti Audio Player Engine (YouTube & Local MP3)
window.playAartiItemDirect = function(aartiId) {{
  const item = window.DIVINE_AARTI_DATASET.find(x => x.id === aartiId);
  if (!item) return;

  // If clicking on already playing item, toggle pause
  if (window.activeAartiId === aartiId && window.isAartiPlaying) {{
    window.toggleAartiPlayPause();
    return;
  }}

  window.activeAartiId = aartiId;
  window.selectAartiForStage(aartiId);

  // Update Live Playback Bar on Aarti Stage
  const liveBar = document.getElementById('aarti-live-playback-bar');
  const liveTitle = document.getElementById('aarti-live-playing-title');
  const playNowBtn = document.getElementById('aarti-play-now-btn');
  const barPlayBtn = document.getElementById('aarti-bar-playpause-btn');

  if (liveBar) liveBar.style.display = 'flex';
  if (liveTitle) liveTitle.textContent = item.title;
  if (playNowBtn) playNowBtn.innerHTML = '<span>⏸️</span> पावन महाआरती रोकें (Pause)';
  if (barPlayBtn) barPlayBtn.innerHTML = '⏸️ रोकें';

  // Fast Thali rotation & golden flame pulse
  const thali = document.getElementById('aarti-thali-disc');
  if (thali) thali.style.animation = 'spinDisc 6s linear infinite';
  const flame = document.getElementById('aarti-central-flame');
  if (flame) flame.style.filter = 'drop-shadow(0 0 25px #F59E0B)';

  // Update all card buttons in grid
  document.querySelectorAll('.aarti-card-play-btn').forEach(btn => {{
    btn.innerHTML = '▶';
    btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btn.style.color = '#1A0B2E';
  }});
  document.querySelectorAll('[id^="aarti-card-"]').forEach(c => {{
    c.style.background = 'rgba(255,255,255,0.06)';
    c.style.borderColor = 'rgba(248,200,59,0.3)';
  }});

  const activeCard = document.getElementById(`aarti-card-${{aartiId}}`);
  if (activeCard) {{
    activeCard.style.background = 'rgba(255,255,255,0.12)';
    activeCard.style.borderColor = '#F8C83B';
  }}
  const activeBtn = document.getElementById(`aarti-play-btn-${{aartiId}}`);
  if (activeBtn) {{
    activeBtn.innerHTML = '⏸️';
    activeBtn.style.background = '#10B981';
    activeBtn.style.color = '#FFF';
  }}

  const isYT = /(?:youtube\.com|youtu\.be)/i.test(item.audio);

  if (isYT) {{
    // ══════════════════════════════════════════════════════
    // A. YOUTUBE AUDIO STREAMING
    // ══════════════════════════════════════════════════════
    // 1. Stop local audio if playing
    if (window.coreAudioElement) window.coreAudioElement.pause();
    const ca = document.getElementById('core-app-audio');
    if (ca) ca.pause();

    // 2. Extract YouTube Video ID
    const match = item.audio.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\\w-]{{11}})/i);
    const videoId = match ? match[1] : null;

    if (videoId) {{
      let ytContainer = document.getElementById('aarti-stage-youtube-container');
      if (!ytContainer) {{
        ytContainer = document.createElement('div');
        ytContainer.id = 'aarti-stage-youtube-container';
        ytContainer.style.cssText = 'position:fixed; bottom:0; right:0; width:1px; height:1px; opacity:0.01; pointer-events:none; z-index:-1;';
        document.body.appendChild(ytContainer);
      }}

      // Load YouTube iframe in Pure Audio mode
      ytContainer.innerHTML = `
        <iframe 
          id="aarti-stage-yt-iframe"
          src="https://www.youtube-nocookie.com/embed/${{videoId}}?autoplay=1&enablejsapi=1&rel=0&playsinline=1"
          frameborder="0"
          allow="autoplay; encrypted-media"
          style="width:1px; height:1px;">
        </iframe>
      `;

      if (window.MediaRouter) {{
        window.MediaRouter.activeMode = 'youtube';
        window.MediaRouter.currentYouTubeId = videoId;
        window.MediaRouter.isYouTubePaused = false;
      }}
    }} else {{
      _playLocalAartiTrack('assets/audio/bhajan_achyutam_keshavam.mp3');
    }}
  }} else {{
    // ══════════════════════════════════════════════════════
    // B. LOCAL MP3 AUDIO PLAYBACK
    // ══════════════════════════════════════════════════════
    const ytContainer = document.getElementById('aarti-stage-youtube-container');
    if (ytContainer) ytContainer.innerHTML = '';
    if (window.MediaRouter && window.MediaRouter.activeMode === 'youtube') {{
      window.MediaRouter.destroyYouTubePlayer();
    }}

    _playLocalAartiTrack(item.audio);
    if (window.MediaRouter) window.MediaRouter.activeMode = 'local';
  }}

  window.isAartiPlaying = true;

  // Sync with global mini player dock
  if (typeof updateMiniPlayerDock === 'function') {{
    updateMiniPlayerDock({{
      title: item.title,
      deity: item.deity,
      singer: item.desc,
      audio_url: item.audio
    }}, true);
  }}

  // Ring Bell & Trigger Flower Shower
  if (typeof window.playBellSound === 'function') window.playBellSound();
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (navigator.vibrate) navigator.vibrate([30, 40, 30]);

  if (typeof showToast === 'function') {{
    showToast(`🪔 पावन महाआरती प्रारंभ: ${{item.title}}`);
  }}
}};

// Helper for local audio playback with automatic fallback resilience
function _playLocalAartiTrack(src) {{
  let audio = window.coreAudioElement || document.getElementById('core-app-audio');
  if (!audio) {{
    audio = new Audio();
    audio.id = 'core-app-audio';
    document.body.appendChild(audio);
    window.coreAudioElement = audio;
  }}

  audio.src = src;
  audio.load();
  audio.play().catch(err => {{
    console.warn('Local aarti playback notice:', err);
    // Automatic fallback if file unreadable
    audio.src = 'assets/audio/bhajan_achyutam_keshavam.mp3';
    audio.play().catch(() => {{}});
  }});
}}

// 5. Toggle Play/Pause for the currently active Aarti
window.toggleAartiPlayPause = function() {{
  const item = window.currentSelectedAartiItem || window.DIVINE_AARTI_DATASET[0];
  if (!item) return;

  const playNowBtn = document.getElementById('aarti-play-now-btn');
  const barPlayBtn = document.getElementById('aarti-bar-playpause-btn');
  const thali = document.getElementById('aarti-thali-disc');
  const activeBtn = document.getElementById(`aarti-play-btn-${{window.activeAartiId}}`);

  if (window.isAartiPlaying) {{
    // PAUSE
    const isYT = /(?:youtube\.com|youtu\.be)/i.test(item.audio);
    if (isYT) {{
      const iframe = document.getElementById('aarti-stage-yt-iframe');
      if (iframe && iframe.contentWindow) {{
        iframe.contentWindow.postMessage(JSON.stringify({{
          event: 'command',
          func: 'pauseVideo',
          args: []
        }}), '*');
      }}
    }} else {{
      if (window.coreAudioElement) window.coreAudioElement.pause();
      const ca = document.getElementById('core-app-audio');
      if (ca) ca.pause();
    }}

    window.isAartiPlaying = false;
    if (playNowBtn) playNowBtn.innerHTML = '<span>▶</span> पावन महाआरती सुनें';
    if (barPlayBtn) barPlayBtn.innerHTML = '▶ बजाएं';
    if (activeBtn) {{
      activeBtn.innerHTML = '▶';
      activeBtn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      activeBtn.style.color = '#1A0B2E';
    }}
    if (thali) thali.style.animation = 'spinDisc 25s linear infinite';
    if (typeof showToast === 'function') showToast('⏸️ आरती रोकी गई');
  }} else {{
    // RESUME
    const isYT = /(?:youtube\.com|youtu\.be)/i.test(item.audio);
    if (isYT) {{
      const iframe = document.getElementById('aarti-stage-yt-iframe');
      if (iframe && iframe.contentWindow) {{
        iframe.contentWindow.postMessage(JSON.stringify({{
          event: 'command',
          func: 'playVideo',
          args: []
        }}), '*');
      }} else {{
        window.playAartiItemDirect(item.id);
        return;
      }}
    }} else {{
      if (window.coreAudioElement) {{
        window.coreAudioElement.play().catch(() => {{}});
      }} else {{
        window.playAartiItemDirect(item.id);
        return;
      }}
    }}

    window.isAartiPlaying = true;
    if (playNowBtn) playNowBtn.innerHTML = '<span>⏸️</span> पावन महाआरती रोकें (Pause)';
    if (barPlayBtn) barPlayBtn.innerHTML = '⏸️ रोकें';
    if (activeBtn) {{
      activeBtn.innerHTML = '⏸️';
      activeBtn.style.background = '#10B981';
      activeBtn.style.color = '#FFF';
    }}
    if (thali) thali.style.animation = 'spinDisc 6s linear infinite';
    if (typeof showToast === 'function') showToast('▶ आरती पुनः प्रारंभ');
  }}
}};

// 6. Category Filtering for Aarti Cards
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

// 7. Toggle Thali Rotation Speed
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

// 8. Open Reader for Current or Specific Aarti
window.openAartiReader = function(aartiId) {{
  const item = window.DIVINE_AARTI_DATASET.find(x => x.id === aartiId);
  if (!item) return;

  if (typeof window.openContentItemReader === 'function') {{
    window.openContentItemReader(aartiId);
  }} else if (typeof window.showPage === 'function') {{
    window.playAartiItemDirect(aartiId);
  }}
}};

window.openCurrentAartiReader = function() {{
  const item = window.currentSelectedAartiItem || window.DIVINE_AARTI_DATASET[0];
  if (item) {{
    window.openAartiReader(item.id);
  }}
}};

// Initialize Aarti Stage Cards on page load
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => window.renderAartiStageCards('all'));
}} else {{
  window.renderAartiStageCards('all');
}}

"""

js = js[:start] + new_aarti_engine_js + "\n\n" + js[end:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Successfully upgraded Aarti Audio Engine in app.js!")
