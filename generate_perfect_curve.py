def make_smooth_scoop(cx, view_w=1000, view_h=160, corner_r=36, scoop_w=88, depth=115):
    p1 = cx - scoop_w
    p2 = cx + scoop_w
    
    cp1_x = cx - scoop_w + 35  # cx - 53
    cp2_x = cx - 36
    
    cp3_x = cx + 36
    cp4_x = cx + scoop_w - 35  # cx + 53
    
    return (
        f"M 0,{corner_r} "
        f"A {corner_r},{corner_r} 0 0 1 {corner_r},0 "
        f"L {p1:.1f},0 "
        f"C {cp1_x:.1f},0 {cp2_x:.1f},{depth} {cx:.1f},{depth} "
        f"C {cp3_x:.1f},{depth} {cp4_x:.1f},0 {p2:.1f},0 "
        f"L {view_w - corner_r},0 "
        f"A {corner_r},{corner_r} 0 0 1 {view_w},{corner_r} "
        f"L {view_w},{view_h - corner_r} "
        f"A {corner_r},{corner_r} 0 0 1 {view_w - corner_r},{view_h} "
        f"L {corner_r},{view_h} "
        f"A {corner_r},{corner_r} 0 0 1 0,{view_h - corner_r} "
        f"Z"
    )

cx = 160.0
path = make_smooth_scoop(cx)
print(path)

# Let's save a clear visual test file
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 160" width="800" height="128" style="background:#581c87; padding:20px;">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="rgba(30, 20, 50, 0.75)"/>
      <stop offset="100%" stop-color="rgba(12, 8, 22, 0.92)"/>
    </linearGradient>
  </defs>
  <!-- Background bar -->
  <path d="{path}" fill="url(#g)" stroke="rgba(255,255,255,0.4)" stroke-width="3"/>
  <!-- Active circle -->
  <circle cx="{cx}" cy="46" r="50" fill="#22c55e" stroke="rgba(255,255,255,0.3)" stroke-width="2"/>
  <!-- Other tab indicator dots -->
  <circle cx="330" cy="80" r="14" fill="#a1a1aa"/>
  <circle cx="500" cy="80" r="14" fill="#a1a1aa"/>
  <circle cx="670" cy="80" r="14" fill="#a1a1aa"/>
  <circle cx="840" cy="80" r="14" fill="#a1a1aa"/>
</svg>'''

with open('perfect_curve_demo.svg', 'w') as f:
    f.write(svg)
print("Saved perfect_curve_demo.svg")
