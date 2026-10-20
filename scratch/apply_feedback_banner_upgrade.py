import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
ENGINE_FILE = os.path.join(BASE_DIR, "epic_games_engine.js")
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")

print("=== 1. Updating epic_games_engine.js with Feedback Banner ===")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine = f.read()

# Replace showCoinToast calls inside handleSwipeCommit with showSwipeFeedbackBanner
old_commit_feedback = """        showCoinToast(i18n.correct);
      } else {
        playSound('wrong');
        showCoinToast(i18n.wrong);
      }"""

new_commit_feedback = """        showSwipeFeedbackBanner(true, char, chosenSide);
        showCoinToast('+50 🪙');
      } else {
        playSound('wrong');
        showSwipeFeedbackBanner(false, char, chosenSide);
      }"""

if old_commit_feedback in engine:
    engine = engine.replace(old_commit_feedback, new_commit_feedback, 1)
    print("✓ Updated handleSwipeCommit feedback invocation")
else:
    print("⚠ Could not find exact old_commit_feedback in engine")

# Add showSwipeFeedbackBanner function before showCoinToast
feedback_func_code = """  function showSwipeFeedbackBanner(isCorrect, char, chosenSide) {
    var arena = document.getElementById('swipe-arena');
    if (!arena) return;

    var existing = document.getElementById('swipe-feedback-banner');
    if (existing && existing.parentNode) {
      existing.parentNode.removeChild(existing);
    }

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var lang = epicGameState.currentLanguage || 'en';
    
    // Correct side details
    var correctIsLeft = char.correctSwipe === 'LEFT';
    var correctSideObj = correctIsLeft ? cat.leftSide : cat.rightSide;
    var correctSideName = (lang === 'te' && correctSideObj.name_te) ? correctSideObj.name_te : 
                          ((lang === 'en' && correctSideObj.name_en) ? correctSideObj.name_en : 
                          (correctSideObj.name_hi || correctSideObj.name));

    var headingText = "";
    var subText = "";

    if (isCorrect) {
      if (lang === 'te') {
        headingText = "సరైనది!";
        subText = `<span style="color:#C2410C; font-weight:900;">${correctSideName}</span> కోసం పోరాడారు`;
      } else if (lang === 'en') {
        headingText = "Correct!";
        subText = `Fought for <span style="color:#C2410C; font-weight:900;">${correctSideName}</span>`;
      } else {
        headingText = "सही!";
        subText = `<span style="color:#C2410C; font-weight:900;">${correctSideName}</span> के लिए लड़े`;
      }
    } else {
      if (lang === 'te') {
        headingText = "తప్పు!";
        subText = `సరైన పక్షం: <span style="color:#15803D; font-weight:900;">${correctSideName}</span>`;
      } else if (lang === 'en') {
        headingText = "Incorrect!";
        subText = `Correct side: <span style="color:#15803D; font-weight:900;">${correctSideName}</span>`;
      } else {
        headingText = "गलत!";
        subText = `सही पक्ष: <span style="color:#15803D; font-weight:900;">${correctSideName}</span>`;
      }
    }

    var banner = document.createElement('div');
    banner.id = 'swipe-feedback-banner';
    banner.className = 'swipe-feedback-banner ' + (isCorrect ? 'feedback-correct' : 'feedback-wrong');
    banner.innerHTML = `
      <img src="assets/games/banner_feedback_base.png" alt="Feedback Base" class="feedback-banner-base-img">
      <div class="feedback-banner-text-content">
        <div class="feedback-banner-heading ${isCorrect ? 'text-correct' : 'text-wrong'}">${headingText}</div>
        <div class="feedback-banner-subtext">${subText}</div>
      </div>
    `;

    arena.appendChild(banner);

    // Auto remove after 1.35 seconds
    setTimeout(function() {
      if (banner && banner.parentNode) {
        banner.classList.add('feedback-banner-fadeout');
        setTimeout(function() {
          if (banner.parentNode) banner.parentNode.removeChild(banner);
        }, 300);
      }
    }, 1250);
  }

  """

if "function showSwipeFeedbackBanner" not in engine:
    engine = engine.replace("  function showCoinToast(msg) {", feedback_func_code + "function showCoinToast(msg) {", 1)
    print("✓ Added showSwipeFeedbackBanner function to epic_games_engine.js")
else:
    print("⚠ showSwipeFeedbackBanner already exists in engine")

with open(ENGINE_FILE, "w", encoding="utf-8") as f:
    f.write(engine)
print("✓ Saved epic_games_engine.js successfully")

print("\n=== 2. Updating epic_games.css with Banner Styles ===")
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

feedback_banner_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   SWIPE ANSWER FEEDBACK BANNER (Exact Match to User Image 1 & Image 2)
   ══════════════════════════════════════════════════════════════════════════════ */
.swipe-feedback-banner {
  position: absolute;
  top: 64% !important;
  left: 50% !important;
  transform: translate(-50%, -50%);
  width: clamp(290px, 86vw, 360px);
  aspect-ratio: 1024 / 434;
  z-index: 35000;
  pointer-events: none;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: feedbackBannerPop 0.38s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  filter: drop-shadow(0 12px 28px rgba(0, 0, 0, 0.55));
}

.swipe-feedback-banner.feedback-banner-fadeout {
  animation: feedbackBannerExit 0.3s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.feedback-banner-base-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
  pointer-events: none;
}

.feedback-banner-text-content {
  position: relative;
  z-index: 5;
  width: 72%;
  height: 60%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 4px;
  box-sizing: border-box;
}

.feedback-banner-heading {
  font-family: 'Rozha One', 'Yatra One', 'Cinzel', system-ui;
  font-size: clamp(1.65rem, 5.5vw, 2.2rem);
  font-weight: 900;
  line-height: 1.05;
  margin: 0;
  letter-spacing: 0.5px;
}

.feedback-banner-heading.text-correct {
  color: #15803D !important; /* Rich Emerald Green */
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.95), 0 0 14px rgba(34, 197, 94, 0.45);
}

.feedback-banner-heading.text-wrong {
  color: #DC2626 !important; /* Fiery Crimson Red */
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.95), 0 0 14px rgba(239, 68, 68, 0.45);
}

.feedback-banner-subtext {
  font-family: 'Cinzel', 'Rozha One', system-ui;
  font-size: clamp(0.85rem, 3.2vw, 1.05rem);
  font-weight: 800;
  color: #381E0D;
  margin-top: 3px;
  line-height: 1.15;
  letter-spacing: 0.3px;
  text-shadow: 0 1px 1px rgba(255, 255, 255, 0.9);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 92%;
}

@keyframes feedbackBannerPop {
  0% {
    opacity: 0;
    transform: translate(-50%, -40%) scale(0.65);
  }
  70% {
    opacity: 1;
    transform: translate(-50%, -52%) scale(1.05);
  }
  100% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
}

@keyframes feedbackBannerExit {
  0% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
  100% {
    opacity: 0;
    transform: translate(-50%, -38%) scale(0.85);
  }
}
"""

if ".swipe-feedback-banner" not in css:
    css += "\n" + feedback_banner_css
    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(css)
    print("✓ Appended feedback banner CSS to epic_games.css successfully")
else:
    print("⚠ .swipe-feedback-banner already in epic_games.css")

print("\n=== All Feedback Banner Updates Applied Successfully ===")
