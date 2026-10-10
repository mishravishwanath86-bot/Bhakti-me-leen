import os

print("Files in assets/gallery:")
for f in os.listdir(r'assets\gallery'):
    print(" ", f)

print("\nFiles in assets:")
for f in os.listdir(r'assets'):
    if os.path.isfile(os.path.join(r'assets', f)):
        print(" ", f)
