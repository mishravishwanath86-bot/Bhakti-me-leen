/**
 * Simulation Test for all 4 Bhakti App sections:
 * 1. Sundarkand Doha Sangrah
 * 2. Vedic Mantra Sangrah
 * 3. Nitya Pavan Chalisa Sangrah
 * 4. Nitya Pavan Aarti Sangrah
 */

const fs = require('fs');
const path = require('path');

// Mock DOM environment
const elements = {};
function createMockEl(tag = 'div') {
  return {
    tagName: tag.toUpperCase(),
    innerHTML: '',
    innerText: '',
    textContent: '',
    style: {},
    classList: {
      add: () => {},
      remove: () => {},
      contains: () => false,
      toggle: () => {}
    },
    dataset: {},
    appendChild: (child) => child,
    removeChild: (child) => child,
    remove: function() {},
    setAttribute: () => {},
    getAttribute: () => null,
    querySelector: (sel) => createMockEl(),
    querySelectorAll: (sel) => [],
    addEventListener: () => {},
    dispatchEvent: () => {},
    click: () => {},
    focus: () => {},
    scrollIntoView: () => {}
  };
}

global.window = global;
global.document = {
  getElementById: (id) => {
    if (!elements[id]) elements[id] = createMockEl();
    return elements[id];
  },
  querySelector: (sel) => createMockEl(),
  querySelectorAll: (sel) => [],
  createElement: (tag) => createMockEl(tag),
  body: createMockEl('body'),
  addEventListener: () => {}
};

global.Audio = class {
  constructor(src) {
    this.src = src || '';
    this.paused = true;
    this.currentTime = 0;
    this.duration = 120;
    this.playbackRate = 1.0;
  }
  play() {
    this.paused = false;
    return Promise.resolve();
  }
  pause() {
    this.paused = true;
  }
  addEventListener(event, cb) {}
  removeEventListener(event, cb) {}
};

global.AudioContext = class {
  constructor() {
    this.state = 'running';
    this.currentTime = 0;
    this.destination = {};
  }
  createOscillator() {
    return {
      type: 'sine',
      frequency: { setValueAtTime: () => {} },
      connect: () => {},
      start: () => {},
      stop: () => {}
    };
  }
  createGain() {
    return {
      gain: {
        value: 0,
        setValueAtTime: () => {},
        exponentialRampToValueAtTime: () => {},
        linearRampToValueAtTime: () => {},
        cancelScheduledValues: () => {}
      },
      connect: () => {}
    };
  }
  createBiquadFilter() {
    return {
      type: 'lowpass',
      frequency: { setValueAtTime: () => {} },
      connect: () => {}
    };
  }
  close() { return Promise.resolve(); }
};
global.webkitAudioContext = global.AudioContext;

// Mock fetch to test API calls
let fetchCalls = [];
global.fetch = function(url, options) {
  fetchCalls.push({ url, options });
  if (url.includes('/api/ai-audio/generate')) {
    const body = options && options.body ? JSON.parse(options.body) : {};
    return Promise.resolve({
      ok: true,
      json: () => Promise.resolve({
        success: true,
        audio_url: `/assets/ai_audio/simulated_${body.content_type || 'test'}.mp3`,
        cadence: 'simulated',
        cached: true
      })
    });
  }
  return Promise.resolve({
    ok: true,
    json: () => Promise.resolve({ items: [] })
  });
};

// Track toasts / alerts
let toasts = [];
global.showToast = function(msg) {
  toasts.push(msg);
  console.log('   [Toast]:', msg);
};

// Load AiBhaktiPlayer
const playerCode = fs.readFileSync(path.join(__dirname, 'ai_bhakti_player.js'), 'utf8');
eval(playerCode);

// Load Mantra Engine
const mantraCode = fs.readFileSync(path.join(__dirname, 'mantra_engine.js'), 'utf8');
eval(mantraCode);

// Load Sundarkand Engine
const sundarkandCode = fs.readFileSync(path.join(__dirname, 'sundarkand_engine.js'), 'utf8');
eval(sundarkandCode);

console.log('======================================================');
console.log('SIMULATION TEST: 4 BHAKTI APP SECTIONS');
console.log('======================================================\n');

let passCount = 0;
let failCount = 0;

function assert(condition, testName) {
  if (condition) {
    console.log(`[PASS] ${testName}`);
    passCount++;
  } else {
    console.error(`[FAIL] ${testName}`);
    failCount++;
  }
}

async function runTests() {
  // ------------------------------------------------------------------
  // 1. Aarti Section Simulation
  // ------------------------------------------------------------------
  console.log('--- 1. Testing Aarti Section Wiring ---');
  toasts = [];
  fetchCalls = [];
  
  // Simulate Aarti reading & playing
  const mockAarti = {
    id: 'aarti-hanuman-test',
    title: 'श्री हनुमान जी की आरती',
    deity_id: 'hanuman',
    content_type: 'aarti',
    content_text: 'आरती कीजै हनुमान लला की। दुष्ट दलन रघुनाथ कला की॥ जाके बल से गिरिवर कांपै। रोग दोष जाके निकट न झांपै॥'
  };

  // As wired in app.js:
  window.AiBhaktiPlayer.loadContent({
    id: mockAarti.id,
    title: mockAarti.title,
    text: mockAarti.content_text,
    type: 'aarti',
    deity: mockAarti.deity_id
  });

  assert(window.AiBhaktiPlayer.currentContent !== null, 'Aarti: currentContent is loaded');
  assert(window.AiBhaktiPlayer.currentContent.id === mockAarti.id, 'Aarti: Content ID matches');
  assert(window.AiBhaktiPlayer.currentContent.type === 'aarti', 'Aarti: Content Type is aarti');
  
  // Now simulate user tapping Play
  await window.AiBhaktiPlayer.togglePlay();
  assert(toasts.every(t => !t.includes('कोई सामग्री लोड नहीं')), 'Aarti: No "कोई सामग्री लोड नहीं है" error on play');
  assert(fetchCalls.some(f => f.url.includes('/api/ai-audio/generate')), 'Aarti: /api/ai-audio/generate was called');

  // ------------------------------------------------------------------
  // 2. Chalisa Section Simulation
  // ------------------------------------------------------------------
  console.log('\n--- 2. Testing Chalisa Section Wiring ---');
  toasts = [];
  fetchCalls = [];

  const mockChalisa = {
    id: 'chalisa-shiv-test',
    title: 'श्री शिव चालीसा',
    deity_id: 'shiva',
    content_type: 'chalisa',
    content_text: 'जय गणेश गिरिजा सुवन, मंगल मूल सुजान। कहत अयोध्यादास तुम, देहु अभय वरदान॥ जय गिरिजापति दीन दयाला...'
  };

  // As wired in app.js:
  window.AiBhaktiPlayer.loadContent({
    id: mockChalisa.id,
    title: mockChalisa.title,
    text: mockChalisa.content_text,
    type: 'chalisa',
    deity: mockChalisa.deity_id
  });

  assert(window.AiBhaktiPlayer.currentContent !== null, 'Chalisa: currentContent is loaded');
  assert(window.AiBhaktiPlayer.currentContent.id === mockChalisa.id, 'Chalisa: Content ID matches');
  assert(window.AiBhaktiPlayer.currentContent.type === 'chalisa', 'Chalisa: Content Type is chalisa');

  await window.AiBhaktiPlayer.togglePlay();
  assert(toasts.every(t => !t.includes('कोई सामग्री लोड नहीं')), 'Chalisa: No "कोई सामग्री लोड नहीं है" error on play');
  assert(fetchCalls.some(f => f.url.includes('/api/ai-audio/generate')), 'Chalisa: /api/ai-audio/generate was called');

  // ------------------------------------------------------------------
  // 3. Vedic Mantra Section Simulation
  // ------------------------------------------------------------------
  console.log('\n--- 3. Testing Vedic Mantra Section Wiring ---');
  toasts = [];
  fetchCalls = [];

  const mockMantra = {
    id: 'mantra-mrityunjaya-test',
    title: 'महामृत्युंजय मंत्र',
    deity: 'shiva',
    sanskrit: 'ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय माऽमृतात्॥',
    meaning: 'हम त्रिनेत्रधारी भगवान शिव की आराधना करते हैं...'
  };

  // Call the actual function in mantra_engine.js:
  window.readMantraItemDirect(mockMantra);

  assert(window.AiBhaktiPlayer.currentContent !== null, 'Mantra: currentContent is loaded via readMantraItemDirect');
  assert(window.AiBhaktiPlayer.currentContent.id === mockMantra.id, 'Mantra: Content ID matches');
  assert(window.AiBhaktiPlayer.currentContent.type === 'mantra', 'Mantra: Content Type is mantra');
  assert(window.AiBhaktiPlayer.currentContent.text === mockMantra.sanskrit, 'Mantra: Text is pure Sanskrit mantra');

  // Trigger play via playMantraItemDirect
  await window.playMantraItemDirect(mockMantra);
  assert(toasts.every(t => !t.includes('कोई सामग्री लोड नहीं')), 'Mantra: No "कोई सामग्री लोड नहीं है" error on play');
  assert(fetchCalls.some(f => f.url.includes('/api/ai-audio/generate')), 'Mantra: /api/ai-audio/generate was called');

  // ------------------------------------------------------------------
  // 4. Sundarkand Doha Section Simulation
  // ------------------------------------------------------------------
  console.log('\n--- 4. Testing Sundarkand Doha Section Wiring ---');
  toasts = [];
  fetchCalls = [];

  const mockDoha = {
    doha_no: 1,
    title: 'दोहा 1: मंगलाचरण व हनुमान जी का लंका प्रस्थान',
    shloka: 'शान्तं शाश्वतमप्रमेयमनघं मोक्षप्रदं शान्तिदं...',
    chaupais: ['जामवंत के बचन सुहाए। सुनि हनुमंत हृदय अति भाए॥', 'तब लगि मोहि परिखेहु तुम्ह भाई। सहि दुखु कंद मूल फल खाई॥'],
    chhand: 'जय राम सोभा धाम जगपति जन मनोरथ दायका...',
    doha: 'प्रबिसि नगर कीजे सब काजा। हृदयं राखि कोसलपुर राजा॥',
    meaning: 'हे भाई! जब तक मैं सीताजी को देखकर लौट न आऊं...'
  };

  // Call openSundarkandDohaReader from sundarkand_engine.js
  window.openSundarkandDohaReader(mockDoha);

  assert(window.AiBhaktiPlayer.currentContent !== null, 'Sundarkand: currentContent is loaded via openSundarkandDohaReader');
  assert(window.AiBhaktiPlayer.currentContent.id === 'sundarkand-doha-1', 'Sundarkand: Content ID is formatted correctly');
  assert(window.AiBhaktiPlayer.currentContent.type === 'sundarkand', 'Sundarkand: Content Type is sundarkand');
  assert(window.AiBhaktiPlayer.currentContent.text.includes(mockDoha.doha), 'Sundarkand: Recitation includes Doha verse');
  assert(window.AiBhaktiPlayer.currentContent.text.includes('शान्तं शाश्वत'), 'Sundarkand: Recitation includes Shloka');

  // Trigger play via playSundarkandDoha
  await window.playSundarkandDoha(mockDoha);
  assert(toasts.every(t => !t.includes('कोई सामग्री लोड नहीं')), 'Sundarkand: No "कोई सामग्री लोड नहीं है" error on play');
  assert(fetchCalls.some(f => f.url.includes('/api/ai-audio/generate')), 'Sundarkand: /api/ai-audio/generate was called');

  // ------------------------------------------------------------------
  // 5. Fallback autoDetectCurrentContent Test
  // ------------------------------------------------------------------
  console.log('\n--- 5. Testing autoDetectCurrentContent Fallback ---');
  toasts = [];
  window.AiBhaktiPlayer.currentContent = null;
  // If user opens a reader modal that sets innerHTML but somehow currentContent is null:
  elements['aarti-reader-title'] = { innerText: 'श्री सत्यनारायण जी की आरती' };
  elements['aarti-reader-body'] = { innerText: 'जय लक्ष्मीरमणा, श्री जय लक्ष्मीरमणा। सत्यनारायण स्वामी जन पातक हरणा॥' };

  const detected = window.AiBhaktiPlayer.autoDetectCurrentContent();
  assert(detected !== null, 'Fallback: autoDetectCurrentContent detected active reader content');
  assert(detected.title === 'श्री सत्यनारायण जी की आरती', 'Fallback: Detected title matches modal');
  assert(detected.type === 'aarti', 'Fallback: Detected type matches aarti');

  console.log('\n======================================================');
  console.log(`TEST SUMMARY: ${passCount} PASSED, ${failCount} FAILED`);
  console.log('======================================================\n');

  if (failCount > 0) {
    process.exit(1);
  } else {
    console.log('ALL SECTION INTEGRATIONS VERIFIED 100% SUCCESSFUL!');
  }
}

runTests().catch(err => {
  console.error('Unhandled error during simulation:', err);
  process.exit(1);
});
