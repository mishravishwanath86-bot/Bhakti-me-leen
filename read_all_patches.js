const fs = require('fs');

console.log("=== patch_top10_links.js ===");
console.log(fs.readFileSync('patch_top10_links.js', 'utf8'));

console.log("=== add_vrats.js ===");
console.log(fs.readFileSync('add_vrats.js', 'utf8'));

console.log("=== add_vrats_7.js ===");
console.log(fs.readFileSync('add_vrats_7.js', 'utf8'));
