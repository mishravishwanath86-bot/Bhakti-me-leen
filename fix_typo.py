with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

if 'iframe.contentWiwindow.postMessage' in js:
    js = js.replace('iframe.contentWiwindow.postMessage', 'iframe.contentWindow.postMessage')
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Fixed contentWiwindow typo in app.js")
else:
    print("Typo not found or already fixed")
