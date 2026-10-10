const fs = require('fs');
const path = require('path');

console.log('=== RUNNING 2026 MASIK SHIVARATRI VERIFICATION TEST ===\n');

// 1. Verify Assets
const baseAssetDir = path.join(__dirname, 'assets');
const requiredAssets = [
  'shiva_parvati.jpg',
  'ladies_maha_shivaratri_puja.jpg',
  'sawan_shivaratri.jpg',
  'moon_chaturdashi_krishna.svg'
];

let assetsPass = true;
requiredAssets.forEach(f => {
  const p = path.join(baseAssetDir, f);
  if (fs.existsSync(p)) {
    const sz = fs.statSync(p).size;
    console.log(`[PASS] Asset exists: ${f} (${sz} bytes)`);
  } else {
    console.error(`[FAIL] Asset missing: ${f}`);
    assetsPass = false;
  }
});

// 2. Verify HTML Page Section
const indexHtml = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
const hasKathaPage = indexHtml.includes('id="page-shivaratri-vrat-katha"');
const hasTabs = indexHtml.includes("switchShivaratriPageTab('katha'") &&
                indexHtml.includes("switchShivaratriPageTab('chitrabhanu'") &&
                indexHtml.includes("switchShivaratriPageTab('vidhi'") &&
                indexHtml.includes("switchShivaratriPageTab('guide'") &&
                indexHtml.includes("switchShivaratriPageTab('aarti'");

console.log(`[${hasKathaPage ? 'PASS' : 'FAIL'}] index.html has #page-shivaratri-vrat-katha`);
console.log(`[${hasTabs ? 'PASS' : 'FAIL'}] index.html has 5 interactive tabs for Shivaratri Katha & Guide`);

// 3. Verify JavaScript Configuration and Rendering
const appJs = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf-8');
const hasData = appJs.includes('const SHIVARATRI_DATES_2026 =');
const hasRender = appJs.includes('function renderDrikShivaratri');
const hasKathaRouting = appJs.includes('page-shivaratri-vrat-katha');
const hasVratConfig = appJs.includes('"masik-shivaratri": {') || appJs.includes("'masik-shivaratri': {");
const hasHighlight = appJs.includes('dp-shiv-row-adhika') && appJs.includes('#76C5DF');

console.log(`[${hasData ? 'PASS' : 'FAIL'}] app.js contains SHIVARATRI_DATES_2026`);
console.log(`[${hasRender ? 'PASS' : 'FAIL'}] app.js contains renderDrikShivaratri`);
console.log(`[${hasKathaRouting ? 'PASS' : 'FAIL'}] app.js routes Katha to page-shivaratri-vrat-katha`);
console.log(`[${hasVratConfig ? 'PASS' : 'FAIL'}] app.js configures masik-shivaratri in VRAT_PAGES_DATA`);
console.log(`[${hasHighlight ? 'PASS' : 'FAIL'}] app.js includes cyan-blue highlight (#76C5DF) for Adhika month`);

// 4. Test parsing data
try {
  const startIdx = appJs.indexOf('const SHIVARATRI_DATES_2026 = [');
  const arrayStart = startIdx + 'const SHIVARATRI_DATES_2026 = '.length;
  const arrayEnd = appJs.indexOf('];', arrayStart) + 1;
  
  const rawArrayStr = appJs.slice(arrayStart, arrayEnd).trim();
  const shivData = JSON.parse(rawArrayStr);
  console.log(`[PASS] SHIVARATRI_DATES_2026 parsed successfully. Total occurrences: ${shivData.length}`);
  
  const hasFebMaha = shivData.some(d => d.date.includes('February 15, 2026') && d.names.includes('Maha Shivaratri'));
  const hasJunAdhika = shivData.some(d => d.date.includes('June 13, 2026') && d.is_adhika === true);
  const hasAugSawan = shivData.some(d => d.date.includes('August 11, 2026') && d.names.includes('Sawan Shivaratri'));

  console.log(`[${hasFebMaha ? 'PASS' : 'FAIL'}] February 15, 2026 is Maha Shivaratri`);
  console.log(`[${hasJunAdhika ? 'PASS' : 'FAIL'}] June 13, 2026 is Adhika Masik Shivaratri`);
  console.log(`[${hasAugSawan ? 'PASS' : 'FAIL'}] August 11, 2026 is Sawan Shivaratri`);

  if (assetsPass && hasKathaPage && hasTabs && hasData && hasRender && hasKathaRouting && hasVratConfig && hasHighlight && shivData.length === 12 && hasFebMaha && hasJunAdhika && hasAugSawan) {
    console.log('\n🌟 ALL 2026 MASIK SHIVARATRI CHECKS PASSED WITH 100% SUCCESS! 🌟');
    process.exit(0);
  } else {
    console.error('\n❌ SOME CHECKS FAILED!');
    process.exit(1);
  }
} catch (e) {
  console.error("Evaluation error:", e);
  process.exit(1);
}
