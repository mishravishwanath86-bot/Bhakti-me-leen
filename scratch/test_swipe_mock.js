const fs = require('fs');

// Mock DOM environment
class Element {
  constructor(tag, id = '', className = '') {
    this.tagName = tag.toUpperCase();
    this.id = id;
    this.className = className;
    this.classList = {
      _classes: new Set(className ? className.split(' ') : []),
      add: (c) => this.classList._classes.add(c),
      remove: (c) => this.classList._classes.delete(c),
      contains: (c) => this.classList._classes.has(c)
    };
    this.style = {};
    this.children = [];
    this.attributes = {};
    this.textContent = '';
    this.innerHTML = '';
  }
  setAttribute(k, v) { this.attributes[k] = v; }
  getAttribute(k) { return this.attributes[k] || null; }
  appendChild(child) { this.children.push(child); }
  removeChild(child) { this.children = this.children.filter(c => c !== child); }
  addEventListener() {}
}

const elementsById = {};
const elementsByClass = {};

const doc = {
  getElementById: (id) => elementsById[id] || null,
  querySelectorAll: (selector) => {
    if (selector.startsWith('.')) {
      const cls = selector.replace('.', '').split('[')[0];
      return elementsByClass[cls] || [];
    }
    return [];
  },
  querySelector: (selector) => {
    const list = doc.querySelectorAll(selector);
    return list[0] || null;
  },
  createElement: (tag) => new Element(tag),
  body: new Element('body'),
  addEventListener: () => {}
};

function reg(el) {
  if (el.id) elementsById[el.id] = el;
  el.classList._classes.forEach(c => {
    if (!elementsByClass[c]) elementsByClass[c] = [];
    elementsByClass[c].push(el);
  });
  return el;
}

// Setup necessary elements
reg(new Element('div', 'swipe-launcher-screen', 'swipe-launcher-screen'));
reg(new Element('div', 'swipe-arena', 'swipe-game-arena'));
reg(new Element('div', 'swipe-review-arena', 'swipe-review-arena'));
reg(new Element('span', 'swipe-launch-lang-ribbon-text'));
reg(new Element('h2', 'swipe-launch-cat-header-text'));
reg(new Element('span', 'swipe-launch-play-btn-text'));
reg(new Element('div', 'swipe-cat-carousel-stage'));
reg(new Element('div', 'swipe-card-deck'));
reg(new Element('span', 'swipe-cat-title'));
reg(new Element('div', 'swipe-instruction'));
reg(new Element('span', 'swipe-left-portal-label'));
reg(new Element('span', 'swipe-right-portal-label'));
reg(new Element('span', 'swipe-left-score'));
reg(new Element('span', 'swipe-right-score'));
reg(new Element('div', 'swipe-review-tokens-rail'));
reg(new Element('div', 'swipe-review-card-container'));

// Setup 3 language cards
['te', 'hi', 'en'].forEach(lang => {
  const card = new Element('div', '', 'swipe-lang-card');
  card.setAttribute('data-lang', lang);
  reg(card);
});

// Setup 3 category slide cards
['cat_1_ramayana', 'cat_2_lanka_war', 'cat_3_mahabharat'].forEach((id, idx) => {
  const card = new Element('div', `cat-card-${idx+1}`, 'swipe-cat-slide-card');
  reg(card);
  reg(new Element('span', `vs-cat-${idx+1}-left`));
  reg(new Element('span', `vs-cat-${idx+1}-right`));
});

global.document = doc;
global.window = {
  innerWidth: 400,
  innerHeight: 800,
  localStorage: {
    data: {},
    getItem(k) { return this.data[k] || null; },
    setItem(k, v) { this.data[k] = v; }
  },
  navigator: { vibrate: () => {} }
};
global.localStorage = global.window.localStorage;

// Execute epic_games_engine.js
const code = fs.readFileSync('epic_games_engine.js', 'utf-8');
eval(code);

console.log("=== Testing Swipe Launcher Engine Flow ===");

// 1. Open Launcher
console.log("1. Calling window.openSwipeGame('cat_1_ramayana')...");
window.openSwipeGame('cat_1_ramayana');
const launcher = document.getElementById('swipe-launcher-screen');
console.log("Launcher display:", launcher.style.display);
if (launcher.style.display !== 'flex') throw new Error("Launcher display should be flex");

// 2. Select Language Telugu
console.log("2. Switching to Telugu ('te')...");
window.selectSwipeLanguage('te');
const ribbon = document.getElementById('swipe-launch-lang-ribbon-text');
console.log("Telugu ribbon text:", ribbon.textContent);
if (ribbon.textContent !== "ఆట భాషను ఎంచుకోండి") throw new Error("Telugu ribbon text incorrect");

// 3. Category slide
console.log("3. Sliding category...");
window.nextSwipeCategory();
console.log("Selected category after next:", window.epicGameState.selectedLauncherCategory);
if (window.epicGameState.selectedLauncherCategory !== 'cat_2_lanka_war') throw new Error("Category slide failed");

// 4. Start Game
console.log("4. Starting game from launcher...");
window.startSwipeGameFromLauncher();
console.log("Launcher display after start:", launcher.style.display);
console.log("Arena display after start:", document.getElementById('swipe-arena').style.display);
console.log("In-game category title (Telugu):", document.getElementById('swipe-cat-title').textContent);
console.log("In-game instruction (Telugu):", document.getElementById('swipe-instruction').textContent);
console.log("Deck size loaded:", window.epicGameState.deck.length);

console.log("\n>>> SUCCESS: ALL TESTS PASSED! <<<");
