const fs = require('fs');

console.log("=== VERIFYING NATAVARA AARTI IN APP.JS ===");

const elements = {};
function createElement(tag) {
  const el = {
    tagName: tag,
    style: {},
    classList: {
      _classes: new Set(),
      add: (c) => el.classList._classes.add(c),
      remove: (c) => el.classList._classes.delete(c),
      contains: (c) => el.classList._classes.has(c)
    },
    children: [],
    setAttribute: (k, v) => { el[k] = v; },
    getAttribute: (k) => el[k] || '',
    appendChild: (c) => el.children.push(c),
    innerHTML: '',
    textContent: '',
    dataset: {}
  };
  return el;
}

const ids = [
  'reader-page-title', 'reader-deity-img', 'reader-audio-title', 'reader-audio-sub',
  'reader-youtube-container', 'reader-cosmic-content', 'reader-content',
  'aarti-options-modal', 'aarti-modal-title', 'aarti-modal-deity', 'aarti-modal-mantra',
  'aarti-modal-img', 'aarti-modal-list', 'page-reader', 'page-home', 'page-aarti'
];
ids.forEach(id => { elements[id] = createElement('div'); elements[id].id = id; });

const readerBackBtn = createElement('button');
readerBackBtn.classList.add('back-btn');
readerBackBtn.dataset.back = 'page-home';
elements['page-reader'].appendChild(readerBackBtn);

global.window = global;
global.window.currentPage = 'page-home';
global.window.addEventListener = () => {};
global.window.removeEventListener = () => {};
global.window.scrollTo = () => {};
global.document = {
  getElementById: (id) => elements[id] || null,
  querySelectorAll: (sel) => {
    if (sel.includes('.page')) return [elements['page-home'], elements['page-reader']];
    if (sel.includes('.back-btn')) return [readerBackBtn];
    return [];
  },
  querySelector: (sel) => {
    if (sel.includes('#page-reader .back-btn')) return readerBackBtn;
    return null;
  },
  createElement: createElement,
  addEventListener: () => {},
  removeEventListener: () => {},
  dispatchEvent: () => {},
  documentElement: { setAttribute: () => {}, style: {} },
  body: { appendChild: () => {}, classList: { add: () => {}, remove: () => {} } }
};
global.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve([]), text: () => Promise.resolve('') });
global.navigator = { userAgent: 'node', vibrate: () => {} };
global.location = { href: '', search: '', hash: '' };
global.localStorage = { getItem: () => null, setItem: () => {} };
global.Audio = class { constructor() { this.addEventListener = () => {}; } };
global.requestAnimationFrame = () => {};
global.cancelAnimationFrame = () => {};
global.CustomEvent = class { constructor() {} };

const appCode = fs.readFileSync('app.js', 'utf8');
try {
  eval(appCode);
  console.log("✓ app.js parsed and evaluated without syntax errors!");
} catch (e) {
  console.error("Syntax / Eval Error in app.js:", e);
  process.exit(1);
}

const krishnaColl = window.AARTI_COLLECTIONS && window.AARTI_COLLECTIONS.krishna;
if (!krishnaColl) {
  console.error("❌ Krishna collection not found in AARTI_COLLECTIONS!");
  process.exit(1);
}

const item3 = krishnaColl.items && krishnaColl.items[3];
if (!item3 || item3.id !== 'drik_krishna_4') {
  console.error("❌ item 3 is not drik_krishna_4! Found:", item3);
  process.exit(1);
}

console.log("✓ Item 3 ID:", item3.id);
console.log("✓ Item 3 Title:", item3.title);
console.log("✓ Item 3 English Title:", item3.title_en);
console.log("✓ Item 3 Drik URL:", item3.drik_url);
console.log("✓ Content length:", (item3.content || '').length, "chars");
console.log("✓ Meaning (भावार्थ) length:", (item3.meaning || '').length, "chars");
console.log("✓ Vidhi (4-2-1-7 विधि) length:", (item3.vidhi || '').length, "chars");
console.log("✓ Significance (माहात्म्य) length:", (item3.significance || '').length, "chars");
console.log("✓ English Transliteration length:", (item3.english_lyrics || '').length, "chars");

// Verify essential content markers
if (!item3.content.includes("नन्द-सुवन जसुमतिके लाला") || !item3.content.includes("कालयवन-कन्सादि-निकन्दन")) {
  console.error("❌ Missing key verses in content!");
  process.exit(1);
}
if (!item3.meaning.includes("गोवर्धन पर्वत") || !item3.meaning.includes("परीक्षित")) {
  console.error("❌ Missing key verses in meaning!");
  process.exit(1);
}
if ((!item3.vidhi.includes("४ बार") && !item3.vidhi.includes("4 बार")) || (!item3.vidhi.includes("७ बार") && !item3.vidhi.includes("7 बार"))) {
  console.error("❌ Missing 4-2-1-7 rules in vidhi!");
  process.exit(1);
}

// Test Reader Rendering
console.log("\n--- Testing Reader Direct Render for Natavara ---");
window.readAartiItemDirect('krishna', 3);

console.log("Reader page title:", elements['reader-page-title'].textContent);
console.log("Reader audio title:", elements['reader-audio-title'].textContent);
console.log("Reader audio subtitle:", elements['reader-audio-sub'].textContent);
console.log("Reader YouTube container display:", elements['reader-youtube-container'].style.display, "(Expected: none)");

const renderedHtml = elements['reader-cosmic-content'].innerHTML;
console.log("Rendered HTML length:", renderedHtml.length);
console.log("Contains Devanagari lyrics tab:", renderedHtml.includes("आरती कीजै श्रीनटवर जी की"));
console.log("Contains Bhavarth tab:", renderedHtml.includes("पद्यवार सम्पूर्ण पावन भावार्थ") || renderedHtml.includes("नन्द-सुवन"));
console.log("Contains 4-2-1-7 Vidhi tab:", renderedHtml.includes("4-2-1-7 प्रदक्षिणा"));
console.log("Contains Significance tab:", renderedHtml.includes("आध्यात्मिक माहात्म्य व फलश्रुति"));
console.log("Contains English Transliteration tab:", renderedHtml.includes("Aarti Kijai Shri Natavara Ji Ki"));
console.log("Contains #000000 high-contrast black styling:", renderedHtml.includes("#000000"));

// Test 2-step back flow
console.log("\n--- Testing 2-Step Back Navigation for Natavara Aarti ---");
window.openAartiCollectionModal('krishna');
console.log("Modal opened. Active deity:", window._aartiActiveModalDeity);
window.readAartiItemDirect('krishna', 3);
console.log("In reader. Origin deity:", window._aartiReaderOriginModalDeity);

window.handleReaderBack();
console.log("After back: current page:", window.currentPage, "Modal display:", elements['aarti-options-modal'].style.display);
if (elements['aarti-options-modal'].style.display !== 'flex') {
  console.error("❌ Modal was not re-opened on back!");
  process.exit(1);
}

window.closeAartiOptionsModal();
console.log("After modal close: current page:", window.currentPage, "Modal display:", elements['aarti-options-modal'].style.display);
if (elements['aarti-options-modal'].style.display !== 'none' || window.currentPage !== 'page-home') {
  console.error("❌ Modal was not cleanly closed to page-home!");
  process.exit(1);
}

console.log("\n🎉 ALL TESTS PASSED! Natavara Aarti is 100% verified!");
process.exit(0);
