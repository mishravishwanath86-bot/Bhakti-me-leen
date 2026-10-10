const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

let lines = code.split('\n');
let opened = false;
for(let i=0; i<lines.length; i++) {
  let btCount = (lines[i].match(/`/g) || []).length;
  if(btCount % 2 !== 0) {
      opened = !opened;
      console.log(`Line ${i+1} has odd backticks (now ${opened ? 'OPEN' : 'CLOSED'})`);
      console.log("->", lines[i].trim());
  }
}
