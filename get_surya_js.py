with open("app.js", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'  chalisa_surya:\s*\{[\s\S]*?\n  \},?\n', text)
if m:
    print("Found chalisa_surya block, length:", len(m.group(0)))
    with open("chalisa_surya_current_js.txt", "w", encoding="utf-8") as out:
        out.write(m.group(0))
else:
    print("Not found with regex")
