import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFYING EPIC GAMES IMPLEMENTATION ===")

# 1. Check game assets
assets_to_check = [
    "assets/games/bg_vedic_temple.jpg",
    "assets/games/cover_match.jpg",
    "assets/games/cover_swipe.jpg",
    "assets/games/cover_jigsaw.jpg",
    "assets/games/cover_padabandham.jpg",
    "assets/games/portal_ayodhya.jpg",
    "assets/games/portal_mithila.jpg",
    "assets/games/char_sunaina.jpg",
    "assets/games/char_janak.jpg",
    "assets/games/char_manthara.jpg",
    "assets/games/char_sita.jpg",
    "assets/games/char_shatrughna.jpg",
    "assets/games/char_urmila.jpg",
    "assets/games/card_kaikeyi.jpg",
    "assets/games/avatar_janak.jpg",
    "assets/games/avatar_manthara.jpg",
    "assets/games/avatar_sita.jpg",
    "assets/games/avatar_urmila.jpg",
    "assets/games/avatar_kaushalya.jpg",
    "assets/games/avatar_sumitra.jpg",
    "assets/games/avatar_mandavi.jpg",
    "assets/games/avatar_shrutakirti.jpg",
    "assets/games/avatar_kushadhwaja.jpg"
]

all_assets_ok = True
for a in assets_to_check:
    if os.path.exists(a):
        print(f"  [OK] Asset found: {a} ({os.path.getsize(a)} bytes)")
    else:
        print(f"  [MISSING] Asset: {a}")
        all_assets_ok = False

# 2. Check HTML integration
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

required_elements = [
    ('epic_games.css link', 'href="epic_games.css"'),
    ('epic_games_engine.js script', 'src="epic_games_engine.js"'),
    ('Home banner', 'home-epic-games-banner'),
    ('Epic Games Hub Section', 'id="page-epic-games"'),
    ('Swipe Arena', 'id="swipe-arena"'),
    ('Swipe Review Screen', 'id="swipe-review-arena"'),
    ('Swipe Result Modal', 'id="swipe-result-modal"'),
    ('Match Modal', 'id="match-game-modal"'),
    ('Jigsaw Modal', 'id="jigsaw-game-modal"'),
    ('PadaBandham Modal', 'id="padabandham-game-modal"')
]

all_html_ok = True
for name, tag in required_elements:
    if tag in html:
        print(f"  [OK] HTML element: {name}")
    else:
        print(f"  [MISSING] HTML element: {name}")
        all_html_ok = False

print("\nAsset Verification Status:", "PASS" if all_assets_ok else "FAIL")
print("HTML Verification Status:", "PASS" if all_html_ok else "FAIL")
