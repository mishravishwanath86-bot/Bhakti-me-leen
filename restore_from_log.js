const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript_full.jsonl'),
  crlfDelay: Infinity
});

let foundCode = null;
let highestStep = -1;

rl.on('line', (line) => {
  if (line.includes('write_to_file') && line.includes('app.js')) {
    try {
      const obj = JSON.parse(line);
      if (obj.tool_calls) {
        for (const call of obj.tool_calls) {
          if (call.function && call.function.name === 'default_api:write_to_file') {
            const args = JSON.parse(call.function.arguments);
            if (args.TargetFile && args.TargetFile.endsWith('app.js')) {
              foundCode = args.CodeContent;
              highestStep = obj.step_index;
            }
          }
        }
      }
    } catch(e) {}
  }
});

rl.on('close', () => {
  if (foundCode) {
    fs.writeFileSync('app_restored.js', foundCode, 'utf8');
    console.log("Restored app.js from step", highestStep, "Length:", foundCode.length);
  } else {
    console.log("Could not find app.js in transcript.");
  }
});
