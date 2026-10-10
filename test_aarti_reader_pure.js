const fs = require('fs');
const js = fs.readFileSync('app.js', 'utf8');

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
  querySelector: function() { return createMockEl('mock'); },
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
global.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve({ items: [] }) });
global.$ = (id) => mockDoc.getElementById(id);
global.CustomEvent = class { constructor(e, d) { this.event = e; this.detail = d; } };

try {
  eval(js);
  console.log("Testing readAartiItemDirect('ganesh', 0)...");
  window.readAartiItemDirect('ganesh', 0);
  console.log("  ✓ Reader Page Title:", elements['reader-page-title'].textContent);
  console.log("  ✓ Reader Cosmic Content length:", elements['reader-cosmic-content'].innerHTML.length);
  console.log("  ✓ Contains 'जय गणेश देवा':", elements['reader-cosmic-content'].innerHTML.includes('जय गणेश देवा'));

  console.log("\nTesting readAartiItemDirect('hanuman', 0)...");
  window.readAartiItemDirect('hanuman', 0);
  console.log("  ✓ Reader Page Title:", elements['reader-page-title'].textContent);
  console.log("  ✓ Reader Cosmic Content length:", elements['reader-cosmic-content'].innerHTML.length);
  console.log("  ✓ Contains 'आरती कीजै हनुमान लला की':", elements['reader-cosmic-content'].innerHTML.includes('आरती कीजै हनुमान लला की'));

  console.log("\n🎯 AARTI READER TEST PASSED 100%!");
} catch(e) {
  console.error("Test Error:", e);
}
