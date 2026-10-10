import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🏺 FIXING 3D AMRIT KALASH: REMOVING ALL SKETCHFAB UI & WATERMARKS")
print("======================================================================")

# 1. Update index.html with clean Cropped & Masked Viewport
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_kalash_block = """          <!-- 3D Sketchfab Kalash (Coconut & Marigolds Model) -->
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

new_kalash_block = """          <!-- 3D Pure Divine Kalash Viewport (Completely Hides Sketchfab UI, Watermarks & Avatar) -->
          <div id="kalash-3d-canvas-container" style="width:100%; height:260px; margin:0 auto; cursor:pointer; position:relative; overflow:hidden; border-radius:24px; box-shadow:0 0 30px rgba(248,200,59,0.35); background:radial-gradient(circle at 50% 50%, rgba(248,200,59,0.12) 0%, #150328 85%);" onclick="trigger3DKalashInteraction()" title="कलश स्पर्श करें">
            
            <!-- Cropped Frame: Pushes All 4 Corner UI Elements Outside Visible Box -->
            <div style="position:absolute; inset:-48px -42px -54px -42px; overflow:hidden; pointer-events:auto;">
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
                      style="width: 100%; height: 100%; border: none; transform: scale(1.12); transform-origin: center center;">
              </iframe>
            </div>

            <!-- Soft Divine Corner Vignettes to ensure 100% masking of any branding -->
            <div style="position:absolute; top:0; left:0; width:80px; height:80px; background:radial-gradient(circle at 0% 0%, #1A052E 55%, transparent 100%); pointer-events:none; z-index:5;"></div>
            <div style="position:absolute; top:0; right:0; width:80px; height:80px; background:radial-gradient(circle at 100% 0%, #1A052E 55%, transparent 100%); pointer-events:none; z-index:5;"></div>
            <div style="position:absolute; bottom:0; left:0; width:85px; height:80px; background:radial-gradient(circle at 0% 100%, #1A052E 60%, transparent 100%); pointer-events:none; z-index:5;"></div>
            <div style="position:absolute; bottom:0; right:0; width:140px; height:70px; background:radial-gradient(circle at 100% 100%, #1A052E 70%, transparent 100%); pointer-events:none; z-index:5;"></div>

            <!-- Touch / Click Interaction Shield -->
            <div id="kalash-touch-shield" style="position:absolute; inset:0; z-index:10; cursor:pointer;" onclick="trigger3DKalashInteraction()"></div>
          </div>"""

if old_kalash_block in html:
    html = html.replace(old_kalash_block, new_kalash_block)
    print("✓ Updated #kalash-3d-canvas-container with Cropped Masked Viewport in index.html")
else:
    # Use regex
    html = re.sub(r'<!-- 3D (Sketchfab )?Kalash[^\n]*-->\s*<div id="kalash-3d-canvas-container"[\s\S]*?<\/div>\s*<\/div>', new_kalash_block, html)
    print("✓ Replaced #kalash-3d-canvas-container via regex in index.html")

ts = int(time.time())
html = re.sub(r'amrit_kalash_3d_engine\.js\?v=\d+', f'amrit_kalash_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update amrit_kalash_3d_engine.js init3DKalashCanvas
with open('amrit_kalash_3d_engine.js', 'r', encoding='utf-8') as f:
    engine_js = f.read()

old_init = """window.init3DKalashCanvas = function() {
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
};"""

new_init = """window.init3DKalashCanvas = function() {
  const container = document.getElementById('kalash-3d-canvas-container');
  if (!container) return;
  
  // If iframe already exists, preserve it!
  const iframe = container.querySelector('iframe');
  if (iframe) return;

  // Render Clean Cropped Viewport (Hiding all Sketchfab corner UI/watermarks)
  container.innerHTML = `
    <div style="position:absolute; inset:-48px -42px -54px -42px; overflow:hidden; pointer-events:auto;">
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
              style="width: 100%; height: 100%; border: none; transform: scale(1.12); transform-origin: center center;">
      </iframe>
    </div>
    <div style="position:absolute; top:0; left:0; width:80px; height:80px; background:radial-gradient(circle at 0% 0%, #1A052E 55%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div style="position:absolute; top:0; right:0; width:80px; height:80px; background:radial-gradient(circle at 100% 0%, #1A052E 55%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div style="position:absolute; bottom:0; left:0; width:85px; height:80px; background:radial-gradient(circle at 0% 100%, #1A052E 60%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div style="position:absolute; bottom:0; right:0; width:140px; height:70px; background:radial-gradient(circle at 100% 100%, #1A052E 70%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div id="kalash-touch-shield" style="position:absolute; inset:0; z-index:10; cursor:pointer;" onclick="trigger3DKalashInteraction()"></div>
  `;
};"""

if old_init in engine_js:
    engine_js = engine_js.replace(old_init, new_init)
    print("✓ Updated init3DKalashCanvas in amrit_kalash_3d_engine.js")
else:
    engine_js = re.sub(r'window\.init3DKalashCanvas\s*=\s*function\(\)\s*\{[\s\S]*?\n\};', new_init, engine_js)
    print("✓ Replaced init3DKalashCanvas via regex in amrit_kalash_3d_engine.js")

with open('amrit_kalash_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(engine_js)

print("✓ amrit_kalash_3d_engine.js and index.html updated successfully!")
