# -*- coding: utf-8 -*-
"""
Patch aarti_mantra_puzzle.css and aarti_mantra_puzzle_engine.js for supreme UI/UX & fluid momentum scrolling.
"""

import os
import re

APP_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"

def patch_aarti_puzzle_css():
    css_path = os.path.join(APP_DIR, "aarti_mantra_puzzle.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Append our Supreme Divine Overrides at the very bottom of aarti_mantra_puzzle.css
    override_css = """

/* ══════════════════════════════════════════════════════════════════════════════
   🌟 SUPREME DIVINE OVERHAUL: AARTI & MANTRA SELECTION HUB (UI/UX & SCROLL FIX)
   ══════════════════════════════════════════════════════════════════════════════ */

.amp-selection-modal {
  display: none;
  position: fixed !important;
  inset: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  height: 100dvh !important;
  z-index: 100250 !important;
  background: #140726 !important;
  flex-direction: column !important;
  overflow: hidden !important;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans Devanagari", sans-serif;
  box-sizing: border-box !important;
}

/* ── Top Header with Safe Area Notch Support ── */
.amp-selection-header {
  background: linear-gradient(135deg, #FF6F00 0%, #FF8F00 50%, #FFA000 100%) !important;
  padding: max(14px, env(safe-area-inset-top)) 16px 12px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  box-shadow: 0 4px 22px rgba(255, 111, 0, 0.45) !important;
  color: #FFFFFF !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 30 !important;
  flex-shrink: 0 !important;
}

.amp-header-left {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  min-width: 0 !important;
}

.amp-header-title {
  margin: 0 !important;
  font-size: 1.18rem !important;
  font-weight: 900 !important;
  color: #FFFFFF !important;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3) !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.amp-header-right {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  flex-shrink: 0 !important;
}

.amp-back-btn {
  background: rgba(255, 255, 255, 0.22) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.6) !important;
  color: #FFFFFF !important;
  width: 36px !important;
  height: 36px !important;
  border-radius: 50% !important;
  font-size: 1.15rem !important;
  font-weight: 900 !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: all 0.2s ease !important;
  flex-shrink: 0 !important;
}

.amp-back-btn:active {
  transform: scale(0.92) !important;
  background: rgba(255, 255, 255, 0.4) !important;
}

.amp-streak-pill {
  background: rgba(0, 0, 0, 0.25) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1px solid rgba(255, 255, 255, 0.4) !important;
  border-radius: 18px !important;
  padding: 5px 12px !important;
  font-size: 0.84rem !important;
  font-weight: 800 !important;
  color: #FFFFFF !important;
  display: flex !important;
  align-items: center !important;
  gap: 5px !important;
  white-space: nowrap !important;
}

/* ── Sticky Sub-Header Wrappers (Search & Category Chips) ── */
.amp-search-wrap {
  padding: 10px 16px 6px !important;
  background: #140726 !important;
  flex-shrink: 0 !important;
}

.amp-search-box {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.8px solid rgba(245, 158, 11, 0.4) !important;
  border-radius: 24px !important;
  padding: 9px 16px !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3) !important;
}

.amp-search-box input {
  flex: 1 !important;
  border: none !important;
  outline: none !important;
  background: transparent !important;
  font-size: 0.94rem !important;
  font-family: inherit !important;
  color: #FFFDF8 !important;
}

.amp-search-box input::placeholder {
  color: #94A3B8 !important;
}

.amp-categories-bar {
  display: flex !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  scrollbar-width: none !important;
  padding: 6px 16px 12px !important;
  gap: 8px !important;
  background: #140726 !important;
  touch-action: pan-x !important;
  flex-shrink: 0 !important;
}

.amp-categories-bar::-webkit-scrollbar {
  display: none !important;
}

.amp-cat-chip {
  padding: 8px 18px !important;
  border-radius: 20px !important;
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
  color: #FDE68A !important;
  font-size: 0.88rem !important;
  font-weight: 800 !important;
  white-space: nowrap !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2) !important;
}

.amp-cat-chip.active {
  background: linear-gradient(135deg, #FF8C00 0%, #D97706 100%) !important;
  border-color: #FEF3C7 !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.5) !important;
  transform: scale(1.04) !important;
}

/* ── 🚀 ULTRA-SMOOTH MOMENTUM SCROLL CONTAINER ── */
.amp-items-container {
  flex: 1 1 0px !important;
  min-height: 0 !important;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  overscroll-behavior-y: contain !important;
  touch-action: pan-y !important;
  padding: 8px 14px 140px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  max-width: 620px !important;
  width: 100% !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
}

/* ── Glowing Devotional Hero Marquee Banner ── */
.amp-hero-banner {
  border-radius: 20px !important;
  padding: 14px 16px !important;
  background: linear-gradient(135deg, rgba(255, 111, 0, 0.22) 0%, rgba(109, 40, 217, 0.22) 100%) !important;
  border: 1.8px solid #F59E0B !important;
  box-shadow: 0 6px 22px rgba(0, 0, 0, 0.4), inset 0 0 16px rgba(245, 158, 11, 0.18) !important;
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  margin-bottom: 4px !important;
}

.amp-hero-icon {
  font-size: 2.2rem !important;
  flex-shrink: 0 !important;
  filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.6)) !important;
}

.amp-hero-title {
  font-size: 1.15rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  margin-bottom: 3px !important;
  text-shadow: 0 0 12px rgba(245, 158, 11, 0.5) !important;
}

.amp-hero-desc {
  font-size: 0.82rem !important;
  color: #FDE68A !important;
  line-height: 1.4 !important;
}

/* ── Sacred Aarti/Mantra Item Cards ── */
.amp-item-card {
  background: linear-gradient(145deg, #270C42 0%, #170526 100%) !important;
  border-radius: 20px !important;
  border: 1.6px solid rgba(245, 158, 11, 0.35) !important;
  padding: 12px 14px !important;
  min-height: 78px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 12px !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
  cursor: pointer !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease !important;
  position: relative !important;
  box-sizing: border-box !important;
  flex-shrink: 0 !important;
}

.amp-item-card:hover {
  transform: translateY(-2px) !important;
  border-color: #F59E0B !important;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.3) !important;
}

.amp-item-card.is-locked {
  opacity: 0.8 !important;
  filter: grayscale(0.15) !important;
}

.amp-item-card-left {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  flex: 1 1 auto !important;
  min-width: 0 !important;
}

.amp-item-thumb {
  width: 52px !important;
  height: 52px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
  border: 2px solid #F59E0B !important;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.4) !important;
  flex-shrink: 0 !important;
}

.amp-item-info {
  display: flex !important;
  flex-direction: column !important;
  gap: 3px !important;
  min-width: 0 !important;
  flex: 1 1 auto !important;
}

.amp-item-badge-row {
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  margin-bottom: 2px !important;
}

.amp-level-badge {
  background: rgba(245, 158, 11, 0.25) !important;
  color: #FDE68A !important;
  border: 1px solid rgba(245, 158, 11, 0.45) !important;
  font-size: 0.72rem !important;
  font-weight: 800 !important;
  padding: 2px 8px !important;
  border-radius: 8px !important;
}

.amp-cat-badge {
  background: rgba(255, 255, 255, 0.1) !important;
  color: #E2E8F0 !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  padding: 2px 8px !important;
  border-radius: 8px !important;
}

.amp-item-title {
  margin: 0 !important;
  font-size: 1.05rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  line-height: 1.3 !important;
}

.amp-item-meta {
  font-size: 0.8rem !important;
  font-weight: 700 !important;
  color: #FDE68A !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  line-height: 1.2 !important;
  white-space: nowrap !important;
}

.amp-item-card-right {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-end !important;
  justify-content: center !important;
  gap: 6px !important;
  flex-shrink: 0 !important;
}

.amp-play-btn {
  background: linear-gradient(135deg, #FF8C00 0%, #D97706 100%) !important;
  color: #FFFFFF !important;
  border: 1.2px solid #FDE68A !important;
  font-size: 0.86rem !important;
  font-weight: 900 !important;
  padding: 8px 16px !important;
  border-radius: 20px !important;
  cursor: pointer !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.45) !important;
  transition: all 0.2s ease !important;
  display: flex !important;
  align-items: center !important;
  gap: 5px !important;
  white-space: nowrap !important;
}

.amp-play-btn:active {
  transform: scale(0.95) !important;
}

.amp-lock-icon {
  width: 40px !important;
  height: 40px !important;
  border-radius: 50% !important;
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 1.15rem !important;
  color: #FDE68A !important;
  flex-shrink: 0 !important;
}
"""
    if "/* 🌟 SUPREME DIVINE OVERHAUL: AARTI & MANTRA SELECTION HUB" not in css:
        css += override_css
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("Appended supreme divine overhaul to aarti_mantra_puzzle.css.")
    else:
        print("aarti_mantra_puzzle.css already contains supreme divine overhaul.")

def patch_aarti_puzzle_engine():
    js_path = os.path.join(APP_DIR, "aarti_mantra_puzzle_engine.js")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    # 1. Update title string to pure Hindi without parentheses
    js = js.replace(
        "titleEl.innerHTML = state.currentType === 'aarti' \n        ? '🪔 दिव्य आरती पहेली (Aarti Game)' \n        : '🕉️ दिव्य मन्त्र पहेली (Mantra Game)';",
        "titleEl.innerHTML = state.currentType === 'aarti' \n        ? '🪔 दिव्य आरती पहेली' \n        : '🕉️ दिव्य मन्त्र पहेली';"
    )
    js = js.replace(
        "titleEl.innerHTML = state.currentType === 'aarti' ? '🪔 दिव्य आरती पहेली (Aarti Game)' : '🕉️ दिव्य मन्त्र पहेली (Mantra Game)';",
        "titleEl.innerHTML = state.currentType === 'aarti' ? '🪔 दिव्य आरती पहेली' : '🕉️ दिव्य मन्त्र पहेली';"
    )

    # 2. Update hideNavs to add body class and setProperty display none !important
    old_hide = """  function hideNavs() {
    var nav = document.getElementById('curved-fluid-bottom-nav');
    if (nav) nav.classList.add('nav-hidden');
    var allNavs = document.querySelectorAll('.curved-fluid-bottom-nav, .app-bottom-nav, .bottom-nav');
    allNavs.forEach(function (el) { el.classList.add('nav-hidden'); });
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.display = 'none';
  }"""

    new_hide = """  function hideNavs() {
    document.body.classList.add('game-modal-open');
    var nav = document.getElementById('curved-fluid-bottom-nav');
    if (nav) nav.classList.add('nav-hidden');
    var allNavs = document.querySelectorAll('.curved-fluid-bottom-nav, .app-bottom-nav, .bottom-nav');
    allNavs.forEach(function (el) { el.classList.add('nav-hidden'); });
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.setProperty('display', 'none', 'important');
  }"""

    if old_hide in js:
        js = js.replace(old_hide, new_hide)
        print("Updated hideNavs in aarti_mantra_puzzle_engine.js.")

    # 3. Update restoreNavsIfExited
    old_restore = """    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.display = '';"""

    new_restore = """    document.body.classList.remove('game-modal-open');
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.removeProperty('display');"""

    if old_restore in js:
        js = js.replace(old_restore, new_restore)
        print("Updated restoreNavsIfExited in aarti_mantra_puzzle_engine.js.")

    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Patched aarti_mantra_puzzle_engine.js successfully.")

if __name__ == "__main__":
    patch_aarti_puzzle_css()
    patch_aarti_puzzle_engine()
