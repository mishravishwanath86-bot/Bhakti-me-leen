const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

// Find all backticks
let btCount = 0;
for(let i = 0; i < code.length; i++) {
  if (code[i] === '`') btCount++;
}
console.log("Total backticks:", btCount);

let count = 0;
let lines = code.split('\n');
for(let i=0; i<lines.length; i++) {
  let lineBTs = (lines[i].match(/`/g) || []).length;
  count += lineBTs;
  if(count % 2 !== 0 && lineBTs > 0) {
      console.log("Odd backtick at line", i+1, lines[i]);
  }
}
