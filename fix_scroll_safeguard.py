import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(
    "if (activePill) {\n    activePill.scrollIntoView",
    "if (activePill && typeof activePill.scrollIntoView === 'function') {\n    activePill.scrollIntoView"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Safeguard added for scrollIntoView in app.js")
