import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Map: old src -> new src (only for the specific deity cards in coverflow + aarti)
replacements = [
    # Coverflow Durga card
    ('assets/deity_durga.jpg" alt="माँ दुर्गा"', 'assets/gallery/bal_durga_little.jpg" alt="माँ दुर्गा"'),
    ('src="assets/deity_durga.jpg" alt=""', 'src="assets/gallery/bal_durga_little.jpg" alt=""'),
    # Coverflow Lakshmi card
    ('assets/deity_lakshmi.jpg" alt="लक्ष्मी जी"', 'assets/gallery/bal_lakshmi_little.jpg" alt="लक्ष्मी जी"'),
    ('src="assets/deity_lakshmi.jpg" alt=""', 'src="assets/gallery/bal_lakshmi_little.jpg" alt=""'),
    # Coverflow Ganesh card
    ('assets/deity_ganesh.jpg" alt="गणेश जी"', 'assets/gallery/bal_ganesha_little.jpg" alt="गणेश जी"'),
    ('src="assets/deity_ganesh.jpg" alt=""', 'src="assets/gallery/bal_ganesha_little.jpg" alt=""'),
    # Coverflow Saraswati card
    ('assets/deity_saraswati.jpg" alt="सरस्वती जी"', 'assets/gallery/bal_saraswati_little.jpg" alt="सरस्वती जी"'),
    ('src="assets/deity_saraswati.jpg" alt=""', 'src="assets/gallery/bal_saraswati_little.jpg" alt=""'),
    # Coverflow center Ram/Krishna card -> Ram
    ('assets/deity_krishna.jpg" alt="श्री कृष्ण"', 'assets/gallery/bal_rama_little.jpg" alt="प्रभु श्री राम"'),
    ('src="assets/deity_krishna.jpg" alt=""', 'src="assets/gallery/bal_rama_little.jpg" alt=""'),
    # Aarti section Ganesh card
    ('assets/gallery/bal_ganesha.jpg" onerror="this.src=\'assets/deity_ganesh.jpg\'',
     'assets/gallery/bal_ganesha_little.jpg" onerror="this.src=\'assets/deity_ganesh.jpg\''),
    # Logo / auth (line 118) - keep this too
    ('assets/gallery/bal_ganesha.jpg" class="auth-logo-img"',
     'assets/gallery/bal_ganesha_little.jpg" class="auth-logo-img"'),
    # Profile avatar
    ('assets/gallery/bal_ganesha.jpg" id="prof-user-avatar"',
     'assets/gallery/bal_ganesha_little.jpg" id="prof-user-avatar"'),
    # Aarti modal img
    ('assets/gallery/bal_ganesha.jpg" style="width:75px; height:75px; border-radius:50%',
     'assets/gallery/bal_ganesha_little.jpg" style="width:75px; height:75px; border-radius:50%'),
    # Saraswati in mantras category icon
    ('assets/deity_saraswati.jpg" class="cat-icon-img" alt="मंत्र"',
     'assets/gallery/bal_saraswati_little.jpg" class="cat-icon-img" alt="मंत्र"'),
]

changed = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        changed += 1
        print(f'✓ Replaced: ...{old[:55]}...')
    else:
        print(f'✗ NOT FOUND: ...{old[:55]}...')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'\nDone! {changed}/{len(replacements)} replacements made.')
