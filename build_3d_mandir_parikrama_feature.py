import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Three.js script in <head> if not present
if 'three.min.js' not in html:
    three_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    html = html.replace('</head>', f'  {three_script}\n</head>')

# Add Home Screen Entry Card ("✨ दिव्य परिक्रमा संकल्प") right above "डिजिटल पूजा थाली" or below Hero
parikrama_home_card = """
      <!-- ✨ 3D DIVINE PARIKRAMA SANKALP (दिव्य परिक्रमा संकल्प) CARD ✨ -->
      <div id="parikrama-sankalp-home-card" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(160deg, #2D1047 0%, #1A052E 60%, #0F021B 100%); border: 1.5px solid #F59E0B; border-radius: 24px; padding: 1.3rem 1.2rem; box-shadow: 0 10px 35px rgba(0,0,0,0.7), 0 0 18px rgba(248,200,59,0.15) inset; position: relative; overflow: hidden;">
        
        <!-- Glow accent background -->
        <div style="position:absolute; top:-30px; right:-30px; width:120px; height:120px; border-radius:50%; background:radial-gradient(circle, rgba(248,200,59,0.2) 0%, transparent 70%); pointer-events:none;"></div>

        <!-- Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
          <div style="font-size:1.05rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.35rem; filter:drop-shadow(0 0 8px #F59E0B);">✨</span>
            <span>दिव्य परिक्रमा संकल्प</span>
          </div>
          <span style="font-size:0.72rem; font-weight:900; background:rgba(248,200,59,0.2); border:1.2px solid #F8C83B; color:#FDE68A; padding:3px 10px; border-radius:12px; box-shadow:0 0 10px rgba(248,200,59,0.25);">
            3D Real-Time
          </span>
        </div>

        <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 12px 0; line-height:1.4;">
          गर्भग्रह की 360° परिक्रमा करें, डिजिटल पूजा करें और पुण्य लाभ प्राप्त करें:
        </p>

        <!-- Parikrama Target Selector Chips -->
        <div style="display:flex; align-items:center; justify-content:space-between; gap:6px; margin-bottom:14px;">
          <button onclick="selectParikramaTarget(3, this)" class="parikrama-chip" style="flex:1; padding:8px 4px; border-radius:12px; font-size:0.78rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
            3 चक्कर
          </button>
          <button onclick="selectParikramaTarget(7, this)" class="parikrama-chip" style="flex:1; padding:8px 4px; border-radius:12px; font-size:0.78rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
            7 चक्कर
          </button>
          <button onclick="selectParikramaTarget(11, this)" class="parikrama-chip active" style="flex:1; padding:8px 4px; border-radius:12px; font-size:0.78rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; text-align:center; box-shadow:0 0 12px rgba(248,200,59,0.4);">
            11 चक्कर ⭐
          </button>
          <button onclick="selectParikramaTarget(21, this)" class="parikrama-chip" style="flex:1; padding:8px 4px; border-radius:12px; font-size:0.78rem; font-weight:800; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
            21 चक्कर
          </button>
        </div>

        <!-- Primary CTA Button -->
        <button onclick="start3DMandirParikramaFlow()" style="width:100%; background:linear-gradient(135deg, #FF8C00 0%, #FF512F 100%); color:#FFF; border:none; font-size:0.95rem; font-weight:900; padding:13px 0; border-radius:16px; cursor:pointer; box-shadow:0 6px 20px rgba(255,81,47,0.5); display:flex; align-items:center; justify-content:center; gap:8px; transition:transform 0.15s ease;">
          <span id="parikrama-cta-text">🚩 11 परिक्रमा शुरू करें (3D मंदिर में प्रवेश)</span> ➔
        </button>

      </div>
"""

# Insert right before Digital Puja Thali
if 'id="parikrama-sankalp-home-card"' not in html:
    pos = html.find('<!-- 🪔 8-ITEM INTERACTIVE DIGITAL PUJA THALI')
    if pos == -1:
        pos = html.find('id="digital-puja-thali-card"')
    if pos != -1:
        html = html[:pos] + parikrama_home_card + "\n\n      " + html[pos:]
    else:
        # Fallback after Hero
        pos_hero = html.find('<!-- 🌅 DAILY DHARMIK SUVICHAR')
        html = html[:pos_hero] + parikrama_home_card + "\n\n      " + html[pos_hero:]

# Add 3D Mandir & Parikrama Fullscreen Screen + Door Transition Modal
mandir_3d_viewport_html = """
  <!-- ═════════════════════════════════════════════════════════════════
       🏛️ 3D REAL-TIME MANDIR & PARIKRAMA FULLSCREEN VIEWPORT MODAL 🏛️
       ═════════════════════════════════════════════════════════════════ -->
  <div id="mandir-3d-modal" style="display:none; position:fixed; inset:0; z-index:100080; background:#0B0116; overflow:hidden; flex-direction:column;">
    
    <!-- 🚪 TEMPLE BRASS DOOR OPENING TRANSITION OVERLAY 🚪 -->
    <div id="temple-door-transition-overlay" style="display:none; position:absolute; inset:0; z-index:100; pointer-events:none;">
      <div id="door-left" style="position:absolute; top:0; left:0; width:50%; height:100%; background:radial-gradient(circle at 70% 40%, #D97706 0%, #B45309 50%, #451A03 100%); border-right:3px solid #FEF3C7; box-shadow:inset 0 0 40px rgba(0,0,0,0.8); display:flex; align-items:center; justify-content:flex-end; padding-right:15px; transform-origin:left center; transition:transform 1.2s cubic-bezier(0.4, 0, 0.2, 1);">
        <div style="width:50px; height:50px; border-radius:50%; border:3px solid #FEF3C7; background:#78350F; display:flex; align-items:center; justify-content:center; font-size:1.8rem; box-shadow:0 0 15px rgba(0,0,0,0.6);">
          🕉️
        </div>
      </div>
      <div id="door-right" style="position:absolute; top:0; right:0; width:50%; height:100%; background:radial-gradient(circle at 30% 40%, #D97706 0%, #B45309 50%, #451A03 100%); border-left:3px solid #FEF3C7; box-shadow:inset 0 0 40px rgba(0,0,0,0.8); display:flex; align-items:center; justify-content:flex-start; padding-left:15px; transform-origin:right center; transition:transform 1.2s cubic-bezier(0.4, 0, 0.2, 1);">
        <div style="width:50px; height:50px; border-radius:50%; border:3px solid #FEF3C7; background:#78350F; display:flex; align-items:center; justify-content:center; font-size:1.8rem; box-shadow:0 0 15px rgba(0,0,0,0.6);">
          卐
        </div>
      </div>
    </div>

    <!-- 🌟 TOP GLASS BAR (Controls, Deity Selector, Day/Night, Sound) -->
    <div style="position:absolute; top:0; left:0; right:0; z-index:30; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; background:linear-gradient(180deg, rgba(10,2,18,0.85) 0%, transparent 100%); backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px);">
      
      <!-- Back Button -->
      <button onclick="close3DMandirModal()" title="बाहर जाएं (Exit 3D Mandir)" style="width:38px; height:38px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1.2rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:transform 0.15s ease;">
        ❮
      </button>

      <!-- Mandir Deity Selector Dropdown -->
      <div style="position:relative;">
        <select id="mandir-deity-select" onchange="switch3DMandirDeity(this.value)" style="background:rgba(42,13,78,0.9); border:1.5px solid #F8C83B; color:#FFFDF8; font-size:0.85rem; font-weight:800; padding:6px 28px 6px 12px; border-radius:14px; outline:none; cursor:pointer; appearance:none; -webkit-appearance:none; box-shadow:0 4px 15px rgba(0,0,0,0.5);">
          <option value="kashi">🏛️ श्री काशी विश्वनाथ</option>
          <option value="ayodhya">🪔 श्री राम जन्मभूमि अयोध्या</option>
          <option value="siddhivinayak">🌺 श्री सिद्धिविनायक मंदिर</option>
          <option value="mahakal">🔱 श्री महाकालेश्वर उज्जैन</option>
        </select>
        <span style="position:absolute; right:10px; top:50%; transform:translateY(-50%); color:#FDE68A; pointer-events:none; font-size:0.75rem;">▼</span>
      </div>

      <!-- Right Actions: Day/Night & Sound -->
      <div style="display:flex; align-items:center; gap:6px;">
        <button id="mandir-lighting-toggle-btn" onclick="toggle3DMandirLighting()" title="प्रकाश बदलें (दिन / आरती रात्रि)" style="width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          🌙
        </button>
        <button id="mandir-sound-toggle-btn" onclick="toggle3DMandirSound()" title="मंत्र ध्वनि (Mute / Unmute)" style="width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          🔊
        </button>
      </div>

    </div>

    <!-- 🌌 CENTER 3D CANVAS CONTAINER -->
    <div id="mandir-3d-canvas-container" style="position:absolute; inset:0; width:100%; height:100%; cursor:grab; z-index:10; background:#070110;">
      <!-- Three.js WebGL Canvas attaches here -->
    </div>

    <!-- 🧭 360° GESTURE HINT OVERLAY -->
    <div id="mandir-drag-hint" style="position:absolute; top:75px; left:50%; transform:translateX(-50%); z-index:20; background:rgba(0,0,0,0.6); border:1px solid rgba(248,200,59,0.35); border-radius:20px; padding:4px 14px; font-size:0.75rem; font-weight:800; color:#FDE68A; pointer-events:none; display:flex; align-items:center; gap:6px; animation:pulse 2s infinite;">
      <span>🔄</span> 360° परिक्रमा हेतु स्क्रीन पर स्वाइप करें
    </div>

    <!-- 🎮 RIGHT HUD: AUTO-ORBIT TOGGLE -->
    <div style="position:absolute; right:12px; top:120px; z-index:20; display:flex; flex-direction:column; gap:8px;">
      <button id="mandir-auto-orbit-btn" onclick="toggle3DAutoOrbit()" title="स्वतः परिक्रमा चालू/बंद करें" style="width:40px; height:40px; border-radius:14px; background:rgba(42,13,78,0.85); border:1.5px solid #F8C83B; color:#FDE68A; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.6);">
        ▶
      </button>
      <button onclick="reset3DCameraView()" title="कैमरा रीसेट करें" style="width:40px; height:40px; border-radius:14px; background:rgba(42,13,78,0.85); border:1.5px solid rgba(248,200,59,0.4); color:#FFFDF8; font-size:0.95rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.6);">
        🎯
      </button>
    </div>

    <!-- 🪷 BOTTOM FLOATING SEVA ARC & PARIKRAMA PROGRESS BAR -->
    <div style="position:absolute; bottom:0; left:0; right:0; z-index:30; padding:12px 16px 20px; background:linear-gradient(0deg, rgba(10,2,18,0.95) 0%, rgba(10,2,18,0.7) 60%, transparent 100%); backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); display:flex; flex-direction:column; gap:10px;">
      
      <!-- 3 Floating Seva Buttons: Diya, Pushpa, Ghanti -->
      <div style="display:flex; align-items:center; justify-content:center; gap:12px;">
        
        <!-- Seva 1: Diya -->
        <button onclick="trigger3DDiyaGlow()" class="floating-seva-btn" style="padding:8px 14px; border-radius:18px; background:linear-gradient(145deg, #3D1360 0%, #1A052E 100%); border:1.5px solid #F8C83B; color:#FFFDF8; font-size:0.8rem; font-weight:900; cursor:pointer; display:flex; align-items:center; gap:6px; box-shadow:0 4px 15px rgba(248,200,59,0.3); transition:transform 0.15s ease;">
          <span style="font-size:1.2rem;">🪔</span> दीप जलाएं
        </button>

        <!-- Seva 2: Pushpa Varsha -->
        <button onclick="trigger3DPushpaVarsha()" class="floating-seva-btn" style="padding:8px 14px; border-radius:18px; background:linear-gradient(145deg, #3D1360 0%, #1A052E 100%); border:1.5px solid #F8C83B; color:#FFFDF8; font-size:0.8rem; font-weight:900; cursor:pointer; display:flex; align-items:center; gap:6px; box-shadow:0 4px 15px rgba(248,200,59,0.3); transition:transform 0.15s ease;">
          <span style="font-size:1.2rem;">🌸</span> पुष्प वर्षा
        </button>

        <!-- Seva 3: Ghanti Naad -->
        <button onclick="trigger3DGhantiNaad()" class="floating-seva-btn" style="padding:8px 14px; border-radius:18px; background:linear-gradient(145deg, #3D1360 0%, #1A052E 100%); border:1.5px solid #F8C83B; color:#FFFDF8; font-size:0.8rem; font-weight:900; cursor:pointer; display:flex; align-items:center; gap:6px; box-shadow:0 4px 15px rgba(248,200,59,0.3); transition:transform 0.15s ease;">
          <span style="font-size:1.2rem;">🔔</span> घंटी बजाएं
        </button>

      </div>

      <!-- 📊 Parikrama Progress Bar & Counter -->
      <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.35); border-radius:16px; padding:10px 14px;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
          <span style="font-size:0.82rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
            <span>🚩</span> <span id="parikrama-mandir-label">श्री काशी विश्वनाथ परिक्रमा</span>
          </span>
          <span id="parikrama-live-counter" style="font-size:0.88rem; font-weight:900; color:#F8C83B;">
            0 / 11 पूर्ण
          </span>
        </div>
        
        <!-- Progress Bar Fill -->
        <div style="width:100%; height:8px; background:rgba(0,0,0,0.5); border-radius:6px; overflow:hidden; border:1px solid rgba(255,255,255,0.1);">
          <div id="parikrama-progress-fill" style="width:0%; height:100%; background:linear-gradient(90deg, #F8C83B 0%, #FF512F 100%); border-radius:6px; transition:width 0.3s ease; box-shadow:0 0 10px rgba(248,200,59,0.7);"></div>
        </div>
      </div>

    </div>

    <!-- 🏆 PARIKRAMA SANKALP COMPLETED CELEBRATION MODAL 🏆 -->
    <div id="parikrama-completed-modal" style="display:none; position:fixed; inset:0; z-index:200; background:rgba(10,2,18,0.95); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); align-items:center; justify-content:center; padding:1.2rem;">
      <div style="width:100%; max-width:400px; background:linear-gradient(160deg, #2D1047 0%, #1A052E 60%, #0F021B 100%); border:2px solid #F59E0B; border-radius:28px; padding:1.8rem 1.4rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
        
        <div style="font-size:3.8rem; margin-bottom:8px; filter:drop-shadow(0 0 20px #F59E0B);">🏆</div>
        <h2 style="font-size:1.35rem; font-weight:900; color:#F8C83B; margin:0 0 6px 0;">
          ॥ दिव्य परिक्रमा संपन्न ॥
        </h2>
        <p id="parikrama-completed-desc" style="font-size:0.86rem; color:#FFFDF8; margin:0 0 14px 0; line-height:1.5;">
          आपने <strong>श्री काशी विश्वनाथ मंदिर</strong> की <strong>11 पावन परिक्रमा</strong> व संपूर्ण पूजन पूर्ण किया!
        </p>

        <!-- Sadhana Points Awarded Badge -->
        <div style="background:linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(217,119,6,0.1) 100%); border:1.5px solid #F59E0B; border-radius:18px; padding:10px 14px; margin-bottom:16px; display:flex; align-items:center; justify-content:space-between;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.6rem;">🪙</span>
            <div style="text-align:left;">
              <div style="font-size:0.88rem; font-weight:900; color:#FDE68A;">+25 साधना पुण्य अंक!</div>
              <div style="font-size:0.72rem; color:#CBD5E1;">नित्य साधना स्ट्रीक अपडेट हुई 🔥</div>
            </div>
          </div>
          <span style="font-size:0.82rem; font-weight:900; background:#F59E0B; color:#1A0B2E; padding:4px 10px; border-radius:12px;">
            सत्यापित ✓
          </span>
        </div>

        <!-- 📲 WhatsApp Share Button -->
        <button onclick="share3DParikramaWhatsApp()" style="width:100%; background:#25D366; color:#FFF; border:none; font-size:0.92rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; box-shadow:0 4px 15px rgba(37,211,102,0.4); margin-bottom:10px;">
          <span>📲</span> WhatsApp पर परिक्रमा पुण्य शेयर करें 🚩
        </button>

        <!-- Exit / Pranam Button -->
        <button onclick="close3DParikramaCompletedModal()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.92rem; font-weight:900; padding:11px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4);">
          प्रणाम स्वीकारें 🙏
        </button>

      </div>
    </div>

  </div>
"""

# Append 3D Mandir Modal right before </body>
if 'id="mandir-3d-modal"' not in html:
    html = html.replace('</body>', mandir_3d_viewport_html + '\n</body>')

# Bump cache busters
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with 3D Mandir & Parikrama Modal and Home Card (v={ts})")
