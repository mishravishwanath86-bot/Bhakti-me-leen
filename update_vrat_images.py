import os

path = r'c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # amavasya heroImg
    ('"amavasya": {\n    "title": "अमावस्या 2026",\n    "heroImg": "assets/deity_ganga.jpg"', '"amavasya": {\n    "title": "अमावस्या 2026",\n    "heroImg": "assets/amavasya_moon.jpg"'),
    # skanda-sashti heroImg
    ('"skanda-sashti": {\n    "title": "स्कंद षष्ठी 2026",\n    "heroImg": "assets/deity_narsingh.jpg"', '"skanda-sashti": {\n    "title": "स्कंद षष्ठी 2026",\n    "heroImg": "assets/lord_murugan.jpg"'),
    # karthigai heroImg
    ('"karthigai": {\n    "title": "मासिक कार्तिगाई 2026",\n    "heroImg": "assets/deity_shiv.jpg"', '"karthigai": {\n    "title": "मासिक कार्तिगाई 2026",\n    "heroImg": "assets/karthigai_deepam.jpg"'),
    # shraddha heroImg
    ('"shraddha": {\n    "title": "श्राद्ध तिथियाँ 2026",\n    "heroImg": "assets/deity_ramayana.jpg"', '"shraddha": {\n    "title": "श्राद्ध तिथियाँ 2026",\n    "heroImg": "assets/pitru_paksha.jpg"'),
    # kalashtami heroImg
    ('"kalashtami": {\n    "title": "कालाष्टमी 2026",\n    "heroImg": "assets/deity_shiv.jpg"', '"kalashtami": {\n    "title": "कालाष्टमी 2026",\n    "heroImg": "assets/deity_bhairav.jpg"'),
    # rohini-vrat heroImg
    ('"rohini-vrat": {\n    "title": "रोहिणी व्रत 2026",\n    "heroImg": "assets/deity_krishna.jpg"', '"rohini-vrat": {\n    "title": "रोहिणी व्रत 2026",\n    "heroImg": "assets/lord_mahavira.jpg"'),
    # chandra-darshan heroImg
    ('"chandra-darshan": {\n    "title": "चंद्र दर्शन 2026",\n    "heroImg": "assets/deity_shiv.jpg"', '"chandra-darshan": {\n    "title": "चंद्र दर्शन 2026",\n    "heroImg": "assets/purnima_vrat.jpg"'),
    # kalashtami in HINDU_VRATS
    ("{ name: 'कालाष्टमी', img: 'assets/deity_shiv.jpg', page: 'kalashtami', isDynamic: true }", "{ name: 'कालाष्टमी', img: 'assets/deity_bhairav.jpg', page: 'kalashtami', isDynamic: true }"),
]

applied = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        applied += 1
        print(f"Applied replacement {applied}")
    else:
        print("Not found item")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Total replacements applied: {applied}")
