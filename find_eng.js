const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const s = code.indexOf('function initEngCalendar()');
console.log("initEngCalendar is at index:", s);
