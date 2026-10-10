const fs = require('fs');

console.log("=== VERIFYING AMBE MATA AARTI (drik_goddesses_1) ===");

// 1. Check final_granular_aarti_collections.json
const jsonRaw = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const collections = JSON.parse(jsonRaw);

const durgaItems = collections.durga.items;
const ambeJson = durgaItems.find(item => item.id === 'drik_goddesses_1');

if (!ambeJson) {
  console.error("❌ drik_goddesses_1 not found in final_granular_aarti_collections.json!");
  process.exit(1);
}
console.log("✓ Found drik_goddesses_1 in final_granular_aarti_collections.json");
console.log("  Title:", ambeJson.title);
console.log("  Drik URL:", ambeJson.drik_url);
console.log("  Video ID:", ambeJson.video_id);

// Check all 12 stanzas
const expectedPhrases = [
  'जय अम्बे गौरी, मैया जय श्यामा गौरी',
  'हरि ब्रह्मा शिवरी',
  'माँग सिन्दूर विराजत, टीको मृगमद को',
  'चन्द्रवदन नीको',
  'कनक समान कलेवर, रक्ताम्बर राजै',
  'रक्तपुष्प गल माला',
  'केहरि वाहन राजत, खड्ग खप्परधारी',
  'सुर-नर-मुनि-जन सेवत',
  'कानन कुण्डल शोभित, नासाग्रे मोती',
  'कोटिक चन्द्र दिवाकर',
  'शुम्भ-निशुम्भ बिदारे, महिषासुर घाती',
  'धूम्र विलोचन नैना',
  'चण्ड-मुण्ड संहारे, शोणित बीज हरे',
  'मधु-कैटभ दोउ मारे',
  'ब्रहमाणी रुद्राणी, तुम कमला रानी',
  'आगम-निगम-बखानी, तुम शिव पटरानी',
  'चौंसठ योगिनी मंगल गावत, नृत्य करत भैरूँ',
  'बाजत ताल मृदंगा, अरु बाजत डमरु',
  'तुम ही जग की माता, तुम ही हो भरता',
  'सुख सम्पत्ति करता',
  'भुजा चार अति शोभित, वर-मुद्रा धारी',
  'मनवान्छित फल पावत',
  'कन्चन थाल विराजत, अगर कपूर बाती',
  'श्रीमालकेतु में राजत, कोटि रतन ज्योति',
  'श्री अम्बेजी की आरती, जो कोई नर गावै',
  'कहत शिवानन्द स्वामी, सुख सम्पत्ति पावै'
];

for (const phrase of expectedPhrases) {
  if (!ambeJson.content.includes(phrase)) {
    console.error(`❌ Missing phrase in JSON content: "${phrase}"`);
    process.exit(1);
  }
}
console.log("✓ All 12 stanzas and chorus lines verified in JSON content!");

if (!ambeJson.meaning || !ambeJson.meaning.includes('शुम्भ-निशुम्भ') || !ambeJson.meaning.includes('चौंसठ योगिनी')) {
  console.error("❌ Missing detailed Bhavarth in JSON!");
  process.exit(1);
}
console.log("✓ Verse-by-verse Bhavarth verified with Puranic context!");

if (!ambeJson.vidhi || !ambeJson.vidhi.includes('4-2-1-7')) {
  console.error("❌ Missing 4-2-1-7 Vidhi in JSON!");
  process.exit(1);
}
console.log("✓ 4-2-1-7 Deepa Samarpan Vidhi verified!");

if (!ambeJson.significance || !ambeJson.significance.includes('शिवानन्द स्वामी')) {
  console.error("❌ Missing Significance in JSON!");
  process.exit(1);
}
console.log("✓ Spiritual Significance / Phalasruti verified!");

// 2. Check app.js
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_goddesses_1"')) {
  console.error("❌ drik_goddesses_1 not found in app.js!");
  process.exit(1);
}
for (const phrase of expectedPhrases) {
  if (!appJs.includes(phrase)) {
    console.error(`❌ Missing phrase in app.js content: "${phrase}"`);
    process.exit(1);
  }
}
console.log("✓ All 12 stanzas verified in app.js!");

console.log("\n🎉 ALL VERIFICATION CHECKS FOR AMBE MATA AARTI PASSED 100%!");
