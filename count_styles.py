import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

style_tags = list(re.finditer(r'<style[^>]*>', html))
print(f"Total <style> tags in index.html: {len(style_tags)}")
for i, tag in enumerate(style_tags):
    start = tag.start()
    end = html.find('</style>', start)
    print(f"Style tag {i}: length {end - start}")
