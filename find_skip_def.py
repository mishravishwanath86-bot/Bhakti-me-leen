with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('window.skipIntroVideo =')
if idx != -1:
    print(c[idx:idx+600])
