const fs = require('fs');

// Check what files are in data/ or root
const files = fs.readdirSync('.');
console.log("Root files:", files.filter(f => f.endsWith('.json') || f.endsWith('.js')));

if (fs.existsSync('data')) {
  console.log("data/ files:", fs.readdirSync('data'));
}
