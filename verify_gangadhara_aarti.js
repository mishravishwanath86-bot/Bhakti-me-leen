const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, 'final_granular_aarti_collections.json');
const appJsPath = path.join(__dirname, 'app.js');

console.log("=== Checking final_granular_aarti_collections.json ===");
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const gangadharaItem = data.shiva.items.find(x => x.id === 'drik_shiva_4');

if (!gangadharaItem) {
  console.error("FAIL: drik_shiva_4 not found in JSON!");
  process.exit(1);
}

console.log("Title:", gangadharaItem.title);
console.log("Title EN:", gangadharaItem.title_en);
console.log("Video ID:", gangadharaItem.video_id);
console.log("Drik URL:", gangadharaItem.drik_url);
console.log("Content length:", gangadharaItem.content.length);
console.log("Meaning length:", gangadharaItem.meaning.length);
console.log("Vidhi length:", gangadharaItem.vidhi.length);
console.log("Significance length:", gangadharaItem.significance.length);
console.log("English lyrics length:", gangadharaItem.english_lyrics.length);

console.log("\n=== Checking app.js ===");
const appJs = fs.readFileSync(appJsPath, 'utf8');

if (!appJs.includes('"id": "drik_shiva_4"')) {
  console.error("FAIL: drik_shiva_4 not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('iRxxfJwyxzs')) {
  console.error("FAIL: video_id iRxxfJwyxzs not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('ॐ जय गङ्गाधर जय हर')) {
  console.error("FAIL: Devanagari lyrics not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('शिवसायुज्यं गच्छति')) {
  console.error("FAIL: 8th verse (phalasruti) not found in app.js!");
  process.exit(1);
}

console.log("ALL GANGADHARA AARTI VERIFICATIONS PASSED SUCCESSFULLY!");
