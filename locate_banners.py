import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['BHAKTI AMRIT KALASH', 'today-panchang-card', 'दैनिक साधना संज्ञान', 'divine-gift-bar', 'page-vrats-all', 'हिन्दू व्रत एवं उपवास']):
        print(f"L{i+1}: {line.strip()[:100]}")
