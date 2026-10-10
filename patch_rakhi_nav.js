const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Add page: 'page-rakhi' to Rakhi entry in TOP10_FESTIVALS
code = code.replace(
  "name: 'रक्षा बंधन (Rakhi)',",
  "name: 'रक्षा बंधन (Rakhi)', page: 'page-rakhi',"
);

fs.writeFileSync('app.js', code, 'utf8');

// Cache bust index.html
let html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated Rakhi nav + cache busted!');
