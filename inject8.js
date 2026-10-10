const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');
let data = JSON.parse(fs.readFileSync('vrat_data_8.json', 'utf8'));

for(let key of Object.keys(data)) {
    if(data[key].length > 0) {
        let datesArrayStr = JSON.stringify(data[key]);
        let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
        code = code.replace(regex, `$1${datesArrayStr}`);
    } else {
        let placeholder = JSON.stringify([
           {month: 'N/A', day: '--', weekday: '', name: 'तिथियाँ उपलब्ध नहीं', tithi: ''}
        ]);
        let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
        code = code.replace(regex, `$1${placeholder}`);
    }
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Injected dates for the 8 final vrats!');
