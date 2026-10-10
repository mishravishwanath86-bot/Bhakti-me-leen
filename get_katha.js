const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('function initKatha(){');
const e = code.indexOf('function initCalendar(){');

if(s > -1 && e > -1) {
  let kathaFunc = code.substring(s, e);
  fs.writeFileSync('katha_old.txt', kathaFunc, 'utf8');
  console.log("Saved old katha logic to katha_old.txt");
}
