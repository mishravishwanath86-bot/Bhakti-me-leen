
    (function() {
      const VIEW_W = 1000;
      const VIEW_H = 160;
      const MARGIN_X = 75;
      const USABLE_W = VIEW_W - 2 * MARGIN_X; // 850
      const TOTAL_TABS = 5;
      const TAB_W = USABLE_W / TOTAL_TABS; // 170
      const CORNER_R = 36;

      // Deep, prominent, wide scoop curve (73.8% depth!)
      const SCOOP_W = 88;
      const DEPTH = 118;
      const SHOULDER_W = 35;

      const PAGE_MAP = {
        'page-home': 0,
        'page-katha': 1,
        'page-mala': 2,
        'page-aarti-stage': 3,
        'page-panchang': 4
      };

      const ICONS = [
        '<svg viewBox="0 0 24 24"><path d="M3 10.5L12 3l9 7.5v9.5a1 1 0 01-1 1h-5v-6h-6v6H4a1 1 0 01-1-1v-9.5z"/></svg>',
        '<svg viewBox="0 0 24 24"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 00-2-2H3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg>',
        '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="7.5" stroke-dasharray="2 3"/><circle cx="12" cy="4" r="1.8" fill="currentColor"/><circle cx="12" cy="20" r="1.8" fill="currentColor"/><circle cx="4" cy="12" r="1.8" fill="currentColor"/><circle cx="20" cy="12" r="1.8" fill="currentColor"/><circle cx="6.5" cy="6.5" r="1.8" fill="currentColor"/><circle cx="17.5" cy="6.5" r="1.8" fill="currentColor"/><circle cx="6.5" cy="17.5" r="1.8" fill="currentColor"/><circle cx="17.5" cy="17.5" r="1.8" fill="currentColor"/></svg>',
        '<svg viewBox="0 0 24 24"><path d="M12 2c0 3.5-3.5 5.5-3.5 9a3.5 3.5 0 007 0c0-3.5-3.5-5.5-3.5-9z"/><path d="M4 17c0 3 4 5 8 5s8-2 8-5H4z"/></svg>',
        '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><circle cx="12" cy="15" r="2"/></svg>'
      ];

      function calcCurvedPath(cx) {
        const left_x = cx - SCOOP_W;
        const right_x = cx + SCOOP_W;
        const cp1_x = left_x + SHOULDER_W;
        const cp2_x = cx - 36;
        const cp3_x = cx + 36;
        const cp4_x = right_x - SHOULDER_W;

        return 'M 0,' + CORNER_R + ' ' +
               'A ' + CORNER_R + ',' + CORNER_R + ' 0 0 1 ' + CORNER_R + ',0 ' +
               'L ' + left_x.toFixed(1) + ',0 ' +
               'C ' + cp1_x.toFixed(1) + ',0 ' + cp2_x.toFixed(1) + ',' + DEPTH + ' ' + cx.toFixed(1) + ',' + DEPTH + ' ' +
               'C ' + cp3_x.toFixed(1) + ',' + DEPTH + ' ' + cp4_x.toFixed(1) + ',0 ' + right_x.toFixed(1) + ',0 ' +
               'L ' + (VIEW_W - CORNER_R) + ',0 ' +
               'A ' + CORNER_R + ',' + CORNER_R + ' 0 0 1 ' + VIEW_W + ',' + CORNER_R + ' ' +
               'L ' + VIEW_W + ',' + (VIEW_H - CORNER_R) + ' ' +
               'A ' + CORNER_R + ',' + CORNER_R + ' 0 0 1 ' + (VIEW_W - CORNER_R) + ',' + VIEW_H + ' ' +
               'L ' + CORNER_R + ',' + VIEW_H + ' ' +
               'A ' + CORNER_R + ',' + CORNER_R + ' 0 0 1 0,' + (VIEW_H - CORNER_R) + ' ' +
               'Z';
      }

      let activeIndex = 0;
      let currentAnimatedCx = MARGIN_X + 0.5 * TAB_W; // 160.0
      let targetAnimatedCx = MARGIN_X + 0.5 * TAB_W;
      let animId = null;

      function renderNotch(targetIdx) {
        const pathEl = document.getElementById('curved-nav-dynamic-path');
        const bubbleEl = document.getElementById('curved-nav-bubble');
        const iconWrap = document.getElementById('bubble-icon-wrap');
        if (!pathEl || !bubbleEl) return;

        targetAnimatedCx = MARGIN_X + (targetIdx + 0.5) * TAB_W;
        const percent = (targetAnimatedCx / VIEW_W) * 100;
        bubbleEl.style.left = percent.toFixed(2) + '%';
        if (iconWrap && ICONS[targetIdx]) {
          iconWrap.innerHTML = ICONS[targetIdx];
        }

        if (animId) cancelAnimationFrame(animId);

        function step() {
          currentAnimatedCx += (targetAnimatedCx - currentAnimatedCx) * 0.25;
          if (Math.abs(targetAnimatedCx - currentAnimatedCx) < 0.35) {
            currentAnimatedCx = targetAnimatedCx;
            pathEl.setAttribute('d', calcCurvedPath(currentAnimatedCx));
            return;
          }
          pathEl.setAttribute('d', calcCurvedPath(currentAnimatedCx));
          animId = requestAnimationFrame(step);
        }
        animId = requestAnimationFrame(step);
      }

      window.switchCurvedNavTab = function(idx, pageId) {
        idx = parseInt(idx, 10);
        if (isNaN(idx) || idx < 0 || idx >= TOTAL_TABS) return;
        activeIndex = idx;

        // Update active classes
        document.querySelectorAll('.curved-tab-btn').forEach((btn, i) => {
          btn.classList.toggle('active', i === idx);
        });

        renderNotch(idx);

        if (pageId && typeof window.showPage === 'function') {
          window.showPage(pageId);
        }
      };

      window.updateCurvedBottomNav = function(pageId) {
        if (!pageId) return;
        if (PAGE_MAP.hasOwnProperty(pageId)) {
          const idx = PAGE_MAP[pageId];
          if (idx !== activeIndex) {
            activeIndex = idx;
            document.querySelectorAll('.curved-tab-btn').forEach((btn, i) => {
              btn.classList.toggle('active', i === idx);
            });
            renderNotch(idx);
          }
        }
      };

      // Hook into showPage
      function hookShowPage() {
        if (typeof window.showPage === 'function') {
          const orig = window.showPage;
          window.showPage = function(pageId) {
            orig.apply(this, arguments);
            window.updateCurvedBottomNav(pageId);
          };
        } else {
          setTimeout(hookShowPage, 100);
        }
      }

      // Initialize
      if (document.readyState === 'complete' || document.readyState === 'interactive') {
        renderNotch(0);
        hookShowPage();
      } else {
        document.addEventListener('DOMContentLoaded', function() {
          renderNotch(0);
          hookShowPage();
        });
      }
    })();
  