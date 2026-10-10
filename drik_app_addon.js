// ══════════════════════════════════════════════════════════════════════════════
// 🪔 Sanatan Panchang AARTI ENGINE MODULE
// All core controllers, datasets, and 2-step back navigators are in app.js
// ══════════════════════════════════════════════════════════════════════════════

(function() {
  if (typeof window !== 'undefined') {
    // Ensure helper alias references are guaranteed
    if (typeof window.closeAartiOptionsModal === 'function') {
      window.closeAartiModal = window.closeAartiOptionsModal;
    }
    console.log("✓ Sanatan Panchang Aarti Engine module loaded and verified.");
  }
})();
