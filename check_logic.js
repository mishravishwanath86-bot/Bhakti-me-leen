const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('let audioPlayer = new Audio();');
const e = code.indexOf('initCalendar()'); // Next init block
if(s > -1 && e > -1) {
  console.log(code.substring(s, e));
} else {
  console.log("Could not find audio logic block");
}
