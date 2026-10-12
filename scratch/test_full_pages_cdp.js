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
  console.log('🚀 Spawning Chrome for Full-Page UI testing...');
  const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
    '--headless',
    '--remote-debugging-port=9222',
    '--user-data-dir=C:\\Users\\vishw\\.gemini\antigravity-ide\\scratch\\bhakti-app\\scratch\\chrome-cdp-profile',
    '--no-first-run',
    '--disable-gpu',
    'http://localhost:8000'
  ]);

  await new Promise(r => setTimeout(r, 2500));

  const targets = await getJson('http://127.0.0.1:9222/json/list');
  const pageTarget = targets.find(t => t.type === 'page');
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
      if (line.includes('कोई सामग्री लोड नहीं')) {
        toastsDetected.push(line);
      }
    }
  };

  await new Promise(r => ws.onopen = r);
  await sendCommand('Runtime.enable');
  await sendCommand('Page.enable');

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

  // Hook showToast
  await evaluate(`
    window._capturedToasts = [];
    window.showToast = function(msg) {
      window._capturedToasts.push(msg);
      console.log('TOAST: ' + msg);
    };
  `);

  // Wait until scripts are fully loaded
  console.log('Waiting for window.showPage to become available...');
  await evaluate(`new Promise(resolve => {
    const start = Date.now();
    const interval = setInterval(() => {
      if (typeof window.showPage === 'function' || Date.now() - start > 10000) {
        clearInterval(interval);
        resolve();
      }
    }, 100);
  })`);

  console.log('Testing Full Page rendering and card clicks...');

  // 1. FULL PAGE AARTI
  console.log('\n--- 1. Testing Full Page Aarti (page-aarti) ---');
  await evaluate(`
    window.showPage('page-aarti');
    if (window.renderFullDrikAartiPage) window.renderFullDrikAartiPage('all', '');
  `);
  const aartiCardsCount = await evaluate(`document.querySelectorAll('#drik-aarti-cards-container .drik-image1-card').length`);
  console.log('Rendered Aarti Cards Count in page-aarti:', aartiCardsCount);

  // Click 1st Aarti card
  console.log('Clicking Aarti card...');
  const aartiCardClick = await evaluate(`(() => {
    const firstCard = document.querySelector('#drik-aarti-cards-container .drik-image1-card');
    if (firstCard) {
      firstCard.click();
      return {
        clicked: true,
        currentPage: window.currentPage,
        readerTextLen: (document.getElementById('reader-cosmic-content') ? document.getElementById('reader-cosmic-content').innerText.length : 0),
        aiContent: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.currentContent : null
      };
    }
    return { clicked: false };
  })()`);
  console.log('Aarti Card Click Result:', aartiCardClick);

  // 2. FULL PAGE CHALISA
  console.log('\n--- 2. Testing Full Page Chalisa (page-chalisa) ---');
  await evaluate(`(() => {
    window.showPage('page-chalisa');
    if (window.renderFullDrikChalisaPage) window.renderFullDrikChalisaPage('all', '');
  })()`);
  const chalisaCardsCount = await evaluate(`document.querySelectorAll('#drik-chalisa-cards-container .drik-image1-card').length`);
  console.log('Rendered Chalisa Cards Count in page-chalisa:', chalisaCardsCount);

  console.log('Clicking Chalisa card...');
  const chalisaCardClick = await evaluate(`(() => {
    const firstCard = document.querySelector('#drik-chalisa-cards-container .drik-image1-card');
    if (firstCard) {
      firstCard.click();
      return {
        clicked: true,
        currentPage: window.currentPage,
        readerTextLen: (document.getElementById('reader-cosmic-content') ? document.getElementById('reader-cosmic-content').innerText.length : 0),
        aiContent: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.currentContent : null
      };
    }
    return { clicked: false };
  })()`);
  console.log('Chalisa Card Click Result:', chalisaCardClick);

  // 3. FULL PAGE MANTRA
  console.log('\n--- 3. Testing Full Page Mantra (page-mantra) ---');
  await evaluate(`(() => {
    window.showPage('page-mantra');
    if (window.renderFullDrikMantraPage) window.renderFullDrikMantraPage('all', '');
  })()`);
  const mantraCardsCount = await evaluate(`document.querySelectorAll('#drik-mantra-cards-container .drik-image1-card').length`);
  console.log('Rendered Mantra Cards Count in page-mantra:', mantraCardsCount);

  console.log('Clicking Mantra card...');
  const mantraCardClick = await evaluate(`(() => {
    const firstCard = document.querySelector('#drik-mantra-cards-container .drik-image1-card');
    if (firstCard) {
      firstCard.click();
      return {
        clicked: true,
        currentPage: window.currentPage,
        readerTextLen: (document.getElementById('reader-cosmic-content') ? document.getElementById('reader-cosmic-content').innerText.length : 0),
        aiContent: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.currentContent : null
      };
    }
    return { clicked: false };
  })()`);
  console.log('Mantra Card Click Result:', mantraCardClick);

  // 4. FULL PAGE SUNDARKAND
  console.log('\n--- 4. Testing Full Page Sundarkand (page-sundarkand) ---');
  await evaluate(`(() => {
    window.showPage('page-sundarkand');
    if (window.renderFullSundarkandPage) window.renderFullSundarkandPage('all', '');
  })()`);
  const skCardsCount = await evaluate(`document.querySelectorAll('#drik-sundarkand-cards-container .drik-image1-card, .sundarkand-doha-card').length`);
  console.log('Rendered Sundarkand Cards Count in page-sundarkand:', skCardsCount);

  console.log('Clicking Sundarkand card or Doha item...');
  const skCardClick = await evaluate(`(() => {
    const firstCard = document.querySelector('#drik-sundarkand-cards-container .drik-image1-card, .sundarkand-doha-card, [onclick*="openSundarkand"]');
    if (firstCard) {
      firstCard.click();
      return {
        clicked: true,
        modalDisplay: document.getElementById('sundarkand-reader-modal') ? document.getElementById('sundarkand-reader-modal').style.display : 'none',
        aiContent: window.AiBhaktiPlayer ? window.AiBhaktiPlayer.currentContent : null
      };
    }
    return { clicked: false };
  })()`);
  console.log('Sundarkand Card Click Result:', skCardClick);

  const toasts = await evaluate(`window._capturedToasts`);
  console.log('\nTotal Toasts Captured:', toasts);
  console.log('Any "कोई सामग्री लोड नहीं" errors?:', toasts.some(t => t.includes('कोई सामग्री लोड नहीं')));

  ws.close();
  chrome.kill();
  process.exit(0);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
