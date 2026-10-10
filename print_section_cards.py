import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_section_cards(start_line, end_line, name):
    print(f"=== {name} ===")
    card_indices = []
    for i in range(start_line - 1, end_line):
        line = lines[i]
        if 'class="aarti-preview-card' in line:
            card_indices.append(i + 1)
    print(f"Found {len(card_indices)} cards:")
    for idx in card_indices:
        print(f"  Line {idx}: {lines[idx-1].strip()[:90]}")
    print()

print_section_cards(1685, 1840, "CHALISA")
print_section_cards(1840, 2030, "MANTRA")
print_section_cards(2030, 2125, "SUNDARKAND")
print_section_cards(2125, 2260, "GITA")
