import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(
    'video.play().catch(err => {',
    "if (video && typeof video.play === 'function') video.play().catch(err => {"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Updated video.play guard in app.js")
