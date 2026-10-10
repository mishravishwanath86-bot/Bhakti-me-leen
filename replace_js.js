const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const startStr = 'function initKatha(){';
let startIdx = code.indexOf(startStr);
// The function ends before initCalendar() or the end of file.
let endIdx = code.indexOf('function initCalendar(){');

if(startIdx > -1 && endIdx > startIdx) {
  let oldLogic = code.substring(startIdx, endIdx);
  
  // Create new initKatha logic using the new glassmorphism IDs
  let newLogic = `function initKatha(){
  const grid = document.getElementById('katha-grid');
  if(!grid) return;

  let savedKatha = JSON.parse(localStorage.getItem('bhakti_katha_saved') || '[]');
  let currentKatha = null, playing = false;
  let audioPlayer = new Audio();
  
  // UI Elements
  const miniPlayer = document.getElementById('mini-player');
  const miniThumb = document.getElementById('mini-thumb');
  const miniTitle = document.getElementById('mini-title');
  const miniSub = document.getElementById('mini-sub');
  const miniPlayBtn = document.getElementById('mini-play');
  const miniProgress = document.getElementById('mini-progress-fill');
  
  const fullPlayer = document.getElementById('full-player');
  const fullCloseBtn = document.getElementById('full-close');
  const fullThumb = document.getElementById('full-thumb');
  const fullTitle = document.getElementById('full-title');
  const fullSub = document.getElementById('full-sub');
  const fullPlayBtn = document.getElementById('full-play');
  const fullSlider = document.getElementById('full-slider');
  const fullTimeCur = document.getElementById('full-time-cur');
  const fullTimeTot = document.getElementById('full-time-tot');
  
  // Format MM:SS
  function formatTime(secs) {
    if(isNaN(secs) || !isFinite(secs)) return '0:00';
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return m + ':' + s.toString().padStart(2, '0');
  }

  // Update UI logic
  function updatePlayerUI() {
    miniPlayBtn.textContent = playing ? '⏸' : '▶';
    fullPlayBtn.textContent = playing ? '⏸' : '▶';
  }
  
  function togglePlay() {
    if(!currentKatha) return;
    if(playing) {
      audioPlayer.pause();
      playing = false;
    } else {
      audioPlayer.play();
      playing = true;
    }
    updatePlayerUI();
  }

  // Event Listeners for Mini Player
  miniPlayBtn.addEventListener('click', (e) => {
    e.stopPropagation(); // prevent opening full screen
    togglePlay();
  });
  
  document.getElementById('mini-player-expand').addEventListener('click', () => {
    fullPlayer.classList.remove('hidden');
  });
  
  // Event Listeners for Full Player
  fullCloseBtn.addEventListener('click', () => {
    fullPlayer.classList.add('hidden');
  });
  
  fullPlayBtn.addEventListener('click', togglePlay);
  
  // Seeking
  fullSlider.addEventListener('input', (e) => {
    if(!audioPlayer.duration) return;
    const pct = e.target.value;
    audioPlayer.currentTime = (pct / 100) * audioPlayer.duration;
  });
  
  // Audio events
  audioPlayer.addEventListener('timeupdate', () => {
    if(audioPlayer.duration) {
      const pct = (audioPlayer.currentTime / audioPlayer.duration) * 100;
      if(miniProgress) miniProgress.style.width = pct + '%';
      
      // Don't update slider if user is currently dragging it (basic implementation)
      fullSlider.value = pct;
      fullTimeCur.textContent = formatTime(audioPlayer.currentTime);
      fullTimeTot.textContent = formatTime(audioPlayer.duration);
    }
  });
  
  audioPlayer.addEventListener('loadedmetadata', () => {
    fullTimeTot.textContent = formatTime(audioPlayer.duration);
  });
  
  audioPlayer.addEventListener('ended', () => {
    playing = false;
    updatePlayerUI();
  });

  // Play Katha function
  function playKatha(k){
    if (currentKatha && currentKatha.id === k.id) {
       togglePlay();
       return;
    }
    currentKatha = k;
    playing = true;
    audioPlayer.src = k.url;
    audioPlayer.play();
    
    // Update Mini
    miniThumb.textContent = k.emoji;
    miniTitle.textContent = k.title;
    miniSub.textContent = k.title;
    miniPlayer.classList.remove('hidden');
    
    // Update Full
    fullThumb.textContent = k.emoji;
    fullTitle.textContent = k.title;
    fullSub.textContent = k.title;
    fullSlider.value = 0;
    fullTimeCur.textContent = '0:00';
    
    updatePlayerUI();
  }

  // Build grid
  function renderGrid(list){
    grid.innerHTML = '';
    list.forEach(k => {
      const card = document.createElement('button');
      card.className = 'katha-card';
      const isSaved = savedKatha.includes(k.id);
      card.innerHTML = \`
        <div class="katha-thumb-wrap">
          <div class="katha-thumb">\${k.emoji}</div>
          <button class="katha-bookmark\${isSaved?' saved':''}" data-id="\${k.id}" title="Save">🔖</button>
          <div class="katha-play-count">▶ \${k.plays}</div>
        </div>
        <div class="katha-card-title">\${k.title}</div>\`;
      card.addEventListener('click', () => playKatha(k));
      card.querySelector('.katha-bookmark').addEventListener('click', e => {
        e.stopPropagation();
        const btn = e.currentTarget;
        const idx = savedKatha.indexOf(k.id);
        if(idx === -1){ savedKatha.push(k.id); btn.classList.add('saved'); showToast('कथा सेव हो गई'); }
        else{ savedKatha.splice(idx,1); btn.classList.remove('saved'); showToast('कथा हटा दी गई'); }
        localStorage.setItem('bhakti_katha_saved', JSON.stringify(savedKatha));
      });
      grid.appendChild(card);
    });
  }

  renderGrid(KATHA_LIST);

  // Search
  document.getElementById('katha-search')?.addEventListener('input', e => {
    const q = e.target.value.trim().toLowerCase();
    renderGrid(q ? KATHA_LIST.filter(k => k.title.toLowerCase().includes(q)) : KATHA_LIST);
  });
}
\n`;

  code = code.replace(oldLogic, newLogic);
  fs.writeFileSync('app.js', code, 'utf8');
  console.log("Rewrote initKatha successfully!");
} else {
  console.log("Could not parse start/end strings.");
}
