const fs = require('fs');
let sw = fs.readFileSync('service-worker.js', 'utf8');

let v = parseInt(sw.match(/bhakti-cache-v(\d+)/)[1]);
sw = sw.replace(`bhakti-cache-v${v}`, `bhakti-cache-v${v+1}`);

fs.writeFileSync('service-worker.js', sw, 'utf8');
console.log(`Updated Service Worker to v${v+1}`);
