const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Find the start and end of the block to remove
const startText = "const progFill = document.getElementById('mini-progress-fill');";
const endText = "audioPlayer.addEventListener('loadedmetadata', () => {\n    if(timeDisp) timeDisp.innerHTML = '00:00 / ' + formatTime(audioPlayer.duration);\n  });";

// Let's just remove the first declarations of timeDisp and progFill, and the old timeupdate listener.
const lines = code.split('\n');
let newLines = [];
let skip = false;

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    // We want to keep the NEW logic which is around line 6677 (miniPlayBtn).
    // The old logic starts around 6606. Let's just use regex or exact matching to fix it.
    
    if (line.includes("const progFill = document.getElementById('mini-progress-fill');") && i < 6610) {
        skip = true;
    }
    
    if (skip && line.includes("audioPlayer.addEventListener('loadedmetadata'")) {
        // skip this and next 2 lines
        i += 2;
        skip = false;
        continue;
    }
    
    if (skip && line.includes("audioPlayer.addEventListener('timeupdate'")) {
        // it's skipping...
    }
    
    if (!skip) {
        newLines.push(line);
    }
}

fs.writeFileSync('app.js', newLines.join('\n'), 'utf8');
console.log("Cleanup done.");
