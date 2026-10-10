const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const langSelect = `<select class="inline-select">
            <option>हिन्दी (Hindi)</option>
            <option>English</option>
            <option>ગુજરાતી (Gujarati)</option>
            <option>मराठी (Marathi)</option>
            <option>বাংলা (Bengali)</option>
            <option>తెలుగు (Telugu)</option>
            <option>தமிழ் (Tamil)</option>
            <option>ಕನ್ನಡ (Kannada)</option>
            <option>മലയാളം (Malayalam)</option>
            <option>ਪੰਜਾਬੀ (Punjabi)</option>
            <option>ଓଡ଼ିଆ (Odia)</option>
            <option>Other Languages...</option>
          </select>`;

html = html.replace(/<select class="inline-select"><option>हिंदी<\/option><option>English<\/option><option>Gujarati<\/option><option>Marathi<\/option><\/select>/, langSelect);

// Also cache bust
const time = new Date().getTime();
html = html.replace(/styles\.css(\?v=\d+)?/, `styles.css?v=${time}`);
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Language list updated and cache busted!');
