const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');
console.log(lines.slice(6630, 6750).join('\n'));
