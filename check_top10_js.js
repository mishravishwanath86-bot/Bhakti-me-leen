const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('TOP_10_FESTIVALS');
if (s !== -1) {
  console.log(code.substring(s, s + 1200));
}
