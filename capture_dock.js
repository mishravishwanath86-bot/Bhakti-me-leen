const { spawn } = require('child_process');
const fs = require('fs');

async function capture() {
  const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const edge = spawn(edgePath, [
    '--headless=new',
    '--remote-debugging-port=9226',
    '--window-size=412,860',
    'http://localhost:8000/index.html'
  ]);

  try {
    await new Promise(r => setTimeout(r, 2500));
    const res = await fetch('http://localhost:9226/json');
    const targets = await res.json();
    const page = targets.find(t => t.type === 'page');
    if (!page) {
      console.error('No page target found');
      return;
    }

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

    console.log('Dismissing overlays and showing home...');
    await send('Runtime.evaluate', {
      expression: `(() => {
        ['app-intro-video-overlay', 'splash-screen', 'onboarding-overlay', 'auth-modal'].forEach(id => {
          const el = document.getElementById(id);
          if (el) el.remove();
        });
        document.body.style.overflow = 'auto';
        if (typeof showPage === 'function') {
          showPage('home-page');
        }
        if (typeof updateCurvedNavCutout === 'function') {
          updateCurvedNavCutout(0);
        }
      })()`
    });

    await new Promise(r => setTimeout(r, 1500));

    // Full screenshot
    const fullShot = await send('Page.captureScreenshot', { format: 'png' });
    const fullBuf = Buffer.from(fullShot.result.data, 'base64');
    fs.writeFileSync('C:\\Users\\vishw\\.gemini\\antigravity-ide\\brain\\3b88eaf3-1c95-41f0-845b-726a512c06a7\\full_screen.png', fullBuf);
    console.log('Saved full_screen.png');

    // Bottom dock screenshot
    const navShot = await send('Page.captureScreenshot', {
      format: 'png',
      clip: { x: 0, y: 730, width: 412, height: 130, scale: 1 }
    });
    const navBuf = Buffer.from(navShot.result.data, 'base64');
    fs.writeFileSync('C:\\Users\\vishw\\.gemini\\antigravity-ide\\brain\\3b88eaf3-1c95-41f0-845b-726a512c06a7\\nav_dock_verified.png', navBuf);
    console.log('Saved nav_dock_verified.png');

    ws.close();
  } catch (err) {
    console.error('Error during capture:', err);
  } finally {
    edge.kill();
  }
}

capture();
