/**
 * FRIENDLY FACES GAME — Card Memory Match
 * Classic flip-and-match with friendly emoji faces.
 * Large cards, forgiving timing, encouraging messages.
 */

const FacesGame = (() => {

  const FACE_EMOJIS = [
    '😊', '🥰', '😄', '😁', '🤩',
    '😍', '🥳', '😎', '🤗', '😇',
    '😸', '🦁', '🐶', '🦊', '🐨',
    '🌸', '🌈', '⭐', '🎀', '🏆',
  ];

  const ENCOURAGEMENTS = [
    '🎉 Wonderful!',
    '✨ Amazing match!',
    '🌟 You remembered!',
    '💖 Brilliant!',
    '🎊 Perfect!',
    '🥳 Spectacular!',
  ];

  let flipped = [];
  let matched = [];
  let busy = false;
  let moves = 0;
  let pairs = 0;

  function init() {
    Core.resetScore('faces');
    flipped = [];
    matched = [];
    busy = false;
    moves = 0;
    pairs = 0;
    renderCards();
  }

  function renderCards() {
    const grid = document.getElementById('faces-grid');
    grid.innerHTML = '';

    // 8 pairs = 16 cards (4x4)
    const selected = Core.shuffle(FACE_EMOJIS).slice(0, 8);
    const all = Core.shuffle([...selected, ...selected]);

    all.forEach((emoji, i) => {
      const card = document.createElement('div');
      card.className = 'face-card';
      card.dataset.emoji = emoji;
      card.dataset.index = i;
      card.setAttribute('role', 'button');
      card.setAttribute('aria-label', `Card ${i + 1}`);
      card.setAttribute('tabindex', '0');

      card.innerHTML = `
        <div class="face-card-inner">
          <div class="face-front">❓</div>
          <div class="face-back">${emoji}</div>
        </div>
      `;

      card.addEventListener('click', () => onCardClick(card));
      card.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') onCardClick(card); });

      // Stagger appearance
      card.style.opacity = '0';
      card.style.transform = 'scale(0.7)';
      setTimeout(() => {
        card.style.transition = 'opacity 0.4s ease, transform 0.4s cubic-bezier(0.34,1.56,0.64,1)';
        card.style.opacity = '1';
        card.style.transform = 'scale(1)';
      }, i * 60);

      grid.appendChild(card);
    });
  }

  async function onCardClick(card) {
    Audio.init();
    if (busy) return;
    if (card.classList.contains('flipped')) return;
    if (card.classList.contains('matched')) return;
    if (flipped.length >= 2) return;

    // Flip card
    card.classList.add('flipped');
    Audio.flip();
    flipped.push(card);

    if (flipped.length === 2) {
      busy = true;
      moves++;
      const [a, b] = flipped;

      if (a.dataset.emoji === b.dataset.emoji) {
        // MATCH!
        await Core.delay(400);
        a.classList.add('matched');
        b.classList.add('matched');
        Audio.match();

        const pts = Math.max(10, 20 - moves);
        Core.addScore('faces', pts);

        const msg = Core.pick(ENCOURAGEMENTS);
        Core.showFeedback('faces-feedback', msg, true);

        // Particle burst
        const rectA = a.getBoundingClientRect();
        Particles.burst(rectA.left + rectA.width/2, rectA.top + rectA.height/2);

        pairs++;
        flipped = [];
        busy = false;
        moves = 0;

        if (pairs === 8) {
          await Core.delay(800);
          Core.showWin('faces', '😊 You matched all the friendly faces!');
        }
      } else {
        // No match — flip back
        Audio.wrong();
        Core.showFeedback('faces-feedback', '💙 Try again! You can do it!', false);
        await Core.delay(1000);
        a.classList.remove('flipped');
        b.classList.remove('flipped');
        flipped = [];
        busy = false;
      }
    }
  }

  return { init };
})();
