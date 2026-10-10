def calcCurvedPath(cx):
    CORNER_R = 36
    SCOOP_HALF_W = 66
    DEPTH = 74
    SHOULDER_W = 28
    VIEW_W = 1000
    VIEW_H = 160
    
    p1x = cx - SCOOP_HALF_W
    p2x = cx + SCOOP_HALF_W
    return (
        f"M 0,{CORNER_R} "
        f"A {CORNER_R},{CORNER_R} 0 0 1 {CORNER_R},0 "
        f"L {p1x:.1f},0 "
        f"C {p1x + SHOULDER_W:.1f},0 {cx - 36:.1f},{DEPTH} {cx:.1f},{DEPTH} "
        f"C {cx + 36:.1f},{DEPTH} {p2x - SHOULDER_W:.1f},0 {p2x:.1f},0 "
        f"L {VIEW_W - CORNER_R},0 "
        f"A {CORNER_R},{CORNER_R} 0 0 1 {VIEW_W},{CORNER_R} "
        f"L {VIEW_W},{VIEW_H - CORNER_R} "
        f"A {CORNER_R},{CORNER_R} 0 0 1 {VIEW_W - CORNER_R},{VIEW_H} "
        f"L {CORNER_R},{VIEW_H} "
        f"A {CORNER_R},{CORNER_R} 0 0 1 0,{VIEW_H - CORNER_R} "
        f"Z"
    )

d = calcCurvedPath(100)
print(d)

# Let's save a standalone SVG file to see what it actually draws!
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 160" width="1000" height="160">
  <path d="{d}" fill="#18181D" stroke="red" stroke-width="2"/>
  <circle cx="100" cy="50" r="60" fill="green"/>
</svg>'''

with open('debug_svg.svg', 'w') as f:
    f.write(svg_content)
print("Saved debug_svg.svg")
