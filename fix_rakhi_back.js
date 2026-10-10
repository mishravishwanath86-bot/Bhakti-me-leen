const fs = require('fs');

// Fix app.js
let code = fs.readFileSync('app.js', 'utf8');

// Fix events array: restore Aug 21 → Aug 28
code = code.replace("date:'2026-08-21', name:", "date:'2026-08-28', name:");

// Fix CAL_FESTIVALS: '7-21' (Aug 21) → '7-28' (Aug 28)
code = code.replace("'7-21':", "'7-28':");

fs.writeFileSync('app.js', code, 'utf8');

// Fix index.html Rakhi page
let html = fs.readFileSync('index.html', 'utf8');
const rakhiStart = html.indexOf('id="page-rakhi"');
const rakhiEnd = html.indexOf('</section>', rakhiStart) + 10;
let rakhiSection = html.substring(rakhiStart, rakhiEnd);
rakhiSection = rakhiSection.replace(/August 21/g, 'August 28');
html = html.substring(0, rakhiStart) + rakhiSection + html.substring(rakhiEnd);
fs.writeFileSync('index.html', html, 'utf8');

console.log('✅ Raksha Bandhan fixed back to August 28, 2026!');

// Verify
const check = fs.readFileSync('app.js', 'utf8');
const has28 = check.includes("date:'2026-08-28'");
const has21 = check.includes("date:'2026-08-21'");
console.log(`Events: Aug 28 = ${has28}, Aug 21 = ${has21}`);
