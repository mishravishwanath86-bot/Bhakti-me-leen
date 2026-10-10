with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\n},\n      {\n        "id": "drik_gods_14"', '\n      },\n      {\n        "id": "drik_gods_14"')
text = text.replace('\n},\n      {\n        "id": "drik_gods_12"', '\n      },\n      {\n        "id": "drik_gods_12"')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed indentation.')
