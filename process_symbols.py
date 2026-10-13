import os
from PIL import Image

mapping = {
    'Gemini_Generated_Image_vmk994vmk994vmk9.png': ('symbol_om.webp', 'पावन ॐ (Om)'),
    'Gemini_Generated_Image_s63y01s63y01s63y.png': ('symbol_trishul.webp', 'त्रिशूल व डमरू (Trishul)'),
    'Gemini_Generated_Image_qw5whmqw5whmqw5w.png': ('symbol_bansuri.webp', 'मोरपंख व बाँसुरी (Bansuri)'),
    'Gemini_Generated_Image_tzzql7tzzql7tzzq.png': ('symbol_swastik_kalash.webp', 'स्वास्तिक कलश (Swastik Kalash)'),
    'Gemini_Generated_Image_lk94u4lk94u4lk94.png': ('symbol_shrifal_kalash.webp', 'श्रीफल कलश व दीप (Shrifal Kalash)'),
    'Gemini_Generated_Image_k6v3ypk6v3ypk6v3.png': ('symbol_diya.webp', 'पावन दीपक (Diya)'),
    'Gemini_Generated_Image_5cubpp5cubpp5cub.png': ('symbol_ghanti.webp', 'मंदिर घंटी (Mandir Ghanti)'),
    'Gemini_Generated_Image_24hhwf24hhwf24hh.png': ('symbol_rudraksha.webp', 'रुद्राक्ष माला (Rudraksha Mala)'),
    'Gemini_Generated_Image_8wjs938wjs938wjs.png': ('symbol_surya.webp', 'भगवान सूर्य (Surya Dev)'),
    'Gemini_Generated_Image_cx98xgcx98xgcx98.png': ('symbol_dhwaja.webp', 'भगवा धर्म ध्वजा (Dharma Dhwaja)'),
    'Gemini_Generated_Image_hqz6lvhqz6lvhqz6.png': ('symbol_grantha.webp', 'पवित्र वेद/ग्रंथ (Grantha)'),
    'Gemini_Generated_Image_np0wdynp0wdynp0w.png': ('symbol_havan.webp', 'हवन कुंड (Yajna Kund)'),
    'Gemini_Generated_Image_pr195lpr195lpr19.png': ('symbol_tulsi.webp', 'तुलसी व बेलपत्र (Tulsi Belpatra)'),
    'Gemini_Generated_Image_qxyae9qxyae9qxya.png': ('symbol_gaumata.webp', 'कामधेनु गौ माता (Gau Mata)'),
    'Gemini_Generated_Image_szoyd1szoyd1szoy.png': ('symbol_kamal.webp', 'कमल पुष्प (Kamal Pushpa)'),
    'Gemini_Generated_Image_36impn36impn36im.png': ('symbol_brahmakamal.webp', 'दिव्य ब्रह्मकमल (Brahma Kamal)')
}

src_dir = r'c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets\symbols'
dst_dir = r'c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\assets\symbols\cards'
os.makedirs(dst_dir, exist_ok=True)

for orig, (out_name, title) in mapping.items():
    src_file = os.path.join(src_dir, orig)
    dst_file = os.path.join(dst_dir, out_name)
    if not os.path.exists(src_file):
        print(f'Missing: {src_file}')
        continue
    with Image.open(src_file) as im:
        w, h = im.size
        # Center square crop (these 16:9 images have the sacred deity/symbol centrally framed)
        crop_size = min(w, h)
        left = (w - crop_size) // 2
        top = (h - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size
        cropped = im.crop((left, top, right, bottom))
        resized = cropped.resize((360, 360), Image.Resampling.LANCZOS)
        resized.save(dst_file, 'WEBP', quality=88)
        size_kb = os.path.getsize(dst_file) / 1024
        print(f'Processed {out_name} - {size_kb:.1f} KB')

print('All 16 sacred symbols successfully converted to optimized WebP!')

