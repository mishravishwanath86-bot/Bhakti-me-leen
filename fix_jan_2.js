const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Fix 7-25
code = code.replace("'7-25':'जन्माष्टमी 🦚',", "");

// Add 8-4 before 8-14
code = code.replace(
  "'8-14':'गणेश चतुर्थी 🐘'",
  "'8-4':'जन्माष्टमी 🦚','8-14':'गणेश चतुर्थी 🐘'"
);

// Verify
const match = code.match(/const CAL_FESTIVALS = \{([\s\S]*?)\};/);
console.log("Updated CAL_FESTIVALS:\n" + match[1].trim());

fs.writeFileSync('app.js', code, 'utf8');
