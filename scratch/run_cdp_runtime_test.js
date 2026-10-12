const { spawn } = require('child_process');
const http = require('http');

async function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); } catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

async function main() {
  console.log('🚀 Launching Google Chrome in headless mode with CDP...');
  const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
    '--headless',
    '--remote-debugging-port=9222',
    '--user-data-dir=C:\\Users\\vishw\\.gemini\\antigravity-ide\\scratch\\bhakti-app\\scratch\\chrome-cdp-profile',
    '--no-first-run',
    '--disable-gpu',
    'http://localhost:8000'
  ]);

  chrome.on('error', err => console.error('Chrome spawn error:', err));
  
  // Wait 2.5 seconds for Chrome to start
  await new Promise(r => setTimeout(r, 2500));

  console.log('Fetching targets from http://127.0.0.1:9222/json/list...');
  const targets = await getJson('http://127.0.0.1:9222/json/list');
  console.log(`Found ${targets.length} targets.`);
  const pageTarget = targets.find(t => t.type === 'page');
  if (!pageTarget) {
    throw new Error('No page target found');
  }

  console.log('Connecting to page WebSocket:', pageTarget.webSocketDebuggerUrl);
  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);

  let msgId = 1;
  const pending = new Map();

  function sendCommand(method, params = {}) {
    const id = msgId++;
    return new Promise((resolve, reject) => {
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  const consoleLogs = [];
  const networkRequests = [];
  const toastsDetected = [];

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(msg.error);
      else resolve(msg.result);
      return;
    }

    if (msg.method === 'Runtime.consoleAPICalled') {
      const args = (msg.params.args || []).map(a => a.value !== undefined ? a.value : (a.description || JSON.stringify(a)));
      const line = `[Console ${msg.params.type}] ` + args.join(' ');
      consoleLogs.push(line);
      console.log(line);
      if (line.includes('कोई सामग्री लोड नहीं')) {
        toastsDetected.push(line);
      }
    } else if (msg.method === 'Runtime.exceptionThrown') {
      const desc = msg.params.exceptionDetails.exception ? msg.params.exceptionDetails.exception.description : msg.params.exceptionDetails.text;
      const line = `[Exception] ` + desc;
      consoleLogs.push(line);
      console.error(line);
    } else if (msg.method === 'Network.requestWillBeSent') {
      const url = msg.params.request.url;
      if (url.includes('/api/')) {
        networkRequests.push({ url, method: msg.params.request.method });
        console.log(`[Network API Request]: ${msg.params.request.method} ${url}`);
      }
    }
  };

  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });

  console.log('Connected to CDP! Enabling domains...');
  await sendCommand('Runtime.enable');
  await sendCommand('Page.enable');
  await sendCommand('Network.enable');

  async function evaluate(expression) {
    const res = await sendCommand('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      throw new Error(res.exceptionDetails.exception ? res.exceptionDetails.exception.description : res.exceptionDetails.text);
    }
    return res.result ? res.result.value : undefined;
  }

  // Hook showToast inside the browser to track toasts directly
  await evaluate(`
    window._capturedToasts = [];
    const origShowToast = window.showToast;
    window.showToast = function(msg) {
      window._capturedToasts.push(msg);
      console.log('CAPTURED_TOAST: ' + msg);
      if (typeof origShowToast === 'function') origShowToast.apply(this, arguments);
    };
  `);

  console.log('--- Initial Page State in Chrome ---');
  const title = await evaluate(`document.title`);
  console.log('Page Title:', title);

  const checks = await evaluate(`({
    hasAppJs: typeof window.showPage === 'function',
    hasAiPlayer: typeof window.AiBhaktiPlayer !== 'undefined',
    hasAartiCollections: typeof window.AARTI_COLLECTIONS !== 'undefined',
    hasMantraCollections: typeof window.MANTRA_COLLECTIONS !== 'undefined',
    hasSundarkandData: typeof window.SUNDARKAND_DATA !== 'undefined',
    hasGitaData: typeof window.GITA_DATA !== 'undefined'
  })`);
  console.log('Engine Availability in Browser:', checks);

  // SECTION TEST MATRIX
  const report = {};

  // =========================================================================
  // 1. TEST SUNDARKAND
  // =========================================================================
  console.log('\n======================================================');
  console.log('TEST 1: श्री सुंदरकांड दोहा संग्रहालय');
  console.log('======================================================');
  await evaluate(`window._capturedToasts = [];`);
  
  // Open Doha 1
  const skOpenResult = await evaluate(`
    try {
      window.openSundarkandDohaReader(1);
      const modal = document.getElementById('sundarkand-reader-modal');
      const content = document.getElementById('sundarkand-reader-content');
      ({
        success: true,
        modalDisplay: modal ? window.getComputedStyle(modal).display : 'null',
        contentLength: content ? content.innerText.trim().length : 0,
        contentPreview: content ? content.innerText.trim().slice(0, 100) : '',
        aiContent: window.AiBhaktiPlayer && window.AiBhaktiPlayer.currentContent ? {
          title: window.AiBhaktiPlayer.currentContent.title,
          textLen: (window.AiBhaktiPlayer.currentContent.text || '').length,
          type: window.AiBhaktiPlayer.currentContent.type
        } : null
      });
    } catch(e) {
      ({ success: false, error: e.message });
    }
  `);
  console.log('Sundarkand Open Result:', skOpenResult);

  // Trigger Play
  console.log('Triggering AI Play in Sundarkand...');
  await evaluate(`
    if (window.AiBhaktiPlayer) {
      window.AiBhaktiPlayer.togglePlay();
    }
  `);
  await new Promise(r => setTimeout(r, 1200));

  const skPlayResult = await evaluate(`({
    toasts: window._capturedToasts,
    isPlaying: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.isPlaying : false,
    audioSrc: window.AiBhaktiPlayer && window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null
  })`);
  console.log('Sundarkand Play Result:', skPlayResult);
  report['sundarkand'] = { open: skOpenResult, play: skPlayResult };

  // =========================================================================
  // 2. TEST MANTRA
  // =========================================================================
  console.log('\n======================================================');
  console.log('TEST 2: वैदिक मंत्र संग्रहालय');
  console.log('======================================================');
  await evaluate(`window._capturedToasts = [];`);

  const mOpenResult = await evaluate(`
    try {
      window.readMantraItemDirect('ganesha', 0);
      const content = document.getElementById('reader-cosmic-content');
      ({
        success: true,
        currentPage: window.currentPage,
        contentLength: content ? content.innerText.trim().length : 0,
        contentPreview: content ? content.innerText.trim().slice(0, 100) : '',
        aiContent: window.AiBhaktiPlayer && window.AiBhaktiPlayer.currentContent ? {
          title: window.AiBhaktiPlayer.currentContent.title,
          textLen: (window.AiBhaktiPlayer.currentContent.text || '').length,
          type: window.AiBhaktiPlayer.currentContent.type
        } : null
      });
    } catch(e) {
      ({ success: false, error: e.message });
    }
  `);
  console.log('Mantra Open Result:', mOpenResult);

  console.log('Triggering AI Play in Mantra...');
  await evaluate(`
    if (window.AiBhaktiPlayer) {
      window.AiBhaktiPlayer.togglePlay();
    }
  `);
  await new Promise(r => setTimeout(r, 1200));

  const mPlayResult = await evaluate(`({
    toasts: window._capturedToasts,
    isPlaying: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.isPlaying : false,
    audioSrc: window.AiBhaktiPlayer && window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null
  })`);
  console.log('Mantra Play Result:', mPlayResult);
  report['mantra'] = { open: mOpenResult, play: mPlayResult };

  // =========================================================================
  // 3. TEST CHALISA
  // =========================================================================
  console.log('\n======================================================');
  console.log('TEST 3: नित्य पवन चालीसा संग्रहालय');
  console.log('======================================================');
  await evaluate(`window._capturedToasts = [];`);

  const cOpenResult = await evaluate(`
    try {
      window.readChalisaItemDirect('hanuman', 0);
      const content = document.getElementById('reader-cosmic-content');
      ({
        success: true,
        currentPage: window.currentPage,
        contentLength: content ? content.innerText.trim().length : 0,
        contentPreview: content ? content.innerText.trim().slice(0, 100) : '',
        aiContent: window.AiBhaktiPlayer && window.AiBhaktiPlayer.currentContent ? {
          title: window.AiBhaktiPlayer.currentContent.title,
          textLen: (window.AiBhaktiPlayer.currentContent.text || '').length,
          type: window.AiBhaktiPlayer.currentContent.type
        } : null
      });
    } catch(e) {
      ({ success: false, error: e.message });
    }
  `);
  console.log('Chalisa Open Result:', cOpenResult);

  console.log('Triggering AI Play in Chalisa...');
  await evaluate(`
    if (window.AiBhaktiPlayer) {
      window.AiBhaktiPlayer.togglePlay();
    }
  `);
  await new Promise(r => setTimeout(r, 1200));

  const cPlayResult = await evaluate(`({
    toasts: window._capturedToasts,
    isPlaying: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.isPlaying : false,
    audioSrc: window.AiBhaktiPlayer && window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null
  })`);
  console.log('Chalisa Play Result:', cPlayResult);
  report['chalisa'] = { open: cOpenResult, play: cPlayResult };

  // =========================================================================
  // 4. TEST AARTI (Jugal Kishore - exact user screenshot)
  // =========================================================================
  console.log('\n======================================================');
  console.log('TEST 4: नित्य पवन आरती संग्रहालय (आरती जुगल किशोर)');
  console.log('======================================================');
  await evaluate(`window._capturedToasts = [];`);

  const aOpenResult = await evaluate(`
    try {
      window.readAartiItemDirect('krishna', 2);
      const content = document.getElementById('reader-cosmic-content');
      ({
        success: true,
        currentPage: window.currentPage,
        contentLength: content ? content.innerText.trim().length : 0,
        contentPreview: content ? content.innerText.trim().slice(0, 100) : '',
        aiContent: window.AiBhaktiPlayer && window.AiBhaktiPlayer.currentContent ? {
          title: window.AiBhaktiPlayer.currentContent.title,
          textLen: (window.AiBhaktiPlayer.currentContent.text || '').length,
          type: window.AiBhaktiPlayer.currentContent.type
        } : null
      });
    } catch(e) {
      ({ success: false, error: e.message });
    }
  `);
  console.log('Aarti Open Result:', aOpenResult);

  console.log('Triggering AI Play in Aarti...');
  await evaluate(`
    if (window.AiBhaktiPlayer) {
      window.AiBhaktiPlayer.togglePlay();
    }
  `);
  await new Promise(r => setTimeout(r, 1200));

  const aPlayResult = await evaluate(`({
    toasts: window._capturedToasts,
    isPlaying: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.isPlaying : false,
    audioSrc: window.AiBhaktiPlayer && window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null
  })`);
  console.log('Aarti Play Result:', aPlayResult);
  report['aarti'] = { open: aOpenResult, play: aPlayResult };

  console.log('\n======================================================');
  console.log('TEST REPORT SUMMARY');
  console.log('======================================================');
  console.log(JSON.stringify(report, null, 2));

  ws.close();
  chrome.kill();
  process.exit(0);
}

main().catch(err => {
  console.error('Fatal error in CDP script:', err);
  process.exit(1);
});
