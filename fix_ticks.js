const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(/\\`/g, '`');
code = code.replace(/\\\${/g, '${');
fs.writeFileSync('app.js', code, 'utf8');
