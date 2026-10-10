import subprocess, glob, os

files = glob.glob("test_script_*.js")
errors = 0
for f in files:
    res = subprocess.run(["node", "--check", f], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error in {f}: {res.stderr}")
        errors += 1
    os.remove(f)

if errors == 0:
    print(f"All {len(files)} inline scripts passed node --check with 0 errors!")
