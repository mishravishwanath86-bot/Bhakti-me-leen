const fs = require('fs');
const path = require('path');

console.log('--- Starting Sakat Chauth & Lambodara Sankashti Integration Tests ---');

const appDir = 'c:\\Users\\vishw\\.gemini\\antigravity-ide\\scratch\\bhakti-app';

// 1. Verify Assets
const sakatImg = path.join(appDir, 'assets', 'sakat_chauth_hero.jpg');
const lambodaraImg = path.join(appDir, 'assets', 'lambodara_hero.jpg');

if (fs.existsSync(sakatImg) && fs.statSync(sakatImg).size > 1000) {
  console.log('✅ Sakat Chauth Hero Image verified:', fs.statSync(sakatImg).size, 'bytes');
} else {
  console.error('❌ Missing or invalid Sakat Chauth image');
  process.exit(1);
}

if (fs.existsSync(lambodaraImg) && fs.statSync(lambodaraImg).size > 1000) {
  console.log('✅ Lambodara Hero Image verified:', fs.statSync(lambodaraImg).size, 'bytes');
} else {
  console.error('❌ Missing or invalid Lambodara image');
  process.exit(1);
}

// 2. Verify index.html Sections
const indexHtml = fs.readFileSync(path.join(appDir, 'index.html'), 'utf8');

const requiredTokens = [
  'id="page-sakat-chauth"',
  'id="page-lambodara-sankashti"',
  'Sakat Chauth Pujan',
  'Lambodara Sankashti Chaturthi',
  '08:59 PM',
  '08:01 AM',
  'Jan 06, 2026',
  '06:52 AM',
  'Jan 07, 2026',
  'sakat-moonrise-val',
  'lambodara-moonrise-val',
  'Story of a Potter and the Old Lady',
  'Story of Two Sisters-in-law',
  'The Story of a Brahmin named Rishi Sharma',
  'data-back="page-sankashti"'
];

let allTokensFound = true;
for (const token of requiredTokens) {
  if (indexHtml.includes(token)) {
    console.log(`✅ index.html contains: "${token}"`);
  } else {
    console.error(`❌ Missing token in index.html: "${token}"`);
    allTokensFound = false;
  }
}

// 3. Verify styles.css
const stylesCss = fs.readFileSync(path.join(appDir, 'styles.css'), 'utf8');
const cssClasses = [
  '.dp-fest-hero-wrapper',
  '.dp-fest-hero-grid',
  '.dp-fest-date-box',
  '.dp-fest-img-box',
  '.dp-fest-timing-card',
  '.dp-fest-tab-header',
  '.dp-time-toggle-pill',
  '.dp-fest-quick-link',
  '.dp-fest-katha-banner',
  '.dp-fest-card-block'
];

for (const cls of cssClasses) {
  if (stylesCss.includes(cls)) {
    console.log(`✅ styles.css contains: "${cls}"`);
  } else {
    console.error(`❌ Missing class in styles.css: "${cls}"`);
    allTokensFound = false;
  }
}

// 4. Verify app.js hooks and helpers
const appJs = fs.readFileSync(path.join(appDir, 'app.js'), 'utf8');
const appHooks = [
  'dp-link-sakat',
  'dp-link-lambodara',
  'showPage(\'page-sakat-chauth\')',
  'showPage(\'page-lambodara-sankashti\')',
  'window.switchDpTimeFormat',
  'window.scrollToElementId'
];

for (const hook of appHooks) {
  if (appJs.includes(hook)) {
    console.log(`✅ app.js contains: "${hook}"`);
  } else {
    console.error(`❌ Missing hook in app.js: "${hook}"`);
    allTokensFound = false;
  }
}

if (!allTokensFound) {
  console.error('❌ Some tests failed!');
  process.exit(1);
} else {
  console.log('\n🎉 ALL INTEGRATION TESTS PASSED PERFECTLY!');
}
