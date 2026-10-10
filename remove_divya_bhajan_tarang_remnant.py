import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Exact target block to remove
target = """
        <!-- Station Info & Animated Wave Box -->
        <div style="display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:11px 14px; margin-bottom:12px;">
          
          <div style="display:flex; align-items:center; gap:12px; flex:1;">
            <!-- Spinning Disc Icon -->
            <div id="radio-disc-icon" style="width:44px; height:44px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #B45309 70%, #78350F 100%); border:2px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:1.3rem; box-shadow:0 0 14px rgba(248,200,59,0.45); flex-shrink:0;">
              🎶
            </div>

            <!-- Station Title & Subtitle -->
            <div style="flex:1;">
              <div id="radio-station-title" style="font-size:0.95rem; font-weight:900; color:#FFFDF8; line-height:1.2;">
                🌸 दिव्य भजन तरंग
              </div>
              <div id="radio-track-now" style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-top:2px;">
                अच्युतम केशवम कृष्ण दामोदरम
              </div>

              <!-- Animated Equalizer Sound Bars -->
              <div id="radio-sound-bars" style="display:none; align-items:flex-end; gap:3px; height:12px; margin-top:4px;">
                <span style="width:3px; height:100%; background:#10B981; border-radius:2px; animation:bounceBar 0.8s infinite ease-in-out;"></span>
                <span style="width:3px; height:60%; background:#F59E0B; border-radius:2px; animation:bounceBar 0.6s infinite ease-in-out 0.2s;"></span>
                <span style="width:3px; height:80%; background:#10B981; border-radius:2px; animation:bounceBar 0.9s infinite ease-in-out 0.4s;"></span>
                <span style="width:3px; height:40%; background:#F59E0B; border-radius:2px; animation:bounceBar 0.5s infinite ease-in-out 0.1s;"></span>
                <span style="width:3px; height:90%; background:#10B981; border-radius:2px; animation:bounceBar 0.7s infinite ease-in-out 0.3s;"></span>
              </div>
            </div>
          </div>

          <!-- Large Glowing Play / Pause Button -->
          <button id="radio-play-btn" onclick="toggleLiveRadioPlayback()" title="रेडियो बजाएं / रोकें" style="width:48px; height:48px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; font-size:1.3rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 18px rgba(248,200,59,0.5); flex-shrink:0; transition:transform 0.15s ease;">
            ▶
          </button>
        </div>

        <!-- 4 Station Selector Channels -->
        <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
          <button onclick="switchRadioChannel('bhajan', '🌸 दिव्य भजन तरंग', 'अच्युतम केशवम कृष्ण दामोदरम', this)" class="radio-chan-btn active" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; text-align:center; white-space:nowrap;">
            🌸 भजन
          </button>
          <button onclick="switchRadioChannel('mantra', '🕉️ अखंड महामंत्र', 'भगवान शिव महिमा व महामृत्युंजय', this)" class="radio-chan-btn" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            🕉️ मंत्र
          </button>
          <button onclick="switchRadioChannel('katha', '📖 अमृत रामकथा', 'पावन श्रीराम चरित मानस रस', this)" class="radio-chan-btn" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            📖 कथा
          </button>
          <button onclick="switchRadioChannel('aarti', '🪔 नित्य आरती धाम', 'श्री सत्यनारायण पावन कथा व आरती', this)" class="radio-chan-btn" style="padding:7px 4px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center; white-space:nowrap;">
            🪔 आरती
          </button>
        </div>

      </div>"""

if target in html:
    html = html.replace(target, '')
    print("✓ Successfully removed '🌸 दिव्य भजन तरंग' remnant block!")
else:
    # regex fallback
    html = re.sub(r'<!-- Station Info & Animated Wave Box[\s\S]*?<\/div>\s*<\/div>', '', html)
    print("✓ Removed using regex pattern!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html saved successfully!")
