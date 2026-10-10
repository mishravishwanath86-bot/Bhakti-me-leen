const fs = require('fs');
const path = require('path');

const userUploadedDir = 'C:\\Users\\vishw\\.gemini\\antigravity\\brain\\e50f2a93-46d3-48c0-84de-1c22a15837d4\\.user_uploaded';
const assetsDir = 'assets';

if (!fs.existsSync(assetsDir)) fs.mkdirSync(assetsDir);

const files = fs.readdirSync(userUploadedDir);
console.log("Uploaded files:", files);

for (let f of files) {
  const src = path.join(userUploadedDir, f);
  const dest = path.join(assetsDir, f);
  fs.copyFileSync(src, dest);
  console.log(`Copied ${f} to assets/${f}`);
}

// Also create named copies for the user's images
fs.copyFileSync(path.join(userUploadedDir, 'media_1787442043669.png'), path.join(assetsDir, 'onboard_om_mandala.png'));
fs.copyFileSync(path.join(userUploadedDir, 'media_1787442043671.png'), path.join(assetsDir, 'onboard_ganga_aarti.png'));
console.log("Copied named assets successfully!");
