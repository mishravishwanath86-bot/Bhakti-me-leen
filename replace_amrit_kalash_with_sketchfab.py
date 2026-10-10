import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sketchfab_kalash_html = """          <!-- 3D Sketchfab Kalash (Coconut & Marigolds Model) -->
          <div id="kalash-3d-canvas-container" style="width:100%; height:250px; margin:0 auto; cursor:pointer; position:relative; overflow:hidden; border-radius:20px; box-shadow:0 0 25px rgba(248,200,59,0.35); background:radial-gradient(circle at 50% 50%, rgba(248,200,59,0.1) 0%, transparent 80%);" onclick="trigger3DKalashInteraction()" title="कलश स्पर्श करें">
            <iframe title="Kalash with coconut and marigolds" 
                    id="kalash-sketchfab-iframe"
                    frameborder="0" 
                    allowfullscreen 
                    mozallowfullscreen="true" 
                    webkitallowfullscreen="true" 
                    allow="autoplay; fullscreen; xr-spatial-tracking" 
                    xr-spatial-tracking 
                    execution-while-out-of-viewport 
                    execution-while-not-rendered 
                    web-share 
                    src="https://sketchfab.com/models/2c56e05aad4b4372a8f2e240398810db/embed?autostart=1&preload=1&transparent=1&ui_theme=dark&ui_controls=0&ui_infos=0&ui_watermark=0&ui_stop=0&ui_hint=0" 
                    style="width: 100%; height: 100%; border-radius: 20px; border: none;">
            </iframe>
          </div>"""

# Replace existing kalash-3d-canvas-container
pattern = r'<!-- 3D Three\.js Kalash Container -->[\s\S]*?<div id="kalash-3d-canvas-container"[\s\S]*?<\/div>'
if re.search(pattern, html):
    html = re.sub(pattern, sketchfab_kalash_html, html)
    print("✓ Replaced with Sketchfab 3D Kalash model in index.html")
else:
    # Alternative match
    pattern_alt = r'<div id="kalash-3d-canvas-container"[\s\S]*?<\/div>'
    html = re.sub(pattern_alt, sketchfab_kalash_html, html, count=1)
    print("✓ Replaced container with Sketchfab 3D Kalash model in index.html")

ts = int(time.time())
html = re.sub(r'amrit_kalash_3d_engine\.js\?v=\d+', f'amrit_kalash_3d_engine.js?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update amrit_kalash_3d_engine.js
with open('amrit_kalash_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure init3DKalashCanvas doesn't overwrite the iframe
js = re.sub(
    r'window\.init3DKalashCanvas = function\(\) {[\s\S]*?animate3DKalash\(\);\s*};',
    """window.init3DKalashCanvas = function() {
  const container = document.getElementById('kalash-3d-canvas-container');
  if (!container) return;
  
  // If Sketchfab iframe already exists, preserve it!
  const iframe = container.querySelector('iframe');
  if (iframe) return;

  // Fallback if iframe was not present
  container.innerHTML = `
    <iframe title="Kalash with coconut and marigolds" 
            id="kalash-sketchfab-iframe"
            frameborder="0" 
            allowfullscreen 
            mozallowfullscreen="true" 
            webkitallowfullscreen="true" 
            allow="autoplay; fullscreen; xr-spatial-tracking" 
            xr-spatial-tracking 
            execution-while-out-of-viewport 
            execution-while-not-rendered 
            web-share 
            src="https://sketchfab.com/models/2c56e05aad4b4372a8f2e240398810db/embed?autostart=1&preload=1&transparent=1&ui_theme=dark&ui_controls=0&ui_infos=0&ui_watermark=0&ui_stop=0&ui_hint=0" 
            style="width: 100%; height: 100%; border-radius: 20px; border: none;">
    </iframe>
  `;
};""",
    js
)

# Update tilt3DKalashAndEmitNectar to trigger flower shower & haptics smoothly with the 3D model
tilt_pattern = r'window\.tilt3DKalashAndEmitNectar = function\(callback\) {[\s\S]*?};'
new_tilt_func = """window.tilt3DKalashAndEmitNectar = function(callback) {
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
  if (navigator.vibrate) navigator.vibrate([40, 60, 40]);

  const iframe = document.getElementById('kalash-sketchfab-iframe');
  if (iframe) {
    iframe.style.transition = 'transform 0.3s ease';
    iframe.style.transform = 'scale(1.05) rotate(-3deg)';
    setTimeout(() => {
      iframe.style.transform = 'scale(1) rotate(0deg)';
      if (callback) callback();
    }, 350);
  } else {
    if (callback) callback();
  }
};"""

js = re.sub(tilt_pattern, new_tilt_func, js)

with open('amrit_kalash_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ amrit_kalash_3d_engine.js updated to support Sketchfab 3D Kalash model!")
