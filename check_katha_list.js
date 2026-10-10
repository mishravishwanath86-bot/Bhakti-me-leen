const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('katha-list');
console.log('katha-list index:', s);
if (s !== -1) {
  console.log(code.substring(Math.max(0, s - 200), s + 800));
}
