const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const m1 = code.match(/'7-25':'जन्माष्टमी/g);
const m2 = code.match(/'8-4':'जन्माष्टमी/g);
const m3 = code.match(/2026-08-15.*जन्माष्टमी/g);
const m4 = code.match(/2026-09-04.*जन्माष्टमी/g);

console.log("7-25 present: ", !!m1);
console.log("8-4 present: ", !!m2);
console.log("08-15 present: ", !!m3);
console.log("09-04 present: ", !!m4);
