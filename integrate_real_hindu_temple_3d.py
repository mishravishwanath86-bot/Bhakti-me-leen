import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# Rewrite mandir_3d_engine.js with real Hindu Temple 3D Model Loader and Smart Auto-centering & PBR
real_hindu_temple_engine_js = """// ══════════════════════════════════════════════════════════════════════════════
// 🏛️ 3D REAL-TIME HINDU TEMPLE & PARIKRAMA SANKALP WEBGL ENGINE
// Powered by Three.js GLTFLoader, Realistic 3D Model & Cinematic Camera Walk-in
// ══════════════════════════════════════════════════════════════════════════════

window.targetParikramaLaps = 11;
window.currentParikramaLaps = 0;
window.isAutoOrbiting = false;
window.is3DMandirNightMode = true;
window.is3DMandirMuted = false;
window.current3DDeity = 'mahakal';
window.isCameraWalkingIn = false;

// Deity Configuration
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
  radius: 12.0,
  angle: 0,
  height: 3.2,
  accumulatedAngle: 0,
  prevMouseX: 0
};

// Selection handler on Home Screen
window.selectParikramaTarget = function(laps, btnEl) {
  window.targetParikramaLaps = laps;
  
  document.querySelectorAll('.parikrama-chip').forEach(c => {
    c.classList.remove('active');
    c.style.background = 'rgba(255,255,255,0.08)';
    c.style.color = '#CBD5E1';
    c.style.border = '1px solid rgba(255,255,255,0.15)';
    c.style.boxShadow = 'none';
  });

  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
    btnEl.style.boxShadow = '0 0 12px rgba(248,200,59,0.4)';
  }

  const cta = document.getElementById('parikrama-cta-text');
  if (cta) {
    cta.textContent = `🚩 ${laps} परिक्रमा शुरू करें (3D मंदिर में प्रवेश)`;
  }
};

// Start Flow with Door Open Animation & Smooth Camera Walk-in
window.start3DMandirParikramaFlow = function() {
  const modal = document.getElementById('mandir-3d-modal');
  const doorOverlay = document.getElementById('temple-door-transition-overlay');
  const leftDoor = document.getElementById('door-left');
  const rightDoor = document.getElementById('door-right');

  window.currentParikramaLaps = 0;
  window.updateParikramaProgressBar();

  if (modal) modal.style.display = 'flex';

  window.init3DMandirScene();

  if (doorOverlay && leftDoor && rightDoor) {
    doorOverlay.style.display = 'block';
    leftDoor.style.transform = 'scaleX(1)';
    rightDoor.style.transform = 'scaleX(1)';

    if (typeof playSoundEffect === 'function' && !window.is3DMandirMuted) {
      playSoundEffect('victory');
    }

    setTimeout(() => {
      leftDoor.style.transform = 'scaleX(0)';
      rightDoor.style.transform = 'scaleX(0)';
      window.executeCameraWalkInTransition();
    }, 100);

    setTimeout(() => {
      doorOverlay.style.display = 'none';
    }, 1300);
  } else {
    window.executeCameraWalkInTransition();
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
// 3D SCENE & ENGINE INITIALIZATION
// ══════════════════════════════════════════════════════════════════════════════

window.init3DMandirScene = function() {
  const container = document.getElementById('mandir-3d-canvas-container');
  if (!container) return;

  container.innerHTML = '';

  const width = container.clientWidth || window.innerWidth;
  const height = container.clientHeight || window.innerHeight;

  // 1. Scene & Camera Setup (Initial Position outside the temple entrance)
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x090216);
  scene.fog = new THREE.FogExp2(0x090216, 0.022);
  window.Mandir3D.scene = scene;

  const camera = new THREE.PerspectiveCamera(46, width / height, 0.1, 1000);
  window.Mandir3D.camera = camera;
  window.Mandir3D.angle = 0;
  window.Mandir3D.accumulatedAngle = 0;
  
  // Set camera outside temple entrance
  camera.position.set(0, 4.2, 22.0);
  camera.lookAt(0, 2.8, 0);

  // 2. High-Performance WebGL Renderer with ACES Tone Mapping
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.45;
  renderer.outputEncoding = THREE.sRGBEncoding;
  container.appendChild(renderer.domElement);
  window.Mandir3D.renderer = renderer;

  // 3. HDRI Room Environment Reflections
  if (THREE.PMREMGenerator && THREE.RoomEnvironment) {
    const pmrem = new THREE.PMREMGenerator(renderer);
    scene.environment = pmrem.fromScene(new THREE.RoomEnvironment(), 0.04).texture;
  }

  // 4. Sacred Lighting Setup
  const ambient = new THREE.AmbientLight(0x6D3D9E, 1.3);
  scene.add(ambient);
  window.Mandir3D.ambientLight = ambient;

  // Directional Sun / Moonlight
  const sunLight = new THREE.DirectionalLight(0xFFE8B3, 2.2);
  sunLight.position.set(15, 30, 20);
  sunLight.castShadow = true;
  sunLight.shadow.mapSize.width = 1024;
  sunLight.shadow.mapSize.height = 1024;
  scene.add(sunLight);
  window.Mandir3D.sunLight = sunLight;

  // Inner Garbhagriha Altar Spotlight
  const altarSpot = new THREE.SpotLight(0xFFEAA7, 4.5, 35, Math.PI / 3.2, 0.35, 1.1);
  altarSpot.position.set(0, 14, 5);
  altarSpot.castShadow = true;
  scene.add(altarSpot);
  window.Mandir3D.altarSpot = altarSpot;

  // Dynamic Point Lights attached to entrance and sanctum diyas
  window.Mandir3D.diyaLights = [];
  [[-2.8, 1.2, 3.5], [2.8, 1.2, 3.5], [0, 1.0, -1.5]].forEach(pos => {
    const dLight = new THREE.PointLight(0xFF8800, 2.8, 12);
    dLight.position.set(pos[0], pos[1], pos[2]);
    scene.add(dLight);
    window.Mandir3D.diyaLights.push(dLight);
  });

  // 5. Load Custom Hindu Temple 3D Model
  window.loadHinduTempleGLTFModel(scene);

  // 6. Particle Systems (Golden Aura & Flower Shower)
  window.initTempleParticleSystems(scene);

  // 7. Interaction Listeners
  setup3DMandirInteractions(container);

  // 8. Render Animation Loop
  animate3DMandir();
};

// ══════════════════════════════════════════════════════════════════════════════
// GLTF LOADER WITH SMART AUTO-CENTERING & HIGH-FIDELITY PBR
// ══════════════════════════════════════════════════════════════════════════════

window.loadHinduTempleGLTFModel = function(scene) {
  const loaderEl = document.getElementById('mandir-3d-loader');
  const barEl = document.getElementById('mandir-loader-bar');
  const pctEl = document.getElementById('mandir-loader-percent');

  const gltfPath = 'assets/models/hindu_temple/scene.gltf';

  if (typeof THREE.GLTFLoader !== 'undefined') {
    const loader = new THREE.GLTFLoader();

    if (loaderEl) loaderEl.style.display = 'flex';

    loader.load(
      gltfPath,
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
        const targetSize = 18.0;
        const scale = targetSize / maxDim;
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
          showToast('🏛️ भव्य 3D हिन्दू मंदिर मॉडल सफलतापूर्वक लोड हुआ!');
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
        console.warn("GLTF Model load error, falling back to PBR sanctum:", error);
        if (loaderEl) loaderEl.style.display = 'none';
        if (typeof window.buildGrandSanctumEnvironment === 'function') {
          window.buildGrandSanctumEnvironment(scene);
        }
      }
    );
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// PARTICLE SYSTEMS & SOFT GLOW TEXTURES
// ══════════════════════════════════════════════════════════════════════════════

function createSoftGlowParticleTex() {
  const canvas = document.createElement('canvas');
  canvas.width = 64;
  canvas.height = 64;
  const ctx = canvas.getContext('2d');

  const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
  grad.addColorStop(0, 'rgba(254, 243, 199, 1)');
  grad.addColorStop(0.3, 'rgba(248, 200, 59, 0.85)');
  grad.addColorStop(0.7, 'rgba(217, 119, 6, 0.3)');
  grad.addColorStop(1, 'rgba(0, 0, 0, 0)');

  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, 64, 64);
  return new THREE.CanvasTexture(canvas);
}

window.initTempleParticleSystems = function(scene) {
  // 1. Golden Aura Sparkles
  const count = 180;
  const pos = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i += 3) {
    pos[i] = (Math.random() - 0.5) * 14;
    pos[i + 1] = 0.5 + Math.random() * 8;
    pos[i + 2] = (Math.random() - 0.5) * 14;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  
  const mat = new THREE.PointsMaterial({
    map: createSoftGlowParticleTex(),
    size: 0.45,
    transparent: true,
    opacity: 0.9,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });

  const sparkles = new THREE.Points(geo, mat);
  scene.add(sparkles);
  window.Mandir3D.sparkleSystem = sparkles;

  // 2. Lotus Flower Petals for Pushpa Varsha
  window.Mandir3D.petals = [];
  for (let i = 0; i < 80; i++) {
    const petalMat = new THREE.MeshStandardMaterial({
      color: i % 2 === 0 ? 0xF43F5E : 0xFB7185,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0,
      roughness: 0.3
    });
    const petal = new THREE.Mesh(new THREE.PlaneGeometry(0.32, 0.45), petalMat);
    petal.position.set((Math.random() - 0.5) * 8, 8 + Math.random() * 4, (Math.random() - 0.5) * 8);
    petal.visible = false;
    scene.add(petal);
    window.Mandir3D.petals.push({
      mesh: petal,
      vy: 0.055 + Math.random() * 0.05,
      rotX: Math.random() * 0.04,
      rotY: Math.random() * 0.04,
      active: false
    });
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// CAMERA WALK-IN & 360° PARIKRAMA ORBIT
// ══════════════════════════════════════════════════════════════════════════════

window.executeCameraWalkInTransition = function() {
  const camera = window.Mandir3D.camera;
  if (!camera) return;

  window.isCameraWalkingIn = true;

  if (typeof gsap !== 'undefined') {
    gsap.to(camera.position, {
      x: 0,
      y: window.Mandir3D.height,
      z: window.Mandir3D.radius,
      duration: 1.8,
      ease: "power2.out",
      onUpdate: () => {
        camera.lookAt(0, 2.5, 0);
      },
      onComplete: () => {
        window.isCameraWalkingIn = false;
        if (typeof showToast === 'function') {
          showToast('🕉️ भव्य 3D मंदिर में प्रवेश पूर्ण — 360° परिक्रमा आरंभ करें!');
        }
        if (typeof window.checkAndShowFirstTime3DGuide === 'function') {
          window.checkAndShowFirstTime3DGuide();
        }
      }
    });
  } else {
    camera.position.set(0, window.Mandir3D.height, window.Mandir3D.radius);
    camera.lookAt(0, 2.5, 0);
    window.isCameraWalkingIn = false;
  }
};

function setup3DMandirInteractions(container) {
  let isPointerDown = false;

  function onPointerStart(x) {
    if (window.isCameraWalkingIn) return;
    isPointerDown = true;
    window.Mandir3D.prevMouseX = x;
  }

  function onPointerMove(x) {
    if (!isPointerDown || window.isCameraWalkingIn) return;
    const deltaX = x - window.Mandir3D.prevMouseX;
    window.Mandir3D.prevMouseX = x;

    const rotSpeed = 0.007;
    window.Mandir3D.angle -= deltaX * rotSpeed;

    if (deltaX > 0) {
      window.Mandir3D.accumulatedAngle += deltaX * rotSpeed;
      if (window.Mandir3D.accumulatedAngle >= Math.PI * 2) {
        window.Mandir3D.accumulatedAngle -= Math.PI * 2;
        window.onParikramaLapCompleted();
      }
    }
  }

  function onPointerEnd() {
    isPointerDown = false;
  }

  container.addEventListener('mousedown', e => onPointerStart(e.clientX));
  window.addEventListener('mousemove', e => onPointerMove(e.clientX));
  window.addEventListener('mouseup', onPointerEnd);

  container.addEventListener('touchstart', e => {
    if (e.touches.length > 0) onPointerStart(e.touches[0].clientX);
  }, { passive: true });

  window.addEventListener('touchmove', e => {
    if (e.touches.length > 0) onPointerMove(e.touches[0].clientX);
  }, { passive: true });

  window.addEventListener('touchend', onPointerEnd);
}

// ══════════════════════════════════════════════════════════════════════════════
// ANIMATION RENDER LOOP & REAL-TIME LIGHTING
// ══════════════════════════════════════════════════════════════════════════════

function animate3DMandir() {
  window.mandir3DAnimFrame = requestAnimationFrame(animate3DMandir);

  const M = window.Mandir3D;
  if (!M.renderer || !M.scene || !M.camera) return;

  // Parikrama Orbit Positioning
  if (!window.isCameraWalkingIn) {
    if (window.isAutoOrbiting) {
      M.angle += 0.008;
      M.accumulatedAngle += 0.008;
      if (M.accumulatedAngle >= Math.PI * 2) {
        M.accumulatedAngle -= Math.PI * 2;
        window.onParikramaLapCompleted();
      }
    }

    M.camera.position.x = Math.sin(M.angle) * M.radius;
    M.camera.position.z = Math.cos(M.angle) * M.radius;
    M.camera.position.y = M.height;
    M.camera.lookAt(0, 2.5, 0);
  }

  // Dynamic Flickering Diya Point Lights
  if (M.diyaLights && M.diyaLights.length) {
    M.diyaLights.forEach(l => {
      l.intensity = 2.8 + Math.sin(Date.now() * 0.012 + l.position.x) * 0.5;
    });
  }

  // Golden Sparkles Slow Orbit
  if (M.sparkleSystem) {
    M.sparkleSystem.rotation.y += 0.0025;
  }

  // Lotus Petals Physics
  if (M.petals) {
    M.petals.forEach(p => {
      if (p.active) {
        p.mesh.position.y -= p.vy;
        p.mesh.rotation.x += p.rotX;
        p.mesh.rotation.y += p.rotY;
        if (p.mesh.position.y <= 0.2) {
          p.mesh.position.y = 0.2;
          p.mesh.rotation.x = Math.PI / 2;
          p.active = false;
        }
      }
    });
  }

  M.renderer.render(M.scene, M.camera);
}

// ══════════════════════════════════════════════════════════════════════════════
// SEVA ACTIONS, DAY/NIGHT LIGHTING & REWARDS
// ══════════════════════════════════════════════════════════════════════════════

window.onParikramaLapCompleted = function() {
  window.currentParikramaLaps++;
  
  if (navigator.vibrate) navigator.vibrate([40, 30, 60]);

  if (typeof playSoundEffect === 'function' && !window.is3DMandirMuted) {
    playSoundEffect('correct');
  }

  window.updateParikramaProgressBar();

  if (typeof showToast === 'function') {
    showToast(`🚩 परिक्रमा ${window.currentParikramaLaps} पूर्ण! 🕉️`);
  }

  if (window.currentParikramaLaps >= window.targetParikramaLaps) {
    window.isAutoOrbiting = false;
    const btn = document.getElementById('mandir-auto-orbit-btn');
    if (btn) btn.innerHTML = '▶';

    if (typeof playSoundEffect === 'function') playSoundEffect('victory');
    if (typeof triggerFlowerShower === 'function') triggerFlowerShower();

    setTimeout(() => {
      window.showParikramaCompletedCelebration();
    }, 600);
  }
};

window.updateParikramaProgressBar = function() {
  const counter = document.getElementById('parikrama-live-counter');
  const fill = document.getElementById('parikrama-progress-fill');
  const label = document.getElementById('parikrama-mandir-label');

  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
  if (label) label.textContent = deityConfig.title;

  if (counter) {
    counter.textContent = `${window.currentParikramaLaps} / ${window.targetParikramaLaps} पूर्ण`;
  }
  if (fill) {
    const pct = Math.min(100, Math.round((window.currentParikramaLaps / window.targetParikramaLaps) * 100));
    fill.style.width = `${pct}%`;
  }
};

window.trigger3DDiyaGlow = function() {
  if (window.Mandir3D.diyaLights) {
    window.Mandir3D.diyaLights.forEach(l => {
      l.intensity = 5.5;
      l.distance = 20;
    });
    setTimeout(() => {
      if (window.Mandir3D.diyaLights) {
        window.Mandir3D.diyaLights.forEach(l => {
          l.intensity = 2.8;
          l.distance = 12;
        });
      }
    }, 2000);
  }

  if (navigator.vibrate) navigator.vibrate(40);
  if (typeof showToast === 'function') {
    showToast('🪔 दीप ज्योति प्रज्वलित हुई! शुभम् करोति कल्याणम्');
  }
};

window.trigger3DPushpaVarsha = function() {
  if (window.Mandir3D.petals) {
    window.Mandir3D.petals.forEach((p, idx) => {
      setTimeout(() => {
        p.mesh.visible = true;
        p.mesh.material.opacity = 0.95;
        p.mesh.position.set((Math.random() - 0.5) * 8, 8 + Math.random() * 3, (Math.random() - 0.5) * 8);
        p.active = true;
      }, idx * 25);
    });
  }

  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof showToast === 'function') showToast('🌸 प्रभु के चरणों में पुष्प वर्षा समर्पित!');
};

window.trigger3DGhantiNaad = function() {
  if (navigator.vibrate) navigator.vibrate([60, 40, 80]);
  
  if (typeof playSoundEffect === 'function' && !window.is3DMandirMuted) {
    playSoundEffect('correct');
  }
  if (typeof showToast === 'function') {
    showToast('🔔 दिव्य घंटा नाद... ॐ शान्तिः');
  }
};

window.toggle3DAutoOrbit = function() {
  window.isAutoOrbiting = !window.isAutoOrbiting;
  const btn = document.getElementById('mandir-auto-orbit-btn');
  if (btn) {
    btn.innerHTML = window.isAutoOrbiting ? '❚❚' : '▶';
    btn.style.background = window.isAutoOrbiting ? 'linear-gradient(135deg, #10B981, #059669)' : 'rgba(42,13,78,0.85)';
  }
  if (typeof showToast === 'function') {
    showToast(window.isAutoOrbiting ? '▶ स्वतः परिक्रमा चालू' : '⏸️ स्वतः परिक्रमा रोकी गई');
  }
};

window.reset3DCameraView = function() {
  window.Mandir3D.angle = 0;
  window.Mandir3D.height = 3.2;
  window.Mandir3D.radius = 12.0;
  if (typeof showToast === 'function') showToast('🎯 कैमरा दृश्य रीसेट हुआ');
};

window.toggle3DMandirLighting = function() {
  window.is3DMandirNightMode = !window.is3DMandirNightMode;
  const btn = document.getElementById('mandir-lighting-toggle-btn');
  const M = window.Mandir3D;

  if (window.is3DMandirNightMode) {
    if (btn) btn.textContent = '🌙';
    if (M.scene) M.scene.background = new THREE.Color(0x090216);
    if (M.ambientLight) M.ambientLight.color.setHex(0x6D3D9E);
    if (M.sunLight) M.sunLight.intensity = 1.0;
    if (typeof showToast === 'function') showToast('🌙 रात्रि महा-आरती प्रकाश सक्रिय');
  } else {
    if (btn) btn.textContent = '☀️';
    if (M.scene) M.scene.background = new THREE.Color(0x241142);
    if (M.ambientLight) M.ambientLight.color.setHex(0xFFE8D6);
    if (M.sunLight) M.sunLight.intensity = 2.8;
    if (typeof showToast === 'function') showToast('☀️ प्रातःकालीन दिव्य सूर्य प्रकाश सक्रिय');
  }
};

window.toggle3DMandirSound = function() {
  window.is3DMandirMuted = !window.is3DMandirMuted;
  const btn = document.getElementById('mandir-sound-toggle-btn');
  if (btn) btn.textContent = window.is3DMandirMuted ? '🔇' : '🔊';
  if (typeof showToast === 'function') {
    showToast(window.is3DMandirMuted ? '🔇 ध्वनि बंद (Muted)' : '🔊 ध्वनि चालू (Unmuted)');
  }
};

window.switch3DMandirDeity = function(deityKey) {
  window.current3DDeity = deityKey;
  const deityConfig = window.MANDIR_DEITIES[deityKey];
  if (!deityConfig) return;

  window.updateParikramaProgressBar();

  if (typeof showToast === 'function') {
    showToast(`🏛️ ${deityConfig.name} दर्शन`);
  }
};

window.showParikramaCompletedCelebration = function() {
  let currentPoints = parseInt(localStorage.getItem('sanatan_sadhana_points') || '108');
  currentPoints += 25;
  localStorage.setItem('sanatan_sadhana_points', currentPoints.toString());

  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
  const desc = document.getElementById('parikrama-completed-desc');
  if (desc) {
    desc.innerHTML = `आपने <strong>${deityConfig.name}</strong> की <strong>${window.targetParikramaLaps} पावन परिक्रमा</strong> व संपूर्ण दर्शन पूर्ण किया!`;
  }

  const modal = document.getElementById('parikrama-completed-modal');
  if (modal) modal.style.display = 'flex';
};

window.close3DParikramaCompletedModal = function() {
  const modal = document.getElementById('parikrama-completed-modal');
  if (modal) modal.style.display = 'none';
  window.close3DMandirModal();
};

window.share3DParikramaWhatsApp = function() {
  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
  const msg = `🚩 *सनातन दिव्य परिक्रमा संकल्प पूर्ण* 🚩\\nमैंने आज *${deityConfig.name}* के 3D मंदिर में *${window.targetParikramaLaps} पावन परिक्रमा* व दीप-पुष्प पूजन संपन्न किया! 🪔✨\\n\\nआप भी घर बैठे 3D मंदिर में दर्शन व परिक्रमा करें: 'भक्ति में लीन' ऐप डाउनलोड करें 🕉️`;
  
  const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
  window.open(shareUrl, '_blank');
};

// Instructions Guide handlers
window.open3DInstructionsModal = function() {
  const modal = document.getElementById('mandir-3d-instructions-modal');
  if (modal) modal.style.display = 'flex';
};

window.close3DInstructionsModal = function() {
  const modal = document.getElementById('mandir-3d-instructions-modal');
  if (modal) modal.style.display = 'none';
  localStorage.setItem('sanatan_3d_guide_shown', 'true');
};

window.checkAndShowFirstTime3DGuide = function() {
  const isSeen = localStorage.getItem('sanatan_3d_guide_shown');
  if (!isSeen) {
    setTimeout(() => {
      window.open3DInstructionsModal();
    }, 1000);
  }
};
"""

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(real_hindu_temple_engine_js)

# Bump cache buster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
html = re.sub(r'mandir_3d_engine\.js\?v=\d+', f'mandir_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Successfully integrated real Hindu Temple 3D Model into mandir_3d_engine.js (v={ts})")
