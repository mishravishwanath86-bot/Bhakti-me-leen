const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

// List all function definitions in app.js
const fns = code.match(/function\s+([a-zA-Z0-9_]+)\s*\(/g);
console.log("Functions in app.js:", fns);

// Search for 'chalisa' or 'mantra' or 'aarti' data in app.js
console.log("CHALISA in code:", code.includes('chalisa_') || code.includes('CHALISA'));
console.log("MANTRA in code:", code.includes('mantra_') || code.includes('MANTRA'));
console.log("AARTI in code:", code.includes('aarti_') || code.includes('AARTI'));
