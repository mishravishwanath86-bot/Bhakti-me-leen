const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

// Wipe out ALL old vrat-icon-img and vrat-icon CSS to start fresh and clean
css = css.replace(/\.vrat-card > div:first-child[\s\S]*?transition: all 0\.3s ease;\n\}/g, '');
css = css.replace(/\.vrat-card:active > div:first-child[\s\S]*?rgba\(245, 158, 11, 0\.5\);\n\}/g, '');
css = css.replace(/\.vrat-icon-img[\s\S]*?display: block;\n\}/g, '');

// The old old ones
css = css.replace(/\.vrat-icon-img \{[\s\S]*?box-shadow: 0 8px 16px rgba\(180, 83, 9, 0\.25\), 0 0 10px rgba\(245, 158, 11, 0\.4\);\n\}/g, '');
css = css.replace(/\.vrat-card:active \.vrat-icon-img, \n\.vrat-card:hover \.vrat-icon-img \{[\s\S]*?transition: all 0\.3s ease;\n\}/g, '');
css = css.replace(/\.vrat-icon-img \{[\s\S]*?transition: all 0\.3s ease;\n\}/g, '');
css = css.replace(/\.vrat-icon \{[\s\S]*?filter: drop-shadow\(0 2px 3px rgba\(0,0,0,0\.2\)\);\n\}/g, '');
css = css.replace(/\/\* NEW CENTERING FIX \*\/[\s\S]*?rgba\(245, 158, 11, 0\.5\);\n\}/g, '');

// Append clean unified styles
css += `
/* ------------------------------------- */
/* CLEAN VRAT ICON CENTERING FIX */
/* ------------------------------------- */
.vrat-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  text-align: center;
  padding: 0.8rem 0.2rem 0.5rem;
}

.vrat-icon-wrapper {
  width: 68px !important;
  height: 68px !important;
  border-radius: 50% !important;
  background: #fff !important;
  border: 3px solid #f59e0b !important;
  box-shadow: 0 0 0 2px #fff, 0 4px 10px rgba(245,158,11,0.4) !important; /* Double border effect */
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 0.6rem auto !important;
  transition: all 0.3s ease !important;
  padding: 0 !important;
  overflow: hidden !important; /* Ensure image doesn't bleed */
}

.vrat-icon-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  border-radius: 50% !important;
  margin: 0 !important;
  padding: 2px !important; /* Tiny gap inside the ring */
  background: #fff !important;
  border: none !important;
  display: block !important;
}

.vrat-icon {
  font-size: 2.2rem !important;
  line-height: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.vrat-card:hover .vrat-icon-wrapper,
.vrat-card:active .vrat-icon-wrapper {
  transform: scale(1.08) !important;
  box-shadow: 0 0 0 2px #fff, 0 8px 16px rgba(245,158,11,0.6) !important;
}
`;

fs.writeFileSync('styles.css', css, 'utf8');
console.log("CSS completely rewritten for vrat icons.");
