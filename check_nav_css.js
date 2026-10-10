const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

// Find all occurrences of .bottom-nav or .nav-item
const matches = css.match(/\.bottom-nav[\s\S]*?\}/g) || [];
console.log("=== .bottom-nav CSS rules ===");
matches.forEach(m => console.log(m));

const itemMatches = css.match(/\.nav-item[\s\S]*?\}/g) || [];
console.log("\n=== .nav-item CSS rules ===");
itemMatches.forEach(m => console.log(m));
