import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for engine_file in ['gita_engine.js', 'sundarkand_engine.js', 'mantra_engine.js', 'ai_bhakti_player.js']:
    print(f'================= {engine_file} =================')
    with open(engine_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f'Total length: {len(content)} chars')
    
    # Check fetch / API calls
    fetch_calls = re.findall(r'fetch\([\'\"`]([^\'\"`]+)[\'\"`]', content)
    print(f'Fetch calls ({len(fetch_calls)}):', set(fetch_calls))
    
    # Check AiBhaktiPlayer usage
    ai_calls = re.findall(r'AiBhaktiPlayer\.[a-zA-Z0-9_]+', content)
    print(f'AiBhaktiPlayer calls ({len(ai_calls)}):', set(ai_calls))
    
    # Check function names defined
    funcs = re.findall(r'(?:window\.|function\s+)([a-zA-Z0-9_]+)\s*=?\s*function', content)
    print(f'Functions defined ({len(funcs)}):', funcs[:15])
    print()
