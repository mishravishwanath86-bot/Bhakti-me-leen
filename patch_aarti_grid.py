import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

app_js = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js")
with open(app_js, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Enhance buildDeityGrid or openDeityContent
interceptor_code = """
// Aarti Deity Grid Click Interceptor for Multi-Aarti Options
const originalBuildDeityGrid = window.buildDeityGrid;
window.buildDeityGrid = function(containerId, items, contentPrefix, fromPage) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = '';
  items.forEach(d => {
    const card = document.createElement('button');
    card.className = 'deity-card';
    const imgHtml = d.img 
      ? `<img src="${d.img}" alt="${d.name}" class="deity-card-img" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'" /><div class="deity-card-emoji" style="display:none">${d.emoji || '🕉️'}</div>`
      : `<div class="deity-card-emoji">${d.emoji || '🕉️'}</div>`;
    
    card.innerHTML = `${imgHtml}<span class="deity-card-name">${d.name}</span>`;
    
    card.addEventListener('click', () => {
      if (contentPrefix === 'aarti') {
        if (d.id === 'ganesh' || d.id === 'ganesha') {
          openAartiCollectionModal('ganesh');
          return;
        }
        if (d.id === 'hanuman') {
          openAartiCollectionModal('hanuman');
          return;
        }
      }
      const contentKey = d.contentKey || (contentPrefix + '_' + d.id);
      openReader(contentKey, fromPage);
    });
    container.appendChild(card);
  });
};
"""

if "Aarti Deity Grid Click Interceptor" not in js:
    js += "\n" + interceptor_code
    with open(app_js, 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Added Aarti deity grid interceptor to app.js")
else:
    print("Interceptor already present")
