import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8', newline='') as f:
    html = f.read()

# Remove stray duplicate img tags that got injected near </main>
stray1 = '<img id="reward-wallpaper-img" src="assets/gallery/bal_narasimha_little.jpg" alt="4K Wallpaper" style="width:65px; height:65px; border-radius:12px; object-fit:cover; border:2px solid #F8C83B;" />\r\n'
stray2 = '<img id="reward-wallpaper-img" src="assets/gallery/bal_radha_little.jpg" alt="4K Wallpaper" style="width:65px; height:65px; border-radius:12px; object-fit:cover; border:2px solid #F8C83B;" />\r\n'
stray3 = '<img id="reward-wallpaper-img" src="assets/gallery/bal_kubera_little.jpg" alt="4K Wallpaper" style="width:65px; height:65px; border-radius:12px; object-fit:cover; border:2px solid #F8C83B;" />\r\n'

for stray in [stray1, stray2, stray3]:
    if stray in html:
        html = html.replace('        ' + stray, '', 1)
        print('Removed stray: ' + stray[:60])
    else:
        print('Not found (clean): ' + stray[:60])

# Now fix reward-wallpaper-img src to Radha
old_rw = 'src="assets/gallery/bal_ganesha.jpg" alt="4K Wallpaper"'
new_rw = 'src="assets/gallery/bal_radha_little.jpg" alt="4K Wallpaper"'
if old_rw in html:
    html = html.replace(old_rw, new_rw, 1)
    print('Fixed reward-wallpaper-img -> Radha')
else:
    print('reward-wallpaper-img already updated')

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)

# Final verification
all_little = [
    'bal_ganesha_little','bal_rama_little','bal_lakshmi_little',
    'bal_saraswati_little','bal_durga_little',
    'bal_vishnu_little','bal_murugan_little','bal_indra_little',
    'bal_parvati_little','bal_agni_little',
    'bal_vayu_little','bal_varuna_little','bal_surya_little',
    'bal_chandra_little','bal_kali_little',
    'bal_brahma_little','bal_narasimha_little','bal_radha_little',
    'bal_balarama_little','bal_kubera_little'
]
print()
ok = 0
for name in all_little:
    cnt = html.count(name)
    if cnt > 0:
        ok += 1
    print(name + ': ' + str(cnt) + ' [' + ('OK' if cnt > 0 else 'MISSING') + ']')

print()
print('FINAL SCORE: ' + str(ok) + '/20 little deity images in app')
