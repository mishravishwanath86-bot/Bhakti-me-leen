const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
// Update styles.css version too
html = html.replace(/styles\.css(\?v=\d+)?/, `styles.css?v=${time}`);
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Cache busted: ' + time);
