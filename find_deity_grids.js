const fs = require('fs');

// Check all js files to find where buildDeityGrid or DEITIES or AARTI_LIST was defined
const files = fs.readdirSync('.').filter(f => f.endsWith('.js'));
for (let f of files) {
  const content = fs.readFileSync(f, 'utf8');
  if (content.includes('chalisa-deity-grid') || content.includes('buildDeityGrid') || content.includes('initDeityGrids')) {
    console.log(`Found in: ${f}`);
  }
}
