const fs = require('fs');
const ts = new Date().getTime();

let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(/styles\.css(\?v=\d+)?/, `styles.css?v=${ts}`);
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${ts}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Version: ' + ts);
