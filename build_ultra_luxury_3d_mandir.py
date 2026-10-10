import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# Write the new ultra-realistic luxury 3D Mandir Engine
ultra_3d_mandir_code = """// ══════════════════════════════════════════════════════════════════════════════
// 🏛️ ULTRA-REALISTIC 3D TEMPLE GARBHAGRIHA & PARIKRAMA SANKALP ENGINE
// Full Architectural Sanctum, Mandapam, Torana, Royal Chhatra, Samai & PBR
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
    name: 'श्री महाकालेश्वर उज्जैन',
    title: 'श्री महाकालेश्वर परिक्रमा',
    image: 'assets/gallery/divya_shiva.jpg',
    color: 0x8B5CF6,
    mantra: 'ॐ हौं जूं सः भूर्भुवः स्वः'
  },
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
  }
};

window.Mandir3D = {
  scene: null,
  camera: null,
  renderer: null,
  deityMesh: null,
  bellMesh: null,
  bellAngle: 0,
  bellVelocity: 0,
  sparkleSystem: null,
  petals: [],
  diyaLights: [],
  ambientLight: null,
  altarSpot: null,
  auraLight: null,
  radius: 14.5,
  angle: 0,
  height: 4.0,
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
// TEXTURE GENERATORS (Marble Floor Tile, Lotus Petal, Soft Glow Particle)
// ══════════════════════════════════════════════════════════════════════════════

function createMarbleTileTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 512;
  canvas.height = 512;
  const ctx = canvas.getContext('2d');

  // Deep Royal Marble Background
  ctx.fillStyle = '#120524';
  ctx.fillRect(0, 0, 512, 512);

  // Concentric Gold Inlay Grid
  ctx.strokeStyle = '#D97706';
  ctx.lineWidth = 4;
  ctx.strokeRect(8, 8, 496, 496);

  ctx.strokeStyle = '#F8C83B';
  ctx.lineWidth = 2;
  ctx.strokeRect(24, 24, 464, 464);

  // Sacred Diamond Inlay
  ctx.beginPath();
  ctx.moveTo(256, 40);
  ctx.lineTo(472, 256);
  ctx.lineTo(256, 472);
  ctx.lineTo(40, 256);
  ctx.closePath();
  ctx.strokeStyle = 'rgba(248, 200, 59, 0.4)';
  ctx.lineWidth = 3;
  ctx.stroke();

  // Central Lotus Rosette
  ctx.beginPath();
  ctx.arc(256, 256, 48, 0, Math.PI * 2);
  ctx.fillStyle = 'rgba(217, 119, 6, 0.2)';
  ctx.fill();
  ctx.strokeStyle = '#FEF3C7';
  ctx.lineWidth = 2;
  ctx.stroke();

  const tex = new THREE.CanvasTexture(canvas);
  tex.wrapS = THREE.RepeatWrapping;
  tex.wrapT = THREE.RepeatWrapping;
  tex.repeat.set(6, 6);
  return tex;
}

function createSoftCircleParticleTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 64;
  canvas.height = 64;
  const ctx = canvas.getContext('2d');

  const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
  grad.addColorStop(0, 'rgba(254, 243, 199, 1)');
  grad.addColorStop(0.3, 'rgba(248, 200, 59, 0.8)');
  grad.addColorStop(0.7, 'rgba(217, 119, 6, 0.3)');
  grad.addColorStop(1, 'rgba(0, 0, 0, 0)');

  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, 64, 64);

  return new THREE.CanvasTexture(canvas);
}

// ══════════════════════════════════════════════════════════════════════════════
// THREE.JS 3D SCENE & ULTRA-LUXURY TEMPLE GARBHAGRIHA
// ══════════════════════════════════════════════════════════════════════════════

window.init3DMandirScene = function() {
  const container = document.getElementById('mandir-3d-canvas-container');
  if (!container) return;

  container.innerHTML = '';

  const width = container.clientWidth || window.innerWidth;
  const height = container.clientHeight || window.innerHeight;

  // 1. Scene & Camera (Initial Walk-in Doorway Position)
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0A0318);
  scene.fog = new THREE.FogExp2(0x0A0318, 0.022);
  window.Mandir3D.scene = scene;

  const camera = new THREE.PerspectiveCamera(48, width / height, 0.1, 1000);
  window.Mandir3D.camera = camera;
  window.Mandir3D.angle = 0;
  window.Mandir3D.accumulatedAngle = 0;
  
  camera.position.set(0, 3.2, 26);
  camera.lookAt(0, 2.8, 0);

  // 2. High-Fidelity WebGL Renderer with Tone Mapping
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

  // 3. Realistic HDRI Room Environment Reflections
  if (THREE.PMREMGenerator && THREE.RoomEnvironment) {
    const pmrem = new THREE.PMREMGenerator(renderer);
    scene.environment = pmrem.fromScene(new THREE.RoomEnvironment(), 0.04).texture;
  }

  // 4. Consecrated Temple Lighting System
  const ambient = new THREE.AmbientLight(0x5A358C, 1.2);
  scene.add(ambient);
  window.Mandir3D.ambientLight = ambient;

  // Overhead Sanctum Spotlight
  const altarSpot = new THREE.SpotLight(0xFFEAA7, 4.0, 40, Math.PI / 3, 0.4, 1.1);
  altarSpot.position.set(0, 18, 6);
  altarSpot.castShadow = true;
  scene.add(altarSpot);
  window.Mandir3D.altarSpot = altarSpot;

  // Deity Golden Back Aura Light
  const auraLight = new THREE.PointLight(0xF8C83B, 3.2, 22);
  auraLight.position.set(0, 4.8, -0.8);
  scene.add(auraLight);
  window.Mandir3D.auraLight = auraLight;

  // 5. Build Ultra-Luxurious Temple Garbhagriha
  window.buildGrandSanctumEnvironment(scene);

  // 6. Particle Systems (Soft Circles & Lotus Petals)
  window.initParticleSystems(scene);

  // 7. Interaction Listeners
  setup3DMandirInteractions(container);

  // 8. Animation Loop
  animate3DMandir();
};

// ══════════════════════════════════════════════════════════════════════════════
// GRAND SANCTUM ARCHITECTURE BUILDER
// ══════════════════════════════════════════════════════════════════════════════

window.buildGrandSanctumEnvironment = function(scene) {
  const masterGroup = new THREE.Group();

  // Premium PBR Materials
  const goldPBR = new THREE.MeshStandardMaterial({
    color: 0xF8C83B,
    metalness: 0.92,
    roughness: 0.15,
    envMapIntensity: 2.2
  });

  const brassPBR = new THREE.MeshStandardMaterial({
    color: 0xC26D10,
    metalness: 0.85,
    roughness: 0.22,
    envMapIntensity: 1.8
  });

  const darkMarblePBR = new THREE.MeshStandardMaterial({
    color: 0x1A0830,
    map: createMarbleTileTexture(),
    roughness: 0.12,
    metalness: 0.35,
    envMapIntensity: 1.6
  });

  const carvedSandstonePBR = new THREE.MeshStandardMaterial({
    color: 0x240E3E,
    roughness: 0.7,
    metalness: 0.15
  });

  const redVelvetPBR = new THREE.MeshStandardMaterial({
    color: 0x881337,
    roughness: 0.8,
    metalness: 0.1
  });

  // ══════════════════════════════════════════════════════════
  // A. MARBLE SANCTUM FLOOR WITH MULTI-TIER GOLD BORDERS
  // ══════════════════════════════════════════════════════════
  const floorGeo = new THREE.CylinderGeometry(20, 20, 0.6, 64);
  const floor = new THREE.Mesh(floorGeo, darkMarblePBR);
  floor.position.y = -0.3;
  floor.receiveShadow = true;
  masterGroup.add(floor);

  // Outer Gold Inlay Ring
  const ring1 = new THREE.Mesh(new THREE.RingGeometry(16, 16.5, 64), goldPBR);
  ring1.rotation.x = -Math.PI / 2;
  ring1.position.y = 0.02;
  masterGroup.add(ring1);

  // Inner Parikrama Gold Ring
  const ring2 = new THREE.Mesh(new THREE.RingGeometry(9.2, 9.6, 64), goldPBR);
  ring2.rotation.x = -Math.PI / 2;
  ring2.position.y = 0.02;
  masterGroup.add(ring2);

  // ══════════════════════════════════════════════════════════
  // B. BACK SANCTUM WALL & ARCHED CORNICE (पृष्ठ महराब व दीवार)
  // ══════════════════════════════════════════════════════════
  const backWallGeo = new THREE.CylinderGeometry(19, 19, 14, 48, 1, true, Math.PI * 0.7, Math.PI * 0.6);
  const backWall = new THREE.Mesh(backWallGeo, carvedSandstonePBR);
  backWall.position.set(0, 6.7, -2);
  backWall.material.side = THREE.BackSide;
  masterGroup.add(backWall);

  // ══════════════════════════════════════════════════════════
  // C. 6 ORNATE TEMPLE PILLARS WITH TORANA MANDAPAM (नक्काशीदार स्तंभ)
  // ══════════════════════════════════════════════════════════
  const pillarAngles = [
    Math.PI * 0.15, Math.PI * 0.45, Math.PI * 0.85,
    Math.PI * 1.15, Math.PI * 1.55, Math.PI * 1.85
  ];
  const pRadius = 12.5;

  pillarAngles.forEach(ang => {
    const px = Math.sin(ang) * pRadius;
    const pz = Math.cos(ang) * pRadius;
    const pillarGroup = new THREE.Group();

    // 1. Square Carved Base
    const baseBox = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.0, 1.6), brassPBR);
    baseBox.position.y = 0.5;
    baseBox.castShadow = true;
    pillarGroup.add(baseBox);

    // 2. Octagonal Fluted Pillar Shaft
    const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.55, 0.65, 11, 16), darkMarblePBR);
    shaft.position.y = 6.0;
    shaft.castShadow = true;
    pillarGroup.add(shaft);

    // 3. Middle Gold Ring
    const midRing = new THREE.Mesh(new THREE.TorusGeometry(0.72, 0.15, 12, 24), goldPBR);
    midRing.rotation.x = Math.PI / 2;
    midRing.position.y = 5.5;
    pillarGroup.add(midRing);

    // 4. Ornate Capital / Bracket (शीर्ष कोर्बेल)
    const cap = new THREE.Mesh(new THREE.CylinderGeometry(1.3, 0.6, 0.9, 8), goldPBR);
    cap.position.y = 11.5;
    pillarGroup.add(cap);

    // Hanging Mini Bell under Capital
    const miniBell = new THREE.Mesh(new THREE.ConeGeometry(0.18, 0.35, 12), goldPBR);
    miniBell.position.set(0, 10.8, 0.5);
    pillarGroup.add(miniBell);

    pillarGroup.position.set(px, 0, pz);
    masterGroup.add(pillarGroup);
  });

  // Connecting Overhead Mandapam Ring Beam (प्रस्तरा बीम)
  const beamRing = new THREE.Mesh(new THREE.TorusGeometry(pRadius, 0.35, 12, 48), goldPBR);
  beamRing.rotation.x = Math.PI / 2;
  beamRing.position.y = 12.0;
  masterGroup.add(beamRing);

  // ══════════════════════════════════════════════════════════
  // D. MULTI-TIERED OCTAGONAL ROYAL SINGHASAN (अष्टकोणीय सिंहासन)
  // ══════════════════════════════════════════════════════════
  const altarGroup = new THREE.Group();

  // Tier 1: Bottom Broad Octagonal Platform
  const tier1 = new THREE.Mesh(new THREE.CylinderGeometry(5.2, 5.8, 0.5, 8), darkMarblePBR);
  tier1.position.y = 0.25;
  tier1.castShadow = true;
  tier1.receiveShadow = true;
  altarGroup.add(tier1);

  const t1Border = new THREE.Mesh(new THREE.TorusGeometry(5.2, 0.15, 12, 32), goldPBR);
  t1Border.rotation.x = Math.PI / 2;
  t1Border.position.y = 0.5;
  altarGroup.add(t1Border);

  // Tier 2: Middle Red Velvet & Brass Tier
  const tier2 = new THREE.Mesh(new THREE.CylinderGeometry(4.2, 4.6, 0.6, 8), redVelvetPBR);
  tier2.position.y = 0.8;
  tier2.castShadow = true;
  altarGroup.add(tier2);

  // Tier 3: Lotus Petal Pedestal Base (16 3D Lotus Petals)
  const lotusBase = new THREE.Mesh(new THREE.CylinderGeometry(3.5, 3.8, 0.5, 24), brassPBR);
  lotusBase.position.y = 1.35;
  altarGroup.add(lotusBase);

  for (let i = 0; i < 16; i++) {
    const angle = (i / 16) * Math.PI * 2;
    const petal = new THREE.Mesh(new THREE.ConeGeometry(0.45, 0.9, 4), goldPBR);
    petal.rotation.x = Math.PI / 2.3;
    petal.rotation.y = angle;
    petal.position.set(Math.sin(angle) * 3.6, 1.45, Math.cos(angle) * 3.6);
    altarGroup.add(petal);
  }

  // ══════════════════════════════════════════════════════════
  // E. 3D GOLDEN ARCHWAY & RADIANT PRABHAVALI (तोरण व प्रभावली)
  // ══════════════════════════════════════════════════════════
  
  // 1. Left & Right Arch Columns on Altar
  [-2.2, 2.2].forEach(x => {
    const archCol = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.28, 5.2, 16), goldPBR);
    archCol.position.set(x, 4.2, -0.3);
    archCol.castShadow = true;
    altarGroup.add(archCol);
  });

  // 2. Top Golden Torana Arch (मेहराब)
  const toranaArch = new THREE.Mesh(
    new THREE.TorusGeometry(2.2, 0.22, 16, 32, Math.PI),
    goldPBR
  );
  toranaArch.position.set(0, 6.7, -0.3);
  altarGroup.add(toranaArch);

  // Kalash Finial on top of Arch
  const archKalash = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), goldPBR);
  archKalash.position.set(0, 9.1, -0.3);
  altarGroup.add(archKalash);

  // 3. Multi-layer Radiant Prabhavali (सूर्य किरण आभा मण्डल)
  const prabhavaliDisc = new THREE.Mesh(
    new THREE.RingGeometry(2.4, 3.8, 36),
    new THREE.MeshStandardMaterial({
      color: 0xF8C83B,
      metalness: 0.95,
      roughness: 0.1,
      side: THREE.DoubleSide
    })
  );
  prabhavaliDisc.position.set(0, 4.8, -0.4);
  altarGroup.add(prabhavaliDisc);

  // 24 Prabhavali Sun Rays
  for (let r = 0; r < 24; r++) {
    const rAng = (r / 24) * Math.PI * 2;
    const ray = new THREE.Mesh(new THREE.ConeGeometry(0.12, 0.9, 3), goldPBR);
    ray.rotation.z = -rAng;
    ray.position.set(Math.sin(rAng) * 4.0, 4.8 + Math.cos(rAng) * 4.0, -0.38);
    altarGroup.add(ray);
  }

  // ══════════════════════════════════════════════════════════
  // F. 3D CONSECRATED DEITY IDOL (भव्य देव विग्रह)
  // ══════════════════════════════════════════════════════════
  const deityTexLoader = new THREE.TextureLoader();
  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
  const texture = deityTexLoader.load(deityConfig.image);

  const frameGeo = new THREE.BoxGeometry(3.6, 4.8, 0.25);
  const deityFrontMat = new THREE.MeshStandardMaterial({
    map: texture,
    roughness: 0.25,
    metalness: 0.15,
    envMapIntensity: 1.4
  });

  const deityMaterials = [goldPBR, goldPBR, goldPBR, goldPBR, deityFrontMat, goldPBR];
  const deityMesh = new THREE.Mesh(frameGeo, deityMaterials);
  deityMesh.position.set(0, 4.2, 0);
  deityMesh.castShadow = true;
  altarGroup.add(deityMesh);
  window.Mandir3D.deityMesh = deityMesh;

  // ══════════════════════════════════════════════════════════
  // G. OVERHEAD 3D ROYAL GOLDEN CHHATRA (स्वर्ण छत्र / Canopy)
  // ══════════════════════════════════════════════════════════
  const chhatraGroup = new THREE.Group();
  
  // Dome of Chhatra
  const chhatraDome = new THREE.Mesh(
    new THREE.ConeGeometry(2.0, 0.8, 24, 1, true),
    goldPBR
  );
  chhatraDome.position.y = 8.6;
  chhatraGroup.add(chhatraDome);

  // Top Kalash on Chhatra
  const chhatraKalash = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.35, 0.7, 16), goldPBR);
  chhatraKalash.position.y = 9.2;
  chhatraGroup.add(chhatraKalash);

  // Hanging Pearl / Gold droplets along rim
  for (let d = 0; d < 12; d++) {
    const dAng = (d / 12) * Math.PI * 2;
    const drop = new THREE.Mesh(new THREE.SphereGeometry(0.1, 8, 8), goldPBR);
    drop.position.set(Math.sin(dAng) * 2.0, 8.1, Math.cos(dAng) * 2.0);
    chhatraGroup.add(drop);
  }

  altarGroup.add(chhatraGroup);

  // ══════════════════════════════════════════════════════════
  // H. STANDING 5-TIERED BRASS SAMAI / DIYA LAMPS (पीतल समई दीपमाला)
  // ══════════════════════════════════════════════════════════
  window.Mandir3D.diyaLights = [];

  [-3.8, 3.8].forEach(sx => {
    const samaiGroup = new THREE.Group();

    // Samai Base
    const sBase = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.9, 0.4, 20), brassPBR);
    sBase.position.y = 0.2;
    samaiGroup.add(sBase);

    // Samai Central Stem
    const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.16, 4.5, 16), brassPBR);
    stem.position.y = 2.4;
    samaiGroup.add(stem);

    // 3 Tiers of Oil Cups with Flames
    [1.4, 2.8, 4.2].forEach((ty, tIdx) => {
      const cupRadius = 0.85 - tIdx * 0.15;
      const cup = new THREE.Mesh(new THREE.CylinderGeometry(cupRadius, 0.2, 0.2, 16), goldPBR);
      cup.position.y = ty;
      samaiGroup.add(cup);

      // Glowing Wicks & Flames
      const flame = new THREE.Mesh(
        new THREE.ConeGeometry(0.14, 0.4, 12),
        new THREE.MeshBasicMaterial({ color: 0xFFDD44 })
      );
      flame.position.set(0, ty + 0.25, 0);
      samaiGroup.add(flame);
    });

    // Dynamic Point Light for Samai
    const samaiLight = new THREE.PointLight(0xFF8800, 2.5, 10);
    samaiLight.position.set(0, 3.5, 0);
    samaiGroup.add(samaiLight);
    window.Mandir3D.diyaLights.push(samaiLight);

    samaiGroup.position.set(sx, 0, 1.6);
    masterGroup.add(samaiGroup);
  });

  // ══════════════════════════════════════════════════════════
  // I. HANGING 3D TEMPLE BRASS BELL (घंटा नाद)
  // ══════════════════════════════════════════════════════════
  const bellGroup = new THREE.Group();

  // Braided Chain
  const chain = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 5.2, 12), goldPBR);
  chain.position.y = 9.2;
  bellGroup.add(chain);

  // Polished Bell Body with Flared Rim
  const bellBody = new THREE.Mesh(new THREE.ConeGeometry(0.9, 1.3, 24), goldPBR);
  bellBody.position.y = 6.6;
  bellGroup.add(bellBody);

  const bellRim = new THREE.Mesh(new THREE.TorusGeometry(0.9, 0.12, 12, 32), goldPBR);
  bellRim.rotation.x = Math.PI / 2;
  bellRim.position.y = 5.95;
  bellGroup.add(bellRim);

  // Clapper
  const clapper = new THREE.Mesh(new THREE.SphereGeometry(0.2, 12, 12), brassPBR);
  clapper.position.y = 5.75;
  bellGroup.add(clapper);

  bellGroup.position.set(0, 0, 5.0);
  masterGroup.add(bellGroup);
  window.Mandir3D.bellMesh = bellGroup;

  masterGroup.add(altarGroup);
  scene.add(masterGroup);
};

// ══════════════════════════════════════════════════════════════════════════════
// PARTICLE SYSTEMS (SOFT CIRCLE AURA & LOTUS PETAL CASCADE)
// ══════════════════════════════════════════════════════════════════════════════

window.initParticleSystems = function(scene) {
  // 1. Soft Circular Golden Aura Sparkles
  const count = 160;
  const pos = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i += 3) {
    pos[i] = (Math.random() - 0.5) * 9;
    pos[i + 1] = 1 + Math.random() * 7;
    pos[i + 2] = (Math.random() - 0.5) * 9;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  
  const mat = new THREE.PointsMaterial({
    map: createSoftCircleParticleTexture(),
    size: 0.5,
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
  for (let i = 0; i < 70; i++) {
    const petalMat = new THREE.MeshStandardMaterial({
      color: i % 2 === 0 ? 0xF43F5E : 0xFB7185,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0,
      roughness: 0.3
    });
    const petal = new THREE.Mesh(new THREE.PlaneGeometry(0.32, 0.45), petalMat);
    petal.position.set((Math.random() - 0.5) * 7, 9 + Math.random() * 4, (Math.random() - 0.5) * 7);
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
        camera.lookAt(0, 3.2, 0);
      },
      onComplete: () => {
        window.isCameraWalkingIn = false;
        if (typeof showToast === 'function') {
          showToast('🕉️ भव्य गर्भग्रह में प्रवेश पूर्ण — 360° परिक्रमा आरंभ करें!');
        }
      }
    });
  } else {
    camera.position.set(0, window.Mandir3D.height, window.Mandir3D.radius);
    camera.lookAt(0, 3.2, 0);
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
// ANIMATION RENDER LOOP & PHYSICS
// ══════════════════════════════════════════════════════════════════════════════

function animate3DMandir() {
  window.mandir3DAnimFrame = requestAnimationFrame(animate3DMandir);

  const M = window.Mandir3D;
  if (!M.renderer || !M.scene || !M.camera) return;

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
    M.camera.lookAt(0, 3.2, 0);
  }

  // Dynamic Diya Flickering
  if (M.diyaLights && M.diyaLights.length) {
    M.diyaLights.forEach(l => {
      l.intensity = 2.5 + Math.sin(Date.now() * 0.012 + l.position.x) * 0.45;
    });
  }

  // Floating Golden Sparkles Rotation
  if (M.sparkleSystem) {
    M.sparkleSystem.rotation.y += 0.0025;
  }

  // Bell Pendulum Harmonic Damping
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

  // Lotus Petals Cascade Physics
  if (M.petals) {
    M.petals.forEach(p => {
      if (p.active) {
        p.mesh.position.y -= p.vy;
        p.mesh.rotation.x += p.rotX;
        p.mesh.rotation.y += p.rotY;
        if (p.mesh.position.y <= 0.25) {
          p.mesh.position.y = 0.25;
          p.mesh.rotation.x = Math.PI / 2;
          p.active = false;
        }
      }
    });
  }

  M.renderer.render(M.scene, M.camera);
}

// ══════════════════════════════════════════════════════════════════════════════
// SEVA ACTIONS & PROGRESSION
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
      l.intensity = 5.0;
      l.distance = 18;
    });
    setTimeout(() => {
      if (window.Mandir3D.diyaLights) {
        window.Mandir3D.diyaLights.forEach(l => {
          l.intensity = 2.5;
          l.distance = 10;
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
        p.mesh.position.set((Math.random() - 0.5) * 7, 9 + Math.random() * 3, (Math.random() - 0.5) * 7);
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
  window.Mandir3D.height = 4.0;
  window.Mandir3D.radius = 14.5;
  if (typeof showToast === 'function') showToast('🎯 कैमरा दृश्य रीसेट हुआ');
};

window.toggle3DMandirLighting = function() {
  window.is3DMandirNightMode = !window.is3DMandirNightMode;
  const btn = document.getElementById('mandir-lighting-toggle-btn');
  const M = window.Mandir3D;

  if (window.is3DMandirNightMode) {
    if (btn) btn.textContent = '🌙';
    if (M.scene) M.scene.background = new THREE.Color(0x0A0318);
    if (M.ambientLight) M.ambientLight.color.setHex(0x5A358C);
    if (typeof showToast === 'function') showToast('🌙 रात्रि महा-आरती प्रकाश सक्रिय');
  } else {
    if (btn) btn.textContent = '☀️';
    if (M.scene) M.scene.background = new THREE.Color(0x281446);
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
  let currentPoints = parseInt(localStorage.getItem('sanatan_sadhana_points') || '108');
  currentPoints += 25;
  localStorage.setItem('sanatan_sadhana_points', currentPoints.toString());

  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
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
  const deityConfig = window.MANDIR_DEITIES[window.current3DDeity] || window.MANDIR_DEITIES['mahakal'];
  const msg = `🚩 *सनातन दिव्य परिक्रमा संकल्प पूर्ण* 🚩\\nमैंने आज *${deityConfig.name}* के 3D गर्भग्रह में *${window.targetParikramaLaps} पावन परिक्रमा* व दीप-पुष्प पूजन संपन्न किया! 🪔✨\\n\\nआप भी घर बैठे 3D मंदिर में दर्शन व परिक्रमा करें: 'भक्ति में लीन' ऐप डाउनलोड करें 🕉️`;
  
  const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
  window.open(shareUrl, '_blank');
};
"""

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(ultra_3d_mandir_code)

# Bump cache buster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
html = re.sub(r'mandir_3d_engine\.js\?v=\d+', f'mandir_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Successfully built and saved Ultra-Realistic 3D Temple Garbhagriha Architecture (v={ts})")
