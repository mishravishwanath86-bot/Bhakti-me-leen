import re, glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

js_files = glob.glob('*.js')
print(f'Checking {len(js_files)} JS files...')

for f in js_files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        
        load_calls = [m.start() for m in re.finditer(r'loadContent', content)]
        current_content_refs = [m.start() for m in re.finditer(r'currentContent', content)]
        open_reader_refs = [m.start() for m in re.finditer(r'openReader', content)]
        
        if load_calls or current_content_refs or open_reader_refs:
            print(f'=== {f} ===')
            if load_calls:
                print(f'  loadContent ({len(load_calls)}):')
                for m in load_calls[:5]:
                    snippet = content[max(0, m-50):min(len(content), m+120)].replace('\n', ' ')
                    print(f'    @{m}: {snippet}')
            if current_content_refs:
                print(f'  currentContent ({len(current_content_refs)}):')
                for m in current_content_refs[:5]:
                    snippet = content[max(0, m-50):min(len(content), m+120)].replace('\n', ' ')
                    print(f'    @{m}: {snippet}')
            if open_reader_refs:
                print(f'  openReader ({len(open_reader_refs)}):')
                for m in open_reader_refs[:5]:
                    snippet = content[max(0, m-50):min(len(content), m+120)].replace('\n', ' ')
                    print(f'    @{m}: {snippet}')
    except Exception as e:
        print(f'Error reading {f}: {e}')
