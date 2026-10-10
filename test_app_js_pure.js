const fs = require('fs');
const js = fs.readFileSync('app.js', 'utf8');

// Mock window and document
const elements = {};
function createMockEl(id) {
  return {
    id,
    style: {},
    classList: {
      add: function(c) { this[c] = true; },
      remove: function(c) { delete this[c]; },
      contains: function(c) { return !!this[c]; },
      toggle: function(c, val) { if (val) this.add(c); else this.remove(c); }
    },
    textContent: '',
    innerHTML: '',
    children: [],
    dataset: {},
    getAttribute: function(a) { return this[a]; },
    setAttribute: function(a, v) { this[a] = v; },
    addEventListener: function() {}
  };
}

const mockDoc = {
  getElementById: function(id) {
    if (!elements[id]) elements[id] = createMockEl(id);
    return elements[id];
  },
  querySelectorAll: function() { return []; },
  querySelector: function() { return null; },
  createElement: function(tag) { return createMockEl('new_' + tag); },
  addEventListener: function() {},
  dispatchEvent: function() {}
};

class MockAudio {
  constructor() {
    this.src = '';
    this.currentTime = 0;
    this.duration = 100;
  }
  play() { return Promise.resolve(); }
  pause() {}
  addEventListener() {}
}

const mockWindow = {
  document: mockDoc,
  localStorage: { getItem: () => null, setItem: () => {} },
  scrollTo: () => {},
  addEventListener: () => {},
  navigator: { vibrate: () => {} },
  Audio: MockAudio
};

global.window = mockWindow;
global.document = mockDoc;
global.localStorage = mockWindow.localStorage;
global.navigator = mockWindow.navigator;
global.Audio = MockAudio;
global.$ = (id) => mockDoc.getElementById(id);
global.CustomEvent = class { constructor(e, d) { this.event = e; this.detail = d; } };

try {
  eval(js);
  console.log("app.js evaluated with 0 errors!");
  
  console.log("\nTesting window.openAartiCollectionModal('ganesh')...");
  window.openAartiCollectionModal('ganesh');
  const modal = elements['aarti-options-modal'];
  console.log("Modal display:", modal.style.display);
  console.log("Modal title text:", elements['aarti-modal-title'].textContent);
  console.log("Modal deity text:", elements['aarti-modal-deity'].textContent);
  console.log("Modal list HTML length:", elements['aarti-modal-list'].innerHTML.length);
  
  console.log("\nTesting window.openAartiCollectionModal('hanuman')...");
  window.openAartiCollectionModal('hanuman');
  console.log("Modal title text:", elements['aarti-modal-title'].textContent);
  console.log("Modal deity text:", elements['aarti-modal-deity'].textContent);
  console.log("Modal list HTML length:", elements['aarti-modal-list'].innerHTML.length);
} catch (e) {
  console.error("Evaluation Error:", e);
}
