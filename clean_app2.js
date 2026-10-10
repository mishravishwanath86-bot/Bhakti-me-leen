const fs = require('fs');
const oldCode = fs.readFileSync('app.js', 'utf8');

const s1 = oldCode.indexOf('//  KATHA / PODCAST');
const s2 = oldCode.indexOf('//   ENGLISH CALENDAR  (Google Calendar style)');

console.log("s1:", s1, "s2:", s2);
if (s1 > -1 && s2 > -1) {
    // find the previous line boundary before s2
    const realS2 = oldCode.lastIndexOf('\n', s2 - 50); 
    
    // find the end of the line containing KATHA / PODCAST, plus the next line (the weird separator)
    let s1End = oldCode.indexOf('\n', s1);
    s1End = oldCode.indexOf('\n', s1End + 1);
    
    const part1 = oldCode.substring(0, s1End + 1);
    const part3 = oldCode.substring(realS2 + 1); // skip the newline
    
    // Read the reconstructed logic we want
    const part2 = fs.readFileSync('clean_app.js', 'utf8').match(/const part2 = `([\s\S]*?)`;/)[1];
    
    fs.writeFileSync('app.js', part1 + part2 + '\n' + part3, 'utf8');
    console.log("Cleaned app.js");
}
