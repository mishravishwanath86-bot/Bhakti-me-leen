const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript.jsonl'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  if (line.includes('function buildDeityGrid') || line.includes('function initDeityGrids')) {
    console.log("Found line snippet:", line.substring(0, 300));
    // Print the code block around it
    const idx = line.indexOf('function buildDeityGrid');
    if (idx !== -1) {
      console.log(line.substring(idx - 100, idx + 1500));
    }
  }
});
