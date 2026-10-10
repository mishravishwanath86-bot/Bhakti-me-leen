const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

// Replace the line in generic openVratPage
// <div class="sk-tithi" style="font-size:0.85rem; color:#475569;">${d.tithi}</div>
let oldLine = `<div class="sk-tithi" style="font-size:0.85rem; color:#475569;">\\${d.tithi}</div>`;
let newLine = `\\${d.tithi && d.tithi !== '...' ? \`<div class="sk-tithi" style="font-size:0.85rem; color:#475569;">\\${d.tithi}</div>\` : ''}`;

code = code.replace('<div class="sk-tithi" style="font-size:0.85rem; color:#475569;">${d.tithi}</div>', `${d.tithi && d.tithi !== '...' ? \`<div class="sk-tithi" style="font-size:0.85rem; color:#475569;">${d.tithi}</div>\` : ''}`);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed dot dot dot!');
