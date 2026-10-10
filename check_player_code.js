const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('function openGlassPlayer()');
if (s !== -1) {
  console.log(code.substring(s - 300, s + 1000));
}
