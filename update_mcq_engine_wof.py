import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

print("Starting mcq_test_series_engine.js update for Wall of Fame...")

src_path = 'mcq_test_series_engine.js'
shutil.copy2(src_path, src_path + '.bak_before_wof')

with open(src_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update injectTestSeriesStyles to include Wall of Fame CSS & responsiveness
old_styles = """        #ts-step-topics, #ts-step-tests, #ts-step-instructions, #ts-step-exam, #ts-step-result {
          height: 100vh !important;
          max-height: 100vh !important;
        }"""

new_styles = """        #ts-step-topics, #ts-step-tests, #ts-step-instructions, #ts-step-exam, #ts-step-result, #ts-step-wall-of-fame {
          height: 100vh !important;
          max-height: 100vh !important;
        }
        .wof-card {
          transition: transform 0.18s ease, box-shadow 0.18s ease;
        }
        .wof-card:active {
          transform: scale(0.98);
        }
        .wof-card-user {
          animation: userCardGlow 2.5s infinite ease-in-out;
        }
        @keyframes userCardGlow {
          0%, 100% { box-shadow: 0 4px 18px rgba(245, 158, 11, 0.28); }
          50% { box-shadow: 0 8px 28px rgba(245, 158, 11, 0.55); border-color: #F59E0B; }
        }
        #wof-cards-container::-webkit-scrollbar {
          width: 4px;
        }
        #wof-cards-container::-webkit-scrollbar-thumb {
          background: #CBD5E1;
          border-radius: 4px;
        }"""

if old_styles in code:
    code = code.replace(old_styles, new_styles, 1)
    print("✓ Added Wall of Fame styles to injectTestSeriesStyles()")
else:
    print("⚠ old_styles not found")

# 2. Update submitExam to record correct answers
old_submit_part = """    // Score calculated with +2.0 and -0.5 negative marking
    const rawScore = (correct * 2.0) - (wrong * 0.5);"""

new_submit_part = """    // Record user's correct answers to cumulative Wall of Fame score
    if (correct > 0 && typeof window.recordMcqCorrectAnswers === 'function') {
      window.recordMcqCorrectAnswers(correct);
    }

    // Score calculated with +2.0 and -0.5 negative marking
    const rawScore = (correct * 2.0) - (wrong * 0.5);"""

if old_submit_part in code:
    code = code.replace(old_submit_part, new_submit_part, 1)
    print("✓ Hooked submitExam to recordMcqCorrectAnswers()")
else:
    print("⚠ old_submit_part not found")

# 3. Update goToQuizStep to handle wall of fame step
old_goto = """    const step1 = document.getElementById('ts-step-topics');       // Step 1
    const step2 = document.getElementById('ts-step-tests');        // Step 2
    const step3 = document.getElementById('ts-step-instructions'); // Step 3
    const step4 = document.getElementById('ts-step-exam');         // Step 4
    const step5 = document.getElementById('ts-step-result');       // Step 5

    if (step1) step1.style.display = (stepNum === 1) ? 'flex' : 'none';
    if (step2) step2.style.display = (stepNum === 2) ? 'flex' : 'none';
    if (step3) step3.style.display = (stepNum === 3) ? 'flex' : 'none';
    if (step4) step4.style.display = (stepNum === 4) ? 'flex' : 'none';
    if (step5) step5.style.display = (stepNum === 5) ? 'flex' : 'none';"""

new_goto = """    const step1 = document.getElementById('ts-step-topics');       // Step 1
    const step2 = document.getElementById('ts-step-tests');        // Step 2
    const step3 = document.getElementById('ts-step-instructions'); // Step 3
    const step4 = document.getElementById('ts-step-exam');         // Step 4
    const step5 = document.getElementById('ts-step-result');       // Step 5
    const stepWall = document.getElementById('ts-step-wall-of-fame'); // Step Wall of Fame

    if (step1) step1.style.display = (stepNum === 1) ? 'flex' : 'none';
    if (step2) step2.style.display = (stepNum === 2) ? 'flex' : 'none';
    if (step3) step3.style.display = (stepNum === 3) ? 'flex' : 'none';
    if (step4) step4.style.display = (stepNum === 4) ? 'flex' : 'none';
    if (step5) step5.style.display = (stepNum === 5) ? 'flex' : 'none';
    if (stepWall) stepWall.style.display = (stepNum === 'wall' || stepNum === 6) ? 'flex' : 'none';"""

if old_goto in code:
    code = code.replace(old_goto, new_goto, 1)
    print("✓ Updated goToQuizStep with Wall of Fame support")
else:
    print("⚠ old_goto not found")

# 4. Add the complete Wall of Fame Engine Logic right before the closing of IIFE:
wof_engine_code = """
  // ═════════════════════════════════════════════════════════════════════════════
  // 🏆 SANATAN WALL OF FAME (TESTBOOK STYLE LIVE ALL INDIA LEADERBOARD)
  // ═════════════════════════════════════════════════════════════════════════════

  window.DEFAULT_WOF_TOPPERS = [
    { id: 'samridhi', name: 'Samridhi Talwar', avatar: 'assets/wall_of_fame/rank_1_samridhi.jpg', correctAnswers: 98, exam: 'रामायण महाकाव्य 2024' },
    { id: 'ashish', name: 'Ashish Tiwari', avatar: 'assets/wall_of_fame/rank_2_ashish.jpg', correctAnswers: 94, exam: 'महाभारत एवं गीता 2024' },
    { id: 'debesh', name: 'Debesh Bairagi', avatar: 'assets/wall_of_fame/rank_3_debesh.jpg', correctAnswers: 90, exam: 'चारों वेद एवं उपनिषद' },
    { id: 'ishant', name: 'Ishant Shukla', avatar: 'assets/wall_of_fame/rank_4_ishant.jpg', correctAnswers: 86, exam: 'श्रीमद्भगवद्गीता ज्ञान' },
    { id: 'rohit', name: 'Rohit Chadhar', avatar: 'assets/wall_of_fame/rank_5_rohit.jpg', correctAnswers: 82, exam: 'वैदिक मंत्र एवं स्तोत्र' },
    { id: 'sagardip', name: 'Sagardip Ghosh', avatar: 'assets/wall_of_fame/rank_6_sagardip.jpg', correctAnswers: 78, exam: 'देवी-देवता दर्शन टेस्ट' },
    { id: 'mohan', name: 'Mohan Kumar', avatar: 'assets/wall_of_fame/rank_7_mohan.jpg', correctAnswers: 74, exam: 'भक्ति साहित्य एवं संत' },
    { id: 'sanket', name: 'Sanket Paul', avatar: 'assets/wall_of_fame/rank_8_sanket.jpg', correctAnswers: 70, exam: 'आरती व चालीसा पाठ' },
    { id: 'shaurya', name: 'Shaurya Kumar', avatar: 'assets/wall_of_fame/rank_9_shaurya.jpg', correctAnswers: 66, exam: 'सनातन इतिहास टेस्ट' },
    { id: 'prachi', name: 'Prachi Purohit', avatar: 'assets/wall_of_fame/rank_10_prachi.jpg', correctAnswers: 62, exam: 'उपनिषद दर्शन 2024' },
    { id: 'anam', name: 'Anam Zafar', avatar: 'assets/wall_of_fame/rank_11_anam.jpg', correctAnswers: 58, exam: 'सनातन ज्ञान प्रवाह' },
    { id: 'diksha', name: 'Diksha Dawar', avatar: 'assets/wall_of_fame/rank_12_diksha.jpg', correctAnswers: 54, exam: 'दिव्य तीर्थ महाकुंभ' }
  ];

  window.getWallOfFameUserRecord = function() {
    let raw = localStorage.getItem('bhakti_user');
    let u = {};
    if (raw) {
      try { u = JSON.parse(raw); } catch(e) {}
    }
    const savedName = localStorage.getItem('bhakti_user_name') || u.name || (u.isLoggedIn ? 'सनातन साधक' : 'आप (साधक)');
    const savedAvatar = localStorage.getItem('bhakti_user_avatar') || u.avatar || u.photoURL || 'assets/gallery/bal_ganesha_little.jpg';
    const isLoggedIn = !!(u && (u.isLoggedIn || u.name || u.email));
    const correctCount = parseInt(localStorage.getItem('sanatan_mcq_user_correct_count') || '0', 10);

    return {
      id: 'current_user',
      name: savedName,
      avatar: savedAvatar,
      correctAnswers: correctCount,
      exam: isLoggedIn ? 'सत्यापित सनातन साधक' : 'अतिथि साधक',
      isUser: true,
      isLoggedIn: isLoggedIn
    };
  };

  window.getSortedWallOfFameList = function() {
    const userRec = window.getWallOfFameUserRecord();
    const list = window.DEFAULT_WOF_TOPPERS.map(t => ({ ...t, isUser: false }));

    list.push(userRec);

    // Sort strictly descending by correct answers: whoever answers most correct answers is at top!
    list.sort((a, b) => {
      if (b.correctAnswers !== a.correctAnswers) {
        return b.correctAnswers - a.correctAnswers;
      }
      return a.isUser ? -1 : 1;
    });

    list.forEach((item, idx) => {
      item.rank = idx + 1;
      item.rankBadge = `AIR ${item.rank} | ${item.correctAnswers} प्रश्न सही`;
    });

    return { list, userRec };
  };

  window.recordMcqCorrectAnswers = function(newCorrect) {
    if (!newCorrect || newCorrect <= 0) return;
    const prev = parseInt(localStorage.getItem('sanatan_mcq_user_correct_count') || '0', 10);
    const updated = prev + newCorrect;
    localStorage.setItem('sanatan_mcq_user_correct_count', updated.toString());
    console.log(`✓ [WallOfFame] +${newCorrect} correct answers recorded. Total: ${updated}`);
    if (document.getElementById('ts-step-wall-of-fame')?.style.display === 'flex') {
      window.renderWallOfFame();
    }
  };

  window.boostMcqDemoScore = function(points = 10) {
    const prev = parseInt(localStorage.getItem('sanatan_mcq_user_correct_count') || '0', 10);
    const updated = prev + points;
    localStorage.setItem('sanatan_mcq_user_correct_count', updated.toString());
    if (typeof showEngineToast === 'function') {
      showEngineToast(`🎉 +${points} सही उत्तर जुड़े! कुल: ${updated}`);
    }
    window.renderWallOfFame();
    if (updated > 98 && typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('victory');
    }
  };

  window.resetMcqUserScore = function() {
    localStorage.setItem('sanatan_mcq_user_correct_count', '0');
    if (typeof showEngineToast === 'function') {
      showEngineToast('🔄 आपका स्कोर रीसेट हुआ!');
    }
    window.renderWallOfFame();
  };

  window.renderWallOfFame = function() {
    const { list, userRec } = window.getSortedWallOfFameList();
    const userRank = list.find(x => x.isUser)?.rank || list.length;
    const isRank1 = (userRank === 1);

    // 1. Render User Strip Ribbon
    const stripEl = document.getElementById('wof-user-strip');
    if (stripEl) {
      const topScore = list[0].correctAnswers;
      const neededForRank1 = Math.max(0, topScore - userRec.correctAnswers + 1);

      let statusMsg = '';
      if (isRank1) {
        statusMsg = `<span style="color:#059669; font-weight:900;">👑 अद्भुत! आप ऑल इंडिया रैंक #1 पर हैं! 🚩</span>`;
      } else {
        statusMsg = `<span style="color:#D97706; font-weight:700;">रैंक #1 के लिए और <strong>${neededForRank1}</strong> प्रश्न सही करें</span>`;
      }

      stripEl.innerHTML = `
        <div style="display:flex; align-items:center; gap:10px; flex:1; min-width:0;">
          <div style="position:relative; width:44px; height:44px; flex-shrink:0;">
            <img src="${userRec.avatar}" alt="${userRec.name}" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" style="width:44px; height:44px; border-radius:50%; object-fit:cover; border:2px solid #F59E0B; box-shadow:0 2px 8px rgba(0,0,0,0.15);" onclick="if(typeof openAvatarPickerModal==='function')openAvatarPickerModal();"/>
            <div style="position:absolute; bottom:-2px; right:-2px; background:#F59E0B; color:#1A0B2E; font-size:9px; font-weight:900; width:16px; height:16px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:1.5px solid #FFF;">
              ${userRank}
            </div>
          </div>
          <div style="min-width:0;">
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="font-size:0.88rem; font-weight:900; color:#1E293B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${userRec.name}</span>
              ${userRec.isLoggedIn ? '<span style="background:#10B981; color:#FFF; font-size:0.58rem; font-weight:900; padding:1px 5px; border-radius:6px;">✓ Logged In</span>' : ''}
            </div>
            <div style="font-size:0.72rem; color:#059669; font-weight:800;">
              AIR ${userRank} • ${userRec.correctAnswers} प्रश्न सही
            </div>
            <div style="font-size:0.65rem; margin-top:1px;">
              ${statusMsg}
            </div>
          </div>
        </div>
        <div style="display:flex; flex-direction:column; gap:4px; align-items:flex-end; flex-shrink:0;">
          ${!userRec.isLoggedIn ? `
            <button onclick="if(typeof openGoogleAccountPickerModal==='function'){openGoogleAccountPickerModal();}else{document.getElementById('auth-modal').style.display='flex';}" style="background:#FFFFFF; border:1px solid #CBD5E1; color:#0F172A; font-size:0.7rem; font-weight:800; padding:5px 9px; border-radius:10px; cursor:pointer; display:flex; align-items:center; gap:4px; box-shadow:0 1px 3px rgba(0,0,0,0.08);">
              <span>🔑</span> लॉगिन करें
            </button>
          ` : `
            <button onclick="if(typeof openAvatarPickerModal==='function')openAvatarPickerModal();" style="background:#FFFFFF; border:1px solid #CBD5E1; color:#3B82F6; font-size:0.68rem; font-weight:800; padding:4px 8px; border-radius:8px; cursor:pointer;">
              अवतार बदलें
            </button>
          `}
        </div>
      `;
    }

    // 2. Render 12+ Cards Grid in exact Testbook style
    const gridEl = document.getElementById('wof-cards-grid');
    if (!gridEl) return;

    gridEl.innerHTML = list.map(item => {
      const isUser = item.isUser;
      const cardBorder = isUser ? '2px solid #F59E0B' : '1px solid #E2E8F0';
      const cardBg = isUser ? 'linear-gradient(180deg, #FEFCE8 0%, #FFFFFF 100%)' : '#FFFFFF';
      const cardShadow = isUser ? '0 8px 24px rgba(245,158,11,0.28)' : '0 4px 16px rgba(0,0,0,0.04)';

      return `
        <div class="wof-card ${isUser ? 'wof-card-user' : ''}" onclick="${isUser ? (item.isLoggedIn ? "if(typeof openAvatarPickerModal==='function')openAvatarPickerModal();" : "if(typeof openGoogleAccountPickerModal==='function'){openGoogleAccountPickerModal();}else{document.getElementById('auth-modal').style.display='flex';}") : `showEngineToast('🏆 ${item.name} (${item.rankBadge})')`}" style="background:${cardBg}; border:${cardBorder}; border-radius:18px; padding:14px 8px 12px; text-align:center; box-shadow:${cardShadow}; position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:165px; cursor:pointer;">
          
          ${isUser ? `<div style="position:absolute; top:6px; left:50%; transform:translateX(-50%); background:#F59E0B; color:#1A0B2E; font-size:0.62rem; font-weight:900; padding:2px 8px; border-radius:8px; white-space:nowrap; box-shadow:0 2px 6px rgba(245,158,11,0.4);">⭐ आप (YOU)</div>` : ''}

          <!-- Circular Avatar with Decorative Festive Accents -->
          <div style="position:relative; width:88px; height:88px; display:flex; align-items:center; justify-content:center; margin-top:${isUser ? '10px' : '4px'};">
            
            <!-- SVG Festive Accents: Golden Whiskers & Multi-colored Sparkle Dots -->
            <svg viewBox="0 0 100 100" style="position:absolute; inset:0; width:100%; height:100%; pointer-events:none;">
              <!-- Left Golden Whiskers -->
              <line x1="8" y1="42" x2="19" y2="42" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="4" y1="50" x2="16" y2="50" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="8" y1="58" x2="19" y2="58" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>

              <!-- Right Golden Whiskers -->
              <line x1="81" y1="42" x2="92" y2="42" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="84" y1="50" x2="96" y2="50" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="81" y1="58" x2="92" y2="58" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>

              <!-- Top Whisker -->
              <line x1="50" y1="4" x2="50" y2="14" stroke="#FBBF24" stroke-width="2" stroke-linecap="round"/>

              <!-- Colorful Festive Confetti Dots -->
              <circle cx="20" cy="24" r="2.2" fill="#38BDF8"/>
              <circle cx="80" cy="24" r="2.2" fill="#EC4899"/>
              <circle cx="16" cy="74" r="2.2" fill="#8B5CF6"/>
              <circle cx="82" cy="76" r="2.2" fill="#10B981"/>
              <circle cx="30" cy="14" r="1.8" fill="#F59E0B"/>
              <circle cx="70" cy="14" r="1.8" fill="#F59E0B"/>
            </svg>

            <!-- Devotee Avatar Image -->
            <img src="${item.avatar}" alt="${item.name}" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" style="width:68px; height:68px; border-radius:50%; object-fit:cover; border:2.5px solid #F59E0B; background:#F1F5F9; box-shadow:0 4px 10px rgba(0,0,0,0.1); display:block;"/>

            <!-- Pinned Gold Star Badge -->
            <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; border-radius:50%; background:#FBBF24; border:1.8px solid #FFFFFF; color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:900; box-shadow:0 2px 6px rgba(0,0,0,0.25);">
              ★
            </div>
          </div>

          <!-- Devotee Name -->
          <div style="font-size:0.86rem; font-weight:800; color:#1E293B; margin-top:6px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%; width:100%; text-align:center;">
            ${item.name}
          </div>

          <!-- Rank & Score Badge -->
          <div style="font-size:0.72rem; font-weight:800; color:#059669; margin-top:3px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%;">
            ${item.rankBadge}
          </div>

          <!-- Subtitle / Exam / Accuracy -->
          <div style="font-size:0.64rem; font-weight:600; color:#64748B; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%;">
            ${item.exam}
          </div>

        </div>
      `;
    }).join('');
  };

  window.switchQuizViewTab = function(tabName) {
    const tabMock = document.getElementById('ts-tab-btn-mock');
    const tabWall = document.getElementById('ts-tab-btn-wall');
    const stepTopics = document.getElementById('ts-step-topics');
    const stepWall = document.getElementById('ts-step-wall-of-fame');

    if (tabName === 'wall_of_fame' || tabName === 'wall') {
      if (tabMock) {
        tabMock.style.color = '#71717A';
        tabMock.style.fontWeight = '600';
        tabMock.style.borderBottom = '3px solid transparent';
      }
      if (tabWall) {
        tabWall.style.color = '#F59E0B';
        tabWall.style.fontWeight = '900';
        tabWall.style.borderBottom = '3px solid #F59E0B';
      }
      if (stepTopics) stepTopics.style.display = 'none';
      if (stepWall) {
        stepWall.style.display = 'flex';
        window.renderWallOfFame();
      }
    } else {
      if (tabMock) {
        tabMock.style.color = '#FFFFFF';
        tabMock.style.fontWeight = '800';
        tabMock.style.borderBottom = '3px solid #3B82F6';
      }
      if (tabWall) {
        tabWall.style.color = '#71717A';
        tabWall.style.fontWeight = '600';
        tabWall.style.borderBottom = '3px solid transparent';
      }
      if (stepWall) stepWall.style.display = 'none';
      if (stepTopics) {
        stepTopics.style.display = 'flex';
        if (typeof renderTopicsListStep === 'function') renderTopicsListStep();
      }
    }
  };

  window.openWallOfFameModal = async function() {
    await window.openQuizHubModal();
    window.switchQuizViewTab('wall_of_fame');
  };

  // Re-render Wall of Fame if profile or user avatar changes
  window.addEventListener('storage', (e) => {
    if (e.key === 'bhakti_user' || e.key === 'bhakti_user_avatar' || e.key === 'bhakti_user_name') {
      if (document.getElementById('ts-step-wall-of-fame')?.style.display === 'flex') {
        window.renderWallOfFame();
      }
    }
  });
"""

# Insert wof_engine_code right before the last `})();`
closing_iife = "\n})();"
if closing_iife in code:
    code = code.replace(closing_iife, wof_engine_code + closing_iife, 1)
    print("✓ Appended Wall of Fame Engine Logic to mcq_test_series_engine.js")
else:
    print("⚠ closing_iife not found")

with open(src_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("✓ Saved updated mcq_test_series_engine.js")

# Copy to public/
public_path = os.path.join('public', 'mcq_test_series_engine.js')
if os.path.exists('public'):
    shutil.copy2(src_path, public_path)
    print("✓ Synced to public/mcq_test_series_engine.js")

print("All updates completed successfully!")
