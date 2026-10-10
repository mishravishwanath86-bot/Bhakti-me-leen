const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// We just want to DELETE everything from the SECOND `function initVratGrids()` to the end of its garbage,
// or actually, just keep ONE `initVratGrids()`.
// Since we have a perfect version that we just injected, let's just delete the rest of the file and paste the bottom parts?
// Wait, no, we can just use Regex to find ALL `function initVratGrids() { ... }` blocks and replace them.

// Let's use a very simple approach:
// We will read the file line by line.

let lines = code.split('\n');
let insideCorrupted = false;
let newLines = [];
let foundFirst = false;

for(let i=0; i<lines.length; i++) {
  let line = lines[i];
  
  if(line.includes('function initVratGrids() {')) {
    if(!foundFirst) {
      foundFirst = true;
      // We keep the first one! It's the perfect one we built.
      newLines.push(line);
    } else {
      // This is the second one! We start skipping until we hit another function.
      insideCorrupted = true;
      continue;
    }
  } else if(insideCorrupted && line.startsWith('function ')) {
    // We hit the next function! Stop skipping.
    insideCorrupted = false;
    newLines.push(line);
  } else if(!insideCorrupted) {
    newLines.push(line);
  }
}

fs.writeFileSync('app.js', newLines.join('\n'), 'utf8');
console.log('Removed duplicate corrupted block!');
