const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('const DEITIES');
console.log(code.substring(s, s + 3500));
