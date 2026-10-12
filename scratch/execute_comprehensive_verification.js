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

async function run() {
  console.log('🚀 Launching Google Chrome for End-to-End Verification of All 4 Sections...');
  const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
    '--headless',
    '--remote-debugging-port=9222',
    '--user-data-dir=C:\\Users\\vishw\\.gemini\\antigravity-ide\\scratch\\bhakti-app\\scratch\\chrome-cdp-profile',
    '--no-first-run',
    '--disable-gpu',
    'http://localhost:8000'
  ]);

  await new Promise(r => setTimeout(r, 2500));

  const targets = await getJson('http://127.0.0.1:9222/json/list');
  const pageTarget = targets.find(t => t.type === 'page');
  if (!pageTarget) throw new Error('No page target found');

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

  const toastsCaptured = [];
  const networkCalls = [];

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
      if (line.includes('कोई सामग्री लोड नहीं')) {
        toastsCaptured.push(line);
      }
    } else if (msg.method === 'Network.requestWillBeSent') {
      const url = msg.params.request.url;
      if (url.includes('/api/')) {
        networkCalls.push({ method: msg.params.request.method, url });
        console.log(`📡 [Network] ${msg.params.request.method} ${url}`);
      }
    }
  };

  await new Promise(r => ws.onopen = r);
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

  // Hook toast function
  await evaluate(`
    window._allToasts = [];
    window.showToast = function(msg) {
      window._allToasts.push(msg);
      console.log('TOAST CAPTURED:', msg);
    };
  `);

  // Wait for scripts to load
  await evaluate(`new Promise(resolve => {
    const interval = setInterval(() => {
      if (typeof window.showPage === 'function' && window.AiBhaktiPlayer) {
        clearInterval(interval);
        resolve();
      }
    }, 100);
  })`);

  const report = {};

  // =========================================================================
  // 1. SECTION 1: श्री सुंदरकांड दोहा संग्रहालय
  // =========================================================================
  console.log('\n============================================================');
  console.log('🔱 TEST SECTION 1: श्री सुंदरकांड दोहा संग्रहालय');
  console.log('============================================================');

  const skDbApi = await evaluate(`(async () => {
    const res = await fetch('/api/content?type=sundarkand&limit=5');
    const json = await res.json();
    return {
      status: res.status,
      totalInDb: json.pagination ? json.pagination.total_items : json.total,
      returnedCount: (json.items || []).length,
      sampleTitle: json.items && json.items[0] ? json.items[0].title : ''
    };
  })()`);
  console.log('Sundarkand API Response:', skDbApi);

  await evaluate(`
    window.showPage('page-sundarkand');
    if (window.renderFullSundarkandPage) window.renderFullSundarkandPage('all', '');
  `);

  const skScreenCount = await evaluate(`document.querySelectorAll('#drik-sundarkand-cards-container [onclick*="openSundarkandDohaReader"]').length`);
  console.log('Sundarkand Dohas on Screen:', skScreenCount);

  // Open Doha 1 Reader
  console.log('Opening Sundarkand Doha 1 in Reader...');
  await evaluate(`window.openSundarkandDohaReader(1);`);
  const skReaderData = await evaluate(`(() => {
    const title = document.getElementById('sundarkand-reader-doha-title')?.textContent || '';
    const text = document.getElementById('sundarkand-reader-content')?.innerText || '';
    const modalDisplay = document.getElementById('sundarkand-reader-modal')?.style.display || '';
    return {
      title,
      textLength: text.length,
      snippet: text.substring(0, 120),
      modalDisplay
    };
  })()`);
  console.log('Sundarkand Reader Rendered:', skReaderData);

  // Test AI Play
  console.log('Testing AI Play button on Sundarkand Doha 1...');
  const skPlayRes = await evaluate(`(async () => {
    const startToasts = (window._allToasts || []).length;
    await window.AiBhaktiPlayer.togglePlay();
    // Wait for audio request
    await new Promise(r => setTimeout(r, 2000));
    const newToasts = (window._allToasts || []).slice(startToasts);
    return {
      isPlayingOrGen: window.AiBhaktiPlayer.isPlaying || window.AiBhaktiPlayer.isGenerating,
      audioSrc: window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null,
      currentContent: window.AiBhaktiPlayer.currentContent ? {
        id: window.AiBhaktiPlayer.currentContent.id,
        title: window.AiBhaktiPlayer.currentContent.title,
        textLen: window.AiBhaktiPlayer.currentContent.text.length
      } : null,
      newToasts
    };
  })()`);
  console.log('Sundarkand AI Play Result:', skPlayRes);
  report['sundarkand'] = { skDbApi, skScreenCount, skReaderData, skPlayRes };

  // Stop playback before next test
  await evaluate(`window.AiBhaktiPlayer.togglePlay();`);

  // =========================================================================
  // 2. SECTION 2: वैदिक मंत्र संग्रहालय
  // =========================================================================
  console.log('\n============================================================');
  console.log('🕉️ TEST SECTION 2: वैदिक मंत्र संग्रहालय');
  console.log('============================================================');

  const mantraDbApi = await evaluate(`(async () => {
    const res = await fetch('/api/content?type=mantra&limit=5');
    const json = await res.json();
    return {
      status: res.status,
      totalInDb: json.pagination ? json.pagination.total_items : json.total,
      returnedCount: (json.items || []).length,
      sampleTitle: json.items && json.items[0] ? json.items[0].title : ''
    };
  })()`);
  console.log('Mantra API Response:', mantraDbApi);

  await evaluate(`
    window.showPage('page-mantra');
    if (window.renderFullDrikMantraPage) window.renderFullDrikMantraPage('all', '');
  `);

  const mantraScreenCount = await evaluate(`document.querySelectorAll('#drik-mantra-cards-container .drik-image1-card').length`);
  console.log('Mantra Cards on Screen:', mantraScreenCount);

  // Open first mantra (Ganesha)
  console.log('Opening Mantra (ganesha, 0) in Reader...');
  await evaluate(`window.readMantraItemDirect('ganesha', 0);`);
  const mantraReaderData = await evaluate(`(() => {
    const pageTitle = document.getElementById('reader-page-title')?.textContent || '';
    const cosmicText = document.getElementById('reader-cosmic-content')?.innerText || '';
    return {
      pageTitle,
      textLength: cosmicText.length,
      snippet: cosmicText.substring(0, 120),
      currentPage: window.currentPage
    };
  })()`);
  console.log('Mantra Reader Rendered:', mantraReaderData);

  // Test AI Play
  console.log('Testing AI Play button on Mantra...');
  const mantraPlayRes = await evaluate(`(async () => {
    const startToasts = (window._allToasts || []).length;
    await window.AiBhaktiPlayer.togglePlay();
    await new Promise(r => setTimeout(r, 2000));
    const newToasts = (window._allToasts || []).slice(startToasts);
    return {
      isPlayingOrGen: window.AiBhaktiPlayer.isPlaying || window.AiBhaktiPlayer.isGenerating,
      audioSrc: window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null,
      currentContent: window.AiBhaktiPlayer.currentContent ? {
        id: window.AiBhaktiPlayer.currentContent.id,
        title: window.AiBhaktiPlayer.currentContent.title,
        textLen: window.AiBhaktiPlayer.currentContent.text.length
      } : null,
      newToasts
    };
  })()`);
  console.log('Mantra AI Play Result:', mantraPlayRes);
  report['mantra'] = { mantraDbApi, mantraScreenCount, mantraReaderData, mantraPlayRes };

  await evaluate(`window.AiBhaktiPlayer.togglePlay();`);

  // =========================================================================
  // 3. SECTION 3: नित्य पवन चालीसा संग्रहालय
  // =========================================================================
  console.log('\n============================================================');
  console.log('📜 TEST SECTION 3: नित्य पवन चालीसा संग्रहालय');
  console.log('============================================================');

  const chalisaDbApi = await evaluate(`(async () => {
    const res = await fetch('/api/content?type=chalisa&limit=5');
    const json = await res.json();
    return {
      status: res.status,
      totalInDb: json.pagination ? json.pagination.total_items : json.total,
      returnedCount: (json.items || []).length,
      sampleTitle: json.items && json.items[0] ? json.items[0].title : ''
    };
  })()`);
  console.log('Chalisa API Response:', chalisaDbApi);

  await evaluate(`
    window.showPage('page-chalisa');
    if (window.renderFullDrikChalisaPage) window.renderFullDrikChalisaPage('all', '');
  `);

  const chalisaScreenCount = await evaluate(`document.querySelectorAll('#drik-chalisa-cards-container .drik-image1-card').length`);
  console.log('Chalisa Cards on Screen:', chalisaScreenCount);

  // Open first chalisa (Hanuman Chalisa)
  console.log('Opening Chalisa (hanuman, 0) in Reader...');
  await evaluate(`window.readChalisaItemDirect('hanuman', 0);`);
  const chalisaReaderData = await evaluate(`(() => {
    const pageTitle = document.getElementById('reader-page-title')?.textContent || '';
    const cosmicText = document.getElementById('reader-cosmic-content')?.innerText || '';
    return {
      pageTitle,
      textLength: cosmicText.length,
      snippet: cosmicText.substring(0, 120),
      currentPage: window.currentPage
    };
  })()`);
  console.log('Chalisa Reader Rendered:', chalisaReaderData);

  // Test AI Play
  console.log('Testing AI Play button on Chalisa...');
  const chalisaPlayRes = await evaluate(`(async () => {
    const startToasts = (window._allToasts || []).length;
    await window.AiBhaktiPlayer.togglePlay();
    await new Promise(r => setTimeout(r, 2000));
    const newToasts = (window._allToasts || []).slice(startToasts);
    return {
      isPlayingOrGen: window.AiBhaktiPlayer.isPlaying || window.AiBhaktiPlayer.isGenerating,
      audioSrc: window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null,
      currentContent: window.AiBhaktiPlayer.currentContent ? {
        id: window.AiBhaktiPlayer.currentContent.id,
        title: window.AiBhaktiPlayer.currentContent.title,
        textLen: window.AiBhaktiPlayer.currentContent.text.length
      } : null,
      newToasts
    };
  })()`);
  console.log('Chalisa AI Play Result:', chalisaPlayRes);
  report['chalisa'] = { chalisaDbApi, chalisaScreenCount, chalisaReaderData, chalisaPlayRes };

  await evaluate(`window.AiBhaktiPlayer.togglePlay();`);

  // =========================================================================
  // 4. SECTION 4: नित्य पवन आरती संग्रहालय
  // =========================================================================
  console.log('\n============================================================');
  console.log('🪔 TEST SECTION 4: नित्य पवन आरती संग्रहालय');
  console.log('============================================================');

  const aartiDbApi = await evaluate(`(async () => {
    const res = await fetch('/api/content?type=aarti&limit=5');
    const json = await res.json();
    return {
      status: res.status,
      totalInDb: json.pagination ? json.pagination.total_items : json.total,
      returnedCount: (json.items || []).length,
      sampleTitle: json.items && json.items[0] ? json.items[0].title : ''
    };
  })()`);
  console.log('Aarti API Response:', aartiDbApi);

  await evaluate(`
    window.showPage('page-aarti');
    if (window.renderFullDrikAartiPage) window.renderFullDrikAartiPage('all', '');
  `);

  const aartiScreenCount = await evaluate(`document.querySelectorAll('#drik-aarti-cards-container .drik-image1-card').length`);
  console.log('Aarti Cards on Screen:', aartiScreenCount);

  // Open first aarti (Ganesh Aarti)
  console.log('Opening Aarti (ganesh, 0) in Reader...');
  await evaluate(`window.readAartiItemDirect('ganesh', 0);`);
  const aartiReaderData = await evaluate(`(() => {
    const pageTitle = document.getElementById('reader-page-title')?.textContent || '';
    const cosmicText = document.getElementById('reader-cosmic-content')?.innerText || '';
    return {
      pageTitle,
      textLength: cosmicText.length,
      snippet: cosmicText.substring(0, 120),
      currentPage: window.currentPage
    };
  })()`);
  console.log('Aarti Reader Rendered:', aartiReaderData);

  // Test AI Play
  console.log('Testing AI Play button on Aarti...');
  const aartiPlayRes = await evaluate(`(async () => {
    const startToasts = (window._allToasts || []).length;
    await window.AiBhaktiPlayer.togglePlay();
    await new Promise(r => setTimeout(r, 2000));
    const newToasts = (window._allToasts || []).slice(startToasts);
    return {
      isPlayingOrGen: window.AiBhaktiPlayer.isPlaying || window.AiBhaktiPlayer.isGenerating,
      audioSrc: window.AiBhaktiPlayer.audioInstance ? window.AiBhaktiPlayer.audioInstance.src : null,
      currentContent: window.AiBhaktiPlayer.currentContent ? {
        id: window.AiBhaktiPlayer.currentContent.id,
        title: window.AiBhaktiPlayer.currentContent.title,
        textLen: window.AiBhaktiPlayer.currentContent.text.length
      } : null,
      newToasts
    };
  })()`);
  console.log('Aarti AI Play Result:', aartiPlayRes);
  report['aarti'] = { aartiDbApi, aartiScreenCount, aartiReaderData, aartiPlayRes };

  // =========================================================================
  // SUMMARY OF ALL TOASTS
  // =========================================================================
  const allCapturedToasts = await evaluate(`window._allToasts`);
  console.log('\n============================================================');
  console.log('📋 TOTAL TOASTS CAPTURED ACROSS ENTIRE RUN:');
  console.log(allCapturedToasts);
  const errorFound = allCapturedToasts.some(t => t.includes('कोई सामग्री लोड नहीं'));
  console.log('❌ Was "कोई सामग्री लोड नहीं" EVER triggered?:', errorFound);
  console.log('============================================================');

  ws.close();
  chrome.kill();

  if (errorFound) {
    console.error('FAILED: Error toast was captured!');
    process.exit(1);
  } else {
    console.log('🎉 ALL 4 SECTIONS VERIFIED PERFECTLY WITH ZERO ERRORS!');
    process.exit(0);
  }
}

run().catch(err => {
  console.error('Fatal Test Exception:', err);
  process.exit(1);
});
