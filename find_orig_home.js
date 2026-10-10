const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript.jsonl'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  if (line.includes('<section id="page-home"') && line.includes('cat-card') && line.includes('today-panchang-card')) {
    const json = JSON.parse(line);
    const idx = json.content.indexOf('<section id="page-home"');
    if (idx !== -1) {
      console.log("=== Found full original page-home ===");
      console.log(json.content.substring(idx, idx + 4000));
    }
  }
});
