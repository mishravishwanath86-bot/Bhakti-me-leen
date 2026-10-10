const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const matches = [];
const lines = css.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('.bottom-nav') || line.includes('bottom:0')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.join('\n'));
