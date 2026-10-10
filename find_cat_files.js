const fs = require('fs');
const files = fs.readdirSync('.');

for (let f of files) {
  if (f.endsWith('.js') || f.endsWith('.html')) {
    try {
      const c = fs.readFileSync(f, 'utf8');
      if (c.includes('cat-card') || c.includes('category-grid') || c.includes('today-panchang-card')) {
        console.log(`Found in file: ${f}`);
      }
    } catch(e) {}
  }
}
