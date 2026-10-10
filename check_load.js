const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.lastIndexOf("window.addEventListener('load'");
console.log(code.substring(s));
