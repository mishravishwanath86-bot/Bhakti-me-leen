const fs = require('fs');

// Cache bust index.html
let html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
html = html.replace(/styles\.css(\?v=\d+)?/g, `styles.css?v=${time}`);
html = html.replace(/app\.js(\?v=\d+)?/g, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Cache busted index.html JS/CSS to ' + time);
