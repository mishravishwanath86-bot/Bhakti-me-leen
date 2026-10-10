const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

// Check how Chalisa / Mantra items are rendered or clicked
console.log("=== Checking chalisa / mantra in app.js ===");
const m1 = code.match(/function initDeityGrids[\s\S]*?\n\}/);
if (m1) console.log(m1[0]);

const m2 = code.match(/function buildDeityGrid[\s\S]*?\n\}/);
if (m2) console.log(m2[0]);

const m3 = code.match(/function initReader[\s\S]*?\n\}/);
if (m3) console.log(m3[0]);
