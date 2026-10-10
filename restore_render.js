const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const renderCode = `
  function renderGrid(list) {
    if(!grid) return;
    grid.innerHTML = '';
    list.forEach(k => {
      const isSaved = savedKatha.includes(k.id);
      const card = document.createElement('div');
      card.className = 'katha-card';
      card.innerHTML = \`
        <div class="katha-icon">\${k.emoji}</div>
        <button class="katha-save \${isSaved?'saved':''}" data-id="\${k.id}">\${isSaved?'★':'☆'}</button>
        <div class="katha-stats">▶ \${k.plays}</div>
        <div class="katha-title">\${k.title}</div>
        <div class="katha-ep">\${k.ep} एपिसोड</div>
      \`;
      card.addEventListener('click', (e) => {
        if(e.target.classList.contains('katha-save')){
           const idx = savedKatha.indexOf(k.id);
           if(idx>-1) savedKatha.splice(idx,1); else savedKatha.push(k.id);
           localStorage.setItem('bhakti_katha_saved', JSON.stringify(savedKatha));
           e.target.classList.toggle('saved');
           e.target.textContent = savedKatha.includes(k.id) ? '★' : '☆';
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
`;

code = code.replace(
  "audioPlayer.addEventListener('timeupdate', () => {",
  renderCode + "\n  audioPlayer.addEventListener('timeupdate', () => {"
);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Restored renderGrid and search logic.');
