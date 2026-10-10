const fs = require('fs');

const files = fs.readdirSync('assets');
console.log("=== Asset Images ===");
const imgFiles = files.filter(f => f.endsWith('.jpg') || f.endsWith('.png'));
imgFiles.forEach(f => {
  const stat = fs.statSync(`assets/${f}`);
  if (stat.size > 50000) { // Larger than 50KB = high quality image
    console.log(`${f} (${Math.round(stat.size/1024)} KB)`);
  }
});
