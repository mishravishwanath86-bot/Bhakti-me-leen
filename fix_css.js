const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

// Append correct CSS for centering
css += `
/* NEW CENTERING FIX */
.vrat-icon-wrapper {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  background: linear-gradient(#fff, #fff) padding-box,
              linear-gradient(135deg, #fde047 0%, #f59e0b 50%, #b45309 100%) border-box;
  border: 4px solid transparent;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 0.6rem auto;
  transition: all 0.3s ease;
  padding: 0 !important;
}

.vrat-icon-wrapper .vrat-icon-img {
  width: 58px !important;
  height: 58px !important;
  object-fit: cover !important;
  border-radius: 50% !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  background: none !important;
  box-shadow: none !important;
}

.vrat-icon-wrapper .vrat-icon {
  font-size: 2.5rem !important;
  margin: 0 !important;
  padding: 0 !important;
  line-height: 1 !important;
}

.vrat-card:hover .vrat-icon-wrapper,
.vrat-card:active .vrat-icon-wrapper {
  transform: scale(1.08);
  box-shadow: 0 10px 18px rgba(180, 83, 9, 0.35), 0 0 15px rgba(245, 158, 11, 0.5);
}
`;

fs.writeFileSync('styles.css', css, 'utf8');
console.log("Appended .vrat-icon-wrapper CSS.");
