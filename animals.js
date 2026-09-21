/**
 * ANIMAL FRIENDS — Sound-to-Animal Matching
 * Players hear the sound description and pick the right animal.
 * Includes fun facts for cognitive stimulation.
 */

const AnimalsGame = (() => {

  const ANIMALS = [
    { emoji: '🐶', name: 'Dog',      sound: 'Woof! Woof!',      fact: 'Dogs are very loyal friends!' },
    { emoji: '🐱', name: 'Cat',      sound: 'Meow!',            fact: 'Cats purr when they are happy!' },
    { emoji: '🐮', name: 'Cow',      sound: 'Moo!',             fact: 'Cows live on farms and give us milk!' },
    { emoji: '🐸', name: 'Frog',     sound: 'Ribbit! Ribbit!',  fact: 'Frogs love to jump and swim!' },
    { emoji: '🦆', name: 'Duck',     sound: 'Quack! Quack!',    fact: 'Ducks love to swim in ponds!' },
    { emoji: '🐔', name: 'Chicken',  sound: 'Cluck! Cluck!',    fact: 'Chickens wake us up in the morning!' },
    { emoji: '🐴', name: 'Horse',    sound: 'Neigh!',           fact: 'Horses can run very fast!' },
    { emoji: '🐷', name: 'Pig',      sound: 'Oink! Oink!',      fact: 'Pigs are actually very clever animals!' },
    { emoji: '🦁', name: 'Lion',     sound: 'Roar!!!',          fact: 'Lions are called the king of the jungle!' },
    { emoji: '🐘', name: 'Elephant', sound: 'Trumpet sound!',   fact: 'Elephants have excellent memories!' },
    { emoji: '🦜', name: 'Parrot',   sound: 'Hello! Pretty bird!', fact: 'Parrots can learn to talk!' },
    { emoji: '🐝', name: 'Bee',      sound: 'Buzzzzz!',         fact: 'Bees make delicious honey!' },
  ];

  let queue = [];
  let current = null;
  let round = 0;
  const ROUNDS = 10;

  function init() {
    Core.resetScore('animals');
    round = 0;
    queue = Core.shuffle(ANIMALS);
    nextRound();
  }

  function nextRound() {
    if (round >= ROUNDS) {
      Core.showWin('animals', '🐾 You know all the animal friends!');
      return;
    }
    round++;
    current = queue[round - 1] || Core.pick(ANIMALS);

    // Pick 3 wrong answers
    const others = ANIMALS.filter(a => a.name !== current.name);
    const choices = Core.shuffle([...Core.shuffle(others).slice(0, 3), current]);

    renderSoundDisplay();
    renderChoices(choices);
  }

  function renderSoundDisplay() {
    const display = document.getElementById('animals-sound-display');
    display.innerHTML = `
      <div style="font-size:3rem; font-weight:800; color:#f59e0b; margin-bottom:8px">${current.sound}</div>
      <div style="font-size:1rem; color:rgba(255,255,255,0.5)">Tap the matching animal 👇</div>
    `;
    display.onclick = () => {
      Audio.init();
      Audio.click();
      display.style.animation = 'none';
      display.offsetWidth; // reflow
      display.style.animation = 'animalPulse 0.5s ease';
    };

    document.getElementById('animals-instruct').textContent =
      `What animal says: "${current.sound}"? 🔊`;
  }

  function renderChoices(choices) {
    const container = document.getElementById('animals-choices');
    container.innerHTML = '';

    choices.forEach(animal => {
      const btn = document.createElement('button');
      btn.className = 'animal-choice-btn';
      btn.setAttribute('aria-label', animal.name);
      btn.innerHTML = `
        <span style="font-size:3rem">${animal.emoji}</span>
        <span class="animal-choice-label">${animal.name}</span>
      `;

      btn.style.opacity = '0';
      btn.style.transform = 'scale(0.8)';

      btn.addEventListener('click', () => onChoice(animal, btn, choices));
      container.appendChild(btn);

      setTimeout(() => {
        btn.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        btn.style.opacity = '1';
        btn.style.transform = 'scale(1)';
      }, 100 + Math.random() * 150);
    });
  }

  async function onChoice(animal, btn, allBtns) {
    Audio.init();
    // Disable all buttons
    document.querySelectorAll('.animal-choice-btn').forEach(b => b.disabled = true);

    if (animal.name === current.name) {
      btn.classList.add('correct-answer');
      Audio.correct();
      Core.addScore('animals', 10);

      // Show fact
      Core.showFeedback('animals-feedback', `✅ Yes! ${animal.emoji} ${animal.fact}`, true, 2500);
      Particles.burst(
        btn.getBoundingClientRect().left + 60,
        btn.getBoundingClientRect().top + 50
      );

      await Core.delay(2800);
    } else {
      btn.classList.add('wrong-answer');
      // Reveal correct
      document.querySelectorAll('.animal-choice-btn').forEach(b => {
        if (b.getAttribute('aria-label') === current.name) b.classList.add('correct-answer');
      });
      Audio.wrong();
      Core.showFeedback('animals-feedback', `💙 The answer was ${current.emoji} ${current.name}! Try the next one!`, false, 2000);
      await Core.delay(2200);
    }

    nextRound();
  }

  return { init };
})();
