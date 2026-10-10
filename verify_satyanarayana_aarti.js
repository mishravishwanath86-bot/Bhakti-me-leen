const fs = require('fs');

console.log("=== Verifying drik_narayana_4 ===");

const jsonStr = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const data = JSON.parse(jsonStr);

const narayana = data.narayana;
if (!narayana) {
    console.error("FAIL: narayana collection missing");
    process.exit(1);
}

const item = narayana.items.find(it => it.id === 'drik_narayana_4');
if (!item) {
    console.error("FAIL: drik_narayana_4 not found in json");
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
    "जय लक्ष्मीरमणा श्री जय लक्ष्मीरमणा।",
    "सत्यनारायण स्वामी जनपातक हरणा॥",
    "रत्नजड़ित सिंहासन अद्भुत छवि राजे।",
    "नारद करत निराजन घंटा ध्वनि बाजे॥",
    "प्रगट भये कलि कारण द्विज को दर्श दियो।",
    "बूढ़ो ब्राह्मण बनकर कंचन महल कियो॥",
    "दुर्बल भील कठारो इन पर कृपा करी।",
    "चन्द्रचूड़ एक राजा जिनकी विपति हरी॥",
    "वैश्य मनोरथ पायो श्रद्धा तज दीनी।",
    "भाव भक्ति के कारण छिन-छिन रूप धर्यो।",
    "ग्वाल बाल संग राजा वन में भक्ति करी।",
    "चढ़त प्रसाद सवाया कदली फल मेवा।",
    "श्री सत्यनारायणजी की आरती जो कोई नर गावे।"
];

for (const line of requiredLines) {
    if (!content.includes(line)) {
        console.error(`FAIL: Missing line in content: ${line}`);
        process.exit(1);
    }
}

// Check app.js contains the item
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_narayana_4"') || !appJs.includes('"श्री सत्यनारायण आरती"')) {
    console.error("FAIL: app.js does not contain updated drik_narayana_4");
    process.exit(1);
}

console.log("SUCCESS: drik_narayana_4 verified in both files!");
