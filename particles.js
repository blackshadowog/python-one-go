/**
 * PARTICLE SYSTEM — Memory Garden
 * Draws floating glowing particles on a canvas for the ambient background.
 */

const Particles = (() => {
  let canvas, ctx, particles = [], animId;
  const COUNT = 60;

  function init() {
    canvas = document.getElementById('particle-canvas');
    ctx = canvas.getContext('2d');
    resize();
    createParticles();
    loop();
    window.addEventListener('resize', resize);
  }

  function resize() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function createParticles() {
    particles = [];
    for (let i = 0; i < COUNT; i++) {
      particles.push({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        r: Math.random() * 3 + 1,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        alpha: Math.random() * 0.6 + 0.2,
        hue: Math.random() * 60 + 240,    // purples to pinks
        pulseOffset: Math.random() * Math.PI * 2,
      });
    }
  }

  function loop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const now = Date.now() / 1000;

    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < -10) p.x = canvas.width + 10;
      if (p.x > canvas.width + 10) p.x = -10;
      if (p.y < -10) p.y = canvas.height + 10;
      if (p.y > canvas.height + 10) p.y = -10;

      const pulse = Math.sin(now * 1.5 + p.pulseOffset) * 0.3 + 0.7;
      const alpha = p.alpha * pulse;

      ctx.beginPath();
      const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 3);
      grad.addColorStop(0, `hsla(${p.hue}, 80%, 70%, ${alpha})`);
      grad.addColorStop(1, `hsla(${p.hue}, 80%, 70%, 0)`);
      ctx.fillStyle = grad;
      ctx.arc(p.x, p.y, p.r * 3, 0, Math.PI * 2);
      ctx.fill();
    });

    animId = requestAnimationFrame(loop);
  }

  // Burst of particles at a given position (e.g., on correct answer)
  function burst(x, y, color = '#f59e0b', count = 15) {
    for (let i = 0; i < count; i++) {
      const angle = (i / count) * Math.PI * 2;
      const speed = Math.random() * 3 + 1;
      particles.push({
        x, y,
        r: Math.random() * 4 + 2,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        alpha: 1,
        hue: parseInt(color.replace('#',''), 16) % 360,
        pulseOffset: 0,
        burst: true,
        life: 1,
      });
    }
    // Remove burst particles after a second
    setTimeout(() => {
      particles = particles.filter(p => !p.burst);
    }, 1500);
  }

  return { init, burst };
})();
