const { spawn } = require('child_process');
const http = require('http');

console.log('Spawning Chrome via Node child_process...');
const chrome = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless',
  '--remote-debugging-port=9222',
  '--user-data-dir=C:\\Users\\vishw\\.gemini\\antigravity-ide\\scratch\\bhakti-app\\scratch\\chrome-cdp-profile',
  '--no-first-run',
  '--disable-gpu',
  'http://localhost:8000'
]);

chrome.stdout.on('data', d => console.log('[Chrome stdout]:', d.toString()));
chrome.stderr.on('data', d => console.log('[Chrome stderr]:', d.toString()));

chrome.on('exit', code => console.log('Chrome exited with code:', code));

// Wait 2 seconds, then query /json/version
setTimeout(() => {
  http.get('http://127.0.0.1:9222/json/version', res => {
    let raw = '';
    res.on('data', c => raw += c);
    res.on('end', () => {
      console.log('SUCCESS! CDP Version response:', raw);
      chrome.kill();
      process.exit(0);
    });
  }).on('error', err => {
    console.error('Failed to connect to CDP on 9222:', err.message);
    chrome.kill();
    process.exit(1);
  });
}, 2500);
