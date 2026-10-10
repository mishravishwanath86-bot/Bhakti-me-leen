const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const targets = [
  'home-gita-chapters-grid',
  'id="page-gita"',
  'id="gita-chapter-options-modal"',
  'id="gita-chapter-reader-modal"',
  'id="gita-jumper-modal"',
  'gita_engine.js'
];

targets.forEach(t => {
  const count = html.split(t).length - 1;
  console.log(`${t} => count: ${count}`);
  if (count !== 1) {
    console.error(`ERROR: Expected count 1 for ${t}, got ${count}`);
    process.exit(1);
  }
});
console.log('All elements are unique singletons in index.html!');
