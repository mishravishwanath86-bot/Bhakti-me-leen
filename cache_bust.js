const fs = require('fs');
let code = fs.readFileSync('index.html', 'utf8');

// Increment a version parameter to app.js and styles.css to bust the cache
const time = new Date().getTime();
code = code.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
code = code.replace(/styles\.css(\?v=\d+)?/, `styles.css?v=${time}`);

fs.writeFileSync('index.html', code, 'utf8');
console.log('Cache busted!');
