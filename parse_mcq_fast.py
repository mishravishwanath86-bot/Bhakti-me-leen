import json, os, glob

files = ['raw_mcqs_1401.txt', 'raw_mcqs_1601.txt', 'raw_mcqs_1801.txt', 'raw_mcqs_1901.txt', 'shuffle_mcqs.py', 'shuffle_mcqs_1301.py', 'shuffle_1401_1600.py', 'shuffle_1601_1700.py', 'shuffle_1801_1900.py', 'shuffle_1901_2000.py']

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            text = fp.read()
            # find JSON array
            s_idx = text.find('[')
            e_idx = text.rfind(']')
            if s_idx != -1 and e_idx != -1 and e_idx > s_idx:
                try:
                    data = json.loads(text[s_idx:e_idx+1])
                    if isinstance(data, list):
                        ids = [q.get('id') for q in data if isinstance(q, dict) and 'id' in q]
                        print(f"File {f}: parsed JSON with {len(data)} items, IDs: {min(ids) if ids else None} to {max(ids) if ids else None}")
                except Exception as e:
                    print(f"File {f}: JSON parse error: {e}")
            else:
                print(f"File {f}: No [ ] brackets found")
