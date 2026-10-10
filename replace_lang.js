const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const regex = /<select class="inline-select"><option>.*?<\/option><option>English<\/option>.*?<\/select>/;

const newSelect = `<select class="inline-select">
  <option>हिन्दी (Hindi)</option>
  <option>English</option>
  <option>ગુજરાતી (Gujarati)</option>
  <option>मराठी (Marathi)</option>
  <option>বাংলা (Bengali)</option>
  <option>தமிழ் (Tamil)</option>
  <option>తెలుగు (Telugu)</option>
  <option>ಕನ್ನಡ (Kannada)</option>
  <option>മലയാളം (Malayalam)</option>
  <option>ਪੰਜਾਬੀ (Punjabi)</option>
  <option>ଓଡ଼ିଆ (Odia)</option>
  <option>অসমীয়া (Assamese)</option>
</select>`;

html = html.replace(regex, newSelect);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Language select updated via regex!');
