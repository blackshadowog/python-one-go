/**
 * SETTINGS MODULE
 * Font size, sound toggle, speed, theme colour.
 */

const Settings = (() => {

  let soundOn = true;
  let speed = 'slow';
  let currentTheme = 'default';

  function init() {
    document.getElementById('btn-settings').addEventListener('click', () => {
      Core.showOverlay('settings');
    });
    document.getElementById('settings-close').addEventListener('click', () => {
      Core.hideOverlay('settings');
    });

    // Font size
    document.getElementById('font-small').addEventListener('click', () => setFont('small'));
    document.getElementById('font-medium').addEventListener('click', () => setFont('medium'));
    document.getElementById('font-large').addEventListener('click', () => setFont('large'));

    // Sound toggle
    document.getElementById('toggle-sound').addEventListener('click', () => {
      soundOn = !soundOn;
      Audio.setSoundEnabled(soundOn);
      const btn = document.getElementById('toggle-sound');
      btn.textContent = soundOn ? '🔊 On' : '🔇 Off';
      btn.classList.toggle('off', !soundOn);
    });

    // Speed
    document.getElementById('speed-slow').addEventListener('click', () => setSpeed('slow'));
    document.getElementById('speed-normal').addEventListener('click', () => setSpeed('normal'));

    // Themes
    document.querySelectorAll('.swatch').forEach(swatch => {
      swatch.addEventListener('click', () => {
        setTheme(swatch.dataset.theme);
        document.querySelectorAll('.swatch').forEach(s => s.classList.remove('active'));
        swatch.classList.add('active');
      });
    });
  }

  function setFont(size) {
    document.body.className = document.body.className.replace(/font-\w+/g, '');
    document.body.classList.add(`font-${size}`);
    document.querySelectorAll('.setting-btn').forEach(b => {
      if (['font-small','font-medium','font-large'].includes(b.id)) b.classList.remove('active');
    });
    document.getElementById(`font-${size}`).classList.add('active');
  }

  function setSpeed(s) {
    speed = s;
    document.getElementById('speed-slow').classList.toggle('active', s === 'slow');
    document.getElementById('speed-normal').classList.toggle('active', s === 'normal');
  }

  function setTheme(theme) {
    currentTheme = theme;
    document.documentElement.dataset.theme = theme;
  }

  function getSpeed() { return speed; }

  return { init, getSpeed };
})();
