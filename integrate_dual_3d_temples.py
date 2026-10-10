import re, time, sys, os

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🏛️ INTEGRATING DUAL 3D TEMPLES (CLASSICAL STONE & INDIAN HERITAGE)")
print("======================================================================")

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Temple Selector Pill in #parikrama-sankalp-home-card if not present
if 'id="home-temple-select-classical"' not in html:
    target_card_text = """        <!-- Parikrama Target Selector Chips -->"""
    replacement_card_text = """        <!-- 🏛️ 3D Temple Selection Tabs on Home Card -->
        <div style="display:flex; align-items:center; justify-content:center; gap:8px; margin-bottom:12px; background:rgba(0,0,0,0.3); border:1px solid rgba(248,200,59,0.3); border-radius:14px; padding:4px;">
          <button id="home-temple-select-classical" onclick="setHome3DTempleTarget('temple_classical')" style="flex:1; padding:7px; border-radius:10px; font-size:0.75rem; font-weight:800; border:none; cursor:pointer; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; display:flex; align-items:center; justify-content:center; gap:4px; box-shadow:0 0 10px rgba(248,200,59,0.4);">
            <span>🏛️</span> पाषाण मंदिर (Temple 1)
          </button>
          <button id="home-temple-select-heritage" onclick="setHome3DTempleTarget('temple_heritage')" style="flex:1; padding:7px; border-radius:10px; font-size:0.75rem; font-weight:800; border:none; cursor:pointer; background:transparent; color:#CBD5E1; display:flex; align-items:center; justify-content:center; gap:4px;">
            <span>🛕</span> धरोहर मंदिर (Temple 2)
          </button>
        </div>

        <!-- Parikrama Target Selector Chips -->"""
    if target_card_text in html:
        html = html.replace(target_card_text, replacement_card_text, 1)
        print("✓ Added Temple Model Selection Tabs on Home Screen Card in index.html")

# Add 3D Temple Architecture Switcher in #mandir-3d-modal
if 'id="temple-model-btn-classical"' not in html:
    target_topbar = """      <!-- Right Actions: Instructions, Day/Night & Sound -->"""
    replacement_topbar = """      <!-- 🏛️ 3D Temple Switcher Tabs (2 3D Temples) -->
      <div style="display:flex; align-items:center; gap:6px; background:rgba(20,5,38,0.9); border:1.2px solid rgba(248,200,59,0.45); border-radius:18px; padding:3px; box-shadow:0 4px 15px rgba(0,0,0,0.6);">
        <button id="temple-model-btn-classical" onclick="switch3DTempleModel('temple_classical')" class="temple-model-tab active" style="padding:4px 10px; border-radius:14px; font-size:0.74rem; font-weight:900; border:none; cursor:pointer; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; box-shadow:0 0 10px rgba(248,200,59,0.5); display:flex; align-items:center; gap:4px; transition:all 0.2s ease;">
          <span>🏛️</span> मंदिर 1
        </button>
        <button id="temple-model-btn-heritage" onclick="switch3DTempleModel('temple_heritage')" class="temple-model-tab" style="padding:4px 10px; border-radius:14px; font-size:0.74rem; font-weight:900; border:none; cursor:pointer; background:transparent; color:#CBD5E1; display:flex; align-items:center; gap:4px; transition:all 0.2s ease;">
          <span>🛕</span> मंदिर 2
        </button>
      </div>

      <!-- Right Actions: Instructions, Day/Night & Sound -->"""
    if target_topbar in html:
        html = html.replace(target_topbar, replacement_topbar, 1)
        print("✓ Added Temple Model Switcher Tabs in #mandir-3d-modal Top Bar in index.html")

ts = int(time.time())
html = re.sub(r'mandir_3d_engine\.js\?v=\d+', f'mandir_3d_engine.js?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html saved successfully!")


# 2. Update mandir_3d_engine.js
with open('mandir_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Define Temple Models Configuration at top
temple_models_config = """// ══════════════════════════════════════════════════════════════════════════════
// 🏛️ 3D REAL-TIME HINDU TEMPLE & PARIKRAMA SANKALP WEBGL ENGINE
// Powered by Three.js GLTFLoader, Dual 3D Temples (Classical & Indian Heritage)
// ══════════════════════════════════════════════════════════════════════════════

window.targetParikramaLaps = 11;
window.currentParikramaLaps = 0;
window.isAutoOrbiting = false;
window.is3DMandirNightMode = true;
window.is3DMandirMuted = false;
window.current3DDeity = 'mahakal';
window.isCameraWalkingIn = false;

// 🛕 Dual 3D Temples Configuration
window.TEMPLE_3D_MODELS = {
  'temple_classical': {
    id: 'temple_classical',
    name: 'भव्य सनातन पाषाण मंदिर (Classical Stone Temple)',
    shortName: 'पाषाण मंदिर (Temple 1)',
    path: 'assets/models/hindu_temple/scene.gltf',
    type: 'gltf',
    targetSize: 18.0,
    cameraRadius: 12.0,
    cameraHeight: 3.2
  },
  'temple_heritage': {
    id: 'temple_heritage',
    name: 'प्राचीन भारतीय धरोहर मंदिर (Grand Indian Heritage Temple)',
    shortName: 'धरोहर मंदिर (Temple 2)',
    path: 'assets/models/indian_temples/Tempal.glb',
    type: 'glb',
    targetSize: 18.0,
    cameraRadius: 12.0,
    cameraHeight: 3.2
  }
};

window.current3DTempleModel = 'temple_classical';
"""

# Replace top config in mandir_3d_engine.js
top_pattern = r'\/\/ ══════════════════════════════════════════════════════════════════════════════\n\/\/ 🏛️ 3D REAL-TIME HINDU TEMPLE[\s\S]*?window\.isCameraWalkingIn = false;'
if re.search(top_pattern, js):
    js = re.sub(top_pattern, lambda m: temple_models_config, js, count=1)
    print("✓ Updated top configuration with Dual 3D Temples in mandir_3d_engine.js")

# Replace loadHinduTempleGLTFModel with multi-model loader
new_loader_block = """// ══════════════════════════════════════════════════════════════════════════════
// GLTF LOADER WITH DUAL 3D TEMPLE SUPPORT, SMART AUTO-CENTERING & PBR
// ══════════════════════════════════════════════════════════════════════════════

window.loadTemple3DModel = function(scene, templeKey) {
  scene = scene || window.Mandir3D.scene;
  if (!scene) return;

  templeKey = templeKey || window.current3DTempleModel || 'temple_classical';
  window.current3DTempleModel = templeKey;
  const config = window.TEMPLE_3D_MODELS[templeKey] || window.TEMPLE_3D_MODELS['temple_classical'];

  const loaderEl = document.getElementById('mandir-3d-loader');
  const barEl = document.getElementById('mandir-loader-bar');
  const pctEl = document.getElementById('mandir-loader-percent');

  // Update Switcher Tabs UI if present
  const btnClassical = document.getElementById('temple-model-btn-classical');
  const btnHeritage = document.getElementById('temple-model-btn-heritage');
  if (btnClassical && btnHeritage) {
    if (templeKey === 'temple_classical') {
      btnClassical.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnClassical.style.color = '#1A0B2E';
      btnClassical.style.boxShadow = '0 0 10px rgba(248,200,59,0.5)';
      btnHeritage.style.background = 'transparent';
      btnHeritage.style.color = '#CBD5E1';
      btnHeritage.style.boxShadow = 'none';
    } else {
      btnHeritage.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnHeritage.style.color = '#1A0B2E';
      btnHeritage.style.boxShadow = '0 0 10px rgba(248,200,59,0.5)';
      btnClassical.style.background = 'transparent';
      btnClassical.style.color = '#CBD5E1';
      btnClassical.style.boxShadow = 'none';
    }
  }

  // Remove existing temple model cleanly and dispose geometries/materials
  if (window.Mandir3D.templeModel && scene) {
    scene.remove(window.Mandir3D.templeModel);
    window.Mandir3D.templeModel.traverse((child) => {
      if (child.isMesh) {
        if (child.geometry) child.geometry.dispose();
        if (child.material) {
          if (Array.isArray(child.material)) {
            child.material.forEach(m => m.dispose());
          } else {
            child.material.dispose();
          }
        }
      }
    });
    window.Mandir3D.templeModel = null;
  }

  if (typeof THREE.GLTFLoader !== 'undefined') {
    const loader = new THREE.GLTFLoader();

    if (loaderEl) {
      loaderEl.style.display = 'flex';
      const loaderTitle = loaderEl.querySelector('div:nth-child(2)');
      if (loaderTitle) loaderTitle.textContent = `3D ${config.shortName} लोड हो रहा है...`;
      if (barEl) barEl.style.width = '15%';
      if (pctEl) pctEl.textContent = '15%';
    }

    loader.load(
      config.path,
      (gltf) => {
        const model = gltf.scene;

        // Auto-center and normalize bounding box
        const box = new THREE.Box3().setFromObject(model);
        const center = box.getCenter(new THREE.Vector3());
        const size = box.getSize(new THREE.Vector3());

        // Position model centered on floor
        model.position.x -= center.x;
        model.position.y -= box.min.y; // Sit flat on floor
        model.position.z -= center.z;

        // Scale appropriately
        const maxDim = Math.max(size.x, size.y, size.z);
        const targetSize = config.targetSize || 18.0;
        const scale = targetSize / (maxDim || 1.0);
        model.scale.set(scale, scale, scale);

        // Enhance PBR materials and shadows
        model.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
            if (child.material) {
              child.material.envMapIntensity = 1.8;
              if (child.material.map) {
                child.material.map.encoding = THREE.sRGBEncoding;
              }
            }
          }
        });

        scene.add(model);
        window.Mandir3D.templeModel = model;

        if (loaderEl) loaderEl.style.display = 'none';

        if (typeof showToast === 'function') {
          showToast(`🛕 ${config.name} सक्रिय!`);
        }
      },
      (xhr) => {
        if (xhr.lengthComputable) {
          const percent = Math.round((xhr.loaded / xhr.total) * 100);
          if (barEl) barEl.style.width = percent + '%';
          if (pctEl) pctEl.textContent = percent + '%';
        }
      },
      (error) => {
        console.warn(`GLTF Model load error for ${config.path}:`, error);
        if (loaderEl) loaderEl.style.display = 'none';
        if (typeof window.buildGrandSanctumEnvironment === 'function') {
          window.buildGrandSanctumEnvironment(scene);
        }
      }
    );
  }
};

window.loadHinduTempleGLTFModel = window.loadTemple3DModel;

window.switch3DTempleModel = function(templeKey) {
  if (window.current3DTempleModel === templeKey && window.Mandir3D.templeModel) {
    return;
  }
  window.current3DTempleModel = templeKey;
  if (window.Mandir3D.scene) {
    window.loadTemple3DModel(window.Mandir3D.scene, templeKey);
  }
};

window.setHome3DTempleTarget = function(templeKey) {
  window.current3DTempleModel = templeKey;
  const btnC = document.getElementById('home-temple-select-classical');
  const btnH = document.getElementById('home-temple-select-heritage');
  if (btnC && btnH) {
    if (templeKey === 'temple_classical') {
      btnC.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnC.style.color = '#1A0B2E';
      btnC.style.boxShadow = '0 0 10px rgba(248,200,59,0.4)';
      btnH.style.background = 'transparent';
      btnH.style.color = '#CBD5E1';
      btnH.style.boxShadow = 'none';
    } else {
      btnH.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnH.style.color = '#1A0B2E';
      btnH.style.boxShadow = '0 0 10px rgba(248,200,59,0.4)';
      btnC.style.background = 'transparent';
      btnC.style.color = '#CBD5E1';
      btnC.style.boxShadow = 'none';
    }
  }
  const config = window.TEMPLE_3D_MODELS[templeKey];
  if (typeof showToast === 'function' && config) {
    showToast(`🛕 चयनित 3D मंदिर: ${config.shortName}`);
  }
};"""

loader_pattern = r'window\.loadHinduTempleGLTFModel\s*=\s*function\(scene\)\s*\{[\s\S]*?\n\};'
if re.search(loader_pattern, js):
    js = re.sub(loader_pattern, lambda m: new_loader_block, js, count=1)
    print("✓ Successfully replaced model loader with Dual 3D Temple Loader in mandir_3d_engine.js")

# In init3DMandirScene, ensure it passes window.current3DTempleModel
init_pattern = r'window\.loadHinduTempleGLTFModel\(scene\);'
if re.search(init_pattern, js):
    js = re.sub(init_pattern, "window.loadTemple3DModel(scene, window.current3DTempleModel);", js, count=1)
    print("✓ Updated init3DMandirScene to load active temple model")

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ mandir_3d_engine.js saved successfully!")
