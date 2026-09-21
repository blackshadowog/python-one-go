/**
 * THE SEASONS GAME — Category Sorting
 * Sort items/symbols into their correct season.
 * Great for temporal orientation and reminiscence.
 */

const SeasonsGame = (() => {

  const SEASON_ITEMS = [
    // Spring
    { emoji: '🌸', name: 'Cherry Blossom', season: 'spring' },
    { emoji: '🌱', name: 'New Seedling',   season: 'spring' },
    { emoji: '🐣', name: 'Baby Chick',     season: 'spring' },
    { emoji: '🌷', name: 'Tulip',          season: 'spring' },
    { emoji: '🌦️', name: 'April Shower',   season: 'spring' },
    // Summer
    { emoji: '☀️', name: 'Bright Sun',     season: 'summer' },
    { emoji: '🏖️', name: 'Beach',          season: 'summer' },
    { emoji: '🍦', name: 'Ice Cream',      season: 'summer' },
    { emoji: '🌻', name: 'Sunflower',      season: 'summer' },
    { emoji: '🩳', name: 'Shorts',         season: 'summer' },
    // Autumn
    { emoji: '🍂', name: 'Autumn Leaf',    season: 'autumn' },
    { emoji: '🎃', name: 'Pumpkin',        season: 'autumn' },
    { emoji: '🍎', name: 'Apple',          season: 'autumn' },
    { emoji: '🦔', name: 'Hedgehog',       season: 'autumn' },
    { emoji: '🧣', name: 'Scarf',          season: 'autumn' },
    // Winter
    { emoji: '❄️', name: 'Snowflake',      season: 'winter' },
    { emoji: '⛄', name: 'Snowman',        season: 'winter' },
    { emoji: '🧥', name: 'Winter Coat',    season: 'winter' },
    { emoji: '🎄', name: 'Christmas Tree', season: 'winter' },
    { emoji: '🍵', name: 'Hot Cocoa',      season: 'winter' },
  ];

  const SEASONS = [
    { key: 'spring', emoji: '🌸', label: 'Spring', desc: 'Warm & Blooming'  },
    { key: 'summer', emoji: '☀️', label: 'Summer', desc: 'Hot & Sunny'      },
    { key: 'autumn', emoji: '🍂', label: 'Autumn', desc: 'Cool & Colourful' },
    { key: 'winter', emoji: '❄️', label: 'Winter', desc: 'Cold & Snowy'     },
  ];

  let queue = [];
  let round = 0;
  let currentItem = null;
  const ROUNDS = 12;

  function init() {
    Core.resetScore('seasons');
    round = 0;
    queue = Core.shuffle([...SEASON_ITEMS]);
    renderBuckets();
    nextRound();
  }

  function renderBuckets() {
    const container = document.getElementById('seasons-buckets');
    container.innerHTML = '';
    SEASONS.forEach(s => {
      const btn = document.createElement('button');
      btn.className = 'season-bucket';
      btn.dataset.season = s.key;
      btn.innerHTML = `
        <span style="font-size:2.5rem">${s.emoji}</span>
        <span class="season-bucket-label">${s.label}</span>
        <span class="season-bucket-desc">${s.desc}</span>
      `;
      btn.addEventListener('click', () => onSeasonClick(s.key, btn));
      container.appendChild(btn);
    });
  }

  function nextRound() {
    if (round >= ROUNDS || round >= queue.length) {
      Core.showWin('seasons', '🍂 You sorted all the seasons!');
      return;
    }
    currentItem = queue[round];
    round++;

    const display = document.getElementById('seasons-item-display');
    display.style.opacity = '0';
    display.style.transform = 'scale(0.5)';
    setTimeout(() => {
      display.innerHTML = `
        <div style="font-size:5rem; line-height:1">${currentItem.emoji}</div>
        <div style="font-size:1.2rem; font-weight:700; margin-top:12px; color:rgba(255,255,255,0.8)">${currentItem.name}</div>
      `;
      display.style.transition = 'opacity 0.4s ease, transform 0.4s cubic-bezier(0.34,1.56,0.64,1)';
      display.style.opacity = '1';
      display.style.transform = 'scale(1)';
    }, 100);

    // Reset bucket states
    document.querySelectorAll('.season-bucket').forEach(b => {
      b.classList.remove('correct-season', 'wrong-season');
      b.disabled = false;
    });
  }

  async function onSeasonClick(season, btn) {
    if (!currentItem) return;
    Audio.init();

    document.querySelectorAll('.season-bucket').forEach(b => b.disabled = true);

    if (season === currentItem.season) {
      btn.classList.add('correct-season');
      Audio.correct();
      Core.addScore('seasons', 10);

      const seasonInfo = SEASONS.find(s => s.key === season);
      Core.showFeedback('seasons-feedback',
        `✅ Yes! ${currentItem.emoji} is ${seasonInfo.label}! ${seasonInfo.emoji}`, true, 1800);

      Particles.burst(
        btn.getBoundingClientRect().left + 70,
        btn.getBoundingClientRect().top + 40
      );

      await Core.delay(1800);
    } else {
      btn.classList.add('wrong-season');
      // Highlight correct
      document.querySelectorAll('.season-bucket').forEach(b => {
        if (b.dataset.season === currentItem.season) b.classList.add('correct-season');
      });
      Audio.wrong();
      const correct = SEASONS.find(s => s.key === currentItem.season);
      Core.showFeedback('seasons-feedback',
        `💙 It's ${correct.label} ${correct.emoji}! You'll get the next one!`, false, 2000);
      await Core.delay(2200);
    }

    nextRound();
  }

  return { init };
})();
