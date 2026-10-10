const fs = require('fs');
let sw = fs.readFileSync('service-worker.js', 'utf8');

// Increment cache version
let v = parseInt(sw.match(/bhakti-cache-v(\d+)/)[1]);
sw = sw.replace(`bhakti-cache-v${v}`, `bhakti-cache-v${v+1}`);

const ts = new Date().getTime();
sw = sw.replace(
  "const ASSETS_TO_CACHE = [",
  `const ASSETS_TO_CACHE = [
  '/?v=${ts}',
  '/index.html?v=${ts}',
  '/styles.css?v=${ts}',
  '/app.js?v=${ts}',`
);

fs.writeFileSync('service-worker.js', sw, 'utf8');
console.log(`Updated Service Worker to v${v+1} with busted cache URLs`);
