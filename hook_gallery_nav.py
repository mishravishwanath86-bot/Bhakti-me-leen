import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

app_js = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js")
with open(app_js, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Add gallery auto-render inside showPage if not already present
hook = """
  if (pageId === 'page-gallery' && typeof renderDivineGallery === 'function') {
    setTimeout(renderDivineGallery, 20);
  }
"""

if "pageId === 'page-gallery'" not in js:
    # Append to showPage or at end
    js += f"\n// Auto hook for gallery navigation\nconst originalShowPage = window.showPage;\nwindow.showPage = function(pageId) {{\n  if (originalShowPage) originalShowPage(pageId);\n  if (pageId === 'page-gallery' && typeof renderDivineGallery === 'function') {{\n    setTimeout(renderDivineGallery, 20);\n  }}\n}};\n"
    with open(app_js, 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Added showPage hook for page-gallery")
else:
    print("Hook already present")
