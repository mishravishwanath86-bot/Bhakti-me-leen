const fs = require('fs');
const path = require('path');

// 1. Verify JSON file
const jsonPath = path.join(__dirname, 'bhagavad_gita_chapters.json');
if (!fs.existsSync(jsonPath)) {
  console.error("FAIL: bhagavad_gita_chapters.json does not exist!");
  process.exit(1);
}

const gitaJson = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const chapters = gitaJson.chapters;
console.log(`PASS: Found ${chapters.length} chapters in bhagavad_gita_chapters.json.`);
if (chapters.length !== 18) {
  console.error("FAIL: Expected 18 chapters, got " + chapters.length);
  process.exit(1);
}

let totalVerses = 0;
chapters.forEach(c => {
  totalVerses += c.verses_count;
  if (!c.chapter_number || !c.name || !c.summary || !c.key_shlokas || c.key_shlokas.length === 0) {
    console.error(`FAIL: Chapter ${c.chapter_number} has missing fields!`);
    process.exit(1);
  }
});
console.log(`PASS: All 18 chapters validated. Total verses counted: ${totalVerses} (Standard Gita = 700/701 verses).`);

// 2. Setup mock browser DOM environment
global.window = global;
function makeElement(id) {
  return {
    id: id || '',
    style: {},
    innerHTML: '',
    children: [],
    classList: {
      add: () => {},
      remove: () => {},
      toggle: () => {},
      contains: () => false
    },
    querySelector: () => null,
    querySelectorAll: () => [],
    addEventListener: () => {},
    focus: () => {},
    setAttribute: () => {},
    appendChild: function(child) { this.children.push(child); }
  };
}

global.document = {
  addEventListener: () => {},
  getElementById: (id) => makeElement(id),
  querySelector: () => makeElement(''),
  querySelectorAll: () => [],
  createElement: (tag) => makeElement(tag),
  body: {
    style: {},
    appendChild: () => {}
  }
};
global.navigator = { userAgent: 'node' };
global.Audio = function() {
  return {
    play: () => Promise.resolve(),
    pause: () => {},
    currentTime: 0,
    paused: true
  };
};

// 3. Load gita_engine.js
try {
  require('./gita_engine.js');
  console.log("PASS: gita_engine.js loaded successfully into mock environment.");
} catch (e) {
  console.error("FAIL loading gita_engine.js:", e);
  process.exit(1);
}

// 4. Test methods
if (typeof window.openGitaChapterModal !== 'function') {
  console.error("FAIL: window.openGitaChapterModal is not a function!");
  process.exit(1);
}
if (typeof window.openGitaChapterReader !== 'function') {
  console.error("FAIL: window.openGitaChapterReader is not a function!");
  process.exit(1);
}
if (typeof window.renderFullGitaPage !== 'function') {
  console.error("FAIL: window.renderFullGitaPage is not a function!");
  process.exit(1);
}

console.log("Testing openGitaChapterModal(1)...");
window.openGitaChapterModal(1);
console.log("PASS: openGitaChapterModal(1) executed without error.");

console.log("Testing openGitaChapterReader(1)...");
window.openGitaChapterReader(1);
console.log("PASS: openGitaChapterReader(1) executed without error.");

console.log("Testing openGitaChapterReader(18)...");
window.openGitaChapterReader(18);
console.log("PASS: openGitaChapterReader(18) executed without error.");

console.log("Testing renderFullGitaPage('all', '')...");
window.renderFullGitaPage('all', '');
console.log("PASS: renderFullGitaPage('all', '') executed without error.");

console.log("Testing renderFullGitaPage('bhakti', 'भक्तियोग')...");
window.renderFullGitaPage('bhakti', 'भक्तियोग');
console.log("PASS: renderFullGitaPage with filters executed without error.");

console.log("Testing openGitaJumperModal()...");
window.openGitaJumperModal();
console.log("PASS: openGitaJumperModal executed without error.");

console.log("\n>>> ALL UNIT AND INTEGRATION TESTS PASSED SUCCESSFULLY! 🚀");
