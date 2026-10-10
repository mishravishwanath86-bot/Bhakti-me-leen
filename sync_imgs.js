const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

// We need to parse HINDU_VRATS and SPECIAL_VRATS, extract the page -> img mapping,
// then update VRAT_PAGES_DATA's heroImg.

// Let's do it safely by just finding the mapping dynamically inside the JS context.
// Or we can just use Regex.

let map = {};
const vratsStr = code.match(/const HINDU_VRATS = \[([\s\S]*?)\];/)[1];
const svratsStr = code.match(/const SPECIAL_VRATS = \[([\s\S]*?)\];/)[1];

function extractMap(str) {
  let lines = str.split('\n');
  for(let l of lines) {
    let pageMatch = l.match(/page:\s*'([^']+)'/);
    let imgMatch = l.match(/img:\s*'([^']+)'/);
    if(pageMatch && imgMatch) {
      map[pageMatch[1]] = imgMatch[1];
    }
  }
}

extractMap(vratsStr);
extractMap(svratsStr);

for (let key in map) {
  let img = map[key];
  // Replace heroImg: 'assets/...' with heroImg: 'actual_img'
  // But wait, the heroImg might be generic like 'assets/deity_shiv.jpg'
  
  let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?heroImg:\\s*)'[^']+'`);
  code = code.replace(regex, `$1'${img}'`);
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Hero images synced to grid icons!');
