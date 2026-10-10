const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

// Test that CONTENT contains the keys
const keys = ['chalisa_hanuman', 'chalisa_shiv', 'mantra_gayatri', 'mantra_mahamrityunjaya', 'aarti_ganesh'];
for (let k of keys) {
  console.log(`Key ${k} exists in CONTENT:`, code.includes(k + ':'));
}
