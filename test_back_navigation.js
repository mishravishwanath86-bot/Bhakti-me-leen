const fs = require('fs');

console.log("=== TESTING 2-STEP BACK NAVIGATION FLOW ===");

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

// Load app.js and drik_app_addon.js
const appJsCode = fs.readFileSync('app.js', 'utf8');
eval(appJsCode);

const drikJsCode = fs.readFileSync('drik_app_addon.js', 'utf8');
eval(drikJsCode);

console.log("Scripts loaded successfully!");

// TEST 1: Home page (Image 3) -> Modal (Image 2) -> Reader (Image 1) -> Back to Modal (Image 2) -> Close to Home (Image 3)
console.log("\n[TEST 1] Standard flow from Home Page:");
window.showPage('page-home');
console.log("Initial page:", window.currentPage);

console.log("Step 1: User clicks Ganesha Aarti card on Home Page (Image 3)");
window.openAartiCollectionModal('ganesh');
const modal = elements['aarti-options-modal'];
console.log("  Modal display:", modal.style.display, "(Expected: flex)");
console.log("  Modal title:", elements['aarti-modal-title'].textContent);
if (modal.style.display !== 'flex') throw new Error("Modal failed to open!");

console.log("Step 2: User clicks 'जय गणेश जय गणेश देवा' inside Modal (Image 2)");
window.readAartiItemDirect('ganesh', 0);
console.log("  Current page:", window.currentPage, "(Expected: page-reader)");
console.log("  Modal display:", modal.style.display, "(Expected: none)");
console.log("  Reader title:", elements['reader-page-title'].textContent);
if (window.currentPage !== 'page-reader') throw new Error("Did not navigate to reader!");
if (modal.style.display !== 'none') throw new Error("Modal not hidden in reader!");

console.log("Step 3: User clicks Back Button (❮) on Reader (Image 1)");
window.handleReaderBack();
console.log("  Current page:", window.currentPage, "(Expected: page-home)");
console.log("  Modal display:", modal.style.display, "(Expected: flex)");
console.log("  Modal title:", elements['aarti-modal-title'].textContent);
if (modal.style.display !== 'flex') throw new Error("Modal was NOT re-opened on back!");
if (!elements['aarti-modal-title'].textContent.includes('Ganesha')) throw new Error("Modal did not restore Ganesha collection!");

console.log("Step 4: User clicks Close (✕) on Modal (Image 2)");
window.closeAartiOptionsModal();
console.log("  Modal display:", modal.style.display, "(Expected: none)");
console.log("  Current page:", window.currentPage, "(Expected: page-home)");
if (modal.style.display !== 'none') throw new Error("Modal was not closed!");
if (window.currentPage !== 'page-home') throw new Error("User did not return to page-home!");

console.log("✓ TEST 1 PASSED PERFECTLY!");

// TEST 2: Deity Switching inside Modal
console.log("\n[TEST 2] Switching deity inside Modal:");
window.showPage('page-home');
window.openAartiCollectionModal('ganesh');
console.log("Switched to Hanuman pill inside modal:");
window.openAartiCollectionModal('hanuman');
console.log("  Modal title:", elements['aarti-modal-title'].textContent);
window.readAartiItemDirect('hanuman', 0);
console.log("  Current page in reader:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('Hanuman')) throw new Error("Modal did not restore Hanuman collection!");

window.closeAartiOptionsModal();
console.log("  Closed to:", window.currentPage);
console.log("✓ TEST 2 PASSED PERFECTLY!");

// TEST 3: Origin from 'page-aarti' (All Aartis page)
console.log("\n[TEST 3] Opening from All Aartis page (page-aarti):");
window.showPage('page-aarti');
window.openAartiCollectionModal('ganesh');
window.readAartiItemDirect('ganesh', 1);
console.log("  Reader opened. Audio title:", elements['reader-audio-title'].textContent);
console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("Clicking Close on Modal:");
window.closeAartiOptionsModal();
console.log("  Returned to:", window.currentPage, "(Expected: page-aarti)");
if (window.currentPage !== 'page-aarti') throw new Error("Should return to page-aarti!");
console.log("✓ TEST 3 PASSED PERFECTLY!");

// TEST 4: Opening Shiva Collection Modal and selecting drik_shiva_3 (Lord Shankara Aarti)
console.log("\n[TEST 4] Opening Shiva Collection -> drik_shiva_3 (जयति जयति जग-निवास):");
window.showPage('page-home');
window.openAartiCollectionModal('shiva');
console.log("  Shiva modal open display:", modal.style.display);
console.log("  Shiva modal title:", elements['aarti-modal-title'].textContent);

// Read drik_shiva_3 directly (index 2)
window.readAartiItemDirect('shiva', 2);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जयति जयति जग-निवास')) {
  throw new Error("Reader audio title does not match Shankara Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('अशरण जन नित्य शरण')) {
  throw new Error("Reader cosmic content does not contain stanza 8 of Shankara Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics, hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('शिव')) {
  throw new Error("Modal did not restore Shiva collection!");
}
window.closeAartiOptionsModal();
console.log("✓ TEST 4 (SHIVA - SHANKARA AARTI) PASSED PERFECTLY!");

// TEST 5: Opening Shiva Collection Modal and selecting drik_shiva_4 (Lord Gangadhara Aarti)
console.log("\n[TEST 5] Opening Shiva Collection -> drik_shiva_4 (ॐ जय गंगाधर):");
window.showPage('page-home');
window.openAartiCollectionModal('shiva');
console.log("  Shiva modal open display:", modal.style.display);
console.log("  Shiva modal title:", elements['aarti-modal-title'].textContent);

// Read drik_shiva_4 directly (index 3)
window.readAartiItemDirect('shiva', 3);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('ॐ जय गंगाधर')) {
  throw new Error("Reader audio title does not match Gangadhara Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शिवसायुज्यं गच्छति')) {
  throw new Error("Reader cosmic content does not contain stanza 9 (phalasruti) of Gangadhara Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics, hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('शिव')) {
  throw new Error("Modal did not restore Shiva collection!");
}
window.closeAartiOptionsModal();
console.log("✓ TEST 5 (SHIVA - GANGADHARA AARTI) PASSED PERFECTLY!");

// TEST 6: Opening Shiva Collection Modal and selecting drik_shiva_5 (Lord Kailasavasi Aarti)
console.log("\n[TEST 6] Opening Shiva Collection -> drik_shiva_5 (शीश गंग अर्धन्ग पार्वती):");
window.showPage('page-home');
window.openAartiCollectionModal('shiva');
console.log("  Shiva modal open display:", modal.style.display);
console.log("  Shiva modal title:", elements['aarti-modal-title'].textContent);

// Read drik_shiva_5 directly (index 4)
window.readAartiItemDirect('shiva', 4);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('शीश गंग अर्धन्ग पार्वती')) {
  throw new Error("Reader audio title does not match Kailasavasi Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('किंकरकी विनती सुनियो')) {
  throw new Error("Reader cosmic content does not contain stanza 10 of Kailasavasi Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (10 stanzas), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('शिव')) {
  throw new Error("Modal did not restore Shiva collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 6 (SHIVA - KAILASAVASI AARTI) PASSED PERFECTLY!");

// TEST 7: Opening Narayana Collection Modal and selecting drik_narayana_1 (Om Jai Jagdish Hare)
console.log("\n[TEST 7] Opening Narayana Collection -> drik_narayana_1 (ॐ जय जगदीश हरे):");
window.showPage('page-home');
window.openAartiCollectionModal('narayana');
console.log("  Narayana modal open display:", modal.style.display);
console.log("  Narayana modal title:", elements['aarti-modal-title'].textContent);

// Read drik_narayana_1 directly (index 0)
window.readAartiItemDirect('narayana', 0);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('ॐ जय जगदीश हरे')) {
  throw new Error("Reader audio title does not match Jagdish Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('कहत शिवानन्द स्वामी')) {
  throw new Error("Reader cosmic content does not contain stanza 8 (phalasruti) of Jagdish Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('विषय-विकार मिटाओ')) {
  throw new Error("Reader cosmic content does not contain stanza 7 of Jagdish Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 8 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('नारायण')) {
  throw new Error("Modal did not restore Narayana collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 7 (NARAYANA - OM JAI JAGDISH HARE) PASSED PERFECTLY!");

// TEST 8: Opening Narayana Collection Modal and selecting drik_narayana_2 (Shri Lakshminarayana Aarti)
console.log("\n[TEST 8] Opening Narayana Collection -> drik_narayana_2 (जय लक्ष्मी-विष्णो, जय लक्ष्मीनारायण):");
window.showPage('page-home');
window.openAartiCollectionModal('narayana');
console.log("  Narayana modal open display:", modal.style.display);
console.log("  Narayana modal title:", elements['aarti-modal-title'].textContent);

// Read drik_narayana_2 directly (index 1)
window.readAartiItemDirect('narayana', 1);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जय लक्ष्मी-विष्णो')) {
  throw new Error("Reader audio title does not match Lakshminarayana Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('जय चम्पा सम-वर्णे')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Lakshminarayana Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('नव-मन्गल दाता')) {
  throw new Error("Reader cosmic content does not contain stanza 7 of Lakshminarayana Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 7 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('नारायण')) {
  throw new Error("Modal did not restore Narayana collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 8 (NARAYANA - LAKSHMINARAYANA AARTI) PASSED PERFECTLY!");

// TEST 9: Opening Narayana Collection Modal and selecting drik_narayana_3 (Lord Badarinatha Aarti)
console.log("\n[TEST 9] Opening Narayana Collection -> drik_narayana_3 (जय जय श्री बदरीनाथ):");
window.showPage('page-home');
window.openAartiCollectionModal('narayana');
console.log("  Narayana modal open display:", modal.style.display);
console.log("  Narayana modal title:", elements['aarti-modal-title'].textContent);

// Read drik_narayana_3 directly (index 2)
window.readAartiItemDirect('narayana', 2);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जय जय श्री बदरीनाथ')) {
  throw new Error("Reader audio title does not match Badarinatha Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('मेघवर्ण अति अनूप')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Badarinatha Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('विनवत श्यामा हमेश')) {
  throw new Error("Reader cosmic content does not contain stanza 5 of Badarinatha Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 5 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('नारायण')) {
  throw new Error("Modal did not restore Narayana collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 9 (NARAYANA - BADARINATHA AARTI) PASSED PERFECTLY!");

// TEST 10: Opening Narayana Collection Modal and selecting drik_narayana_4 (Lord Satyanarayana Aarti)
console.log("\n[TEST 10] Opening Narayana Collection -> drik_narayana_4 (जय लक्ष्मीरमणा श्री जय लक्ष्मीरमणा):");
window.showPage('page-home');
window.openAartiCollectionModal('narayana');
console.log("  Narayana modal open display:", modal.style.display);
console.log("  Narayana modal title:", elements['aarti-modal-title'].textContent);

// Read drik_narayana_4 directly (index 3)
window.readAartiItemDirect('narayana', 3);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जय लक्ष्मीरमणा')) {
  throw new Error("Reader audio title does not match Satyanarayana Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('रत्नजड़ित सिंहासन')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Satyanarayana Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('चढ़त प्रसाद सवाया')) {
  throw new Error("Reader cosmic content does not contain stanza 7 of Satyanarayana Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 8 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('नारायण')) {
  throw new Error("Modal did not restore Narayana collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 10 (NARAYANA - SATYANARAYANA AARTI) PASSED PERFECTLY!");

// TEST 11: Opening Narayana Collection Modal and selecting drik_narayana_5 (Lord Purushottam Aarti)
console.log("\n[TEST 11] Opening Narayana Collection -> drik_narayana_5 (जय पुरुषोत्तम देवा):");
window.showPage('page-home');
window.openAartiCollectionModal('narayana');
console.log("  Narayana modal open display:", modal.style.display);
console.log("  Narayana modal title:", elements['aarti-modal-title'].textContent);

// Read drik_narayana_5 directly (index 4)
window.readAartiItemDirect('narayana', 4);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जय पुरुषोत्तम देवा')) {
  throw new Error("Reader audio title does not match Purushottam Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('मेधावी मुनि कन्या')) {
  throw new Error("Reader cosmic content does not contain stanza 3 (Medhavi muni kanya) of Purushottam Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शूद्र मणीग्रिव पापी')) {
  throw new Error("Reader cosmic content does not contain stanza 6 (Manigriva) of Purushottam Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('प्रभुदास भव नद से')) {
  throw new Error("Reader cosmic content does not contain stanza 7 (Phalasruti) of Purushottam Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 7 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('नारायण')) {
  throw new Error("Modal did not restore Narayana collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 11 (NARAYANA - PURUSHOTTAM AARTI) PASSED PERFECTLY!");

// TEST 12: Opening Durga Collection Modal and selecting drik_goddesses_1 (Ambe Mata Aarti)
console.log("\n[TEST 12] Opening Durga Collection -> drik_goddesses_1 (जय अम्बे गौरी):");
window.showPage('page-home');
window.openAartiCollectionModal('durga');
console.log("  Durga modal open display:", modal.style.display);
console.log("  Durga modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_1 directly (index 0)
window.readAartiItemDirect('durga', 0);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जय अम्बे गौरी')) {
  throw new Error("Reader audio title does not match Ambe Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शुम्भ-निशुम्भ बिदारे')) {
  throw new Error("Reader cosmic content does not contain stanza 5 of Ambe Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('चौंसठ योगिनी मंगल गावत')) {
  throw new Error("Reader cosmic content does not contain stanza 8 of Ambe Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('कहत शिवानन्द स्वामी')) {
  throw new Error("Reader cosmic content does not contain stanza 12 of Ambe Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 12 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('दुर्गा')) {
  throw new Error("Modal did not restore Durga collection!");
}
console.log("✓ TEST 12 (DURGA - AMBE MATA AARTI) PASSED PERFECTLY!");

// TEST 13: Opening Durga Collection Modal and selecting drik_goddesses_5 (Vaishno Mata Aarti)
console.log("\n[TEST 13] Opening Durga Collection -> drik_goddesses_5 (जय वैष्णवी माता):");
window.showPage('page-home');
window.openAartiCollectionModal('durga');
console.log("  Durga modal open display:", modal.style.display);
console.log("  Durga modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_5 directly (index 1)
window.readAartiItemDirect('durga', 1);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('जय वैष्णवी माता')) {
  throw new Error("Reader audio title does not match Vaishno Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शीश पे छत्र विराजे')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Vaishno Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('सुन्दर गुफा तुम्हारी')) {
  throw new Error("Reader cosmic content does not contain stanza 3 of Vaishno Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('कहते सेवक ध्यानू')) {
  throw new Error("Reader cosmic content does not contain stanza 7 (Dhyanu Bhagat) of Vaishno Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 7 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('दुर्गा')) {
  throw new Error("Modal did not restore Durga collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 13 (DURGA - VAISHNO MATA AARTI) PASSED PERFECTLY!");

// TEST 14: Opening Durga Collection Modal and selecting drik_goddesses_8 (Durga Mata Aarti / अम्बे तू है जगदम्बे काली)
console.log("\n[TEST 14] Opening Durga Collection -> drik_goddesses_8 (अम्बे तू है जगदम्बे काली):");
window.showPage('page-home');
window.openAartiCollectionModal('durga');
console.log("  Durga modal open display:", modal.style.display);
console.log("  Durga modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_8 directly (index 2)
window.readAartiItemDirect('durga', 2);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('दुर्गा माता') && !elements['reader-audio-title'].textContent.includes('अम्बे तू है जगदम्बे')) {
  throw new Error("Reader audio title does not match Durga Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('अम्बे तू है जगदम्बे काली')) {
  throw new Error("Reader cosmic content does not contain refrain of Durga Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('तेरे भक्त जनो पर माता')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Durga Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('पूत-कपूत सुने है')) {
  throw new Error("Reader cosmic content does not contain stanza 2 of Durga Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('नहीं मांगते धन और दौलत')) {
  throw new Error("Reader cosmic content does not contain stanza 3 of Durga Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('चरण शरण में खड़े तुम्हारी')) {
  throw new Error("Reader cosmic content does not contain stanza 4 of Durga Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 4 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('दुर्गा')) {
  throw new Error("Modal did not restore Durga collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 14 (DURGA - AMBE TU HAI JAGDAMBE KALI) PASSED PERFECTLY!");

// TEST 15: Opening Durga Collection Modal and selecting drik_goddesses_11 (Parvati Mata Aarti / जय पार्वती माता)
console.log("\n[TEST 15] Opening Durga Collection -> drik_goddesses_11 (जय पार्वती माता):");
window.showPage('page-home');
window.openAartiCollectionModal('durga');
console.log("  Durga modal open display:", modal.style.display);
console.log("  Durga modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_11 directly (index 3)
window.readAartiItemDirect('durga', 3);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('पार्वती माता') && !elements['reader-audio-title'].textContent.includes('जय पार्वती माता')) {
  throw new Error("Reader audio title does not match Parvati Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('ब्रह्म सनातन देवी')) {
  throw new Error("Reader cosmic content does not contain refrain of Parvati Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('अरिकुल पद्म विनाशिनि')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Parvati Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('सतयुग रूपशील अतिसुन्दर')) {
  throw new Error("Reader cosmic content does not contain stanza 3 of Parvati Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शुम्भ निशुम्भ विदारे')) {
  throw new Error("Reader cosmic content does not contain stanza 4 of Parvati Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('श्री प्रताप आरती मैया की')) {
  throw new Error("Reader cosmic content does not contain stanza 7 of Parvati Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 7 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('दुर्गा')) {
  throw new Error("Modal did not restore Durga collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 15 (DURGA - PARVATI MATA AARTI) PASSED PERFECTLY!");

// TEST 16: Opening Durga Collection Modal and selecting drik_goddesses_12 (Lalita Mata Aarti / श्री मातेश्वरी जय त्रिपुरेश्वरी)
console.log("\n[TEST 16] Opening Durga Collection -> drik_goddesses_12 (श्री मातेश्वरी जय त्रिपुरेश्वरी):");
window.showPage('page-home');
window.openAartiCollectionModal('durga');
console.log("  Durga modal open display:", modal.style.display);
console.log("  Durga modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_12 directly (index 4)
window.readAartiItemDirect('durga', 4);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('ललिता माता') && !elements['reader-audio-title'].textContent.includes('श्री मातेश्वरी जय त्रिपुरेश्वरी')) {
  throw new Error("Reader audio title does not match Lalita Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('श्री मातेश्वरी जय त्रिपुरेश्वरी')) {
  throw new Error("Reader cosmic content does not contain refrain of Lalita Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('करुणामयी सकल अघ हारिणी')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Lalita Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('भण्डासुर वधकारिणी')) {
  throw new Error("Reader cosmic content does not contain stanza 3 (Bhandasura) of Lalita Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('भव भय हारिणी, कष्ट निवारिणी')) {
  throw new Error("Reader cosmic content does not contain stanza 4 of Lalita Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('जय त्रिपुर सुन्दरी नमो नमः')) {
  throw new Error("Reader cosmic content does not contain stanza 5 (Tripura Sundari) of Lalita Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 5 पद + समापन), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('दुर्गा')) {
  throw new Error("Modal did not restore Durga collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 16 (DURGA - LALITA MATA AARTI) PASSED PERFECTLY!");

// TEST 17: Opening Lakshmi Collection Modal and selecting drik_goddesses_2 (Lakshmi Mata Aarti / ॐ जय लक्ष्मी माता)
console.log("\n[TEST 17] Opening Lakshmi Collection -> drik_goddesses_2 (ॐ जय लक्ष्मी माता):");
window.showPage('page-home');
window.openAartiCollectionModal('lakshmi');
console.log("  Lakshmi modal open display:", modal.style.display);
console.log("  Lakshmi modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_2 directly (index 0)
window.readAartiItemDirect('lakshmi', 0);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('लक्ष्मी माता') && !elements['reader-audio-title'].textContent.includes('ॐ जय लक्ष्मी माता')) {
  throw new Error("Reader audio title does not match Lakshmi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('ॐ जय लक्ष्मी माता')) {
  throw new Error("Reader cosmic content does not contain refrain of Lakshmi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('उमा, रमा, ब्रह्माणी')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Lakshmi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('तुम पाताल-निवासिनि')) {
  throw new Error("Reader cosmic content does not contain stanza 3 of Lakshmi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शुभ-गुण मन्दिर सुन्दर')) {
  throw new Error("Reader cosmic content does not contain stanza 6 of Lakshmi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('महालक्ष्मीजी की आरती')) {
  throw new Error("Reader cosmic content does not contain stanza 7 (Phalasruti) of Lakshmi Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 7 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('लक्ष्मी')) {
  throw new Error("Modal did not restore Lakshmi collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 17 (LAKSHMI - OM JAI LAKSHMI MATA) PASSED PERFECTLY!");

console.log("\n[TEST 18] Opening Lakshmi Collection -> drik_goddesses_9 (जय अहोई माता, जय अहोई माता):");
window.openAartiCollectionModal('lakshmi');
console.log("  Lakshmi modal open display:", modal.style.display);
console.log("  Lakshmi modal title:", elements['aarti-modal-title'].textContent);

// Read drik_goddesses_9 directly (index 1 in lakshmi collection)
window.readAartiItemDirect('lakshmi', 1);
console.log("  Reader opened page:", window.currentPage);
console.log("  Reader audio title:", elements['reader-audio-title'].textContent);
if (!elements['reader-audio-title'].textContent.includes('अहोई माता') && !elements['reader-audio-title'].textContent.includes('जय अहोई माता')) {
  throw new Error("Reader audio title does not match Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('जय अहोई माता')) {
  throw new Error("Reader cosmic content does not contain refrain of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('ब्रह्माणी, रुद्राणी, कमला')) {
  throw new Error("Reader cosmic content does not contain stanza 1 of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('माता रूप निरंजन')) {
  throw new Error("Reader cosmic content does not contain stanza 2 of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('तू ही पाताल बसंती')) {
  throw new Error("Reader cosmic content does not contain stanza 3 of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('जिस घर थारो वासा')) {
  throw new Error("Reader cosmic content does not contain stanza 4 of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('न कोई पुत्र पाता')) {
  throw new Error("Reader cosmic content does not contain stanza 5 of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('शुभ गुण सुंदर युक्ता')) {
  throw new Error("Reader cosmic content does not contain stanza 6 of Ahoi Mata Aarti!");
}
if (!elements['reader-cosmic-content'].innerHTML.includes('श्री अहोई माँ की आरती')) {
  throw new Error("Reader cosmic content does not contain stanza 7 (Phalasruti) of Ahoi Mata Aarti!");
}
if (elements['reader-youtube-container'].style.display !== 'none') {
  throw new Error("Top video container should be hidden (display: none)!");
}
console.log("  Reader verified: full Devanagari lyrics (टेक + 7 पद), hidden video container.");

console.log("Clicking Back from Reader:");
window.handleReaderBack();
console.log("  Modal re-opened display:", modal.style.display);
console.log("  Modal restored title:", elements['aarti-modal-title'].textContent);
if (!elements['aarti-modal-title'].textContent.includes('लक्ष्मी')) {
  throw new Error("Modal did not restore Lakshmi collection!");
}
window.closeAartiOptionsModal();
console.log("  Closed back to:", window.currentPage);
console.log("✓ TEST 18 (LAKSHMI - AHOI MATA AARTI) PASSED PERFECTLY!");

console.log("\n🎉 ALL 18 NAVIGATION AND CONTENT TESTS PASSED 100%!");
process.exit(0);








