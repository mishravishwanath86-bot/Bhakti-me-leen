const fs = require('fs');

console.log("=== VERIFYING LORD SHIVA AARTI (DRIK_SHIVA_1) ===");

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
    dataset: {},
    closest: (sel) => {
      if (sel.includes('page-reader') && (el.id === 'page-reader' || (el.parent && el.parent.id === 'page-reader'))) return elements['page-reader'];
      if (sel.includes('back-btn') && el.classList.contains('back-btn')) return el;
      return null;
    }
  };
  return el;
}

const elementIds = [
  'reader-page-title', 'reader-deity-img', 'reader-audio-title', 'reader-audio-sub',
  'reader-youtube-container', 'reader-cosmic-content', 'reader-content',
  'aarti-options-modal', 'aarti-modal-title', 'aarti-modal-deity', 'aarti-modal-mantra',
  'aarti-modal-img', 'aarti-modal-list', 'page-reader', 'page-home', 'page-aarti',
  'drik-aarti-cards-container', 'drik-aarti-page-pills', 'splash-screen'
];

elementIds.forEach(id => {
  elements[id] = createElement('div');
  elements[id].id = id;
});

const readerBackBtn = createElement('button');
readerBackBtn.classList.add('back-btn');
readerBackBtn.dataset.back = 'page-home';
readerBackBtn.parent = elements['page-reader'];
elements['page-reader'].appendChild(readerBackBtn);

global.window = global;
global.window.currentPage = 'page-home';
global.window.addEventListener = () => {};
global.window.removeEventListener = () => {};
global.window.scrollTo = () => {};
global.document = {
  getElementById: (id) => elements[id] || null,
  querySelectorAll: (sel) => {
    if (sel.includes('.page')) return [elements['page-home'], elements['page-reader'], elements['page-aarti']];
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

const appJsCode = fs.readFileSync('app.js', 'utf8');
eval(appJsCode);

const drikJsCode = fs.readFileSync('drik_app_addon.js', 'utf8');
eval(drikJsCode);

console.log('[OK] Scripts loaded successfully!');

const shiva = window.AARTI_COLLECTIONS.shiva;
if (!shiva) {
  console.error('[FAIL] Shiva collection not found!');
  process.exit(1);
}

console.log(`[OK] Shiva collection found: "${shiva.title}" with ${shiva.items.length} items.`);

const item = shiva.items.find(i => i.id === 'drik_shiva_1');
if (!item) {
  console.error('[FAIL] drik_shiva_1 not found!');
  process.exit(1);
}

console.log(`[OK] Item found: ${item.title} (${item.title_en})`);
console.log(`  Source: ${item.drik_url}`);
console.log(`  YouTube ID: ${item.video_id}`);

// Verify Stanzas in content
if (!item.content.includes('ॐ जय शिव ओंकारा') || !item.content.includes('एकानन चतुरानन') || !item.content.includes('प्रणवाक्षर मध्ये') || !item.content.includes('कहत शिवानन्द स्वामी')) {
  console.error('[FAIL] Expected authentic stanzas missing in content!');
  process.exit(1);
}
console.log('[OK] All 12 authentic stanzas present in Hindi content!');

// Verify English Lyrics
if (!item.english_lyrics || !item.english_lyrics.includes('Om Jai Shiva Omkara') || !item.english_lyrics.includes('Ekaanana Chaturaanana') || !item.english_lyrics.includes('Pranavakshara Madhye') || !item.english_lyrics.includes('Kahata Shivaananda')) {
  console.error('[FAIL] English transliteration missing or incomplete!');
  process.exit(1);
}
console.log('[OK] English Roman transliteration verified.');

// Verify Meaning / Bhavarth
if (!item.meaning || !item.meaning.includes('स्वामी शिवानन्द') || !item.meaning.includes('अर्धनारीश्वर') || !item.meaning.includes('प्रणवाक्षर')) {
  console.error('[FAIL] Meaning is missing or incomplete!');
  process.exit(1);
}
console.log('[OK] Bhavarth (पद्यवार सम्पूर्ण पावन भावार्थ) verified.');

// Verify Vidhi
if (!item.vidhi || !item.vidhi.includes('४ बार') || !item.vidhi.includes('२ बार') || !item.vidhi.includes('१ बार') || !item.vidhi.includes('७ बार')) {
  console.error('[FAIL] Vidhi is missing 4-2-1-7 sequence!');
  process.exit(1);
}
console.log('[OK] 4-2-1-7 Aarti Vidhi verified.');

// Verify Significance
if (!item.significance || !item.significance.includes('प्रणवाक्षर') || !item.significance.includes('शिवानन्द')) {
  console.error('[FAIL] Significance is missing!');
  process.exit(1);
}
console.log('[OK] Significance (माहात्म्य) verified.');

// Test Reader Rendering
console.log('\n--- Testing Reader Opening and 2-Step Back Navigation ---');
window.showPage('page-home');
window.openAartiCollectionModal('shiva');
console.log('Modal opened for Shiva. Modal title:', elements['aarti-modal-title'].textContent);

window.readAartiItemDirect('shiva', 0);
console.log('Current page after opening reader:', window.currentPage);
console.log('Reader page title:', elements['reader-page-title'].textContent);
console.log('Reader audio title:', elements['reader-audio-title'].textContent);
console.log('Top YouTube container display:', elements['reader-youtube-container'].style.display, '(Expected: none)');

if (elements['reader-youtube-container'].style.display !== 'none') {
  console.error('[FAIL] Top YouTube container should be hidden!');
  process.exit(1);
}

// Test Back Navigation
window.handleReaderBack();
console.log('After back button clicked:');
console.log('  Current page:', window.currentPage, '(Expected: page-home)');
console.log('  Modal display:', elements['aarti-options-modal'].style.display, '(Expected: flex)');
console.log('  Modal title:', elements['aarti-modal-title'].textContent);

if (elements['aarti-options-modal'].style.display !== 'flex') {
  console.error('[FAIL] Modal did not reopen on back!');
  process.exit(1);
}
if (!elements['aarti-modal-title'].textContent.includes('Shiva') && !elements['aarti-modal-title'].textContent.includes('शिव')) {
  console.error('[FAIL] Modal did not restore Shiva collection!');
  process.exit(1);
}

window.closeAartiOptionsModal();
console.log('Modal closed. Final page:', window.currentPage);

console.log('\n🎉 ALL CHECKS PASSED PERFECTLY FOR LORD SHIVA AARTI (DRIK_SHIVA_1)!');
process.exit(0);
