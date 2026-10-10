import re, sys, os, shutil, glob
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
GALLERY_DIR = BASE_DIR / "assets" / "gallery"
GALLERY_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("BUILDING DIVINE GALLERY: BAL ROOP & DIVYA ROOP (60+ DEITIES)")
print("=" * 80)

# 1. Copy generated images from artifacts into assets/gallery/
brain_dir = Path(r"C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9")
gen_mappings = {
    'bal_ganesha': 'bal_ganesha.jpg',
    'bal_krishna': 'bal_krishna.jpg',
    'bal_shiva': 'bal_shiva.jpg',
    'bal_hanuman': 'bal_hanuman.jpg',
    'bal_rama': 'bal_rama.jpg',
    'bal_durga': 'bal_durga.jpg',
    'bal_saraswati': 'bal_saraswati.jpg',
    'bal_lakshmi': 'bal_lakshmi.jpg'
}

for prefix, dest_name in gen_mappings.items():
    matches = list(brain_dir.glob(f"{prefix}_*.jpg"))
    if matches:
        latest = sorted(matches, key=os.path.getmtime, reverse=True)[0]
        dest_path = GALLERY_DIR / dest_name
        shutil.copyfile(latest, dest_path)
        print(f"✓ Copied {latest.name} -> assets/gallery/{dest_name}")

# 2. Add Gallery Data & Renderer to app.js
gallery_data_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🖼️ DIVINE GALLERY SYSTEM (BAL ROOP & DIVYA ROOP - 60+ GODS)
// ══════════════════════════════════════════════════════════════════════════════

window.BAL_ROOP_GALLERY = [
  {
    id: 'bal-ganesha',
    nameHi: 'बाल गणेश',
    nameEn: 'Little Bal Ganesha',
    category: 'tridev',
    mantra: '॥ ॐ गं गणपतये नमः ॥',
    img: 'assets/gallery/bal_ganesha.jpg',
    fallbackImg: 'assets/deity_ganesh.jpg',
    desc: 'Cute chibi baby Ganesha happily eating a tiny sweet laddu, seated on a soft decorative cushion, baby mouse beside him, soft festive background.'
  },
  {
    id: 'bal-krishna',
    nameHi: 'बाल कृष्ण',
    nameEn: 'Little Bal Krishna',
    category: 'avatar',
    mantra: '॥ ॐ नमो भगवते वासुदेवाय ॥',
    img: 'assets/gallery/bal_krishna.jpg',
    fallbackImg: 'assets/deity_krishna.jpg',
    desc: 'Adorable chibi baby Krishna with a small peacock feather crown, crawling happily towards a little butter pot, soft pastel Vrindavan background.'
  },
  {
    id: 'bal-shiva',
    nameHi: 'बाल शिव',
    nameEn: 'Little Bal Shiva',
    category: 'tridev',
    mantra: '॥ ॐ नमः शिवाय ॥',
    img: 'assets/gallery/bal_shiva.jpg',
    fallbackImg: 'assets/deity_shiv.jpg',
    desc: 'Cute chibi baby Shiva sitting in meditation, tiny crescent moon in hair, holding a small toy damru and trident, gentle snow-covered Himalayan background.'
  },
  {
    id: 'bal-hanuman',
    nameHi: 'बाल हनुमान',
    nameEn: 'Little Bal Hanuman',
    category: 'avatar',
    mantra: '॥ ॐ हं हनुमते नमः ॥',
    img: 'assets/gallery/bal_hanuman.jpg',
    fallbackImg: 'assets/deity_hanuman.jpg',
    desc: 'Adorable baby Hanuman with small golden mace, flying playfully in the sky reaching for a tiny glowing sun, cheerful clouds.'
  },
  {
    id: 'bal-rama',
    nameHi: 'बाल राम',
    nameEn: 'Little Bal Rama',
    category: 'avatar',
    mantra: '॥ श्री राम जय राम जय जय राम ॥',
    img: 'assets/gallery/bal_rama.jpg',
    fallbackImg: 'assets/deity_ramayana.jpg',
    desc: 'Cute chibi baby Rama holding a tiny toy bow and arrow, seated on a royal velvet mat, soft golden palace background.'
  },
  {
    id: 'bal-durga',
    nameHi: 'बाल दुर्गा',
    nameEn: 'Little Devi Durga',
    category: 'devi',
    mantra: '॥ ॐ दुं दुर्गायै नमः ॥',
    img: 'assets/gallery/bal_durga.jpg',
    fallbackImg: 'assets/deity_durga.jpg',
    desc: 'Adorable baby Durga with eight tiny arms holding cute symbolic items, sitting happily beside a friendly baby lion cub, warm golden glow background.'
  },
  {
    id: 'bal-saraswati',
    nameHi: 'बाल सरस्वती',
    nameEn: 'Little Devi Saraswati',
    category: 'devi',
    mantra: '॥ ॐ ऐं सरस्वत्यै नमः ॥',
    img: 'assets/gallery/bal_saraswati.jpg',
    fallbackImg: 'assets/deity_saraswati.jpg',
    desc: 'Adorable chibi baby Saraswati playing a tiny veena, sitting on a soft white lotus, miniature white swan beside her, soft glowing background.'
  },
  {
    id: 'bal-lakshmi',
    nameHi: 'बाल लक्ष्मी',
    nameEn: 'Little Devi Lakshmi',
    category: 'devi',
    mantra: '॥ ॐ श्रीं महालक्ष्म्यै नमः ॥',
    img: 'assets/gallery/bal_lakshmi.jpg',
    fallbackImg: 'assets/deity_lakshmi.jpg',
    desc: 'Cute chibi baby Lakshmi showering tiny gold coins from her small hands, seated on a glowing pink lotus, gentle festive background with traditional motifs.'
  },
  {
    id: 'bal-kartikeya',
    nameHi: 'बाल कार्तिकेय / मुरुगन',
    nameEn: 'Little Bal Kartikeya / Murugan',
    category: 'tridev',
    mantra: '॥ ॐ शरवणभवाय नमः ॥',
    img: 'assets/deity_kartikeya.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Kartikeya holding a tiny golden Vel spear, sitting next to a colorful baby peacock, vibrant traditional temple background.'
  },
  {
    id: 'bal-vishnu',
    nameHi: 'बाल विष्णु',
    nameEn: 'Little Bal Vishnu',
    category: 'tridev',
    mantra: '॥ ॐ विष्णवे नमः ॥',
    img: 'assets/deity_vishnu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Vishnu with four tiny arms holding miniature conch and chakra, resting gently on a soft cartoon Sheshanaga, cosmic soft glow background.'
  },
  {
    id: 'bal-indra',
    nameHi: 'बाल इंद्र',
    nameEn: 'Little Bal Indra',
    category: 'vedic',
    mantra: '॥ ॐ इंद्राय नमः ॥',
    img: 'assets/deity_indra.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Indra sitting on a miniature white elephant (Airavata), holding a tiny lightning bolt (Vajra), cheerful cartoon style, soft blue sky background.'
  },
  {
    id: 'bal-parvati',
    nameHi: 'बाल पार्वती',
    nameEn: 'Little Devi Parvati',
    category: 'devi',
    mantra: '॥ ॐ उमाये नमः ॥',
    img: 'assets/deity_parvati.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Parvati making tiny mountain-shaped mud pies, sitting in a gentle snowy Himalayan landscape, cute baby mountain goat beside her.'
  },
  {
    id: 'bal-agni',
    nameHi: 'बाल अग्नि',
    nameEn: 'Little Bal Agni',
    category: 'vedic',
    mantra: '॥ ॐ अग्नये नमः ॥',
    img: 'assets/deity_agni.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Agni with small flickering flames for hair, sitting safely inside a gentle glowing fire pit, warm orange and yellow background.'
  },
  {
    id: 'bal-vayu',
    nameHi: 'बाल वायु',
    nameEn: 'Little Bal Vayu',
    category: 'vedic',
    mantra: '॥ ॐ वायवे नमः ॥',
    img: 'assets/deity_vayu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Vayu with small transparent wings, gently floating on a cloud, dynamic light blue wind effect background with stylized leaves.'
  },
  {
    id: 'bal-varuna',
    nameHi: 'बाल वरुण',
    nameEn: 'Little Bal Varuna',
    category: 'vedic',
    mantra: '॥ ॐ वरुणाय नमः ॥',
    img: 'assets/deity_varuna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Varuna sitting on a miniature sea turtle, holding a tiny lasso, blue ocean background with cartoon fish and soft waves.'
  },
  {
    id: 'bal-surya',
    nameHi: 'बाल सूर्य',
    nameEn: 'Little Bal Surya',
    category: 'navagraha',
    mantra: '॥ ॐ सूर्याय नमः ॥',
    img: 'assets/deity_surya.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Bright and cute chibi baby Surya wearing a radiant sun-shaped crown, sitting on a tiny single-wheeled chariot drawn by a cute miniature horse.'
  },
  {
    id: 'bal-chandra',
    nameHi: 'बाल चंद्र',
    nameEn: 'Little Devi Chandra',
    category: 'navagraha',
    mantra: '॥ ॐ सोमाय नमः ॥',
    img: 'assets/deity_chandra.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Chandra with a small crescent moon behind their head, sitting gently on a glowing blue lotus in a peaceful night sky background.'
  },
  {
    id: 'bal-kali',
    nameHi: 'बाल काली',
    nameEn: 'Little Devi Kali',
    category: 'devi',
    mantra: '॥ ॐ क्रीं कालिकायै नमः ॥',
    img: 'assets/deity_kali.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Kali with deep blue skin, a sweet smile, tiny decorative ornaments, four arms holding miniature stylized symbolic items.'
  },
  {
    id: 'bal-brahma',
    nameHi: 'बाल ब्रह्मा',
    nameEn: 'Little Bal Brahma',
    category: 'tridev',
    mantra: '॥ ॐ ब्रह्मणे नमः ॥',
    img: 'assets/deity_brahma.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Brahma with four tiny faces, sitting on a miniature white swan, holding small stylized scriptures (Vedas).'
  },
  {
    id: 'bal-narasimha',
    nameHi: 'बाल नरसिंह',
    nameEn: 'Little Bal Narasimha',
    category: 'avatar',
    mantra: '॥ ॐ नृसिंहाय नमः ॥',
    img: 'assets/deity_narasimha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Narasimha, a playful half-man half-lion cub with a small decorative crown, sitting happily and roaring gently.'
  },
  {
    id: 'bal-radha',
    nameHi: 'बाल राधा',
    nameEn: 'Little Devi Radha',
    category: 'devi',
    mantra: '॥ ॐ राधायै नमः ॥',
    img: 'assets/deity_radha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Radha holding a tiny pot of flowers and making a sweet gesture, bright traditional dress with floral patterns, Vrindavan garden.'
  },
  {
    id: 'bal-balarama',
    nameHi: 'बाल बलराम',
    nameEn: 'Little Bal Balarama',
    category: 'avatar',
    mantra: '॥ ॐ बलभद्राय नमः ॥',
    img: 'assets/deity_balarama.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Balarama with light blue skin, holding a miniature toy plow and pestle, cheerful smile, vibrant blue background.'
  },
  {
    id: 'bal-kubera',
    nameHi: 'बाल कुबेर',
    nameEn: 'Little Bal Kubera',
    category: 'vedic',
    mantra: '॥ ॐ कुबेराय नमः ॥',
    img: 'assets/deity_kubera.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Kubera sitting on a small pot filled with cartoon gold coins, holding a tiny mongoose, cheerful smile, rich golden background.'
  },
  {
    id: 'bal-annapurna',
    nameHi: 'बाल अन्नपूर्णा',
    nameEn: 'Little Devi Annapurna',
    category: 'devi',
    mantra: '॥ ॐ अन्नपूर्णायै नमः ॥',
    img: 'assets/deity_annapurna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Annapurna holding a tiny golden ladle and a small bowl filled with grain, gentle expression, soft pink and green background.'
  },
  {
    id: 'bal-kamadhenu',
    nameHi: 'बाल कामधेनु',
    nameEn: 'Little Devi Kamadhenu',
    category: 'vedic',
    mantra: '॥ ॐ सुरभ्यै नमः ॥',
    img: 'assets/deity_kamadhenu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Kamadhenu, a cute chibi calf with tiny ornate decorations, sitting peacefully in a gentle meadow, soft green and blue background.'
  },
  {
    id: 'bal-hayagriva',
    nameHi: 'बाल हयग्रीव',
    nameEn: 'Little Bal Hayagriva',
    category: 'avatar',
    mantra: '॥ ॐ हयग्रीवाय नमः ॥',
    img: 'assets/deity_hayagriva.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Hayagriva with a playful horse head on a small human body, sitting on a miniature book, cheerful expression, light blue background.'
  },
  {
    id: 'bal-gayatri',
    nameHi: 'बाल गायत्री',
    nameEn: 'Little Devi Gayatri',
    category: 'devi',
    mantra: '॥ ॐ भूर्भुवः स्वः ॥',
    img: 'assets/deity_gayatri.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Gayatri with multiple faces and small golden light effects, sitting inside a glowing mandala, peaceful Vedic background.'
  },
  {
    id: 'bal-ganga',
    nameHi: 'बाल गंगा',
    nameEn: 'Little Devi Ganga',
    category: 'river',
    mantra: '॥ ॐ गंगायै नमः ॥',
    img: 'assets/deity_ganga.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Ganga sitting on a miniature crocodile, holding a small stylized water pot, blue river background with cartoon waves.'
  },
  {
    id: 'bal-yamuna',
    nameHi: 'बाल यमुना',
    nameEn: 'Little Devi Yamuna',
    category: 'river',
    mantra: '॥ ॐ यमुनाथाय नमः ॥',
    img: 'assets/deity_yamuna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Yamuna sitting on a small turtle, holding a tiny water vessel, dynamic blue and green background with stylized water patterns.'
  },
  {
    id: 'bal-shakti',
    nameHi: 'बाल शक्ति',
    nameEn: 'Little Devi Shakti',
    category: 'devi',
    mantra: '॥ ॐ पराशक्त्यै नमः ॥',
    img: 'assets/deity_shakti.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Shakti representing divine power, holding a small glowing trident and tiny symbolic items, seated inside a radiant chakra.'
  },
  {
    id: 'bal-kurma',
    nameHi: 'बाल कूर्म',
    nameEn: 'Little Bal Kurma',
    category: 'avatar',
    mantra: '॥ ॐ कूर्माय नमः ॥',
    img: 'assets/deity_kurma.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Kurma avatar, adorable little turtle form with divine golden ornaments, swimming gently in a celestial milky ocean.'
  },
  {
    id: 'bal-matsya',
    nameHi: 'बाल मत्स्य',
    nameEn: 'Little Bal Matsya',
    category: 'avatar',
    mantra: '॥ ॐ मत्स्याय नमः ॥',
    img: 'assets/deity_matsya.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Matsya avatar, half-baby half-golden-fish, holding tiny holy scriptures, floating playfully in glowing turquoise waters.'
  },
  {
    id: 'bal-varaha',
    nameHi: 'बाल वराह',
    nameEn: 'Little Bal Varaha',
    category: 'avatar',
    mantra: '॥ ॐ वराहाय नमः ॥',
    img: 'assets/deity_varaha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Varaha avatar with a tiny boar face and golden crown, playfully balancing a tiny cute planet Earth on his snout.'
  },
  {
    id: 'bal-vamana',
    nameHi: 'बाल वामन',
    nameEn: 'Little Bal Vamana',
    category: 'avatar',
    mantra: '॥ ॐ वामनाय नमः ॥',
    img: 'assets/deity_vamana.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Vamana dressed as a cute little monk, holding a tiny wooden umbrella and water pot, cheerful innocent smile.'
  },
  {
    id: 'bal-parashurama',
    nameHi: 'बाल परशुराम',
    nameEn: 'Little Bal Parashurama',
    category: 'avatar',
    mantra: '॥ ॐ परशुरामाय नमः ॥',
    img: 'assets/deity_parashurama.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Parashurama holding a miniature decorative battle axe, tiny rudraksha beads, sitting peacefully in a lush forest clearing.'
  },
  {
    id: 'bal-kalki',
    nameHi: 'बाल कल्कि',
    nameEn: 'Little Bal Kalki',
    category: 'avatar',
    mantra: '॥ ॐ कल्किने नमः ॥',
    img: 'assets/deity_kalki.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Kalki sitting atop a cute white winged pony, holding a tiny sparkling toy sword, glowing sunset sky background.'
  },
  {
    id: 'bal-dhanvantari',
    nameHi: 'बाल धन्वंतरि',
    nameEn: 'Little Bal Dhanvantari',
    category: 'avatar',
    mantra: '॥ ॐ धन्वंतरये नमः ॥',
    img: 'assets/deity_dhanvantari.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Dhanvantari holding a tiny pot of golden nectar (Amrita) and miniature healing herbs, soft soothing green and gold aura.'
  },
  {
    id: 'bal-vishwakarma',
    nameHi: 'बाल विश्वकर्मा',
    nameEn: 'Little Bal Vishwakarma',
    category: 'vedic',
    mantra: '॥ ॐ विश्वकर्मणे नमः ॥',
    img: 'assets/deity_vishwakarma.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Vishwakarma holding a tiny cute hammer and blueprint scroll, surrounded by small floating mechanical toys and golden gears.'
  },
  {
    id: 'bal-brihaspati',
    nameHi: 'बाल बृहस्पति',
    nameEn: 'Little Bal Brihaspati',
    category: 'navagraha',
    mantra: '॥ ॐ बृहस्पतये नमः ॥',
    img: 'assets/deity_brihaspati.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Brihaspati sitting with tiny glowing palm leaves and an ink pot, wearing soft yellow robes, golden intellectual aura.'
  },
  {
    id: 'bal-shukra',
    nameHi: 'बाल शुक्र',
    nameEn: 'Little Bal Shukra',
    category: 'navagraha',
    mantra: '॥ ॐ शुक्राय नमः ॥',
    img: 'assets/deity_shukra.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Shukracharya holding a tiny crystal lotus and golden staff, surrounded by soft celestial sparkles, diamond glow.'
  },
  {
    id: 'bal-shani',
    nameHi: 'बाल शनि',
    nameEn: 'Little Bal Shani',
    category: 'navagraha',
    mantra: '॥ ॐ शनैश्चराय नमः ॥',
    img: 'assets/deity_shani.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Shani sitting next to a playful little baby crow, holding a tiny glowing staff, deep sapphire blue and starry night background.'
  },
  {
    id: 'bal-mangala',
    nameHi: 'बाल मंगल',
    nameEn: 'Little Bal Mangala',
    category: 'navagraha',
    mantra: '॥ ॐ भौमाय नमः ॥',
    img: 'assets/deity_mangala.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Mangala wearing bright crimson garments, holding a tiny toy spear, sitting beside a friendly miniature ram.'
  },
  {
    id: 'bal-budha',
    nameHi: 'बाल बुध',
    nameEn: 'Little Bal Budha',
    category: 'navagraha',
    mantra: '॥ ॐ बुधाय नमः ॥',
    img: 'assets/deity_budha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Budha holding a small stylized scroll and riding a miniature cartoon lion, bright emerald green luminous background.'
  },
  {
    id: 'bal-rahu',
    nameHi: 'बाल राहु',
    nameEn: 'Little Bal Rahu',
    category: 'navagraha',
    mantra: '॥ ॐ राहवे नमः ॥',
    img: 'assets/deity_rahu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Rahu floating playfully on a tiny smoky cloud, soft dark violet colors with gentle stars.'
  },
  {
    id: 'bal-ketu',
    nameHi: 'बाल केतु',
    nameEn: 'Little Bal Ketu',
    category: 'navagraha',
    mantra: '॥ ॐ केतवे नमः ॥',
    img: 'assets/deity_ketu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Ketu sitting peacefully inside a glowing celestial ring, soft misty background with shooting stars.'
  },
  {
    id: 'bal-yama',
    nameHi: 'बाल यम',
    nameEn: 'Little Bal Yama',
    category: 'vedic',
    mantra: '॥ ॐ यमाय नमः ॥',
    img: 'assets/deity_yama.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Yama sitting happily atop a friendly baby water buffalo, holding a tiny golden mace, dark teal background.'
  },
  {
    id: 'bal-sita',
    nameHi: 'बाल सीता',
    nameEn: 'Little Devi Sita',
    category: 'devi',
    mantra: '॥ ॐ श्री सीतायै नमः ॥',
    img: 'assets/deity_sita.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Sita sitting among blooming jasmine and lotuses, making a gentle blessing gesture, soft golden palace garden background.'
  },
  {
    id: 'bal-lakshmana',
    nameHi: 'बाल लक्ष्मण',
    nameEn: 'Little Bal Lakshmana',
    category: 'avatar',
    mantra: '॥ ॐ लक्ष्मणाय नमः ॥',
    img: 'assets/deity_lakshmana.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Lakshmana standing loyally with a tiny toy bow, bright royal clothing, radiant and cheerful forest morning background.'
  },
  {
    id: 'bal-bharata',
    nameHi: 'बाल भरत',
    nameEn: 'Little Bal Bharata',
    category: 'avatar',
    mantra: '॥ ॐ भरताय नमः ॥',
    img: 'assets/deity_bharata.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Bharata reverently holding a pair of tiny wooden sandals (padukas), peaceful sunrise background.'
  },
  {
    id: 'bal-shatrughna',
    nameHi: 'बाल शत्रुघ्न',
    nameEn: 'Little Bal Shatrughna',
    category: 'avatar',
    mantra: '॥ ॐ शत्रुघ्नाय नमः ॥',
    img: 'assets/deity_shatrughna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Shatrughna playfully holding a tiny wooden shield, wearing princely ornaments, soft warm royal court background.'
  },
  {
    id: 'bal-tulsi',
    nameHi: 'बाल तुलसी',
    nameEn: 'Little Devi Tulsi',
    category: 'devi',
    mantra: '॥ ॐ तुलस्यै नमः ॥',
    img: 'assets/deity_tulsi.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Tulsi Devi holding a tiny sprig of holy basil, sitting beside a decorated Vrindavan planter, soft pastel morning glow.'
  },
  {
    id: 'bal-narmada',
    nameHi: 'बाल नर्मदा',
    nameEn: 'Little Devi Narmada',
    category: 'river',
    mantra: '॥ ॐ नर्मदायै नमः ॥',
    img: 'assets/deity_narmada.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable baby Narmada sitting beside a sparkling freshwater stream, playing with smooth river pebbles, gentle greenery.'
  },
  {
    id: 'bal-saraswati-river',
    nameHi: 'बाल सरस्वती नदी',
    nameEn: 'Little Devi Saraswati River',
    category: 'river',
    mantra: '॥ ॐ पावकायै नमः ॥',
    img: 'assets/deity_saraswati_river.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby river goddess sitting on a riverbank with blooming lotus flowers, gentle waves and flowing divine waters.'
  },
  {
    id: 'bal-garuda',
    nameHi: 'बाल गरुड़',
    nameEn: 'Little Bal Garuda',
    category: 'vedic',
    mantra: '॥ ॐ गरुडाय नमः ॥',
    img: 'assets/deity_garuda.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Garuda with fluffy golden feathers and tiny wings, sitting on a soft cloud, holding a tiny snake playfully.'
  },
  {
    id: 'bal-shesha',
    nameHi: 'बाल शेषनाग',
    nameEn: 'Little Bal Shesha',
    category: 'vedic',
    mantra: '॥ ॐ अनन्ताय नमः ॥',
    img: 'assets/deity_shesha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi multi-hooded baby snake deity Sheshanaga, smiling cheerfully with a tiny crown atop each head, ocean of milk background.'
  },
  {
    id: 'bal-nandi',
    nameHi: 'बाल नंदी',
    nameEn: 'Little Bal Nandi',
    category: 'vedic',
    mantra: '॥ ॐ नन्दिने नमः ॥',
    img: 'assets/deity_nandi.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby bull Nandi with tiny golden bells around his neck, sitting playfully next to a small cartoon Shiva lingam.'
  },
  {
    id: 'bal-katyayani',
    nameHi: 'बाल कात्यायनी',
    nameEn: 'Little Devi Katyayani',
    category: 'devi',
    mantra: '॥ ॐ कात्यायन्यै नमः ॥',
    img: 'assets/deity_katyayani.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Katyayani wearing bright red and gold, holding a tiny toy sword, seated beside a sleeping baby tiger.'
  },
  {
    id: 'bal-brahmacharini',
    nameHi: 'बाल ब्रह्मचारिणी',
    nameEn: 'Little Devi Brahmacharini',
    category: 'devi',
    mantra: '॥ ॐ ब्रह्मचारिण्यै नमः ॥',
    img: 'assets/deity_brahmacharini.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Brahmacharini holding a miniature rosary (japamala) and tiny water pot, serene white robes, soft celestial light.'
  },
  {
    id: 'bal-kushmanda',
    nameHi: 'बाल कूष्मांडा',
    nameEn: 'Little Devi Kushmanda',
    category: 'devi',
    mantra: '॥ ॐ कूष्मांडायै नमः ॥',
    img: 'assets/deity_kushmanda.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Cute chibi baby Kushmanda surrounded by glowing solar sparkles, holding tiny glowing orbs, radiant orange and cosmic background.'
  },
  {
    id: 'bal-mahagauri',
    nameHi: 'बाल महागौरी',
    nameEn: 'Little Devi Mahagauri',
    category: 'devi',
    mantra: '॥ ॐ महागौर्ये नमः ॥',
    img: 'assets/deity_mahagauri.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Adorable chibi baby Mahagauri sitting gently on a miniature white bull calf, dressed in pure white and pastel pink, calm moonlit mountain background.'
  }
];

window.DIVYA_ROOP_GALLERY = [
  {
    id: 'divya-shiva',
    nameHi: 'भगवान शिव (महाकाल)',
    nameEn: 'Lord Shiva (Mahakal)',
    category: 'tridev',
    mantra: '॥ कर्पूरगौरं करुणावतारं संसारसारम् ॥',
    img: 'assets/deity_shiv.jpg',
    desc: 'त्रिनेत्रधारी, नीलकंठ, डमरू और त्रिशूल धारण किए हुए देवाधिदेव महादेव का परम कल्याणकारी दिव्य स्वरूप।'
  },
  {
    id: 'divya-krishna',
    nameHi: 'श्री राधा-कृष्ण',
    nameEn: 'Shri Radha Krishna',
    category: 'avatar',
    mantra: '॥ हरे कृष्ण हरे राम ॥',
    img: 'assets/deity_krishna.jpg',
    desc: 'मुरली मनोहर, पीताम्बरधारी श्यामसुंदर और रासेश्वरी राधा रानी का नित्य दिव्य युगल स्वरूप।'
  },
  {
    id: 'divya-hanuman',
    nameHi: 'श्री हनुमान जी महाराज',
    nameEn: 'Lord Hanuman',
    category: 'avatar',
    mantra: '॥ मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम् ॥',
    img: 'assets/deity_hanuman.jpg',
    desc: 'अष्टसिद्धि नवनिधि के दाता, संकटमोचन पवनसुत श्री हनुमान जी का अभय प्रदायक स्वरूप।'
  },
  {
    id: 'divya-rama',
    nameHi: 'मर्यादा पुरुषोत्तम श्री राम',
    nameEn: 'Lord Shri Rama',
    category: 'avatar',
    mantra: '॥ रामाय रामभद्राय रामचन्द्राय वेधसे ॥',
    img: 'assets/deity_ramayana.jpg',
    desc: 'कोदंड धनुर्धारी, सूर्यवंश भूषण प्रभु श्री राम एवं जानकी माता का पावन राज्याभिषेक दर्शन।'
  },
  {
    id: 'divya-durga',
    nameHi: 'माँ जगदम्बा दुर्गा',
    nameEn: 'Maa Durga Bhavani',
    category: 'devi',
    mantra: '॥ सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके ॥',
    img: 'assets/deity_durga.jpg',
    desc: 'सिंहवाहिनी, अष्टभुजाधारी, महिषासुरमर्दिनी माँ आदिशक्ति जगदम्बा का तेजोमय स्वरूप।'
  },
  {
    id: 'divya-ganesh',
    nameHi: 'विघ्नहर्ता श्री गणेश',
    nameEn: 'Lord Ganesha',
    category: 'tridev',
    mantra: '॥ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ॥',
    img: 'assets/deity_ganesh.jpg',
    desc: 'प्रथम पूज्य, मोदकप्रिय, रिद्धि-सिद्धि के स्वामी गजानन भगवान श्री गणेश।'
  },
  {
    id: 'divya-lakshmi',
    nameHi: 'माँ महालक्ष्मी',
    nameEn: 'Maa Mahalakshmi',
    category: 'devi',
    mantra: '॥ ॐ श्रीं ह्रीं क्लीं श्री सिद्ध लक्ष्म्यै नमः ॥',
    img: 'assets/deity_lakshmi.jpg',
    desc: 'कमलवासिनी, धन-धान्य और अष्टैश्वर्य प्रदायिनी जगत जननी माँ महालक्ष्मी।'
  },
  {
    id: 'divya-saraswati',
    nameHi: 'माँ ज्ञानदायिनी सरस्वती',
    nameEn: 'Maa Saraswati',
    category: 'devi',
    mantra: '॥ ॐ ऐं सरस्वत्यै नमः ॥',
    img: 'assets/deity_saraswati.jpg',
    desc: 'श्वेत पद्मासना, वीणा-पुस्तक धारिणी, विद्या एवं संगीत की अधिष्ठात्री देवी।'
  },
  {
    id: 'divya-vishnu',
    nameHi: 'भगवान श्री हरि विष्णु',
    nameEn: 'Lord Vishnu (Narayan)',
    category: 'tridev',
    mantra: '॥ शान्ताकारं भुजगशयनं पद्मनाभं सुरेशम् ॥',
    img: 'assets/deity_vishnu.jpg',
    desc: 'क्षीरसागर वासी, चतुर्भुजधारी, शंख-चक्र-गदा-पद्म सुशोभित जगतपालक श्री हरि।'
  },
  {
    id: 'divya-khatushyam',
    nameHi: 'हारे का सहारा - खाटू श्याम जी',
    nameEn: 'Shri Khatu Shyam Ji',
    category: 'avatar',
    mantra: '॥ ॐ श्री श्याम देवाय नमः ॥',
    img: 'assets/speaker_khatushyam.jpg',
    desc: 'शीश के दानी, कलयुग के अवतारी, मोरछड़ी वाले लखदातार श्री खाटू श्याम जी।'
  }
];

window.galleryActiveTab = 'bal'; // 'bal' | 'divya'
window.galleryActiveCategory = 'all';

function renderDivineGallery() {
  const container = document.getElementById('gallery-grid');
  if (!container) return;

  const dataset = window.galleryActiveTab === 'bal' ? window.BAL_ROOP_GALLERY : window.DIVYA_ROOP_GALLERY;
  const searchInput = document.getElementById('gallery-search-input');
  const query = (searchInput ? searchInput.value : '').trim().toLowerCase();

  let filtered = dataset.filter(item => {
    const matchesCat = window.galleryActiveCategory === 'all' || item.category === window.galleryActiveCategory;
    const matchesQuery = !query || 
      item.nameHi.toLowerCase().includes(query) || 
      item.nameEn.toLowerCase().includes(query) || 
      (item.desc && item.desc.toLowerCase().includes(query));
    return matchesCat && matchesQuery;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column:1/-1; text-align:center; padding:3rem 1rem; color:#FDE68A;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">🌸</div>
        <div style="font-size:1.1rem; font-weight:800;">कोई देव स्वरूप नहीं मिला</div>
        <div style="font-size:0.85rem; color:#FBCFE8; margin-top:4px;">कृपया अन्य नाम या श्रेणी खोजें</div>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <div class="gallery-card" onclick="openGalleryLightbox('${item.id}', '${window.galleryActiveTab}')">
      <div class="gallery-card-img-wrap">
        <img 
          src="${item.img}" 
          class="gallery-card-img" 
          alt="${item.nameHi}" 
          loading="lazy"
          onerror="this.src='${item.fallbackImg || 'assets/app_logo_circle.png'}'"
        />
        <div class="gallery-card-badge">${window.galleryActiveTab === 'bal' ? '👶 बाल स्वरूप' : '👑 दिव्य स्वरूप'}</div>
      </div>
      <div class="gallery-card-content">
        <div class="gallery-card-title">${item.nameHi}</div>
        <div class="gallery-card-sub">${item.nameEn}</div>
        <p class="gallery-card-desc">${item.desc.substring(0, 75)}...</p>
        <div class="gallery-card-footer">
          <button class="gallery-card-btn" onclick="event.stopPropagation(); openGalleryLightbox('${item.id}', '${window.galleryActiveTab}')">
            <span>👁️ दर्शन करें</span>
          </button>
          <button class="gallery-fav-mini-btn" onclick="event.stopPropagation(); triggerFlowerShower(); showToast('🌸 ${item.nameHi} के चरणों में पुष्प अर्पित')">
            🌸
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

function switchGalleryTab(tab) {
  window.galleryActiveTab = tab;
  document.querySelectorAll('.gallery-mode-tab-btn').forEach(b => {
    b.classList.toggle('active', b.getAttribute('data-tab') === tab);
  });
  renderDivineGallery();
}

function filterGalleryCategory(cat, btn) {
  window.galleryActiveCategory = cat;
  document.querySelectorAll('.gallery-filter-pill').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  renderDivineGallery();
}

function openGalleryLightbox(itemId, tab) {
  const dataset = tab === 'bal' ? window.BAL_ROOP_GALLERY : window.DIVYA_ROOP_GALLERY;
  const item = dataset.find(x => x.id === itemId);
  if (!item) return;

  const modal = document.getElementById('gallery-lightbox-modal');
  if (!modal) return;

  document.getElementById('lightbox-img').src = item.img;
  document.getElementById('lightbox-img').onerror = function() {
    this.src = item.fallbackImg || 'assets/app_logo_circle.png';
  };
  document.getElementById('lightbox-title').textContent = item.nameHi;
  document.getElementById('lightbox-sub').textContent = item.nameEn;
  document.getElementById('lightbox-mantra').textContent = item.mantra || '॥ ॐ नमो भगवते वासुदेवाय ॥';
  document.getElementById('lightbox-desc').textContent = item.desc;

  modal.style.display = 'flex';
  modal.style.opacity = '1';
  modal.style.pointerEvents = 'auto';

  // Haptic feedback
  if (navigator.vibrate) navigator.vibrate(30);
}

function closeGalleryLightbox() {
  const modal = document.getElementById('gallery-lightbox-modal');
  if (modal) {
    modal.style.display = 'none';
  }
}
"""

with open(BASE_DIR / "app.js", 'a', encoding='utf-8') as f:
    f.write("\n" + gallery_data_js)
print("✓ Injected BAL_ROOP_GALLERY & DIVYA_ROOP_GALLERY dataset into app.js")

# 3. Add Gallery HTML Page (#page-gallery) and Lightbox Modal into index.html
with open(BASE_DIR / "index.html", 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Add Gallery Promo card into #page-home
gallery_home_banner = """
      <!-- 🖼️ DIVINE GALLERY HERO PROMO BANNER 🖼️ -->
      <div style="margin: 0 1.2rem 1.4rem;" onclick="showPage('page-gallery'); setTimeout(renderDivineGallery, 50);">
        <div style="background: linear-gradient(135deg, #1F0738 0%, #43105B 50%, #17042B 100%); border: 1.5px solid #F8C83B; border-radius: 20px; padding: 1.1rem 1.2rem; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 8px 25px rgba(0,0,0,0.4), 0 0 20px rgba(248,200,59,0.25); cursor: pointer; transition: transform 0.2s ease;">
          <div style="display:flex; align-items:center; gap: 1rem;">
            <div style="font-size: 2.3rem; filter: drop-shadow(0 0 12px #F8C83B);">🖼️</div>
            <div>
              <div style="color:#FDE68A; font-weight:900; font-size:1.1rem; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
                <span>पावन दिव्य गैलरी</span>
                <span style="font-size:0.7rem; background:#FF6B00; color:#FFF; padding:2px 8px; border-radius:10px; font-weight:800;">60+ देव स्वरूप</span>
              </div>
              <div style="color:#FBCFE8; font-size:0.82rem;">👶 बाल रूप एवं 👑 दिव्य रूप दर्शन ❯</div>
            </div>
          </div>
          <div style="background:rgba(248,200,59,0.2); width:36px; height:36px; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#FDE68A; font-size:1.2rem; font-weight:900;">❯</div>
        </div>
      </div>
"""

if 'पावन दिव्य गैलरी' not in html:
    # Insert right after coverflow in #page-home
    html = html.replace('<!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->', gallery_home_banner + '\n      <!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->')
    print("✓ Added Divine Gallery banner to #page-home")

# Add #page-gallery page inside <main>
page_gallery_html = """
    <!-- ═════════════════════════════════════════════════════════════════
         🖼️ DIVINE GALLERY PAGE (BAL ROOP & DIVYA ROOP - 60+ GODS)
         ═════════════════════════════════════════════════════════════════ -->
    <section id="page-gallery" class="page">
      <div class="page-header-bar">
        <button class="back-btn" onclick="showPage('page-home')">←</button>
        <h2>🖼️ दिव्य देव दर्शन गैलरी</h2>
        <button class="katha-search-btn" onclick="triggerFlowerShower()">🌸</button>
      </div>

      <!-- Hero Banner -->
      <div class="gallery-hero-stage">
        <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.18); border:1px solid rgba(248,200,59,0.4); padding:4px 14px; border-radius:20px; font-size:0.8rem; font-weight:800; color:#FDE68A; margin-bottom:0.6rem;">
          <span>✨</span> पावन देव दर्शन व बाल स्वरूप झांकी
        </div>
        <h1 style="font-size:1.55rem; font-weight:900; color:#FFFDF8; margin-bottom:0.3rem;">
          दिव्य देव दर्शन गैलरी
        </h1>
        <p style="font-size:0.84rem; color:#FBCFE8; margin-bottom:1.1rem;">
          समस्त 60+ देवी-देवताओं के बाल स्वरूप व दिव्य तेजोमय स्वरूप का पावन दर्शन करें
        </p>

        <!-- Mode Toggle Tabs (बाल रूप vs दिव्य रूप) -->
        <div class="gallery-mode-tabs">
          <button class="gallery-mode-tab-btn active" data-tab="bal" onclick="switchGalleryTab('bal')">
            <span>👶</span> बाल रूप दर्शन (60+)
          </button>
          <button class="gallery-mode-tab-btn" data-tab="divya" onclick="switchGalleryTab('divya')">
            <span>👑</span> दिव्य रूप दर्शन
          </button>
        </div>
      </div>

      <!-- Search Bar -->
      <div class="katha-search-bar" style="margin-bottom:0.9rem;">
        <span class="katha-search-icon">🔍</span>
        <input type="text" class="katha-search-input" id="gallery-search-input" placeholder="देवी-देवता का नाम खोजें (उदा: बाल गणेश, बाल कृष्ण, शिव)..." oninput="renderDivineGallery()" />
      </div>

      <!-- Category Filter Pills -->
      <div style="display:flex; gap:8px; overflow-x:auto; padding-bottom:8px; margin-bottom:1.2rem; scrollbar-width:none;">
        <button class="gallery-filter-pill active" onclick="filterGalleryCategory('all', this)">✨ समस्त स्वरूप</button>
        <button class="gallery-filter-pill" onclick="filterGalleryCategory('avatar', this)">🏹 अवतार व प्रभु</button>
        <button class="gallery-filter-pill" onclick="filterGalleryCategory('devi', this)">🌺 देवियां व माताएं</button>
        <button class="gallery-filter-pill" onclick="filterGalleryCategory('tridev', this)">🔱 त्रिदेव व परिवार</button>
        <button class="gallery-filter-pill" onclick="filterGalleryCategory('navagraha', this)">☀️ नवग्रह देव</button>
        <button class="gallery-filter-pill" onclick="filterGalleryCategory('river', this)">🌊 पावन नदियां</button>
        <button class="gallery-filter-pill" onclick="filterGalleryCategory('vedic', this)">🕉️ वैदिक देव</button>
      </div>

      <!-- Gallery Cards Grid -->
      <div class="gallery-grid" id="gallery-grid">
        <!-- Rendered dynamically by JS -->
      </div>

      <div style="height:6rem;"></div>
    </section>
"""

if 'id="page-gallery"' not in html:
    html = html.replace('</main>', page_gallery_html + '\n  </main>')
    print("✓ Injected #page-gallery into index.html")

# Add Lightbox Full Screen Modal
lightbox_html = """
  <!-- ═════════════════════════════════════════════════════════════════
       👁️ FULL-SCREEN DIVINE DARSHAN LIGHTBOX MODAL
       ═════════════════════════════════════════════════════════════════ -->
  <div id="gallery-lightbox-modal" class="gallery-lightbox-modal" style="display:none;">
    <div class="gallery-lightbox-content">
      <div class="gallery-lightbox-topbar">
        <button class="glass-topbar-btn" onclick="closeGalleryLightbox()">✕</button>
        <div style="font-size:0.95rem; font-weight:800; color:#FDE68A;">॥ पावन दिव्य दर्शन ॥</div>
        <button class="glass-topbar-btn" onclick="triggerFlowerShower()">🌸</button>
      </div>

      <!-- Large Image Frame with Glowing Halo -->
      <div class="gallery-lightbox-img-frame">
        <img id="lightbox-img" src="" alt="Divine Darshan" class="gallery-lightbox-img" />
      </div>

      <!-- Deity Details -->
      <div class="gallery-lightbox-info">
        <div id="lightbox-title" style="font-size:1.45rem; font-weight:900; color:#FFFDF8; margin-bottom:4px;"></div>
        <div id="lightbox-sub" style="font-size:0.88rem; color:#FDE68A; font-weight:700; margin-bottom:8px;"></div>
        
        <!-- Sacred Mantra Box -->
        <div id="lightbox-mantra" style="background:rgba(248,200,59,0.15); border:1px solid rgba(248,200,59,0.4); border-radius:14px; padding:8px 14px; color:#FDE68A; font-weight:800; font-size:0.95rem; margin-bottom:12px; text-shadow:0 0 10px rgba(248,200,59,0.3);"></div>

        <p id="lightbox-desc" style="font-size:0.88rem; color:#FFFDF8; line-height:1.65; margin-bottom:1.4rem; opacity:0.9;"></p>

        <!-- Actions Row -->
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
          <button onclick="triggerFlowerShower(); showToast('🌸 प्रभु के चरणों में पुष्प वर्षा की गई!');" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; font-size:0.9rem; padding:10px 22px; border-radius:20px; border:none; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 4px 15px rgba(248,200,59,0.4);">
            <span>🌸</span> पुष्प अर्पित करें
          </button>
          <button onclick="showToast('📥 वॉलपेपर सहेजा गया!');" style="background:rgba(255,255,255,0.1); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-weight:800; font-size:0.9rem; padding:10px 20px; border-radius:20px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            <span>📥</span> वॉलपेपर लगाएं
          </button>
        </div>
      </div>
    </div>
  </div>
"""

if 'id="gallery-lightbox-modal"' not in html:
    html = html.replace('</body>', lightbox_html + '\n</body>')
    print("✓ Injected #gallery-lightbox-modal into index.html")

with open(BASE_DIR / "index.html", 'w', encoding='utf-8') as f:
    f.write(html)

# 4. Add Gallery CSS styles to styles.css
gallery_css = """
/* ══════════════════════════════════════════════════════════════════
   🖼️ DIVINE GALLERY STYLING (BAL ROOP & DIVYA ROOP)
   ══════════════════════════════════════════════════════════════════ */
.gallery-hero-stage {
  background: linear-gradient(135deg, #1C0A35 0%, #3B1259 50%, #150628 100%);
  border-radius: 24px;
  padding: 1.4rem 1.2rem;
  margin-bottom: 1.2rem;
  border: 1.5px solid rgba(248, 200, 59, 0.4);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.gallery-mode-tabs {
  display: flex;
  justify-content: center;
  gap: 10px;
  background: rgba(18, 6, 36, 0.7);
  padding: 6px;
  border-radius: 26px;
  border: 1px solid rgba(248, 200, 59, 0.3);
  max-width: 380px;
  margin: 0 auto;
}

.gallery-mode-tab-btn {
  flex: 1;
  background: transparent;
  border: none;
  color: #FDE68A;
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: 800;
  font-size: 0.85rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.25s ease;
}

.gallery-mode-tab-btn.active {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  box-shadow: 0 4px 15px rgba(248, 200, 59, 0.4);
  transform: scale(1.02);
}

.gallery-filter-pill {
  background: rgba(35, 14, 66, 0.6);
  border: 1px solid rgba(248, 200, 59, 0.3);
  color: #FDE68A;
  padding: 6px 14px;
  border-radius: 18px;
  font-weight: 700;
  font-size: 0.8rem;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.2s ease;
}

.gallery-filter-pill.active {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  border-color: #F8C83B;
  box-shadow: 0 3px 12px rgba(248, 200, 59, 0.35);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 14px;
  margin-bottom: 1.5rem;
}

@media (min-width: 600px) {
  .gallery-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 18px;
  }
}

.gallery-card {
  background: linear-gradient(145deg, rgba(32, 12, 60, 0.9) 0%, rgba(18, 6, 36, 0.95) 100%);
  border: 1.5px solid rgba(248, 200, 59, 0.25);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  display: flex;
  flex-direction: column;
}

.gallery-card:hover {
  transform: translateY(-5px) scale(1.02);
  border-color: rgba(248, 200, 59, 0.7);
  box-shadow: 0 14px 30px rgba(248, 200, 59, 0.2), 0 8px 30px rgba(0,0,0,0.6);
}

.gallery-card-img-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 1 / 1;
  overflow: hidden;
  background: #140728;
}

.gallery-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.gallery-card:hover .gallery-card-img {
  transform: scale(1.08);
}

.gallery-card-badge {
  position: absolute;
  top: 8px;
  left: 8px;
  background: rgba(18, 6, 36, 0.85);
  border: 1px solid rgba(248, 200, 59, 0.5);
  color: #FDE68A;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 10px;
  backdrop-filter: blur(8px);
}

.gallery-card-content {
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.gallery-card-title {
  font-size: 0.98rem;
  font-weight: 900;
  color: #FFFDF8;
  line-height: 1.25;
  margin-bottom: 2px;
}

.gallery-card-sub {
  font-size: 0.72rem;
  color: #FDE68A;
  font-weight: 600;
  margin-bottom: 6px;
}

.gallery-card-desc {
  font-size: 0.72rem;
  color: #E2E8F0;
  line-height: 1.4;
  margin-bottom: 10px;
  flex: 1;
}

.gallery-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
}

.gallery-card-btn {
  flex: 1;
  background: linear-gradient(135deg, rgba(248, 200, 59, 0.18) 0%, rgba(217, 119, 6, 0.25) 100%);
  border: 1px solid rgba(248, 200, 59, 0.4);
  color: #FDE68A;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 6px 10px;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.gallery-card-btn:hover {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
}

.gallery-fav-mini-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.3);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.15s ease;
}

.gallery-fav-mini-btn:hover {
  transform: scale(1.2);
}

/* Lightbox Modal */
.gallery-lightbox-modal {
  position: fixed;
  inset: 0;
  z-index: 100000;
  background: radial-gradient(circle at 50% 20%, rgba(35, 10, 68, 0.98) 0%, rgba(12, 3, 25, 0.99) 55%, rgba(5, 1, 12, 1) 100%);
  backdrop-filter: blur(35px);
  -webkit-backdrop-filter: blur(35px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  overflow-y: auto;
  padding: 1.2rem 1.4rem 2.5rem;
}

.gallery-lightbox-content {
  width: 100%;
  max-width: 440px;
  display: flex;
  flex-direction: column;
  margin: auto 0;
  text-align: center;
}

.gallery-lightbox-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 1.2rem;
}

.gallery-lightbox-img-frame {
  width: 100%;
  max-width: 320px;
  aspect-ratio: 1 / 1;
  margin: 0 auto 1.4rem;
  border-radius: 28px;
  background: linear-gradient(145deg, #2D104E 0%, #150628 100%);
  border: 2px solid rgba(248, 200, 59, 0.5);
  padding: 6px;
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.8), 0 0 35px rgba(248, 200, 59, 0.35);
  overflow: hidden;
}

.gallery-lightbox-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 22px;
}
"""

with open(BASE_DIR / "styles.css", 'a', encoding='utf-8') as f:
    f.write("\n" + gallery_css)
print("✓ Appended gallery CSS styles to styles.css")

print("=" * 80)
print("DIVINE GALLERY BUILD COMPLETE")
print("=" * 80)
