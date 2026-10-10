VIEW_W = 1000
VIEW_H = 160
MARGIN_X = 60
USABLE_W = VIEW_W - 2 * MARGIN_X # 880
TOTAL_TABS = 5
TAB_W = USABLE_W / TOTAL_TABS # 176
CORNER_R = 36

# Deep, wide, unmistakable scoop curve
SCOOP_HALF_W = 76
DEPTH = 94
SHOULDER_W = 32

def get_path(idx):
    cx = MARGIN_X + (idx + 0.5) * TAB_W
    left_x = cx - SCOOP_HALF_W
    right_x = cx + SCOOP_HALF_W
    
    return (
        f"M 0,{CORNER_R} "
        f"A {CORNER_R},{CORNER_R} 0 0 1 {CORNER_R},0 "
        f"L {left_x:.1f},0 "
        f"C {(left_x + SHOULDER_W):.1f},0 {(cx - 44):.1f},{DEPTH} {cx:.1f},{DEPTH} "
        f"C {(cx + 44):.1f},{DEPTH} {(right_x - SHOULDER_W):.1f},0 {right_x:.1f},0 "
        f"L {VIEW_W - CORNER_R},0 "
        f"A {CORNER_R},{CORNER_R} 0 0 1 {VIEW_W},{CORNER_R} "
        f"L {VIEW_W},{VIEW_H - CORNER_R} "
        f"A {CORNER_R},{CORNER_R} 0 0 1 {VIEW_W - CORNER_R},{VIEW_H} "
        f"L {CORNER_R},{VIEW_H} "
        f"A {CORNER_R},{CORNER_R} 0 0 1 0,{VIEW_H - CORNER_R} "
        f"Z"
    )

for i in range(5):
    cx = MARGIN_X + (i + 0.5) * TAB_W
    p = get_path(i)
    bubble_x_percent = (cx / VIEW_W) * 100
    print(f"Tab {i}: cx={cx:.1f}, bubble={bubble_x_percent:.1f}%, path_len={len(p)}")
    
# Generate an SVG file for Tab 0 (Home) to inspect
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 160" width="500" height="80">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a2040"/>
      <stop offset="100%" stop-color="#140e24"/>
    </linearGradient>
  </defs>
  <path d="{get_path(0)}" fill="url(#g)" stroke="#ffffff" stroke-width="2"/>
  <circle cx="{MARGIN_X + 0.5 * TAB_W}" cy="40" r="42" fill="#22c55e"/>
</svg>'''

with open('preview_tab0.svg', 'w') as f:
    f.write(svg)
print("Saved preview_tab0.svg")
