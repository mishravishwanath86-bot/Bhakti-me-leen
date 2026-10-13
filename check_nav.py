with open('test_glass_curve.html', 'r', encoding='utf-8') as f:
    tg = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

import re
m1 = re.search(r'<style>(.*?)</style>', tg, re.DOTALL)
m2 = re.search(r'<style id="curved-fluid-bottom-nav-styles">(.*?)</style>', idx, re.DOTALL)
print('test_glass_curve style len:', len(m1.group(1)) if m1 else 0)
print('index.html style len:', len(m2.group(1)) if m2 else 0)

# Check SVG in test_glass_curve
svg1 = re.search(r'<svg class="dock-svg".*?</svg>', tg, re.DOTALL)
print('test_glass_curve svg found:', bool(svg1))
if svg1:
    print(svg1.group(0)[:300])

# Check items in test_glass_curve
items1 = re.search(r'<div class="dock-items".*?</div>\s*</div>', tg, re.DOTALL)
if items1:
    print('Items in test_glass_curve:\n', items1.group(0))
