const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Replace \` with `
code = code.replace(/\\`/g, '`');
// Replace \${ with ${
code = code.replace(/\\\${/g, '${');

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed escaping issues in app.js');
