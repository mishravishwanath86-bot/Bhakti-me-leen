const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript.jsonl'),
  crlfDelay: Infinity
});

let found = 0;
rl.on('line', (line) => {
  if (line.includes('cat-card') && found < 2) {
    const idx = line.indexOf('<section id="page-home"');
    if (idx !== -1) {
      console.log("=== Found page-home snippet ===");
      console.log(line.substring(idx, idx + 2500));
      found++;
    }
  }
});
