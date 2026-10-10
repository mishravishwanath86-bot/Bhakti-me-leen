const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript.jsonl'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  if (line.includes('function initReader()') || line.includes('function buildDeityGrid(')) {
    const json = JSON.parse(line);
    if (json.content && json.content.includes('function initReader()')) {
      console.log("=== Found initReader ===");
      const idx = json.content.indexOf('function initReader()');
      console.log(json.content.substring(idx - 200, idx + 2500));
    }
  }
});
