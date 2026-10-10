const fs = require('fs');
const data = fs.readFileSync('data/festivals_detail.json', 'utf8');
const parsed = JSON.parse(data);
console.log('JSON Valid! Festivals count:', parsed.festivals.length);
parsed.festivals.forEach((f, idx) => {
  console.log(`${idx+1}. ${f.festivalName} (${f.date})`);
});
