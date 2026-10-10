import shutil, os, time, re, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

src_png = r"C:\Users\vishw\.gemini\antigravity-ide\brain\d4edbe0a-4cba-49d1-897b-87cc2ffb0ce9\.user_uploaded\media_1788295807775.png"

# 1. Save as PNG assets
shutil.copy2(src_png, "assets/app_logo.png")
shutil.copy2(src_png, "assets/app_logo_circle.png")
print("✓ Copied new transparent PNG logo to assets/app_logo.png and assets/app_logo_circle.png")

# 2. Convert to high quality JPG (with nice subtle dark background for fallback)
im = Image.open(src_png).convert("RGBA")

bg = Image.new("RGB", im.size, (26, 7, 48))
bg.paste(im, mask=im.split()[3]) # alpha mask
bg.save("assets/app_logo.jpg", "JPEG", quality=98)
print("✓ Generated high-res assets/app_logo.jpg")

# 3. Create 192x192 and 512x512 PWA icons
icon_192 = im.resize((192, 192), Image.Resampling.LANCZOS)
icon_192.save("assets/icon-192.png", "PNG")

icon_512 = im.resize((512, 512), Image.Resampling.LANCZOS)
icon_512.save("assets/icon-512.png", "PNG")
print("✓ Generated PWA icons 192x192 and 512x512")

# 4. Update index.html logo references
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

ts = int(time.time())

html = re.sub(r'assets/app_logo\.(jpg|png)(\?v=\d+)?', f'assets/app_logo.png?v={ts}', html)
html = re.sub(r'assets/app_logo_circle\.png(\?v=\d+)?', f'assets/app_logo_circle.png?v={ts}', html)

# Header Logo styling adjustment for transparent wing logo
if 'filter:drop-shadow(0 0 8px rgba(248,200,59,0.6))' not in html:
    html = html.replace(
        'class="header-logo" />',
        'class="header-logo" style="width:38px; height:38px; object-fit:contain; filter:drop-shadow(0 0 8px rgba(248,200,59,0.6));" />'
    )
    html = html.replace(
        'class="drawer-logo" />',
        'class="drawer-logo" style="width:55px; height:55px; object-fit:contain; filter:drop-shadow(0 0 12px rgba(248,200,59,0.7));" />'
    )
    html = html.replace(
        'class="splash-logo" />',
        'class="splash-logo" style="width:130px; height:130px; object-fit:contain; filter:drop-shadow(0 0 25px rgba(248,200,59,0.85));" />'
    )

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✓ index.html updated with new logo & luxury styling (v={ts})")
