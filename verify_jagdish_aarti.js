const fs = require('fs');

console.log("=== Verifying drik_narayana_1 ===");

const jsonStr = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const data = JSON.parse(jsonStr);

const narayana = data.narayana;
if (!narayana) {
    console.error("FAIL: narayana collection missing");
    process.exit(1);
}

const item = narayana.items.find(it => it.id === 'drik_narayana_1');
if (!item) {
    console.error("FAIL: drik_narayana_1 not found in json");
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

// Verify presence of all key phrases
const content = item.content;
const requiredLines = [
    "ॐ जय जगदीश हरे, स्वामी ! जय जगदीश हरे।",
    "भक्त जनों के संकट, क्षण में दूर करे॥",
    "जो ध्यावे फल पावे, दुःख विनसे मन का।",
    "मात-पिता तुम मेरे, शरण गहूँ मैं किसकी।",
    "तुम पूरण परमात्मा, तुम अन्तर्यामी।",
    "तुम करुणा के सागर, तुम पालन-कर्ता।",
    "तुम हो एक अगोचर, सबके प्राणपति।",
    "दीनबन्धु दुखहर्ता, तुम ठाकुर मेरे।",
    "विषय-विकार मिटाओ, पाप हरो देवा।",
    "श्री जगदीशजी की आरती, जो कोई नर गावे।"
];

for (const line of requiredLines) {
    if (!content.includes(line)) {
        console.error(`FAIL: Missing line in content: ${line}`);
        process.exit(1);
    }
}

// Check app.js contains the item
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_narayana_1"') || !appJs.includes('"video_id": "ty_BRH3b9lY"')) {
    console.error("FAIL: app.js does not contain updated drik_narayana_1");
    process.exit(1);
}

console.log("SUCCESS: drik_narayana_1 verified in both files!");
