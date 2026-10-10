const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('const KATHA_PLAYLIST =');
if (s !== -1) {
  console.log(code.substring(s, s + 1500));
}
