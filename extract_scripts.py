import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} inline scripts.")

for i, s in enumerate(scripts):
    fname = f"test_script_{i}.js"
    with open(fname, 'w', encoding='utf-8') as out:
        out.write(s)

print("Saved inline scripts for syntax check.")
