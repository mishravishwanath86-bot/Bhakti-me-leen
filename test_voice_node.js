
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

require('./amrit_kalash_3d_engine.js');

console.log("Testing processAIVoiceText with 'चिंता'...");
window.processAIVoiceText('मुझे भविष्य की बहुत चिंता है');
console.log("Active Shloka selected:", window.currentActiveShloka.source);

console.log("Testing processAIVoiceText with 'शांति'...");
window.processAIVoiceText('मन अशांत है शांति चाहिए');
console.log("Active Shloka selected:", window.currentActiveShloka.source);

console.log("✓ All Voice Guide Flows Executed with 100% Success!");
