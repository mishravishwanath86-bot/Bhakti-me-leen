const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript.jsonl'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  if (line.includes('"step_index":905')) {
    const json = JSON.parse(line);
    console.log(json.content);
  }
});
