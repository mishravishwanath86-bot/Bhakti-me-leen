const fs = require('fs');

// ---- Fix app.js ----
let code = fs.readFileSync('app.js', 'utf8');

// Fix events array: change Raksha Bandhan from Aug 28 to Aug 21
code = code.replace("date:'2026-08-28', name:", "date:'2026-08-21', name:");

// Fix Ganesha Chaturthi in CAL_FESTIVALS: '8-7' is Sep 7 (2024 data), should be '8-14' for 2026
code = code.replace("'8-7':'", "'8-14':'");

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed app.js dates!');

// ---- Fix index.html Rakhi page ----
let html = fs.readFileSync('index.html', 'utf8');

// Fix all August 28 references in Rakhi page to August 21
// The Rakhi page section
const rakhiStart = html.indexOf('id="page-rakhi"');
const rakhiEnd = html.indexOf('</section>', rakhiStart) + 10;
let rakhiSection = html.substring(rakhiStart, rakhiEnd);

rakhiSection = rakhiSection
  .replace(/August 28/g, 'August 21')
  .replace(/28.*August.*2026/g, '21 August 2026')
  .replace(/Aug 28/g, 'Aug 21');

html = html.substring(0, rakhiStart) + rakhiSection + html.substring(rakhiEnd);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed Rakhi page date August 28 → August 21!');

// Verify fix
const check = fs.readFileSync('index.html', 'utf8');
const rStart = check.indexOf('id="page-rakhi"');
const rEnd = check.indexOf('</section>', rStart);
const rSection = check.substring(rStart, rEnd);
const remaining28 = (rSection.match(/August 28/g) || []).length;
const count21 = (rSection.match(/August 21/g) || []).length;
console.log(`August 28 remaining in Rakhi: ${remaining28}`);
console.log(`August 21 in Rakhi: ${count21}`);
