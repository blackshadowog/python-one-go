/**
 * CELEBRATE OVERLAY — Confetti & Joy
 * Shows a celebration overlay with animated confetti.
 */

const Celebrate = (() => {

  const CONFETTI_COLORS = [
    '#ef4444','#f59e0b','#10b981','#3b82f6',
    '#8b5cf6','#ec4899','#f97316','#06b6d4',
    '#fbbf24','#a3e635'
  ];

  const MESSAGES = [
    "You're doing amazing! 🌟",
    "What a superstar! ⭐",
    "You make us so proud! 💖",
    "Brilliant! Keep going! 🎊",
    "You are wonderful! 🌸",
    "Today was a great day! 🎉",
  ];

  function open() {
    Core.showOverlay('celebrate');
    spawnConfetti();
    const msg = document.getElementById('celebrate-msg');
    if (msg) msg.textContent = Core.pick(MESSAGES);
    Audio.init();
    Audio.celebrate();
  }

  function spawnConfetti() {
    const area = document.getElementById('confetti-area');
    area.innerHTML = '';
    for (let i = 0; i < 60; i++) {
      const piece = document.createElement('div');
      piece.className = 'confetti-piece';
      piece.style.left = `${Math.random() * 100}%`;
      piece.style.background = Core.pick(CONFETTI_COLORS);
      piece.style.width  = `${Core.randInt(8, 16)}px`;
      piece.style.height = `${Core.randInt(8, 16)}px`;
      piece.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
      piece.style.animationDuration = `${Core.randInt(1200, 2600)}ms`;
      piece.style.animationDelay    = `${Math.random() * 400}ms`;
      area.appendChild(piece);
    }
  }

  function init() {
    document.getElementById('btn-celebrate').addEventListener('click', () => {
      Audio.init();
      open();
    });
    document.getElementById('celebrate-close').addEventListener('click', () => {
      Core.hideOverlay('celebrate');
    });
  }

  return { init, open };
})();
