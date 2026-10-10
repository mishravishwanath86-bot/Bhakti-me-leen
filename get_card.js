const fs = require('fs');
let app = fs.readFileSync('app.js', 'utf8');

// Find how vrat-card is generated
const m = app.match(/<button class="vrat-card"[^>]*>([\s\S]*?)<\/button>/);
console.log(m ? m[1] : "not found");
