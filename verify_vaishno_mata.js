const fs = require('fs');

console.log("=== VERIFYING VAISHNO MATA AARTI (drik_goddesses_5) ===");

// 1. Check final_granular_aarti_collections.json
const jsonRaw = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const collections = JSON.parse(jsonRaw);

const durgaItems = collections.durga.items;
const vaishnoJson = durgaItems.find(item => item.id === 'drik_goddesses_5');

if (!vaishnoJson) {
  console.error("❌ drik_goddesses_5 not found in final_granular_aarti_collections.json!");
  process.exit(1);
}
console.log("✓ Found drik_goddesses_5 in final_granular_aarti_collections.json");
console.log("  Title:", vaishnoJson.title);
console.log("  Drik URL:", vaishnoJson.drik_url);
console.log("  Video ID:", vaishnoJson.video_id);

// Check all stanzas
const expectedPhrases = [
  'जय वैष्णवी माता, मैया जय वैष्णवी माता',
  'हाथ जोड़ तेरे आगे, आरती मैं गाता',
  'शीश पे छत्र विराजे, मूरतिया प्यारी',
  'गंगा बहती चरनन, ज्योति जगे न्यारी',
  'ब्रह्मा वेद पढ़े नित द्वारे, शंकर ध्यान धरे',
  'सेवक चंवर डुलावत, नारद नृत्य करे',
  'सुन्दर गुफा तुम्हारी, मन को अति भावे',
  'बार-बार देखन को, ऐ माँ मन चावे',
  'भवन पे झण्डे झूलें, घंटा ध्वनि बाजे',
  'ऊँचा पर्वत तेरा, माता प्रिय लागे',
  'पान सुपारी ध्वजा नारियल, भेंट पुष्प मेवा',
  'दास खड़े चरणों में, दर्शन दो देवा',
  'जो जन निश्चय करके, द्वार तेरे आवे',
  'उसकी इच्छा पूरण, माता हो जावे',
  'इतनी स्तुति निश-दिन, जो नर भी गावे',
  'कहते सेवक ध्यानू, सुख सम्पत्ति पावे'
];

for (const phrase of expectedPhrases) {
  if (!vaishnoJson.content.includes(phrase)) {
    console.error(`❌ Missing phrase in JSON content: "${phrase}"`);
    process.exit(1);
  }
}
console.log("✓ All 8 stanzas verified in JSON content!");

if (!vaishnoJson.meaning || !vaishnoJson.meaning.includes('ध्यानू') || !vaishnoJson.meaning.includes('बाणगंगा')) {
  console.error("❌ Missing detailed Bhavarth in JSON!");
  process.exit(1);
}
console.log("✓ Verse-by-verse Bhavarth verified with Puranic context!");

if (!vaishnoJson.vidhi || !vaishnoJson.vidhi.includes('4-2-1-7')) {
  console.error("❌ Missing 4-2-1-7 Vidhi in JSON!");
  process.exit(1);
}
console.log("✓ 4-2-1-7 Deepa Samarpan Vidhi verified!");

if (!vaishnoJson.significance || !vaishnoJson.significance.includes('सेवक ध्यानू')) {
  console.error("❌ Missing Significance in JSON!");
  process.exit(1);
}
console.log("✓ Spiritual Significance / Phalasruti verified!");

// 2. Check app.js
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_goddesses_5"')) {
  console.error("❌ drik_goddesses_5 not found in app.js!");
  process.exit(1);
}
for (const phrase of expectedPhrases) {
  if (!appJs.includes(phrase)) {
    console.error(`❌ Missing phrase in app.js content: "${phrase}"`);
    process.exit(1);
  }
}
console.log("✓ All 8 stanzas verified in app.js!");

console.log("\n🎉 ALL VERIFICATION CHECKS FOR VAISHNO MATA AARTI PASSED 100%!");
