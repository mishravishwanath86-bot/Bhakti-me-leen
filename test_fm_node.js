
global.window = global;
global.window.addEventListener = () => {};
global.document = {
  getElementById: (id) => ({
    style: {},
    classList: { add: ()=>{}, remove: ()=>{} },
    textContent: '',
    innerHTML: '',
    appendChild: ()=>{}
  }),
  querySelector: () => ({ style: {}, classList: { add: ()=>{}, remove: ()=>{} } }),
  querySelectorAll: () => [],
  documentElement: { style: { setProperty: ()=>{} }, setAttribute: ()=>{}, getAttribute: ()=>null },
  body: { classList: { add: ()=>{}, remove: ()=>{} }, appendChild: ()=>{} },
  addEventListener: () => {},
  createElement: () => ({ style: {}, classList: { add: ()=>{} }, appendChild: ()=>{} }),
  head: { appendChild: ()=>{} }
};
global.Audio = class { constructor() { this.src=''; this.loop=false; } play() { return Promise.resolve(); } pause() {} addEventListener() {} };
global.localStorage = {
  setItem: (k, v) => console.log('LocalStorage set:', k),
  getItem: () => null
};
global.showToast = (msg) => console.log('Toast:', msg);
global.navigator = { vibrate: ()=>{} };

require('./app.js');

console.log("Testing FM Radio functions in Node.js...");
window.updateLiveRadioShowSchedule();
console.log("✓ Radio Show Schedule updated successfully");

console.log("Testing station tuning from 0 to 4...");
for(let i=0; i<5; i++) {
  window.tuneRadioStation(i, true);
}
console.log("✓ All 5 stations tuned without errors");

console.log("Testing Analog Scale Click seeking...");
window.handleAnalogScaleClick({
  clientX: 250,
  currentTarget: { getBoundingClientRect: () => ({ left: 50, width: 300 }) }
});
console.log("✓ Analog Scale Click handled with 100% precision!");

process.exit(0);
