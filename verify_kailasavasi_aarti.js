const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, 'final_granular_aarti_collections.json');
const appJsPath = path.join(__dirname, 'app.js');

console.log("=== Checking final_granular_aarti_collections.json ===");
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const kailasavasiItem = data.shiva.items.find(x => x.id === 'drik_shiva_5');

if (!kailasavasiItem) {
  console.error("FAIL: drik_shiva_5 not found in JSON!");
  process.exit(1);
}

console.log("Title:", kailasavasiItem.title);
console.log("Title EN:", kailasavasiItem.title_en);
console.log("Video ID:", kailasavasiItem.video_id);
console.log("Drik URL:", kailasavasiItem.drik_url);
console.log("Content length:", kailasavasiItem.content.length);
console.log("Meaning length:", kailasavasiItem.meaning.length);
console.log("Vidhi length:", kailasavasiItem.vidhi.length);
console.log("Significance length:", kailasavasiItem.significance.length);
console.log("English lyrics length:", kailasavasiItem.english_lyrics.length);

console.log("\n=== Checking app.js ===");
const appJs = fs.readFileSync(appJsPath, 'utf8');

if (!appJs.includes('"id": "drik_shiva_5"')) {
  console.error("FAIL: drik_shiva_5 not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('ia-VnDrt3Oc')) {
  console.error("FAIL: video_id ia-VnDrt3Oc not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('शीश गंग अर्धन्ग पार्वती')) {
  console.error("FAIL: Devanagari lyrics not found in app.js!");
  process.exit(1);
}

if (!appJs.includes('किंकरकी विनती सुनियो')) {
  console.error("FAIL: 10th verse not found in app.js!");
  process.exit(1);
}

console.log("ALL KAILASAVASI AARTI VERIFICATIONS PASSED SUCCESSFULLY!");
