import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app'
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(('.css', '.html')):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            count = len(re.findall(r'(\.theme-light|\.light-mode|data-theme=["\']light["\'])', content))
            if count > 0:
                print(f'{file}: {count} occurrences of light theme selectors')
