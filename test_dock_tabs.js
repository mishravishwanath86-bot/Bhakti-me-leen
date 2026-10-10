const { spawn } = require('child_process');
const fs = require('fs');

async function testTabs() {
  const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const edge = spawn(edgePath, [
    '--headless=new',
    '--remote-debugging-port=9227',
    '--window-size=412,860',
    'http://localhost:8000/index.html'
  ]);

  try {
    await new Promise(r => setTimeout(r, 2500));
    const res = await fetch('http://localhost:9227/json');
    const targets = await res.json();
    const page = targets.find(t => t.type === 'page');
    const ws = new WebSocket(page.webSocketDebuggerUrl);

    let id = 1;
    const pending = new Map();
    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && pending.has(msg.id)) {
        pending.get(msg.id)(msg);
        pending.delete(msg.id);
      }
    };
    await new Promise((resolve) => ws.onopen = resolve);

    function send(method, params = {}) {
      const reqId = id++;
      return new Promise((resolve) => {
        pending.set(reqId, resolve);
        ws.send(JSON.stringify({ id: reqId, method, params }));
      });
    }

    // Dismiss overlays
    await send('Runtime.evaluate', {
      expression: `(() => {
        ['app-intro-video-overlay', 'splash-screen', 'onboarding-overlay', 'auth-modal'].forEach(id => {
          const el = document.getElementById(id);
          if (el) el.remove();
        });
        document.body.style.overflow = 'auto';
        showPage('home-page');
      })()`
    });

    await new Promise(r => setTimeout(r, 1000));

    // Get dock bounding rect
    const evalRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const el = document.getElementById('custom-curved-nav');
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return { x: r.x, y: r.y, width: r.width, height: r.height };
      })()`,
      returnByValue: true
    });

    console.log('Dock rect:', evalRes.result.value);
    const rect = evalRes.result.value;

    // Capture Tab 0 (Home)
    let shot = await send('Page.captureScreenshot', {
      format: 'png',
      clip: { x: Math.max(0, rect.x - 10), y: Math.max(0, rect.y - 30), width: rect.width + 20, height: rect.height + 40, scale: 2 }
    });
    fs.writeFileSync('C:\\Users\\vishw\\.gemini\\antigravity-ide\\brain\\3b88eaf3-1c95-41f0-845b-726a512c06a7\\dock_tab0.png', Buffer.from(shot.result.data, 'base64'));

    // Switch to Tab 2 (Jap Mala)
    await send('Runtime.evaluate', {
      expression: `showPage('jap-page')`
    });
    await new Promise(r => setTimeout(r, 600));

    shot = await send('Page.captureScreenshot', {
      format: 'png',
      clip: { x: Math.max(0, rect.x - 10), y: Math.max(0, rect.y - 30), width: rect.width + 20, height: rect.height + 40, scale: 2 }
    });
    fs.writeFileSync('C:\\Users\\vishw\\.gemini\\antigravity-ide\\brain\\3b88eaf3-1c95-41f0-845b-726a512c06a7\\dock_tab2.png', Buffer.from(shot.result.data, 'base64'));

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    edge.kill();
  }
}

testTabs();
