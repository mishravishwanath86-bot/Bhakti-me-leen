import sys, re, shutil, os, time
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("🌞 COMPLETE LIGHT MODE FIX — All Dark Elements Override")
print("=" * 70)

# Backup
ts = int(time.time())
shutil.copy('styles.css', f'styles.css.bak_lightfix_{ts}')
print(f"✅ Backup: styles.css.bak_lightfix_{ts}")

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# ══════════════════════════════════════════════════════════════════
# COMPREHENSIVE LIGHT THEME OVERRIDE — covers ALL missed elements
# ══════════════════════════════════════════════════════════════════
LIGHT_OVERRIDE = """

/* ══════════════════════════════════════════════════════════════════════════════
   ☀️ COMPLETE LIGHT THEME OVERRIDE — ALL ELEMENTS
   ══════════════════════════════════════════════════════════════════════════════ */

/* Base Body & HTML */
body.theme-light,
body.theme-light html,
html[data-theme="light"] body {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

/* All pages / sections */
body.theme-light .page,
body.theme-light .page-content,
body.theme-light .app-main,
body.theme-light section {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

/* ── CARDS ── */
body.theme-light .grid-card,
body.theme-light .cat-card,
body.theme-light .fest-card,
body.theme-light .vrat-card,
body.theme-light .katha-card,
body.theme-light .katha-card-luxury,
body.theme-light .bhajan-card,
body.theme-light .setting-card,
body.theme-light .gallery-card-item,
body.theme-light .amrit-mood-card,
body.theme-light .panchang-card,
body.theme-light .top10-card,
body.theme-light .today-panchang-card,
body.theme-light .tpc-card,
body.theme-light .muhurat-home-card,
body.theme-light .temple-card-royal,
body.theme-light .gallery-card-royal,
body.theme-light .profile-royal-card,
body.theme-light .sadhana-hub-container {
  background: #FFFFFF !important;
  color: #2D1400 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.22) !important;
  box-shadow: 0 4px 16px rgba(180, 83, 9, 0.08) !important;
}

/* ── COVERFLOW / HERO ── */
body.theme-light .coverflow-card {
  background: #FFF8E8 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  color: #2D1400 !important;
  box-shadow: 0 8px 30px rgba(180, 83, 9, 0.1) !important;
}

body.theme-light .bhakti-leen-hero {
  background: radial-gradient(circle at 50% 30%, #FFEFC2 0%, #FFF5D6 50%, #FFFBF0 100%) !important;
}

body.theme-light .gallery-hero-stage {
  background: linear-gradient(180deg, #FFF3D0 0%, #FFFBF0 100%) !important;
}

body.theme-light .gallery-lightbox-img-frame {
  background: #FFF8E8 !important;
}

body.theme-light .gallery-card-img-wrap {
  background: #FFF3D0 !important;
}

/* ── AUTH / ONBOARDING ── */
body.theme-light #auth-modal,
body.theme-light .auth-card {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.25) !important;
  box-shadow: 0 20px 60px rgba(180, 83, 9, 0.15) !important;
}

body.theme-light .auth-logo-img {
  filter: drop-shadow(0 4px 12px rgba(217, 119, 6, 0.3)) !important;
}

body.theme-light #onboarding-overlay {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

/* ── MEDIA PLAYERS ── */
body.theme-light .mini-player,
body.theme-light .glass-mini-player,
body.theme-light #glass-mini-player {
  background: rgba(255, 248, 232, 0.97) !important;
  border: 1.5px solid rgba(217, 119, 6, 0.3) !important;
  box-shadow: 0 8px 32px rgba(180, 83, 9, 0.15) !important;
  color: #2D1400 !important;
}

body.theme-light .glass-full-player,
body.theme-light .glass-full-player-modal,
body.theme-light #glass-full-player-modal {
  background: radial-gradient(circle at 50% 30%, #FFF3D0 0%, #FFFBF0 70%, #FFF5D6 100%) !important;
  border: 1.5px solid rgba(217, 119, 6, 0.3) !important;
  color: #2D1400 !important;
}

body.theme-light .glass-disk-halo {
  background: radial-gradient(circle, #FDE68A 0%, #F59E0B 60%, #D97706 100%) !important;
  box-shadow: 0 0 40px rgba(217, 119, 6, 0.4) !important;
}

/* ── READER PAGE ── */
body.theme-light #page-reader {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

body.theme-light .reader-body,
body.theme-light .reader-content {
  background: #FFFDF8 !important;
  color: #2D1400 !important;
}

/* ── GALLERY PAGE ── */
body.theme-light #page-gallery {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

/* ── KATHA HERO ── */
body.theme-light .katha-hero-royal {
  background: linear-gradient(180deg, #FFF3D0 0%, #FFFBF0 70%, #FFF5D6 100%) !important;
  color: #2D1400 !important;
}

/* ── PROFILE ── */
body.theme-light .profile-avatar-img {
  border: 3px solid rgba(217, 119, 6, 0.4) !important;
  box-shadow: 0 0 20px rgba(217, 119, 6, 0.25) !important;
}

/* ── TEXT OVERRIDES ── */
body.theme-light p,
body.theme-light span,
body.theme-light label,
body.theme-light div {
  color: inherit;
}

body.theme-light .text-gold,
body.theme-light .gold-text,
body.theme-light .highlight {
  color: #B45309 !important;
}

/* ── INPUTS / FORMS ── */
body.theme-light input,
body.theme-light textarea,
body.theme-light select {
  background: #FFF8E8 !important;
  color: #2D1400 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.3) !important;
}

body.theme-light input::placeholder,
body.theme-light textarea::placeholder {
  color: #78350F !important;
  opacity: 0.7;
}

/* ── MODAL OVERLAYS ── */
body.theme-light .modal-overlay,
body.theme-light .overlay-bg {
  background: rgba(255, 251, 240, 0.85) !important;
  backdrop-filter: blur(10px);
}

body.theme-light .modal-content,
body.theme-light .modal-body {
  background: #FFFFFF !important;
  color: #2D1400 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.25) !important;
  box-shadow: 0 20px 60px rgba(180, 83, 9, 0.15) !important;
}

/* ── PROGRESS / BADGES ── */
body.theme-light .progress-bar-fill {
  background: linear-gradient(90deg, #F59E0B, #D97706) !important;
}

body.theme-light .badge,
body.theme-light .tag,
body.theme-light .chip {
  background: rgba(217, 119, 6, 0.15) !important;
  color: #92400E !important;
  border: 1px solid rgba(217, 119, 6, 0.3) !important;
}

/* ── TOGGLE SWITCH ── */
body.theme-light .vedic-toggle-switch input:checked + .vedic-toggle-slider {
  background: linear-gradient(90deg, #F59E0B, #10B981) !important;
}

body.theme-light .vedic-toggle-slider {
  background: rgba(217, 119, 6, 0.25) !important;
}

/* ── SCROLLBAR ── */
body.theme-light ::-webkit-scrollbar-track {
  background: #FFF3D0 !important;
}
body.theme-light ::-webkit-scrollbar-thumb {
  background: linear-gradient(#F59E0B, #D97706) !important;
}

/* ── DIVIDERS / SEPARATORS ── */
body.theme-light hr,
body.theme-light .divider,
body.theme-light .separator {
  border-color: rgba(217, 119, 6, 0.2) !important;
  background: rgba(217, 119, 6, 0.15) !important;
}

/* ── PANCHANG ── */
body.theme-light .panchang-label,
body.theme-light .panchang-val,
body.theme-light .panchang-lbl {
  color: #3B1600 !important;
}

/* ── SECTION HEADERS ── */
body.theme-light .section-header,
body.theme-light .home-section-title,
body.theme-light .home-grid-title,
body.theme-light .section-title {
  color: #3B1600 !important;
  text-shadow: none !important;
}

/* ── NAV GRID ICONS ── */
body.theme-light .nav-grid-item,
body.theme-light .grid-icon-wrap {
  background: #FFF3D0 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  color: #3B1600 !important;
}

body.theme-light .nav-grid-label,
body.theme-light .grid-label {
  color: #3B1600 !important;
}

/* ── SADHNA HUB ── */
body.theme-light .sadhana-hub-container,
body.theme-light .sadhana-streak-bar,
body.theme-light .sadhana-info-row {
  background: #FFFFFF !important;
  color: #2D1400 !important;
  border-color: rgba(217, 119, 6, 0.2) !important;
}

/* ── SEARCH BAR ── */
body.theme-light .search-bar,
body.theme-light .search-input,
body.theme-light .search-wrap {
  background: #FFF8E8 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.25) !important;
  color: #2D1400 !important;
}

/* ── TABS ── */
body.theme-light .tab-bar,
body.theme-light .filter-tabs,
body.theme-light .tabs-row {
  background: #FFF3D0 !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.2) !important;
}

body.theme-light .tab-btn,
body.theme-light .filter-tab {
  color: #78350F !important;
  background: transparent !important;
}

body.theme-light .tab-btn.active,
body.theme-light .filter-tab.active {
  background: linear-gradient(135deg, #FDE68A, #F59E0B) !important;
  color: #1A0B2E !important;
}

/* ── LIST ITEMS ── */
body.theme-light .list-item,
body.theme-light .menu-item,
body.theme-light .drawer-item {
  color: #3B1600 !important;
  border-bottom: 1px solid rgba(217, 119, 6, 0.1) !important;
}

body.theme-light .list-item:hover,
body.theme-light .menu-item:hover,
body.theme-light .drawer-item:hover {
  background: rgba(245, 158, 11, 0.1) !important;
}

/* ── BHAJAN / UPLOAD CARDS ── */
body.theme-light .bhajan-upload-card,
body.theme-light .upload-area,
body.theme-light .bhajan-list-item {
  background: #FFFFFF !important;
  border: 1.5px solid rgba(217, 119, 6, 0.22) !important;
  color: #2D1400 !important;
}

/* ── BACK DROP / OVERLAYS ── */
body.theme-light .backdrop,
body.theme-light .dark-overlay {
  background: rgba(45, 20, 0, 0.5) !important;
}

/* ── FLOATING ELEMENTS ── */
body.theme-light .floating-btn,
body.theme-light .fab {
  background: linear-gradient(135deg, #F59E0B, #D97706) !important;
  color: #1A0B2E !important;
  box-shadow: 0 8px 24px rgba(217, 119, 6, 0.4) !important;
}

"""

# Check if comprehensive override already exists
marker = "COMPLETE LIGHT THEME OVERRIDE — ALL ELEMENTS"
if marker in css:
    # Replace existing
    start = css.find("/* ══════════════════════════════════════════════════════════════════════════════\n   ☀️ COMPLETE LIGHT THEME OVERRIDE")
    if start != -1:
        # Find the end (next major comment section or EOF)
        end_search = css.find("\n/* ══", start + 100)
        if end_search == -1:
            end_search = len(css)
        css = css[:start] + LIGHT_OVERRIDE + css[end_search:]
        print("✅ Replaced existing COMPLETE LIGHT THEME OVERRIDE block")
    else:
        css = css + LIGHT_OVERRIDE
        print("✅ Appended COMPLETE LIGHT THEME OVERRIDE (marker found, block not)")
else:
    # Append at end
    css = css + LIGHT_OVERRIDE
    print("✅ Appended new COMPLETE LIGHT THEME OVERRIDE block")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print(f"\n✅ styles.css updated — total size: {len(css)} chars")
print("\n✅ COMPLETE LIGHT MODE FIX APPLIED")
print("=" * 70)
