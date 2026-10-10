const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.lastIndexOf('function initOnboarding');
console.log(code.substring(s - 200));
