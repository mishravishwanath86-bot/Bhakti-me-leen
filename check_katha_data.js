const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('KATHA');
if (s !== -1) {
  console.log(code.substring(s, s + 1200));
} else {
  console.log('KATHA not found in app.js');
}
