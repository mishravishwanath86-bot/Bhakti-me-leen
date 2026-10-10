const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Fix function definition
code = code.replace("function initCalendar(); initEngCalendar(){", "function initCalendar(){");

// Fix function call at initialization
// To be safe, first replace all 'initCalendar();' calls, but it might replace the one we just fixed if we are not careful.
// Actually, since we know it's near the end (DOM content loaded or initApp), let's just do a string replace of the exact call.
code = code.replace(/initCalendar\(\);\s*$/, "initCalendar();\n  initEngCalendar();");

// Since regex on end of line can be tricky with formatting, let's just use exact replace:
code = code.replace("  initCalendar();\n", "  initCalendar();\n  initEngCalendar();\n");

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed syntax error!');
