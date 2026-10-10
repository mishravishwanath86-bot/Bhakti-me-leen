import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
app_js_path = BASE_DIR / "app.js"

with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Replace window.initAllAppModules with string array lookups
broken_inits = """  const inits = [
    initNavigation, initDeityGrids, initPanchang, initCoverflow3D, 
    initFestivals, initCalendar, initMuhuratPage, initReader, 
    initDrawer, initPanchangPage, initKathaPage
  ];

  inits.forEach(fn => {
    try {
      if (typeof fn === 'function') fn();
    } catch(err) {
      console.warn('Module init warning:', err);
    }
  });"""

safe_inits = """  const fnNames = [
    'initNavigation', 'initDeityGrids', 'initPanchang', 'initCoverflow3D', 
    'initFestivals', 'initCalendar', 'initMuhuratPage', 'initReader', 
    'initDrawer', 'initPanchangPage', 'initKathaPage', 'initAudioLibraryPage',
    'renderDivineGallery'
  ];

  fnNames.forEach(fn => {
    try {
      if (typeof window[fn] === 'function') {
        window[fn]();
      } else if (typeof globalThis[fn] === 'function') {
        globalThis[fn]();
      }
    } catch(err) {
      console.warn('Module init warning for ' + fn, err);
    }
  });"""

if broken_inits in js:
    js = js.replace(broken_inits, safe_inits)
    print("✓ Replaced broken inits with safe fnNames")
else:
    print("broken_inits pattern not matched exactly, applying regex replace")
    js = re.sub(r'const inits = \[[^\]]*\];\s*inits\.forEach\([^)]*\)\s*\{[\s\S]*?\}\);', safe_inits, js)

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
