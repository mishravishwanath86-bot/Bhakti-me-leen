with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = 27348
print(c[idx-1200:idx].encode('ascii', errors='replace').decode('ascii'))
