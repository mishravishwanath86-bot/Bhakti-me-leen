const fs = require('fs');

console.log("=== VERIFYING LORD PURUSHOTTAM AARTI (drik_narayana_5) ===");

// 1. Check final_granular_aarti_collections.json
const jsonRaw = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const collections = JSON.parse(jsonRaw);

const narayanaItems = collections.narayana.items;
const purushottamJson = narayanaItems.find(item => item.id === 'drik_narayana_5');

if (!purushottamJson) {
  console.error("❌ drik_narayana_5 not found in final_granular_aarti_collections.json!");
  process.exit(1);
}
console.log("✓ Found drik_narayana_5 in final_granular_aarti_collections.json");
console.log("  Title:", purushottamJson.title);
console.log("  Drik URL:", purushottamJson.drik_url);
console.log("  Video ID:", purushottamJson.video_id);

// Check content
const expectedLines = [
  'जय पुरुषोत्तम देवा, स्वामी जय पुरुषोत्तम देवा',
  'महिमा अमित तुम्हारी, सुर-मुनि करें सेवा',
  'सब मासों में उत्तम, तुमको बतलाया',
  'कृपा हुई जब हरि की, कृष्ण रूप पाया',
  'पूजा तुमको जिसने, सर्व सुक्ख दीना',
  'निर्मल करके काया, पाप छार कीना',
  'मेधावी मुनि कन्या, महिमा जब जानी',
  'द्रोपदि नाम सती से, जग ने सन्मानी',
  'विप्र सुदेव सेवा कर, मृत सुत पुनि पाया',
  'धाम हरि का पाया, यश जग में छाया',
  'नृप दृढ़धन्वा पर जब, तुमने कृपा करी',
  'व्रतविधि नियम और पूजा, कीनी भक्ति भरी',
  'शूद्र मणीग्रिव पापी, दीपदान किया',
  'निर्मल बुद्धि तुम करके, हरि धाम दिया',
  'पुरुषोत्तम व्रत-पूजा, हित चित से करते',
  'प्रभुदास भव नद से, सहजही वे तरते'
];

for (const line of expectedLines) {
  if (!purushottamJson.content.includes(line)) {
    console.error(`❌ Missing line in JSON content: "${line}"`);
    process.exit(1);
  }
}
console.log("✓ All 16 authentic Sanatan Panchang lines verified in JSON content!");

if (!purushottamJson.meaning || !purushottamJson.meaning.includes('द्रौपदी') || !purushottamJson.meaning.includes('मणिग्रीव')) {
  console.error("❌ Missing detailed Bhavarth stories in JSON!");
  process.exit(1);
}
console.log("✓ Verse-by-verse Bhavarth verified with Puranic context!");

if (!purushottamJson.vidhi || !purushottamJson.vidhi.includes('4-2-1-7') || !purushottamJson.vidhi.includes('दीपदान')) {
  console.error("❌ Missing Vidhi in JSON!");
  process.exit(1);
}
console.log("✓ 4-2-1-7 Purushottam Deepa Samarpan Vidhi verified!");

if (!purushottamJson.significance || !purushottamJson.significance.includes('अधिकमास')) {
  console.error("❌ Missing Significance in JSON!");
  process.exit(1);
}
console.log("✓ Spiritual Significance / Phalasruti verified!");

// 2. Check app.js
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_narayana_5"')) {
  console.error("❌ drik_narayana_5 not found in app.js!");
  process.exit(1);
}
for (const line of expectedLines) {
  if (!appJs.includes(line)) {
    console.error(`❌ Missing line in app.js content: "${line}"`);
    process.exit(1);
  }
}
console.log("✓ All lines verified in app.js!");

console.log("\n🎉 ALL VERIFICATION CHECKS FOR LORD PURUSHOTTAM AARTI PASSED 100%!");
