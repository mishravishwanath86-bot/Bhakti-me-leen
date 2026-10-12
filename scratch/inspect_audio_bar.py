import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('ai-bhakti-audio-bar')
print('=== ai-bhakti-audio-bar context ===')
print(text[idx-200:idx+1500])
