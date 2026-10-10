import json, re, glob, os

all_mcqs = {}

def clean_and_extract_json(text):
    questions = []
    # Find all { "id": ... } objects
    pattern = re.compile(r'\{\s*"id"\s*:\s*(\d+)[\s\S]*?"question"\s*:\s*"([^"]+)"[\s\S]*?"options"\s*:\s*(\[[^\]]+\])[\s\S]*?"correct_answer"\s*:\s*(\d+)[\s\S]*?\}')
    for m in pattern.finditer(text):
        try:
            qid = int(m.group(1))
            qtext = m.group(2)
            opts = json.loads(m.group(3))
            ans = int(m.group(4))
            
            # extract explanation if present
            exp_match = re.search(r'"explanation"\s*:\s*"([^"]+)"', m.group(0))
            exp = exp_match.group(1) if exp_match else ''

            # extract category if present
            cat_match = re.search(r'"category"\s*:\s*"([^"]+)"', m.group(0))
            cat = cat_match.group(1) if cat_match else 'All'

            questions.append({
                "id": qid,
                "question": qtext,
                "options": opts,
                "correct_answer": ans,
                "explanation": exp,
                "category": cat
            })
        except Exception as e:
            pass
    return questions

# Process files in scratch
files = glob.glob('raw_mcqs_*.txt') + glob.glob('shuffle_*.py')
for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    qs = clean_and_extract_json(content)
    for q in qs:
        all_mcqs[q['id']] = q
    print(f"File {fpath}: extracted {len(qs)} MCQs")

print(f"\nTotal extracted MCQs: {len(all_mcqs)}")
if all_mcqs:
    s_ids = sorted(all_mcqs.keys())
    print(f"Min ID: {min(s_ids)}, Max ID: {max(s_ids)}")

# Save to all_sanatan_mcqs.json
with open('all_sanatan_mcqs.json', 'w', encoding='utf-8') as f:
    json.dump(list(all_mcqs.values()), f, ensure_ascii=False, indent=2)

print(f"Saved {len(all_mcqs)} questions to all_sanatan_mcqs.json")
