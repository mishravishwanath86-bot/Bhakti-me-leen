const fs = require('fs');
// Let's generate a quick base64 string of the image so we can inspect it or just rely on the assumption.
const img = fs.readFileSync('assets/fest_0_0.jpg', 'base64');
console.log(img.substring(0, 100) + "...");
