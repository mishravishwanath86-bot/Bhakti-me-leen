import subprocess

js_test = """
// Mock DOM
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable", url: "http://localhost:8000/" });

dom.window.addEventListener('load', () => {
  console.log("DOM loaded. Testing showPage...");
  console.log("typeof window.showPage:", typeof dom.window.showPage);
  console.log("typeof window.initPanchang:", typeof dom.window.initPanchang);
  console.log("typeof window.initNavigation:", typeof dom.window.initNavigation);
  
  // Test showPage
  if (typeof dom.window.showPage === 'function') {
    dom.window.showPage('page-panchang');
    const panchangActive = dom.window.document.getElementById('page-panchang').classList.contains('active');
    console.log("page-panchang has active class:", panchangActive);
  }
});
"""

with open(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\test_dom_sim.js", "w", encoding="utf-8") as f:
    f.write(js_test)

print("Created test_dom_sim.js")
