tile_css = """
/* ── Additional Styles for Match & JigSaw Tiles ── */
.match-tile {
  aspect-ratio: 1 / 1;
  perspective: 600px;
  cursor: pointer;
}

.match-tile-inner {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.4s ease;
  border-radius: 14px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

.match-tile.flipped .match-tile-inner,
.match-tile.matched .match-tile-inner {
  transform: rotateY(180deg);
}

.match-tile-back, .match-tile-front {
  position: absolute;
  inset: 0;
  border-radius: 14px;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.match-tile-back {
  background: linear-gradient(135deg, #4A154B 0%, #2D104E 100%);
  border: 1.5px solid #FCD34D;
  font-size: 1.6rem;
}

.match-tile-front {
  background: #FFFBEB;
  border: 2px solid #F59E0B;
  transform: rotateY(180deg);
}

.match-tile.matched .match-tile-front {
  background: #D1FAE5;
  border-color: #10B981;
}

.jigsaw-tile {
  background: linear-gradient(135deg, #1E1B4B 0%, #312E81 100%);
  border: 2px solid #F59E0B;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  transition: transform 0.15s ease;
  user-select: none;
}

.jigsaw-tile:hover {
  transform: scale(1.04);
}

.jigsaw-tile.empty-slot {
  background: transparent;
  border: 2px dashed rgba(245, 158, 11, 0.3);
  box-shadow: none;
  cursor: default;
}
"""

with open('epic_games.css', 'a', encoding='utf-8') as f:
    f.write(tile_css)

print("Appended tile CSS to epic_games.css!")
