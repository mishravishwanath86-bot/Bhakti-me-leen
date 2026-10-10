const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Find the load event listener at the end
const loadStart = code.lastIndexOf("window.addEventListener('load', () => {");
if (loadStart > -1) {
    const newLoad = `window.addEventListener('load', () => {
    const splash = document.getElementById('splash-screen');
    if (splash) {
        splash.style.opacity = 0;
        setTimeout(() => splash.style.display = 'none', 300);
    }
    
    // Call all initialization functions safely
    const inits = [
        'initPanchang', 'initFestivals', 'initCalendar', 'initMuhuratPage',
        'initReader', 'initDeityGrids', 'initNavigation', 'initPanchangPage',
        'initDrawer', 'initModals', 'initStarRating', 'initAuth',
        'initDeityFilter', 'initRefreshButtons', 'initSettings', 'initPWA', 'initKatha'
    ];
    
    inits.forEach(fn => {
        try {
            if (typeof window[fn] === 'function') window[fn]();
            else if (typeof eval(fn) === 'function') eval(fn + '()');
        } catch(e) { console.error(fn, e); }
    });
});
`;
    code = code.substring(0, loadStart) + newLoad;
    fs.writeFileSync('app.js', code, 'utf8');
    console.log('Updated load listener to call all init functions.');
}
