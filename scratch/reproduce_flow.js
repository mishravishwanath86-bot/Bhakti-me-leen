const fs = require('fs');

// Create minimal DOM
const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id: id,
      style: {},
      classList: {
        add: () => {},
        remove: () => {},
        toggle: () => {},
        contains: () => false
      },
      innerHTML: '',
      innerText: '',
      textContent: '',
      setAttribute: () => {},
      getAttribute: () => null,
      querySelector: () => null,
      querySelectorAll: () => [],
      appendChild: () => {},
      removeChild: () => {},
      addEventListener: () => {},
      removeEventListener: () => {}
    };
  }
  return elements[id];
}

global.window = global;
global.CustomEvent = class {
  constructor(name, opts) { this.name = name; this.detail = opts && opts.detail; }
};
global.document = {
  documentElement: getEl('html'),
  getElementById: (id) => getEl(id),
  createElement: (tag) => getEl(tag),
  querySelector: (sel) => getEl('sel_' + sel),
  querySelectorAll: () => [],
  addEventListener: () => {},
  removeEventListener: () => {},
  dispatchEvent: () => {},
  body: getEl('body')
};
global.navigator = { vibrate: () => {} };
global.localStorage = {
  getItem: () => null,
  setItem: () => {},
  removeItem: () => {}
};
global.window.addEventListener = () => {};
global.window.removeEventListener = () => {};
global.window.scrollTo = () => {};
global.window.location = { pathname: '/', search: '', hash: '' };
global.Audio = class {
  constructor() {
    this.currentTime = 0;
    this.duration = 100;
  }
  play() { return Promise.resolve(); }
  pause() {}
  addEventListener() {}
  removeEventListener() {}
};
global.fetch = async (url, opts) => {
  return {
    json: async () => ({ success: true, audio_url: '/assets/ai_audio/test.mp3' })
  };
};

// 1. Load app.js
console.log("Loading app.js...");
require('../app.js');

// 2. Load ai_bhakti_player.js
console.log("Loading ai_bhakti_player.js...");
require('../ai_bhakti_player.js');

console.log("window.readAartiItemDirect:", typeof window.readAartiItemDirect);
console.log("window.AiBhaktiPlayer:", typeof window.AiBhaktiPlayer);

// 3. Test readAartiItemDirect('krishna', 2)
console.log("\nCalling window.readAartiItemDirect('krishna', 2)...");
window.readAartiItemDirect('krishna', 2);

console.log("AiBhaktiPlayer.currentContent after readAartiItemDirect:", window.AiBhaktiPlayer.currentContent);

// 4. Test togglePlay()
console.log("\nCalling window.AiBhaktiPlayer.togglePlay()...");
window.AiBhaktiPlayer.togglePlay().then(() => {
  console.log("After togglePlay - isPlaying:", window.AiBhaktiPlayer.isPlaying);
  console.log("isGenerating:", window.AiBhaktiPlayer.isGenerating);
});
