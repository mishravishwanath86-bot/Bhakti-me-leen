const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

console.log("=== Checking index.html sections ===");
const pageMatches = html.match(/<section id="([^"]+)"/g);
console.log("Pages found:", pageMatches);

console.log("\n=== Checking page-home content ===");
const s = html.indexOf('id="page-home"');
const e = html.indexOf('</section>', s);
console.log("page-home length:", e - s);
console.log(html.substring(s, Math.min(s + 1500, e)));
