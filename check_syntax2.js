const fs = require('fs');
try {
  let code = fs.readFileSync('app.js', 'utf8');
  // Check if there are any syntax errors
  new Function(code);
  console.log("No syntax errors in app.js");
} catch(e) {
  console.log("Error:", e);
}
