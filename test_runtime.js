
global.window = global;
global.window.addEventListener = () => {};
global.window.removeEventListener = () => {};
global.document = {
  getElementById: (id) => ({
    style: {},
    classList: { add: ()=>{}, remove: ()=>{}, contains: ()=>false },
    addEventListener: ()=>{},
    textContent: '',
    innerHTML: '',
    value: '',
    dataset: {}
  }),
  querySelector: () => ({
    style: {},
    classList: { add: ()=>{}, remove: ()=>{} },
    addEventListener: ()=>{}
  }),
  querySelectorAll: () => [],
  addEventListener: ()=>{},
  documentElement: { 
    style: { setProperty: ()=>{} },
    setAttribute: ()=>{},
    getAttribute: ()=>null
  },
  body: {
    classList: { add: ()=>{}, remove: ()=>{} },
    style: {}
  },
  createElement: () => ({ style: {}, classList: { add: ()=>{} }, appendChild: ()=>{} }),
  head: { appendChild: ()=>{} }
};
global.localStorage = {
  getItem: (k) => null,
  setItem: (k, v) => {},
  removeItem: (k) => {}
};
global.navigator = { vibrate: ()=>true };
global.Audio = class {
  constructor() {
    this.src = '';
    this.loop = false;
  }
  play() { return Promise.resolve(); }
  pause() {}
  addEventListener() {}
};
global.location = { href: 'http://localhost:8000/' };

try {
  require('./app.js');
  console.log('SUCCESS: app.js loaded and executed with ZERO errors!');
  console.log('toggleLiveRadioPlayback is ready:', typeof window.toggleLiveRadioPlayback === 'function');
  console.log('switchRadioChannel is ready:', typeof window.switchRadioChannel === 'function');
  console.log('openAuthModal is ready:', typeof window.openAuthModal === 'function');
  console.log('setGlobalFontSize is ready:', typeof window.setGlobalFontSize === 'function');
} catch (err) {
  console.error('Runtime Error in app.js:', err);
  process.exit(1);
}
