import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

svg_strokes = re.findall(r'<svg[^>]*>.*?</svg>', html, re.DOTALL)
print(f"Total SVGs in index.html: {len(svg_strokes)}")
light_svg = 0
for s in svg_strokes:
    if '#FFF' in s or '#fff' in s or '#FDE68A' in s or 'white' in s:
        light_svg += 1
print(f"SVGs with light strokes/fills: {light_svg}")
