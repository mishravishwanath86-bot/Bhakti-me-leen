import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update ringTempleBell with ducking
js = js.replace(
"""window.ringTempleBell = function() {
  if (typeof playBellSound === 'function') playBellSound();""",
"""window.ringTempleBell = function() {
  if (typeof window.duckRadioAudio === 'function') window.duckRadioAudio(3000);
  if (typeof playBellSound === 'function') playBellSound();"""
)

# Update blowTempleConch with ducking
js = js.replace(
"""window.blowTempleConch = function() {
  if (typeof playConchSound === 'function') playConchSound();""",
"""window.blowTempleConch = function() {
  if (typeof window.duckRadioAudio === 'function') window.duckRadioAudio(5000);
  if (typeof playConchSound === 'function') playConchSound();"""
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Connected auto-ducking to temple bell & conch in app.js")
