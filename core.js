/**
 * CORE ENGINE — Memory Garden
 * Screen navigation, date/time display, shared utilities.
 */

const Core = (() => {

  // ----- Screen Navigation -----
  const screens = {};

  function registerScreen(id) {
    screens[id] = document.getElementById(`screen-${id}`);
  }

  function showScreen(id) {
    Object.values(screens).forEach(s => {
      s.classList.remove('active');
      s.style.display = 'none';
    });
    const target = screens[id];
    if (target) {
      target.style.display = 'flex';
      // Trigger reflow then add active for CSS transitions
      target.offsetWidth;
      target.classList.add('active');
    }
  }

  // ----- Date / Time -----
  function updateDateTime() {
    const now = new Date();
    const hour = now.getHours();
    let greeting;
    if (hour < 12)       greeting = '☀️ Good Morning!';
    else if (hour < 17)  greeting = '🌤️ Good Afternoon!';
    else if (hour < 20)  greeting = '🌅 Good Evening!';
    else                 greeting = '🌙 Good Night!';

    const days   = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const dayName  = days[now.getDay()];
    const monthName = months[now.getMonth()];
    const dateNum   = now.getDate();
    const year      = now.getFullYear();

    const greetEl = document.getElementById('time-greeting');
    const dateEl  = document.getElementById('date-display');
    if (greetEl) greetEl.textContent = greeting;
    if (dateEl)  dateEl.textContent  = `${dayName}, ${monthName} ${dateNum}, ${year}`;
  }

  // ----- Score Manager -----
  const scores = {};

  function addScore(game, pts = 10) {
    scores[game] = (scores[game] || 0) + pts;
    const el = document.getElementById(`${game}-score`);
    if (el) {
      el.textContent = scores[game];
      el.style.transform = 'scale(1.4)';
      setTimeout(() => el.style.transform = 'scale(1)', 300);
    }
    return scores[game];
  }

  function getScore(game) { return scores[game] || 0; }
  function resetScore(game) { scores[game] = 0; const el = document.getElementById(`${game}-score`); if (el) el.textContent = '0'; }

  // ----- Feedback Popup -----
  function showFeedback(id, msg, isCorrect, duration = 1800) {
    const el = document.getElementById(id);
    if (!el) return;
    el.textContent = msg;
    el.className = `feedback-popup show ${isCorrect ? 'correct' : 'wrong'}`;
    clearTimeout(el._timer);
    el._timer = setTimeout(() => {
      el.classList.remove('show');
    }, duration);
  }

  // ----- Win Screen -----
  function showWin(game, msg) {
    const winMsg   = document.getElementById('win-msg');
    const winScore = document.getElementById('win-score-val');
    if (winMsg)   winMsg.textContent   = msg || 'Fantastic job!';
    if (winScore) winScore.textContent = getScore(game);
    showScreen('win');
    Audio.celebrate();
    showOverlay('celebrate');
  }

  // ----- Overlay Management -----
  function showOverlay(name) {
    document.getElementById(`overlay-${name}`).classList.remove('hidden');
  }
  function hideOverlay(name) {
    document.getElementById(`overlay-${name}`).classList.add('hidden');
  }

  // ----- Random Helpers -----
  function shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function randInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  function pick(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
  }

  function delay(ms) {
    return new Promise(res => setTimeout(res, ms));
  }

  return { registerScreen, showScreen, updateDateTime, addScore, getScore, resetScore, showFeedback, showWin, showOverlay, hideOverlay, shuffle, randInt, pick, delay };
})();
