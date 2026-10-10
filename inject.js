const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');
let data = JSON.parse(fs.readFileSync('vrat_data.json', 'utf8'));

// We need to inject data.ekadashi into VRAT_PAGES_DATA['ekadashi'].dates
for(let key of Object.keys(data)) {
    let datesArrayStr = JSON.stringify(data[key]);
    let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
    code = code.replace(regex, `$1${datesArrayStr}`);
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Injected dates into app.js');
