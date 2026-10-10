const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf8');
const js = fs.readFileSync('app.js', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });

// Inject script
const scriptEl = dom.window.document.createElement("script");
scriptEl.textContent = js;
dom.window.document.body.appendChild(scriptEl);

dom.window.addEventListener('load', () => {
  console.log("Testing openAartiCollectionModal('ganesh')...");
  try {
    dom.window.openAartiCollectionModal('ganesh');
    const modal = dom.window.document.getElementById('aarti-options-modal');
    console.log("Modal display style:", modal.style.display);
    console.log("Modal class list:", Array.from(modal.classList));
    console.log("Modal inner HTML length:", modal.innerHTML.length);
    console.log("Modal list items count:", dom.window.document.getElementById('aarti-modal-list').children.length);
  } catch (e) {
    console.error("ERROR running openAartiCollectionModal:", e);
  }
});
