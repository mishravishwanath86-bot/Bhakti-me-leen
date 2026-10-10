const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('function initNavigation()');
const e = code.indexOf('function loadMPData(', s);
console.log(code.substring(s, e !== -1 ? e : s + 1000));
