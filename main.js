/**
 * MAIN.JS — Entry Point & Navigation Wiring
 * Bootstraps all modules and wires up navigation.
 */

// ---- Register Screens ----
['home', 'garden', 'music', 'faces', 'sky', 'animals', 'seasons', 'win'].forEach(id => {
  Core.registerScreen(id);
});

// ---- Current game tracker ----
let currentGame = null;

// ---- Game Launchers ----
const GAME_LAUNCHERS = {
  garden:  () => GardenGame.init(),
  music:   () => MusicGame.init(),
  faces:   () => FacesGame.init(),
  sky:     () => SkyGame.init(),
  animals: () => AnimalsGame.init(),
  seasons: () => SeasonsGame.init(),
};

// ---- Home → Game ----
document.querySelectorAll('.game-card').forEach(card => {
  card.addEventListener('click', () => {
    const game = card.dataset.game;
    Audio.init();
    Audio.click();
    currentGame = game;
    Core.showScreen(game);
    if (GAME_LAUNCHERS[game]) GAME_LAUNCHERS[game]();
  });
});

// ---- Back buttons (game → home) ----
document.querySelectorAll('.back-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    Audio.click();
    Core.showScreen('home');
  });
});

// ---- Win Screen ----
document.getElementById('win-play-again').addEventListener('click', () => {
  Audio.click();
  Core.hideOverlay('celebrate');
  Core.showScreen(currentGame);
  if (GAME_LAUNCHERS[currentGame]) GAME_LAUNCHERS[currentGame]();
});
document.getElementById('win-home').addEventListener('click', () => {
  Audio.click();
  Core.hideOverlay('celebrate');
  Core.showScreen('home');
});

// ---- Initialize Modules ----
window.addEventListener('DOMContentLoaded', () => {
  // Init particles
  Particles.init();

  // Init date/time
  Core.updateDateTime();
  setInterval(Core.updateDateTime, 60000);

  // Init overlays
  Breathe.init();
  Celebrate.init();
  Settings.init();

  // Show home
  Core.showScreen('home');

  // First interaction unlocks audio context
  document.addEventListener('click', () => { Audio.init(); }, { once: true });

  console.log('🌸 Memory Garden loaded! Let the joy begin!');
});
