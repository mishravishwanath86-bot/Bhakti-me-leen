const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const pages = [
  'page-top10',
  'page-sankashti',
  'page-vrat-detail',
  'page-holi',
  'page-rakhi',
  'page-diwali',
  'page-dussehra',
  'page-durgapuja',
  'page-navratri',
  'page-ganeshchaturthi',
  'page-ramnavami',
  'page-english-calendar'
];

pages.forEach(p => {
  const idx = html.indexOf(`id="${p}"`);
  if (idx === -1) {
    console.log(`❌ Missing ${p}`);
  } else {
    const end = html.indexOf('</section>', idx);
    console.log(`✅ ${p}: ${end - idx} bytes`);
  }
});
