import json, re, glob, os

all_mcqs = {}

# Load existing
if os.path.exists('all_sanatan_mcqs.json'):
    with open('all_sanatan_mcqs.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)
        for q in existing:
            all_mcqs[q['id']] = q

print("Starting with existing:", len(all_mcqs))

# Scan all transcript files
transcript_files = glob.glob(r"C:\Users\vishw\.gemini\antigravity-ide\brain\*\.system_generated\logs\transcript.jsonl")

pattern = re.compile(r'\{\s*"id"\s*:\s*(\d+)[\s\S]*?"question"\s*:\s*"([^"]+)"[\s\S]*?"options"\s*:\s*(\[[^\]]+\])[\s\S]*?"correct_answer"\s*:\s*(\d+)[\s\S]*?\}')

for tf in transcript_files:
    print(f"Scanning {tf}...")
    try:
        with open(tf, 'r', encoding='utf-8', errors='ignore') as f:
            for line_no, line in enumerate(f):
                if '"id":' in line and '"question":' in line:
                    for m in pattern.finditer(line):
                        try:
                            qid = int(m.group(1))
                            qtext = m.group(2)
                            opts = json.loads(m.group(3))
                            ans = int(m.group(4))
                            
                            exp_match = re.search(r'"explanation"\s*:\s*"([^"]+)"', m.group(0))
                            exp = exp_match.group(1) if exp_match else ''

                            cat_match = re.search(r'"category"\s*:\s*"([^"]+)"', m.group(0))
                            cat = cat_match.group(1) if cat_match else 'All'

                            if qid not in all_mcqs:
                                all_mcqs[qid] = {
                                    "id": qid,
                                    "question": qtext,
                                    "options": opts,
                                    "correct_answer": ans,
                                    "explanation": exp,
                                    "category": cat
                                }
                        except Exception:
                            pass
    except Exception as e:
        print(f"Error scanning {tf}: {e}")

print(f"\nTotal extracted MCQs after transcript scan: {len(all_mcqs)}")
if all_mcqs:
    s_ids = sorted(all_mcqs.keys())
    print(f"Min ID: {min(s_ids)}, Max ID: {max(s_ids)}")

with open('all_sanatan_mcqs.json', 'w', encoding='utf-8') as f:
    json.dump(list(all_mcqs.values()), f, ensure_ascii=False, indent=2)

print(f"Saved {len(all_mcqs)} questions to all_sanatan_mcqs.json")
