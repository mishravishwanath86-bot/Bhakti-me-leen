import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Complete Authentic FM Radio HTML
rich_fm_radio_html = """      <!-- 📻 24x7 AUTHENTIC VEDIC FM BROADCAST RADIO (रेडियो मिर्ची/बिग एफएम स्टाइल) 📻 -->
      <div id="home-live-radio-card" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(155deg, #2D0B4E 0%, #18042B 45%, #0B0114 100%); border: 2px solid #F8C83B; border-radius: 28px; padding: 1.3rem 1.1rem; box-shadow: 0 15px 40px rgba(0,0,0,0.85), 0 0 25px rgba(248,200,59,0.18) inset; position:relative; overflow:hidden;">
        
        <!-- Live Glowing Beacon & Top Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
          <div style="font-size:1.05rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.45rem; filter:drop-shadow(0 0 8px #F59E0B);">📻</span>
            <span>24×7 लाइव भक्ति रेडियो FM</span>
          </div>
          
          <div id="radio-live-status-badge" style="display:flex; align-items:center; gap:6px; background:rgba(239,68,68,0.22); border:1.2px solid #EF4444; padding:4px 10px; border-radius:14px; box-shadow:0 0 10px rgba(239,68,68,0.3);">
            <span id="radio-pulse-dot" style="width:8px; height:8px; background:#EF4444; border-radius:50%; box-shadow:0 0 8px #EF4444; animation:pulseGlow 1.2s infinite;"></span>
            <span id="radio-live-text" style="font-size:0.72rem; font-weight:900; color:#F87171; letter-spacing:0.5px;">🔴 LIVE ON AIR</span>
          </div>
        </div>

        <!-- 🎙️ LIVE SHOW & RJ METADATA BADGE BAR -->
        <div style="background:rgba(248,200,59,0.12); border:1px solid rgba(248,200,59,0.3); border-radius:14px; padding:6px 12px; margin-bottom:12px; display:flex; align-items:center; justify-content:space-between; gap:8px;">
          <div style="font-size:0.75rem; font-weight:900; color:#FDE68A; display:flex; align-items:center; gap:6px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
            <span>🎙️ शो:</span>
            <span id="radio-live-show-name" style="color:#FFFDF8;">अमृत वेला प्रभात</span>
            <span id="radio-live-rj-name" style="background:rgba(248,200,59,0.25); border:1px solid #F8C83B; color:#FDE68A; padding:1px 7px; border-radius:8px; font-size:0.68rem;">RJ दिव्या</span>
          </div>
          <div style="font-size:0.7rem; color:#A7F3D0; font-weight:800; white-space:nowrap;">
            HD 320kbps 📡
          </div>
        </div>

        <!-- 📟 RETRO ANALOG RADIO FREQUENCY SCALE & TUNING NEEDLE -->
        <div style="background:rgba(0,0,0,0.55); border:1.5px solid rgba(248,200,59,0.4); border-radius:18px; padding:10px 12px; margin-bottom:12px; position:relative; box-shadow:inset 0 0 15px rgba(0,0,0,0.8);">
          
          <div style="display:flex; justify-content:space-between; font-size:0.68rem; font-weight:900; color:#CBD5E1; margin-bottom:4px; letter-spacing:0.5px; font-family:monospace;">
            <span>100.8</span>
            <span>102.4</span>
            <span>104.0</span>
            <span>106.0</span>
            <span>108.1</span>
            <span>108.5</span>
            <span>108.9</span>
          </div>

          <!-- Glass Tuning Track with Moving Red Needle -->
          <div style="position:relative; width:100%; height:22px; background:linear-gradient(180deg, #111 0%, #222 50%, #050505 100%); border-radius:6px; border:1px solid rgba(255,255,255,0.15); overflow:hidden; cursor:pointer;" onclick="handleAnalogScaleClick(event)">
            
            <!-- Scale Ticks -->
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

            <!-- Red Illuminated Tuning Needle -->
            <div id="analog-tuning-needle" style="position:absolute; top:0; bottom:0; left:88%; width:3px; background:#EF4444; box-shadow:0 0 10px #EF4444, 0 0 4px #FFF; transition:left 0.35s cubic-bezier(0.4, 0, 0.2, 1); z-index:3;"></div>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
            <span style="font-size:0.65rem; color:#94A3B8;">ANALOG FM BAND</span>
            <span id="analog-frequency-label" style="font-size:0.75rem; font-weight:900; color:#F8C83B; font-family:monospace;">TUNED: 108.5 MHz</span>
            <span style="font-size:0.65rem; color:#94A3B8;">STEREO KHZ</span>
          </div>

        </div>

        <!-- [Station Metadata & Live Visualizer Box] -->
        <div style="background:rgba(0,0,0,0.35); border:1.2px solid rgba(248,200,59,0.3); border-radius:20px; padding:12px 14px; margin-bottom:12px; display:flex; align-items:center; justify-content:space-between; gap:12px;">
          
          <div style="display:flex; align-items:center; gap:12px; flex:1; min-width:0;">
            <!-- Rotating Vinyl Disc with Deity Chakra -->
            <div id="radio-disc-icon" style="width:48px; height:48px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 65%, #451A03 100%); border:2.5px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:1.4rem; box-shadow:0 0 16px rgba(248,200,59,0.5); flex-shrink:0;">
              🪷
            </div>

            <!-- Metadata Details -->
            <div style="flex:1; min-width:0;">
              <div id="radio-freq-tag" style="font-size:0.75rem; font-weight:900; color:#F8C83B; display:flex; align-items:center; gap:5px; text-shadow:0 0 8px rgba(248,200,59,0.4);">
                <span>📡 108.5 FM</span> • <span id="radio-station-title">श्री राधा-कृष्ण रस</span>
              </div>
              <div id="radio-track-now" style="font-size:0.88rem; font-weight:900; color:#FFFDF8; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                अच्युतम केशवम कृष्ण दामोदरम
              </div>
              <div id="radio-artist-sub" style="font-size:0.7rem; color:#CBD5E1; margin-top:1px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                श्री अनिरुद्धाचार्य जी महाराज • 24×7 लाइव प्रसारण
              </div>
            </div>
          </div>

          <!-- Animated Equalizer Sound Bars -->
          <div id="radio-sound-bars" style="display:flex; align-items:flex-end; gap:3px; height:20px; flex-shrink:0; padding-right:4px;">
            <span style="width:3.5px; height:100%; background:#10B981; border-radius:2px; animation:bounceBar 0.8s infinite ease-in-out;"></span>
            <span style="width:3.5px; height:60%; background:#F59E0B; border-radius:2px; animation:bounceBar 0.6s infinite ease-in-out 0.2s;"></span>
            <span style="width:3.5px; height:85%; background:#10B981; border-radius:2px; animation:bounceBar 0.9s infinite ease-in-out 0.4s;"></span>
            <span style="width:3.5px; height:45%; background:#F8C83B; border-radius:2px; animation:bounceBar 0.5s infinite ease-in-out 0.1s;"></span>
            <span style="width:3.5px; height:90%; background:#10B981; border-radius:2px; animation:bounceBar 0.7s infinite ease-in-out 0.3s;"></span>
          </div>

        </div>

        <!-- [Station Dial / Channel Switcher Carousel] -->
        <div style="margin-bottom:14px;">
          <div style="display:flex; gap:8px; overflow-x:auto; padding-bottom:6px; scrollbar-width:none; -webkit-overflow-scrolling:touch;">
            
            <!-- Station 1: Shiv -->
            <button onclick="tuneRadioStation(0)" class="radio-station-pill" id="radio-pill-0" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
              <span>🔱</span> 108.1 FM • शिव भजन
            </button>

            <!-- Station 2: Krishna (Active) -->
            <button onclick="tuneRadioStation(1)" class="radio-station-pill active" id="radio-pill-1" style="background:linear-gradient(135deg, #F8C83B, #D97706); border:none; border-radius:14px; padding:7px 12px; color:#1A0B2E; font-size:0.75rem; font-weight:900; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0; box-shadow:0 0 12px rgba(248,200,59,0.4);">
              <span>🪷</span> 108.5 FM • कृष्ण रस ⭐
            </button>

            <!-- Station 3: Hanuman -->
            <button onclick="tuneRadioStation(2)" class="radio-station-pill" id="radio-pill-2" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
              <span>🚩</span> 108.9 FM • हनुमान वाणी
            </button>

            <!-- Station 4: Om Mantra -->
            <button onclick="tuneRadioStation(3)" class="radio-station-pill" id="radio-pill-3" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
              <span>🕉️</span> 100.8 FM • अखंड मंत्र
            </button>

            <!-- Station 5: Mandir Aarti -->
            <button onclick="tuneRadioStation(4)" class="radio-station-pill" id="radio-pill-4" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(255,255,255,0.18); border-radius:14px; padding:7px 12px; color:#CBD5E1; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:6px; white-space:nowrap; flex-shrink:0;">
              <span>🪔</span> 102.4 FM • लाइव आरती
            </button>

          </div>
        </div>

        <!-- [Player Controls: Prev, Large Play/Pause, Next] -->
        <div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-bottom:12px;">
          
          <button onclick="tunePrevRadioStation()" title="पिछला चैनल" style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.09); border:1.3px solid rgba(248,200,59,0.35); color:#FDE68A; font-size:1.2rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3); transition:transform 0.15s ease;">
            ⏮️
          </button>

          <button id="radio-play-btn" onclick="toggleLiveRadioPlayback()" title="लाइव रेडियो चलाएं / रोकें" style="width:58px; height:58px; border-radius:50%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); border:2.5px solid #FEF3C7; color:#1A0B2E; font-size:1.6rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 25px rgba(248,200,59,0.6); transition:transform 0.15s ease;">
            ▶
          </button>

          <button onclick="tuneNextRadioStation()" title="अगला चैनल" style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.09); border:1.3px solid rgba(248,200,59,0.35); color:#FDE68A; font-size:1.2rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3); transition:transform 0.15s ease;">
            ⏭️
          </button>

        </div>

        <!-- 📢 UPCOMING SHOW TICKER -->
        <div style="background:rgba(255,255,255,0.05); border-radius:12px; padding:6px 12px; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
          <span style="font-size:0.85rem;">📢</span>
          <span id="radio-upcoming-show-ticker" style="font-size:0.72rem; color:#CBD5E1; font-weight:700;">
            अगला कार्यक्रम: शाम 06:00 बजे • काशी विश्वनाथ लाइव महाआरती
          </span>
        </div>

        <!-- 🔴 LIVE AUDIENCE LISTENER TICKER -->
        <div style="text-align:center; padding-top:4px; border-top:1px solid rgba(255,255,255,0.08);">
          <span style="font-size:0.75rem; font-weight:800; color:#A7F3D0; display:inline-flex; align-items:center; gap:6px;">
            <span style="width:7px; height:7px; background:#10B981; border-radius:50%; box-shadow:0 0 6px #10B981;"></span>
            <span>🔴 LIVE: देश भर के <strong id="radio-live-listener-count" style="color:#FDE68A;">14,280+</strong> भक्त अभी एक साथ सुन रहे हैं</span>
          </span>
        </div>

      </div>
"""

# Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<!-- 📻 24x7 LIVE[\s\S]*?<!-- 🎯 SACRED KNOWLEDGE ZONE', rich_fm_radio_html + '\n\n            <!-- 🎯 SACRED KNOWLEDGE ZONE', html)

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Replaced Radio card in index.html with Authentic FM Broadcast UI (v={ts})")
