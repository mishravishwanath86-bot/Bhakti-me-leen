# ====================================================================
# BHAKTI APP: BILINGUAL HINDI-ENGLISH NORMALIZER & KEYWORD ENGINE
# ====================================================================

import re
import unicodedata
from typing import List, Set

BILINGUAL_MAP = {
    'ram': ['राम', 'श्रीराम', 'रघुनाथ', 'राघव', 'shri ram', 'ram', 'raghav', 'raghunath', 'sita ram', 'सियाराम'],
    'krishna': ['कृष्ण', 'श्रीकृष्ण', 'कान्हा', 'गोपाल', 'मुरलीधर', 'माधव', 'shri krishna', 'krishna', 'kanha', 'gopal', 'murlidhar', 'madhav', 'govind', 'गोविंद'],
    'radharani': ['राधा', 'राधारानी', 'किशोरी', 'बरसाने', 'radha', 'radharani', 'kishori', 'barsana', 'radhe radhe', 'राधे'],
    'shiva': ['शिव', 'भोलेनाथ', 'महादेव', 'शंकर', 'त्रिकाल', 'रुद्र', 'shiva', 'bholenath', 'mahadev', 'shankar', 'rudra', 'neelkanth', 'नीलकंठ'],
    'hanuman': ['हनुमान', 'बजरंगबली', 'संकटमोचन', 'मारुति', 'पवनपुत्र', 'hanuman', 'bajrangbali', 'sankatmochan', 'maruti', 'pavanputra', 'anjaneya'],
    'durga_mata': ['दुर्गा', 'माता रानी', 'अम्बे', 'वैष्णो', 'काली', 'जगदम्बे', 'durga', 'mata rani', 'ambe', 'vaishno devi', 'kali', 'jagadambe', 'navdurga'],
    'ganesh': ['गणेश', 'गणपति', 'विनायक', 'गजानन', 'लंबोदर', 'ganesh', 'ganpati', 'vinayaka', 'gajanand', 'lambodar'],
    'vishnu': ['विष्णु', 'नारायण', 'हरि', 'सत्यनारायण', 'vishnu', 'narayan', 'hari', 'satyanarayan', 'lord vishnu'],
    'lakshmi': ['लक्ष्मी', 'महालक्ष्मी', 'कमला', 'धनलक्ष्मी', 'lakshmi', 'mahalakshmi', 'dhan lakshmi'],
    'saraswati': ['सरस्वती', 'शारदा', 'वीणावादिनी', 'विद्या', 'saraswati', 'sharda', 'veena vadini'],
    'surya': ['सूर्य', 'सूर्यदेव', 'भास्कर', 'आदित्य', 'surya', 'suryadev', 'bhaskar', 'aditya', 'sun god'],
    'shanidev': ['शनि', 'शनिदेव', 'शनिश्चर', 'shani', 'shanidev', 'shanishchar'],
    'khatushyam': ['खाटू श्याम', 'श्याम बाबा', 'हारे का सहारा', 'शीश का दानी', 'khatu shyam', 'shyam baba', 'hare ka sahara', 'lakhdatar'],
    'bhairav': ['भैरव', 'काल भैरव', 'बटुक भैरव', 'bhairav', 'kaal bhairav', 'batuk bhairav'],
    'santoshi': ['संतोषी माता', 'मां संतोषी', 'santoshi mata', 'maa santoshi'],
    'ganga': ['गंगा', 'गंगा मैया', 'भागीरथी', 'ganga', 'ganga maiya', 'bhagirathi'],
    'yamuna': ['यमुना', 'यमुना मैया', 'कालिंदी', 'yamuna', 'yamuna maiya', 'kalindi'],
    'guru_sant': ['गुरु', 'संत', 'साईं बाबा', 'रविदास', 'कबीर', 'तुलसीदास', 'मीरा', 'guru', 'sant', 'sai baba', 'kabir', 'tulsidas', 'meera'],
    'bhajan': ['भजन', 'कीर्तन', 'संकीर्तन', 'गीत', 'bhajan', 'kirtan', 'sankirtan', 'song', 'audio'],
    'aarti': ['आरती', 'मंगला आरती', 'संध्या आरती', 'aarti', 'arti', 'mangala aarti'],
    'chalisa': ['चालीसा', 'chalisa', 'chaalisa'],
    'mantra': ['मंत्र', 'महामंत्र', 'जप', 'mantra', 'mahamantra', 'jaap'],
    'stotram': ['स्तोत्र', 'स्तोत्रम्', 'स्तुति', 'अष्टकम', 'stotra', 'stotram', 'stuti', 'ashtakam'],
    'katha': ['कथा', 'प्रवचन', 'कहानी', 'चरित्र', 'katha', 'pravachan', 'story', 'charitra'],
    'dharmik_gyan': ['ज्ञान', 'धार्मिक ज्ञान', 'उपदेश', 'gyan', 'dharmik gyan', 'updesh', 'wisdom'],
    'satsang': ['सत्संग', 'अमृत वचन', 'satsang', 'amrit vachan'],
    'chetawani_bhajan': ['चेतावनी', 'निर्गुण', 'वैराग्य भजन', 'chetawani', 'nirgun bhajan'],
    'festival_special': ['त्योहार', 'पर्व', 'जयंती', 'festival', 'parva', 'jayanti'],
    'vrat_katha': ['व्रत कथा', 'उपवास', 'एकादशी', 'पूर्णिमा', 'vrat katha', 'upvas', 'ekadashi', 'purnima'],
    'temple_katha': ['मंदिर कथा', 'तीर्थ', 'धाम', 'temple katha', 'teerth', 'dham'],
    'naam_jaap': ['नाम जप', 'राम नाम', 'राधे राधे', 'हरे कृष्ण', 'naam jaap', 'ram naam', 'radhe radhe', 'hare krishna']
}

def normalize_devanagari(text: str) -> str:
    if not text:
        return ""
    text = unicodedata.normalize('NFC', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\u200c', '').replace('\u200d', '')
    return text.strip()

def build_search_tokens(
    title: str,
    title_en: str = None,
    deity_id: str = None,
    content_type: str = None,
    tags: List[str] = None,
    short_desc: str = None
) -> str:
    tokens: Set[str] = set()

    if title:
        norm_t = normalize_devanagari(title)
        tokens.add(norm_t)
        words = re.findall(r'[a-zA-Z0-9\u0900-\u097F]+', norm_t)
        for word in words:
            if len(word) > 1:
                tokens.add(word)

    if title_en:
        norm_en = title_en.lower().strip()
        tokens.add(norm_en)
        for word in re.findall(r'[a-zA-Z0-9]+', norm_en):
            if len(word) > 1:
                tokens.add(word)

    if deity_id and deity_id in BILINGUAL_MAP:
        for syn in BILINGUAL_MAP[deity_id]:
            tokens.add(syn.lower())

    if content_type and content_type in BILINGUAL_MAP:
        for syn in BILINGUAL_MAP[content_type]:
            tokens.add(syn.lower())

    if tags:
        for tag in tags:
            tag_clean = normalize_devanagari(tag).lower()
            tokens.add(tag_clean)

    if short_desc:
        for word in re.findall(r'[a-zA-Z0-9\u0900-\u097F]+', short_desc):
            if len(word) > 2:
                tokens.add(word.lower())

    return " ".join(sorted(tokens))

def build_fts_query(user_query: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z0-9\u0900-\u097F\s]', ' ', user_query).strip()
    if not cleaned:
        return ""

    words = cleaned.split()
    query_parts = []
    
    for w in words:
        w_lower = w.lower()
        expanded_terms = [f'"{w}"*']
        for key, aliases in BILINGUAL_MAP.items():
            if any(w_lower == a.lower() for a in aliases):
                for a in aliases[:4]:
                    expanded_terms.append(f'"{a}"*')
                break
        
        if len(expanded_terms) == 1:
            query_parts.append(expanded_terms[0])
        else:
            query_parts.append(f"({' OR '.join(expanded_terms)})")

    return " AND ".join(query_parts)
