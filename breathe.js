/**
 * BREATHE OVERLAY — Guided Breathing Exercise
 * 4-second inhale, 6-second exhale breathing cycle.
 * Therapeutic for anxiety and agitation common in dementia.
 */

const Breathe = (() => {

  let intervalId = null;
  let phase = 'in'; // 'in' | 'hold' | 'out'
  let active = false;

  const PHASES = [
    { name: 'Breathe In',  duration: 4000, expand: true,  sound: 'in'  },
    { name: 'Hold...',     duration: 1500, expand: true,  sound: null  },
    { name: 'Breathe Out', duration: 6000, expand: false, sound: 'out' },
    { name: 'And Rest...',  duration: 1000, expand: false, sound: null  },
  ];

  let phaseIndex = 0;

  function open() {
    Core.showOverlay('breathe');
    active = true;
    phaseIndex = 0;
    Audio.init();
    runPhase();
  }

  function close() {
    active = false;
    clearTimeout(intervalId);
    Core.hideOverlay('breathe');
    const circle = document.getElementById('breathe-circle');
    circle.classList.remove('expand');
  }

  function runPhase() {
    if (!active) return;
    const phase = PHASES[phaseIndex % PHASES.length];

    const circle = document.getElementById('breathe-circle');
    const text   = document.getElementById('breathe-text');
    const cap    = document.getElementById('breathe-caption');

    text.textContent = phase.name;

    if (phase.expand) {
      circle.classList.add('expand');
    } else {
      circle.classList.remove('expand');
    }

    if (phase.sound === 'in')  Audio.breatheIn();
    if (phase.sound === 'out') Audio.breatheOut();

    phaseIndex++;
    intervalId = setTimeout(runPhase, phase.duration);
  }

  function init() {
    document.getElementById('btn-breathe').addEventListener('click', () => {
      Audio.init();
      open();
    });
    document.getElementById('breathe-close').addEventListener('click', close);
  }

  return { init, open, close };
})();
