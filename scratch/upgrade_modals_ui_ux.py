# -*- coding: utf-8 -*-
"""
Script to upgrade UI/UX and scroll behavior for:
1. Aarti & Mantra Selection Modal (#aarti-mantra-selection-modal)
2. PadaBandham Word Grid Game Modal (#padabandham-game-modal)
"""

import os
import re

APP_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"

def main():
    print("Starting UI/UX & scroll overhaul...")
    index_path = os.path.join(APP_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Ensure .app-header hiding CSS is in <style> in <head>
    header_hide_css = """
/* ══════════════════════════════════════════════════════════════════
   🚫 FULLSCREEN GAME & MODAL OVERLAY: HIDE APP HEADER & BOTTOM DOCK
   ══════════════════════════════════════════════════════════════════ */
body.game-modal-open .app-header,
body:has(#aarti-mantra-selection-modal[style*="flex"]) .app-header,
body:has(#aarti-mantra-selection-modal.active) .app-header,
body:has(#aarti-mantra-game-arena[style*="flex"]) .app-header,
body:has(#aarti-mantra-game-arena.active) .app-header,
body:has(#padabandham-game-modal[style*="flex"]) .app-header,
body:has(#padabandham-game-modal.active) .app-header,
body:has(#jigsaw-game-modal[style*="flex"]) .app-header,
body:has(#jigsaw-game-modal.active) .app-header,
body:has(#match-game-modal[style*="flex"]) .app-header,
body:has(#match-game-modal.active) .app-header,
body:has(#phool-arpan-arena[style*="flex"]) .app-header,
body:has(#phool-arpan-arena.active) .app-header {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transform: translateY(-120%) !important;
}

body.game-modal-open .curved-fluid-bottom-nav,
body.game-modal-open .bottom-nav,
body.game-modal-open .app-bottom-nav {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transform: translate(-50%, 150%) !important;
}
"""

    if "/* 🚫 FULLSCREEN GAME & MODAL OVERLAY: HIDE APP HEADER & BOTTOM DOCK */" not in html:
        # Insert right before </head>
        html = html.replace("</head>", f"<style>{header_hide_css}</style>\n</head>", 1)
        print("Inserted fullscreen game header-hiding CSS into <head>.")

    # 2. Extract PadaBandham modal + Win dialog from inside <main>
    # Search for start of PadaBandham modal and end of dialog
    pada_start = html.find('<!-- ══════════ 📖 3. PADABANDHAM WORD GRID MODAL (वैदिक शब्द संधान) ══════════ -->')
    pada_end = html.find('<!-- ══════════ 🌸 4. PHOOL ARPAN GAME ARENA (फूल अर्पण खेल) ══════════ -->')
    
    # 3. Extract Aarti & Mantra game module from inside <main>
    aarti_start = html.find('<!-- ══════════ 🪔 AARTI & MANTRA PUZZLE GAME MODULE (आरती व मन्त्र पहेली) ══════════ -->')
    aarti_end = html.find('<section id="page-aarti" class="page">')

    pada_block = ""
    aarti_block = ""

    if pada_start != -1 and pada_end != -1 and pada_start < pada_end:
        pada_block = html[pada_start:pada_end].strip()
        print(f"Found PadaBandham block ({len(pada_block)} chars).")

    if aarti_start != -1 and aarti_end != -1 and aarti_start < aarti_end:
        aarti_block = html[aarti_start:aarti_end].strip()
        print(f"Found Aarti block ({len(aarti_block)} chars).")

    # If both found in <main>, remove them from original location and place before </body>
    if pada_block and aarti_block:
        # Remove aarti first (since it's after pada in index.html)
        html = html[:aarti_start] + html[aarti_end:]
        # Recalculate pada locations
        p_start = html.find('<!-- ══════════ 📖 3. PADABANDHAM WORD GRID MODAL (वैदिक शब्द संधान) ══════════ -->')
        p_end = html.find('<!-- ══════════ 🌸 4. PHOOL ARPAN GAME ARENA (फूल अर्पण खेल) ══════════ -->')
        if p_start != -1 and p_end != -1:
            html = html[:p_start] + html[p_end:]

        # Now polish PadaBandham block inline style
        old_pada_style = 'id="padabandham-game-modal" class="epic-game-modal-overlay" style="display:none; z-index:100250 !important; background:rgba(12,4,24,0.94); backdrop-filter:blur(18px); -webkit-backdrop-filter:blur(18px); position:fixed; inset:0; align-items:center; justify-content:center; padding:12px; overflow-y:auto;"'
        new_pada_style = 'id="padabandham-game-modal" class="epic-game-modal-overlay" style="display:none; z-index:100250 !important; background:rgba(12,4,24,0.96); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); position:fixed; inset:0; flex-direction:column; align-items:center; justify-content:flex-start; padding:max(16px, env(safe-area-inset-top)) 12px calc(90px + env(safe-area-inset-bottom)); overflow-y:auto; -webkit-overflow-scrolling:touch; overscroll-behavior-y:contain; touch-action:pan-y; box-sizing:border-box;"'
        pada_block = pada_block.replace(old_pada_style, new_pada_style)

        # Place them before </body>
        combined_modals = f"\n\n    {pada_block}\n\n    {aarti_block}\n\n"
        html = html.replace("</body>", f"{combined_modals}</body>", 1)
        print("Moved PadaBandham and Aarti modals outside <main> to direct children of <body>.")

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Updated index.html successfully.")
    else:
        print("Warning: Blocks not found at expected positions in index.html, skipping extraction.")

if __name__ == "__main__":
    main()
