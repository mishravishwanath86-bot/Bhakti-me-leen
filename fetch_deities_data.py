import urllib.request
import re
import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

pages = [
    {
        "id": "bhairava-ravivara",
        "dayEn": "Sunday",
        "dayHi": "रविवार",
        "dayNum": 0,
        "nameEn": "Bhairava Ravivara Vrat",
        "nameHi": "भैरव रविवार व्रत",
        "deityEn": "Lord Bhairava",
        "deityHi": "भगवान कालभैरव",
        "image": "/deities/bhairava.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/gods/kalabhairava/720x480/xkalabhairava.jpg.pagespeed.ic.pAuzQ3kkZ1.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/ravivara/bhairava-ravivara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/ravivara/bhairava-ravivara-vrat.html?lang=hi"
    },
    {
        "id": "shiva-somavara",
        "dayEn": "Monday",
        "dayHi": "सोमवार",
        "dayNum": 1,
        "nameEn": "Shiva Somavara Vrat",
        "nameHi": "शिव सोमवार व्रत",
        "deityEn": "Lord Shiva",
        "deityHi": "भगवान शिव",
        "image": "/deities/shiva.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/gods/shiva/2x/lord_shiva_with_parvati_ganesha_kartikeya.jpg.pagespeed.ce.SN1vrbC2TE.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/somavara/shiva-somavara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/somavara/shiva-somavara-vrat.html?lang=hi"
    },
    {
        "id": "hanumana-mangalavara",
        "dayEn": "Tuesday",
        "dayHi": "मङ्गलवार",
        "dayNum": 2,
        "nameEn": "Hanumana Mangalavara Vrat",
        "nameHi": "हनुमान मङ्गलवार व्रत",
        "deityEn": "Lord Hanuman",
        "deityHi": "भगवान हनुमान",
        "image": "/deities/hanuman.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/gods/hanuman/720x480/xlord_hanuman_twilight_silhouette_mountain.jpg.pagespeed.ic.7A1SdZXSpU.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/mangalavara/hanumana-mangalavara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/mangalavara/hanumana-mangalavara-vrat.html?lang=hi"
    },
    {
        "id": "murugan-mangalavara",
        "dayEn": "Tuesday",
        "dayHi": "मङ्गलवार",
        "dayNum": 2,
        "nameEn": "Murugan Mangalavara Vrat",
        "nameHi": "मुरुगन मङ्गलवार व्रत",
        "deityEn": "Lord Murugan (Kartikeya)",
        "deityHi": "भगवान मुरुगन (कार्तिकेय)",
        "image": "/deities/murugan.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/gods/murugan/2x/murugan_peacock.jpg.pagespeed.ce.el8fSqANnE.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/mangalavara/murugana-mangalavara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/mangalavara/murugana-mangalavara-vrat.html?lang=hi"
    },
    {
        "id": "ganesha-budhavara",
        "dayEn": "Wednesday",
        "dayHi": "बुधवार",
        "dayNum": 3,
        "nameEn": "Ganesha Budhavara Vrat",
        "nameHi": "गणेश बुधवार व्रत",
        "deityEn": "Lord Ganesha",
        "deityHi": "भगवान गणेश",
        "image": "/deities/ganesha.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/gods/ganesha/2x/lord_ganesha_with_riddhi_siddhi.jpg.pagespeed.ce.h59wjv_ltE.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/budhavara/ganesha-budhavara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/budhavara/ganesha-budhavara-vrat.html?lang=hi"
    },
    {
        "id": "vishnu-brihaspativara",
        "dayEn": "Thursday",
        "dayHi": "बृहस्पतिवार",
        "dayNum": 4,
        "nameEn": "Vishnu Brihaspativara Vrat",
        "nameHi": "विष्णु बृहस्पतिवार व्रत",
        "deityEn": "Lord Vishnu",
        "deityHi": "भगवान विष्णु",
        "image": "/deities/vishnu.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/gods/dashavatara/lord-vishnu/720x480/lord_vishnu_with_goddess_lakshmi.jpg.pagespeed.ce.s9J2bhdzV8.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/brihaspativara/vishnu-brihaspativara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/brihaspativara/vishnu-brihaspativara-vrat.html?lang=hi"
    },
    {
        "id": "santoshi-mata-shukravara",
        "dayEn": "Friday",
        "dayHi": "शुक्रवार",
        "dayNum": 5,
        "nameEn": "Santoshi Mata Shukravara Vrat",
        "nameHi": "सन्तोषी माता शुक्रवार व्रत",
        "deityEn": "Goddess Santoshi Mata",
        "deityHi": "माँ सन्तोषी",
        "image": "/deities/santoshi.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/goddesses/santoshi/720x480/goddess_santoshi_mata.jpg.pagespeed.ce.8_WDiDwa5z.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/shukravara/santoshi-mata-shukravara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/shukravara/santoshi-mata-shukravara-vrat.html?lang=hi"
    },
    {
        "id": "vaibhava-lakshmi-shukravara",
        "dayEn": "Friday",
        "dayHi": "शुक्रवार",
        "dayNum": 5,
        "nameEn": "Vaibhava Lakshmi Shukravara Vrat",
        "nameHi": "वैभव लक्ष्मी शुक्रवार व्रत",
        "deityEn": "Goddess Vaibhava Lakshmi",
        "deityHi": "माँ वैभव लक्ष्मी",
        "image": "/deities/lakshmi.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/goddesses/vaibhava-lakshmi/720x480/goddess_vaibhava_lakshmi.jpg.pagespeed.ce.t9bLmYp0Om.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/shukravara/vaibhava-lakshmi-shukravara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/shukravara/vaibhava-lakshmi-shukravara-vrat.html?lang=hi"
    },
    {
        "id": "maa-kali-shanivara",
        "dayEn": "Saturday",
        "dayHi": "शनिवार",
        "dayNum": 6,
        "nameEn": "Maa Kali Shanivara Vrat",
        "nameHi": "माँ काली शनिवार व्रत",
        "deityEn": "Goddess Kali",
        "deityHi": "माँ काली",
        "image": "/deities/kali.jpg",
        "fallbackImage": "https://www.drikpanchang.com/images/goddesses/parvati/dasha-mahavidya/720x480/goddess_kali.jpg.pagespeed.ce.JG8vAC9the.jpg",
        "urlEn": "https://www.drikpanchang.com/vrats/weekdays/shanivara/maa-kali-shanivara-vrat.html",
        "urlHi": "https://www.drikpanchang.com/vrats/weekdays/shanivara/maa-kali-shanivara-vrat.html?lang=hi"
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def clean_html(html_str):
    if not html_str:
        return ""
    text = re.sub(r'<script.*?</script>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</li>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&quot;', '"', text)
    text = re.sub(r'&#39;', "'", text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_sections(html):
    sections = {}
    if not html:
        return sections
    
    # Extract dpPageShortTitle or dpPageTitle
    title_m = re.search(r'<h1 class="dpPageTitle"[^>]*>(.*?)</h1>', html, re.DOTALL)
    if title_m:
        sections['pageTitle'] = clean_html(title_m.group(1))

    # Extract all h2 / h3 headings and following content
    # Find all headings with classes like dpContentTitle, dpMiddleTitle, etc.
    heading_matches = list(re.finditer(r'<h[234]\s+class="([^"]*)"[^>]*>(.*?)</h[234]>', html, re.DOTALL))
    
    for i, hm in enumerate(heading_matches):
        h_class = hm.group(1)
        h_text = clean_html(hm.group(2))
        start_pos = hm.end()
        end_pos = heading_matches[i+1].start() if i+1 < len(heading_matches) else len(html)
        content_chunk = html[start_pos:end_pos]
        # remove ad sections, comments, footers
        content_chunk = re.sub(r'<div class="dpAdSection.*?</div>', '', content_chunk, flags=re.DOTALL)
        content_chunk = re.sub(r'<div class="dpCommentContainer.*?</div>', '', content_chunk, flags=re.DOTALL)
        clean_text = clean_html(content_chunk)
        if len(clean_text) > 10 and not h_text.startswith("टिप्पणी") and not h_text.startswith("Comment") and not h_text.startswith("Other Pages"):
            sections[h_text] = clean_text

    return sections

results = []
for p in pages:
    print(f"Fetching {p['nameEn']}...")
    html_en = fetch_url(p['urlEn'])
    time.sleep(0.5)
    html_hi = fetch_url(p['urlHi'])
    time.sleep(0.5)
    
    sec_en = extract_sections(html_en)
    sec_hi = extract_sections(html_hi)
    
    entry = {
        **p,
        "sectionsEn": sec_en,
        "sectionsHi": sec_hi
    }
    results.append(entry)
    print(f"  Done: {len(sec_en)} EN sections, {len(sec_hi)} HI sections")

out_file = r'c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\deities_saptavara_full.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nAll saved to {out_file}!")
