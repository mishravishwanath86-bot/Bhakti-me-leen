import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

quiz_functions = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎯 DEDICATED SACRED MCQ QUIZ HUB MODAL CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.openQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) {
    modal.style.display = 'flex';
    if (typeof window.renderCurrentQuiz === 'function') {
      window.renderCurrentQuiz();
    }
    if (navigator.vibrate) navigator.vibrate(30);
  } else {
    console.warn("#quiz-hub-modal not found in DOM");
  }
};

window.closeQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) modal.style.display = 'none';
};
"""

target = "window.switchQuizCategory = function(cat, btnEl) {"
if target in js:
    js = js.replace(target, quiz_functions + "\n" + target, 1)
    print("Added openQuizHubModal and closeQuizHubModal right before switchQuizCategory in app.js")
else:
    js += "\n\n" + quiz_functions
    print("Appended openQuizHubModal to app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Bump version in index.html
import re, time
ts = int(time.time())

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped app.js version in index.html to", ts)
