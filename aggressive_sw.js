const fs = require('fs');
let sw = fs.readFileSync('service-worker.js', 'utf8');

if(!sw.includes('self.skipWaiting()')) {
  sw = sw.replace(
    'self.addEventListener(\'install\', event => {',
    'self.addEventListener(\'install\', event => {\n  self.skipWaiting();'
  );
}

if(!sw.includes('clients.claim()')) {
  sw = sw.replace(
    'self.addEventListener(\'activate\', event => {',
    'self.addEventListener(\'activate\', event => {\n  event.waitUntil(clients.claim());'
  );
}

// Change fetch strategy to network-first for index.html or at least try network first
sw = sw.replace(
  'return cachedResponse || fetch(event.request);',
  'return fetch(event.request).catch(() => cachedResponse);'
);

fs.writeFileSync('service-worker.js', sw, 'utf8');
console.log(`Updated Service Worker logic to network-first and skipWaiting`);
