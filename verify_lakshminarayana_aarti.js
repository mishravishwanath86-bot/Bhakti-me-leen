const fs = require('fs');

console.log("=== Verifying drik_narayana_2 ===");

const jsonStr = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const data = JSON.parse(jsonStr);

const narayana = data.narayana;
if (!narayana) {
    console.error("FAIL: narayana collection missing");
    process.exit(1);
}

const item = narayana.items.find(it => it.id === 'drik_narayana_2');
if (!item) {
    console.error("FAIL: drik_narayana_2 not found in json");
    process.exit(1);
}

console.log("ID:", item.id);
console.log("Title:", item.title);
console.log("Title EN:", item.title_en);
console.log("Video ID:", item.video_id);
console.log("Drik URL:", item.drik_url);
console.log("Audio URL:", item.audio_url);
console.log("Content length:", item.content ? item.content.length : 0);
console.log("Meaning length:", item.meaning ? item.meaning.length : 0);
console.log("Vidhi length:", item.vidhi ? item.vidhi.length : 0);
console.log("Significance length:", item.significance ? item.significance.length : 0);
console.log("English lyrics length:", item.english_lyrics ? item.english_lyrics.length : 0);

// Verify presence of all key lines
const content = item.content;
const requiredLines = [
    "जय लक्ष्मी-विष्णो।",
    "जय लक्ष्मीनारायण, जय लक्ष्मी-विष्णो।",
    "जय माधव, जय श्रीपति, जय, जय, जय विष्णो॥",
    "जय चम्पा सम-वर्णे, जय नीरदकान्ते।",
    "कमल वराभय-हस्ते, शङ्खादिकधारिन्।",
    "सच्चिन्मयकरचरणे, सच्चिन्मयमूर्ते।",
    "तुम त्रिभुवन की माता, तुम सबके त्राता।",
    "तुम धन जन सुख सन्तति, जय देनेवाली।",
    "तुम हो सुमति घरों में, तुम सबके स्वामी।",
    "शरणागत हूँ मुझ पर, कृपा करो माता।",
    "जय लक्ष्मी-नारायण, नव-मन्गल दाता॥"
];

for (const line of requiredLines) {
    if (!content.includes(line)) {
        console.error(`FAIL: Missing line in content: ${line}`);
        process.exit(1);
    }
}

// Check app.js contains the item
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_narayana_2"') || !appJs.includes('"video_id": "xcVv68gwc5Y"')) {
    console.error("FAIL: app.js does not contain updated drik_narayana_2");
    process.exit(1);
}

console.log("SUCCESS: drik_narayana_2 verified in both files!");
