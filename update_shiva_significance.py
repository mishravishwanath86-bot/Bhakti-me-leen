# -*- coding: utf-8 -*-
import json

with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    collections = json.load(f)

for it in collections['shiva']['items']:
    if it.get('id') == 'drik_shiva_2':
        it['significance'] = """॥ हर हर हर महादेव — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. परम पूज्य भाईजी श्री हनुमान प्रसाद जी पोद्दार कृत:
यह दिव्य स्तुति-आरती गीताप्रेस गोरखपुर के आदि-संपादक श्रद्धेय भाईजी श्री हनुमान प्रसाद जी पोद्दार द्वारा रचित है, जो कल्याण पत्रिका व शिवोपासना में अत्यंत समादृत है।

२. रुद्र एवं सौम्य स्वरूपों का अद्वैत समन्वय:
यह आरती साधक को यह बोध कराती है कि संहारक रुद्र और कल्याणकारी आशुतोष शिव एक ही परमात्मा के दो पहलू हैं।

३. समस्त पापों एवं भय का समूल नाश:
"अमल, अरूप, अगोचर, अविचल, अघहारी"—इस आरती का नित्य श्रवण-कीर्तन करने से जन्म-जन्मांतरों के पाप, काल-भय और रोग-शोक नष्ट होते हैं।

४. निर्मल मति एवं शरणागति:
"सब विधि निर्मल मति कर, अपना कर लीजै"—साधक का चित्त परम निर्मल होकर काम-क्रोधादि विकारों से मुक्त होता है और शिव-कृपा प्राप्त होती है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह पाठ द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक ग्यारह पदों एवं टेक पर पूर्णतः आधारित है।"""
        break

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(collections, f, ensure_ascii=False, indent=2)

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Update significance of drik_shiva_2 in app.js
obj_start = app_js.find('"id": "drik_shiva_2"')
brace_start = app_js.rfind('{', 0, obj_start)
next_obj = app_js.find('"id": "drik_shiva_3"', obj_start)
brace_end = app_js.rfind('}', brace_start, next_obj) + 1

item_data = [x for x in collections['shiva']['items'] if x.get('id') == 'drik_shiva_2'][0]
new_block = json.dumps(item_data, ensure_ascii=False, indent=8)
app_js = app_js[:brace_start] + new_block + app_js[brace_end:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("[OK] Updated drik_shiva_2 with Poddar Ji in significance in both files!")
