import sys
sys.stdout.reconfigure(encoding='utf-8')

css_content = """/* ══════════════════════════════════════════════════════════════════════════════
   ☀️ SANATAN BHAKTI — COMPREHENSIVE HIGH-CONTRAST LIGHT MODE ENGINE
   Guarantees ALL text is ALWAYS dark, crisp, and readable on light backgrounds
   ══════════════════════════════════════════════════════════════════════════════ */

/* ── 1. Root & Base Tokens for Light Mode ── */
body.theme-light,
body.light-mode,
[data-theme="light"] {
  --bg-primary: #FAF7F2 !important;
  --bg-secondary: #F4EDE2 !important;
  --card-surface: #FFFFFF !important;
  --text-main: #111827 !important;
  --text-sub: #374151 !important;
  --text-muted: #4B5563 !important;
  --gold-accent: #B45309 !important;
  --border-gold: rgba(217, 119, 6, 0.22) !important;
  --header-bg: rgba(255, 255, 255, 0.96) !important;
  --nav-bg: rgba(255, 253, 247, 0.96) !important;

  background: #FAF7F2 !important;
  color: #111827 !important;
}

body.theme-light .app-main,
body.theme-light .page,
body.light-mode .app-main,
body.light-mode .page,
[data-theme="light"] .app-main,
[data-theme="light"] .page {
  background: #FAF7F2 !important;
  color: #111827 !important;
}

/* ── 2. App Header in Light Mode ── */
body.theme-light .app-header,
body.light-mode .app-header,
[data-theme="light"] .app-header {
  background: rgba(255, 255, 255, 0.96) !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  box-shadow: 0 4px 18px rgba(180, 83, 9, 0.06) !important;
}

body.theme-light .header-title,
body.light-mode .header-title,
[data-theme="light"] .header-title {
  color: #1F1527 !important;
  text-shadow: none !important;
  font-weight: 900 !important;
}

body.theme-light .app-header button,
body.light-mode .app-header button,
[data-theme="light"] .app-header button {
  color: #1F1527 !important;
}

body.theme-light #global-theme-toggle-btn,
body.light-mode #global-theme-toggle-btn,
[data-theme="light"] #global-theme-toggle-btn {
  background: rgba(217, 119, 6, 0.12) !important;
  border: 1.5px solid #D97706 !important;
  color: #78350F !important;
  box-shadow: 0 0 10px rgba(217, 119, 6, 0.25) !important;
}

/* ── 3. Universal Typography: All Headings Must Be Dark ── */
body.theme-light h1, body.theme-light h2, body.theme-light h3,
body.theme-light h4, body.theme-light h5, body.theme-light h6,
body.light-mode h1, body.light-mode h2, body.light-mode h3,
body.light-mode h4, body.light-mode h5, body.light-mode h6,
[data-theme="light"] h1, [data-theme="light"] h2, [data-theme="light"] h3,
[data-theme="light"] h4, [data-theme="light"] h5, [data-theme="light"] h6 {
  color: #111827 !important;
  text-shadow: none !important;
}

body.theme-light .page-title,
body.theme-light .section-title,
body.theme-light .section-heading,
body.theme-light .card-title,
body.theme-light .grid-title,
body.theme-light .fest-title,
body.theme-light .vrat-title,
body.theme-light .drawer-title,
body.theme-light .modal-title,
body.theme-light .deity-name,
body.theme-light .bhajan-title,
body.theme-light .aarti-title,
body.theme-light .chapter-title,
body.light-mode .page-title,
body.light-mode .section-title,
body.light-mode .section-heading,
body.light-mode .card-title,
body.light-mode .grid-title,
body.light-mode .fest-title,
body.light-mode .vrat-title,
body.light-mode .drawer-title,
body.light-mode .modal-title,
body.light-mode .deity-name,
body.light-mode .bhajan-title,
body.light-mode .aarti-title,
body.light-mode .chapter-title,
[data-theme="light"] .page-title,
[data-theme="light"] .section-title,
[data-theme="light"] .section-heading,
[data-theme="light"] .card-title,
[data-theme="light"] .grid-title,
[data-theme="light"] .fest-title,
[data-theme="light"] .vrat-title,
[data-theme="light"] .drawer-title,
[data-theme="light"] .modal-title,
[data-theme="light"] .deity-name,
[data-theme="light"] .bhajan-title,
[data-theme="light"] .aarti-title,
[data-theme="light"] .chapter-title {
  color: #111827 !important;
  text-shadow: none !important;
  font-weight: 800 !important;
}

/* ── 4. Universal Typography: Body, Paragraphs, Articles ── */
body.theme-light p,
body.theme-light article,
body.theme-light .page-content,
body.theme-light .katha-content,
body.theme-light .katha-text,
body.theme-light .card-desc,
body.theme-light .card-subtitle,
body.theme-light .section-sub,
body.theme-light .desc,
body.theme-light .info-text,
body.theme-light .summary,
body.light-mode p,
body.light-mode article,
body.light-mode .page-content,
body.light-mode .katha-content,
body.light-mode .katha-text,
body.light-mode .card-desc,
body.light-mode .card-subtitle,
body.light-mode .section-sub,
body.light-mode .desc,
body.light-mode .info-text,
body.light-mode .summary,
[data-theme="light"] p,
[data-theme="light"] article,
[data-theme="light"] .page-content,
[data-theme="light"] .katha-content,
[data-theme="light"] .katha-text,
[data-theme="light"] .card-desc,
[data-theme="light"] .card-subtitle,
[data-theme="light"] .section-sub,
[data-theme="light"] .desc,
[data-theme="light"] .info-text,
[data-theme="light"] .summary {
  color: #374151 !important;
  text-shadow: none !important;
}

/* ── 5. Shlokas, Mantras, Choupai, Stutis, Aarti Lyrics ── */
body.theme-light .shloka-text,
body.theme-light .mantra-text,
body.theme-light .choupai-text,
body.theme-light .aarti-lyrics,
body.theme-light .lyrics-line,
body.theme-light .chalisa-doha,
body.theme-light .chalisa-choupai,
body.theme-light .gita-verse,
body.theme-light .gita-verse-sanskrit,
body.light-mode .shloka-text,
body.light-mode .mantra-text,
body.light-mode .choupai-text,
body.light-mode .aarti-lyrics,
body.light-mode .lyrics-line,
body.light-mode .chalisa-doha,
body.light-mode .chalisa-choupai,
body.light-mode .gita-verse,
body.light-mode .gita-verse-sanskrit,
[data-theme="light"] .shloka-text,
[data-theme="light"] .mantra-text,
[data-theme="light"] .choupai-text,
[data-theme="light"] .aarti-lyrics,
[data-theme="light"] .lyrics-line,
[data-theme="light"] .chalisa-doha,
[data-theme="light"] .chalisa-choupai,
[data-theme="light"] .gita-verse,
[data-theme="light"] .gita-verse-sanskrit {
  color: #1A0B2E !important;
  font-weight: 700 !important;
  text-shadow: none !important;
}

/* Arth & Translation Text */
body.theme-light .shloka-arth,
body.theme-light .choupai-meaning,
body.theme-light .gita-verse-hindi,
body.theme-light .mantra-meaning,
body.light-mode .shloka-arth,
body.light-mode .choupai-meaning,
body.light-mode .gita-verse-hindi,
body.light-mode .mantra-meaning,
[data-theme="light"] .shloka-arth,
[data-theme="light"] .choupai-meaning,
[data-theme="light"] .gita-verse-hindi,
[data-theme="light"] .mantra-meaning {
  color: #4A2000 !important;
  font-weight: 600 !important;
  text-shadow: none !important;
}

/* ── 6. Overriding Inline Light Text Colors (White, Yellow, Pale Gray) ── */
body.theme-light [style*="color:#FFF"],
body.theme-light [style*="color: #FFF"],
body.theme-light [style*="color:#fff"],
body.theme-light [style*="color: #fff"],
body.theme-light [style*="color:#FFFDF8"],
body.theme-light [style*="color: #FFFDF8"],
body.theme-light [style*="color:#FDE68A"],
body.theme-light [style*="color: #FDE68A"],
body.theme-light [style*="color:#CBD5E1"],
body.theme-light [style*="color: #CBD5E1"],
body.theme-light [style*="color:#E9D5FF"],
body.theme-light [style*="color: #E9D5FF"],
body.theme-light [style*="color:#FBCFE8"],
body.theme-light [style*="color: #FBCFE8"],
body.theme-light [style*="color:white"],
body.theme-light [style*="color: white"],
body.theme-light [style*="color: rgba(255"],
body.theme-light [style*="color:rgba(255"],
body.light-mode [style*="color:#FFF"],
body.light-mode [style*="color: #FFF"],
body.light-mode [style*="color:#fff"],
body.light-mode [style*="color: #fff"],
body.light-mode [style*="color:#FFFDF8"],
body.light-mode [style*="color: #FFFDF8"],
body.light-mode [style*="color:#FDE68A"],
body.light-mode [style*="color: #FDE68A"],
body.light-mode [style*="color:#CBD5E1"],
body.light-mode [style*="color: #CBD5E1"],
body.light-mode [style*="color:#E9D5FF"],
body.light-mode [style*="color: #E9D5FF"],
body.light-mode [style*="color:#FBCFE8"],
body.light-mode [style*="color: #FBCFE8"],
body.light-mode [style*="color:white"],
body.light-mode [style*="color: white"],
body.light-mode [style*="color: rgba(255"],
body.light-mode [style*="color:rgba(255"],
[data-theme="light"] [style*="color:#FFF"],
[data-theme="light"] [style*="color: #FFF"],
[data-theme="light"] [style*="color:#fff"],
[data-theme="light"] [style*="color: #fff"],
[data-theme="light"] [style*="color:#FFFDF8"],
[data-theme="light"] [style*="color: #FFFDF8"],
[data-theme="light"] [style*="color:#FDE68A"],
[data-theme="light"] [style*="color: #FDE68A"],
[data-theme="light"] [style*="color:#CBD5E1"],
[data-theme="light"] [style*="color: #CBD5E1"],
[data-theme="light"] [style*="color:#E9D5FF"],
[data-theme="light"] [style*="color: #E9D5FF"],
[data-theme="light"] [style*="color:#FBCFE8"],
[data-theme="light"] [style*="color: #FBCFE8"],
[data-theme="light"] [style*="color:white"],
[data-theme="light"] [style*="color: white"],
[data-theme="light"] [style*="color: rgba(255"],
[data-theme="light"] [style*="color:rgba(255"] {
  color: #111827 !important;
  text-shadow: none !important;
}

/* Secondary Subtitle / Description Inline Elements */
body.theme-light span[style*="color:#CBD5E1"],
body.theme-light div[style*="color:#CBD5E1"],
body.theme-light p[style*="color:#CBD5E1"],
body.theme-light span[style*="color:#E9D5FF"],
body.theme-light div[style*="color:#E9D5FF"],
body.theme-light span[style*="color:#FBCFE8"],
body.theme-light div[style*="color:#FBCFE8"],
body.light-mode span[style*="color:#CBD5E1"],
body.light-mode div[style*="color:#CBD5E1"],
body.light-mode p[style*="color:#CBD5E1"],
body.light-mode span[style*="color:#E9D5FF"],
body.light-mode div[style*="color:#E9D5FF"],
body.light-mode span[style*="color:#FBCFE8"],
body.light-mode div[style*="color:#FBCFE8"],
[data-theme="light"] span[style*="color:#CBD5E1"],
[data-theme="light"] div[style*="color:#CBD5E1"],
[data-theme="light"] p[style*="color:#CBD5E1"],
[data-theme="light"] span[style*="color:#E9D5FF"],
[data-theme="light"] div[style*="color:#E9D5FF"],
[data-theme="light"] span[style*="color:#FBCFE8"],
[data-theme="light"] div[style*="color:#FBCFE8"] {
  color: #4B5563 !important;
}

/* Golden / Amber Text Accents */
body.theme-light span[style*="color:#FDE68A"],
body.theme-light div[style*="color:#FDE68A"],
body.theme-light span[style*="color:#F8C83B"],
body.theme-light div[style*="color:#F8C83B"],
body.light-mode span[style*="color:#FDE68A"],
body.light-mode div[style*="color:#FDE68A"],
body.light-mode span[style*="color:#F8C83B"],
body.light-mode div[style*="color:#F8C83B"],
[data-theme="light"] span[style*="color:#FDE68A"],
[data-theme="light"] div[style*="color:#FDE68A"],
[data-theme="light"] span[style*="color:#F8C83B"],
[data-theme="light"] div[style*="color:#F8C83B"] {
  color: #B45309 !important;
}

/* ── 7. Overriding Dark Card Gradients with Clean Ivory/White Surfaces ── */
body.theme-light [style*="background: linear-gradient(135deg, #1F0738"],
body.theme-light [style*="background: linear-gradient(135deg, #1C0A35"],
body.theme-light [style*="background: linear-gradient(135deg, rgba(88"],
body.theme-light [style*="background: linear-gradient(160deg, #2D1047"],
body.theme-light [style*="background: linear-gradient(145deg, #1A103C"],
body.theme-light [style*="background: linear-gradient(145deg, #172554"],
body.theme-light [style*="background: linear-gradient(145deg, #431407"],
body.theme-light [style*="background: linear-gradient(145deg, #4C0519"],
body.light-mode [style*="background: linear-gradient(135deg, #1F0738"],
body.light-mode [style*="background: linear-gradient(135deg, #1C0A35"],
body.light-mode [style*="background: linear-gradient(135deg, rgba(88"],
body.light-mode [style*="background: linear-gradient(160deg, #2D1047"],
body.light-mode [style*="background: linear-gradient(145deg, #1A103C"],
body.light-mode [style*="background: linear-gradient(145deg, #172554"],
body.light-mode [style*="background: linear-gradient(145deg, #431407"],
body.light-mode [style*="background: linear-gradient(145deg, #4C0519"],
[data-theme="light"] [style*="background: linear-gradient(135deg, #1F0738"],
[data-theme="light"] [style*="background: linear-gradient(135deg, #1C0A35"],
[data-theme="light"] [style*="background: linear-gradient(135deg, rgba(88"],
[data-theme="light"] [style*="background: linear-gradient(160deg, #2D1047"],
[data-theme="light"] [style*="background: linear-gradient(145deg, #1A103C"],
[data-theme="light"] [style*="background: linear-gradient(145deg, #172554"],
[data-theme="light"] [style*="background: linear-gradient(145deg, #431407"],
[data-theme="light"] [style*="background: linear-gradient(145deg, #4C0519"] {
  background: #FFFFFF !important;
  border-color: rgba(217, 119, 6, 0.25) !important;
  box-shadow: 0 4px 18px rgba(180, 83, 9, 0.08) !important;
}

/* Home 3D Parikrama Card in Light Mode */
body.theme-light #parikrama-sankalp-home-card,
body.light-mode #parikrama-sankalp-home-card,
[data-theme="light"] #parikrama-sankalp-home-card {
  background: linear-gradient(145deg, #FFFFFF 0%, #FFF9F0 100%) !important;
  border: 1.5px solid #F59E0B !important;
  box-shadow: 0 8px 25px rgba(217, 119, 6, 0.12) !important;
}
body.theme-light #parikrama-sankalp-home-card *,
body.light-mode #parikrama-sankalp-home-card *,
[data-theme="light"] #parikrama-sankalp-home-card * {
  text-shadow: none !important;
}

/* Home Epic Games Banner in Light Mode */
body.theme-light .home-epic-games-banner,
body.light-mode .home-epic-games-banner,
[data-theme="light"] .home-epic-games-banner {
  background: linear-gradient(135deg, #FFFDF8 0%, #FEF3C7 100%) !important;
  border: 1.5px solid #F59E0B !important;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.15) !important;
}

/* Category Cards (.cat-card) in Light Mode */
body.theme-light .cat-card,
body.light-mode .cat-card,
[data-theme="light"] .cat-card {
  background: #FFFFFF !important;
  border: 1.5px solid rgba(217, 119, 6, 0.22) !important;
  box-shadow: 0 4px 14px rgba(180, 83, 9, 0.07) !important;
}
body.theme-light .cat-card span,
body.theme-light .cat-card .cat-name,
body.theme-light button.cat-card span,
body.light-mode .cat-card span,
body.light-mode .cat-card .cat-name,
body.light-mode button.cat-card span,
[data-theme="light"] .cat-card span,
[data-theme="light"] .cat-card .cat-name,
[data-theme="light"] button.cat-card span {
  color: #111827 !important;
  font-weight: 800 !important;
  text-shadow: none !important;
}

/* Side Drawer in Light Mode */
body.theme-light .drawer,
body.theme-light #side-drawer,
body.light-mode .drawer,
body.light-mode #side-drawer,
[data-theme="light"] .drawer,
[data-theme="light"] #side-drawer {
  background: #FFFFFF !important;
  border-right: 1.5px solid rgba(217, 119, 6, 0.22) !important;
  box-shadow: 4px 0 25px rgba(0, 0, 0, 0.1) !important;
}
body.theme-light .drawer-nav a,
body.theme-light .drawer-item,
body.light-mode .drawer-nav a,
body.light-mode .drawer-item,
[data-theme="light"] .drawer-nav a,
[data-theme="light"] .drawer-item {
  color: #111827 !important;
}
body.theme-light .drawer-item-title,
body.light-mode .drawer-item-title,
[data-theme="light"] .drawer-item-title {
  color: #111827 !important;
  font-weight: 800 !important;
}
body.theme-light .drawer-item-sub,
body.light-mode .drawer-item-sub,
[data-theme="light"] .drawer-item-sub {
  color: #4B5563 !important;
}

/* Settings Theme Card & Settings Rows in Light Mode */
body.theme-light #settings-theme-card,
body.theme-light .setting-row,
body.theme-light .setting-card,
body.light-mode #settings-theme-card,
body.light-mode .setting-row,
body.light-mode .setting-card,
[data-theme="light"] #settings-theme-card,
[data-theme="light"] .setting-row,
[data-theme="light"] .setting-card {
  background: #FFFFFF !important;
  border: 1px solid rgba(217, 119, 6, 0.22) !important;
  box-shadow: 0 2px 10px rgba(0,0,0,0.04) !important;
}

/* Panchang Tables, Vrat, Festival Cards in Light Mode */
body.theme-light .panchang-card,
body.theme-light .today-panchang-card,
body.theme-light .tpc-card,
body.theme-light .fest-card,
body.theme-light .vrat-card,
body.theme-light .grid-card,
body.light-mode .panchang-card,
body.light-mode .today-panchang-card,
body.light-mode .tpc-card,
body.light-mode .fest-card,
body.light-mode .vrat-card,
body.light-mode .grid-card,
[data-theme="light"] .panchang-card,
[data-theme="light"] .today-panchang-card,
[data-theme="light"] .tpc-card,
[data-theme="light"] .fest-card,
[data-theme="light"] .vrat-card,
[data-theme="light"] .grid-card {
  background: #FFFFFF !important;
  border: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  box-shadow: 0 4px 16px rgba(180, 83, 9, 0.06) !important;
}
body.theme-light .tpc-row,
body.theme-light .panchang-row,
body.light-mode .tpc-row,
body.light-mode .panchang-row,
[data-theme="light"] .tpc-row,
[data-theme="light"] .panchang-row {
  color: #111827 !important;
}
body.theme-light .tpc-label,
body.theme-light .panchang-lbl-text,
body.light-mode .tpc-label,
body.light-mode .panchang-lbl-text,
[data-theme="light"] .tpc-label,
[data-theme="light"] .panchang-lbl-text {
  color: #78350F !important;
  font-weight: 700 !important;
}
body.theme-light .tpc-value,
body.theme-light .panchang-val-text,
body.light-mode .tpc-value,
body.light-mode .panchang-val-text,
[data-theme="light"] .tpc-value,
[data-theme="light"] .panchang-val-text {
  color: #111827 !important;
  font-weight: 800 !important;
}

/* Gita & Chapter List in Light Mode */
body.theme-light .gita-chapter-card,
body.theme-light .gita-card,
body.light-mode .gita-chapter-card,
body.light-mode .gita-card,
[data-theme="light"] .gita-chapter-card,
[data-theme="light"] .gita-card {
  background: #FFFFFF !important;
  border: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  box-shadow: 0 4px 16px rgba(180, 83, 9, 0.06) !important;
}
body.theme-light .gita-chapter-title,
body.light-mode .gita-chapter-title,
[data-theme="light"] .gita-chapter-title {
  color: #111827 !important;
  font-weight: 800 !important;
}
body.theme-light .gita-chapter-desc,
body.light-mode .gita-chapter-desc,
[data-theme="light"] .gita-chapter-desc {
  color: #4B5563 !important;
}

/* Audio Player in Light Mode */
body.theme-light #audio-player-bar,
body.theme-light .audio-bar,
body.theme-light .mini-player,
body.light-mode #audio-player-bar,
body.light-mode .audio-bar,
body.light-mode .mini-player,
[data-theme="light"] #audio-player-bar,
[data-theme="light"] .audio-bar,
[data-theme="light"] .mini-player {
  background: #FFFFFF !important;
  border-top: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.08) !important;
}
body.theme-light .track-title,
body.theme-light .audio-title,
body.light-mode .track-title,
body.light-mode .audio-title,
[data-theme="light"] .track-title,
[data-theme="light"] .audio-title {
  color: #111827 !important;
  font-weight: 800 !important;
}
body.theme-light .track-artist,
body.theme-light .audio-artist,
body.light-mode .track-artist,
body.light-mode .audio-artist,
[data-theme="light"] .track-artist,
[data-theme="light"] .audio-artist {
  color: #4B5563 !important;
}

/* ── 8. Preserving Badges & Filled Buttons ── */
/* Solid Golden Action Buttons keep dark text */
body.theme-light button[style*="linear-gradient(135deg, #F8C83B"],
body.theme-light button[style*="linear-gradient(135deg, #F59E0B"],
body.light-mode button[style*="linear-gradient(135deg, #F8C83B"],
body.light-mode button[style*="linear-gradient(135deg, #F59E0B"],
[data-theme="light"] button[style*="linear-gradient(135deg, #F8C83B"],
[data-theme="light"] button[style*="linear-gradient(135deg, #F59E0B"] {
  color: #1A0B2E !important;
}

/* Saturated Alert Badges (Red/Orange/Green) keep white text */
body.theme-light span[style*="background:#FF6B00"],
body.theme-light span[style*="background: #FF6B00"],
body.theme-light span[style*="background:#EF4444"],
body.theme-light span[style*="background: #EF4444"],
body.theme-light span[style*="background:#DC2626"],
body.theme-light span[style*="background: #DC2626"],
body.light-mode span[style*="background:#FF6B00"],
body.light-mode span[style*="background: #FF6B00"],
body.light-mode span[style*="background:#EF4444"],
body.light-mode span[style*="background: #EF4444"],
body.light-mode span[style*="background:#DC2626"],
body.light-mode span[style*="background: #DC2626"],
[data-theme="light"] span[style*="background:#FF6B00"],
[data-theme="light"] span[style*="background: #FF6B00"],
[data-theme="light"] span[style*="background:#EF4444"],
[data-theme="light"] span[style*="background: #EF4444"],
[data-theme="light"] span[style*="background:#DC2626"],
[data-theme="light"] span[style*="background: #DC2626"] {
  color: #FFFFFF !important;
}
"""

with open('light_theme.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Created light_theme.css successfully! Length:", len(css_content))
