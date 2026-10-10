with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'<script id="curved-fluid-bottom-nav-engine">(.*?)</script>', html, re.DOTALL)
if m:
    with open('test_curved_script.js', 'w', encoding='utf-8') as f_out:
        f_out.write(m.group(1))
    print("Script extracted to test_curved_script.js")
else:
    print("Script NOT found!")
