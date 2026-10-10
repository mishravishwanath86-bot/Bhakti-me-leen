import json, os, glob, re

brain_dir = r"C:\Users\vishw\.gemini\antigravity-ide\brain"
all_mcqs = {}

# 1. Search all .json, .py, .txt, .jsonl in brain_dir
for root, dirs, files in os.walk(brain_dir):
    for fname in files:
        if fname.endswith(('.json', '.py', '.txt', '.jsonl', '.db', '.dart')):
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Look for { "id": 123, "question": ... }
                # Find all occurrences of "id": <number>
                for m in re.finditer(r'\{\s*"id":\s*(\d+)\s*,\s*"question":\s*"([^"]+)"\s*,\s*"options":\s*(\[[^\]]+\])\s*,\s*"correct_answer":\s*(\d+)', content):
                    qid = int(m.group(1))
                    qtext = m.group(2)
                    opts = json.loads(m.group(3))
                    ans = int(m.group(4))
                    if qid not in all_mcqs:
                        all_mcqs[qid] = {
                            "id": qid,
                            "question": qtext,
                            "options": opts,
                            "correct_answer": ans
                        }
            except Exception:
                pass

print(f"Total MCQs recovered from conversation history & scratch: {len(all_mcqs)}")
if all_mcqs:
    s_ids = sorted(all_mcqs.keys())
    print(f"Min ID: {min(s_ids)}, Max ID: {max(s_ids)}")
    print(f"Missing IDs count between {min(s_ids)} and {max(s_ids)}: {max(s_ids) - min(s_ids) + 1 - len(all_mcqs)}")
