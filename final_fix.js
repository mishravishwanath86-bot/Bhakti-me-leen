const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// The broken initKatha starts around line 6386 (where function initKatha() is)
let s = code.indexOf('function initKatha(){');
let e = code.indexOf('//   ENGLISH CALENDAR');
let realEnd = code.lastIndexOf('// ═', e);

// Read clean_app.js and extract part2 manually (we can just split by 'const part2 = `')
let cleanApp = fs.readFileSync('clean_app.js', 'utf8');
let parts = cleanApp.split('const part2 = `');
let part2_raw = parts[1].split('`;\n    \n    fs.writeFileSync')[0];
// Unescape
let part2_clean = part2_raw.replace(/\\`/g, '`').replace(/\\\${/g, '${');

// Now replace the broken initKatha with part2_clean
code = code.substring(0, s) + part2_clean + '\n\n' + code.substring(realEnd);
fs.writeFileSync('app.js', code, 'utf8');
console.log("Fixed app.js");
