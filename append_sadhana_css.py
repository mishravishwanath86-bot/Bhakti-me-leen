import sys

sys.stdout.reconfigure(encoding='utf-8')

extra_css = """

/* ══════════════════════════════════════════════════════════════════════════════
   🛡️ SADHANA STREAK SHIELD & SANGHA MANDAL MICRO-ANIMATIONS 🛡️
   ══════════════════════════════════════════════════════════════════════════════ */

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(18px) scale(0.98);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes shieldPulse {
  0%, 100% {
    box-shadow: 0 0 10px rgba(245, 158, 11, 0.4), inset 0 0 10px rgba(245, 158, 11, 0.2);
  }
  50% {
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.8), inset 0 0 15px rgba(245, 158, 11, 0.4);
  }
}

.shield-pulse-active {
  animation: shieldPulse 2.5s infinite ease-in-out;
}

#sadhana-streak-shield-vault button:active,
#sadhana-collective-sangha-card button:active {
  transform: scale(0.97);
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(extra_css)

print("✓ Successfully appended sadhana gamification CSS to styles.css")
