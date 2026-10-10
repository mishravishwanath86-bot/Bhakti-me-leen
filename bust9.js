const fs = require('fs');

// Cache bust index.html
let html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Cache busted HTML to ' + time);
