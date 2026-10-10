import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Multi-Channel Live Radio Card HTML
radio_card_html = """
      <!-- 📻 24x7 LIVE MULTI-CHANNEL BHAKTI RADIO (अखंड दिव्य रेडियो इंजन) 📻 -->
      <div id="home-live-radio-card" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(155deg, #2A0D4E 0%, #17052E 50%, #0B0116 100%); border: 1.8px solid #F8C83B; border-radius: 26px; padding: 1.3rem 1.1rem; box-shadow: 0 12px 35px rgba(0,0,0,0.75), 0 0 20px rgba(248,200,59,0.15) inset; position:relative; overflow:hidden;">
        
        <!-- Live Glowing Badge & Top Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="font-size:1.02rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.4rem;">📻</span>
            <span>24×7 लाइव भक्ति रेडियो</span>
          </div>
          <div id="radio-live-status-badge" style="display:flex; align-items:center; gap:6px; background:rgba(239,68,68,0.22); border:1.2px solid #EF4444; padding:3px 10px; border-radius:12px;">
            <span id="radio-pulse-dot" style="width:8px; height:8px; background:#EF4444; border-radius:50%; box-shadow:0 0 8px #EF4444; animation:pulseGlow 1.2s infinite;"></span>
            <span id="radio-live-text" style="font-size:0.72rem; font-weight:900; color:#F87171; letter-spacing:0.5px;">🔴 LIVE STREAM</span>
          </div>
        </div>

        <!-- [Station Frequency / Visualizer Display Box] -->
        <div style="background:rgba(0,0,0,0.4); border:1.3px solid rgba(248,200,59,0.35); border-radius:20px; padding:12px 14px; margin-bottom:14px; display:flex; align-items:center; justify-content:space-between; gap:12px; box-shadow:0 4px 15px rgba(0,0,0,0.4);">
          
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
          <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-bottom:6px; display:flex; align-items:center; justify-content:space-between;">
            <span>📻 लाइव स्टेशन चयन (5 चैनल्स):</span>
            <span id="radio-current-chan-index" style="color:#A7F3D0; font-size:0.7rem;">चैनल 2 / 5</span>
          </div>

          <div id="radio-channels-scroll-row" style="display:flex; gap:8px; overflow-x:auto; padding-bottom:6px; scrollbar-width:none; -webkit-overflow-scrolling:touch;">
            
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
        <div style="display:flex; align-items:center; justify-content:center; gap:20px; margin-bottom:14px;">
          
          <button onclick="tunePrevRadioStation()" title="पिछला चैनल (Previous Station)" style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.09); border:1.3px solid rgba(248,200,59,0.35); color:#FDE68A; font-size:1.2rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3); transition:transform 0.15s ease;">
            ⏮️
          </button>

          <button id="radio-play-btn" onclick="toggleLiveRadioPlayback()" title="लाइव रेडियो चलाएं / रोकें" style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); border:2.5px solid #FEF3C7; color:#1A0B2E; font-size:1.5rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 25px rgba(248,200,59,0.6); transition:transform 0.15s ease;">
            ▶
          </button>

          <button onclick="tuneNextRadioStation()" title="अगला चैनल (Next Station)" style="width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.09); border:1.3px solid rgba(248,200,59,0.35); color:#FDE68A; font-size:1.2rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3); transition:transform 0.15s ease;">
            ⏭️
          </button>

        </div>

        <!-- [Quick Category Filter Buttons] -->
        <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 6px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px;">
          <button onclick="tuneRadioStation(1)" style="background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); color:#FDE68A; font-size:0.72rem; font-weight:800; padding:6px 4px; border-radius:12px; cursor:pointer; text-align:center;">
            🌸 भजन स्टेशन्स
          </button>
          <button onclick="tuneRadioStation(3)" style="background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); color:#FDE68A; font-size:0.72rem; font-weight:800; padding:6px 4px; border-radius:12px; cursor:pointer; text-align:center;">
            🕉️ 24×7 मंत्र
          </button>
          <button onclick="tuneRadioStation(4)" style="background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); color:#FDE68A; font-size:0.72rem; font-weight:800; padding:6px 4px; border-radius:12px; cursor:pointer; text-align:center;">
            🪔 लाइव आरती
          </button>
        </div>

      </div>
"""

# 2. Insert into index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace existing home-live-radio-card or place above quiz hub
if 'id="home-live-radio-card"' in html:
    html = re.sub(r'<!-- 📻 24x7 LIVE[\s\S]*?<\/div>\s*<\/div>', radio_card_html, html)
    print("✓ Replaced existing radio card in index.html")
else:
    # Insert before Quiz Hub
    pos_quiz = html.find('<!-- 🎯 SACRED KNOWLEDGE ZONE')
    if pos_quiz != -1:
        html = html[:pos_quiz] + radio_card_html + "\n\n      " + html[pos_quiz:]
        print("✓ Inserted radio card before Quiz Hub in index.html")
    else:
        # Insert before Panchang
        pos_panchang = html.find('<!-- 📅 DAILY LIVE VEDIC PANCHANG')
        html = html[:pos_panchang] + radio_card_html + "\n\n      " + html[pos_panchang:]
        print("✓ Inserted radio card before Panchang in index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ index.html updated with Multi-Channel Live Radio Card (v={ts})")
