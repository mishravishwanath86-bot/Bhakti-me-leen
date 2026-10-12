/**
 * Comprehensive End-to-End Verification of all 4 Devotional Sections:
 * 1. श्री सुंदरकांड दोहा संग्रहालय
 * 2. वैदिक मंत्र संग्रहालय
 * 3. नित्य पवन चालीसा संग्रहालय
 * 4. नित्य पवन आरती संग्रहालय
 */

const fs = require('fs');
const http = require('http');

// Setup minimal browser DOM environment
const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id: id,
      style: {},
      classList: {
        _classes: new Set(),
        add: function(c) { this._classes.add(c); },
        remove: function(c) { this._classes.delete(c); },
        toggle: function(c, force) {
          if (force === undefined) {
            if (this._classes.has(c)) this._classes.delete(c);
            else this._classes.add(c);
          } else if (force) this._classes.add(c);
          else this._classes.delete(c);
        },
        contains: function(c) { return this._classes.has(c); }
      },
      innerHTML: '',
      innerText: '',
      textContent: '',
      setAttribute: () => {},
      getAttribute: () => null,
      querySelector: function(sel) {
        if (sel === 'h1' && this.innerHTML.includes('<h1')) {
          const match = this.innerHTML.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
          return match ? { textContent: match[1].replace(/<[^>]+>/g, '').trim() } : null;
        }
        return null;
      },
      querySelectorAll: () => [],
      appendChild: () => {},
      removeChild: () => {},
      addEventListener: () => {},
      removeEventListener: () => {}
    };
  }
  return elements[id];
}

global.window = global;
global.window.window = global;
global.CustomEvent = class {
  constructor(name, opts) { this.name = name; this.detail = opts && opts.detail; }
};
global.document = {
  documentElement: getEl('html'),
  getElementById: (id) => getEl(id),
  createElement: (tag) => getEl(tag),
  querySelector: (sel) => {
    if (sel.startsWith('#')) return getEl(sel.slice(1));
    return getEl('sel_' + sel);
  },
  querySelectorAll: () => [],
  addEventListener: () => {},
  removeEventListener: () => {},
  dispatchEvent: () => {},
  body: getEl('body')
};
global.navigator = { vibrate: () => {} };
global.localStorage = {
  getItem: () => null,
  setItem: () => {},
  removeItem: () => {}
};
global.window.addEventListener = () => {};
global.window.removeEventListener = () => {};
global.window.scrollTo = () => {};
global.window.location = { pathname: '/', search: '', hash: '' };

const toastsShown = [];
global.window.showToast = function(msg) {
  toastsShown.push(msg);
  console.log(`   [TOAST NOTIFICATION]: "${msg}"`);
};

global.Audio = class {
  constructor(src) {
    this.src = src || '';
    this.currentTime = 0;
    this.duration = 100;
    this.ended = false;
    this.paused = true;
  }
  play() {
    this.paused = false;
    return Promise.resolve();
  }
  pause() {
    this.paused = true;
  }
  addEventListener() {}
  removeEventListener() {}
};

// Real HTTP Fetch implementation pointing to localhost:8000
global.fetch = function(url, options = {}) {
  const fullUrl = url.startsWith('http') ? url : `http://localhost:8000${url}`;
  const u = new URL(fullUrl);
  return new Promise((resolve, reject) => {
    const postData = options.body || '';
    const req = http.request({
      hostname: u.hostname,
      port: u.port || 8000,
      path: u.pathname + u.search,
      method: options.method || 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData),
        ...(options.headers || {})
      }
    }, (res) => {
      let body = '';
      res.setEncoding('utf8');
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        resolve({
          status: res.statusCode,
          ok: res.statusCode >= 200 && res.statusCode < 300,
          json: async () => JSON.parse(body),
          text: async () => body
        });
      });
    });
    req.on('error', reject);
    if (postData) req.write(postData);
    req.end();
  });
};

console.log("======================================================================");
console.log("🚀 STARTING RUNTIME TEST FOR ALL 4 DEVOTIONAL SECTIONS");
console.log("======================================================================\n");

// 1. Load app.js
require('../app.js');
// 2. Load ai_bhakti_player.js
require('../ai_bhakti_player.js');
// 3. Load engines
require('../mantra_engine.js');
require('../sundarkand_engine.js');
require('../gita_engine.js');

async function runTests() {
  const results = {};

  // =========================================================================
  // TEST 1: श्री सुंदरकांड दोहा संग्रहालय (Sundarkand Doha Sangrah)
  // =========================================================================
  console.log("--------------------------------------------------");
  console.log("1️⃣ परीक्षण: श्री सुंदरकांड दोहा संग्रहालय");
  console.log("--------------------------------------------------");
  toastsShown.length = 0;

  // Open Doha 1
  console.log("-> Calling window.openSundarkandDohaReader(1)...");
  window.openSundarkandDohaReader(1);

  const skTitle = getEl('sundarkand-reader-doha-title').textContent;
  const skContent = getEl('sundarkand-reader-content').innerHTML;
  console.log(`   शीर्षक: ${skTitle}`);
  console.log(`   सामग्री लंबाई (DOM HTML): ${skContent.length} chars`);
  console.log(`   AiBhaktiPlayer.currentContent:`, window.AiBhaktiPlayer.currentContent ? {
    id: window.AiBhaktiPlayer.currentContent.id,
    title: window.AiBhaktiPlayer.currentContent.title,
    textLen: window.AiBhaktiPlayer.currentContent.text.length,
    type: window.AiBhaktiPlayer.currentContent.type
  } : 'NULL');

  // Trigger Play
  console.log("-> User taps 'AI दिव्य पाठ सुनें' (AiBhaktiPlayer.togglePlay)...");
  await window.AiBhaktiPlayer.togglePlay();
  await new Promise(r => setTimeout(r, 600));

  const skAudioUrl = window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null;
  const skHasError = toastsShown.some(t => t.includes('कोई सामग्री लोड नहीं'));
  console.log(`   Audio Instance Source: ${skAudioUrl}`);
  console.log(`   क्या error toast आया?: ${skHasError ? 'हाँ (FAILED)' : 'नहीं (PASSED)'}`);

  results['sundarkand'] = {
    title: skTitle,
    textLength: skContent.length,
    hasError: skHasError,
    audioUrl: skAudioUrl,
    status: !skHasError && skAudioUrl ? 'PASS' : 'FAIL'
  };

  // =========================================================================
  // TEST 2: वैदिक मंत्र संग्रहालय (Vedic Mantra Sangrah)
  // =========================================================================
  console.log("\n--------------------------------------------------");
  console.log("2️⃣ परीक्षण: वैदिक मंत्र संग्रहालय");
  console.log("--------------------------------------------------");
  toastsShown.length = 0;

  // Open Ganesh Mantra (ganesh, idx 0)
  console.log("-> Calling window.readMantraItemDirect('ganesh', 0)...");
  window.readMantraItemDirect('ganesh', 0);

  const mContent = getEl('reader-cosmic-content').innerHTML;
  console.log(`   सामग्री लंबाई (DOM HTML): ${mContent.length} chars`);
  console.log(`   AiBhaktiPlayer.currentContent:`, window.AiBhaktiPlayer.currentContent ? {
    id: window.AiBhaktiPlayer.currentContent.id,
    title: window.AiBhaktiPlayer.currentContent.title,
    textLen: window.AiBhaktiPlayer.currentContent.text.length,
    type: window.AiBhaktiPlayer.currentContent.type
  } : 'NULL');

  // Trigger Play
  console.log("-> User taps 'AI दिव्य पाठ / गायन सुनें' (AiBhaktiPlayer.togglePlay)...");
  await window.AiBhaktiPlayer.togglePlay();
  await new Promise(r => setTimeout(r, 600));

  const mAudioUrl = window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null;
  const mHasError = toastsShown.some(t => t.includes('कोई सामग्री लोड नहीं'));
  console.log(`   Audio Instance Source: ${mAudioUrl}`);
  console.log(`   क्या error toast आया?: ${mHasError ? 'हाँ (FAILED)' : 'नहीं (PASSED)'}`);

  results['mantra'] = {
    title: window.AiBhaktiPlayer.currentContent ? window.AiBhaktiPlayer.currentContent.title : '',
    textLength: mContent.length,
    hasError: mHasError,
    audioUrl: mAudioUrl,
    status: !mHasError && mAudioUrl ? 'PASS' : 'FAIL'
  };

  // =========================================================================
  // TEST 3: नित्य पवन चालीसा संग्रहालय (Chalisa Sangrah)
  // =========================================================================
  console.log("\n--------------------------------------------------");
  console.log("3️⃣ परीक्षण: नित्य पवन चालीसा संग्रहालय");
  console.log("--------------------------------------------------");
  toastsShown.length = 0;

  // Open Hanuman Chalisa (hanuman, idx 0)
  console.log("-> Calling window.readChalisaItemDirect('hanuman', 0)...");
  window.readChalisaItemDirect('hanuman', 0);

  const cContent = getEl('reader-cosmic-content').innerHTML;
  console.log(`   सामग्री लंबाई (DOM HTML): ${cContent.length} chars`);
  console.log(`   AiBhaktiPlayer.currentContent:`, window.AiBhaktiPlayer.currentContent ? {
    id: window.AiBhaktiPlayer.currentContent.id,
    title: window.AiBhaktiPlayer.currentContent.title,
    textLen: window.AiBhaktiPlayer.currentContent.text.length,
    type: window.AiBhaktiPlayer.currentContent.type
  } : 'NULL');

  // Trigger Play
  console.log("-> User taps 'AI दिव्य पाठ / गायन सुनें' (AiBhaktiPlayer.togglePlay)...");
  await window.AiBhaktiPlayer.togglePlay();
  await new Promise(r => setTimeout(r, 600));

  const cAudioUrl = window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null;
  const cHasError = toastsShown.some(t => t.includes('कोई सामग्री लोड नहीं'));
  console.log(`   Audio Instance Source: ${cAudioUrl}`);
  console.log(`   क्या error toast आया?: ${cHasError ? 'हाँ (FAILED)' : 'नहीं (PASSED)'}`);

  results['chalisa'] = {
    title: window.AiBhaktiPlayer.currentContent ? window.AiBhaktiPlayer.currentContent.title : '',
    textLength: cContent.length,
    hasError: cHasError,
    audioUrl: cAudioUrl,
    status: !cHasError && cAudioUrl ? 'PASS' : 'FAIL'
  };

  // =========================================================================
  // TEST 4: नित्य पवन आरती संग्रहालय (Aarti Jugal Kishore - User's exact screenshot!)
  // =========================================================================
  console.log("\n--------------------------------------------------");
  console.log("4️⃣ परीक्षण: नित्य पवन आरती संग्रहालय (Aarti Jugal Kishore - drik_krishna_3)");
  console.log("--------------------------------------------------");
  toastsShown.length = 0;

  // Open Aarti Jugal Kishore (krishna, idx 2)
  console.log("-> Calling window.readAartiItemDirect('krishna', 2)...");
  window.readAartiItemDirect('krishna', 2);

  const aContent = getEl('reader-cosmic-content').innerHTML;
  console.log(`   सामग्री लंबाई (DOM HTML): ${aContent.length} chars`);
  console.log(`   AiBhaktiPlayer.currentContent:`, window.AiBhaktiPlayer.currentContent ? {
    id: window.AiBhaktiPlayer.currentContent.id,
    title: window.AiBhaktiPlayer.currentContent.title,
    textLen: window.AiBhaktiPlayer.currentContent.text.length,
    type: window.AiBhaktiPlayer.currentContent.type
  } : 'NULL');

  // Trigger Play
  console.log("-> User taps 'AI दिव्य पाठ / गायन सुनें' (AiBhaktiPlayer.togglePlay)...");
  await window.AiBhaktiPlayer.togglePlay();
  await new Promise(r => setTimeout(r, 600));

  const aAudioUrl = window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null;
  const aHasError = toastsShown.some(t => t.includes('कोई सामग्री लोड नहीं'));
  console.log(`   Audio Instance Source: ${aAudioUrl}`);
  console.log(`   क्या error toast आया?: ${aHasError ? 'हाँ (FAILED)' : 'नहीं (PASSED)'}`);

  results['aarti'] = {
    title: window.AiBhaktiPlayer.currentContent ? window.AiBhaktiPlayer.currentContent.title : '',
    textLength: aContent.length,
    hasError: aHasError,
    audioUrl: aAudioUrl,
    status: !aHasError && aAudioUrl ? 'PASS' : 'FAIL'
  };

  // =========================================================================
  // TEST 5: Fallback Resilience Test (Direct Play without explicit loadContent)
  // =========================================================================
  console.log("\n--------------------------------------------------");
  console.log("5️⃣ परीक्षण: Resilient Auto-Detection Fallback (यदि loadContent मिस हो जाए)");
  console.log("--------------------------------------------------");
  toastsShown.length = 0;
  // Intentionally clear currentContent
  window.AiBhaktiPlayer.currentContent = null;
  console.log("-> Manually set AiBhaktiPlayer.currentContent = null while reader-cosmic-content has Aarti text...");
  await window.AiBhaktiPlayer.togglePlay();
  await new Promise(r => setTimeout(r, 600));

  const fHasError = toastsShown.some(t => t.includes('कोई सामग्री लोड नहीं'));
  const fAudioUrl = window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null;
  console.log(`   क्या fallback autoDetect काम किया?: ${!fHasError && fAudioUrl ? 'हाँ (PASSED)' : 'नहीं (FAILED)'}`);

  // Summary
  console.log("\n======================================================================");
  console.log("📊 FINAL TEST MATRIX");
  console.log("======================================================================");
  console.table(results);

  process.exit(0);
}

runTests().catch(err => {
  console.error("Test execution failed:", err);
  process.exit(1);
});
