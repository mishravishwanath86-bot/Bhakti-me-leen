const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, 'final_granular_aarti_collections.json');
const appJsPath = path.join(__dirname, 'app.js');

console.log("=== Checking final_granular_aarti_collections.json ===");
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const shivaItem = data.shiva.items.find(x => x.id === 'drik_shiva_3');

if (!shivaItem) {
  console.error("FAIL: drik_shiva_3 not found in JSON!");
  process.exit(1);
}

console.log("Title:", shivaItem.title);
console.log("Title EN:", shivaItem.title_en);
console.log("Video ID:", shivaItem.video_id);
console.log("Drik URL:", shivaItem.drik_url);
console.log("Content length:", shivaItem.content.length);
console.log("Meaning length:", shivaItem.meaning.length);
console.log("Vidhi length:", shivaItem.vidhi.length);
console.log("Significance length:", shivaItem.significance.length);
console.log("English lyrics length:", shivaItem.english_lyrics.length);

console.log("\n=== Checking app.js ===");
const appJs = fs.readFileSync(appJsPath, 'utf8');

if (!appJs.includes('"id": "drik_shiva_3"')) {
  console.error("FAIL: drik_shiva_3 not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('2wDdtliebqk')) {
  console.error("FAIL: video_id 2wDdtliebqk not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('जयति जयति जग-निवास')) {
  console.error("FAIL: Devanagari lyrics not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('अशरण जन नित्य शरण')) {
  console.error("FAIL: 8th verse not found in app.js!");
  process.exit(1);
}

console.log("ALL SHANKARA AARTI VERIFICATIONS PASSED SUCCESSFULLY!");
