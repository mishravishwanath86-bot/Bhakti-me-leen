// ══════════════════════════════════════════════════════════════════════════════
// 🏛️ 3D REAL-TIME VEDIC MANDIR & PARIKRAMA SANKALP WEBGL ENGINE
// Powered by Three.js, OrbitControls, GLTFLoader, Realistic PBR Lighting
// ══════════════════════════════════════════════════════════════════════════════

window.targetParikramaLaps = 11;
window.currentParikramaLaps = 0;
window.isAutoOrbiting = false;
window.is3DMandirNightMode = false;
window.is3DMandirMuted = false;
window.current3DDeity = 'mahakal';
window.current3DTempleModel = 'vedic_mandir';

// 🛕 3D Temples Configuration (.GLB / .GLTF)
window.TEMPLE_3D_MODELS = {
  'vedic_mandir': {
    id: 'vedic_mandir',
    name: 'भव्य वैदिक सनातन मंदिर (Custom 3D Vedic Mandir)',
    shortName: 'वैदिक मंदिर (Vedic .GLB)',
    path: 'assets/models/vedic_mandir.glb',
    type: 'glb',
    targetSize: 18.0,
    cameraRadius: 12.0,
    cameraHeight: 4.5
  },
  'temple_heritage': {
    id: 'temple_heritage',
    name: 'प्राचीन भारतीय धरोहर मंदिर (Grand Heritage Temple)',
    shortName: 'धरोहर मंदिर (Heritage .GLB)',
    path: 'assets/models/indian_temples/Tempal.glb',
    type: 'glb',
    targetSize: 18.0,
    cameraRadius: 12.0,
    cameraHeight: 4.5
  },
  'temple_classical': {
    id: 'temple_classical',
    name: 'भव्य सनातन पाषाण मंदिर (Classical Stone Temple)',
    shortName: 'पाषाण मंदिर (Classical .GLTF)',
    path: 'assets/models/hindu_temple/scene.gltf',
    type: 'gltf',
    targetSize: 18.0,
    cameraRadius: 12.0,
    cameraHeight: 4.5
  }
};

// 🕉️ Deity Configuration
window.MANDIR_DEITIES = {
  'mahakal': {
    name: 'श्री महाकालेश्वर ज्योतिर्लिंग',
    title: 'श्री महाकालेश्वर परिक्रमा',
    image: 'assets/gallery/divya_shiva.jpg',
    color: 0x8B5CF6,
    mantra: 'ॐ हौं जूं सः भूर्भुवः स्वः'
  },
  'kashi': {
    name: 'श्री काशी विश्वनाथ मंदिर',
    title: 'श्री काशी विश्वनाथ परिक्रमा',
    image: 'assets/gallery/divya_shiva.jpg',
    color: 0x3B82F6,
    mantra: 'ॐ नमः शिवाय'
  },
  'ayodhya': {
    name: 'श्री राम जन्मभूमि अयोध्या',
    title: 'श्री राम जन्मभूमि परिक्रमा',
    image: 'assets/gallery/bal_rama.jpg',
    color: 0xF59E0B,
    mantra: 'श्री राम जय राम जय जय राम'
  },
  'siddhivinayak': {
    name: 'श्री सिद्धिविनायक मंदिर',
    title: 'श्री सिद्धिविनायक परिक्रमा',
    image: 'assets/gallery/bal_ganesha_little.jpg',
    color: 0xEF4444,
    mantra: 'ॐ गं गणपतये नमः'
  }
};

window.Mandir3D = {
  scene: null,
  camera: null,
  renderer: null,
  controls: null,
  templeModel: null,
  bellMesh: null,
  bellAngle: 0,
  bellVelocity: 0,
  sparkleSystem: null,
  petals: [],
  diyaLights: [],
  ambientLight: null,
  sunLight: null,
  altarSpot: null,
  accumulatedAngle: 0,
  prevOrbitAzimuth: 0
};

// 🎯 Parikrama Target Selection

// 🎯 Parikrama Target Selection (3, 7, 11, 21 Laps)
window.selectParikramaTarget = function(laps, btnEl) {
  window.targetParikramaLaps = parseInt(laps, 10) || 11;
  
  // Highlight active chip
  document.querySelectorAll('.parikrama-chip').forEach(c => {
    c.classList.remove('active');
    c.style.background = 'rgba(255,255,255,0.08)';
    c.style.borderColor = 'rgba(255,255,255,0.15)';
    c.style.color = '#CBD5E1';
    c.style.boxShadow = 'none';
  });
  
  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.borderColor = '#FEF3C7';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.boxShadow = '0 0 12px rgba(248,200,59,0.5)';
  }
  
  // Update CTA text on Home Card
  const ctaText = document.getElementById('parikrama-cta-text');
  if (ctaText) {
    ctaText.textContent = `🚩 ${laps} परिक्रमा शुरू करें (3D मंदिर में प्रवेश)`;
  }
  
  const badge = document.getElementById('target-laps-badge');
  if (badge) badge.textContent = `${laps} परिक्रमा संकल्प`;

  if (navigator.vibrate) navigator.vibrate(25);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
};

// 🚩 Start 3D Mandir Parikrama Flow
window.start3DMandirParikramaFlow = function(deityKey) {
  deityKey = deityKey || window.current3DDeity || 'mahakal';
  window.open3DMandirModal(deityKey);
};

// 🏛️ Home Screen 3D Temple Target Switcher
window.setHome3DTempleTarget = function(modelKey) {
  window.current3DTempleModel = modelKey;
  const btnClassical = document.getElementById('home-temple-select-classical');
  const btnHeritage = document.getElementById('home-temple-select-heritage');
  
  if (btnClassical && btnHeritage) {
    if (modelKey === 'temple_classical') {
      btnClassical.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnClassical.style.color = '#1A0B2E';
      btnClassical.style.boxShadow = '0 0 10px rgba(248,200,59,0.4)';
      btnHeritage.style.background = 'transparent';
      btnHeritage.style.color = '#CBD5E1';
      btnHeritage.style.boxShadow = 'none';
    } else {
      btnHeritage.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnHeritage.style.color = '#1A0B2E';
      btnHeritage.style.boxShadow = '0 0 10px rgba(248,200,59,0.4)';
      btnClassical.style.background = 'transparent';
      btnClassical.style.color = '#CBD5E1';
      btnClassical.style.boxShadow = 'none';
    }
  }
  if (navigator.vibrate) navigator.vibrate(25);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
};


window.open3DMandirModal = function(deityKey) {
  if (deityKey && window.MANDIR_DEITIES[deityKey]) {
    window.current3DDeity = deityKey;
  }
  const deity = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
  
  const modal = document.getElementById('mandir-3d-modal');
  if (!modal) return;
  modal.style.display = 'flex';

  const titleEl = document.getElementById('mandir-modal-title');
  if (titleEl) titleEl.textContent = `॥ ${deity.title} ॥`;

  const mantraEl = document.getElementById('mandir-mantra-text');
  if (mantraEl) mantraEl.textContent = deity.mantra;

  window.currentParikramaLaps = 0;
  window.updateParikramaLapUI();

  // Initialize Three.js Scene
  setTimeout(() => {
    window.init3DMandirScene();
  }, 50);

  // Play entry bell sound
  if (typeof ringTempleBell === 'function') ringTempleBell();
  if (typeof showToast === 'function') {
    showToast(`🛕 ${deity.name} के 3D दिव्य गर्भगृह में आपका स्वागत है`);
  }
};

window.close3DMandirModal = function() {
  const modal = document.getElementById('mandir-3d-modal');
  if (modal) modal.style.display = 'none';
  if (window.mandir3DAnimFrame) {
    cancelAnimationFrame(window.mandir3DAnimFrame);
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// 3D SCENE & ENGINE INITIALIZATION WITH FULL 3D ORBIT CONTROLS
// ══════════════════════════════════════════════════════════════════════════════

window.init3DMandirScene = function() {
  const container = document.getElementById('mandir-3d-canvas-container');
  if (!container) return;

  container.innerHTML = '';

  const width = container.clientWidth || window.innerWidth;
  const height = container.clientHeight || window.innerHeight;

  // 1. Scene Setup
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(window.is3DMandirNightMode ? 0x070112 : 0x1A0B2E);
  scene.fog = new THREE.FogExp2(window.is3DMandirNightMode ? 0x070112 : 0x1A0B2E, 0.018);
  window.Mandir3D.scene = scene;

  // 2. Camera Setup (Positioned for grand full-angle entrance view)
  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.set(0, 5.0, 18.0);
  camera.lookAt(0, 2.5, 0);
  window.Mandir3D.camera = camera;

  // 3. High-Performance WebGL Renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.4;
  renderer.outputEncoding = THREE.sRGBEncoding;
  container.appendChild(renderer.domElement);
  window.Mandir3D.renderer = renderer;

  // 4. OrbitControls with Full 3D Freedom & Smooth Damping
  if (typeof THREE.OrbitControls !== 'undefined') {
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.screenSpacePanning = true; // Full up/down/left/right panning
    controls.minDistance = 2.0;         // Prevent camera clipping into sanctum
    controls.maxDistance = 32.0;        // Max zoom distance
    controls.maxPolarAngle = Math.PI / 2 + 0.05; // Prevent dipping underground
    controls.minPolarAngle = 0.05;      // Top bird-eye / Shikhar view
    controls.target.set(0, 2.5, 0);
    controls.update();
    window.Mandir3D.controls = controls;
    window.Mandir3D.prevOrbitAzimuth = controls.getAzimuthalAngle();
  }

  // 5. HDRI Room Environment
  if (THREE.PMREMGenerator && THREE.RoomEnvironment) {
    const pmrem = new THREE.PMREMGenerator(renderer);
    scene.environment = pmrem.fromScene(new THREE.RoomEnvironment(), 0.04).texture;
  }

  // 6. Divine Temple Lighting Setup
  const ambientLight = new THREE.AmbientLight(0xfff3db, 1.3); // Warm sacred temple tone
  scene.add(ambientLight);
  window.Mandir3D.ambientLight = ambientLight;

  const divineSunLight = new THREE.DirectionalLight(0xffdf9e, 2.5);
  divineSunLight.position.set(12, 24, 14);
  divineSunLight.castShadow = true;
  divineSunLight.shadow.mapSize.width = 2048;
  divineSunLight.shadow.mapSize.height = 2048;
  divineSunLight.shadow.camera.near = 0.5;
  divineSunLight.shadow.camera.far = 60;
  divineSunLight.shadow.bias = -0.0005;
  scene.add(divineSunLight);
  window.Mandir3D.sunLight = divineSunLight;

  // Inner Garbhagriha Altar Spotlight
  const altarSpot = new THREE.SpotLight(0xFFEAA7, 4.0, 35, Math.PI / 3.0, 0.3, 1.0);
  altarSpot.position.set(0, 14, 4);
  altarSpot.castShadow = true;
  scene.add(altarSpot);
  window.Mandir3D.altarSpot = altarSpot;

  // Floating Diya Flames Point Lights
  window.Mandir3D.diyaLights = [];
  [[-3.2, 1.2, 4.0], [3.2, 1.2, 4.0], [0, 1.0, -1.0]].forEach(pos => {
    const dLight = new THREE.PointLight(0xFF8800, 2.5, 10);
    dLight.position.set(pos[0], pos[1], pos[2]);
    scene.add(dLight);
    window.Mandir3D.diyaLights.push(dLight);
  });

  // 7. Load Custom 3D Mandir Model (.GLB / .GLTF)
  window.loadTemple3DModel(scene, window.current3DTempleModel);

  // 8. Particle Systems (Golden Aura & Flower Shower)
  window.initTempleParticleSystems(scene);

  // 9. Window Resize Listener
  window.addEventListener('resize', window.on3DMandirResize);

  // 10. Start Animation & Render Loop
  window.animate3DMandir();
};

window.on3DMandirResize = function() {
  const container = document.getElementById('mandir-3d-canvas-container');
  if (!container || !window.Mandir3D.renderer || !window.Mandir3D.camera) return;
  const w = container.clientWidth || window.innerWidth;
  const h = container.clientHeight || window.innerHeight;
  window.Mandir3D.camera.aspect = w / h;
  window.Mandir3D.camera.updateProjectionMatrix();
  window.Mandir3D.renderer.setSize(w, h);
};

// ══════════════════════════════════════════════════════════════════════════════
// GLTF/GLB LOADER WITH AUTO-CENTERING, PBR OPTIMIZATION & PROGRESS BAR
// ══════════════════════════════════════════════════════════════════════════════


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


// Old loadTemple3DModel replaced above
var _oldLoadTemple = function(scene, templeKey) {
  scene = scene || window.Mandir3D.scene;
  if (!scene) return;

  templeKey = templeKey || window.current3DTempleModel || 'vedic_mandir';
  window.current3DTempleModel = templeKey;
  const config = window.TEMPLE_3D_MODELS[templeKey] || window.TEMPLE_3D_MODELS['vedic_mandir'];

  const loaderEl = document.getElementById('mandir-3d-loader');
  const barEl = document.getElementById('mandir-loader-bar');
  const pctEl = document.getElementById('mandir-loader-percent');

  // Dispose old model
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

  // Show loading indicator
  if (loaderEl) {
    loaderEl.style.display = 'flex';
    const loaderTitle = loaderEl.querySelector('div:nth-child(2)');
    if (loaderTitle) loaderTitle.textContent = `3D ${config.shortName} लोड हो रहा है...`;
    if (barEl) barEl.style.width = '20%';
    if (pctEl) pctEl.textContent = '20%';
  }

  if (typeof THREE.GLTFLoader !== 'undefined') {
    const loader = new THREE.GLTFLoader();

    loader.load(
      config.path,
      (gltf) => {
        const templeModel = gltf.scene;

        // Shadow & Material Optimization
        templeModel.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
            if (child.material && child.material.map) {
              child.material.map.anisotropy = 16;
            }
          }
        });

        // Auto-center the model regardless of bounding size
        const box = new THREE.Box3().setFromObject(templeModel);
        const center = box.getCenter(new THREE.Vector3());
        const size = box.getSize(new THREE.Vector3());

        // Center pivot point to (0,0,0) and ground base on y = 0
        templeModel.position.x -= center.x;
        templeModel.position.y -= box.min.y;
        templeModel.position.z -= center.z;

        // Normalize scale
        const maxDim = Math.max(size.x, size.y, size.z);
        const targetSize = config.targetSize || 18.0;
        const scale = targetSize / (maxDim || 1.0);
        templeModel.scale.set(scale, scale, scale);

        scene.add(templeModel);
        window.Mandir3D.templeModel = templeModel;

        if (loaderEl) loaderEl.style.display = 'none';
        if (typeof showToast === 'function') {
          showToast(`✓ 3D ${config.shortName} 360° दर्शन हेतु तैयार है!`);
        }
      },
      (xhr) => {
        if (xhr.total > 0) {
          const percent = Math.min(99, Math.round((xhr.loaded / xhr.total) * 100));
          if (barEl) barEl.style.width = `${percent}%`;
          if (pctEl) pctEl.textContent = `${percent}%`;
        }
      },
      (error) => {
        console.warn('GLTF loader error, generating procedural temple fallback:', error);
        if (loaderEl) loaderEl.style.display = 'none';
        window.buildProceduralTempleFallback(scene);
      }
    );
  } else {
    if (loaderEl) loaderEl.style.display = 'none';
    window.buildProceduralTempleFallback(scene);
  }
};

// Procedural Fallback Temple if GLTF fails to load
window.buildProceduralTempleFallback = function(scene) {
  const templeGroup = new THREE.Group();
  
  // Plinth
  const plinthMat = new THREE.MeshStandardMaterial({ color: 0x8C6D4F, roughness: 0.6, metalness: 0.2 });
  const plinth = new THREE.Mesh(new THREE.BoxGeometry(14, 1.2, 14), plinthMat);
  plinth.position.y = 0.6;
  plinth.receiveShadow = true;
  templeGroup.add(plinth);

  // Mandap
  const wallMat = new THREE.MeshStandardMaterial({ color: 0xD4AF37, roughness: 0.4, metalness: 0.4 });
  const mandap = new THREE.Mesh(new THREE.BoxGeometry(8, 5, 8), wallMat);
  mandap.position.y = 3.7;
  mandap.castShadow = true;
  templeGroup.add(mandap);

  // Shikhar (Cone Tower)
  const shikhar = new THREE.Mesh(new THREE.ConeGeometry(4.5, 9, 8), wallMat);
  shikhar.position.y = 10.7;
  shikhar.castShadow = true;
  templeGroup.add(shikhar);

  // Golden Kalash
  const kalashMat = new THREE.MeshStandardMaterial({ color: 0xFFD700, roughness: 0.2, metalness: 0.8 });
  const kalash = new THREE.Mesh(new THREE.SphereGeometry(0.8, 16, 16), kalashMat);
  kalash.position.y = 15.5;
  templeGroup.add(kalash);

  scene.add(templeGroup);
  window.Mandir3D.templeModel = templeGroup;
};

// ══════════════════════════════════════════════════════════════════════════════
// PARTICLE SYSTEMS & ANIMATION LOOP
// ══════════════════════════════════════════════════════════════════════════════

window.initTempleParticleSystems = function(scene) {
  // Sparkle / Aura Particles
  const count = 120;
  const geom = new THREE.BufferGeometry();
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 18;
    positions[i + 1] = Math.random() * 12 + 0.5;
    positions[i + 2] = (Math.random() - 0.5) * 18;
  }
  geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  const mat = new THREE.PointsMaterial({
    color: 0xFDE68A,
    size: 0.22,
    transparent: true,
    opacity: 0.75,
    blending: THREE.AdditiveBlending
  });
  const sparkles = new THREE.Points(geom, mat);
  scene.add(sparkles);
  window.Mandir3D.sparkleSystem = sparkles;
};

// Main Animation Loop
window.animate3DMandir = function() {
  window.mandir3DAnimFrame = requestAnimationFrame(window.animate3DMandir);

  const controls = window.Mandir3D.controls;
  const camera = window.Mandir3D.camera;
  const renderer = window.Mandir3D.renderer;
  const scene = window.Mandir3D.scene;

  // Update OrbitControls for smooth inertia damping
  if (controls) {
    if (window.isAutoOrbiting) {
      controls.autoRotate = true;
      controls.autoRotateSpeed = 2.0;
    } else {
      controls.autoRotate = false;
    }
    controls.update();

    // Track parikrama lap completion based on azimuthal rotation
    const currentAzimuth = controls.getAzimuthalAngle();
    let delta = currentAzimuth - window.Mandir3D.prevOrbitAzimuth;
    if (delta < -Math.PI) delta += Math.PI * 2;
    if (delta > Math.PI) delta -= Math.PI * 2;
    window.Mandir3D.accumulatedAngle += Math.abs(delta);
    window.Mandir3D.prevOrbitAzimuth = currentAzimuth;

    if (window.Mandir3D.accumulatedAngle >= Math.PI * 2) {
      window.Mandir3D.accumulatedAngle -= Math.PI * 2;
      window.currentParikramaLaps++;
      window.updateParikramaLapUI();
      if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('victory');
    }
  }

  // Animate Diya Lights flicker
  const time = performance.now() * 0.003;
  if (window.Mandir3D.diyaLights) {
    window.Mandir3D.diyaLights.forEach((light, i) => {
      light.intensity = 2.2 + Math.sin(time + i * 2.0) * 0.45;
    });
  }

  // Animate Falling Petals
  if (window.Mandir3D.petals && window.Mandir3D.petals.length > 0) {
    window.Mandir3D.petals.forEach((petal, idx) => {
      petal.position.y -= petal.userData.speedY;
      petal.rotation.x += 0.02;
      petal.rotation.y += 0.03;
      if (petal.position.y < 0.2) {
        scene.remove(petal);
        window.Mandir3D.petals.splice(idx, 1);
      }
    });
  }

  if (renderer && scene && camera) {
    renderer.render(scene, camera);
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// INTERACTIVE CONTROLS & CAMERA PRESETS
// ══════════════════════════════════════════════════════════════════════════════

window.toggleAutoOrbit = function() {
  window.isAutoOrbiting = !window.isAutoOrbiting;
  const btn = document.getElementById('mandir-auto-orbit-btn');
  if (btn) {
    if (window.isAutoOrbiting) {
      btn.textContent = '⏸️ परिक्रमा रोकें';
      btn.style.background = 'linear-gradient(135deg, #10B981, #059669)';
      btn.style.color = '#FFFFFF';
    } else {
      btn.textContent = '🪔 स्वतः परिक्रमा';
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.color = '#1A0B2E';
    }
  }
  if (typeof showToast === 'function') {
    showToast(window.isAutoOrbiting ? '🪔 स्वतः 360° परिक्रमा प्रारंभ' : '⏸️ परिक्रमा रोकी गई');
  }
};

// Camera Angle Presets (Garbhagriha, Shikhar, Bird's-Eye, Front Entrance)
window.setCameraViewPreset = function(preset) {
  const camera = window.Mandir3D.camera;
  const controls = window.Mandir3D.controls;
  if (!camera || !controls) return;

  window.isAutoOrbiting = false;
  const orbitBtn = document.getElementById('mandir-auto-orbit-btn');
  if (orbitBtn) {
    orbitBtn.textContent = '🪔 स्वतः परिक्रमा';
    orbitBtn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    orbitBtn.style.color = '#1A0B2E';
  }

  if (typeof gsap !== 'undefined') {
    let targetPos = { x: 0, y: 5.0, z: 18.0 };
    let targetLook = { x: 0, y: 2.5, z: 0 };

    if (preset === 'garbhagriha') {
      targetPos = { x: 0, y: 2.2, z: 6.5 }; // Close darshan
      targetLook = { x: 0, y: 2.0, z: 0 };
    } else if (preset === 'shikhar') {
      targetPos = { x: 0, y: 16.0, z: 12.0 }; // Shikhar & Kalash
      targetLook = { x: 0, y: 8.0, z: 0 };
    } else if (preset === 'vihangam') {
      targetPos = { x: 18.0, y: 22.0, z: 18.0 }; // Bird's Eye View
      targetLook = { x: 0, y: 2.0, z: 0 };
    } else {
      targetPos = { x: 0, y: 5.0, z: 18.0 }; // Front Entrance
      targetLook = { x: 0, y: 2.5, z: 0 };
    }

    gsap.to(camera.position, {
      x: targetPos.x,
      y: targetPos.y,
      z: targetPos.z,
      duration: 1.2,
      ease: "power2.inOut"
    });
    gsap.to(controls.target, {
      x: targetLook.x,
      y: targetLook.y,
      z: targetLook.z,
      duration: 1.2,
      ease: "power2.inOut"
    });
  } else {
    if (preset === 'garbhagriha') {
      camera.position.set(0, 2.2, 6.5);
      controls.target.set(0, 2.0, 0);
    } else if (preset === 'shikhar') {
      camera.position.set(0, 16.0, 12.0);
      controls.target.set(0, 8.0, 0);
    } else if (preset === 'vihangam') {
      camera.position.set(18.0, 22.0, 18.0);
      controls.target.set(0, 2.0, 0);
    } else {
      camera.position.set(0, 5.0, 18.0);
      controls.target.set(0, 2.5, 0);
    }
  }

  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
};

// Flower Shower 3D Effect
window.triggerFlowerShower3D = function() {
  const scene = window.Mandir3D.scene;
  if (!scene) return;

  const colors = [0xFF69B4, 0xFFA500, 0xFFD700, 0xFF4500, 0xFFFFFF];
  for (let i = 0; i < 40; i++) {
    const col = colors[Math.floor(Math.random() * colors.length)];
    const geom = new THREE.CircleGeometry(0.18, 5);
    const mat = new THREE.MeshStandardMaterial({ color: col, side: THREE.DoubleSide });
    const petal = new THREE.Mesh(geom, mat);
    petal.position.set(
      (Math.random() - 0.5) * 10,
      12 + Math.random() * 5,
      (Math.random() - 0.5) * 10
    );
    petal.userData = { speedY: 0.06 + Math.random() * 0.05 };
    scene.add(petal);
    window.Mandir3D.petals.push(petal);
  }

  if (typeof showToast === 'function') showToast('🌸 गर्भगृह में पुष्प वर्षा समर्पित की गई!');
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
};

// UI Update
window.updateParikramaLapUI = function() {
  const currentEl = document.getElementById('current-laps-counter');
  const targetEl = document.getElementById('target-laps-counter');
  const barEl = document.getElementById('parikrama-progress-bar');

  if (currentEl) currentEl.textContent = window.currentParikramaLaps;
  if (targetEl) targetEl.textContent = window.targetParikramaLaps;
  if (barEl) {
    const pct = Math.min(100, Math.round((window.currentParikramaLaps / window.targetParikramaLaps) * 100));
    barEl.style.width = `${pct}%`;
  }
};


// Aliases for HTML modal buttons
window.toggle3DAutoOrbit = window.toggleAutoOrbit;
window.reset3DCameraView = function() { window.setCameraViewPreset('front'); };
window.trigger3DDiyaGlow = function() {
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
  if (typeof showToast === 'function') showToast('🪔 दीप प्रज्ज्वलित किया गया!');
  if (navigator.vibrate) navigator.vibrate(30);
};
window.trigger3DPushpaVarsha = window.triggerFlowerShower3D;
window.trigger3DGhantiNaad = function() {
  if (typeof ringTempleBell === 'function') ringTempleBell();
  if (typeof showToast === 'function') showToast('🔔 मंदिर महाघंट नाद गुंजायमान!');
  if (navigator.vibrate) navigator.vibrate([0, 60, 30, 80]);
};
window.close3DParikramaCompletedModal = function() {
  const m = document.getElementById('parikrama-completed-modal');
  if (m) m.style.display = 'none';
};
window.share3DParikramaWhatsApp = function() {
  const text = `🚩 मैंने "Bhakti Me Leen" ऐप में भव्य 3D मंदिर की ${window.targetParikramaLaps} परिक्रमा और दिव्य दर्शन पूर्ण किए! आप भी दर्शन करें ➔ https://bhaktimeleen.app`;
  window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
};
