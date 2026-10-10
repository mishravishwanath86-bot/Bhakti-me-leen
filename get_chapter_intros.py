import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for ch in [1, 2, 3, 4, 5]:
    with open(f"chapter_{ch}_hi.html", 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract the main intro text
    # In bhagavadgita.com, the chapter intro paragraph is in:
    # <p class="text-justify font-serif text-lg leading-loose text-foreground/90">(.*?)</p>
    m = re.search(r'<p class="text-justify font-serif text-lg leading-loose text-foreground/90">(.*?)</p>', html, re.DOTALL)
    if m:
        clean = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        print(f"=== Chapter {ch} Intro ===")
        print(clean)
        print()
    else:
        print(f"Chapter {ch} intro not found!")
