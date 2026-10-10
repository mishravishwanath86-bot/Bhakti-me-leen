const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('नित्य भक्ति संग्रह');
if (s !== -1) {
  console.log(html.substring(s - 100, s + 1500));
}
