import os
import sys
import math
from PIL import Image, ImageDraw, ImageFilter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
GATES_DIR = os.path.join(BASE_DIR, "assets", "gates")
os.makedirs(GATES_DIR, exist_ok=True)

GATES = [
    {
        "filename": "gate_ayodhya.png",
        "name": "अयोध्या द्वार",
        "primary": (107, 33, 168),     # #6B21A8 Purple
        "secondary": (245, 158, 11),   # Gold
        "glow": (253, 230, 138),
        "symbol": "सूर्य",
        "decor": "सूर्यवंशी तोरण"
    },
    {
        "filename": "gate_mithila.png",
        "name": "मिथिला द्वार",
        "primary": (220, 38, 38),     # #DC2626 Crimson
        "secondary": (251, 191, 36),   # Amber/Gold
        "glow": (254, 226, 226),
        "symbol": "कमल",
        "decor": "वैदेही तोरण"
    },
    {
        "filename": "gate_ram_sena.png",
        "name": "श्रीराम सेना द्वार",
        "primary": (234, 88, 12),     # #EA580C Saffron Orange
        "secondary": (254, 240, 138),  # Warm Gold
        "glow": (255, 237, 213),
        "symbol": "धनुष",
        "decor": "विजयी ध्वज"
    },
    {
        "filename": "gate_ravan_sena.png",
        "name": "रावण सेना द्वार",
        "primary": (127, 29, 29),     # #7F1D1D Deep Red
        "secondary": (217, 119, 6),    # Bronze Gold
        "glow": (254, 202, 202),
        "symbol": "खड्ग",
        "decor": "स्वर्ण लंका दुर्ग"
    },
    {
        "filename": "gate_pandav.png",
        "name": "पाण्डव द्वार",
        "primary": (21, 128, 61),      # #15803D Forest Green
        "secondary": (250, 204, 21),   # Pure Gold
        "glow": (220, 252, 231),
        "symbol": "शंख",
        "decor": "इंद्रप्रस्थ तोरण"
    },
    {
        "filename": "gate_kaurav.png",
        "name": "कौरव द्वार",
        "primary": (153, 27, 27),     # #991B1B Royal Red
        "secondary": (234, 179, 8),    # Royal Gold
        "glow": (254, 226, 226),
        "symbol": "गदा",
        "decor": "हस्तिनापुर द्वार"
    }
]

def draw_temple_gate(info):
    W, H = 400, 480
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    p_col = info["primary"] + (255,)
    s_col = info["secondary"] + (255,)
    glow_col = info["glow"] + (180,)
    gold = (245, 158, 11, 255)
    dark_gold = (180, 115, 10, 255)
    light_gold = (254, 240, 138, 255)

    # 1. Subtle glowing arch background in gate opening
    center_x = W // 2
    inner_w, inner_h = 160, 260
    opening_rect = [center_x - inner_w//2, H - inner_h - 40, center_x + inner_w//2, H - 40]
    
    # Inner gate gradient/halo
    for r in range(40, 0, -2):
        alpha = int(120 * (1 - r/40))
        glow_draw = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d_glow = ImageDraw.Draw(glow_draw)
        d_glow.ellipse([center_x - inner_w//2 - r, H - inner_h - 40 - r, center_x + inner_w//2 + r, H - 40 + r],
                       fill=info["primary"] + (alpha,))
        im = Image.alpha_composite(im, glow_draw)
        draw = ImageDraw.Draw(im)

    # Portal opening portal door (dark arched gate opening)
    # Portal inner arched path
    draw.chord([center_x - inner_w//2, H - inner_h - 60, center_x + inner_w//2, H - inner_h + 100], 180, 360, fill=(15, 7, 28, 240))
    draw.rectangle([center_x - inner_w//2, H - inner_h + 20, center_x + inner_w//2, H - 40], fill=(15, 7, 28, 240))

    # Inner decorative mystical rays
    for angle in range(200, 345, 18):
        rad = math.radians(angle)
        ex = center_x + math.cos(rad) * 110
        ey = (H - inner_h + 40) + math.sin(rad) * 90
        draw.line([center_x, H - inner_h + 40, ex, ey], fill=light_gold[:3] + (50,), width=2)

    # 2. Left & Right Heavy Vedic Pillars
    pillar_w = 46
    p_left_x = center_x - inner_w//2 - pillar_w
    p_right_x = center_x + inner_w//2
    p_top_y = H - inner_h - 10
    p_bot_y = H - 35

    for px in [p_left_x, p_right_x]:
        # Pillar Base (Plinth)
        draw.rectangle([px - 6, p_bot_y - 20, px + pillar_w + 6, p_bot_y], fill=dark_gold)
        draw.rectangle([px - 3, p_bot_y - 35, px + pillar_w + 3, p_bot_y - 20], fill=gold)
        draw.rectangle([px, p_bot_y - 45, px + pillar_w, p_bot_y - 35], fill=p_col)

        # Main Shaft
        draw.rectangle([px + 3, p_top_y + 35, px + pillar_w - 3, p_bot_y - 45], fill=p_col)
        # Vertical fluting/grooves
        for gx in range(px + 9, px + pillar_w - 6, 8):
            draw.line([gx, p_top_y + 40, gx, p_bot_y - 50], fill=s_col, width=2)
            draw.line([gx + 2, p_top_y + 40, gx + 2, p_bot_y - 50], fill=light_gold, width=1)

        # Pillar Capital (Top ornate bracket)
        draw.rectangle([px, p_top_y + 20, px + pillar_w, p_top_y + 35], fill=dark_gold)
        draw.rectangle([px - 5, p_top_y + 8, px + pillar_w + 5, p_top_y + 20], fill=gold)
        draw.rectangle([px - 10, p_top_y - 5, px + pillar_w + 10, p_top_y + 8], fill=s_col)

        # Hanging bell / kalash
        bx = px + pillar_w // 2
        draw.line([bx, p_top_y + 8, bx, p_top_y + 35], fill=gold, width=2)
        draw.ellipse([bx - 6, p_top_y + 28, bx + 6, p_top_y + 42], fill=light_gold, outline=dark_gold)

    # 3. Grand Ornate Arch (Torang / Shikhara / Dome)
    arch_cx = center_x
    arch_cy = H - inner_h + 15
    outer_rx = inner_w // 2 + pillar_w + 12
    outer_ry = 120

    # Multi-layered ornate concentric arch rings
    for dr in [0, -8, -16, -24]:
        fill_c = s_col if dr in [0, -16] else p_col
        draw.arc([arch_cx - outer_rx - dr, arch_cy - outer_ry - dr, arch_cx + outer_rx + dr, arch_cy + outer_ry + dr],
                 start=180, end=360, fill=fill_c, width=7)

    # Arch decorative floral cusps (pointed arch peaks)
    cusp_points = []
    for deg in range(180, 365, 15):
        rad = math.radians(deg)
        r_dist = outer_rx + 8 + (6 if (deg // 15) % 2 == 0 else 0)
        cx = arch_cx + math.cos(rad) * r_dist
        cy = arch_cy + math.sin(rad) * (outer_ry + 10)
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=light_gold, outline=dark_gold)

    # 4. Apex Kalash / Mandir Shikhara Crown
    crest_y = arch_cy - outer_ry - 35
    # Shikhara tiers
    draw.polygon([
        (arch_cx - 36, crest_y + 25),
        (arch_cx + 36, crest_y + 25),
        (arch_cx + 20, crest_y),
        (arch_cx - 20, crest_y)
    ], fill=p_col, outline=gold)

    draw.polygon([
        (arch_cx - 22, crest_y),
        (arch_cx + 22, crest_y),
        (arch_cx + 8, crest_y - 25),
        (arch_cx - 8, crest_y - 25)
    ], fill=s_col, outline=dark_gold)

    # Golden Amrit Kalash atop
    kalash_y = crest_y - 42
    draw.ellipse([arch_cx - 12, kalash_y, arch_cx + 12, kalash_y + 20], fill=gold, outline=light_gold)
    draw.polygon([
        (arch_cx, kalash_y - 18),
        (arch_cx - 8, kalash_y + 2),
        (arch_cx + 8, kalash_y + 2)
    ], fill=light_gold, outline=dark_gold)

    # Celestial Dhwaja (Flag) flying
    draw.line([arch_cx + 2, kalash_y - 30, arch_cx + 2, kalash_y], fill=dark_gold, width=2)
    draw.polygon([
        (arch_cx + 2, kalash_y - 30),
        (arch_cx + 32, kalash_y - 22),
        (arch_cx + 2, kalash_y - 14)
    ], fill=s_col, outline=gold)

    # Left & Right Pinnacle Mini Kalash atop pillars
    for px in [p_left_x, p_right_x]:
        bx = px + pillar_w // 2
        draw.polygon([(bx - 12, p_top_y - 5), (bx + 12, p_top_y - 5), (bx, p_top_y - 28)], fill=s_col, outline=gold)
        draw.ellipse([bx - 5, p_top_y - 35, bx + 5, p_top_y - 25], fill=light_gold, outline=dark_gold)

    # 5. Arch Crest Emblem Medallion in center
    med_y = arch_cy - 45
    draw.ellipse([arch_cx - 28, med_y - 28, arch_cx + 28, med_y + 28], fill=p_col, outline=gold, width=3)
    draw.ellipse([arch_cx - 22, med_y - 22, arch_cx + 22, med_y + 22], fill=(26, 11, 46, 255), outline=light_gold, width=2)
    # Divine rays inside medallion
    for deg in range(0, 360, 45):
        rad = math.radians(deg)
        x1 = arch_cx + math.cos(rad) * 4
        y1 = med_y + math.sin(rad) * 4
        x2 = arch_cx + math.cos(rad) * 16
        y2 = med_y + math.sin(rad) * 16
        draw.line([x1, y1, x2, y2], fill=light_gold, width=2)

    # 6. Smooth anti-aliased glow filter
    glow = im.filter(ImageFilter.GaussianBlur(radius=1.2))
    final = Image.alpha_composite(glow, im)

    out_path = os.path.join(GATES_DIR, info["filename"])
    final.save(out_path, "PNG", optimize=True)
    print(f"✓ Generated sacred gate: {info['filename']} ({info['name']})")

print("Generating 6 Divine Gates...")
for g in GATES:
    draw_temple_gate(g)
print("All 6 Gates successfully generated in assets/gates/!")
