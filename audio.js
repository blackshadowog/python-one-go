/**
 * AUDIO ENGINE — Memory Garden
 * Uses Web Audio API to generate all sounds procedurally.
 * No external audio files needed!
 */

const Audio = (() => {
  let ctx = null;
  let soundEnabled = true;
  let masterGain;

  function init() {
    if (ctx) return;
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    masterGain = ctx.createGain();
    masterGain.gain.value = 0.5;
    masterGain.connect(ctx.destination);
  }

  function resume() {
    if (ctx && ctx.state === 'suspended') ctx.resume();
  }

  function setSoundEnabled(val) { soundEnabled = val; }

  // ---- Note Frequencies (pentatonic scale — always sounds nice!) ----
  const NOTES = {
    C4: 261.63, D4: 293.66, E4: 329.63, G4: 392.00, A4: 440.00,
    C5: 523.25, D5: 587.33, E5: 659.25, G5: 783.99, A5: 880.00,
    C6: 1046.5
  };

  const NOTE_LIST = Object.values(NOTES);

  function playTone(freq, type = 'sine', duration = 0.4, gainVal = 0.4, delay = 0) {
    if (!soundEnabled || !ctx) return;
    resume();
    const now = ctx.currentTime + delay;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(masterGain);
    osc.type = type;
    osc.frequency.setValueAtTime(freq, now);
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(gainVal, now + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.001, now + duration);
    osc.start(now);
    osc.stop(now + duration + 0.05);
  }

  function correct() {
    playTone(NOTES.E5, 'sine', 0.2, 0.4);
    playTone(NOTES.G5, 'sine', 0.25, 0.35, 0.15);
    playTone(NOTES.C6, 'sine', 0.4, 0.3, 0.28);
  }

  function wrong() {
    playTone(220, 'sawtooth', 0.2, 0.2);
    playTone(180, 'sawtooth', 0.2, 0.15, 0.12);
  }

  function click() {
    playTone(NOTES.G4, 'sine', 0.12, 0.25);
  }

  function celebrate() {
    // Happy ascending arpeggio
    const melody = [NOTES.C5, NOTES.E5, NOTES.G5, NOTES.C6];
    melody.forEach((freq, i) => playTone(freq, 'sine', 0.5, 0.3, i * 0.12));
    setTimeout(() => {
      playTone(NOTES.C6, 'sine', 0.8, 0.35, 0);
    }, 500);
  }

  function flip() {
    playTone(NOTES.G4, 'triangle', 0.15, 0.3);
  }

  function match() {
    playTone(NOTES.C5, 'sine', 0.15, 0.3, 0);
    playTone(NOTES.G5, 'sine', 0.25, 0.25, 0.1);
  }

  function breatheIn() {
    // Rising tone
    if (!soundEnabled || !ctx) return;
    resume();
    const now = ctx.currentTime;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(masterGain);
    osc.type = 'sine';
    osc.frequency.setValueAtTime(200, now);
    osc.frequency.linearRampToValueAtTime(400, now + 4);
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(0.15, now + 1);
    gain.gain.linearRampToValueAtTime(0.0001, now + 4);
    osc.start(now);
    osc.stop(now + 4.1);
  }

  function breatheOut() {
    if (!soundEnabled || !ctx) return;
    resume();
    const now = ctx.currentTime;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(masterGain);
    osc.type = 'sine';
    osc.frequency.setValueAtTime(400, now);
    osc.frequency.linearRampToValueAtTime(200, now + 6);
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.linearRampToValueAtTime(0.12, now + 0.5);
    gain.gain.linearRampToValueAtTime(0.0001, now + 6);
    osc.start(now);
    osc.stop(now + 6.1);
  }

  // Music notes at specific frequencies for the music game
  function playMusicNote(noteIndex) {
    if (!soundEnabled || !ctx) return;
    resume();
    const freq = NOTE_LIST[noteIndex % NOTE_LIST.length];
    playTone(freq, 'triangle', 0.6, 0.5, 0);
    // Add harmonics for richness
    playTone(freq * 1.5, 'sine', 0.4, 0.2, 0);
    playTone(freq * 2, 'sine', 0.3, 0.1, 0);
  }

  function playMelody(notes) {
    notes.forEach((noteIndex, i) => {
      setTimeout(() => playMusicNote(noteIndex), i * 400);
    });
  }

  return { init, correct, wrong, click, celebrate, flip, match, breatheIn, breatheOut, playMusicNote, playMelody, setSoundEnabled, resume };
})();
