import json, os, glob

all_questions = {}

log_files = glob.glob(r"C:\Users\vishw\.gemini\antigravity-ide\brain\*\.system_generated\logs\transcript.jsonl")
print("Found transcript files:", len(log_files))

for lf in log_files:
    print(f"Reading {lf}...")
    with open(lf, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if '"id":' in line and '"question":' in line and '"options":' in line:
                try:
                    obj = json.loads(line)
                    content = obj.get('content', '')
                    if isinstance(content, str):
                        # look for blocks starting with [ and ending with ]
                        # or parse question objects
                        lines = content.split('\n')
                        for subline in lines:
                            pass
                except Exception:
                    pass

print("Done scanning.")
