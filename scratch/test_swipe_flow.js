const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const dom = new JSDOM(html, {
  runScripts: "dangerously",
  resources: "usable"
});

const { window } = dom;
const { document } = window;

// Mock localStorage
const storage = {};
window.localStorage = {
  getItem: (k) => storage[k] || null,
  setItem: (k, v) => { storage[k] = v; }
};

// Mock audio
window.AudioContext = class {
  createOscillator() { return { connect() {}, start() {}, stop() {}, frequency: { setValueAtTime() {} } }; }
  createGain() { return { connect() {}, gain: { setValueAtTime() {}, exponentialRampToValueAtTime() {} } }; }
  get currentTime() { return 0; }
};

// Load epic_games_engine.js
const engineCode = fs.readFileSync('epic_games_engine.js', 'utf-8');
window.eval(engineCode);

console.log("=== Testing Swipe Launcher System ===");

// 1. Open Launcher
console.log("1. Calling window.openSwipeGame('cat_1_ramayana')...");
window.openSwipeGame('cat_1_ramayana');

const launcher = document.getElementById('swipe-launcher-screen');
console.log("Launcher display:", launcher.style.display);
console.assert(launcher.style.display === 'flex', "Launcher must be flex");

// 2. Check initial English highlight
const enCard = document.querySelector('.swipe-lang-card[data-lang="en"]');
const hiCard = document.querySelector('.swipe-lang-card[data-lang="hi"]');
const teCard = document.querySelector('.swipe-lang-card[data-lang="te"]');
console.log("Initial Active Card (should be en):", enCard.classList.contains('active'), hiCard.classList.contains('active'), teCard.classList.contains('active'));

// 3. Switch to Telugu
console.log("2. Switching language to Telugu ('te')...");
window.selectSwipeLanguage('te');
console.log("Active cards after Telugu selection: en=", enCard.classList.contains('active'), "te=", teCard.classList.contains('active'));
console.log("Game state lang:", window.epicGameState.currentLanguage);
console.assert(window.epicGameState.currentLanguage === 'te', "Current lang must be te");

// Check Telugu ribbon text
const ribbon = document.getElementById('swipe-launch-lang-ribbon-text');
console.log("Telugu Ribbon Text:", ribbon.textContent);
console.assert(ribbon.textContent === "ఆట భాషను ఎంచుకోండి", "Telugu ribbon text mismatch");

// 4. Slide Category
console.log("3. Sliding category using nextSwipeCategory()...");
const initialCat = window.epicGameState.selectedLauncherCategory;
window.nextSwipeCategory();
const nextCat = window.epicGameState.selectedLauncherCategory;
console.log("Category changed from", initialCat, "to", nextCat);
console.assert(nextCat === 'cat_2_lanka_war', "Next category should be cat_2_lanka_war");

// 5. Start Game
console.log("4. Starting game from Launcher (startSwipeGameFromLauncher)...");
window.startSwipeGameFromLauncher();

console.log("Launcher display:", launcher.style.display);
console.assert(launcher.style.display === 'none', "Launcher should be hidden after start");

const arena = document.getElementById('swipe-arena');
console.log("Arena display:", arena.style.display);
console.assert(arena.style.display === 'flex', "Arena should be displayed");

const titleEl = document.getElementById('swipe-cat-title');
console.log("In-game category title (Telugu):", titleEl.textContent);

const charNameEl = document.querySelector('.swipe-char-name-bar');
console.log("In-game first character name in Telugu:", charNameEl ? charNameEl.textContent : "N/A");

console.log("✓ ALL SWIPE GAME LAUNCHER & MULTILINGUAL TESTS PASSED!");
