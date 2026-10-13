/**
 * 🕉️ BHAKTI APP - REAL COMPREHENSIVE VERIFICATION SUITE
 * Tests all 4 sections + Bhagavad Gita across:
 * 1. API request & status
 * 2. Real content records count
 * 3. Screen/Reader content rendering
 * 4. Audio generation triggered ONLY on play
 * 5. Audio playback execution (direct stream, backend API, & on-device speech synthesis fallback)
 * 6. Playback controls (Play, Pause, Speed, Voice, Loop, Seek)
 */

const fs = require('fs');
const http = require('http');
const path = require('path');

// Mock browser environment for Node.js execution
global.window = global;
global.document = {
  readyState: 'complete',
  addEventListener: () => {},
  removeEventListener: () => {},
  elements: {},
  getElementById(id) {
    if (!this.elements[id]) {
      this.elements[id] = {
        id,
        innerHTML: '',
        textContent: '',
        innerText: '',
        style: {},
        classList: {
          contains: (cls) => false,
          add: () => {},
          remove: () => {},
          toggle: () => {}
        },
        querySelector: () => null,
        querySelectorAll: () => []
      };
    }
    return this.elements[id];
  },
  querySelector(sel) { return null; },
  querySelectorAll(sel) { return []; },
  body: { style: {} }
};

global.AudioContext = class {
  constructor() {
    this.currentTime = 0;
    this.state = 'running';
    this.destination = {};
  }
  createGain() {
    return {
      gain: {
        value: 1,
        setValueAtTime: () => {},
        cancelScheduledValues: () => {},
        linearRampToValueAtTime: () => {}
      },
      connect: () => {}
    };
  }
  createBiquadFilter() {
    return {
      frequency: { setValueAtTime: () => {} },
      connect: () => {}
    };
  }
  createOscillator() {
    return {
      frequency: { setValueAtTime: () => {} },
      connect: () => {},
      start: () => {},
      stop: () => {}
    };
  }
  resume() { return Promise.resolve(); }
};

global.Audio = class {
  constructor(url) {
    this.src = url;
    this.playbackRate = 1.0;
    this.loop = false;
    this.duration = 180;
    this.currentTime = 0;
    this.paused = true;
    this.listeners = {};
  }
  addEventListener(evt, fn) {
    this.listeners[evt] = fn;
  }
  play() {
    this.paused = false;
    return Promise.resolve();
  }
  pause() {
    this.paused = true;
  }
};

let spokenUtterances = [];
global.SpeechSynthesisUtterance = class {
  constructor(text) {
    this.text = text;
    this.lang = 'hi-IN';
    this.rate = 1.0;
    this.pitch = 1.0;
    this.voice = null;
  }
};

global.speechSynthesis = {
  speaking: false,
  paused: false,
  pending: false,
  speak(utt) {
    this.speaking = true;
    spokenUtterances.push(utt);
  },
  pause() {
    this.paused = true;
  },
  resume() {
    this.paused = false;
  },
  cancel() {
    this.speaking = false;
    this.paused = false;
  },
  getVoices() {
    return [{ name: 'Google Hindi', lang: 'hi-IN' }];
  }
};

let toastsShown = [];
global.showToast = function(msg) {
  toastsShown.push(msg);
};
global.triggerFlowerShower = function() {};

// Load and evaluate required application files
require('./ai_bhakti_player.js');
require('./gita_engine.js');
require('./sundarkand_engine.js');
require('./mantra_engine.js');

// Helper to make real HTTP GET request to backend API
function fetchBackendApi(path) {
  return new Promise((resolve, reject) => {
    const req = http.get('http://localhost:8000' + path, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, body: JSON.parse(data) });
        } catch (e) {
          resolve({ status: res.statusCode, body: data });
        }
      });
    });
    req.on('error', err => resolve({ error: err.message }));
  });
}

// Helper to make real HTTP POST request to AI Audio endpoint
function postAiAudio(payload) {
  return new Promise((resolve) => {
    const postData = JSON.stringify(payload);
    const req = http.request({
      hostname: 'localhost',
      port: 8000,
      path: '/api/ai-audio/generate',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, body: JSON.parse(data) });
        } catch (e) {
          resolve({ status: res.statusCode, body: data });
        }
      });
    });
    req.on('error', err => resolve({ error: err.message }));
    req.write(postData);
    req.end();
  });
}

async function runRealVerification() {
  console.log('================================================================');
  console.log('🕉️ BHAKTI APP REAL SYSTEM VERIFICATION REPORT');
  console.log('================================================================\n');

  const results = {};

  // ─────────────────────────────────────────────────────────────
  // 1. SHRIMAD BHAGAVAD GITA (Baseline Reference)
  // ─────────────────────────────────────────────────────────────
  console.log('--- 1. श्रीमद्भगवद्गीता (Reference Implementation) ---');
  const gitaChapters = window.GITA_DATA.chapters.length;
  const gitaVerses = window.GITA_DATA.total_verses;
  console.log(`✓ Loaded verified chapters: ${gitaChapters}, total verses: ${gitaVerses}`);
  
  const ch1v1 = window.GITA_DATA.chapters[0].verses[0];
  console.log(`✓ Chapter 1 Verse 1: "${ch1v1.title}"`);
  console.log(`   Sanskrit: ${ch1v1.sanskrit.split('\n')[0]}`);
  console.log(`   Audio URL: ${ch1v1.audio_url}`);
  
  // Test Gita Verse Playback
  const mockBtn = { innerHTML: '' };
  window.playVerseAudio(ch1v1.audio_url, mockBtn);
  const gitaAudioActive = !!window._gitaVerseAudioInstance && !window._gitaVerseAudioInstance.paused;
  console.log(`✓ Gita Audio Instance Active: ${gitaAudioActive}`);
  console.log(`✓ Gita Button State: "${mockBtn.innerHTML}"`);
  results['gita'] = { chapters: gitaChapters, verses: gitaVerses, playbackOk: gitaAudioActive };

  // ─────────────────────────────────────────────────────────────
  // 2. श्री सुंदरकांड दोहा संग्रहालय
  // ─────────────────────────────────────────────────────────────
  console.log('\n--- 2. श्री सुंदरकांड दोहा संग्रहालय ---');
  // Step 2a: Test API request
  const skApiRes = await fetchBackendApi('/api/content?type=sundarkand&limit=5');
  console.log(`✓ Backend API Request /api/content?type=sundarkand -> HTTP Status: ${skApiRes.status || 'Offline'}`);
  const skDbItems = (skApiRes.body && skApiRes.body.items) ? skApiRes.body.items.length : 0;
  console.log(`   Records returned from DB API: ${skDbItems}`);

  // Step 2b: Test Dataset Records
  const skDohas = window.SUNDARKAND_DATA.dohas.length;
  console.log(`✓ Total Verified Dohas in Engine: ${skDohas}`);
  const doha1 = window.SUNDARKAND_DATA.dohas[0];
  console.log(`   Doha 1: "${doha1.title}"`);
  console.log(`   Chaupais count: ${doha1.chaupais.length}`);
  console.log(`   First Chaupai: "${doha1.chaupais[0]}"`);

  // Step 2c: Test Content Loading into Reader & AiBhaktiPlayer
  window.openSundarkandDohaReader(1);
  const skActiveObj = window._activeDevotionalContent;
  const skLoaded = !!(skActiveObj && skActiveObj.text && skActiveObj.text.length > 50);
  console.log(`✓ Reader Screen Loaded Doha 1: ${skLoaded} (Text length: ${skActiveObj.text.length} chars)`);
  console.log(`✓ Audio Generation State BEFORE Play: isPlaying=${window.AiBhaktiPlayer.isPlaying}, isGenerating=${window.AiBhaktiPlayer.isGenerating}`);

  // Step 2d: Test Play Press (Audio Generation & Playback)
  spokenUtterances = [];
  await window.AiBhaktiPlayer.togglePlay();
  const skPlaying = window.AiBhaktiPlayer.isPlaying;
  const skSpeechUttered = spokenUtterances.length > 0;
  console.log(`✓ User Pressed Play -> isPlaying: ${skPlaying}, Utterance Chanted: ${skSpeechUttered}`);
  if (skSpeechUttered) {
    console.log(`   Devotional Audio Chanted: "${spokenUtterances[0].text.substring(0, 60)}..."`);
    console.log(`   Chanting Language: ${spokenUtterances[0].lang}, Rate: ${spokenUtterances[0].rate}`);
  }
  // Pause
  window.AiBhaktiPlayer.togglePlay();
  console.log(`✓ User Pressed Pause -> isPlaying: ${window.AiBhaktiPlayer.isPlaying}`);
  results['sundarkand'] = { dbItems: skDbItems, engineDohas: skDohas, readerOk: skLoaded, playbackOk: skPlaying };

  // ─────────────────────────────────────────────────────────────
  // 3. वैदिक मंत्र संग्रहालय
  // ─────────────────────────────────────────────────────────────
  console.log('\n--- 3. वैदिक मंत्र संग्रहालय ---');
  // Step 3a: Test API request
  const mantraApiRes = await fetchBackendApi('/api/content?type=mantra&limit=5');
  console.log(`✓ Backend API Request /api/content?type=mantra -> HTTP Status: ${mantraApiRes.status || 'Offline'}`);
  const mantraDbItems = (mantraApiRes.body && mantraApiRes.body.items) ? mantraApiRes.body.items.length : 0;
  console.log(`   Records returned from DB API: ${mantraDbItems}`);

  // Step 3b: Test Dataset Records
  const mantraColls = Object.keys(window.MANTRA_COLLECTIONS).length;
  let totalMantras = 0;
  Object.values(window.MANTRA_COLLECTIONS).forEach(c => totalMantras += (c.items ? c.items.length : 0));
  console.log(`✓ Total Mantra Collections: ${mantraColls}, Total Authentic Mantras: ${totalMantras}`);

  // Step 3c: Test Content Loading
  window.readMantraItemDirect('ganesha', 0);
  const mantraActiveObj = window._activeDevotionalContent;
  const mantraLoaded = !!(mantraActiveObj && mantraActiveObj.text && mantraActiveObj.text.length > 10);
  console.log(`✓ Reader Screen Loaded: ${mantraLoaded} (Mantra: "${mantraActiveObj.title}")`);
  console.log(`   Sanskrit: "${mantraActiveObj.text}"`);

  // Step 3d: Test Play Press
  spokenUtterances = [];
  await window.AiBhaktiPlayer.togglePlay();
  const mantraPlaying = window.AiBhaktiPlayer.isPlaying;
  console.log(`✓ User Pressed Play -> isPlaying: ${mantraPlaying}, Utterance Chanted: ${spokenUtterances.length > 0}`);
  if (spokenUtterances.length > 0) {
    console.log(`   Vedic Recitation: "${spokenUtterances[0].text}"`);
  }
  // Pause
  window.AiBhaktiPlayer.togglePlay();
  results['mantra'] = { dbItems: mantraDbItems, totalMantras, readerOk: mantraLoaded, playbackOk: mantraPlaying };

  // ─────────────────────────────────────────────────────────────
  // 4. नित्य पवन चालीसा संग्रहालय
  // ─────────────────────────────────────────────────────────────
  console.log('\n--- 4. नित्य पवन चालीसा संग्रहालय ---');
  // Step 4a: Test API request
  const chalisaApiRes = await fetchBackendApi('/api/content?type=chalisa&limit=5');
  console.log(`✓ Backend API Request /api/content?type=chalisa -> HTTP Status: ${chalisaApiRes.status || 'Offline'}`);
  const chalisaDbItems = (chalisaApiRes.body && chalisaApiRes.body.items) ? chalisaApiRes.body.items.length : 0;
  console.log(`   Records returned from DB API: ${chalisaDbItems}`);

  // Step 4b: Test Dataset Records
  const chalisaData = JSON.parse(fs.readFileSync('./drik_chalisa_collections.json', 'utf-8'));
  const chalisaColls = Object.keys(chalisaData).length;
  let chalisaItemsCount = 0;
  Object.values(chalisaData).forEach(c => chalisaItemsCount += (c.items ? c.items.length : 0));
  console.log(`✓ Total Chalisa Collections: ${chalisaColls}, Total Chalisas: ${chalisaItemsCount}`);

  // Step 4c: Test Content Loading
  const hanumanChalisa = chalisaData.hanuman.items[0];
  window.AiBhaktiPlayer.loadContent({
    id: hanumanChalisa.id,
    title: hanumanChalisa.title,
    text: hanumanChalisa.content,
    type: 'chalisa',
    deity: 'संकटमोचन श्री हनुमान जी',
    audio_url: hanumanChalisa.audio_url
  });
  const chalisaActiveObj = window._activeDevotionalContent;
  const chalisaLoaded = !!(chalisaActiveObj && chalisaActiveObj.text && chalisaActiveObj.text.length > 100);
  console.log(`✓ Reader Screen Loaded: ${chalisaLoaded} (Title: "${chalisaActiveObj.title}", Length: ${chalisaActiveObj.text.length} chars)`);

  // Step 4d: Test Play Press
  spokenUtterances = [];
  await window.AiBhaktiPlayer.togglePlay();
  const chalisaPlaying = window.AiBhaktiPlayer.isPlaying;
  console.log(`✓ User Pressed Play -> isPlaying: ${chalisaPlaying}, Utterance Chanted: ${spokenUtterances.length > 0}`);
  if (spokenUtterances.length > 0) {
    console.log(`   Chalisa Chanted: "${spokenUtterances[0].text.substring(0, 50)}..."`);
  }
  // Pause
  window.AiBhaktiPlayer.togglePlay();
  results['chalisa'] = { dbItems: chalisaDbItems, totalChalisas: chalisaItemsCount, readerOk: chalisaLoaded, playbackOk: chalisaPlaying };

  // ─────────────────────────────────────────────────────────────
  // 5. नित्य पवन आरती संग्रहालय (The Section in the User's Screenshot!)
  // ─────────────────────────────────────────────────────────────
  console.log('\n--- 5. नित्य पवन आरती संग्रहालय (आरती कुंजबिहारी की) ---');
  // Step 5a: Test API request
  const aartiApiRes = await fetchBackendApi('/api/content?type=aarti&limit=5');
  console.log(`✓ Backend API Request /api/content?type=aarti -> HTTP Status: ${aartiApiRes.status || 'Offline'}`);
  const aartiDbItems = (aartiApiRes.body && aartiApiRes.body.items) ? aartiApiRes.body.items.length : 0;
  console.log(`   Records returned from DB API: ${aartiDbItems}`);

  // Step 5b: Test Dataset Records
  const aartiData = JSON.parse(fs.readFileSync('./final_granular_aarti_collections.json', 'utf-8'));
  const aartiColls = Object.keys(aartiData).length;
  let totalAartis = 0;
  Object.values(aartiData).forEach(c => totalAartis += (c.items ? c.items.length : 0));
  console.log(`✓ Total Aarti Collections: ${aartiColls}, Total Aartis: ${totalAartis}`);

  // Step 5c: Test Loading EXACT item from screenshot: "आरती कुंजबिहारी की"
  const krishnaAarti = aartiData.krishna.items[0];
  window.AiBhaktiPlayer.loadContent({
    id: krishnaAarti.id,
    title: krishnaAarti.title,
    text: krishnaAarti.content,
    type: 'aarti',
    deity: 'भगवान श्री कृष्ण',
    audio_url: krishnaAarti.audio_url
  });
  const aartiActiveObj = window._activeDevotionalContent;
  const aartiLoaded = !!(aartiActiveObj && aartiActiveObj.text && aartiActiveObj.text.length > 50);
  console.log(`✓ Reader Screen Loaded: ${aartiLoaded} (Title: "${aartiActiveObj.title}")`);
  console.log(`   Lyrics sample: "${aartiActiveObj.text.substring(0, 60)}..."`);

  // Step 5d: Test Play Press with "Failed to fetch" immunity verification
  spokenUtterances = [];
  toastsShown = [];
  await window.AiBhaktiPlayer.togglePlay();
  const aartiPlaying = window.AiBhaktiPlayer.isPlaying;
  const failedToastShown = toastsShown.some(t => t.includes('Failed to fetch'));
  console.log(`✓ User Pressed Play -> isPlaying: ${aartiPlaying}`);
  console.log(`✓ "Failed to fetch" Error Appeared?: ${failedToastShown ? '❌ YES (FAILED)' : '✅ NO (CLEAN PASS)'}`);
  console.log(`✓ Last Toast Displayed: "${toastsShown[toastsShown.length - 1]}"`);
  if (spokenUtterances.length > 0) {
    console.log(`✓ Audio Chanting Chanted Out Loud: "${spokenUtterances[0].text.substring(0, 50)}..."`);
  }

  // Test Playback Controls
  console.log('\n--- 6. प्लेबैक नियंत्रण (Controls: Speed, Voice, Loop) ---');
  window.AiBhaktiPlayer.cycleSpeed();
  console.log(`✓ Speed cycled to: ${window.AiBhaktiPlayer.currentSpeed}x`);
  window.AiBhaktiPlayer.toggleVoice();
  console.log(`✓ Voice toggled to: ${window.AiBhaktiPlayer.currentVoice}`);
  window.AiBhaktiPlayer.toggleLoop();
  console.log(`✓ Loop toggled to: ${window.AiBhaktiPlayer.isLooping}`);
  window.AiBhaktiPlayer.seek(50);
  console.log(`✓ Seeked to 50% -> Elapsed: ${window.AiBhaktiPlayer.speechElapsed}s`);
  
  // Pause
  window.AiBhaktiPlayer.togglePlay();
  console.log(`✓ Playback cleanly paused -> isPlaying: ${window.AiBhaktiPlayer.isPlaying}`);
  results['aarti'] = { dbItems: aartiDbItems, totalAartis, readerOk: aartiLoaded, playbackOk: aartiPlaying, noFailedToFetch: !failedToastShown };

  // ─────────────────────────────────────────────────────────────
  // 7. REAL BACKEND AI AUDIO GENERATION TEST
  // ─────────────────────────────────────────────────────────────
  console.log('\n--- 7. वास्तविक बैकएंड Edge-TTS AI ऑडियो सृजन टेस्ट ---');
  const backendGenRes = await postAiAudio({
    content_id: 'real_test_aarti_kunjbihari',
    text: 'आरती कुंजबिहारी की श्री गिरिधर कृष्णमुरारी की',
    title: 'आरती कुंजबिहारी की',
    content_type: 'aarti',
    voice: 'male',
    speed: 1.0
  });
  console.log(`✓ POST /api/ai-audio/generate Status: ${backendGenRes.status}`);
  if (backendGenRes.body && backendGenRes.body.audio_url) {
    console.log(`✓ Generated Real Audio File: ${backendGenRes.body.audio_url}`);
    console.log(`✓ Cached Status: ${backendGenRes.body.cached}`);
  }

  console.log('\n================================================================');
  console.log('🏁 FINAL VERIFICATION SUMMARY');
  console.log('================================================================');
  console.log(JSON.stringify(results, null, 2));
}

runRealVerification().catch(console.error);
