const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const matches = [];
const lines = code.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('.wav') || line.includes('.webm')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log('Matches:', matches.length);
if (matches.length > 0) {
  console.log(matches.join('\n'));
}
