const fs = require('fs');
const path = require('path');

const data = JSON.parse(fs.readFileSync('bhagavad_gita_chapters.json', 'utf8'));

console.log("=================================================");
console.log("   VERIFYING CHAPTERS 1 TO 5 (BHAGAVADGITA.COM)");
console.log("=================================================\n");

const expected = [
  { ch: 1, name: "अर्जुनविषादयोग", verses: 47 },
  { ch: 2, name: "सांख्ययोग", verses: 72 },
  { ch: 3, name: "कर्मयोग", verses: 43 },
  { ch: 4, name: "ज्ञानकर्मसंन्यासयोग", verses: 42 },
  { ch: 5, name: "कर्मसंन्यासयोग", verses: 29 }
];

let total1to5 = 0;
expected.forEach(exp => {
  const chap = data.chapters.find(c => c.chapter_number === exp.ch);
  if (!chap) {
    console.error(`FAIL: Chapter ${exp.ch} not found!`);
    process.exit(1);
  }

  console.log(`✓ Chapter ${exp.ch}: ${chap.name} (${chap.name_transliterated})`);
  console.log(`  - Verses Count: ${chap.verses.length} (Expected: ${exp.verses})`);
  if (chap.verses.length !== exp.verses) {
    console.error(`FAIL: Mismatched verses count for Chapter ${exp.ch}! Got ${chap.verses.length}, expected ${exp.verses}`);
    process.exit(1);
  }
  total1to5 += chap.verses.length;

  console.log(`  - Summary length: ${chap.summary.length} characters`);
  console.log(`  - Summary snippet: ${chap.summary.substring(0, 100)}...`);
  if (chap.summary.length < 300) {
    console.error(`FAIL: Summary too short for Chapter ${exp.ch}!`);
    process.exit(1);
  }

  // Check first and last verse
  const firstV = chap.verses[0];
  const lastV = chap.verses[chap.verses.length - 1];
  console.log(`  - Verse ${firstV.verse_number}:`);
  console.log(`    Sanskrit: ${firstV.sanskrit.split('\n')[0]}...`);
  console.log(`    Hindi: ${firstV.hindi.substring(0, 80)}...`);
  console.log(`    Audio: ${firstV.audio_url}`);
  console.log(`  - Last Verse ${lastV.verse_number}:`);
  console.log(`    Sanskrit: ${lastV.sanskrit.split('\n')[0]}...`);
  console.log(`    Hindi: ${lastV.hindi.substring(0, 80)}...\n`);
});

console.log(`>>> TOTAL VERSES FOR CHAPTERS 1 TO 5: ${total1to5} (47 + 72 + 43 + 42 + 29 = 233)`);
console.log(">>> ALL 5 CHAPTERS AND 233 VERSES VERIFIED SUCCESSFULLY FROM BHAGAVADGITA.COM! ✨\n");
