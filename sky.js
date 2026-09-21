/**
 * SKY JOURNEY — Shape/Emoji Sort
 * Drag (or tap) clouds to their matching target zones.
 * Tap-to-select fallback for touch users who can't drag.
 */

const SkyGame = (() => {

  const CLOUD_ITEMS = [
    { emoji: '🌤️',  label: 'Sunny Cloud',  group: 'sun'   },
    { emoji: '🌧️',  label: 'Rain Cloud',   group: 'rain'  },
    { emoji: '❄️',   label: 'Snow Cloud',   group: 'snow'  },
    { emoji: '⛈️',  label: 'Storm Cloud',  group: 'storm' },
    { emoji: '🌤️',  label: 'Sunny Cloud',  group: 'sun'   },
    { emoji: '🌧️',  label: 'Rain Cloud',   group: 'rain'  },
    { emoji: '❄️',   label: 'Snow Cloud',   group: 'snow'  },
    { emoji: '⛈️',  label: 'Storm Cloud',  group: 'storm' },
  ];

  const TARGET_ZONES = [
    { group: 'sun',   emoji: '☀️',  label: 'Sunny' },
    { group: 'rain',  emoji: '🌧️', label: 'Rainy' },
    { group: 'snow',  emoji: '❄️',  label: 'Snowy' },
    { group: 'storm', emoji: '⛈️', label: 'Stormy'},
  ];

  let placed = {};
  let selected = null;

  function init() {
    Core.resetScore('sky');
    placed = {};
    selected = null;
    renderTargets();
    renderClouds();
  }

  function renderTargets() {
    const area = document.getElementById('sky-targets');
    area.innerHTML = '';
    TARGET_ZONES.forEach(t => {
      const div = document.createElement('div');
      div.className = 'sky-target';
      div.dataset.group = t.group;
      div.innerHTML = `
        <span style="font-size:2.5rem">${t.emoji}</span>
        <span class="sky-target-label">${t.label}</span>
      `;
      div.addEventListener('click', () => onTargetClick(t.group, div));
      div.addEventListener('dragover', e => { e.preventDefault(); div.classList.add('drag-over'); });
      div.addEventListener('dragleave',    ()     => div.classList.remove('drag-over'));
      div.addEventListener('drop',    e => { e.preventDefault(); div.classList.remove('drag-over'); onDrop(t.group, div); });
      area.appendChild(div);
    });
  }

  function renderClouds() {
    const area = document.getElementById('sky-clouds');
    area.innerHTML = '';
    const shuffled = Core.shuffle(CLOUD_ITEMS);

    shuffled.forEach((item, i) => {
      const div = document.createElement('div');
      div.className = 'sky-cloud';
      div.dataset.group = item.group;
      div.dataset.label = item.label;
      div.draggable = true;
      div.setAttribute('aria-label', item.label);
      div.innerHTML = `<span>${item.emoji}</span>`;

      div.addEventListener('dragstart', e => {
        e.dataTransfer.setData('group', item.group);
        e.dataTransfer.setData('index', i);
        div.classList.add('dragging');
        selected = div;
      });
      div.addEventListener('dragend', () => div.classList.remove('dragging'));
      div.addEventListener('click', () => onCloudClick(div, item.group));

      // Stagger entrance
      div.style.opacity = '0';
      div.style.transform = 'translateY(20px)';
      setTimeout(() => {
        div.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        div.style.opacity = '1';
        div.style.transform = 'translateY(0)';
      }, i * 80);

      area.appendChild(div);
    });
  }

  function onCloudClick(div, group) {
    Audio.init();
    if (div.classList.contains('placed')) return;
    if (selected && selected !== div) {
      selected.style.outline = '';
      selected = null;
    }
    selected = div;
    div.style.outline = '3px solid #f59e0b';
    Core.showFeedback('sky-feedback', `Now tap the matching sky! ☁️`, true);
  }

  function onTargetClick(group, targetDiv) {
    if (!selected) return;
    Audio.init();
    onDropInternal(group, targetDiv, selected.dataset.group, selected);
    selected.style.outline = '';
    selected = null;
  }

  function onDrop(group, targetDiv) {
    Audio.init();
    if (!selected) return;
    onDropInternal(group, targetDiv, selected.dataset.group, selected);
    selected = null;
  }

  function onDropInternal(targetGroup, targetDiv, cloudGroup, cloudDiv) {
    if (cloudGroup === targetGroup) {
      // CORRECT
      cloudDiv.classList.add('placed');
      targetDiv.classList.add('filled');
      Audio.correct();
      Core.addScore('sky', 10);
      Core.showFeedback('sky-feedback', `✅ Great! ${cloudDiv.dataset.label}!`, true);
      Particles.burst(
        targetDiv.getBoundingClientRect().left + 70,
        targetDiv.getBoundingClientRect().top + 50
      );

      placed[targetGroup] = (placed[targetGroup] || 0) + 1;
      const totalPlaced = Object.values(placed).reduce((a,b) => a+b, 0);

      if (totalPlaced >= CLOUD_ITEMS.length) {
        setTimeout(() => Core.showWin('sky', '☁️ You sorted all the clouds perfectly!'), 600);
      }
    } else {
      // WRONG
      Audio.wrong();
      Core.showFeedback('sky-feedback', `Try another spot! 💙`, false);
      cloudDiv.style.animation = 'wrongShake 0.5s ease';
      setTimeout(() => cloudDiv.style.animation = '', 600);
    }
  }

  return { init };
})();
