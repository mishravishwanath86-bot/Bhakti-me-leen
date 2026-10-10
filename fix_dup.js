const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const parts = code.split('const SPECIAL_VRATS = [');
if (parts.length > 2) {
  // It has at least 3 parts (so 2 occurrences)
  // We should remove the second occurrence.
  // The second occurrence is parts[2]. Where does it end?
  const endIdx = parts[2].indexOf('];') + 2;
  parts[2] = parts[2].substring(endIdx); // delete the array block
  code = parts.join('const SPECIAL_VRATS = [');
  // Wait, joining it back with "const SPECIAL_VRATS =" will just recreate it!
  // It's better to manually remove it using Regex
}

code = code.replace(/const SPECIAL_VRATS = \[[^\]]*\];/g, (match, offset, string) => {
    // only keep the first occurrence
    return offset === string.indexOf('const SPECIAL_VRATS = [') ? match : '';
});

fs.writeFileSync('app.js', code, 'utf8');
console.log('Removed duplicate SPECIAL_VRATS');
