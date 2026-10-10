import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modals_html = """
  <!-- ═══════════════════════════════════════════════════════════════════════════
       🏆 VEDIC RANKS & BADGES MODAL (वैदिक साधना पदवियां) 🏆
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="vedic-ranks-modal" style="display:none; position:fixed; inset:0; z-index:100085; background:rgba(7,1,16,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:400px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <!-- Header -->
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; border-bottom:1px solid rgba(248,200,59,0.25); padding-bottom:10px;">
        <div>
          <h3 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:6px;">
            <span>🔱</span> वैदिक साधना पदवियां
          </h3>
          <div style="font-size:0.72rem; color:#FDE68A; font-weight:700; margin-top:2px;">Vedic Sadhana Milestones & Rewards</div>
        </div>
        <button onclick="closeVedicRanksModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
      </div>

      <!-- Rank List -->
      <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:16px; max-height:340px; overflow-y:auto;">
        
        <!-- Rank 1: 7 Days Sadhak -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:16px; padding:10px 12px; display:flex; align-items:center; gap:10px;">
          <div style="font-size:1.8rem;">🌿</div>
          <div style="flex:1;">
            <div style="display:flex; align-items:center; justify-content:space-between;">
              <strong style="color:#FDE68A; font-size:0.85rem;">साधक (Sadhak)</strong>
              <span style="font-size:0.68rem; background:rgba(248,200,59,0.2); color:#FDE68A; padding:2px 8px; border-radius:8px; font-weight:800;">7 दिन स्ट्रीक</span>
            </div>
            <div style="font-size:0.72rem; color:#CBD5E1; margin-top:2px;">🏆 <strong>स्वर्ण ऐप आइकन:</strong> दिव्य गोल्ड थीम अनलॉक!</div>
          </div>
        </div>

        <!-- Rank 2: 21 Days Tapaswi (Active) -->
        <div style="background:linear-gradient(135deg, rgba(248,200,59,0.18) 0%, rgba(217,119,6,0.12) 100%); border:1.5px solid #F8C83B; border-radius:16px; padding:10px 12px; display:flex; align-items:center; gap:10px; box-shadow:0 0 15px rgba(248,200,59,0.25);">
          <div style="font-size:1.8rem;">🔱</div>
          <div style="flex:1;">
            <div style="display:flex; align-items:center; justify-content:space-between;">
              <strong style="color:#FFFDF8; font-size:0.88rem;">तपस्वी (Tapaswi) ⭐ वर्तमान</strong>
              <span style="font-size:0.68rem; background:#F8C83B; color:#1A0B2E; padding:2px 8px; border-radius:8px; font-weight:900;">21 दिन स्ट्रीक</span>
            </div>
            <div style="font-size:0.72rem; color:#FDE68A; margin-top:2px;">🔔 <strong>मंदिर घंटा नाद:</strong> विशेष शंख व घंटा ध्वनि अनलॉक!</div>
          </div>
        </div>

        <!-- Rank 3: 51 Days Siddha Sadhak -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(255,255,255,0.1); border-radius:16px; padding:10px 12px; display:flex; align-items:center; gap:10px;">
          <div style="font-size:1.8rem;">🪔</div>
          <div style="flex:1;">
            <div style="display:flex; align-items:center; justify-content:space-between;">
              <strong style="color:#CBD5E1; font-size:0.85rem;">सिद्ध साधक (Siddha Sadhak)</strong>
              <span style="font-size:0.68rem; background:rgba(255,255,255,0.1); color:#CBD5E1; padding:2px 8px; border-radius:8px; font-weight:800;">51 दिन स्ट्रीक</span>
            </div>
            <div style="font-size:0.72rem; color:#94A3B8; margin-top:2px;">⚡ <strong>1.5x पुण्य मल्टीप्लायर:</strong> 50% अधिक पुण्य अंक!</div>
          </div>
        </div>

        <!-- Rank 4: 108 Days Rishi Kalp -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(255,255,255,0.1); border-radius:16px; padding:10px 12px; display:flex; align-items:center; gap:10px;">
          <div style="font-size:1.8rem;">👑</div>
          <div style="flex:1;">
            <div style="display:flex; align-items:center; justify-content:space-between;">
              <strong style="color:#CBD5E1; font-size:0.85rem;">ऋषि कल्प (Rishi Kalp)</strong>
              <span style="font-size:0.68rem; background:rgba(255,255,255,0.1); color:#CBD5E1; padding:2px 8px; border-radius:8px; font-weight:800;">108 दिन स्ट्रीक</span>
            </div>
            <div style="font-size:0.72rem; color:#94A3B8; margin-top:2px;">📜 <strong>वैदिक प्रमाणपत्र:</strong> डिजिटल सिद्धि पत्र व शंखनाद!</div>
          </div>
        </div>

      </div>

      <button onclick="closeVedicRanksModal()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.9rem; font-weight:900; padding:11px 0; border-radius:14px; cursor:pointer;">
        समझ गया (बंद करें)
      </button>

    </div>
  </div>


  <!-- ═══════════════════════════════════════════════════════════════════════════
       📿 DEDICATE JAP TO SANGHA MODAL (जप समर्पण) 📿
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="dedicate-jap-modal" style="display:none; position:fixed; inset:0; z-index:100085; background:rgba(7,1,16,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:380px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <div style="font-size:2.8rem; margin-bottom:8px; filter:drop-shadow(0 0 15px #F59E0B);">📿</div>
      <h3 style="font-size:1.2rem; font-weight:900; color:#FFFDF8; margin:0 0 6px 0;">
        आज के जप समर्पित करें
      </h3>
      <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 16px 0;">
        अपने व्यक्तिगत जप को <strong>महा-अनुष्ठान</strong> में जोड़ें और पुण्य लाभ प्राप्त करें:
      </p>

      <!-- Quick Count Buttons -->
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:14px;">
        <button onclick="submitDedicatedJap(108)" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:0.85rem; font-weight:900; padding:10px 0; border-radius:14px; cursor:pointer;">
          📿 1 माला (108)
        </button>
        <button onclick="submitDedicatedJap(216)" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:0.85rem; font-weight:900; padding:10px 0; border-radius:14px; cursor:pointer;">
          📿 2 माला (216)
        </button>
        <button onclick="submitDedicatedJap(540)" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:0.85rem; font-weight:900; padding:10px 0; border-radius:14px; cursor:pointer;">
          📿 5 माला (540)
        </button>
        <button onclick="submitDedicatedJap(1008)" style="background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:0.85rem; font-weight:900; padding:10px 0; border-radius:14px; cursor:pointer;">
          🌟 1,008 महा-जप
        </button>
      </div>

      <!-- Custom Input -->
      <div style="margin-bottom:16px;">
        <input type="number" id="custom-jap-dedicate-input" placeholder="या अन्य जप संख्या दर्ज करें..." style="width:100%; background:rgba(0,0,0,0.4); border:1.5px solid rgba(248,200,59,0.4); border-radius:14px; padding:10px 12px; color:#FFFDF8; font-size:0.85rem; outline:none; text-align:center;">
      </div>

      <div style="display:flex; gap:8px;">
        <button onclick="closeDedicateJapModal()" style="flex:1; background:rgba(255,255,255,0.1); border:none; color:#CBD5E1; font-weight:800; padding:11px 0; border-radius:14px; cursor:pointer;">
          रद्द करें
        </button>
        <button onclick="submitDedicatedJap(0)" style="flex:2; background:linear-gradient(135deg, #FF8C00 0%, #FF512F 100%); color:#FFF; border:none; font-weight:900; font-size:0.88rem; padding:11px 0; border-radius:14px; cursor:pointer; box-shadow:0 4px 15px rgba(255,81,47,0.4);">
          समर्पित करें ➔
        </button>
      </div>

    </div>
  </div>


  <!-- ═══════════════════════════════════════════════════════════════════════════
       ➕ ADD SANGHA MEMBER MODAL (सदस्य जोड़ें) ➕
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="add-sangha-member-modal" style="display:none; position:fixed; inset:0; z-index:100085; background:rgba(7,1,16,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:380px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <div style="font-size:2.8rem; margin-bottom:8px;">👨‍👩‍👧‍👦</div>
      <h3 style="font-size:1.2rem; font-weight:900; color:#FFFDF8; margin:0 0 6px 0;">
        परिवार व मित्रों को जोड़ें
      </h3>
      <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 16px 0;">
        इस आमंत्रण कोड से परिवार के सदस्यों को महा-अनुष्ठान में शामिल करें:
      </p>

      <!-- Invite Code Box -->
      <div style="background:rgba(0,0,0,0.4); border:1.5px dashed #F8C83B; border-radius:16px; padding:14px; margin-bottom:14px;">
        <div style="font-size:0.7rem; color:#CBD5E1; margin-bottom:4px;">सामूहिक मंडल कोड (Invite Code)</div>
        <div style="font-size:1.6rem; font-weight:900; color:#F8C83B; letter-spacing:4px;">OM1008</div>
        <button onclick="copySanghaInviteCode()" style="margin-top:8px; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; font-size:0.75rem; font-weight:800; padding:5px 12px; border-radius:10px; cursor:pointer;">
          📋 कोड कॉपी करें
        </button>
      </div>

      <!-- Action Buttons -->
      <button onclick="shareSanghaProgressWhatsApp()" style="width:100%; background:linear-gradient(135deg, #25D366 0%, #128C7E 100%); color:#FFF; border:none; font-size:0.88rem; font-weight:900; padding:11px 0; border-radius:14px; cursor:pointer; box-shadow:0 4px 15px rgba(37,211,102,0.35); margin-bottom:8px; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>📲</span> WhatsApp पर निमंत्रण भेजें
      </button>

      <button onclick="closeAddMemberModal()" style="width:100%; background:rgba(255,255,255,0.1); border:none; color:#CBD5E1; font-weight:800; padding:10px 0; border-radius:14px; cursor:pointer;">
        बंद करें
      </button>

    </div>
  </div>


  <!-- ═══════════════════════════════════════════════════════════════════════════
       👥 CREATE / JOIN SANGHA MODAL (नया मंडल बनाएं या जुड़ें) 👥
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="create-join-sangha-modal" style="display:none; position:fixed; inset:0; z-index:100085; background:rgba(7,1,16,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:390px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; border-bottom:1px solid rgba(248,200,59,0.25); padding-bottom:8px;">
        <h3 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0;">
          👥 सामूहिक साधना मंडल
        </h3>
        <button onclick="closeCreateJoinSanghaModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:30px; height:30px; border-radius:50%; font-size:1rem; cursor:pointer;">✕</button>
      </div>

      <!-- Option 1: Create New Circle -->
      <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px; margin-bottom:12px;">
        <div style="font-size:0.85rem; font-weight:900; color:#FDE68A; margin-bottom:8px;">
          ➕ नया साधना मंडल (अनुष्ठान) बनाएं
        </div>
        <input type="text" id="new-sangha-title-input" placeholder="उदा. 'हनुमान चालीसा 1,008 पाठ'..." style="width:100%; background:rgba(0,0,0,0.4); border:1px solid rgba(248,200,59,0.3); border-radius:12px; padding:8px 10px; color:#FFFDF8; font-size:0.8rem; margin-bottom:8px; outline:none;">
        
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:8px;">
          <input type="number" id="new-sangha-target-input" placeholder="लक्ष्य संख्या (10,000)" style="background:rgba(0,0,0,0.4); border:1px solid rgba(248,200,59,0.3); border-radius:12px; padding:8px 10px; color:#FFFDF8; font-size:0.8rem; outline:none;">
          <select id="new-sangha-mantra-select" style="background:#2A0D4E; border:1px solid rgba(248,200,59,0.3); border-radius:12px; padding:8px 10px; color:#FFFDF8; font-size:0.75rem; outline:none;">
            <option value="महामृत्युंजय मंत्र">महामृत्युंजय मंत्र</option>
            <option value="हनुमान चालीसा">हनुमान चालीसा</option>
            <option value="गायत्री मंत्र">गायत्री मंत्र</option>
            <option value="राम नाम जप">राम नाम जप</option>
          </select>
        </div>

        <button onclick="createNewSanghaCircle()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.8rem; font-weight:900; padding:8px 0; border-radius:12px; cursor:pointer;">
          नया मंडल बनाएं ➔
        </button>
      </div>

      <!-- Option 2: Join Existing Circle -->
      <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(255,255,255,0.15); border-radius:18px; padding:12px;">
        <div style="font-size:0.85rem; font-weight:900; color:#CBD5E1; margin-bottom:8px;">
          🤝 कोड द्वारा मंडल से जुड़ें
        </div>
        <div style="display:flex; gap:8px;">
          <input type="text" id="join-sangha-code-input" placeholder="आमंत्रण कोड (उदा. OM1008)" style="flex:1; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.2); border-radius:12px; padding:8px 10px; color:#FFFDF8; font-size:0.8rem; text-transform:uppercase; outline:none;">
          <button onclick="joinSanghaCircle()" style="background:linear-gradient(135deg, #10B981, #059669); color:#FFF; border:none; font-size:0.8rem; font-weight:900; padding:8px 14px; border-radius:12px; cursor:pointer;">
            जुड़ें ➔
          </button>
        </div>
      </div>

    </div>
  </div>


  <!-- ═══════════════════════════════════════════════════════════════════════════
       🛡️ STREAK RESCUE CELEBRATION MODAL (संकल्प रक्षा कवच सक्रिय) 🛡️
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="streak-rescue-celebration-modal" style="display:none; position:fixed; inset:0; z-index:100095; background:rgba(7,1,16,0.95); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:390px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F59E0B; border-radius:28px; padding:1.8rem 1.4rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <div style="font-size:3.5rem; margin-bottom:8px; filter:drop-shadow(0 0 20px #F59E0B);">🛡️</div>
      <h2 style="font-size:1.3rem; font-weight:900; color:#F8C83B; margin:0 0 6px 0;">
        ॥ संकल्प रक्षा कवच सक्रिय ॥
      </h2>
      <p id="streak-rescue-desc" style="font-size:0.85rem; color:#FFFDF8; margin:0 0 16px 0; line-height:1.5;">
        आपका नियम छूटा था, परंतु <strong>1 रक्षा कवच</strong> ने स्वतः सक्रिय होकर आपकी <strong>21-दिन की पावन स्ट्रीक</strong> को टूटने से बचा लिया! 🕉️
      </p>

      <button onclick="closeStreakRescueModal()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4);">
        🙏 धन्यवाद प्रभु (साधना जारी रखें)
      </button>

    </div>
  </div>
"""

target_script = '  <script src="mandir_3d_engine.js'
if target_script in html and 'id="vedic-ranks-modal"' not in html:
    html = html.replace(target_script, modals_html + '\n\n' + target_script, 1)
    print("✓ Successfully inserted modals right before scripts in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html saved!")
