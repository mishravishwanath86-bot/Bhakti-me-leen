const fs = require('fs');
const path = require('path');

const dir = 'assets/audio';
const files = fs.readdirSync(dir);
files.forEach(f => {
  const stat = fs.statSync(path.join(dir, f));
  console.log(`${f}: ${(stat.size / 1024 / 1024).toFixed(2)} MB`);
});
