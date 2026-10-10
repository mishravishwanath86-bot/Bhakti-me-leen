const fs = require('fs');
const lines = fs.readFileSync('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript_full.jsonl', 'utf8').split('\n');

for (const line of lines) {
  if (line.includes('VRAT_PAGES_DATA') && (line.includes('.dates =') || line.includes('dates:'))) {
    try {
      const obj = JSON.parse(line);
      console.log("Step:", obj.step_index);
      if (obj.tool_calls) {
        for (const tc of obj.tool_calls) {
          console.log("Tool:", tc.name, "Args:", JSON.stringify(tc.args).substring(0, 300));
        }
      }
    } catch(e) {}
  }
}
