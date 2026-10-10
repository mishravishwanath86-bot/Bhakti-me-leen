import re, sys, os, shutil, glob
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
GALLERY_DIR = BASE_DIR / "assets" / "gallery"
GALLERY_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("INTEGRATING FULL 60 DEITIES INTO DIVYA ROOP GALLERY")
print("=" * 80)

# 1. Copy generated images from artifacts
brain_dir = Path(r"C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9")
divya_mappings = {
    'divya_ganesha': 'divya_ganesha.jpg',
    'divya_shiva': 'divya_shiva.jpg',
    'divya_krishna': 'divya_krishna.jpg',
    'divya_hanuman': 'divya_hanuman.jpg',
    'divya_durga': 'divya_durga.jpg'
}

for prefix, dest_name in divya_mappings.items():
    matches = list(brain_dir.glob(f"{prefix}_*.jpg"))
    if matches:
        latest = sorted(matches, key=os.path.getmtime, reverse=True)[0]
        dest_path = GALLERY_DIR / dest_name
        shutil.copyfile(latest, dest_path)
        print(f"✓ Copied {latest.name} -> assets/gallery/{dest_name}")

# 2. Build DIVYA_ROOP_GALLERY array with all 60 deities
divya_roop_js_code = """
window.DIVYA_ROOP_GALLERY = [
  {
    id: 'divya-ganesha',
    nameHi: 'भगवान श्री गणेश',
    nameEn: 'Lord Ganesha',
    category: 'tridev',
    mantra: '॥ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ । निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥',
    img: 'assets/gallery/divya_ganesha.jpg',
    fallbackImg: 'assets/deity_ganesh.jpg',
    desc: 'Majestic and divine Lord Ganesha seated on an ornate golden throne, holding modaka, axe, and noose, large sacred elephant head with a brilliant radiant crown, vibrant temple background.'
  },
  {
    id: 'divya-krishna',
    nameHi: 'भगवान श्री कृष्ण',
    nameEn: 'Lord Krishna',
    category: 'avatar',
    mantra: '॥ ॐ कृष्णाय वासुदेवाय हरये परमात्मने । प्रणत क्लेशनाशाय गोविंदाय नमो नमः ॥',
    img: 'assets/gallery/divya_krishna.jpg',
    fallbackImg: 'assets/deity_krishna.jpg',
    desc: 'Divine Lord Krishna with radiant bluish skin, adorned with a peacock feather in his golden crown, gracefully playing the bansuri flute, wearing yellow silk pitambara, standing beside the sacred Yamuna in Vrindavan.'
  },
  {
    id: 'divya-shiva',
    nameHi: 'भगवान सदाशिव',
    nameEn: 'Lord Shiva (Mahadev)',
    category: 'tridev',
    mantra: '॥ कर्पूरगौरं करुणावतारं संसारसारम् भुजगेन्द्रहारम् । सदावसन्तं हृदयारविन्दे भवं भवानीसहितं नमामि ॥',
    img: 'assets/gallery/divya_shiva.jpg',
    fallbackImg: 'assets/deity_shiv.jpg',
    desc: 'Lord Shiva in deep meditative posture atop Mount Kailash, crescent moon in matted hair, holy Ganga flowing from his locks, holding a trident (Trishula) and damru, snake coiled around neck.'
  },
  {
    id: 'divya-hanuman',
    nameHi: 'श्री हनुमान',
    nameEn: 'Lord Hanuman',
    category: 'avatar',
    mantra: '॥ मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम् । वातात्मजं वानरयूथमुख्यं श्रीरामदूतं शरणं प्रपद्ये ॥',
    img: 'assets/gallery/divya_hanuman.jpg',
    fallbackImg: 'assets/deity_hanuman.jpg',
    desc: 'Mighty Lord Hanuman in a powerful standing posture, radiant orange-gold aura, holding a heavy golden gada (mace), chest glowing with pure devotion, mountain peak background with clouds.'
  },
  {
    id: 'divya-rama',
    nameHi: 'मर्यादा पुरुषोत्तम श्री राम',
    nameEn: 'Lord Rama',
    category: 'avatar',
    mantra: '॥ रामाय रामभद्राय रामचन्द्राय वेधसे । रघुनाथाय नाथाय सीतायाः पतये नमः ॥',
    img: 'assets/deity_ramayana.jpg',
    fallbackImg: 'assets/gallery/bal_rama.jpg',
    desc: 'Noble Lord Rama holding a grand golden bow (Kodanda) and arrow, glowing radiant aura, princely royal silk attire, divine serene expression, Ayodhya palace terrace at sunset.'
  },
  {
    id: 'divya-saraswati',
    nameHi: 'माँ सरस्वती',
    nameEn: 'Goddess Saraswati',
    category: 'devi',
    mantra: '॥ या कुन्देन्दुतुषारहारधवला या शुभ्रवस्त्रावृता । या वीणावरदण्डमण्डितकरा या श्वेतपद्मासना ॥',
    img: 'assets/deity_saraswati.jpg',
    fallbackImg: 'assets/gallery/bal_saraswati.jpg',
    desc: 'Goddess Saraswati adorned in pure white silk saree, gracefully playing the holy veena, seated on a full-blooming white lotus in a serene river, white swan nearby, glowing golden halo.'
  },
  {
    id: 'divya-lakshmi',
    nameHi: 'माँ लक्ष्मी',
    nameEn: 'Goddess Lakshmi',
    category: 'devi',
    mantra: '॥ ॐ श्रीं ह्रीं क्लीं श्री सिद्ध लक्ष्म्यै नमः ॥',
    img: 'assets/deity_lakshmi.jpg',
    fallbackImg: 'assets/gallery/bal_lakshmi.jpg',
    desc: 'Radiant Goddess Lakshmi seated upon an opulent pink lotus, holding blooming lotuses, shower of shining gold coins flowing from her hand, flanked by royal white elephants offering water.'
  },
  {
    id: 'divya-durga',
    nameHi: 'माँ दुर्गा',
    nameEn: 'Goddess Durga',
    category: 'devi',
    mantra: '॥ सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके । शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते ॥',
    img: 'assets/gallery/divya_durga.jpg',
    fallbackImg: 'assets/deity_durga.jpg',
    desc: 'Fierce and magnificent Goddess Durga riding a mighty roaring lion, ten arms holding divine weapons including trident and sword, blazing radiant halo, epic battlefield against darkness.'
  },
  {
    id: 'divya-kartikeya',
    nameHi: 'भगवान कार्तिकेय (मुरुगन)',
    nameEn: 'Lord Kartikeya / Murugan',
    category: 'tridev',
    mantra: '॥ ॐ शरवणभवाय नमः ॥',
    img: 'assets/deity_kartikeya.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Radiant warrior deity Lord Murugan holding the divine golden Vel spear, seated on a majestic vibrant peacock, royal armor and crown, glowing spiritual light, ancient Dravidian temple backdrop.'
  },
  {
    id: 'divya-vishnu',
    nameHi: 'भगवान श्री विष्णु',
    nameEn: 'Lord Vishnu',
    category: 'tridev',
    mantra: '॥ शान्ताकारं भुजगशयनं पद्मनाभं सुरेशं विश्वाधारं गगनसदृशं मेघवर्णं शुभाङ्गम् ॥',
    img: 'assets/deity_vishnu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Paramount Lord Vishnu reclining peacefully on the cosmic serpent Sheshanaga in the Kshira Sagara (Milky Ocean), four arms holding Shankha, Chakra, Gada, and Padma, infinite cosmic backdrop.'
  },
  {
    id: 'divya-indra',
    nameHi: 'देवराज इंद्र',
    nameEn: 'Lord Indra',
    category: 'vedic',
    mantra: '॥ ॐ इंद्राय नमः ॥',
    img: 'assets/deity_indra.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Majestic King of the Devas, Lord Indra, riding the grand multi-tusked white elephant Airavata, raising a crackling golden lightning bolt (Vajra), towering above celestial storm clouds.'
  },
  {
    id: 'divya-parvati',
    nameHi: 'माँ पार्वती',
    nameEn: 'Goddess Parvati',
    category: 'devi',
    mantra: '॥ ॐ उमा महेश्वराभ्यां नमः ॥',
    img: 'assets/deity_parvati.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Graceful Goddess Parvati seated majestically amidst snow-clad Himalayan peaks, elegant traditional saree and intricate gold jewelry, serene motherly expression, sacred mountain aura.'
  },
  {
    id: 'divya-agni',
    nameHi: 'अग्नि देव',
    nameEn: 'Lord Agni',
    category: 'vedic',
    mantra: '॥ ॐ अग्नये नमः स्वाहा ॥',
    img: 'assets/deity_agni.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Lord Agni with two radiant faces and fiery golden-red hair, riding a powerful flaming ram, surrounded by sacred sacrificial yajna flames, intense warm glowing illumination.'
  },
  {
    id: 'divya-vayu',
    nameHi: 'वायु देव',
    nameEn: 'Lord Vayu',
    category: 'vedic',
    mantra: '॥ ॐ वायवे नमः ॥',
    img: 'assets/deity_vayu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Dynamic and swift Lord Vayu standing atop rushing currents of wind and swirling clouds, holding a celestial banner, transparent divine scarf flowing in the gale.'
  },
  {
    id: 'divya-varuna',
    nameHi: 'वरुण देव',
    nameEn: 'Lord Varuna',
    category: 'vedic',
    mantra: '॥ ॐ वरुणाय नमः ॥',
    img: 'assets/deity_varuna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Sovereign of the cosmic waters Lord Varuna riding a massive mythical Makara beast across stormy ocean waves, holding the sacred noose (pasha), deep blue oceanic glow.'
  },
  {
    id: 'divya-surya',
    nameHi: 'भगवान सूर्य',
    nameEn: 'Lord Surya',
    category: 'navagraha',
    mantra: '॥ ॐ सूर्याय नमः । ॐ घृणि सूर्याय नमः ॥',
    img: 'assets/deity_surya.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Magnificent Lord Surya the Sun God, driving a grand golden single-wheeled chariot drawn by seven radiant white horses, blinding solar flares, soaring across the dawn sky.'
  },
  {
    id: 'divya-chandra',
    nameHi: 'चंद्र देव',
    nameEn: 'Lord Chandra',
    category: 'navagraha',
    mantra: '॥ ॐ सों सोमाय नमः ॥',
    img: 'assets/deity_chandra.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Luminous and peaceful Lord Chandra, God of the Moon, seated on an ornate silver chariot with glowing white antelopes, holding a crystal lotus, tranquil star-studded night sky.'
  },
  {
    id: 'divya-kali',
    nameHi: 'माँ काली',
    nameEn: 'Goddess Kali',
    category: 'devi',
    mantra: '॥ ॐ क्रीं कालिकायै नमः ॥',
    img: 'assets/deity_kali.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Ferocious and supreme Goddess Mahakali with deep dark blue-black complexion, flowing unbound black hair, garland of skulls, holding a raised khadga (curved sword) and severed head.'
  },
  {
    id: 'divya-brahma',
    nameHi: 'भगवान ब्रह्मा',
    nameEn: 'Lord Brahma',
    category: 'tridev',
    mantra: '॥ ॐ ब्रह्मणे नमः ॥',
    img: 'assets/deity_brahma.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Venerable creator Lord Brahma with four bearded wise faces, seated gracefully upon a sacred royal swan (Hamsa), holding holy Vedas and rosary, surrounded by swirling cosmic creation energies.'
  },
  {
    id: 'divya-narasimha',
    nameHi: 'भगवान नरसिंह',
    nameEn: 'Lord Narasimha',
    category: 'avatar',
    mantra: '॥ ॐ उग्रं वीरं महाविष्णुं ज्वलन्तं सर्वतोमुखम् । नृसिंहं भीषणं भद्रं मृत्युमृत्युं नमाम्यहम् ॥',
    img: 'assets/deity_narasimha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Fierce divine incarnation Lord Narasimha, colossal half-man half-lion avatar with blazing mane and glowing sharp eyes, seated upon a shattered palace pillar, ornate golden royal armor.'
  },
  {
    id: 'divya-radha',
    nameHi: 'श्री राधारानी',
    nameEn: 'Goddess Radha',
    category: 'devi',
    mantra: '॥ तप्तकाञ्चनगौराङ्गि राधे वृन्दावनेश्वरि । वृषभानुसुते देवि प्रणमामि हरिप्रिये ॥',
    img: 'assets/deity_radha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Exquisitely beautiful Goddess Radha in a rich traditional Vrindavan lehenga, adorned with pearl jewelry and fresh forest flowers, standing near blooming Kadamba trees by the Yamuna.'
  },
  {
    id: 'divya-balarama',
    nameHi: 'भगवान बलराम',
    nameEn: 'Lord Balarama',
    category: 'avatar',
    mantra: '॥ ॐ बलभद्राय नमः ॥',
    img: 'assets/deity_balarama.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Strong and majestic Lord Balarama with fair moon-like complexion, dressed in deep blue silk robes, wielding a heavy golden plow (Hala) and pestle (Musala), massive serpentine Shesha coils rising behind.'
  },
  {
    id: 'divya-kubera',
    nameHi: 'धनपति कुबेर',
    nameEn: 'Lord Kubera',
    category: 'vedic',
    mantra: '॥ ॐ यक्षाय कुबेराय वैश्रवणाय धनधान्याधिपतये धनधान्यसमृद्धिं मे देहि दापय स्वाहा ॥',
    img: 'assets/deity_kubera.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Prosperous Lord Kubera seated upon an ornate jewel-encrusted golden throne, holding a jewel-spitting mongoose and a vessel overflowing with precious gems and gold coins.'
  },
  {
    id: 'divya-annapurna',
    nameHi: 'माँ अन्नपूर्णा',
    nameEn: 'Goddess Annapurna',
    category: 'devi',
    mantra: '॥ अन्नपूर्णे सदा पूर्णे शङ्करप्राणवल्लभे । ज्ञानवैराग्यसिद्ध्यर्थं भिक्षां देहि च पार्वति ॥',
    img: 'assets/deity_annapurna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Benevolent Goddess Annapurna seated inside the holy city of Kashi, holding a solid gold serving ladle and a bejeweled vessel filled with sacred food grain, warm nurturing expression.'
  },
  {
    id: 'divya-kamadhenu',
    nameHi: 'कामधेनु माता',
    nameEn: 'Goddess Kamadhenu',
    category: 'vedic',
    mantra: '॥ ॐ सुरभ्यै नमः ॥',
    img: 'assets/deity_kamadhenu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Sacred wish-fulfilling cow Goddess Kamadhenu with a divine crown, beautiful white bovine form with intricate spiritual markings and golden horns, standing in a lush heavenly meadow.'
  },
  {
    id: 'divya-hayagriva',
    nameHi: 'भगवान हयग्रीव',
    nameEn: 'Lord Hayagriva',
    category: 'avatar',
    mantra: '॥ ज्ञानानन्दमयं देवं निर्मलस्फटिकाकृतिम् । आधारं सर्वविद्यानां हयग्रीवमुपास्महे ॥',
    img: 'assets/deity_hayagriva.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Lord Hayagriva, the horse-headed incarnation of Lord Vishnu, brilliantly white in complexion, holding palm-leaf sacred scriptures (Vedas) and conch, radiating pure supreme wisdom.'
  },
  {
    id: 'divya-gayatri',
    nameHi: 'माँ गायत्री',
    nameEn: 'Goddess Gayatri',
    category: 'devi',
    mantra: '॥ ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात् ॥',
    img: 'assets/deity_gayatri.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Supreme mother Goddess Gayatri with five radiant crowned faces and ten arms holding sacred Vedic instruments, seated on a magnificent open red lotus, surrounded by a giant golden solar mandala.'
  },
  {
    id: 'divya-ganga',
    nameHi: 'माँ गंगा',
    nameEn: 'Goddess Ganga',
    category: 'river',
    mantra: '॥ ॐ नमो भगवत्यै हिलि हिलि मिलि मिलि गङ्गे माँ पालय पालय स्वाहा ॥',
    img: 'assets/deity_ganga.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Divine Goddess Ganga descending from the heavens, seated majestically upon a sacred Makara (crocodile), holding an overflowing Amrita vessel, surrounded by torrential sacred white water currents.'
  },
  {
    id: 'divya-yamuna',
    nameHi: 'माँ यमुना',
    nameEn: 'Goddess Yamuna',
    category: 'river',
    mantra: '॥ ॐ यमुनाथाय नमः ॥',
    img: 'assets/deity_yamuna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Graceful Goddess Yamuna seated upon a grand river turtle, adorned in ornate dark blue silk garments and pearl ornaments, flowing shimmering waters of the Yamuna River.'
  },
  {
    id: 'divya-shakti',
    nameHi: 'आदि पराशक्ति',
    nameEn: 'Goddess Adi Parashakti',
    category: 'devi',
    mantra: '॥ ॐ श्रीं ह्रीं क्लीं ऐं सौः ॐ ह्रीं श्रीं क ए ई ल ह्रीं ह स क ह ल ह्रीं स क ल ह्रीं सौः ऐं क्लीं ह्रीं श्रीं ॥',
    img: 'assets/deity_shakti.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Supreme primordial energy Goddess Adi Parashakti seated upon the sacred Sri Yantra throne, glowing with the brilliance of a thousand suns, holding trident, bow, arrows, and lotus.'
  },
  {
    id: 'divya-kurma',
    nameHi: 'भगवान कूर्म',
    nameEn: 'Lord Kurma',
    category: 'avatar',
    mantra: '॥ ॐ कूर्माय नमः ॥',
    img: 'assets/deity_kurma.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Massive divine Kurma avatar, colossal ancient cosmic tortoise supporting the churning mountain Mandara upon its back in the churning ocean of milk (Samudra Manthan).'
  },
  {
    id: 'divya-matsya',
    nameHi: 'भगवान मत्स्य',
    nameEn: 'Lord Matsya',
    category: 'avatar',
    mantra: '॥ ॐ मत्स्यरूपाय नमः ॥',
    img: 'assets/deity_matsya.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Mighty Lord Matsya avatar, half-human Vishnu form emerging from the body of an enormous glowing golden horned fish, navigating raging deluge waters and rescuing the sacred Vedas.'
  },
  {
    id: 'divya-varaha',
    nameHi: 'भगवान वराह',
    nameEn: 'Lord Varaha',
    category: 'avatar',
    mantra: '॥ ॐ नमो भगवते वराहरूपाय भूः पदं पतये नमः ॥',
    img: 'assets/deity_varaha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Colossal Lord Varaha avatar, powerful boar-headed deity emerging triumphantly from the dark cosmic ocean, gently lifting Mother Earth (Bhudevi) upon his white tusks.'
  },
  {
    id: 'divya-vamana',
    nameHi: 'भगवान वामन',
    nameEn: 'Lord Vamana',
    category: 'avatar',
    mantra: '॥ ॐ वामनाय नमः ॥',
    img: 'assets/deity_vamana.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Young and radiant Brahmin scholar Lord Vamana holding a wooden umbrella (Chhatra) and water pot (Kamandalu), wearing simple sacred thread and deer skin, stepping gracefully.'
  },
  {
    id: 'divya-parashurama',
    nameHi: 'भगवान परशुराम',
    nameEn: 'Lord Parashurama',
    category: 'avatar',
    mantra: '॥ ॐ जामदग्न्याय विद्महे महावीराय धीमहि तन्नः परशुरामः प्रचोदयात् ॥',
    img: 'assets/deity_parashurama.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Fierce warrior sage Lord Parashurama with ascetic matted locks and rudraksha beads, wielding a razor-sharp divine battle axe (Parashu), standing resolutely in dense forest.'
  },
  {
    id: 'divya-kalki',
    nameHi: 'भगवान कल्कि',
    nameEn: 'Lord Kalki',
    category: 'avatar',
    mantra: '॥ ॐ कल्किने नमः ॥',
    img: 'assets/deity_kalki.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Prophesied Lord Kalki the tenth avatar, fierce warrior clad in shining golden armor, riding a magnificent winged white steed (Devadatta), raising a blazing fiery sword against darkness.'
  },
  {
    id: 'divya-dhanvantari',
    nameHi: 'भगवान धन्वंतरि',
    nameEn: 'Lord Dhanvantari',
    category: 'avatar',
    mantra: '॥ ॐ नमो भगवते महासुदर्शनाय वासुदेवाय धन्वन्तरये अमृतकलशहस्ताय सर्वभयविनाशाय सर्वरोगनिवारणाय ॥',
    img: 'assets/deity_dhanvantari.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Divine physician Lord Dhanvantari emerging from the milky ocean, four arms holding the immortal pot of Amrita, medicinal herbs, radiant healing emerald and gold aura.'
  },
  {
    id: 'divya-vishwakarma',
    nameHi: 'भगवान विश्वकर्मा',
    nameEn: 'Lord Vishwakarma',
    category: 'vedic',
    mantra: '॥ ॐ विश्वकर्मणे नमः ॥',
    img: 'assets/deity_vishwakarma.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Supreme divine architect Lord Vishwakarma holding celestial measuring tools, hammer, and blueprints, surrounded by the towering golden palaces of heaven.'
  },
  {
    id: 'divya-brihaspati',
    nameHi: 'गुरु बृहस्पति',
    nameEn: 'Lord Brihaspati',
    category: 'navagraha',
    mantra: '॥ ॐ ग्रां ग्रीं ग्रौं सः गुरवे नमः ॥',
    img: 'assets/deity_brihaspati.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Wise Guru Brihaspati, preceptor of the gods, draped in yellow pitambara robes, seated on a golden pedestal with sacred Vedic palm manuscripts, radiating supreme golden intellect.'
  },
  {
    id: 'divya-shukra',
    nameHi: 'शुक्राचार्य',
    nameEn: 'Lord Shukra',
    category: 'navagraha',
    mantra: '॥ ॐ द्रां द्रीं द्रौं सः शुक्राय नमः ॥',
    img: 'assets/deity_shukra.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Formidable sage Shukracharya in luminous white garments, holding a staff and crystal rosary, surrounded by mystical Sanjivani glowing herbs, deep diamond-like white luminescence.'
  },
  {
    id: 'divya-shani',
    nameHi: 'शनि देव',
    nameEn: 'Lord Shani',
    category: 'navagraha',
    mantra: '॥ ॐ प्रां प्रीं प्रौं सः शनैश्चराय नमः ॥',
    img: 'assets/deity_shani.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Stern and mighty Lord Shani (Saturn) clad in dark blue and black robes, wielding a heavy iron bow and sword, riding a majestic black raven (crow), dark nebula night sky.'
  },
  {
    id: 'divya-mangala',
    nameHi: 'मंगल देव',
    nameEn: 'Lord Mangala',
    category: 'navagraha',
    mantra: '॥ ॐ क्रां क्रीं क्रौं सः भौमाय नमः ॥',
    img: 'assets/deity_mangala.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Fierce Mars deity Lord Mangala with a blazing red complexion and crimson royal garments, wielding a spear and shield, riding a powerful charging ram.'
  },
  {
    id: 'divya-budha',
    nameHi: 'बुध देव',
    nameEn: 'Lord Budha',
    category: 'navagraha',
    mantra: '॥ ॐ ब्रां ब्रीं ब्रौं सः बुधाय नमः ॥',
    img: 'assets/deity_budha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Graceful Mercury deity Lord Budha draped in emerald green garments, riding a fierce winged lion, holding ancient scrolls of knowledge, bright radiant green halo.'
  },
  {
    id: 'divya-rahu',
    nameHi: 'राहु देव',
    nameEn: 'Lord Rahu',
    category: 'navagraha',
    mantra: '॥ ॐ भ्रां भ्रीं भ्रौं सः राहवे नमः ॥',
    img: 'assets/deity_rahu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Mysterious shadow deity Lord Rahu, a colossal cosmic head emerging from dark nebula smoke, fierce expression with glowing eyes, eclipsing the golden sun.'
  },
  {
    id: 'divya-ketu',
    nameHi: 'केतु देव',
    nameEn: 'Lord Ketu',
    category: 'navagraha',
    mantra: '॥ ॐ स्रां स्रीं स्रौं सः केतवे नमः ॥',
    img: 'assets/deity_ketu.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Ethereal shadow deity Lord Ketu, celestial torso draped in starry cosmic robes, riding a luminous vulture amidst meteor showers and deep-space celestial formations.'
  },
  {
    id: 'divya-yama',
    nameHi: 'यमराज',
    nameEn: 'Lord Yama',
    category: 'vedic',
    mantra: '॥ ॐ सूर्यपुत्राय विद्महे दण्डधराय धीमहि तन्नो यमः प्रचोदयात् ॥',
    img: 'assets/deity_yama.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Imposing God of Justice and Death, Lord Yamaraja, dark complexion, holding a heavy golden mace (Gada) and the rope of mortality (Pasha), riding a massive water buffalo.'
  },
  {
    id: 'divya-sita',
    nameHi: 'माँ सीता',
    nameEn: 'Goddess Sita',
    category: 'devi',
    mantra: '॥ ॐ जानक्यै नमः ॥',
    img: 'assets/deity_sita.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Graceful and royal Goddess Sita in elegant golden silk saree, adorned with exquisite traditional jewelry, standing beside Lord Rama in the court of Ayodhya, divine serene smile.'
  },
  {
    id: 'divya-lakshmana',
    nameHi: 'श्री लक्ष्मण',
    nameEn: 'Lord Lakshmana',
    category: 'avatar',
    mantra: '॥ ॐ लक्ष्मणाय नमः ॥',
    img: 'assets/deity_lakshmana.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Steadfast warrior Lord Lakshmana with keen determined eyes, holding a taut bow and quiver of arrows, standing protectively in dense Dandakaranya forest.'
  },
  {
    id: 'divya-bharata',
    nameHi: 'श्री भरत',
    nameEn: 'Lord Bharata',
    category: 'avatar',
    mantra: '॥ ॐ भरताय नमः ॥',
    img: 'assets/deity_bharata.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Noble Lord Bharata dressed in simple hermit robes, holding the holy wooden padukas (sandals) of Lord Rama atop his head with deep reverence, sunrise over Nandigram.'
  },
  {
    id: 'divya-shatrughna',
    nameHi: 'श्री शत्रुघ्न',
    nameEn: 'Lord Shatrughna',
    category: 'avatar',
    mantra: '॥ ॐ शत्रुघ्नाय नमः ॥',
    img: 'assets/deity_shatrughna.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Heroic prince Lord Shatrughna in majestic battle attire, holding sword and shield, standing triumphantly before the city gates of Mathura.'
  },
  {
    id: 'divya-tulsi',
    nameHi: 'तुलसी माता',
    nameEn: 'Goddess Tulsi Devi',
    category: 'devi',
    mantra: '॥ महाप्रसाद जननी सर्व सौभाग्यवर्धिनी । आधि व्याधि हरा नित्यं तुलसी त्वं नमोऽस्तु ते ॥',
    img: 'assets/deity_tulsi.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Divine Goddess Tulsi Devi with a gentle glowing aura, holding a sacred lotus, manifesting beside a grand ornate carved stone Tulsi Vrindavan planter.'
  },
  {
    id: 'divya-narmada',
    nameHi: 'माँ नर्मदा',
    nameEn: 'Goddess Narmada',
    category: 'river',
    mantra: '॥ नर्मदे हर । ॐ नर्मदायै नमः ॥',
    img: 'assets/deity_narmada.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Serene Goddess Narmada sitting on a smooth river rock, dressed in sparkling green and blue silks, holy Shivalingas visible on the riverbed through clear sparkling waters.'
  },
  {
    id: 'divya-saraswati-river',
    nameHi: 'सरस्वती नदी देवी',
    nameEn: 'Goddess Saraswati River',
    category: 'river',
    mantra: '॥ ॐ सरस्वत्यै पावकनः सरस्वति ॥',
    img: 'assets/deity_saraswati_river.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Ancient and mystical River Goddess Saraswati with glowing translucent form, flowing gracefully amidst fertile Vedic plains, holding water vessels and ancient scripts.'
  },
  {
    id: 'divya-garuda',
    nameHi: 'गरुड़ देव',
    nameEn: 'Lord Garuda',
    category: 'vedic',
    mantra: '॥ ॐ खं खगाय गरुडाय नमः ॥',
    img: 'assets/deity_garuda.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Massive and majestic eagle king Lord Garuda, colossal golden wings with brilliant feathers, sharp eagle beak on a powerful muscular warrior body, soaring across high Himalayan skies.'
  },
  {
    id: 'divya-shesha',
    nameHi: 'अनंत शेषनाग',
    nameEn: 'Lord Sheshanaga',
    category: 'vedic',
    mantra: '॥ ॐ अनन्ताय नमः ॥',
    img: 'assets/deity_shesha.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Gigantic thousand-headed cosmic serpent Ananta Sheshanaga rising from the boundless Kshira Sagara ocean, each golden-crowned hood emitting radiant beams of light, supporting the cosmos.'
  },
  {
    id: 'divya-nandi',
    nameHi: 'नंदी देव',
    nameEn: 'Lord Nandi',
    category: 'vedic',
    mantra: '॥ ॐ तत्पुरुषाय विद्महे नन्दिकेश्वराय धीमहि तन्नो वृषभः प्रचोदयात् ॥',
    img: 'assets/deity_nandi.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Lord Nandi in his majestic anthropomorphic warrior form with a sacred white bull head, muscular build, holding golden axe, wearing temple bells and rudraksha garlands.'
  },
  {
    id: 'divya-katyayani',
    nameHi: 'माँ कात्यायनी',
    nameEn: 'Goddess Katyayani',
    category: 'devi',
    mantra: '॥ ॐ कात्यायनि महामाये महायोगिन्यधीश्वरि । नन्दगोपसुतं देवि पतिं मे कुरु ते नमः ॥',
    img: 'assets/deity_katyayani.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Fierce warrior form Goddess Katyayani with blazing golden complexion, holding a flashing sword and lotus, riding a ferocious roaring lion into battle against demons.'
  },
  {
    id: 'divya-brahmacharini',
    nameHi: 'माँ ब्रह्मचारिणी',
    nameEn: 'Goddess Brahmacharini',
    category: 'devi',
    mantra: '॥ दधाना करपद्माभ्यामक्षमालाकमण्डलू । देवी प्रसीदतु मयि ब्रह्मचारिण्यनुत्तमा ॥',
    img: 'assets/deity_brahmacharini.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Ascetic Goddess Brahmacharini walking barefoot in pristine white robes, holding a rudraksha japamala in one hand and kamandalu in the other, serene meditation glow.'
  },
  {
    id: 'divya-kushmanda',
    nameHi: 'माँ कूष्मांडा',
    nameEn: 'Goddess Kushmanda',
    category: 'devi',
    mantra: '॥ सुरासम्पूर्णकलशं रुधिराप्लुतमेव च । दधाना हस्तपद्माभ्यां कूष्माण्डा शुभदास्तु मे ॥',
    img: 'assets/deity_kushmanda.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Radiant Goddess Kushmanda sitting on a majestic lion inside the blazing core of the Sun, eight arms holding divine weapons and glowing amrita vessel, blinding solar atmosphere.'
  },
  {
    id: 'divya-mahagauri',
    nameHi: 'माँ महागौरी',
    nameEn: 'Goddess Mahagauri',
    category: 'devi',
    mantra: '॥ श्वेते वृषे समारूढा श्वेताम्बरधरा शुचिः । महागौरी शुभं दद्यान्महादेवप्रमोददा ॥',
    img: 'assets/deity_mahagauri.jpg',
    fallbackImg: 'assets/app_logo_circle.png',
    desc: 'Extremely fair and luminous Goddess Mahagauri dressed in pure white silk, riding a peaceful white bull, holding trident and damru while raising her hand in blessing.'
  }
];
"""

# Replace window.DIVYA_ROOP_GALLERY in app.js
app_js_path = BASE_DIR / "app.js"
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js_content = f.read()

# Replace the previous DIVYA_ROOP_GALLERY definition with the full 60 deities array
old_pattern = r'window\.DIVYA_ROOP_GALLERY\s*=\s*\[[\s\S]*?\];'
if re.search(old_pattern, js_content):
    js_content = re.sub(old_pattern, divya_roop_js_code.strip(), js_content, count=1)
    print("✓ Replaced window.DIVYA_ROOP_GALLERY in app.js with full 60 deities array")
else:
    js_content += "\n" + divya_roop_js_code
    print("✓ Appended window.DIVYA_ROOP_GALLERY to app.js")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("=" * 80)
print("60 DEITIES DIVYA ROOP INTEGRATION COMPLETE")
print("=" * 80)
