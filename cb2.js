const fs = require('fs');
let code = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
code = code.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', code, 'utf8');
