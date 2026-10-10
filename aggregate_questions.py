import json, re, glob, os

all_questions = {}

# 1. Check all python and txt files in scratch
for fpath in glob.glob('*'):
    if not os.path.isfile(fpath):
        continue
    try:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Try to find JSON arrays
        for match in re.finditer(r'\[\s*\{\s*"id":\s*(\d+)[\s\S]*?\}\s*\]', content):
            snippet = match.group(0)
            try:
                data = json.loads(snippet)
                for q in data:
                    if isinstance(q, dict) and 'id' in q:
                        all_questions[q['id']] = q
            except Exception:
                pass
        
        # Try finding individual question objects
        for match in re.finditer(r'\{\s*"id":\s*(\d+),\s*"question":[\s\S]*?"answer":[\s\S]*?\}', content):
            snippet = match.group(0)
            try:
                q = json.loads(snippet)
                all_questions[q['id']] = q
            except Exception:
                pass
    except Exception as e:
        pass

print(f"Total unique questions found in scratch files: {len(all_questions)}")
sorted_ids = sorted(all_questions.keys())
if sorted_ids:
    print(f"ID range: {min(sorted_ids)} to {max(sorted_ids)}")
