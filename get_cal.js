const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Find the CAL_FESTIVALS object
const match = code.match(/const CAL_FESTIVALS = \{([\s\S]*?)\};/);
if(match) {
   console.log("CAL_FESTIVALS:\n" + match[1].trim());
} else {
   console.log("CAL_FESTIVALS not found, let's search just '7-25'");
   const lines = code.split('\n');
   lines.forEach((l, i) => {
      if(l.includes("'7-25'")) {
         console.log(`Line ${i+1}: ${l}`);
      }
   });
}
