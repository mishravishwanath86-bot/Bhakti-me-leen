import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html for page-jar and Bhojpatra / Vault Modals
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modern_amrit_jar_html = """    <!-- 🏺 BHAKTI AMRIT KALASH (3D INTERACTIVE & AI VOICE REVEAL ENGINE) 🏺 -->
    <section id="page-jar" class="page">
      
      <!-- Top Bar -->
      <div class="page-header-bar" style="background:rgba(10,2,18,0.85); backdrop-filter:blur(10px); border-bottom:1px solid rgba(248,200,59,0.25);">
        <button class="back-btn" onclick="showPage('page-home')">❮</button>
        <h2 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
          <span>🏺</span> भक्ति अमृत कलश
        </h2>
        <button onclick="openAmritVaultModal()" style="background:rgba(248,200,59,0.18); border:1.2px solid #F8C83B; color:#FDE68A; padding:4px 10px; border-radius:14px; font-size:0.75rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:4px; box-shadow:0 0 10px rgba(248,200,59,0.2);">
          <span>📜</span> अमृत संग्रह
        </button>
      </div>

      <div style="padding: 0 1rem 1.2rem;">
        
        <!-- Hero Section: 3D Floating Golden Kalash Canvas -->
        <div style="background: radial-gradient(circle at 50% 40%, #2E0B4E 0%, #170428 65%, #0A0114 100%); border: 1.5px solid rgba(248,200,59,0.4); border-radius: 26px; padding: 1.2rem 1rem; text-align: center; margin-bottom: 1.2rem; box-shadow: 0 12px 35px rgba(0,0,0,0.7), 0 0 20px rgba(248,200,59,0.12) inset; position: relative; overflow: hidden;">
          
          <!-- 3D Three.js Kalash Container -->
          <div id="kalash-3d-canvas-container" style="width:100%; height:190px; margin:0 auto; cursor:pointer; position:relative;" onclick="trigger3DKalashInteraction()" title="कलश स्पर्श करें">
            <!-- Three.js Canvas attaches here -->
          </div>

          <div style="font-size: 1.05rem; font-weight: 900; color: #F8C83B; margin-top: 4px; text-shadow: 0 0 12px rgba(248,200,59,0.4);">
            ॥ मन का मंथन करें, दिव्य अमृत पाएं ॥
          </div>
          <p style="font-size: 0.78rem; color: #CBD5E1; margin: 4px 0 0 0; line-height: 1.4;">
            अपनी वर्तमान मनःस्थिति चुनें या बोलकर बताएं — भगवान श्री कृष्ण का मार्गदर्शन प्राप्त करें।
          </p>
        </div>

        <!-- 6 Dark Glassmorphic Emotion Chips Grid -->
        <div style="margin-bottom: 1.2rem;">
          <div style="font-size: 0.85rem; font-weight: 900; color: #FDE68A; margin-bottom: 8px; display:flex; align-items:center; gap:6px;">
            <span>✨</span> अपनी वर्तमान मनःस्थिति का चयन करें:
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            
            <!-- Mood 1: Anxious / Overthink -->
            <button onclick="revealAmritWisdom('anxious')" class="amrit-mood-card" style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 10px; cursor:pointer; text-align:left; display:flex; align-items:center; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.4); transition:all 0.15s ease;">
              <div style="width:40px; height:40px; border-radius:14px; background:rgba(239,68,68,0.2); border:1px solid #EF4444; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
                🌪️
              </div>
              <div>
                <div style="color:#FFFDF8; font-weight:900; font-size:0.85rem; line-height:1.2;">अशांत / व्याकुल</div>
                <div style="color:#FCA5A5; font-size:0.68rem; font-weight:700; margin-top:2px;">Anxiety • Overthink</div>
              </div>
            </button>

            <!-- Mood 2: Peace / Stillness -->
            <button onclick="revealAmritWisdom('peace')" class="amrit-mood-card" style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 10px; cursor:pointer; text-align:left; display:flex; align-items:center; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.4); transition:all 0.15s ease;">
              <div style="width:40px; height:40px; border-radius:14px; background:rgba(16,185,129,0.2); border:1px solid #10B981; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
                🪷
              </div>
              <div>
                <div style="color:#FFFDF8; font-weight:900; font-size:0.85rem; line-height:1.2;">शांति / ध्यान</div>
                <div style="color:#A7F3D0; font-size:0.68rem; font-weight:700; margin-top:2px;">Peace • Stillness</div>
              </div>
            </button>

            <!-- Mood 3: Sadness / Low Energy -->
            <button onclick="revealAmritWisdom('sad')" class="amrit-mood-card" style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 10px; cursor:pointer; text-align:left; display:flex; align-items:center; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.4); transition:all 0.15s ease;">
              <div style="width:40px; height:40px; border-radius:14px; background:rgba(139,92,246,0.2); border:1px solid #8B5CF6; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
                💔
              </div>
              <div>
                <div style="color:#FFFDF8; font-weight:900; font-size:0.85rem; line-height:1.2;">निराशा / दुःख</div>
                <div style="color:#DDD6FE; font-size:0.68rem; font-weight:700; margin-top:2px;">Sadness • Low Energy</div>
              </div>
            </button>

            <!-- Mood 4: Fear / Courage Needed -->
            <button onclick="revealAmritWisdom('fear')" class="amrit-mood-card" style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 10px; cursor:pointer; text-align:left; display:flex; align-items:center; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.4); transition:all 0.15s ease;">
              <div style="width:40px; height:40px; border-radius:14px; background:rgba(245,158,11,0.2); border:1px solid #F59E0B; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
                ⚔️
              </div>
              <div>
                <div style="color:#FFFDF8; font-weight:900; font-size:0.85rem; line-height:1.2;">भय / साहस</div>
                <div style="color:#FDE68A; font-size:0.68rem; font-weight:700; margin-top:2px;">Fear • Courage</div>
              </div>
            </button>

            <!-- Mood 5: Grateful / Joyful -->
            <button onclick="revealAmritWisdom('grateful')" class="amrit-mood-card" style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 10px; cursor:pointer; text-align:left; display:flex; align-items:center; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.4); transition:all 0.15s ease;">
              <div style="width:40px; height:40px; border-radius:14px; background:rgba(236,72,153,0.2); border:1px solid #EC4899; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
                🌸
              </div>
              <div>
                <div style="color:#FFFDF8; font-weight:900; font-size:0.85rem; line-height:1.2;">कृतज्ञ / आनंद</div>
                <div style="color:#FBCFE8; font-size:0.68rem; font-weight:700; margin-top:2px;">Grateful • Joyful</div>
              </div>
            </button>

            <!-- Mood 6: Doubt / Clarity -->
            <button onclick="revealAmritWisdom('doubt')" class="amrit-mood-card" style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px 10px; cursor:pointer; text-align:left; display:flex; align-items:center; gap:10px; box-shadow:0 4px 15px rgba(0,0,0,0.4); transition:all 0.15s ease;">
              <div style="width:40px; height:40px; border-radius:14px; background:rgba(59,130,246,0.2); border:1px solid #3B82F6; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0;">
                ⚖️
              </div>
              <div>
                <div style="color:#FFFDF8; font-weight:900; font-size:0.85rem; line-height:1.2;">अनिर्णय / भ्रम</div>
                <div style="color:#BFDBFE; font-size:0.68rem; font-weight:700; margin-top:2px;">Doubt • Clarity</div>
              </div>
            </button>

          </div>
        </div>

        <!-- Floating AI Voice Input Mic Bar -->
        <div style="background:linear-gradient(135deg, #3B1259 0%, #1A052E 100%); border:1.5px solid #F8C83B; border-radius:20px; padding:12px 14px; box-shadow:0 6px 20px rgba(0,0,0,0.5); display:flex; align-items:center; justify-content:space-between; gap:10px;">
          <div style="flex:1;">
            <div style="font-size:0.82rem; font-weight:900; color:#FDE68A; display:flex; align-items:center; gap:6px;">
              <span>🤖</span> AI वैदिक वॉइस गाइड
            </div>
            <div id="ai-voice-bar-subtext" style="font-size:0.72rem; color:#CBD5E1; margin-top:2px;">
              अपनी समस्या बोलकर बताएं (उदा. "मुझे भविष्य की चिंता है")
            </div>
          </div>

          <button id="amrit-mic-btn" onclick="startAIVoiceMoodRecognition()" style="width:46px; height:46px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); border:none; color:#1A0B2E; font-size:1.35rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 15px rgba(248,200,59,0.5); flex-shrink:0; transition:transform 0.15s ease;">
            🎤
          </button>
        </div>

      </div>
      <div style="height:6rem"></div>
    </section>

    <!-- 📜 BHOJPATRA SCROLL REVEAL MODAL (भोजपत्र समाधान) 📜 -->
    <div id="amrit-bhojpatra-modal" style="display:none; position:fixed; inset:0; z-index:100100; background:rgba(10,2,18,0.94); backdrop-filter:blur(22px); -webkit-backdrop-filter:blur(22px); align-items:center; justify-content:center; padding:1.2rem;">
      <div style="width:100%; max-width:400px; background:radial-gradient(circle at 50% 30%, #351352 0%, #1B062C 60%, #0D0218 100%); border:2px solid #F59E0B; border-radius:28px; padding:1.6rem 1.3rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease; max-height:90vh; overflow-y:auto;">
        
        <!-- Header Tag & Close -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:4px 12px; border-radius:12px; font-size:0.75rem; font-weight:900;">
            <span id="bhojpatra-source-tag">📜 श्रीमद्भगवद्गीता (2.47)</span>
          </div>
          <button onclick="closeAmritBhojpatraModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:30px; height:30px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>

        <!-- Layer 1: Mool Sanskrit Shlok Box -->
        <div style="background:rgba(248,200,59,0.1); border:1.2px solid rgba(248,200,59,0.35); border-radius:18px; padding:14px; margin-bottom:12px; text-align:center;">
          <div id="bhojpatra-sanskrit-text" style="font-family:'Tiro Devanagari Hindi', serif; font-size:1.15rem; font-weight:700; color:#FFFDF8; line-height:1.6; margin-bottom:8px; text-shadow:0 0 12px rgba(248,200,59,0.3);">
            कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।<br>मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥
          </div>
          
          <button onclick="playCurrentShlokaVoice()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.75rem; font-weight:900; padding:5px 14px; border-radius:12px; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 2px 10px rgba(248,200,59,0.35);">
            <span>🔊</span> दिव्य वाणी सुनें (Audio)
          </button>
        </div>

        <!-- Layer 2: Divya Arth (Simplified Wisdom) -->
        <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.12); border-radius:16px; padding:12px; margin-bottom:12px;">
          <div style="font-size:0.78rem; font-weight:900; color:#F8C83B; margin-bottom:4px;">
            💡 दिव्य अर्थ (सरल भावार्थ):
          </div>
          <div id="bhojpatra-hindi-meaning" style="font-size:0.84rem; color:#FFFDF8; line-height:1.5;">
            तुम्हारा अधिकार केवल अपने कर्तव्य कर्म पर है, उसके फल पर कभी नहीं। फल की चिंता छोड़कर निष्काम भाव से कार्य करो।
          </div>
        </div>

        <!-- Layer 3: Aaj Ka Karma (Actionable Resolution) -->
        <div style="background:rgba(16,185,129,0.15); border:1.2px solid #10B981; border-radius:16px; padding:12px; margin-bottom:16px;">
          <div style="font-size:0.78rem; font-weight:900; color:#34D399; margin-bottom:4px; display:flex; align-items:center; gap:6px;">
            <span>🎯</span> आज का संकल्प / कर्म (Action):
          </div>
          <div id="bhojpatra-action-karma" style="font-size:0.82rem; color:#FFFDF8; line-height:1.4;">
            2 मिनट आंखें बंद करके गहरी सांस लें और 11 बार ॐ का उच्चारण करके चिंता प्रभु को समर्पित करें।
          </div>
        </div>

        <!-- Action Buttons -->
        <div style="display:flex; flex-direction:column; gap:8px;">
          <button onclick="saveCurrentShlokaToVault()" id="vault-save-btn" style="width:100%; background:linear-gradient(135deg, #EC4899, #BE185D); color:#FFF; border:none; font-size:0.88rem; font-weight:900; padding:11px 0; border-radius:14px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px; box-shadow:0 4px 15px rgba(236,72,153,0.35);">
            <span>💾</span> अमृत संग्रह में सहेजें (Save)
          </button>

          <button onclick="shareCurrentShlokaWhatsApp()" style="width:100%; background:#25D366; color:#FFF; border:none; font-size:0.88rem; font-weight:900; padding:11px 0; border-radius:14px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px; box-shadow:0 4px 15px rgba(37,211,102,0.35);">
            <span>📲</span> WhatsApp पर दिव्य स्टेटस शेयर करें
          </button>
        </div>

      </div>
    </div>

    <!-- 📜 AMRIT VAULT (SAVED SHLOKA VAULT MODAL) 📜 -->
    <div id="amrit-vault-modal" style="display:none; position:fixed; inset:0; z-index:100110; background:rgba(10,2,18,0.94); backdrop-filter:blur(22px); -webkit-backdrop-filter:blur(22px); align-items:center; justify-content:center; padding:1.2rem;">
      <div style="width:100%; max-width:420px; background:linear-gradient(160deg, #2D1047 0%, #1A052E 60%, #0F021B 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.6rem 1.3rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease; max-height:85vh; display:flex; flex-direction:column;">
        
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="font-size:1.1rem; font-weight:900; color:#F8C83B; display:flex; align-items:center; gap:6px;">
            <span>📜</span> सहेजा गया अमृत संग्रह (Vault)
          </div>
          <button onclick="closeAmritVaultModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:30px; height:30px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>

        <div id="amrit-vault-list" style="flex:1; overflow-y:auto; display:flex; flex-direction:column; gap:10px; padding-right:4px;">
          <!-- Dynamically populated via renderAmritVaultList() -->
        </div>

      </div>
    </div>

    <!-- 🎙️ VOICE LISTENING OVERLAY (ACTIVE RECORDING PREVIEW) 🎙️ -->
    <div id="voice-listening-overlay" style="display:none; position:fixed; inset:0; z-index:100120; background:rgba(10,2,18,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); flex-direction:column; align-items:center; justify-content:center; padding:1.5rem; text-align:center;">
      
      <!-- Pulsing Mic Orb -->
      <div style="width:80px; height:80px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #D97706 70%); border:3px solid #FEF3C7; display:flex; align-items:center; justify-content:center; font-size:2.2rem; box-shadow:0 0 35px rgba(248,200,59,0.8); animation:pulseGlow 1.5s infinite; margin-bottom:16px;">
        🎤
      </div>

      <h3 style="font-size:1.25rem; font-weight:900; color:#F8C83B; margin:0 0 6px 0;">
        सुन रहे हैं... अपनी बात कहें
      </h3>
      <p style="font-size:0.8rem; color:#CBD5E1; margin:0 0 16px 0;">
        (उदा. "मुझे व्यापार में चिंता हो रही है" या "मन अशांत है")
      </p>

      <!-- Live Transcription Transcript Preview -->
      <div id="voice-transcript-preview" style="width:100%; max-width:320px; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); border-radius:18px; padding:12px; font-size:0.9rem; font-weight:700; color:#FFFDF8; min-height:48px; display:flex; align-items:center; justify-content:center; margin-bottom:20px;">
        बोलना शुरू करें...
      </div>

      <button onclick="stopAIVoiceMoodRecognition()" style="background:rgba(239,68,68,0.25); border:1.5px solid #EF4444; color:#FCA5A5; font-size:0.85rem; font-weight:800; padding:8px 24px; border-radius:16px; cursor:pointer;">
        रद्द करें (Cancel)
      </button>

    </div>
"""

# Replace in index.html
s_jar = html.find('<!-- 🏺 BHAKTI AMRIT JAR PAGE')
if s_jar != -1:
    e_jar = html.find('<!-- 📿 INTERACTIVE DIGITAL JAPA MALA', s_jar)
    html = html[:s_jar] + modern_amrit_jar_html + "\n\n    " + html[e_jar:]

# Bump cache buster
ts = int(time.time())
html = re.sub(r'amrit_kalash_3d_engine\.js\?v=\d+', f'amrit_kalash_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with 3D Kalash Viewport, Bhojpatra Scroll & Voice Overlay (v={ts})")
