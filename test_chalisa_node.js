const fs = require('fs');

global.window = global;
global.window.addEventListener = () => {};
global.Audio = class { addEventListener() {} };
global.localStorage = {
  getItem: () => null,
  setItem: () => {},
  removeItem: () => {}
};
const mockElem = () => ({
  textContent: '',
  innerHTML: '',
  classList: { add: () => {}, remove: () => {} },
  style: {},
  appendChild: () => {},
  querySelectorAll: () => [],
  addEventListener: () => {}
});

global.document = {
  body: {
    classList: { add: () => {}, remove: () => {} }
  },
  documentElement: {
    setAttribute: () => {},
    classList: { add: () => {}, remove: () => {} }
  },
  getElementById: (id) => mockElem(),
  createElement: (tag) => mockElem(),
  querySelectorAll: () => [],
  addEventListener: () => {}
};
global.navigator = { vibrate: () => {} };

require('./app.js');

console.log('\n=============================================');
console.log('CHALISA_COLLECTIONS keys count:', Object.keys(window.CHALISA_COLLECTIONS).length);
console.log('Categories:', Object.keys(window.CHALISA_COLLECTIONS));

let total = 0;
for (const [k, v] of Object.entries(window.CHALISA_COLLECTIONS)) {
  total += v.items.length;
  console.log(`  ${k}: ${v.items.length} chalisas (${v.title})`);
}

console.log('Total Chalisas in app.js:', total);

if (total === 54 && Object.keys(window.CHALISA_COLLECTIONS).length === 18) {
  console.log('\n>>> ALL VERIFICATIONS PASSED 100%! <<<');
} else {
  console.error('MISMATCH!');
  process.exit(1);
}
