import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Wall of Fame integration...")

# 1. Update index.html
index_path = 'index.html'
shutil.copy2(index_path, index_path + '.bak_before_wof')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target 1: Home MCQ Banner button
old_home_btn = """          <button onclick="event.stopPropagation(); openQuizHubModal()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.82rem; font-weight:900; padding:8px 18px; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:flex; align-items:center; gap:5px;">
            <span>MCQ खेलें</span> ❯
          </button>"""

new_home_btn = """          <div style="display:flex; align-items:center; gap:8px;">
            <button onclick="event.stopPropagation(); openWallOfFameModal()" style="background:linear-gradient(135deg, #0284C7 0%, #0369A1 100%); color:#FFFFFF; border:none; font-size:0.78rem; font-weight:900; padding:8px 12px; border-radius:14px; cursor:pointer; box-shadow:0 3px 12px rgba(2,132,199,0.35); display:flex; align-items:center; gap:4px;">
              <span>🏆</span> Wall of Fame
            </button>
            <button onclick="event.stopPropagation(); openQuizHubModal()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.82rem; font-weight:900; padding:8px 16px; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:flex; align-items:center; gap:5px;">
              <span>MCQ खेलें</span> ❯
            </button>
          </div>"""

if old_home_btn in content:
    content = content.replace(old_home_btn, new_home_btn, 1)
    print("✓ Updated Home MCQ Banner with Wall of Fame button")
else:
    print("⚠ old_home_btn not found exactly, searching alternative...")
    # Search for button with openQuizHubModal
    needle = 'openQuizHubModal()"'
    idx = content.find(needle)
    if idx != -1:
        print("Found openQuizHubModal() at", idx)

# Target 2: Top Tab Bar in ts-step-topics
old_tab_bar = """        <!-- Tab Bar (Mock Tests Tab - Image 1 Style) -->
        <div style="display:flex; align-items:center; border-bottom:1px solid #27272A; background:#121214; padding:0 16px;">
          <div style="padding:12px 14px 10px; font-size:0.95rem; font-weight:800; color:#FFFFFF; border-bottom:3px solid #FFFFFF; cursor:pointer;">
            Mock Tests
          </div>
          <div onclick="openTopicTestSets('all')" style="padding:12px 14px 10px; font-size:0.95rem; font-weight:600; color:#71717A; cursor:pointer;">
            All India Mega
          </div>
        </div>"""

new_tab_bar = """        <!-- Tab Bar (Mock Tests & Wall of Fame) -->
        <div style="display:flex; align-items:center; border-bottom:1px solid #27272A; background:#121214; padding:0 16px;">
          <div id="ts-tab-btn-mock" onclick="switchQuizViewTab('tests')" style="padding:12px 14px 10px; font-size:0.92rem; font-weight:800; color:#FFFFFF; border-bottom:3px solid #3B82F6; cursor:pointer;">
            Mock Tests
          </div>
          <div id="ts-tab-btn-wall" onclick="switchQuizViewTab('wall_of_fame')" style="padding:12px 14px 10px; font-size:0.92rem; font-weight:700; color:#F59E0B; border-bottom:3px solid transparent; cursor:pointer; display:flex; align-items:center; gap:5px;">
            <span>🏆</span> Wall of Fame
          </div>
          <div onclick="openTopicTestSets('all')" style="padding:12px 14px 10px; font-size:0.88rem; font-weight:600; color:#71717A; cursor:pointer; margin-left:auto;">
            All India Mega
          </div>
        </div>"""

if old_tab_bar in content:
    content = content.replace(old_tab_bar, new_tab_bar, 1)
    print("✓ Updated tab bar in ts-step-topics")
else:
    print("⚠ old_tab_bar not found, checking...")

# Target 3: Add ts-step-wall-of-fame markup after ts-step-topics
wof_markup = """
      <!-- ═════════════════════════════════════════════════════════
           🏆 STEP: WALL OF FAME (TESTBOOK STYLE ALL INDIA TOPPERS)
           ═════════════════════════════════════════════════════════ -->
      <div id="ts-step-wall-of-fame" style="display:none; flex-direction:column; height:100%; max-height:92vh; overflow:hidden; background:#F8FAFC;">
        
        <!-- Header: Back button, Logo + Wall of Fame, Close button -->
        <div style="display:flex; align-items:center; justify-content:space-between; padding:12px 16px; background:#FFFFFF; border-bottom:1px solid #E2E8F0; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
          <div style="display:flex; align-items:center; gap:10px;">
            <button onclick="switchQuizViewTab('tests')" title="पीछे जाएं" style="background:#F1F5F9; border:none; color:#334155; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
              ←
            </button>
            <div style="display:flex; align-items:center; gap:8px;">
              <div style="width:30px; height:30px; border-radius:8px; background:linear-gradient(135deg, #0284C7, #06B6D4); display:flex; align-items:center; justify-content:center; color:#FFF; font-weight:900; font-size:0.95rem; box-shadow:0 2px 8px rgba(2,132,199,0.35);">
                📐
              </div>
              <div>
                <div style="display:flex; align-items:baseline; gap:5px;">
                  <span style="font-size:1.15rem; font-weight:900; color:#0284C7; letter-spacing:-0.3px;">sanatan</span>
                  <span style="font-size:1.15rem; font-weight:900; color:#0F172A; letter-spacing:-0.2px;">Wall of Fame</span>
                </div>
                <div style="font-size:0.68rem; color:#64748B; font-weight:600;">शीर्ष सनातन साधक एवं प्रतियोगी • All India Rankers</div>
              </div>
            </div>
          </div>
          <button onclick="closeQuizHubModal()" title="बंद करें" style="background:#F1F5F9; border:none; color:#64748B; width:30px; height:30px; border-radius:50%; font-size:0.9rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>

        <!-- Logged-in Devotee Interactive Rank Ribbon -->
        <div id="wof-user-strip" style="background:linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%); border-bottom:1.5px solid #FCD34D; padding:10px 14px; display:flex; align-items:center; justify-content:space-between; gap:10px;">
          <!-- Dynamically filled by renderWallOfFame() -->
        </div>

        <!-- Live Leaderboard Status Bar & Controls -->
        <div style="display:flex; align-items:center; justify-content:space-between; padding:8px 14px; background:#FFFFFF; border-bottom:1px solid #E2E8F0;">
          <div style="font-size:0.75rem; font-weight:800; color:#475569; display:flex; align-items:center; gap:5px;">
            <span>🏆</span> <span>ऑल इंडिया रैंक सूची (Live Leaderboard)</span>
          </div>
          <div style="display:flex; align-items:center; gap:6px;">
            <button onclick="boostMcqDemoScore(10)" title="10 प्रश्न सही जोड़कर रैंक बढ़ाएं" style="background:#ECFDF5; border:1px solid #10B981; color:#059669; font-size:0.68rem; font-weight:800; padding:4px 8px; border-radius:10px; cursor:pointer;">
              ⚡ +10 सही उत्तर
            </button>
            <button onclick="openTopicTestSets('all')" style="background:#2563EB; color:#FFF; border:none; font-size:0.72rem; font-weight:800; padding:5px 10px; border-radius:10px; cursor:pointer; display:flex; align-items:center; gap:4px;">
              <span>🚀</span> टेस्ट दें
            </button>
          </div>
        </div>

        <!-- Scrollable Cards Grid Container -->
        <div id="wof-cards-container" style="flex:1; overflow-y:auto; padding:12px 14px 20px; -webkit-overflow-scrolling:touch; background:#F8FAFC;">
          <div id="wof-cards-grid" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:12px;">
            <!-- 12+ Cards injected dynamically -->
          </div>
        </div>

        <!-- Bottom CTA Bar -->
        <div style="padding:10px 16px; background:#FFFFFF; border-top:1px solid #E2E8F0; display:flex; gap:8px;">
          <button onclick="openTopicTestSets('all')" style="flex:1; background:linear-gradient(135deg, #0284C7 0%, #0369A1 100%); color:#FFFFFF; border:none; font-size:0.88rem; font-weight:800; padding:11px 0; border-radius:12px; cursor:pointer; box-shadow:0 4px 12px rgba(2,132,199,0.3); display:flex; align-items:center; justify-content:center; gap:6px;">
            <span>🎯</span> नया टेस्ट देकर रैंक बढ़ाएं
          </button>
        </div>

      </div>
"""

step1_end = """        <!-- Bottom CTA Button (Image 1 Style: "Enroll In Test Series" -> "Start Any Test") -->
        <div style="padding:12px 16px; background:#18181B; border-top:1px solid #27272A;">
          <button onclick="openTopicTestSets('all')" style="width:100%; background:#2563EB; color:#FFFFFF; border:none; font-size:0.95rem; font-weight:800; padding:13px 0; border-radius:12px; cursor:pointer; box-shadow:0 4px 16px rgba(37,99,235,0.4); display:flex; align-items:center; justify-content:center; gap:8px;">
            <span>🚀</span> ऑल इंडिया मॉक टेस्ट शुरू करें
          </button>
        </div>

      </div>"""

if step1_end in content and 'id="ts-step-wall-of-fame"' not in content:
    content = content.replace(step1_end, step1_end + "\n" + wof_markup, 1)
    print("✓ Inserted #ts-step-wall-of-fame into index.html")
else:
    print("⚠ step1_end not matched or already inserted")

# Target 4: Add Wall of Fame CTA in Step 5 Scorecard
old_scorecard_cta = """          <!-- Action Buttons: Re-attempt & Change Topic -->
          <div style="display:flex; gap:10px; margin-bottom:18px;">
            <button onclick="startActualExam()" style="flex:1; background:#27272A; border:1px solid #3F3F46; color:#F4F4F5; font-size:0.82rem; font-weight:800; padding:10px 0; border-radius:10px; cursor:pointer;">
              🔄 पुनः टेस्ट दें
            </button>
            <button onclick="goToQuizStep(1)" style="flex:1; background:#3B82F6; border:none; color:#FFFFFF; font-size:0.82rem; font-weight:800; padding:10px 0; border-radius:10px; cursor:pointer;">
              📚 अन्य टॉपिक चुनें
            </button>
          </div>"""

new_scorecard_cta = """          <!-- Wall of Fame View Rank Button -->
          <button onclick="switchQuizViewTab('wall_of_fame')" style="width:100%; background:linear-gradient(135deg, #F59E0B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.88rem; font-weight:900; padding:12px 0; border-radius:12px; cursor:pointer; margin-bottom:12px; box-shadow:0 4px 15px rgba(245,158,11,0.35); display:flex; align-items:center; justify-content:center; gap:8px;">
            <span>🏆</span> Wall of Fame पर अपनी रैंक देखें ➔
          </button>

          <!-- Action Buttons: Re-attempt & Change Topic -->
          <div style="display:flex; gap:10px; margin-bottom:18px;">
            <button onclick="startActualExam()" style="flex:1; background:#27272A; border:1px solid #3F3F46; color:#F4F4F5; font-size:0.82rem; font-weight:800; padding:10px 0; border-radius:10px; cursor:pointer;">
              🔄 पुनः टेस्ट दें
            </button>
            <button onclick="goToQuizStep(1)" style="flex:1; background:#3B82F6; border:none; color:#FFFFFF; font-size:0.82rem; font-weight:800; padding:10px 0; border-radius:10px; cursor:pointer;">
              📚 अन्य टॉपिक चुनें
            </button>
          </div>"""

if old_scorecard_cta in content:
    content = content.replace(old_scorecard_cta, new_scorecard_cta, 1)
    print("✓ Added Wall of Fame CTA to scorecard in index.html")
else:
    print("⚠ old_scorecard_cta not matched")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ index.html successfully updated!")
