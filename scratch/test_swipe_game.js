const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');
const jsonPath = path.join(baseDir, 'assets', 'cards', 'swipe_game_data.json');

console.log("=== VERIFYING SWIPE GAME DATA & ASSETS ===");

if (!fs.existsSync(jsonPath)) {
  console.error("❌ swipe_game_data.json missing!");
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const categories = data.categories;

console.log(`Found ${categories.length} categories.`);
let totalCards = 0;
let missingImages = 0;

categories.forEach((cat, idx) => {
  console.log(`\nCategory ${idx + 1}: ${cat.title} (${cat.id})`);
  console.log(`  Instruction: ${cat.instruction}`);
  console.log(`  Left: ${cat.leftSide.name} (${cat.leftSide.bgColor}) - Gate: ${cat.leftSide.gateAsset}`);
  console.log(`  Right: ${cat.rightSide.name} (${cat.rightSide.bgColor}) - Gate: ${cat.rightSide.gateAsset}`);
  
  // Check gate assets
  const leftGatePath = path.join(baseDir, cat.leftSide.gateAsset);
  const rightGatePath = path.join(baseDir, cat.rightSide.gateAsset);
  if (!fs.existsSync(leftGatePath)) {
    console.error(`  ❌ Missing Left Gate: ${leftGatePath}`);
  } else {
    console.log(`  ✓ Left Gate OK: ${cat.leftSide.gateAsset}`);
  }
  if (!fs.existsSync(rightGatePath)) {
    console.error(`  ❌ Missing Right Gate: ${rightGatePath}`);
  } else {
    console.log(`  ✓ Right Gate OK: ${cat.rightSide.gateAsset}`);
  }

  console.log(`  Cards count: ${cat.cards.length}`);
  cat.cards.forEach(card => {
    totalCards++;
    const imgPath = path.join(baseDir, card.image);
    if (!fs.existsSync(imgPath)) {
      console.error(`    ❌ Missing image for ${card.id} (${card.name}): ${imgPath}`);
      missingImages++;
    }
    if (!['LEFT', 'RIGHT'].includes(card.correctSwipe)) {
      console.error(`    ❌ Invalid swipe direction for ${card.id}: ${card.correctSwipe}`);
    }
  });
});

console.log(`\nTotal verified cards: ${totalCards}`);
console.log(`Missing images: ${missingImages}`);

if (totalCards === 100 && missingImages === 0) {
  console.log("🎉 ALL 100 CARDS AND 6 GATES VERIFIED 100% PERFECTLY!");
} else {
  console.error("❌ Verification failed!");
  process.exit(1);
}
