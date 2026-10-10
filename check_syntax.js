const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

try {
  Function(code);
  console.log("No syntax errors found by Function constructor.");
} catch(e) {
  console.log("Error:", e.message);
  // Function throws just a SyntaxError without a line number if it's generic, but let's see
}
