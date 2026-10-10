const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('top10-list-container');
if (s !== -1) {
  console.log(code.substring(s - 100, s + 800));
}
