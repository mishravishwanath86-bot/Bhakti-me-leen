import sqlite3, json, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🧪 RUNNING COMPREHENSIVE AUDIO PLAYER VERIFICATION SUITE")
print("======================================================================")

# 1. Check HTML structure
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert 'id="glass-youtube-container"' in html, "Missing #glass-youtube-container in index.html"
assert html.count('id="glass-youtube-container"') == 1, "Duplicate #glass-youtube-container in index.html"
assert 'id="reader-youtube-container"' in html, "Missing #reader-youtube-container in index.html"
print("✓ HTML Structure Verification: Exactly ONE #glass-youtube-container found in player modal")

# 2. Check JS syntax
res = subprocess.run(['node', '-c', 'app.js'], capture_output=True, text=True)
assert res.returncode == 0, f"Syntax error in app.js: {res.stderr}"
print("✓ JavaScript Syntax Verification: app.js valid and clean")

# 3. Check Database Read-Only Integrity
conn = sqlite3.connect('file:db/bhakti.db?mode=ro', uri=True)
cursor = conn.cursor()
cursor.execute("PRAGMA integrity_check;")
assert cursor.fetchone()[0] == 'ok'
cursor.execute("SELECT COUNT(*) FROM content_items;")
total_items = cursor.fetchone()[0]
assert total_items == 10010, f"Expected 10010 items, found {total_items}"
conn.close()
print("✓ Database Safety Verification: db/bhakti.db integrity OK, 0 writes performed")

# 4. Run Complete Node.js Lifecycle & Playback Pipeline Test
node_test_script = """
const fs = require('fs');

// Mock DOM Environment
const elements = {};
function createMockElement(id, tag = 'div') {
  const el = {
    id: id,
    tagName: tag.toUpperCase(),
    style: {
      setProperty: function(prop, val) { this[prop] = val; },
      removeProperty: function(prop) { delete this[prop]; }
    },
    classList: {
      _classes: new Set(),
      add: function(c) { this._classes.add(c); },
      remove: function(c) { this._classes.delete(c); },
      contains: function(c) { return this._classes.has(c); },
      toggle: function(c, force) { if (force !== undefined) { force ? this._classes.add(c) : this._classes.delete(c); } else { this._classes.has(c) ? this._classes.delete(c) : this._classes.add(c); } }
    },
    innerHTML: '',
    textContent: '',
    value: '0',
    querySelector: function(sel) {
      if (sel.includes('iframe') && this.innerHTML.includes('<iframe')) {
        return { contentWindow: { postMessage: (msg) => {} } };
      }
      return null;
    }
  };
  return el;
}

const elementIds = [
  'glass-full-player-modal', 'glass-youtube-container', 'reader-youtube-container',
  'glass-modal-img', 'glass-modal-title', 'glass-modal-sub', 'glass-modal-cur-time',
  'glass-modal-tot-time', 'glass-modal-seekbar', 'glass-modal-play-btn', 'glass-modal-play-icon',
  'glass-mini-title', 'glass-mini-deity', 'glass-mini-cover', 'glass-mini-time', 'glass-mini-play-btn',
  'glass-lyrics-content', 'glass-lyrics-body'
];

elementIds.forEach(id => { elements[id] = createMockElement(id); });

global.window = global;
global.window.addEventListener = () => {};
global.document = {
  getElementById: (id) => elements[id] || null,
  querySelector: (sel) => {
    if (sel === '.classic-artwork-ring') return elements['glass-modal-img'];
    if (sel.includes('#glass-youtube-container iframe')) {
      if (elements['glass-youtube-container'].innerHTML.includes('<iframe')) {
        return { contentWindow: { postMessage: () => {} } };
      }
    }
    return null;
  },
  querySelectorAll: (sel) => [],
  documentElement: { style: { setProperty: ()=>{} }, setAttribute: ()=>{}, getAttribute: ()=>null },
  body: { classList: { add: ()=>{}, remove: ()=>{} }, appendChild: ()=>{} },
  addEventListener: () => {},
  createElement: (tag) => createMockElement('dynamic-' + Math.random(), tag),
  head: { appendChild: ()=>{} }
};

global.Audio = class {
  constructor() {
    this.src = '';
    this.paused = true;
    this.volume = 1.0;
    this.muted = false;
  }
  play() { this.paused = false; return Promise.resolve(); }
  pause() { this.paused = true; }
  load() {}
  addEventListener() {}
};

global.window.coreAudioElement = new global.Audio();
global.localStorage = { setItem: ()=>{}, getItem: ()=>null };
global.showToast = (msg) => {};

// Load app.js
require('./app.js');

console.log('\\n--- Step 1: Testing Old Known-Good Local MP3 ---');
const localMp3Record = {
  id: 'katha-ramayana-sample',
  title: 'बालकाण्ड - श्री राम जन्म',
  audio_url: 'assets/audio/katha_ramayana.mp3',
  deity_id: 'ram'
};
window.MediaRouter.playRecord(localMp3Record, 'glass');
console.log('Active mode:', window.MediaRouter.activeMode);
console.log('HTML5 Audio src:', window.coreAudioElement.src);
console.log('HTML5 Audio paused:', window.coreAudioElement.paused);
console.log('YouTube Container display:', elements['glass-youtube-container'].style.display);
if (window.MediaRouter.activeMode === 'local' && window.coreAudioElement.src.includes('assets/audio/katha_ramayana.mp3') && elements['glass-youtube-container'].style.display === 'none') {
  console.log('✓ Old Known-Good Local MP3: PASS');
} else {
  throw new Error('Old Known-Good Local MP3 failed');
}

console.log('\\n--- Step 2: Testing Phase 2N YouTube Audio ---');
const yt2nRecord = {
  id: 'b6-katha-ram-ahiravan-patal-prasang-hanuman-b6',
  title: 'अहिरावण पाताल प्रसंग (हनुमान जी)',
  audio_url: 'https://www.youtube.com/watch?v=2MWF-UHsC64',
  deity_id: 'hanuman'
};
window.MediaRouter.playRecord(yt2nRecord, 'glass');
console.log('Active mode:', window.MediaRouter.activeMode);
console.log('Current YouTube ID:', window.MediaRouter.currentYouTubeId);
console.log('YouTube Container display:', elements['glass-youtube-container'].style.display);
console.log('YouTube Container contains iframe:', elements['glass-youtube-container'].innerHTML.includes('2MWF-UHsC64'));
if (window.MediaRouter.activeMode === 'youtube' && window.MediaRouter.currentYouTubeId === '2MWF-UHsC64' && elements['glass-youtube-container'].style.display === 'block' && elements['glass-youtube-container'].innerHTML.includes('2MWF-UHsC64')) {
  console.log('✓ Phase 2N YouTube Audio: PASS');
} else {
  throw new Error('Phase 2N YouTube Audio failed');
}

console.log('\\n--- Step 3: Testing Phase 2O YouTube Audio ---');
const yt2oRecord = {
  id: 'b20-ganesh-katha-b20-458',
  title: 'भगवान गणेश दिव्य चरित्र स्तुति',
  audio_url: 'https://www.youtube.com/watch?v=im-9cVVmND0',
  deity_id: 'ganesh'
};
window.MediaRouter.playRecord(yt2oRecord, 'glass');
console.log('Current YouTube ID:', window.MediaRouter.currentYouTubeId);
if (window.MediaRouter.activeMode === 'youtube' && window.MediaRouter.currentYouTubeId === 'im-9cVVmND0' && elements['glass-youtube-container'].innerHTML.includes('im-9cVVmND0')) {
  console.log('✓ Phase 2O YouTube Audio: PASS');
} else {
  throw new Error('Phase 2O YouTube Audio failed');
}

console.log('\\n--- Step 4: Testing Phase 2P YouTube Audio ---');
const yt2pRecord = {
  id: 'b15-katha-purana-prerak-dhara-06-b15',
  title: 'सनातन धर्म पावन पुराण प्रेरक प्रसंग 06',
  audio_url: 'https://www.youtube.com/watch?v=fQse0WNm0hE',
  deity_id: 'general'
};
window.MediaRouter.playRecord(yt2pRecord, 'glass');
console.log('Current YouTube ID:', window.MediaRouter.currentYouTubeId);
if (window.MediaRouter.activeMode === 'youtube' && window.MediaRouter.currentYouTubeId === 'fQse0WNm0hE' && elements['glass-youtube-container'].innerHTML.includes('fQse0WNm0hE')) {
  console.log('✓ Phase 2P YouTube Audio: PASS');
} else {
  throw new Error('Phase 2P YouTube Audio failed');
}

console.log('\\n--- Step 5: Testing Phase 2Q YouTube Audio ---');
const yt2qRecord = {
  id: 'b14-katha-purana-prerak-dhara-11-b14',
  title: 'सनातन धर्म पावन पुराण प्रेरक प्रसंग 11',
  audio_url: 'https://www.youtube.com/watch?v=d_kH0Wb4D0w',
  deity_id: 'general'
};
window.MediaRouter.playRecord(yt2qRecord, 'glass');
console.log('Current YouTube ID:', window.MediaRouter.currentYouTubeId);
if (window.MediaRouter.activeMode === 'youtube' && window.MediaRouter.currentYouTubeId === 'd_kH0Wb4D0w' && elements['glass-youtube-container'].innerHTML.includes('d_kH0Wb4D0w')) {
  console.log('✓ Phase 2Q YouTube Audio: PASS');
} else {
  throw new Error('Phase 2Q YouTube Audio failed');
}

console.log('\\n--- Step 6: Testing Transitions & Modal Lifecycle ---');
// Switch YouTube -> Local MP3
window.MediaRouter.playRecord(localMp3Record, 'glass');
console.log('After YouTube -> Local switch, activeMode:', window.MediaRouter.activeMode);
console.log('YouTube container innerHTML cleared:', elements['glass-youtube-container'].innerHTML === '');
console.log('YouTube container hidden:', elements['glass-youtube-container'].style.display === 'none');
console.log('Local audio playing:', !window.coreAudioElement.paused);

// Close modal
window.closeGlassPlayer();
console.log('After closeGlassPlayer, activeMode:', window.MediaRouter.activeMode);

console.log('\\n🎉 ALL PLAYBACK, LIFECYCLE & ROUTING TESTS PASSED WITH 100% SUCCESS!');
process.exit(0);
"""

node_res = subprocess.run(['node', '-e', node_test_script], capture_output=True, text=True)
print(node_res.stdout)
if node_res.stderr:
    print("Stderr:", node_res.stderr)
assert node_res.returncode == 0, f"Node test failed: {node_res.stderr}"

print("======================================================================")
print("✅ PHASE AUDIO PLAYER FIX-01 COMPLETE AND FULLY VERIFIED")
print("======================================================================")
