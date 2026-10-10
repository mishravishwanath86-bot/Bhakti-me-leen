import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Compact Home Stage 1 Card
compact_home_card = """      <!-- 📻 STAGE 1: HOME PAGE COMPACT RADIO TRIGGER CARD 📻 -->
      <div id="home-live-radio-card" onclick="openRadioStudioModal()" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(145deg, #24083E 0%, #150424 100%); border: 1.5px solid #F59E0B; border-radius: 22px; padding: 1.1rem 1.2rem; cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.6), 0 0 15px rgba(248,200,59,0.12) inset; position: relative; overflow: hidden; transition: transform 0.18s ease;">
        <div style="position:absolute; right:-10px; bottom:-10px; font-size:4.5rem; opacity:0.08; pointer-events:none;">📻</div>
        
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
          <div style="font-size:0.98rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.4rem; filter:drop-shadow(0 0 8px #F59E0B);">📻</span>
            <span>24×7 लाइव भक्ति रेडियो</span>
          </div>
          
          <div style="display:flex; align-items:center; gap:6px; background:rgba(239,68,68,0.22); border:1.2px solid #EF4444; padding:3px 10px; border-radius:12px;">
            <span style="width:7px; height:7px; background:#EF4444; border-radius:50%; box-shadow:0 0 8px #EF4444; animation:pulseGlow 1.2s infinite;"></span>
            <span style="font-size:0.7rem; font-weight:900; color:#F87171; letter-spacing:0.5px;">🔴 LIVE STREAM</span>
          </div>
        </div>

        <!-- Station & Song Name -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div>
            <div id="home-compact-radio-freq" style="font-size:0.75rem; font-weight:900; color:#F8C83B;">
              📡 108.5 FM • श्री राधा-कृष्ण रस
            </div>
            <div id="home-compact-radio-track" style="font-size:0.88rem; font-weight:800; color:#FFFDF8; margin-top:2px;">
              🎶 "अच्युतम केशवम कृष्ण दामोदरम..."
            </div>
          </div>
          
          <!-- Mini Equalizer / Disc Icon -->
          <div id="home-compact-disc-icon" style="width:38px; height:38px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 65%, #451A03 100%); border:2px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:1.15rem; box-shadow:0 0 12px rgba(248,200,59,0.4);">
            🪷
          </div>
        </div>

        <!-- Trigger Button -->
        <div style="background:rgba(248,200,59,0.18); border:1.2px solid #F8C83B; border-radius:14px; padding:8px 12px; display:flex; align-items:center; justify-content:space-between; color:#FDE68A; font-size:0.82rem; font-weight:900;">
          <span style="display:flex; align-items:center; gap:6px;">
            <span>▶</span> तुरंत ट्यून करें / रेडियो स्टूडियो खोलें
          </span>
          <span>➔</span>
        </div>
      </div>"""

# 2. Stage 2 Full-Screen Studio Modal + Mini-Player
stage_2_studio_modal = """
  <!-- 📻 STAGE 2: FULL-SCREEN RADIO BROADCAST STUDIO MODAL 📻 -->
  <div id="radio-broadcast-studio-modal" style="display:none; position:fixed; inset:0; z-index:100400; background:rgba(8,2,14,0.96); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div style="width:100%; max-width:440px; background:radial-gradient(circle at 50% 20%, #340C54 0%, #19042D 55%, #0A0114 100%); border:2px solid #F8C83B; border-radius:30px; padding:1.4rem 1.2rem; box-shadow:0 25px 80px rgba(0,0,0,0.95), 0 0 30px rgba(248,200,59,0.2) inset; position:relative; animation:fadeInUp 0.3s ease; max-height:94vh; overflow-y:auto;">
      
      <!-- 1. Top Bar -->
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:8px;">
        <button onclick="closeRadioStudioModal()" style="background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; padding:4px 10px; border-radius:12px; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:4px;">
          <span>↓</span> नीचे करें
        </button>

        <div style="font-size:0.95rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
          <span>📻</span> भक्ति FM स्टूडियो
        </div>

        <div style="font-size:0.7rem; font-weight:900; color:#A7F3D0; background:rgba(16,185,129,0.18); border:1px solid #10B981; padding:3px 8px; border-radius:10px; display:flex; align-items:center; gap:4px;">
          <span style="width:6px; height:6px; background:#10B981; border-radius:50%;"></span>
          <span id="radio-studio-listener-count">14,280+ लाइव</span>
        </div>
      </div>

      <!-- 2. Show & RJ Header -->
      <div style="background:rgba(248,200,59,0.12); border:1px solid rgba(248,200,59,0.3); border-radius:16px; padding:8px 12px; margin-bottom:12px; display:flex; align-items:center; justify-content:space-between;">
        <div>
          <div style="font-size:0.68rem; color:#CBD5E1; font-weight:700;">वर्तमान लाइव शो:</div>
          <div style="font-size:0.85rem; font-weight:900; color:#FFFDF8; margin-top:1px;">
            <span id="radio-studio-show-name">अमृत वेला प्रभात</span>
            <span id="radio-studio-rj-name" style="background:#F8C83B; color:#1A0B2E; padding:1px 6px; border-radius:6px; font-size:0.68rem; margin-left:6px; font-weight:900;">RJ दिव्या</span>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:0.65rem; color:#A7F3D0; font-weight:800;">🔴 ON AIR</div>
          <div style="font-size:0.68rem; color:#CBD5E1; margin-top:1px;">HD Stereo</div>
        </div>
      </div>

      <!-- 3. Retro Analog Frequency Tuner Scale -->
      <div style="background:rgba(0,0,0,0.55); border:1.5px solid rgba(248,200,59,0.4); border-radius:18px; padding:10px 12px; margin-bottom:14px; position:relative; box-shadow:inset 0 0 15px rgba(0,0,0,0.8);">
        <div style="display:flex; justify-content:space-between; font-size:0.68rem; font-weight:900; color:#CBD5E1; margin-bottom:4px; font-family:monospace;">
          <span>100.8</span>
          <span>102.4</span>
          <span>104.0</span>
          <span>106.0</span>
          <span>108.1</span>
          <span>108.5</span>
          <span>108.9</span>
        </div>

        <div style="position:relative; width:100%; height:22px; background:linear-gradient(180deg, #111 0%, #222 50%, #050505 100%); border-radius:6px; border:1px solid rgba(255,255,255,0.15); overflow:hidden; cursor:pointer;" onclick="handleAnalogScaleClick(event)">
          <div style="position:absolute; inset:0; display:flex; justify-content:space-between; align-items:flex-end; padding:0 6px 3px; pointer-events:none;">
            <span style="width:1px; height:12px; background:#F8C83B;"></span>
            <span style="width:1px; height:6px; background:#888;"></span>
            <span style="width:1px; height:12px; background:#F8C83B;"></span>
            <span style="width:1px; height:6px; background:#888;"></span>
            <span style="width:1px; height:8px; background:#888;"></span>
            <span style="width:1px; height:12px; background:#F8C83B;"></span>
            <span style="width:1px; height:6px; background:#888;"></span>
            <span style="width:1px; height:12px; background:#F8C83B;"></span>
            <span style="width:1px; height:6px; background:#888;"></span>
            <span style="width:1px; height:14px; background:#EF4444;"></span>
          </div>
          <div id="analog-tuning-needle" style="position:absolute; top:0; bottom:0; left:88%; width:3px; background:#EF4444; box-shadow:0 0 10px #EF4444, 0 0 4px #FFF; transition:left 0.35s cubic-bezier(0.4, 0, 0.2, 1); z-index:3;"></div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
          <span style="font-size:0.65rem; color:#94A3B8;">ANALOG FM BAND</span>
          <span id="analog-frequency-label" style="font-size:0.75rem; font-weight:900; color:#F8C83B; font-family:monospace;">TUNED: 108.5 MHz</span>
          <span style="font-size:0.65rem; color:#94A3B8;">STEREO KHZ</span>
        </div>
      </div>

      <!-- 4. Rotating Vinyl Disc & Deity Artwork Display -->
      <div style="text-align:center; margin-bottom:14px; position:relative;">
        <div id="radio-studio-disc" style="width:90px; height:90px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 65%, #451A03 100%); border:3.5px solid #FEF3C7; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; font-size:2.8rem; box-shadow:0 0 30px rgba(248,200,59,0.5);">
          🪷
        </div>

        <div id="radio-studio-freq-tag" style="font-size:0.85rem; font-weight:900; color:#F8C83B;">
          📡 108.5 FM • <span id="radio-studio-station-title">श्री राधा-कृष्ण रस</span>
        </div>
        <div id="radio-studio-track-now" style="font-size:1.05rem; font-weight:900; color:#FFFDF8; margin-top:3px;">
          अच्युतम केशवम कृष्ण दामोदरम
        </div>
        <div id="radio-studio-artist-sub" style="font-size:0.75rem; color:#CBD5E1; margin-top:2px;">
          श्री अनिरुद्धाचार्य जी महाराज • 24×7 लाइव प्रसारण
        </div>

        <!-- Sound Waves Bars -->
        <div id="radio-studio-sound-bars" style="display:flex; align-items:flex-end; justify-content:center; gap:4px; height:22px; margin-top:8px;">
          <span style="width:4px; height:100%; background:#10B981; border-radius:2px; animation:bounceBar 0.8s infinite ease-in-out;"></span>
          <span style="width:4px; height:60%; background:#F59E0B; border-radius:2px; animation:bounceBar 0.6s infinite ease-in-out 0.2s;"></span>
          <span style="width:4px; height:85%; background:#10B981; border-radius:2px; animation:bounceBar 0.9s infinite ease-in-out 0.4s;"></span>
          <span style="width:4px; height:45%; background:#F8C83B; border-radius:2px; animation:bounceBar 0.5s infinite ease-in-out 0.1s;"></span>
          <span style="width:4px; height:90%; background:#10B981; border-radius:2px; animation:bounceBar 0.7s infinite ease-in-out 0.3s;"></span>
        </div>
      </div>

      <!-- 5. 5 Dedicated Stations Switcher Horizontal Pills -->
      <div style="margin-bottom:14px;">
        <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-bottom:6px;">
          📻 पावन स्टेशन चुनें (5 चैनल्स):
        </div>
        <div style="display:flex; gap:8px; overflow-x:auto; padding-bottom:6px; scrollbar-width:none; -webkit-overflow-scrolling:touch;">
          <button onclick="tuneRadioStation(0)" class="radio-station-pill" id="radio-pill-0" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
            <span>🔱</span> 108.1 FM • शिव भजन
          </button>
          <button onclick="tuneRadioStation(1)" class="radio-station-pill active" id="radio-pill-1" style="background:linear-gradient(135deg, #F8C83B, #D97706); border:none; border-radius:14px; padding:7px 12px; color:#1A0B2E; font-size:0.75rem; font-weight:900; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0; box-shadow:0 0 12px rgba(248,200,59,0.4);">
            <span>🪷</span> 108.5 FM • कृष्ण रस ⭐
          </button>
          <button onclick="tuneRadioStation(2)" class="radio-station-pill" id="radio-pill-2" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
            <span>🚩</span> 108.9 FM • हनुमान वाणी
          </button>
          <button onclick="tuneRadioStation(3)" class="radio-station-pill" id="radio-pill-3" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
            <span>🕉️</span> 100.8 FM • अखंड मंत्र
          </button>
          <button onclick="tuneRadioStation(4)" class="radio-station-pill" id="radio-pill-4" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
            <span>🪔</span> 102.4 FM • लाइव आरती
          </button>
        </div>
      </div>

      <!-- 6. Studio Player Controls -->
      <div style="display:flex; align-items:center; justify-content:center; gap:24px; margin-bottom:14px;">
        <button onclick="tunePrevRadioStation()" title="पिछला चैनल" style="width:48px; height:48px; border-radius:50%; background:rgba(255,255,255,0.09); border:1.3px solid rgba(248,200,59,0.35); color:#FDE68A; font-size:1.3rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3);">
          ⏮️
        </button>

        <button id="radio-play-btn" onclick="toggleLiveRadioPlayback()" title="लाइव रेडियो चलाएं / रोकें" style="width:64px; height:64px; border-radius:50%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); border:3px solid #FEF3C7; color:#1A0B2E; font-size:1.8rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 30px rgba(248,200,59,0.7);">
          ▶
        </button>

        <button onclick="tuneNextRadioStation()" title="अगला चैनल" style="width:48px; height:48px; border-radius:50%; background:rgba(255,255,255,0.09); border:1.3px solid rgba(248,200,59,0.35); color:#FDE68A; font-size:1.3rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3);">
          ⏭️
        </button>
      </div>

      <!-- Upcoming Show Ticker -->
      <div style="background:rgba(255,255,255,0.05); border-radius:12px; padding:6px 12px; text-align:center;">
        <span id="radio-studio-upcoming-show" style="font-size:0.72rem; color:#CBD5E1; font-weight:700;">
          📢 अगला कार्यक्रम: शाम 06:00 बजे • महाकाल संध्या आरती & दीप दर्शन
        </span>
      </div>

    </div>
  </div>

  <!-- 📻 FLOATING MINI-PLAYER BAR (WHEN MODAL IS CLOSED WHILE PLAYING) 📻 -->
  <div id="radio-floating-mini-player" style="display:none; position:fixed; bottom:64px; left:12px; right:12px; max-width:480px; margin:0 auto; z-index:100150; background:linear-gradient(135deg, rgba(30,11,54,0.95) 0%, rgba(15,4,28,0.98) 100%); border:1.5px solid #F8C83B; border-radius:20px; padding:8px 14px; backdrop-filter:blur(15px); -webkit-backdrop-filter:blur(15px); box-shadow:0 10px 30px rgba(0,0,0,0.85); align-items:center; justify-content:space-between; gap:10px; animation:slideUp 0.3s ease;" onclick="openRadioStudioModal()">
    <div style="display:flex; align-items:center; gap:10px; flex:1; min-width:0;">
      <div id="mini-radio-disc" style="width:36px; height:36px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 70%); border:2px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:1.1rem; flex-shrink:0;">
        🪷
      </div>
      <div style="flex:1; min-width:0;">
        <div id="mini-radio-freq-title" style="font-size:0.72rem; font-weight:900; color:#F8C83B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
          📡 108.5 FM • श्री राधा-कृष्ण रस
        </div>
        <div id="mini-radio-track-title" style="font-size:0.8rem; font-weight:800; color:#FFFDF8; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
          अच्युतम केशवम कृष्ण दामोदरम
        </div>
      </div>
    </div>

    <div style="display:flex; align-items:center; gap:8px;" onclick="event.stopPropagation()">
      <button id="mini-radio-play-btn" onclick="toggleLiveRadioPlayback()" style="width:36px; height:36px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; font-size:1.1rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 10px rgba(248,200,59,0.5);">
        ▶
      </button>
      <button onclick="openRadioStudioModal()" title="स्टूडियो खोलें" style="background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; padding:6px 10px; border-radius:12px; font-size:0.72rem; font-weight:800; cursor:pointer;">
        ⤢ खोलें
      </button>
    </div>
  </div>
"""

# Replace in index.html
pattern = r'<div id="home-live-radio-card"[\s\S]*?<\/div>\s*<\/div>'
html = re.sub(pattern, compact_home_card, html)

# Insert Stage 2 modal if not present
if 'id="radio-broadcast-studio-modal"' not in html:
    pos_modals = html.find('<!-- 📜 BHOJPATRA SCROLL REVEAL MODAL')
    if pos_modals != -1:
        html = html[:pos_modals] + stage_2_studio_modal + "\n\n    " + html[pos_modals:]
    else:
        html = html.replace('</body>', stage_2_studio_modal + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html updated with Two-Stage Radio Architecture (Compact Card + Fullscreen Studio + Mini-Player)")
