const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('function getGlobalAudio()');
if (s !== -1) {
  console.log(code.substring(s, s + 2000));
}
