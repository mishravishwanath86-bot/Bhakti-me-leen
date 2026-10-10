import re, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🛕 INTEGRATING DRACO-COMPRESSED LOADCUSTOMMANDIRMODEL INTO 3D ENGINE")
print("======================================================================")

with open('mandir_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add loadCustomMandirModel implementation
draco_function_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🛕 3D वैदिक मंदिर कस्टम .GLB लोडर इंजन (DRACO + PBR OPTIMIZATION)
// ══════════════════════════════════════════════════════════════════════════════

window.loadCustomMandirModel = function(scene, modelPath, onProgressCallback) {
  scene = scene || window.Mandir3D.scene;
  if (!scene) return;

  // 1. Draco कंप्रेशन सपोर्ट (ताकि भारी 3D मॉडल भी तेज़ी से डिकोड हो)
  let dracoLoader = null;
  if (typeof THREE.DRACOLoader !== 'undefined') {
    dracoLoader = new THREE.DRACOLoader();
    dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.6/');
  }

  const gltfLoader = new THREE.GLTFLoader();
  if (dracoLoader) {
    gltfLoader.setDRACOLoader(dracoLoader);
  }

  // Dispose old model if present
  if (window.Mandir3D.templeModel && scene) {
    scene.remove(window.Mandir3D.templeModel);
    window.Mandir3D.templeModel.traverse((child) => {
      if (child.isMesh) {
        if (child.geometry) child.geometry.dispose();
        if (child.material) {
          if (Array.isArray(child.material)) child.material.forEach(m => m.dispose());
          else child.material.dispose();
        }
      }
    });
    window.Mandir3D.templeModel = null;
  }

  // 2. मॉडल लोडिंग
  gltfLoader.load(
    modelPath,
    (gltf) => {
      const mandirScene = gltf.scene;

      // 3. PBR मटीरियल, शैडो एवं टेक्सचर ऑप्टिमाइज़ेशन
      mandirScene.traverse((child) => {
        if (child.isMesh) {
          child.castShadow = true;
          child.receiveShadow = true;

          // टेक्सचर शार्पनेस और क्लैरिटी बूस्ट
          if (child.material) {
            child.material.roughness = Math.min(child.material.roughness, 0.85);
            child.material.metalness = Math.max(child.material.metalness, 0.15);

            if (child.material.map) {
              child.material.map.anisotropy = 16; // 16x Anisotropic Filtering
              child.material.map.needsUpdate = true;
            }
          }
        }
      });

      // 4. बाउंडिंग बॉक्स स्वतः केंद्रन (Auto-Centering & Grounding)
      const bbox = new THREE.Box3().setFromObject(mandirScene);
      const center = bbox.getCenter(new THREE.Vector3());
      const size = bbox.getSize(new THREE.Vector3());

      // मॉडल के पिवट को ठीक (0, 0, 0) पर लाएं
      mandirScene.position.x += mandirScene.position.x - center.x;
      mandirScene.position.z += mandirScene.position.z - center.z;
      // मंदिर के आधार को ज़मीन (Y = 0) पर टिकाएं
      mandirScene.position.y -= bbox.min.y;

      // दृश्य में मॉडल जोड़ें
      scene.add(mandirScene);
      window.Mandir3D.templeModel = mandirScene;

      // लोडिंग स्क्रीन समाप्त करने का सिग्नल
      if (onProgressCallback) onProgressCallback(100, true);
      
      const loaderEl = document.getElementById('mandir-3d-loader');
      if (loaderEl) loaderEl.style.display = 'none';

      if (typeof showToast === 'function') {
        showToast('✓ 3D वैदिक मंदिर मॉडल पूर्णतः लोड हो चुका है!');
      }
    },
    (xhr) => {
      // 5. रियल-टाइम लोडिंग प्रोग्रेस गणना
      const percentComplete = (xhr.total && xhr.total > 0) ? Math.round((xhr.loaded / xhr.total) * 100) : (xhr.loaded > 0 ? 65 : 15);
      if (onProgressCallback) {
        onProgressCallback(percentComplete, false);
      }
      
      const barEl = document.getElementById('mandir-loader-bar');
      const pctEl = document.getElementById('mandir-loader-percent');
      if (barEl) barEl.style.width = `${percentComplete}%`;
      if (pctEl) pctEl.textContent = `${percentComplete}%`;
    },
    (error) => {
      console.error('3D मंदिर मॉडल लोड करने में त्रुटि:', error);
      const loaderEl = document.getElementById('mandir-3d-loader');
      if (loaderEl) loaderEl.style.display = 'none';
      if (typeof window.buildProceduralTempleFallback === 'function') {
        window.buildProceduralTempleFallback(scene);
      }
    }
  );
};
"""

# Replace window.loadTemple3DModel inside mandir_3d_engine.js to delegate to loadCustomMandirModel
wrapper_code = """
window.loadTemple3DModel = function(scene, templeKey) {
  scene = scene || window.Mandir3D.scene;
  if (!scene) return;

  templeKey = templeKey || window.current3DTempleModel || 'vedic_mandir';
  window.current3DTempleModel = templeKey;
  const config = window.TEMPLE_3D_MODELS[templeKey] || window.TEMPLE_3D_MODELS['vedic_mandir'];

  const loaderEl = document.getElementById('mandir-3d-loader');
  const barEl = document.getElementById('mandir-loader-bar');
  const pctEl = document.getElementById('mandir-loader-percent');

  if (loaderEl) {
    loaderEl.style.display = 'flex';
    const loaderTitle = loaderEl.querySelector('div:nth-child(2)');
    if (loaderTitle) loaderTitle.textContent = `3D ${config.shortName} लोड हो रहा है...`;
    if (barEl) barEl.style.width = '15%';
    if (pctEl) pctEl.textContent = '15%';
  }

  window.loadCustomMandirModel(scene, config.path, (percent, isDone) => {
    if (barEl) barEl.style.width = `${percent}%`;
    if (pctEl) pctEl.textContent = `${percent}%`;
    if (isDone && loaderEl) loaderEl.style.display = 'none';
  });
};
"""

# Inject before loadTemple3DModel or replace it
if 'window.loadCustomMandirModel' not in js:
    js = js.replace('window.loadTemple3DModel = function', draco_function_code + '\n\n' + wrapper_code + '\n\n// Old loadTemple3DModel replaced above\nvar _oldLoadTemple = function')
    print("✓ Injected loadCustomMandirModel with DRACO support into mandir_3d_engine.js")

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ mandir_3d_engine.js updated successfully!")
