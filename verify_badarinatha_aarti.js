const fs = require('fs');

console.log("=== Verifying drik_narayana_3 ===");

const jsonStr = fs.readFileSync('final_granular_aarti_collections.json', 'utf8');
const data = JSON.parse(jsonStr);

const narayana = data.narayana;
if (!narayana) {
    console.error("FAIL: narayana collection missing");
    process.exit(1);
}

const item = narayana.items.find(it => it.id === 'drik_narayana_3');
if (!item) {
    console.error("FAIL: drik_narayana_3 not found in json");
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
    "जय जय श्री बदरीनाथ, जयति योग ध्यानी॥",
    "निर्गुण सगुण स्वरूप, मेघवर्ण अति अनूप।",
    "सेवत चरण सुरभूप, ज्ञानी विज्ञानी॥",
    "झलकत है शीश छत्र, छवि अनूप अति विचित्र।",
    "बरनत पावन चरित्र, सकुचत बरबानी॥",
    "तिलक भाल अति विशाल, गल में मणि मुक्त-माल।",
    "प्रनतपाल अति दयाल, सेवक सुखदानी॥",
    "कानन कुण्डल ललाम, मूरति सुखमा की धाम।",
    "गावत गुण शम्भु, शेष, इन्द्र, चन्द्र अरु दिनेश।",
    "विनवत श्यामा हमेश, जोरी जुगल पानी॥"
];

for (const line of requiredLines) {
    if (!content.includes(line)) {
        console.error(`FAIL: Missing line in content: ${line}`);
        process.exit(1);
    }
}

// Check app.js contains the item
const appJs = fs.readFileSync('app.js', 'utf8');
if (!appJs.includes('"id": "drik_narayana_3"') || !appJs.includes('"भगवान बदरीनाथ आरती"')) {
    console.error("FAIL: app.js does not contain updated drik_narayana_3");
    process.exit(1);
}

console.log("SUCCESS: drik_narayana_3 verified in both files!");
