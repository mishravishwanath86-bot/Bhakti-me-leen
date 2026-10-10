const fs = require('fs');
const path = require('path');

console.log('=== RUNNING 2026 DWADASHI DATES VERIFICATION TEST ===\n');

// 1. Check Assets
const baseAssetDir = path.join(__dirname, 'assets');
const requiredAssets = [
  'dwadashi_kurma.jpg',
  'dwadashi_vishnu_garuda.jpg',
  'dwadashi_narasimha.jpg',
  'dwadashi_vamana.jpg',
  'dwadashi_parashurama.jpg',
  'dwadashi_govatsa.jpg',
  'dwadashi_kalki.jpg',
  'dwadashi_matsya.jpg',
  'moon_dwadashi_krishna.svg',
  'moon_dwadashi_shukla.svg',
  'dwadashi_banner.jpg'
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

// 2. Check index.html
const indexHtml = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
const hasKathaPage = indexHtml.includes('id="page-dwadashi-vrat-katha"');
const hasTabs = indexHtml.includes("switchDwadashiTab('main'") &&
                indexHtml.includes("switchDwadashiTab('avatars'") &&
                indexHtml.includes("switchDwadashiTab('vidhi'") &&
                indexHtml.includes("switchDwadashiTab('stotra'");

console.log(`[${hasKathaPage ? 'PASS' : 'FAIL'}] index.html has #page-dwadashi-vrat-katha`);
console.log(`[${hasTabs ? 'PASS' : 'FAIL'}] index.html has 4 interactive tabs for Dwadashi Katha`);

// 3. Check app.js content
const appJs = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf-8');
const hasData = appJs.includes('const DWADASHI_DATES_2026 =');
const hasRender = appJs.includes('function renderDrikDwadashi');
const hasKathaRouting = appJs.includes('page-dwadashi-vrat-katha');
const hasVratConfig = appJs.includes("vratKey === 'dwadashi'");
const hasHighlight = appJs.includes('dp-row-highlight') && appJs.includes('#76C5DF');

console.log(`[${hasData ? 'PASS' : 'FAIL'}] app.js contains DWADASHI_DATES_2026`);
console.log(`[${hasRender ? 'PASS' : 'FAIL'}] app.js contains renderDrikDwadashi`);
console.log(`[${hasKathaRouting ? 'PASS' : 'FAIL'}] app.js routes Dwadashi to page-dwadashi-vrat-katha`);
console.log(`[${hasVratConfig ? 'PASS' : 'FAIL'}] app.js routes openVratPage for dwadashi`);
console.log(`[${hasHighlight ? 'PASS' : 'FAIL'}] app.js includes cyan-blue highlight (#76C5DF)`);

// 4. Test parsing DWADASHI_DATES_2026
try {
  const startIdx = appJs.indexOf('const DWADASHI_DATES_2026 = [');
  const endMarker = 'function renderDrikDwadashi';
  const endIdx = appJs.indexOf(endMarker, startIdx);
  
  const rawArrayStr = appJs.slice(startIdx + 'const DWADASHI_DATES_2026 = '.length, endIdx).trim().replace(/;\s*$/, '');
  const dwadashiData = JSON.parse(rawArrayStr);
  console.log(`[PASS] DWADASHI_DATES_2026 parsed successfully. Total months: ${dwadashiData.length}`);
  
  let totalEvents = 0;
  let highlightedCount = 0;
  dwadashiData.forEach(m => {
    totalEvents += m.items.length;
    m.items.forEach(e => {
      if (e.isHighlight) highlightedCount++;
    });
  });
  console.log(`[PASS] Total Dwadashi events across 12 months: ${totalEvents}`);
  console.log(`[PASS] Highlighted events (Adhika Dwadashis): ${highlightedCount}`);

  if (assetsPass && hasKathaPage && hasTabs && hasData && hasRender && hasKathaRouting && hasVratConfig && hasHighlight && totalEvents === 25 && highlightedCount === 2) {
    console.log('\n🌟 ALL 2026 DWADASHI DATES CHECKS PASSED WITH 100% SUCCESS! 🌟');
    process.exit(0);
  } else {
    console.error('\n❌ SOME CHECKS FAILED!');
    process.exit(1);
  }
} catch (e) {
  console.error("Evaluation error:", e);
  process.exit(1);
}
