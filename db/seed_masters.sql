-- ====================================================================
-- BHAKTI APP: SEED MASTER DATA (DEITIES, CONTENT TYPES, CATEGORIES)
-- ====================================================================

-- 1. SEED DEITIES (20 Master Deities)
INSERT OR REPLACE INTO deities (id, name_hi, name_en, icon_emoji, thumbnail, display_order, is_active) VALUES
('ram', 'श्री राम', 'Shri Ram', '🏹', 'assets/deity_ram.jpg', 1, 1),
('krishna', 'श्री कृष्ण', 'Shri Krishna', '🪈', 'assets/deity_krishna.jpg', 2, 1),
('radharani', 'राधा रानी', 'Radha Rani', '🌸', 'assets/deity_radha_krishna.jpg', 3, 1),
('shiva', 'शिव जी', 'Lord Shiva', '🔱', 'assets/deity_shiv.jpg', 4, 1),
('hanuman', 'हनुमान जी', 'Hanuman Ji', '🐒', 'assets/deity_hanuman.jpg', 5, 1),
('durga_mata', 'माता रानी/दुर्गा', 'Mata Rani / Durga', '🦁', 'assets/deity_durga.jpg', 6, 1),
('ganesh', 'श्री गणेश', 'Lord Ganesha', '🐘', 'assets/deity_ganesh.jpg', 7, 1),
('vishnu', 'भगवान विष्णु', 'Lord Vishnu', '🐚', 'assets/deity_vishnu.jpg', 8, 1),
('lakshmi', 'माता लक्ष्मी', 'Mata Lakshmi', '🪷', 'assets/deity_lakshmi.jpg', 9, 1),
('saraswati', 'सरस्वती माता', 'Mata Saraswati', '🪕', 'assets/deity_saraswati.jpg', 10, 1),
('surya', 'सूर्य देव', 'Surya Dev', '☀️', 'assets/deity_surya.jpg', 11, 1),
('shanidev', 'शनिदेव', 'Shanidev', '⚖️', 'assets/deity_shanidev.jpg', 12, 1),
('khatushyam', 'खाटू श्याम जी', 'Khatu Shyam Ji', '👑', 'assets/deity_khatushyam.jpg', 13, 1),
('bhairav', 'भैरव बाबा', 'Bhairav Baba', '🐕', 'assets/deity_nataraja.jpg', 14, 1),
('santoshi', 'संतोषी माता', 'Santoshi Mata', '🌺', 'assets/deity_santoshi.jpg', 15, 1),
('ganga', 'गंगा मैया', 'Ganga Maiya', '🌊', 'assets/deity_ganga.jpg', 16, 1),
('yamuna', 'यमुना मैया', 'Yamuna Maiya', '💧', 'assets/deity_ganga.jpg', 17, 1),
('guru_sant', 'गुरु/संत', 'Guru / Sant', '🧘', 'assets/deity_saibaba.jpg', 18, 1),
('other_deities', 'अन्य देवी-देवता', 'Other Deities', '🕉️', 'assets/mix_gods_hero.jpg', 19, 1),
('general_bhakti', 'सामान्य भक्ति', 'General Bhakti', '✨', 'assets/auth_divine_emblem.jpg', 20, 1);

-- 2. SEED CONTENT TYPES (13 Primary Types)
INSERT OR REPLACE INTO content_types (id, name_hi, name_en, icon, display_order, is_active) VALUES
('bhajan', 'भजन', 'Bhajan', '🎵', 1, 1),
('aarti', 'आरती', 'Aarti', '🪔', 2, 1),
('chalisa', 'चालीसा', 'Chalisa', '📖', 3, 1),
('mantra', 'मंत्र', 'Mantra', '🕉️', 4, 1),
('stotram', 'स्तोत्र', 'Stotram', '📜', 5, 1),
('katha', 'कथा', 'Katha', '🎙️', 6, 1),
('dharmik_gyan', 'धार्मिक ज्ञान', 'Dharmik Gyan', '💡', 7, 1),
('satsang', 'सत्संग', 'Satsang', '🧘', 8, 1),
('chetawani_bhajan', 'चेतावनी/ज्ञान भजन', 'Chetawani Bhajan', '🔔', 9, 1),
('festival_special', 'त्योहार विशेष', 'Festival Special', '🎉', 10, 1),
('vrat_katha', 'व्रत कथा', 'Vrat Katha', '🌺', 11, 1),
('temple_katha', 'मंदिर/तीर्थ कथा', 'Temple / Pilgrimage Katha', '🛕', 12, 1),
('naam_jaap', 'भगवान के नाम/नाम-जप', 'Naam Jaap', '📿', 13, 1);

-- 3. SEED THEOLOGICAL CATEGORIES
INSERT OR REPLACE INTO categories (id, name_hi, name_en, description, display_order) VALUES
('bhakti', 'भक्ति रस', 'Bhakti Rasa', 'समर्पण, स्तुति व प्रेम रस प्रधान', 1),
('gyan', 'ज्ञान व वैराग्य', 'Gyan & Vairagya', 'आत्मज्ञान, उपदेश व जीवन मूल्य', 2),
('leela', 'चरित्र व दिव्य लीला', 'Divine Leela', 'प्रभु के पावन अवतार व बाल-चरित्र', 3),
('stuti', 'नित्य वंदना व स्तुति', 'Nitya Stuti', 'प्रातः-संध्या स्तुति व ध्यान', 4),
('vrat_puja', 'व्रत व पूजन विधि', 'Vrat & Puja', 'पर्व-उपवास व अनुष्ठान विधि', 5),
('parva_utsav', 'उत्सव व पर्व', 'Festivals & Utsav', 'प्रमुख सनातन पर्व व जयंती विशेष', 6),
('dhyan_naam', 'नाम-स्मरण व जप', 'Naam Smaran', 'दिव्य नाम महिमा व मंत्र-जप', 7);
