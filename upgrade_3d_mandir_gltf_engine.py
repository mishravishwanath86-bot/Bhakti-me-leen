import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html with GLTFLoader, DRACOLoader, RoomEnvironment, GSAP & 3D Loader UI
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add GLTFLoader, DRACOLoader, RoomEnvironment, GSAP
scripts_to_add = """  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/DRACOLoader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/environments/RoomEnvironment.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>"""

if 'GLTFLoader.js' not in html:
    # Replace existing single three.min.js or insert into <head>
    if '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>' in html:
        html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>', scripts_to_add)
    else:
        html = html.replace('</head>', f'{scripts_to_add}\n</head>')

# Add 3D Loading Indicator inside #mandir-3d-modal
loader_ui = """
    <!-- 🌟 3D MODEL LOADING PROGRESS BAR 🌟 -->
    <div id="mandir-3d-loader" style="display:none; position:absolute; inset:0; z-index:90; background:rgba(7,1,16,0.92); backdrop-filter:blur(15px); -webkit-backdrop-filter:blur(15px); flex-direction:column; align-items:center; justify-content:center; padding:1.5rem;">
      <div style="font-size:3rem; margin-bottom:12px; filter:drop-shadow(0 0 18px #F59E0B); animation:pulseGlow 2s infinite;">🏛️</div>
      <div style="font-size:1.1rem; font-weight:900; color:#F8C83B; margin-bottom:6px;">दिव्य 3D गर्भग्रह लोड हो रहा है...</div>
      <p style="font-size:0.8rem; color:#CBD5E1; margin:0 0 16px 0;">3D Real-time PBR Textures & Geometry</p>
      
      <div style="width:240px; height:8px; background:rgba(255,255,255,0.1); border-radius:10px; overflow:hidden; border:1px solid rgba(248,200,59,0.3);">
        <div id="mandir-loader-bar" style="width:15%; height:100%; background:linear-gradient(90deg, #F8C83B, #FF512F); border-radius:10px; transition:width 0.25s ease; box-shadow:0 0 12px rgba(248,200,59,0.8);"></div>
      </div>
      <span id="mandir-loader-percent" style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-top:8px;">15%</span>
    </div>
"""

if 'id="mandir-3d-loader"' not in html:
    html = html.replace('<div id="mandir-3d-canvas-container"', loader_ui + '\n    <div id="mandir-3d-canvas-container"')

# Bump cache buster
ts = int(time.time())
html = re.sub(r'mandir_3d_engine\.js\?v=\d+', f'mandir_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Updated index.html with GLTFLoader, DRACOLoader, RoomEnvironment, GSAP and Loader UI")

# 2. Rewrite mandir_3d_engine.js with GLTFLoader, Walk-in Camera Transition, and PBR Engine
gltf_engine_js = """// ══════════════════════════════════════════════════════════════════════════════
// 🏛️ 3D REAL-TIME MANDIR & PARIKRAMA SANKALP WEBGL ENGINE
// Powered by Three.js, GLTFLoader, DRACOLoader, PBR Lighting & GSAP Walk-in
// ══════════════════════════════════════════════════════════════════════════════

window.targetParikramaLaps = 11;
window.currentParikramaLaps = 0;
window.isAutoOrbiting = false;
window.is3DMandirNightMode = true;
window.is3DMandirMuted = false;
window.current3DDeity = 'kashi';
window.isCameraWalkingIn = false;

// Deity Configuration
window.MANDIR_DEITIES = {
  'kashi': {
    name: 'श्री काशी विश्वनाथ',
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
    image: 'assets/gallery/divya_ganesha.jpg',
    color: 0xEF4444,
    mantra: 'ॐ गं गणपतये नमः'
  },
  'mahakal': {
    name: 'श्री महाकालेश्वर उज्जैन',
    title: 'श्री महाकालेश्वर परिक्रमा',
    image: 'assets/gallery/divya_shiva.jpg',
    color: 0x8B5CF6,
    mantra: 'ॐ हौं जूं सः भूर्भुवः स्वः'
  }
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

// ══════════════════════════════════════════════════════════════════════════════
// 3D SCENE & ENGINE CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.Mandir3D = {
  scene: null,
  camera: null,
  renderer: null,
  pmremGenerator: null,
  gltfModel: null,
  deityMesh: null,
  altarGroup: null,
  bellMesh: null,
  bellAngle: 0,
  bellVelocity: 0,
  sparkleSystem: null,
  petals: [],
  diyaLights: [],
  ambientLight: null,
  sunLight: null,
  radius: 13.5,
  angle: 0,
  height: 4.2,
  accumulatedAngle: 0,
  lastAngle: 0,
  isDragging: false,
  prevMouseX: 0
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

  // Initialize Three.js WebGL Canvas with Camera outside Door
  window.init3DMandirScene();

  if (doorOverlay && leftDoor && rightDoor) {
    doorOverlay.style.display = 'block';
    leftDoor.style.transform = 'scaleX(1)';
    rightDoor.style.transform = 'scaleX(1)';

    // Play Bell/Shankh
    if (typeof playSoundEffect === 'function' && !window.is3DMandirMuted) {
      playSoundEffect('victory');
    }

    // Swing doors open smoothly
    setTimeout(() => {
      leftDoor.style.transform = 'scaleX(0)';
      rightDoor.style.transform = 'scaleX(0)';

      // Trigger Cinematic Camera Walk-in Transition into Garbhagriha
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
// GLTFLOADER & THREE.JS INITIALIZATION
// ══════════════════════════════════════════════════════════════════════════════

window.init3DMandirScene = function() {
  const container = document.getElementById('mandir-3d-canvas-container');
  if (!container) return;

  container.innerHTML = '';

  const width = container.clientWidth || window.innerWidth;
  const height = container.clientHeight || window.innerHeight;

  // 1. Scene & Camera Setup (Initial Position outside doorway)
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x070110);
  scene.fog = new THREE.FogExp2(0x070110, 0.028);
  window.Mandir3D.scene = scene;

  const camera = new THREE.PerspectiveCamera(50, width / height, 0.1, 1000);
  window.Mandir3D.camera = camera;
  window.Mandir3D.angle = 0;
  window.Mandir3D.accumulatedAngle = 0;
  
  // Set initial position outside the temple entrance threshold
  camera.position.set(0, 3.2, 26);
  camera.lookAt(0, 2.5, 0);

  // 2. WebGL Renderer with PBR ACES Filmic Tone Mapping
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.35;
  renderer.outputEncoding = THREE.sRGBEncoding;
  container.appendChild(renderer.domElement);
  window.Mandir3D.renderer = renderer;

  // 3. HDRI / Environment Reflections (PMREMGenerator & RoomEnvironment)
  if (THREE.PMREMGenerator) {
    const pmremGenerator = new THREE.PMREMGenerator(renderer);
    pmremGenerator.compileEquirectangularShader();
    if (THREE.RoomEnvironment) {
      scene.environment = pmremGenerator.fromScene(new THREE.RoomEnvironment(), 0.04).texture;
    }
  }

  // 4. Lighting System
  const ambient = new THREE.AmbientLight(0x52327D, 1.1);
  scene.add(ambient);
  window.Mandir3D.ambientLight = ambient;

  // Main Sanctum Spotlight targeting Deity Altar
  const altarSpot = new THREE.SpotLight(0xFFE5A3, 3.2, 35, Math.PI / 3.5, 0.4, 1.2);
  altarSpot.position.set(0, 16, 7);
  altarSpot.castShadow = true;
  scene.add(altarSpot);

  // Backlight for Sacred Aura
  const auraLight = new THREE.PointLight(0xF8C83B, 2.5, 20);
  auraLight.position.set(0, 4.0, -0.5);
  scene.add(auraLight);

  // Dynamic Point Lights attached to Diya Coordinates
  window.Mandir3D.diyaLights = [];
  [-2.2, 2.2].forEach(x => {
    const dLight = new THREE.PointLight(0xFF8800, 2.2, 9);
    dLight.position.set(x, 1.4, 2.2);
    scene.add(dLight);
    window.Mandir3D.diyaLights.push(dLight);
  });

  // 5. Load Custom 3D Model via GLTFLoader + DRACOLoader
  window.loadTempleGLBModel(scene);

  // 6. Particle Systems (Golden Aura & Pushpa Varsha)
  window.initParticleSystems(scene);

  // 7. Interaction Listeners (360° Drag & Orbit)
  setup3DMandirInteractions(container);

  // 8. Render Animation Loop
  animate3DMandir();
};

// ══════════════════════════════════════════════════════════════════════════════
// GLTF & DRACO LOADER WITH PBR ARCHITECTURAL FALLBACK
// ══════════════════════════════════════════════════════════════════════════════

window.loadTempleGLBModel = function(scene) {
  const loaderEl = document.getElementById('mandir-3d-loader');
  const barEl = document.getElementById('mandir-loader-bar');
  const pctEl = document.getElementById('mandir-loader-percent');

  // Candidate paths for custom GLB model
  const glbPaths = [
    'assets/models/temple_interior.glb',
    'public/assets/models/temple_interior.glb'
  ];

  let isModelLoaded = false;

  if (typeof THREE.GLTFLoader !== 'undefined') {
    const loader = new THREE.GLTFLoader();
    
    if (typeof THREE.DRACOLoader !== 'undefined') {
      const dracoLoader = new THREE.DRACOLoader();
      dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.6/');
      loader.setDRACOLoader(dracoLoader);
    }

    if (loaderEl) loaderEl.style.display = 'flex';

    // Attempt loading primary path
    loader.load(
      glbPaths[0],
      (gltf) => {
        isModelLoaded = true;
        const model = gltf.scene;
        model.scale.set(1.5, 1.5, 1.5);
        model.position.set(0, 0, 0);
        model.traverse((child) => {
          if (child.isMesh) {
            child.castShadow = true;
            child.receiveShadow = true;
            if (child.material) {
              child.material.envMapIntensity = 1.4;
            }
          }
        });
        scene.add(model);
        window.Mandir3D.gltfModel = model;

        if (loaderEl) loaderEl.style.display = 'none';
        if (typeof showToast === 'function') {
          showToast('🏛️ 3D मंदिर मॉडल सफलतापूर्वक लोड हुआ!');
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
        console.warn("GLB file not found on disk or loading failed. Loading High-Fidelity PBR Sanctum Fallback:", error);
        if (loaderEl) loaderEl.style.display = 'none';
        window.buildHighFidelityPBRSanctum(scene);
      }
    );
  } else {
    window.buildHighFidelityPBRSanctum(scene);
  }
};

// High-Fidelity PBR Sanctum Architecture (Graceful, crash-free fallback)
window.buildHighFidelityPBRSanctum = function(scene) {
  const altarGroup = new THREE.Group();

  // PBR Gold & Marble Materials
  const goldPBR = new THREE.MeshStandardMaterial({
    color: 0xF8C83B,
    metalness: 0.9,
    roughness: 0.15,
    envMapIntensity: 2.0
  });

  const brassPBR = new THREE.MeshStandardMaterial({
    color: 0xB45309,
    metalness: 0.75,
    roughness: 0.25,
    envMapIntensity: 1.5
  });

  const marblePBR = new THREE.MeshStandardMaterial({
    color: 0x1A0933,
    metalness: 0.2,
    roughness: 0.18,
    envMapIntensity: 1.2
  });

  // 1. Marble Sanctum Floor
  const floor = new THREE.Mesh(new THREE.CylinderGeometry(18, 18, 0.4, 48), marblePBR);
  floor.position.y = -0.2;
  floor.receiveShadow = true;
  scene.add(floor);

  // Concentric Gold Inlay Ring
  const goldRing = new THREE.Mesh(
    new THREE.RingGeometry(8, 8.4, 64),
    goldPBR
  );
  goldRing.rotation.x = -Math.PI / 2;
  goldRing.position.y = 0.02;
  scene.add(goldRing);

  // 2. Central Altar (सिंहासन / पीठ)
  const base = new THREE.Mesh(new THREE.CylinderGeometry(3.4, 4.0, 1.2, 32), brassPBR);
  base.position.y = 0.6;
  base.castShadow = true;
  base.receiveShadow = true;
  altarGroup.add(base);

  // Golden Lotus Torus Ring
  const lotusTorus = new THREE.Mesh(new THREE.TorusGeometry(3.2, 0.22, 16, 48), goldPBR);
  lotusTorus.rotation.x = Math.PI / 2;
  lotusTorus.position.y = 1.2;
  altarGroup.add(lotusTorus);

  // 3. Consecrated Deity Artwork Idol
  const deityTexLoader = new THREE.TextureLoader();
  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['kashi'];
  const texture = deityTexLoader.load(deityConfig.image);
  
  const frameGeo = new THREE.BoxGeometry(3.8, 5.0, 0.35);
  const deityMat = new THREE.MeshStandardMaterial({ map: texture, roughness: 0.3, envMapIntensity: 1.2 });
  const materials = [goldPBR, goldPBR, goldPBR, goldPBR, deityMat, goldPBR];

  const deityMesh = new THREE.Mesh(frameGeo, materials);
  deityMesh.position.set(0, 4.0, 0);
  deityMesh.castShadow = true;
  altarGroup.add(deityMesh);
  window.Mandir3D.deityMesh = deityMesh;

  // 4. Golden Aura Halo Ring
  const auraRing = new THREE.Mesh(
    new THREE.RingGeometry(2.4, 3.6, 48),
    new THREE.MeshBasicMaterial({ color: 0xF8C83B, side: THREE.DoubleSide, transparent: true, opacity: 0.75 })
  );
  auraRing.position.set(0, 4.5, -0.25);
  altarGroup.add(auraRing);

  // 5. Brass Diyas with Glowing Flame Points
  [-2.2, 2.2].forEach(x => {
    const diya = new THREE.Mesh(new THREE.CylinderGeometry(0.38, 0.22, 0.32, 20), goldPBR);
    diya.position.set(x, 1.2, 2.2);
    altarGroup.add(diya);

    const flame = new THREE.Mesh(
      new THREE.ConeGeometry(0.14, 0.4, 16),
      new THREE.MeshBasicMaterial({ color: 0xFFDD44 })
    );
    flame.position.set(x, 1.5, 2.2);
    altarGroup.add(flame);
  });

  // 6. 4 Carved Brass Pillars
  const pillarCoords = [[-6, -6], [6, -6], [-6, 6], [6, 6]];
  pillarCoords.forEach(p => {
    const pillar = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.65, 12, 24), brassPBR);
    pillar.position.set(p[0], 6, p[1]);
    pillar.castShadow = true;
    scene.add(pillar);

    [0.5, 11.5].forEach(y => {
      const cap = new THREE.Mesh(new THREE.TorusGeometry(0.85, 0.18, 16, 32), goldPBR);
      cap.rotation.x = Math.PI / 2;
      cap.position.set(p[0], y, p[1]);
      scene.add(cap);
    });
  });

  // 7. Hanging Brass Temple Bell (🔔)
  const bellGroup = new THREE.Group();
  const chain = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 4.5, 12), goldPBR);
  chain.position.y = 8.5;
  bellGroup.add(chain);

  const bellBody = new THREE.Mesh(new THREE.ConeGeometry(0.75, 1.1, 24), goldPBR);
  bellBody.position.y = 6.4;
  bellGroup.add(bellBody);

  bellGroup.position.set(0, 0, 4.5);
  scene.add(bellGroup);
  window.Mandir3D.bellMesh = bellGroup;

  scene.add(altarGroup);
  window.Mandir3D.altarGroup = altarGroup;
};

// ══════════════════════════════════════════════════════════════════════════════
// CAMERA WALK-IN & 360° ORBIT TRANSITION
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
        camera.lookAt(0, 2.8, 0);
      },
      onComplete: () => {
        window.isCameraWalkingIn = false;
        if (typeof showToast === 'function') {
          showToast('🕉️ गर्भग्रह में प्रवेश पूर्ण — परिक्रमा आरंभ करें!');
        }
      }
    });
  } else {
    camera.position.set(0, window.Mandir3D.height, window.Mandir3D.radius);
    camera.lookAt(0, 2.8, 0);
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

    // Track Parikrama Clockwise Rotation
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
// PARTICLE SYSTEMS & ANIMATION RENDER LOOP
// ══════════════════════════════════════════════════════════════════════════════

window.initParticleSystems = function(scene) {
  // 1. Golden Aura Sparkles
  const count = 140;
  const pos = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i += 3) {
    pos[i] = (Math.random() - 0.5) * 8;
    pos[i + 1] = 1 + Math.random() * 6;
    pos[i + 2] = (Math.random() - 0.5) * 8;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.PointsMaterial({ color: 0xF8C83B, size: 0.22, transparent: true, opacity: 0.85 });
  const sparkles = new THREE.Points(geo, mat);
  scene.add(sparkles);
  window.Mandir3D.sparkleSystem = sparkles;

  // 2. Flower Petals for Pushpa Varsha
  window.Mandir3D.petals = [];
  for (let i = 0; i < 70; i++) {
    const petalMat = new THREE.MeshStandardMaterial({
      color: i % 2 === 0 ? 0xF472B6 : 0xF97316,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0
    });
    const petal = new THREE.Mesh(new THREE.PlaneGeometry(0.26, 0.36), petalMat);
    petal.position.set((Math.random() - 0.5) * 6, 8 + Math.random() * 4, (Math.random() - 0.5) * 6);
    petal.visible = false;
    scene.add(petal);
    window.Mandir3D.petals.push({
      mesh: petal,
      vy: 0.05 + Math.random() * 0.05,
      rotX: Math.random() * 0.04,
      rotY: Math.random() * 0.04,
      active: false
    });
  }
};

function animate3DMandir() {
  window.mandir3DAnimFrame = requestAnimationFrame(animate3DMandir);

  const M = window.Mandir3D;
  if (!M.renderer || !M.scene || !M.camera) return;

  // Orbit Positioning (if not performing walk-in)
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
    M.camera.lookAt(0, 2.8, 0);
  }

  // Flickering Diya Point Lights
  if (M.diyaLights && M.diyaLights.length) {
    M.diyaLights.forEach(l => {
      l.intensity = 2.2 + Math.sin(Date.now() * 0.012 + l.position.x) * 0.4;
    });
  }

  // Sparkles Floating Rotation
  if (M.sparkleSystem) {
    M.sparkleSystem.rotation.y += 0.003;
  }

  // Bell Pendulum Harmonic Damping Physics
  if (M.bellMesh && M.bellVelocity !== 0) {
    M.bellAngle += M.bellVelocity;
    M.bellVelocity -= M.bellAngle * 0.05;
    M.bellVelocity *= 0.94;
    M.bellMesh.rotation.z = M.bellAngle;
    if (Math.abs(M.bellVelocity) < 0.001 && Math.abs(M.bellAngle) < 0.001) {
      M.bellVelocity = 0;
      M.bellAngle = 0;
      M.bellMesh.rotation.z = 0;
    }
  }

  // Flower Petals Cascade Physics
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
// SEVA ACTIONS, AUDIO & PROGRESSION
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

    if (typeof playSoundEffect === 'function') {
      playSoundEffect('victory');
    }
    if (typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
    }

    setTimeout(() => {
      window.showParikramaCompletedCelebration();
    }, 600);
  }
};

window.updateParikramaProgressBar = function() {
  const counter = document.getElementById('parikrama-live-counter');
  const fill = document.getElementById('parikrama-progress-fill');
  const label = document.getElementById('parikrama-mandir-label');

  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['kashi'];
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
      l.intensity = 4.5;
      l.distance = 16;
    });
    setTimeout(() => {
      if (window.Mandir3D.diyaLights) {
        window.Mandir3D.diyaLights.forEach(l => {
          l.intensity = 2.2;
          l.distance = 9;
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
        p.mesh.position.set((Math.random() - 0.5) * 6, 8 + Math.random() * 3, (Math.random() - 0.5) * 6);
        p.active = true;
      }, idx * 25);
    });
  }

  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof showToast === 'function') showToast('🌸 प्रभु के चरणों में पुष्प वर्षा समर्पित!');
};

window.trigger3DGhantiNaad = function() {
  window.Mandir3D.bellVelocity = 0.18;
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
  window.Mandir3D.height = 4.2;
  window.Mandir3D.radius = 13.5;
  if (typeof showToast === 'function') showToast('🎯 कैमरा दृश्य रीसेट हुआ');
};

window.toggle3DMandirLighting = function() {
  window.is3DMandirNightMode = !window.is3DMandirNightMode;
  const btn = document.getElementById('mandir-lighting-toggle-btn');
  const M = window.Mandir3D;

  if (window.is3DMandirNightMode) {
    if (btn) btn.textContent = '🌙';
    if (M.scene) M.scene.background = new THREE.Color(0x070110);
    if (M.ambientLight) M.ambientLight.color.setHex(0x52327D);
    if (typeof showToast === 'function') showToast('🌙 रात्रि महा-आरती प्रकाश सक्रिय');
  } else {
    if (btn) btn.textContent = '☀️';
    if (M.scene) M.scene.background = new THREE.Color(0x2A1B4E);
    if (M.ambientLight) M.ambientLight.color.setHex(0xFFE8D6);
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

  const textureLoader = new THREE.TextureLoader();
  textureLoader.load(deityConfig.image, (tex) => {
    if (window.Mandir3D.deityMesh) {
      window.Mandir3D.deityMesh.material[4].map = tex;
      window.Mandir3D.deityMesh.material[4].needsUpdate = true;
    }
  });

  window.updateParikramaProgressBar();

  if (typeof showToast === 'function') {
    showToast(`🏛️ ${deityConfig.name} दर्शन`);
  }
};

window.showParikramaCompletedCelebration = function() {
  let currentPoints = parseInt(localStorage.getItem('sanatan_sadhana_points') || '108');
  currentPoints += 25;
  localStorage.setItem('sanatan_sadhana_points', currentPoints.toString());

  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['kashi'];
  const desc = document.getElementById('parikrama-completed-desc');
  if (desc) {
    desc.innerHTML = `आपने <strong>${deityConfig.name}</strong> की <strong>${window.targetParikramaLaps} पावन परिक्रमा</strong> व संपूर्ण पूजन पूर्ण किया!`;
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
  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['kashi'];
  const msg = `🚩 *सनातन दिव्य परिक्रमा संकल्प पूर्ण* 🚩\\nमैंने आज *${deityConfig.name}* के 3D गर्भग्रह में *${window.targetParikramaLaps} पावन परिक्रमा* व दीप-पुष्प पूजन संपन्न किया! 🪔✨\\n\\nआप भी घर बैठे 3D मंदिर में दर्शन व परिक्रमा करें: 'भक्ति में लीन' ऐप डाउनलोड करें 🕉️`;
  
  const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
  window.open(shareUrl, '_blank');
};
"""

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(gltf_engine_js)

print("✓ Updated mandir_3d_engine.js with GLTFLoader, DRACOLoader, PBR Lighting & Camera Walk-in Transition")
