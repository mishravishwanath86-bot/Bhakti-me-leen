import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

styles_css_path = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\styles.css")

with open(styles_css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

player_luxury_css = """
/* ══════════════════════════════════════════════════════════════════
   🎧 LUXURY GLASS FULL-SCREEN PLAYER (SPOTIFY/APPLE MUSIC GRADE)
   ══════════════════════════════════════════════════════════════════ */
.glass-full-player-modal {
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: radial-gradient(circle at 50% 20%, rgba(42, 13, 82, 0.96) 0%, rgba(19, 5, 38, 0.98) 55%, rgba(8, 2, 18, 0.99) 100%);
  backdrop-filter: blur(35px);
  -webkit-backdrop-filter: blur(35px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  overflow-y: auto;
  padding: 1.2rem 1.4rem 2.5rem;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-player-stage {
  width: 100%;
  max-width: 440px;
  display: flex;
  flex-direction: column;
  margin: auto 0;
}

/* Topbar */
.glass-player-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 1.4rem;
}

.glass-topbar-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.3);
  color: #FDE68A;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.glass-topbar-btn:hover {
  background: rgba(248, 200, 59, 0.2);
  transform: scale(1.08);
}

.glass-player-heading {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 700;
  color: #FDE68A;
  letter-spacing: 0.5px;
  text-shadow: 0 0 15px rgba(248, 200, 59, 0.4);
}

/* Dedicated Mode Switch Pill (Audio vs Video) */
.glass-mode-toggle-btn {
  background: linear-gradient(135deg, rgba(248, 200, 59, 0.18) 0%, rgba(217, 119, 6, 0.22) 100%);
  border: 1.5px solid #F8C83B;
  color: #FDE68A;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.78rem;
  font-weight: 800;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  box-shadow: 0 4px 12px rgba(248, 200, 59, 0.25);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-mode-toggle-btn:hover {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  transform: scale(1.05);
}

/* Centerpiece Deity Artwork (Audio Mode) */
.glass-player-centerpiece {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.6rem;
  width: 100%;
}

.glass-disk-halo {
  width: 250px;
  height: 250px;
  border-radius: 28px;
  background: linear-gradient(145deg, #2D104E 0%, #150628 100%);
  border: 2px solid rgba(248, 200, 59, 0.45);
  padding: 8px;
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.8), 0 0 35px rgba(248, 200, 59, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.glass-artwork-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 22px;
  box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
}

/* Video Stage (Video Mode) */
.glass-youtube-container {
  width: 100%;
  border-radius: 20px;
  overflow: hidden;
  border: 2px solid rgba(248, 200, 59, 0.4);
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.8);
  margin-bottom: 1.5rem;
  aspect-ratio: 16 / 9;
}

.glass-youtube-container iframe {
  width: 100%;
  height: 100%;
  border: none;
}

/* Track Metadata */
.glass-track-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.4rem;
}

.glass-track-name {
  font-size: 1.18rem;
  font-weight: 800;
  color: #FFFDF8;
  line-height: 1.35;
  margin-bottom: 4px;
}

.glass-track-artist {
  font-size: 0.82rem;
  color: #FDE68A;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.glass-fav-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.3);
  color: #FDE68A;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  font-size: 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.glass-fav-btn:hover {
  transform: scale(1.1);
  background: rgba(236, 72, 153, 0.2);
  border-color: #F472B6;
}

/* ⏱️ TIMELINE & SCRUBBER */
.glass-scrub-box {
  width: 100%;
  margin-bottom: 1.4rem;
}

.glass-time-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.78rem;
  font-weight: 700;
  color: #FDE68A;
  margin-bottom: 6px;
  letter-spacing: 0.5px;
}

.glass-seekbar {
  width: 100%;
  height: 6px;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.15);
  outline: none;
  -webkit-appearance: none;
  cursor: pointer;
  position: relative;
}

.glass-seekbar::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: radial-gradient(circle, #FFFDF8 20%, #F8C83B 80%);
  border: 2px solid #D97706;
  box-shadow: 0 0 10px rgba(248, 200, 59, 0.8);
  cursor: pointer;
  transition: transform 0.1s ease;
}

.glass-seekbar::-webkit-slider-thumb:hover {
  transform: scale(1.25);
}

/* Controls Row */
.glass-controls-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  width: 100%;
}

.glass-ctrl-btn {
  background: transparent;
  border: none;
  color: #FDE68A;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.glass-ctrl-secondary {
  font-size: 1.25rem;
  opacity: 0.75;
}

.glass-ctrl-secondary:hover {
  opacity: 1;
  transform: scale(1.1);
}

.glass-ctrl-primary {
  font-size: 1.6rem;
}

.glass-ctrl-primary:hover {
  transform: scale(1.15);
  color: #FFF;
}

.glass-ctrl-skip {
  font-size: 0.8rem;
  font-weight: 800;
  color: #FBCFE8;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.25);
  padding: 4px 8px;
  border-radius: 12px;
}

.glass-ctrl-skip:hover {
  background: rgba(248, 200, 59, 0.2);
  color: #FDE68A;
  transform: scale(1.08);
}

.glass-main-play-btn {
  width: 66px;
  height: 66px;
  border-radius: 50%;
  background: linear-gradient(135deg, #F8C83B 0%, #EA580C 100%);
  border: none;
  color: #1A0B2E;
  font-size: 1.6rem;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 6px 25px rgba(248, 200, 59, 0.55), 0 0 15px rgba(234, 88, 12, 0.4);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-main-play-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 8px 30px rgba(248, 200, 59, 0.75);
}

/* Lyrics Drawer */
.glass-lyrics-tab-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(248, 200, 59, 0.3);
  color: #FDE68A;
  width: 100%;
  padding: 10px 16px;
  border-radius: 18px;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.glass-lyrics-tab-btn:hover {
  background: rgba(248, 200, 59, 0.15);
}

.glass-lyrics-drawer {
  background: rgba(16, 5, 32, 0.85);
  border: 1px solid rgba(248, 200, 59, 0.25);
  border-radius: 18px;
  padding: 1.2rem;
  margin-top: 0.8rem;
  max-height: 220px;
  overflow-y: auto;
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + player_luxury_css)

print("✓ Injected luxury player CSS to styles.css")
