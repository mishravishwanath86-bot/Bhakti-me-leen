const fs = require('fs');

const css = `
/* =========================================================
   🎵 GLASSMORPHISM MUSIC PLAYER UI
   ========================================================= */

/* 1. FLOATING MINI PLAYER */
.glass-mini-player {
  position: fixed;
  bottom: 75px; /* Above bottom nav */
  left: 15px;
  right: 15px;
  height: 64px;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 16px;
  display: flex;
  align-items: center;
  padding: 8px 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.4);
  z-index: 100;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.3s;
  overflow: hidden; /* For progress bar at bottom */
}
.glass-mini-player.hidden {
  transform: translateY(150%);
  opacity: 0;
  pointer-events: none;
}
.glass-mini-content {
  display: flex;
  align-items: center;
  flex: 1;
  min-width: 0;
  cursor: pointer;
}
.glass-mini-thumb {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #a855f7, #ec4899);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-right: 12px;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(236, 72, 153, 0.3);
}
.glass-mini-thumb img {
  width: 100%; height: 100%; object-fit: cover; border-radius: 12px;
}
.glass-mini-info {
  flex: 1;
  min-width: 0;
}
.glass-mini-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #1e293b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 2px;
}
.glass-mini-sub {
  font-size: 0.75rem;
  color: #64748b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.glass-mini-controls {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-left: 10px;
}
.glass-btn-icon {
  background: none; border: none;
  font-size: 1.2rem;
  color: #94a3b8;
  padding: 4px;
}
.glass-btn-play {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: #a855f7;
  color: #fff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  box-shadow: 0 4px 12px rgba(168, 85, 247, 0.4);
  transition: transform 0.1s;
}
.glass-btn-play:active { transform: scale(0.9); }

/* Progress bar at the very bottom of mini player */
.glass-mini-progress {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 3px;
  background: rgba(0,0,0,0.05);
}
.glass-mini-progress-fill {
  height: 100%;
  width: 0%;
  background: #a855f7;
  transition: width 0.1s linear;
}


/* 2. FULL SCREEN PLAYER */
.glass-full-player {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(135deg, #2e1065 0%, #701a75 50%, #831843 100%);
  z-index: 9999;
  display: flex;
  flex-direction: column;
  transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  transform: translateY(0);
}
.glass-full-player.hidden {
  transform: translateY(100%);
}

.glass-fp-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  padding-top: max(20px, env(safe-area-inset-top));
}
.glass-fp-icon-btn {
  background: rgba(255,255,255,0.1);
  border: none;
  width: 40px; height: 40px;
  border-radius: 50%;
  color: #fff;
  font-size: 1.1rem;
  display: flex; align-items: center; justify-content: center;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.glass-fp-now-playing {
  color: #fff;
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  opacity: 0.9;
}

.glass-fp-artwork-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.glass-fp-artwork-ring {
  width: 260px;
  height: 260px;
  border-radius: 50%;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 40px rgba(0,0,0,0.3), inset 0 0 20px rgba(255,255,255,0.05);
}
.glass-fp-artwork {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  background: linear-gradient(135deg, #a855f7, #ec4899);
  color: #fff;
  font-size: 5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
  overflow: hidden;
}
.glass-fp-artwork img {
  width: 100%; height: 100%; object-fit: cover;
}

.glass-fp-info {
  text-align: center;
  padding: 0 30px;
  margin-bottom: 30px;
}
.glass-fp-title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 8px;
  text-shadow: 0 2px 10px rgba(0,0,0,0.3);
}
.glass-fp-sub {
  font-size: 1rem;
  color: rgba(255,255,255,0.7);
  font-weight: 500;
}

.glass-fp-progress-container {
  padding: 0 30px;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 40px;
}
.glass-fp-time {
  font-size: 0.75rem;
  color: rgba(255,255,255,0.6);
  font-variant-numeric: tabular-nums;
}
.glass-fp-slider {
  flex: 1;
  -webkit-appearance: none;
  background: transparent;
  height: 30px;
  margin: 0;
  display: flex; align-items: center;
}
.glass-fp-slider::-webkit-slider-runnable-track {
  width: 100%;
  height: 4px;
  background: rgba(255,255,255,0.2);
  border-radius: 2px;
}
.glass-fp-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 14px;
  width: 14px;
  border-radius: 50%;
  background: #fff;
  margin-top: -5px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

.glass-fp-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 0 30px;
  margin-bottom: 60px;
}
.glass-fp-ctrl-sm {
  background: none; border: none;
  color: rgba(255,255,255,0.5);
  font-size: 1.2rem;
  padding: 10px;
}
.glass-fp-ctrl-md {
  background: none; border: none;
  color: #fff;
  font-size: 1.8rem;
  padding: 10px;
}
.glass-fp-ctrl-lg {
  width: 72px; height: 72px;
  border-radius: 50%;
  background: #a855f7;
  background: linear-gradient(135deg, #a855f7, #ec4899);
  color: #fff;
  border: none;
  font-size: 2rem;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 10px 25px rgba(236, 72, 153, 0.4);
  transition: transform 0.1s;
}
.glass-fp-ctrl-lg:active { transform: scale(0.92); }

.glass-fp-lyrics-tab {
  margin-top: auto;
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top-left-radius: 30px;
  border-top-right-radius: 30px;
  padding: 15px;
  text-align: center;
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  display: flex; flex-direction: column; align-items: center;
}
.glass-fp-lyrics-handle {
  width: 40px; height: 5px;
  background: rgba(255,255,255,0.3);
  border-radius: 3px;
  margin-bottom: 15px;
}
`;

fs.appendFileSync('styles.css', css);
console.log("Appended Glassmorphism CSS to styles.css");
