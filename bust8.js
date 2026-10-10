const fs = require('fs');

// Cache bust SW
let sw = fs.readFileSync('service-worker.js', 'utf8');
let v = parseInt(sw.match(/bhakti-cache-v(\d+)/)[1]);
sw = sw.replace(`bhakti-cache-v${v}`, `bhakti-cache-v${v+1}`);
fs.writeFileSync('service-worker.js', sw, 'utf8');

// Cache bust index.html
let html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
html = html.replace(/styles\.css(\?v=\d+)?/, `styles.css?v=${time}`);
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');

console.log('Cache busted SW to v' + (v+1) + ' and HTML to ' + time);
