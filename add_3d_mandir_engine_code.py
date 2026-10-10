import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# Write mandir_3d_engine.js
engine_code = """// ══════════════════════════════════════════════════════════════════════════════
// 🏛️ 3D REAL-TIME MANDIR & PARIKRAMA SANKALP WEBGL ENGINE (THREE.JS)
// ══════════════════════════════════════════════════════════════════════════════

window.targetParikramaLaps = 11;
window.currentParikramaLaps = 0;
window.isAutoOrbiting = false;
window.is3DMandirNightMode = true;
window.is3DMandirMuted = false;
window.current3DDeity = 'kashi';

// Deity Config
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

// Start Flow with Door Open Animation
window.start3DMandirParikramaFlow = function() {
  const modal = document.getElementById('mandir-3d-modal');
  const doorOverlay = document.getElementById('temple-door-transition-overlay');
  const leftDoor = document.getElementById('door-left');
  const rightDoor = document.getElementById('door-right');

  window.currentParikramaLaps = 0;
  window.updateParikramaProgressBar();

  if (modal) {
    modal.style.display = 'flex';
  }

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
    }, 100);

    setTimeout(() => {
      doorOverlay.style.display = 'none';
    }, 1300);
  }

  // Initialize Three.js WebGL Canvas
  window.init3DMandirScene();
};

window.close3DMandirModal = function() {
  const modal = document.getElementById('mandir-3d-modal');
  if (modal) modal.style.display = 'none';
  if (window.mandir3DAnimFrame) {
    cancelAnimationFrame(window.mandir3DAnimFrame);
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// THREE.JS 3D SCENE CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.Mandir3D = {
  scene: null,
  camera: null,
  renderer: null,
  deityMesh: null,
  altarGroup: null,
  bellMesh: null,
  bellAngle: 0,
  bellVelocity: 0,
  sparkleSystem: null,
  petalSystem: null,
  petals: [],
  diyaLights: [],
  ambientLight: null,
  sunLight: null,
  radius: 14,
  angle: 0,
  targetAngle: 0,
  height: 4.5,
  accumulatedAngle: 0,
  lastAngle: 0,
  isDragging: false,
  prevMouseX: 0
};

window.init3DMandirScene = function() {
  const container = document.getElementById('mandir-3d-canvas-container');
  if (!container) return;

  // Clear previous canvas
  container.innerHTML = '';

  const width = container.clientWidth || window.innerWidth;
  const height = container.clientHeight || window.innerHeight;

  // 1. Scene & Camera
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x070110);
  scene.fog = new THREE.FogExp2(0x070110, 0.035);
  window.Mandir3D.scene = scene;

  const camera = new THREE.PerspectiveCamera(50, width / height, 0.1, 1000);
  window.Mandir3D.camera = camera;
  window.Mandir3D.angle = 0;
  window.Mandir3D.accumulatedAngle = 0;
  window.Mandir3D.lastAngle = 0;
  camera.position.set(0, window.Mandir3D.height, window.Mandir3D.radius);
  camera.lookAt(0, 2.5, 0);

  // 2. Renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  container.appendChild(renderer.domElement);
  window.Mandir3D.renderer = renderer;

  // 3. Lighting System
  const ambient = new THREE.AmbientLight(0x4A2E80, 0.9);
  scene.add(ambient);
  window.Mandir3D.ambientLight = ambient;

  const altarSpot = new THREE.SpotLight(0xFFE4A0, 2.5, 30, Math.PI / 4, 0.5, 1);
  altarSpot.position.set(0, 15, 6);
  altarSpot.castShadow = true;
  scene.add(altarSpot);

  const auraLight = new THREE.PointLight(0xF8C83B, 2.0, 18);
  auraLight.position.set(0, 3.5, 0);
  scene.add(auraLight);

  // 2 Diya point lights
  window.Mandir3D.diyaLights = [];
  [-2.2, 2.2].forEach(x => {
    const dLight = new THREE.PointLight(0xFF8800, 1.8, 8);
    dLight.position.set(x, 1.2, 2.2);
    scene.add(dLight);
    window.Mandir3D.diyaLights.push(dLight);
  });

  // 4. Temple Architecture Geometries

  // 4.1 Marble Floor with Gold Ring
  const floorGeo = new THREE.CylinderGeometry(18, 18, 0.4, 32);
  const floorMat = new THREE.MeshStandardMaterial({
    color: 0x1E0D33,
    roughness: 0.2,
    metalness: 0.3
  });
  const floor = new THREE.Mesh(floorGeo, floorMat);
  floor.position.y = -0.2;
  floor.receiveShadow = true;
  scene.add(floor);

  // Concentric Gold Ring
  const ringGeo = new THREE.RingGeometry(8, 8.3, 48);
  const ringMat = new THREE.MeshBasicMaterial({ color: 0xF8C83B, side: THREE.DoubleSide });
  const goldRing = new THREE.Mesh(ringGeo, ringMat);
  goldRing.rotation.x = -Math.PI / 2;
  goldRing.position.y = 0.02;
  scene.add(goldRing);

  // 4.2 Altar Pedestal (सिंहासन / पीठ)
  const altarGroup = new THREE.Group();
  const baseGeo = new THREE.CylinderGeometry(3.2, 3.8, 1.2, 24);
  const baseMat = new THREE.MeshStandardMaterial({ color: 0xB45309, metalness: 0.6, roughness: 0.3 });
  const altarBase = new THREE.Mesh(baseGeo, baseMat);
  altarBase.position.y = 0.6;
  altarGroup.add(altarBase);

  // Gold Lotus Top Ring
  const lotusGeo = new THREE.TorusGeometry(3.0, 0.2, 16, 32);
  const goldMat = new THREE.MeshStandardMaterial({ color: 0xF8C83B, metalness: 0.8, roughness: 0.2 });
  const lotusRing = new THREE.Mesh(lotusGeo, goldMat);
  lotusRing.rotation.x = Math.PI / 2;
  lotusRing.position.y = 1.2;
  altarGroup.add(lotusRing);

  // 4.3 Central Consecrated Deity Artwork Mesh
  const deityTexLoader = new THREE.TextureLoader();
  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['kashi'];
  const texture = deityTexLoader.load(deityConfig.image);
  
  const deityFrameGeo = new THREE.BoxGeometry(3.6, 4.8, 0.3);
  const frameMat = new THREE.MeshStandardMaterial({ color: 0xF8C83B, metalness: 0.8, roughness: 0.2 });
  const deityMat = new THREE.MeshStandardMaterial({ map: texture, roughness: 0.4 });
  
  const deityMaterials = [
    frameMat, frameMat, frameMat, frameMat,
    deityMat, // Front Face
    frameMat  // Back Face
  ];

  const deityMesh = new THREE.Mesh(deityFrameGeo, deityMaterials);
  deityMesh.position.set(0, 3.8, 0);
  deityMesh.castShadow = true;
  altarGroup.add(deityMesh);
  window.Mandir3D.deityMesh = deityMesh;

  // 4.4 Golden Aura Sunburst Behind Deity
  const auraGeo = new THREE.RingGeometry(2.2, 3.5, 32);
  const auraMat = new THREE.MeshBasicMaterial({ color: 0xF8C83B, side: THREE.DoubleSide, transparent: true, opacity: 0.65 });
  const auraHalo = new THREE.Mesh(auraGeo, auraMat);
  auraHalo.position.set(0, 4.2, -0.2);
  altarGroup.add(auraHalo);

  // 4.5 Brass Diyas (Left & Right)
  [-2.2, 2.2].forEach(x => {
    const diyaBase = new THREE.Mesh(
      new THREE.CylinderGeometry(0.35, 0.2, 0.3, 16),
      goldMat
    );
    diyaBase.position.set(x, 1.2, 2.2);
    altarGroup.add(diyaBase);

    // Glowing Flame
    const flame = new THREE.Mesh(
      new THREE.ConeGeometry(0.12, 0.35, 12),
      new THREE.MeshBasicMaterial({ color: 0xFFDD44 })
    );
    flame.position.set(x, 1.45, 2.2);
    altarGroup.add(flame);
  });

  // 4.6 4 Ornate Brass Temple Pillars
  const pillarPos = [
    [-6, -6], [6, -6], [-6, 6], [6, 6]
  ];
  pillarPos.forEach(p => {
    const pillarGeo = new THREE.CylinderGeometry(0.6, 0.6, 12, 16);
    const pillarMat = new THREE.MeshStandardMaterial({ color: 0x92400E, metalness: 0.7, roughness: 0.3 });
    const pillar = new THREE.Mesh(pillarGeo, pillarMat);
    pillar.position.set(p[0], 6, p[1]);
    pillar.castShadow = true;
    scene.add(pillar);

    // Capital & Base Gold Rings
    [0.5, 11.5].forEach(y => {
      const cap = new THREE.Mesh(new THREE.TorusGeometry(0.8, 0.15, 12, 24), goldMat);
      cap.rotation.x = Math.PI / 2;
      cap.position.set(p[0], y, p[1]);
      scene.add(cap);
    });
  });

  // 4.7 Hanging Temple Bell (🔔)
  const bellGroup = new THREE.Group();
  const chainGeo = new THREE.CylinderGeometry(0.04, 0.04, 4.0, 8);
  const chain = new THREE.Mesh(chainGeo, goldMat);
  chain.position.y = 8.5;
  bellGroup.add(chain);

  const bellBodyGeo = new THREE.ConeGeometry(0.7, 1.0, 16);
  const bellBody = new THREE.Mesh(bellBodyGeo, goldMat);
  bellBody.position.y = 6.5;
  bellGroup.add(bellBody);

  bellGroup.position.set(0, 0, 4.5);
  scene.add(bellGroup);
  window.Mandir3D.bellMesh = bellGroup;

  scene.add(altarGroup);
  window.Mandir3D.altarGroup = altarGroup;

  // 5. Particle Systems

  // 5.1 Golden Aura Sparkles
  const sparkleCount = 120;
  const sparkleGeo = new THREE.BufferGeometry();
  const sparklePos = new Float32Array(sparkleCount * 3);
  for (let i = 0; i < sparkleCount * 3; i += 3) {
    sparklePos[i] = (Math.random() - 0.5) * 8;
    sparklePos[i + 1] = 1 + Math.random() * 6;
    sparklePos[i + 2] = (Math.random() - 0.5) * 8;
  }
  sparkleGeo.setAttribute('position', new THREE.BufferAttribute(sparklePos, 3));
  const sparkleMat = new THREE.PointsMaterial({ color: 0xF8C83B, size: 0.22, transparent: true, opacity: 0.8 });
  const sparkles = new THREE.Points(sparkleGeo, sparkleMat);
  scene.add(sparkles);
  window.Mandir3D.sparkleSystem = sparkles;

  // 5.2 Flower Petals Array for Pushpa Varsha
  window.Mandir3D.petals = [];
  for (let i = 0; i < 70; i++) {
    const petalGeo = new THREE.PlaneGeometry(0.25, 0.35);
    const petalMat = new THREE.MeshStandardMaterial({
      color: i % 2 === 0 ? 0xF472B6 : 0xF97316,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0
    });
    const petal = new THREE.Mesh(petalGeo, petalMat);
    petal.position.set((Math.random() - 0.5) * 6, 8 + Math.random() * 4, (Math.random() - 0.5) * 6);
    petal.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);
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

  // 6. Interaction Listeners (Touch & Mouse 360° Drag)
  setup3DMandirInteractions(container);

  // 7. Animation Render Loop
  animate3DMandir();
};

function setup3DMandirInteractions(container) {
  let isPointerDown = false;
  let startX = 0;

  function onPointerStart(x) {
    isPointerDown = true;
    startX = x;
    window.Mandir3D.prevMouseX = x;
  }

  function onPointerMove(x) {
    if (!isPointerDown) return;
    const deltaX = x - window.Mandir3D.prevMouseX;
    window.Mandir3D.prevMouseX = x;

    // Orbit angle sensitivity
    const rotSpeed = 0.007;
    window.Mandir3D.angle -= deltaX * rotSpeed;

    // Track Parikrama 360 Degree Clockwise Rotation
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

function animate3DMandir() {
  window.mandir3DAnimFrame = requestAnimationFrame(animate3DMandir);

  const M = window.Mandir3D;
  if (!M.renderer || !M.scene || !M.camera) return;

  // Auto Orbit Mode
  if (window.isAutoOrbiting) {
    M.angle += 0.008;
    M.accumulatedAngle += 0.008;
    if (M.accumulatedAngle >= Math.PI * 2) {
      M.accumulatedAngle -= Math.PI * 2;
      window.onParikramaLapCompleted();
    }
  }

  // Update Camera Orbit Position
  M.camera.position.x = Math.sin(M.angle) * M.radius;
  M.camera.position.z = Math.cos(M.angle) * M.radius;
  M.camera.position.y = M.height;
  M.camera.lookAt(0, 2.8, 0);

  // Flickering Diya Lights
  if (M.diyaLights && M.diyaLights.length) {
    M.diyaLights.forEach(l => {
      l.intensity = 1.8 + Math.sin(Date.now() * 0.01 + l.position.x) * 0.35;
    });
  }

  // Sparkles Floating Animation
  if (M.sparkleSystem) {
    M.sparkleSystem.rotation.y += 0.003;
  }

  // Bell Pendulum Harmonic Damping Physics
  if (M.bellMesh && M.bellVelocity !== 0) {
    M.bellAngle += M.bellVelocity;
    M.bellVelocity -= M.bellAngle * 0.05; // Spring force
    M.bellVelocity *= 0.94; // Damping
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
          p.mesh.rotation.x = Math.PI / 2; // Flat on floor
          p.active = false;
        }
      }
    });
  }

  M.renderer.render(M.scene, M.camera);
}

// ══════════════════════════════════════════════════════════════════════════════
// SEVA ACTIONS & PARIKRAMA PROGRESSION
// ══════════════════════════════════════════════════════════════════════════════

window.onParikramaLapCompleted = function() {
  window.currentParikramaLaps++;
  
  // Haptic feedback
  if (navigator.vibrate) navigator.vibrate([40, 30, 60]);

  // Play Bell sound
  if (typeof playSoundEffect === 'function' && !window.is3DMandirMuted) {
    playSoundEffect('correct');
  }

  window.updateParikramaProgressBar();

  if (typeof showToast === 'function') {
    showToast(`🚩 परिक्रमा ${window.currentParikramaLaps} पूर्ण! 🕉️`);
  }

  // Check Target Completion
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
      l.intensity = 4.0;
      l.distance = 15;
    });
    setTimeout(() => {
      if (window.Mandir3D.diyaLights) {
        window.Mandir3D.diyaLights.forEach(l => {
          l.intensity = 1.8;
          l.distance = 8;
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

  if (typeof triggerFlowerShower === 'function') {
    triggerFlowerShower();
  }
  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof showToast === 'function') {
    showToast('🌸 प्रभु के चरणों में पुष्प वर्षा समर्पित!');
  }
};

window.trigger3DGhantiNaad = function() {
  window.Mandir3D.bellVelocity = 0.18; // Kick pendulum swing
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
  window.Mandir3D.height = 4.5;
  window.Mandir3D.radius = 14;
  if (typeof showToast === 'function') showToast('🎯 कैमरा दृश्य रीसेट हुआ');
};

window.toggle3DMandirLighting = function() {
  window.is3DMandirNightMode = !window.is3DMandirNightMode;
  const btn = document.getElementById('mandir-lighting-toggle-btn');
  const M = window.Mandir3D;

  if (window.is3DMandirNightMode) {
    if (btn) btn.textContent = '🌙';
    if (M.scene) M.scene.background = new THREE.Color(0x070110);
    if (M.ambientLight) M.ambientLight.color.setHex(0x4A2E80);
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
  if (btn) {
    btn.textContent = window.is3DMandirMuted ? '🔇' : '🔊';
  }
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
  // Sync +25 Sadhana points
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
    f.write(engine_code)

print("✓ Created mandir_3d_engine.js with full Three.js 3D Garbhagriha & Parikrama system")

# Link mandir_3d_engine.js in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
if 'mandir_3d_engine.js' not in html:
    html = html.replace('<script src="app.js', f'<script src="mandir_3d_engine.js?v={ts}"></script>\n  <script src="app.js')

html = re.sub(r'mandir_3d_engine\.js\?v=\d+', f'mandir_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Linked mandir_3d_engine.js in index.html (v={ts})")
