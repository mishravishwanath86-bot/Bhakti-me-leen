const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const m = css.match(/\.vrat-icon-wrapper\s*\{[^}]+\}/g);
const m2 = css.match(/\.vrat-icon-img\s*\{[^}]+\}/g);

console.log("WRAPPER:\n", m ? m.join('\n') : "not found");
console.log("IMG:\n", m2 ? m2.join('\n') : "not found");
