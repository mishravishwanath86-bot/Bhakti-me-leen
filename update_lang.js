const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const oldSelect = `<select class="inline-select"><option>हिन्दी</option><option>English</option><option>Gujarati</option><option>Marathi</option></select>`;

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

if (html.includes(oldSelect)) {
  html = html.replace(oldSelect, newSelect);
  fs.writeFileSync('index.html', html, 'utf8');
  console.log('Language select updated!');
} else {
  console.log('Could not find exact language select string. Searching for similar...');
  const selectStart = html.indexOf('<select class="inline-select"><option>हिन्दी</option>');
  if(selectStart > -1) {
     const selectEnd = html.indexOf('</select>', selectStart) + 9;
     html = html.substring(0, selectStart) + newSelect + html.substring(selectEnd);
     fs.writeFileSync('index.html', html, 'utf8');
     console.log('Language select updated using substring.');
  } else {
     console.log('Not found.');
  }
}
