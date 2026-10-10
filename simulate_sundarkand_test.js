const fs = require('fs');

console.log("--- STARTING SUNDARKAND ENGINE PROGRAMMATIC VALIDATION ---");

// 1. Read sundarkand_engine.js
const code = fs.readFileSync('sundarkand_engine.js', 'utf8');
console.log("sundarkand_engine.js loaded, size:", code.length, "bytes");

// Create mock browser DOM environment
global.window = global;
global.document = {
  getElementById: function(id) {
    return {
      id: id,
      style: {},
      children: [],
      classList: {
        add: () => {},
        remove: () => {}
      },
      querySelectorAll: () => [],
      addEventListener: () => {},
      scrollTop: 0
    };
  },
  querySelectorAll: function(sel) {
    return [];
  },
  body: { style: {} },
  addEventListener: function(event, cb) {
    if (event === 'DOMContentLoaded') cb();
  }
};
global.Audio = function() {
  return {
    addEventListener: () => {},
    play: () => Promise.resolve(),
    pause: () => {}
  };
};

// Evaluate sundarkand_engine.js
try {
  eval(code);
  console.log("✓ sundarkand_engine.js evaluated successfully without any runtime error!");
} catch (e) {
  console.error("✗ Error evaluating sundarkand_engine.js:", e);
  process.exit(1);
}

// Verify SUNDARKAND_DATA
if (!window.SUNDARKAND_DATA) {
  console.error("✗ window.SUNDARKAND_DATA is missing!");
  process.exit(1);
}
console.log("✓ Total chapters in dataset:", window.SUNDARKAND_DATA.chapters.length);
console.log("✓ Total dohas in dataset:", window.SUNDARKAND_DATA.dohas.length);

if (window.SUNDARKAND_DATA.chapters.length !== 10) {
  console.error("✗ Expected 10 chapters, got", window.SUNDARKAND_DATA.chapters.length);
  process.exit(1);
}
if (window.SUNDARKAND_DATA.dohas.length !== 60) {
  console.error("✗ Expected 60 dohas, got", window.SUNDARKAND_DATA.dohas.length);
  process.exit(1);
}

// Test openSundarkandChapterModal
try {
  window.openSundarkandChapterModal(1);
  console.log("✓ window.openSundarkandChapterModal(1) executed cleanly!");
} catch (e) {
  console.error("✗ Error in openSundarkandChapterModal:", e);
  process.exit(1);
}

// Test openSundarkandDohaReader
try {
  window.openSundarkandDohaReader(1);
  console.log("✓ window.openSundarkandDohaReader(1) executed cleanly!");
  window.openSundarkandDohaReader(30);
  console.log("✓ window.openSundarkandDohaReader(30) executed cleanly!");
  window.openSundarkandDohaReader(60);
  console.log("✓ window.openSundarkandDohaReader(60) executed cleanly!");
} catch (e) {
  console.error("✗ Error in openSundarkandDohaReader:", e);
  process.exit(1);
}

// Test renderFullSundarkandPage
try {
  window.renderFullSundarkandPage('all', '');
  console.log("✓ window.renderFullSundarkandPage('all', '') executed cleanly!");
  window.renderFullSundarkandPage('sopan-1-2', 'विभीषण');
  console.log("✓ window.renderFullSundarkandPage with filter and search executed cleanly!");
} catch (e) {
  console.error("✗ Error in renderFullSundarkandPage:", e);
  process.exit(1);
}

// Test toggleSundarkandAudio
try {
  window.toggleSundarkandAudio(false);
  console.log("✓ window.toggleSundarkandAudio executed cleanly!");
} catch (e) {
  console.error("✗ Error in toggleSundarkandAudio:", e);
  process.exit(1);
}

console.log("\n========================================================");
console.log("🎉 ALL SUNDARKAND LOGIC AND UNIT TESTS PASSED WITH 100% SUCCESS!");
console.log("========================================================");
