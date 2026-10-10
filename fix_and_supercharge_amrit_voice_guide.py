import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html: Move scripts to bottom, add dedicated Vedic Voice Modal, add drawer item
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove scripts from the middle if present
html = re.sub(r'<script src="mandir_3d_engine\.js(\?v=\d+)?"><\/script>\s*', '', html)
html = re.sub(r'<script src="amrit_kalash_3d_engine\.js(\?v=\d+)?"><\/script>\s*', '', html)
html = re.sub(r'<script src="app\.js(\?v=\d+)?"><\/script>\s*', '', html)

# Add drawer item for Amrit Kalash if missing
drawer_btn = '<button class="drawer-item" onclick="showPage(\'page-jar\'); const d=document.querySelector(\'.side-drawer\'); if(d) d.classList.remove(\'open\'); const o=document.getElementById(\'overlay\'); if(o) o.style.display=\'none\';"><span class="di">🏺</span><span>भक्ति अमृत कलश</span></button>'
if '<span>भक्ति अमृत कलश</span>' not in html:
    html = html.replace(
        '<button class="drawer-item" id="drawer-downloads">',
        drawer_btn + '\n      <button class="drawer-item" id="drawer-downloads">'
    )
    print("✓ Added Amrit Kalash button in Drawer navigation")

# Dedicated AI Voice Modal HTML
vedic_voice_modal_html = """
  <!-- 🎙️ DEDICATED SMART AI VEDIC VOICE GUIDE MODAL 🎙️ -->
  <div id="vedic-ai-voice-modal" style="display:none; position:fixed; inset:0; z-index:100300; background:rgba(10,2,18,0.96); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div style="width:100%; max-width:420px; background:radial-gradient(circle at 50% 25%, #380C5E 0%, #1A052E 60%, #0A0114 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.6rem 1.3rem; text-align:center; box-shadow:0 25px 80px rgba(0,0,0,0.95), 0 0 30px rgba(248,200,59,0.25) inset; position:relative; animation:fadeInUp 0.3s ease; max-height:92vh; overflow-y:auto;">
      
      <!-- Close Button -->
      <button onclick="closeAIVoiceModal()" style="position:absolute; top:14px; right:14px; background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>

      <!-- Header Tag -->
      <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:4px 14px; border-radius:16px; font-size:0.75rem; font-weight:900; margin-bottom:10px;">
        <span>🤖</span> AI वैदिक वॉइस गाइड
      </div>

      <h3 style="color:#FFFDF8; font-size:1.3rem; font-weight:900; margin:0 0 4px 0;">
        प्रभु से अपनी बात कहें
      </h3>
      <p id="vedic-voice-modal-sub" style="color:#CBD5E1; font-size:0.78rem; margin:0 0 16px 0;">
        अपनी समस्या या मनोभाव बोलें — AI तुरंत श्रीमद्भगवद्गीता से समाधान खोजेगा
      </p>

      <!-- Central Animated Glowing Mic Stage -->
      <div style="position:relative; width:130px; height:130px; margin:0 auto 16px; display:flex; align-items:center; justify-content:center;">
        <div id="vedic-voice-pulse-ring" style="position:absolute; inset:0; border-radius:50%; background:radial-gradient(circle, rgba(248,200,59,0.4) 0%, rgba(217,119,6,0.1) 70%, transparent 100%); border:2px solid #F8C83B; animation:pulseGlow 1.2s infinite;"></div>
        
        <button id="vedic-voice-mic-main-btn" onclick="toggleSpeechRecording()" style="width:84px; height:84px; border-radius:50%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); border:3px solid #FEF3C7; color:#1A0B2E; font-size:2.4rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 30px rgba(248,200,59,0.8); z-index:2; transition:transform 0.15s ease;">
          🎤
        </button>
      </div>

      <!-- Live Voice Status / Transcript Box -->
      <div style="background:rgba(0,0,0,0.45); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px; margin-bottom:16px; min-height:48px; display:flex; align-items:center; justify-content:center;">
        <div id="vedic-voice-live-transcript" style="font-size:0.85rem; font-weight:800; color:#34D399; line-height:1.4;">
          🎙️ माइक पर स्पर्श करें या नीचे दिए गए भावों में से चुनें...
        </div>
      </div>

      <!-- Manual Text Input Box (Alternative to Voice) -->
      <div style="display:flex; gap:6px; margin-bottom:14px;">
        <input type="text" id="vedic-voice-text-input" placeholder="या यहाँ समस्या लिखें (उदा. चिंता, दुःख, भय)..." style="flex:1; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.35); border-radius:14px; padding:9px 12px; color:#FFFDF8; font-size:0.82rem; outline:none;" onkeypress="if(event.key==='Enter') submitManualVedicQuery()" />
        <button onclick="submitManualVedicQuery()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.85rem; font-weight:900; padding:0 14px; border-radius:14px; cursor:pointer;">
          ➔
        </button>
      </div>

      <!-- Quick 1-Tap Voice Prompts Chips -->
      <div style="text-align:left; margin-bottom:6px;">
        <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-bottom:6px;">
          ✨ त्वरित जिज्ञासा (1-टैप में समाधान):
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          <button onclick="selectQuickVoicePrompt('मुझे भविष्य की बहुत चिंता है')" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.72rem; font-weight:700; padding:5px 10px; border-radius:12px; cursor:pointer;">
            🌪️ भविष्य की चिंता
          </button>
          <button onclick="selectQuickVoicePrompt('मन अशांत है शांति कैसे मिले')" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.72rem; font-weight:700; padding:5px 10px; border-radius:12px; cursor:pointer;">
            🪷 मन अशांत है
          </button>
          <button onclick="selectQuickVoicePrompt('बहुत दुःख और निराशा हो रही है')" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.72rem; font-weight:700; padding:5px 10px; border-radius:12px; cursor:pointer;">
            💔 दुःख व निराशा
          </button>
          <button onclick="selectQuickVoicePrompt('अत्यंत भय लग रहा है साहस चाहिए')" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.72rem; font-weight:700; padding:5px 10px; border-radius:12px; cursor:pointer;">
            ⚔️ भय व साहस
          </button>
          <button onclick="selectQuickVoicePrompt('कोई निर्णय नहीं ले पा रहा')" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.72rem; font-weight:700; padding:5px 10px; border-radius:12px; cursor:pointer;">
            ⚖️ निर्णय व भ्रम
          </button>
          <button onclick="selectQuickVoicePrompt('प्रभु का आभार व आनंद व्यक्त करना है')" style="background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.72rem; font-weight:700; padding:5px 10px; border-radius:12px; cursor:pointer;">
            🌸 प्रभु का आभार
          </button>
        </div>
      </div>

    </div>
  </div>
"""

if 'id="vedic-ai-voice-modal"' not in html:
    html = html.replace('<!-- 📜 BHOJPATRA SCROLL REVEAL MODAL', vedic_voice_modal_html + '\n    <!-- 📜 BHOJPATRA SCROLL REVEAL MODAL')
    print("✓ Added #vedic-ai-voice-modal to index.html")

ts = int(time.time())

# Append core scripts right before </body>
core_scripts_html = f"""
  <script src="mandir_3d_engine.js?v={ts}"></script>
  <script src="amrit_kalash_3d_engine.js?v={ts}"></script>
  <script src="app.js?v={ts}"></script>
"""

html = re.sub(r'<\/body>', core_scripts_html + '\n</body>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Moved core scripts to bottom of index.html (v={ts})")
