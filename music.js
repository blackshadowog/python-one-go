/**
 * MUSIC MEMORIES GAME
 * A Simon-Says style rhythm game with glowing coloured notes.
 * Tap the note that glows! As rounds progress, sequences get longer.
 */

const MusicGame = (() => {

  const NOTE_CONFIGS = [
    { emoji: '🎵', color: '#ef4444', name: 'Red Note'    },
    { emoji: '🎶', color: '#f59e0b', name: 'Gold Note'   },
    { emoji: '🎸', color: '#10b981', name: 'Green Note'  },
    { emoji: '🎹', color: '#3b82f6', name: 'Blue Note'   },
    { emoji: '🪗', color: '#8b5cf6', name: 'Purple Note' },
    { emoji: '🎺', color: '#ec4899', name: 'Pink Note'   },
    { emoji: '🥁', color: '#f97316', name: 'Orange Note' },
    { emoji: '🎻', color: '#06b6d4', name: 'Cyan Note'   },
  ];

  let sequence = [];
  let playerIndex = 0;
  let round = 0;
  let playing = false;
  let busy = false;
  const MAX_ROUNDS = 8;
  const VIZ_BARS = 20;

  function init() {
    Core.resetScore('music');
    sequence = [];
    round = 0;
    playerIndex = 0;
    playing = false;
    busy = false;
    renderNotes();
    renderVisualizer();
    startRound();
  }

  function renderNotes() {
    const grid = document.getElementById('music-notes-grid');
    grid.innerHTML = '';
    NOTE_CONFIGS.forEach((note, i) => {
      const btn = document.createElement('button');
      btn.className = 'note-btn';
      btn.id = `note-${i}`;
      btn.setAttribute('aria-label', note.name);
      btn.style.background = `${note.color}22`;
      btn.style.borderColor = note.color;
      btn.style.color = note.color;
      btn.innerHTML = `<span style="font-size:2.4rem">${note.emoji}</span>`;
      btn.addEventListener('click', () => onNoteClick(i));
      grid.appendChild(btn);
    });
  }

  function renderVisualizer() {
    const viz = document.getElementById('music-visualizer');
    viz.innerHTML = '';
    for (let i = 0; i < VIZ_BARS; i++) {
      const bar = document.createElement('div');
      bar.className = 'viz-bar';
      bar.style.height = '4px';
      viz.appendChild(bar);
    }
  }

  function animateVisualizer(noteIndex) {
    const bars = document.querySelectorAll('.viz-bar');
    bars.forEach((bar, i) => {
      const h = Math.abs(Math.sin((i + noteIndex) * 0.8)) * 55 + 5;
      bar.style.height = `${h}px`;
    });
    setTimeout(() => {
      bars.forEach(bar => { bar.style.height = '4px'; });
    }, 400);
  }

  async function startRound() {
    if (round >= MAX_ROUNDS) {
      Core.showWin('music', '🎵 You made beautiful music today!');
      return;
    }
    round++;
    playerIndex = 0;
    busy = true;

    // Add a new note to sequence
    sequence.push(Core.randInt(0, NOTE_CONFIGS.length - 1));

    await Core.delay(800);
    await playSequence();
    busy = false;
  }

  async function playSequence() {
    playing = true;
    for (let i = 0; i < sequence.length; i++) {
      const ni = sequence[i];
      await highlightNote(ni);
      await Core.delay(300);
    }
    playing = false;
  }

  async function highlightNote(noteIndex) {
    const btn = document.getElementById(`note-${noteIndex}`);
    if (!btn) return;
    btn.classList.add('glow');
    Audio.init();
    Audio.playMusicNote(noteIndex);
    animateVisualizer(noteIndex);
    await Core.delay(650);
    btn.classList.remove('glow');
  }

  async function onNoteClick(noteIndex) {
    if (busy || playing) return;
    Audio.init();

    const btn = document.getElementById(`note-${noteIndex}`);
    btn.classList.add('pressed');
    setTimeout(() => btn.classList.remove('pressed'), 350);
    Audio.playMusicNote(noteIndex);
    animateVisualizer(noteIndex);

    if (noteIndex === sequence[playerIndex]) {
      playerIndex++;
      Core.addScore('music', 5);

      if (playerIndex === sequence.length) {
        // Round complete
        busy = true;
        Core.showFeedback('music-feedback', `🎶 Round ${round} complete! Brilliant!`, true);
        Audio.correct();
        await Core.delay(1500);
        startRound();
      }
    } else {
      // Wrong — replay sequence
      busy = true;
      Core.showFeedback('music-feedback', `Almost! Watch again... 🎵`, false);
      Audio.wrong();
      playerIndex = 0;
      await Core.delay(1200);
      Core.showFeedback('music-feedback', ``, false);
      await playSequence();
      busy = false;
    }
  }

  return { init };
})();
