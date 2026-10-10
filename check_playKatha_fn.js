const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('function playKatha');
if (s !== -1) {
  console.log(code.substring(s - 100, s + 1000));
}
