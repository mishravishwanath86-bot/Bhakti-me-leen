import os, glob

dirs = [
  (r'C:\Users\vishw\OneDrive\Videos\रामायण आरंभ', 40, 'Ramayana'),
  (r'C:\Users\vishw\OneDrive\Videos\लंका युद्ध', 35, 'Lanka'),
  (r'C:\Users\vishw\OneDrive\Videos\महाभारत', 25, 'Mahabharat')
]

for d, count, label in dirs:
    files = glob.glob(os.path.join(d, '*.png'))
    files.sort(key=lambda f: os.path.getctime(f))
    print(f'=== {label} ({len(files)} files, expected {count}) ===')
    for i, f in enumerate(files):
        print(f'{i+1}: {os.path.basename(f)}')
