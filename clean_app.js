const fs = require('fs');
const oldCode = fs.readFileSync('app.js', 'utf8');

const s1 = oldCode.indexOf('//  KATHA / PODCAST\n// ══════════════════════════════════════════════════════\n');
const s2 = oldCode.indexOf('// ══════════════════════════════════════════════════════\n//   ENGLISH CALENDAR  (Google Calendar style)');

if(s1 > -1 && s2 > -1) {
    const part1 = oldCode.substring(0, s1 + 162); // Include the header comments
    const part3 = oldCode.substring(s2);
    
    const part2 = `function initKatha(){
  const grid = document.getElementById('katha-grid');
  if(!grid) return;

  let savedKatha = JSON.parse(localStorage.getItem('bhakti_katha_saved') || '[]');
  let currentKatha = null, playing = false;
  let audioPlayer = new Audio();
  const miniPlayBtn = document.getElementById('mini-play');
  const timeDisp = document.getElementById('mini-time');
  const progFill = document.getElementById('mini-progress-fill');
  const miniPlayer = document.getElementById('mini-player');

  function formatTime(s){ if(isNaN(s))return '00:00'; let m=Math.floor(s/60); let sec=Math.floor(s%60); return m.toString().padStart(2,'0')+':'+sec.toString().padStart(2,'0'); }

  function renderGrid(list) {
    if(!grid) return;
    grid.innerHTML = '';
    list.forEach(k => {
      const isSaved = savedKatha.includes(k.id);
      const card = document.createElement('div');
      card.className = 'katha-card';
      card.innerHTML = \`
        <div class="katha-icon">\${k.emoji}</div>
        <button class="katha-save \${isSaved?'saved':''}" data-id="\${k.id}">\${isSaved?'🔖':'🔖'}</button>
        <div class="katha-stats">▶  \${k.plays}</div>
        <div class="katha-title">\${k.title}</div>
        <div class="katha-ep">\${k.ep} एपिसोड</div>
      \`;
      card.addEventListener('click', (e) => {
        if(e.target.classList.contains('katha-save')){
           const idx = savedKatha.indexOf(k.id);
           if(idx>-1) savedKatha.splice(idx,1); else savedKatha.push(k.id);
           localStorage.setItem('bhakti_katha_saved', JSON.stringify(savedKatha));
           e.target.classList.toggle('saved');
           return;
        }
        if(window.playKatha) window.playKatha(k);
      });
      grid.appendChild(card);
    });
  }

  renderGrid(KATHA_LIST);

  const search = document.getElementById('katha-search');
  if(search) {
      search.addEventListener('input', e => {
          const q = e.target.value.trim().toLowerCase();
          renderGrid(q ? KATHA_LIST.filter(k => k.title.toLowerCase().includes(q)) : KATHA_LIST);
      });
  }

  const featBtn = document.querySelector('.katha-feat-btn');
  if(featBtn) {
      featBtn.addEventListener('click', () => {
          if(window.playKatha) window.playKatha(KATHA_LIST[0]);
      });
  }

  audioPlayer.addEventListener('timeupdate', () => {
    if(!audioPlayer.duration) return;
    if(timeDisp) timeDisp.innerText = formatTime(audioPlayer.currentTime) + ' / ' + formatTime(audioPlayer.duration);
    if(progFill) progFill.style.width = ((audioPlayer.currentTime / audioPlayer.duration)*100) + '%';
  });

  audioPlayer.addEventListener('ended', () => { playing = false; updateMiniPlayerUI(); });

  miniPlayBtn?.addEventListener('click', () => {
    if(!currentKatha) return;
    if(playing) {
       audioPlayer.pause();
       playing = false;
    } else {
       audioPlayer.play();
       playing = true;
    }
    updateMiniPlayerUI();
  });

  function updateMiniPlayerUI() {
    if(miniPlayBtn) {
       miniPlayBtn.innerHTML = playing ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>' : '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
       miniPlayBtn.classList.toggle('playing', playing);
    }
  }

  window.playKatha = function(k){
    if (currentKatha && currentKatha.id === k.id) {
       if(playing) { audioPlayer.pause(); playing = false; }
       else { audioPlayer.play(); playing = true; }
       updateMiniPlayerUI();
       return;
    }
    currentKatha = k;
    playing = true;
    audioPlayer.src = k.url || 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg';
    audioPlayer.play();
    document.getElementById('mini-thumb').innerHTML = k.emoji;
    document.getElementById('mini-title').textContent = k.title;
    document.getElementById('mini-sub').textContent = 'Episode 1';
    if(miniPlayer) miniPlayer.classList.remove('hidden');
    updateMiniPlayerUI();
  }
}

`;
    
    fs.writeFileSync('app.js', part1 + part2 + part3, 'utf8');
    console.log("Restored clean app.js");
} else {
    console.log("Could not find boundary markers");
}
