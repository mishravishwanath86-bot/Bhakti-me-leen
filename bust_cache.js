const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
// Add a cache buster comment at the top
code = '// v' + Date.now() + '\n' + code;
fs.writeFileSync('app.js', code, 'utf8');

// Also update version in index.html  
let html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Cache busted! New version: ' + time);
