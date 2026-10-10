const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const constants = ['HINDU_FESTIVALS', 'SANKASHTI_RELATED', 'SANKASHTI_DATES_2026', 'HINDU_VRATS', 'SPECIAL_VRATS', 'TOP10_FESTIVALS', 'VRAT_PAGES_DATA'];

for (let name of constants) {
  let regex = new RegExp(`const ${name} = \\[[\\s\\S]*?\\];`, 'g');
  if(name === 'VRAT_PAGES_DATA') {
    regex = new RegExp(`const ${name} = \\{[\\s\\S]*?\\n\\};`, 'g');
  }
  
  let matches = [...code.matchAll(regex)];
  if(matches.length > 1) {
    console.log(`Found ${matches.length} instances of ${name}`);
    for(let i=1; i<matches.length; i++) {
      code = code.replace(matches[i][0], '');
    }
  }
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Deduplicated all constants');
