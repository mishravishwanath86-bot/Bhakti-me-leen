import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

m = re.search(r'id=["\']sundarkand-options-modal["\'][^>]*style=["\']([^"\']*)["\']', html)
print('1. HTML style attribute on #sundarkand-options-modal:', m.group(1) if m else 'NOT FOUND')

pos = css.find('#sundarkand-options-modal.aarti-options-modal')
snippet = css[pos:pos+500] if pos != -1 else ''
print('2. CSS has display: flex !important on #sundarkand-options-modal:', 'display: flex !important' in snippet)
print('3. CSS has explicit display: none !important rule:', '#sundarkand-options-modal[style*="display: none"]' in css)
