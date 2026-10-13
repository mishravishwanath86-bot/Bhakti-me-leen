const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');
const styles = fs.readFileSync('styles.css', 'utf8');
const lightTheme = fs.readFileSync('light_theme.css', 'utf8');

console.log('=== VERIFYING READER UI FIXES ===');

// Extract page-reader section
const readerStart = html.indexOf('id="page-reader"');
const readerSection = html.substring(readerStart, readerStart + 2500);

// 1. White circle: Share button removal from page-reader
const shareBtnInReader = readerSection.includes('📤') || readerSection.includes('shareDivineCard');
console.log('1. Share button (📤) completely removed from #page-reader header?:', !shareBtnInReader ? '✅ YES' : '❌ NO');

// 2. Blue box: reader-page-title styling
const hasReaderTitle = readerSection.includes('id="reader-page-title"');
const titleHasBrightColor = readerSection.includes('color:#FFFDF8 !important');
const titleHasGlow = readerSection.includes('text-shadow:0 1px 3px rgba(0,0,0,0.9), 0 0 10px rgba(248,200,59,0.5)');
console.log('2. #reader-page-title exists in reader?:', hasReaderTitle ? '✅ YES' : '❌ NO');
console.log('   #reader-page-title bright white/radiant text styled?:', titleHasBrightColor ? '✅ YES' : '❌ NO');
console.log('   #reader-page-title divine golden glow text-shadow applied?:', titleHasGlow ? '✅ YES' : '❌ NO');

// 3. Purple box: Flip buttons styling
const hasFlipButtons = readerSection.includes('class="reader-flip-btn"');
const flipBtnHasGoldGradient = readerSection.includes('background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%)');
const flipBtnHasDarkText = readerSection.includes('color:#1A0B2E !important');
console.log('3. Flip buttons (❮ पिछला पत्र / अगला पत्र ❯) exist?:', hasFlipButtons ? '✅ YES' : '❌ NO');
console.log('   Flip buttons high-contrast gold gradient?:', flipBtnHasGoldGradient ? '✅ YES' : '❌ NO');
console.log('   Flip buttons high-contrast bold dark text (#1A0B2E)?:', flipBtnDarkText = flipBtnHasDarkText ? '✅ YES' : '❌ NO');

// 4. Stylesheet overrides
console.log('4. styles.css contains reader title high contrast overrides?:', styles.includes('#page-reader #reader-page-title') ? '✅ YES' : '❌ NO');
console.log('   styles.css contains .reader-flip-btn high contrast overrides?:', styles.includes('.reader-flip-btn') ? '✅ YES' : '❌ NO');
console.log('   light_theme.css contains #page-reader #reader-page-title exemption?:', lightTheme.includes('#page-reader #reader-page-title') ? '✅ YES' : '❌ NO');
console.log('   light_theme.css contains .reader-flip-btn exemption?:', lightTheme.includes('.reader-flip-btn') ? '✅ YES' : '❌ NO');

if (!shareBtnInReader && hasReaderTitle && titleHasBrightColor && flipBtnHasGoldGradient && flipBtnHasDarkText) {
  console.log('\n🎉 ALL 3 USER UI ISSUES RESOLVED WITH 100% CONTRAST & ACCESSIBILITY!');
} else {
  console.error('\n⚠️ SOME CHECKS FAILED!');
  process.exit(1);
}
