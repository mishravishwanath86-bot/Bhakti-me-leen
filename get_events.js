const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const match = code.match(/const HINDU_FESTIVALS = \[([\s\S]*?)\];/);
if(match) console.log("HINDU_FESTIVALS\n", match[1].substring(0, 500));

const match2 = code.match(/const events = \[([\s\S]*?)\];/);
if(match2) console.log("events\n", match2[1].substring(0, 500));

