import os, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(os.listdir('assets/gallery')):
    print(f)
