const fs = require('fs');
const lines = fs.readFileSync('C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.system_generated\\logs\\transcript_full.jsonl', 'utf8').split('\n');

for (const line of lines) {
  if (line.includes('const TOP10_FESTIVALS =') && line.includes('page: \'page-ramnavami\'')) {
    try {
      const obj = JSON.parse(line);
      console.log("Step with fully wired TOP10_FESTIVALS:", obj.step_index);
      if (obj.tool_calls) {
        for (const tc of obj.tool_calls) {
          console.log(tc.args.CommandLine || tc.args.CodeContent || JSON.stringify(tc.args).substring(0, 500));
        }
      }
    } catch(e) {}
  }
}
