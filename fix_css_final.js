const fs = require('fs');

// ---- Complete mini-player CSS update ----
let css = fs.readFileSync('styles.css', 'utf8');

// Remove old mini-player and progress bar css to rewrite clean
css = css.replace(/\.mini-progress-bar[\s\S]*?\.mini-player-time \{[\s\S]*?\}\n*/g, '');

// Add fresh clean version
css += `
/* ===================== MINI PLAYER ===================== */
.mini-player {
  position: fixed !important;
  bottom: var(--bottom-nav-h, 60px) !important;
  left: 0 !important; right: 0 !important;
  background: #1a0a00 !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.6rem !important;
  padding: 0.6rem 0.8rem !important;
  z-index: 900 !important;
  box-shadow: 0 -2px 12px rgba(0,0,0,0.5) !important;
}
.mini-player.hidden { display: none !important; }
.mini-progress-bar {
  position: absolute !important;
  top: 0 !important; left: 0 !important;
  width: 100% !important; height: 5px !important;
  background: rgba(255,255,255,0.15) !important;
  cursor: pointer !important;
  z-index: 10 !important;
}
.mini-progress-fill {
  height: 100% !important;
  width: 0% !important;
  background: #fbbf24 !important;
  transition: width 0.5s linear !important;
}
.mini-player-thumb {
  font-size: 1.8rem !important;
  width: 40px !important; height: 40px !important;
  flex-shrink: 0 !important;
  display: flex !important;
  align-items: center !important; justify-content: center !important;
}
.mini-player-info {
  flex: 1 !important;
  min-width: 0 !important;
}
.mini-player-title {
  font-size: 0.85rem !important;
  font-weight: 600 !important;
  color: #fff !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}
.mini-player-sub {
  font-size: 0.65rem !important;
  color: #fbbf24 !important;
  margin-top: 1px !important;
}
.mini-seek-btn {
  background: rgba(255,255,255,0.1) !important;
  border: none !important;
  border-radius: 50% !important;
  width: 34px !important; height: 34px !important;
  color: #fff !important;
  font-size: 0.75rem !important;
  cursor: pointer !important;
  display: flex !important; flex-direction: column !important;
  align-items: center !important; justify-content: center !important;
  flex-shrink: 0 !important;
}
.mini-play-btn {
  background: #f59e0b !important;
  border: none !important;
  border-radius: 50% !important;
  width: 38px !important; height: 38px !important;
  color: #fff !important;
  font-size: 1.1rem !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important; justify-content: center !important;
  flex-shrink: 0 !important;
  box-shadow: 0 2px 8px rgba(245,158,11,0.5) !important;
}
`;

fs.writeFileSync('styles.css', css, 'utf8');
console.log('CSS updated!');
