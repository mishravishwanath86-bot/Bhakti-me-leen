const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');
let data = JSON.parse(fs.readFileSync('vrat_data_4.json', 'utf8'));

for(let key of Object.keys(data)) {
    if(data[key].length > 0) {
        let datesArrayStr = JSON.stringify(data[key]);
        let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
        code = code.replace(regex, `$1${datesArrayStr}`);
    } else {
        // If 0 dates, just put a nice message or placeholder
        let placeholder = JSON.stringify([
           {month: 'No Data', day: '--', weekday: '', name: 'इस वर्ष कोई तिथि नहीं', tithi: ''}
        ]);
        let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
        code = code.replace(regex, `$1${placeholder}`);
    }
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Injected dates for the 4 new vrats!');
