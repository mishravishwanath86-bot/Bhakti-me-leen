const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Just remove all occurrences of tithi: '...' in the JSON arrays
code = code.replace(/tithi:\s*'(\.\.\.|)'/g, "tithi: ''");
code = code.replace(/tithi:\s*"(\.\.\.|)"/g, "tithi: ''");

// If tithi is empty, don't show the sk-tithi div at all in openVratPage
code = code.replace(
  /<div class="sk-tithi" style="font-size:0.85rem; color:#475569;">\$\{d\.tithi\}<\/div>/g,
  "${d.tithi ? `<div class='sk-tithi' style='font-size:0.85rem; color:#475569;'>${d.tithi}</div>` : ''}"
);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed dots successfully!');
