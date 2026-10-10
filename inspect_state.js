const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const pages = html.match(/id="page-[^"]+"/g);
console.log("Pages in index.html:", pages);

const app = fs.readFileSync('app.js', 'utf8');
const funcs = app.match(/function\s+[a-zA-Z0-9_]+\s*\(/g);
console.log("Functions in app.js:", funcs);
