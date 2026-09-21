/**
 * GARDEN GAME — Colour Matching
 * Player sees a target colour and must tap the matching flower.
 * Flowers grow, sway, and bloom on correct answers.
 */

const GardenGame = (() => {

  const COLOURS = [
    { name: 'Red',    hex: '#ef4444', emoji: '🌹', water: '💧' },
    { name: 'Yellow', hex: '#f59e0b', emoji: '🌻', water: '💛' },
    { name: 'Blue',   hex: '#3b82f6', emoji: '💙', water: '💧' },
    { name: 'Pink',   hex: '#ec4899', emoji: '🌸', water: '🩷' },
    { name: 'Purple', hex: '#8b5cf6', emoji: '💜', water: '💧' },
    { name: 'Orange', hex: '#f97316', emoji: '🌼', water: '🧡' },
    { name: 'Green',  hex: '#10b981', emoji: '🌿', water: '💚' },
    { name: 'White',  hex: '#f8fafc', emoji: '🤍', water: '💧' },
  ];

  let targetColour = null;
  let score = 0;
  let round = 0;
  const ROUNDS = 10;
  let busy = false;

  function init() {
    score = 0;
    round = 0;
    Core.resetScore('garden');
    busy = false;
    nextRound();
  }

  function nextRound() {
    if (round >= ROUNDS) {
      Core.showWin('garden', '🌻 You watered all the flowers!');
      return;
    }
    round++;
    busy = false;

    // Pick target colour
    targetColour = Core.pick(COLOURS);

    // Pick 5 distractors (distinct from target)
    let pool = COLOURS.filter(c => c.name !== targetColour.name);
    pool = Core.shuffle(pool).slice(0, 5);
    pool.push(targetColour);
    pool = Core.shuffle(pool);

    renderTarget(targetColour);
    renderFlowers(pool);

    document.getElementById('garden-instruct-txt').textContent =
      `Water the ${targetColour.name} flower! 💧`;
  }

  function renderTarget(colour) {
    const zone = document.getElementById('garden-target-zone');
    zone.innerHTML = `
      <div class="garden-target-label">Water this colour:</div>
      <div class="garden-target-swatch" style="background:${colour.hex}; color:${colour.hex}"></div>
      <div style="font-size:1.1rem; font-weight:700; color:${colour.hex}">${colour.name}</div>
    `;
  }

  function renderFlowers(pool) {
    const container = document.getElementById('garden-flowers');
    container.innerHTML = '';

    pool.forEach(colour => {
      const btn = document.createElement('button');
      btn.className = 'flower-btn';
      btn.style.background = `${colour.hex}22`;
      btn.style.borderColor = colour.hex;
      btn.setAttribute('aria-label', `${colour.name} flower`);
      btn.innerHTML = `
        <div class="flower-emoji">${colour.emoji}</div>
        <span>${colour.name}</span>
      `;
      btn.addEventListener('click', () => handleChoice(colour, btn));
      container.appendChild(btn);

      // Stagger entrance
      btn.style.opacity = '0';
      btn.style.transform = 'scale(0.5)';
      setTimeout(() => {
        btn.style.transition = 'opacity 0.4s ease, transform 0.4s cubic-bezier(0.34,1.56,0.64,1)';
        btn.style.opacity = '1';
        btn.style.transform = 'scale(1)';
      }, 50 + Math.random() * 200);
    });
  }

  async function handleChoice(colour, btn) {
    if (busy) return;
    busy = true;
    Audio.init();

    if (colour.name === targetColour.name) {
      // CORRECT
      btn.classList.add('correct-flash');
      Audio.correct();
      Core.addScore('garden', 10);
      Core.showFeedback('garden-feedback', `✅ Yes! ${colour.emoji} ${colour.name}! Beautiful!`, true);

      // Make confetti burst appear
      const rect = btn.getBoundingClientRect();
      Particles.burst(rect.left + rect.width/2, rect.top + rect.height/2, colour.hex);

      await Core.delay(1200);
      document.getElementById('garden-flowers').innerHTML = '';
      document.getElementById('garden-target-zone').innerHTML = '';
      nextRound();
    } else {
      // WRONG
      btn.classList.add('wrong-shake');
      Audio.wrong();
      Core.showFeedback('garden-feedback', `Try again! Look for the ${targetColour.name} one 💙`, false);
      setTimeout(() => btn.classList.remove('wrong-shake'), 600);
      await Core.delay(800);
      busy = false;
    }
  }

  return { init };
})();
