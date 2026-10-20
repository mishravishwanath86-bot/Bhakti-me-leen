import os

left_wing_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 130" fill="none">
  <defs>
    <linearGradient id="goldGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="25%" stop-color="#FDE68A"/>
      <stop offset="60%" stop-color="#F59E0B"/>
      <stop offset="90%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#78350F"/>
    </linearGradient>
    <linearGradient id="goldGrad2" x1="0%" y1="0%" x2="100%" y2="80%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>
    <filter id="goldShadow" x="-20%" y="-20%" width="150%" height="150%">
      <feDropShadow dx="-2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.45"/>
    </filter>
  </defs>
  <g filter="url(#goldShadow)">
    <!-- Top Main Arching Feather -->
    <path d="M95 105 C70 95 40 75 15 45 C5 32 0 18 2 5 C8 15 22 28 42 35 C65 42 85 50 95 58 Z" fill="url(#goldGrad1)" stroke="#FFFBEB" stroke-width="1.2"/>
    <!-- 2nd Feather -->
    <path d="M92 108 C68 98 42 82 22 58 C15 50 12 40 15 32 C18 42 30 52 50 58 C72 65 88 72 95 78 Z" fill="url(#goldGrad2)" stroke="#FDE68A" stroke-width="1"/>
    <!-- 3rd Feather -->
    <path d="M90 112 C68 102 46 88 30 70 C24 64 22 55 26 48 C28 58 40 68 60 74 C78 80 88 88 94 95 Z" fill="url(#goldGrad1)" stroke="#FFFBEB" stroke-width="1"/>
    <!-- 4th Feather -->
    <path d="M88 116 C70 108 52 96 38 82 C34 76 33 68 37 62 C39 70 50 80 68 86 C82 92 90 100 93 108 Z" fill="url(#goldGrad2)" stroke="#FDE68A" stroke-width="1"/>
    <!-- Base Golden Filigree Scroll -->
    <path d="M82 120 C75 118 68 112 65 104 C62 96 68 88 76 86 C84 84 92 90 94 98 C96 106 90 114 82 120 Z" fill="url(#goldGrad1)" stroke="#FDE68A" stroke-width="1.5"/>
    <circle cx="80" cy="102" r="4" fill="#FFFBEB"/>
  </g>
</svg>'''

right_wing_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 130" fill="none">
  <defs>
    <linearGradient id="goldGrad1R" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="25%" stop-color="#FDE68A"/>
      <stop offset="60%" stop-color="#F59E0B"/>
      <stop offset="90%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#78350F"/>
    </linearGradient>
    <linearGradient id="goldGrad2R" x1="100%" y1="0%" x2="0%" y2="80%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>
    <filter id="goldShadowR" x="-20%" y="-20%" width="150%" height="150%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.45"/>
    </filter>
  </defs>
  <g filter="url(#goldShadowR)">
    <!-- Top Main Arching Feather -->
    <path d="M5 105 C30 95 60 75 85 45 C95 32 100 18 98 5 C92 15 78 28 58 35 C35 42 15 50 5 58 Z" fill="url(#goldGrad1R)" stroke="#FFFBEB" stroke-width="1.2"/>
    <!-- 2nd Feather -->
    <path d="M8 108 C32 98 58 82 78 58 C85 50 88 40 85 32 C82 42 70 52 50 58 C28 65 12 72 5 78 Z" fill="url(#goldGrad2R)" stroke="#FDE68A" stroke-width="1"/>
    <!-- 3rd Feather -->
    <path d="M10 112 C32 102 54 88 70 70 C76 64 78 55 74 48 C72 58 60 68 40 74 C22 80 12 88 6 95 Z" fill="url(#goldGrad1R)" stroke="#FFFBEB" stroke-width="1"/>
    <!-- 4th Feather -->
    <path d="M12 116 C30 108 48 96 62 82 C66 76 67 68 63 62 C61 70 50 80 32 86 C18 92 10 100 7 108 Z" fill="url(#goldGrad2R)" stroke="#FDE68A" stroke-width="1"/>
    <!-- Base Golden Filigree Scroll -->
    <path d="M18 120 C25 118 32 112 35 104 C38 96 32 88 24 86 C16 84 8 90 6 98 C4 106 10 114 18 120 Z" fill="url(#goldGrad1R)" stroke="#FDE68A" stroke-width="1.5"/>
    <circle cx="20" cy="102" r="4" fill="#FFFBEB"/>
  </g>
</svg>'''

# Blue Diamond Gem SVG
gem_blue_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" fill="none">
  <defs>
    <linearGradient id="bgem" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0F2FE"/>
      <stop offset="30%" stop-color="#38BDF8"/>
      <stop offset="70%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0369A1"/>
    </linearGradient>
    <filter id="bgemGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#38BDF8" flood-opacity="0.8"/>
    </filter>
  </defs>
  <polygon points="20,2 38,20 20,38 2,20" fill="url(#bgem)" stroke="#FFF" stroke-width="1.2" filter="url(#bgemGlow)"/>
  <polygon points="20,7 33,20 20,33 7,20" fill="#38BDF8" opacity="0.85"/>
  <polygon points="20,11 29,20 20,29 11,20" fill="#BAE6FD" opacity="0.95"/>
  <polygon points="20,14 24,18 20,22 16,18" fill="#FFFFFF"/>
</svg>'''

# Green Diamond Gem SVG
gem_green_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" fill="none">
  <defs>
    <linearGradient id="ggem" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D1FAE5"/>
      <stop offset="30%" stop-color="#34D399"/>
      <stop offset="70%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#064E3B"/>
    </linearGradient>
    <filter id="ggemGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#10B981" flood-opacity="0.8"/>
    </filter>
  </defs>
  <polygon points="20,2 38,20 20,38 2,20" fill="url(#ggem)" stroke="#FFF" stroke-width="1.2" filter="url(#ggemGlow)"/>
  <polygon points="20,7 33,20 20,33 7,20" fill="#10B981" opacity="0.85"/>
  <polygon points="20,11 29,20 20,29 11,20" fill="#A7F3D0" opacity="0.95"/>
  <polygon points="20,14 24,18 20,22 16,18" fill="#FFFFFF"/>
</svg>'''

os.makedirs('assets/games', exist_ok=True)
with open('assets/games/wing_gold_left.svg', 'w', encoding='utf-8') as f:
    f.write(left_wing_svg)
with open('assets/games/wing_gold_right.svg', 'w', encoding='utf-8') as f:
    f.write(right_wing_svg)
with open('assets/games/gem_blue.svg', 'w', encoding='utf-8') as f:
    f.write(gem_blue_svg)
with open('assets/games/gem_green.svg', 'w', encoding='utf-8') as f:
    f.write(gem_green_svg)

print("Generated all vector SVG wings & gems!")
