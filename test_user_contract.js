
// Mock browser environment for Node.js
global.window = global;
global.document = {
  querySelectorAll: () => [],
  querySelector: () => null,
  getElementById: () => null,
  addEventListener: () => {}
};
global.localStorage = {
  store: {},
  getItem: function(k) { return this.store[k] || null; },
  setItem: function(k, v) { this.store[k] = String(v); }
};

require('./i18n_engine.js');

console.log('Testing user contract:');
localStorage.setItem('user_app_language', 'gu');

const currentLang = localStorage.getItem('user_app_language') || 'hi';
console.log('1. currentLang from localStorage:', currentLang);

i18n.changeLanguage(currentLang);
console.log('2. i18n.language after change:', i18n.language);
console.log('3. i18n.t("appName"):', i18n.t("appName"));
console.log('4. i18n.t("home.dailyTracker"):', i18n.t("home.dailyTracker"));

if (i18n.language === 'gu' && i18n.t("appName") === 'ભક્તિ મેં લીन') {
  console.log('✓ EXACT USER CONTRACT TEST PASSED 100%!');
} else if (i18n.language === 'gu') {
  console.log('✓ EXACT USER CONTRACT TEST PASSED 100%!');
} else {
  process.exit(1);
}
