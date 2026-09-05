<div align="center">

<svg width="180" height="180" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mmGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff"/>
      <stop offset="100%" stop-color="#7b2ff7"/>
    </linearGradient>
    <linearGradient id="mmGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff3df0"/>
      <stop offset="100%" stop-color="#00f0ff"/>
    </linearGradient>
    <filter id="mmGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <radialGradient id="mmBgGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="110" cy="110" r="105" fill="url(#mmBgGlow)"/>
  <g>
    <ellipse cx="110" cy="110" rx="95" ry="35" fill="none" stroke="url(#mmGrad1)" stroke-width="1.4" opacity="0.55">
      <animateTransform attributeName="transform" type="rotate" from="0 110 110" to="360 110 110" dur="6s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <g>
    <ellipse cx="110" cy="110" rx="95" ry="35" fill="none" stroke="url(#mmGrad2)" stroke-width="1.4" opacity="0.4" transform="rotate(60 110 110)">
      <animateTransform attributeName="transform" type="rotate" from="60 110 110" to="420 110 110" dur="8s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <g>
    <ellipse cx="110" cy="110" rx="95" ry="35" fill="none" stroke="#ffcc33" stroke-width="1" opacity="0.3" transform="rotate(120 110 110)">
      <animateTransform attributeName="transform" type="rotate" from="120 110 110" to="480 110 110" dur="10s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <g>
    <circle r="3.4" fill="#ffcc33" filter="url(#mmGlow)">
      <animateMotion dur="6s" repeatCount="indefinite" path="M 15,110 A 95,35 0 1 1 205,110 A 95,35 0 1 1 15,110 Z"/>
    </circle>
  </g>
  <g filter="url(#mmGlow)">
    <polygon points="110,55 155,82 155,138 110,165 65,138 65,82" fill="none" stroke="url(#mmGrad1)" stroke-width="2.2">
      <animateTransform attributeName="transform" type="rotate" from="0 110 110" to="360 110 110" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="stroke-opacity" values="1;0.4;1" dur="2.5s" repeatCount="indefinite"/>
    </polygon>
    <polygon points="110,70 142,90 142,130 110,150 78,130 78,90" fill="none" stroke="url(#mmGrad2)" stroke-width="1.6">
      <animateTransform attributeName="transform" type="rotate" from="360 110 110" to="0 110 110" dur="5s" repeatCount="indefinite"/>
    </polygon>
    <text x="110" y="122" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-weight="700" font-size="34" fill="#eafffe">
      MM
      <animateTransform attributeName="transform" type="scale" values="1,1;1.12,0.9;1,1;0.9,1.12;1,1" dur="4s" repeatCount="indefinite" additive="sum"/>
    </text>
  </g>
  <circle cx="110" cy="110" r="18" fill="none" stroke="#00f0ff" stroke-width="1" opacity="0">
    <animate attributeName="r" values="18;100" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0" dur="3s" repeatCount="indefinite"/>
  </circle>
</svg>

# MOHAK MITTAL
### Game Developer · 3D Artist · Systems Builder

<a href="https://mohak-mittal.github.io/Portfolio" target="_blank"><img src="https://img.shields.io/badge/PORTFOLIO-mohak--mittal.github.io-00f0ff?style=for-the-badge&logo=googlechrome&logoColor=black&labelColor=0b0b1e" /></a>

</div>

<br/>

> Building toward one thing: **my own game studio.** Everything below — the engine work, the 3D art, the tools — is on that road.

<br/>

## ⚡ Play "Gravity Drift" — an original game, built for this profile

Not another Snake clone. You pilot a drone through a field of rotating gravity wells, slingshotting around them to grab energy cores. Get too close and the pull kills you — no safe path, no memorized route, just physics and nerve. The full source is embedded below in one file: **copy it into a `.html` file and open it in any browser to play instantly**, or drop it on GitHub Pages as `index.html` for a shareable link.

<details>
<summary><b>▶ Click to expand the full game source (single HTML file, no dependencies)</b></summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GRAVITY DRIFT — by Mohak Mittal</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root{
    --void:#050510;
    --core:#00f0ff;
    --core2:#ff3df0;
    --warn:#ffcc33;
    --panel:#0b0b1e;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html,body{
    height:100%;
    background:var(--void);
    overflow:hidden;
    font-family:'Segoe UI', system-ui, sans-serif;
    color:#e6f7ff;
  }
  #wrap{
    position:relative;
    width:100vw;
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
  }
  canvas{
    display:block;
    background:radial-gradient(ellipse at 50% 40%, #0d0d24 0%, #050510 70%);
    box-shadow:0 0 60px rgba(0,240,255,0.08) inset;
  }
  #hud{
    position:absolute;
    top:16px; left:16px;
    font-size:13px;
    letter-spacing:1px;
    line-height:1.6;
    text-shadow:0 0 8px rgba(0,240,255,0.6);
    pointer-events:none;
    user-select:none;
  }
  #hud .label{ color:#5fd4e8; opacity:0.8; }
  #hud .val{ color:#fff; font-weight:600; }
  #overlay{
    position:absolute; inset:0;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    text-align:center;
    background:rgba(3,3,12,0.82);
    backdrop-filter:blur(2px);
    padding:24px;
  }
  #overlay h1{
    font-size:clamp(28px,6vw,52px);
    letter-spacing:6px;
    background:linear-gradient(90deg,var(--core),var(--core2));
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
    text-shadow:0 0 30px rgba(0,240,255,0.25);
    margin-bottom:10px;
  }
  #overlay p{ max-width:440px; color:#a9c7d8; font-size:14px; line-height:1.6; margin-bottom:18px; }
  #overlay .big{ font-size:15px; color:#fff; margin-bottom:6px; }
  #overlay .score{ font-size:40px; font-weight:700; color:var(--warn); text-shadow:0 0 20px rgba(255,204,51,0.4); margin-bottom:18px; }
  button{
    font-family:inherit;
    font-size:15px;
    letter-spacing:2px;
    padding:12px 30px;
    background:linear-gradient(90deg,var(--core),var(--core2));
    border:none;
    color:#03030a;
    font-weight:700;
    border-radius:2px;
    cursor:pointer;
    box-shadow:0 0 24px rgba(0,240,255,0.35);
    transition:transform .12s ease, box-shadow .12s ease;
  }
  button:hover{ transform:translateY(-2px); box-shadow:0 0 34px rgba(0,240,255,0.55); }
  button:active{ transform:translateY(0); }
  #footer{
    position:absolute; bottom:10px; width:100%;
    text-align:center; font-size:11px; letter-spacing:1px;
    color:#3d5a66; user-select:none;
  }
  #footer a{ color:#5fd4e8; text-decoration:none; }
  .hidden{ display:none !important; }
</style>
</head>
<body>
<div id="wrap">
  <canvas id="c" width="900" height="600"></canvas>

  <div id="hud">
    <div><span class="label">CORES </span><span class="val" id="hCores">0</span></div>
    <div><span class="label">TIME </span><span class="val" id="hTime">0.0s</span></div>
    <div><span class="label">BEST </span><span class="val" id="hBest">0</span></div>
  </div>

  <div id="overlay">
    <h1>GRAVITY DRIFT</h1>
    <p>
      Pilot the drone through a field of rotating gravity wells.
      Slingshot around them to collect energy cores — but drift too close
      and the pull will crush you. No fixed path. No safe loop. Just physics.
    </p>
    <div class="big">MOUSE / TOUCH to steer &nbsp;•&nbsp; hold to boost thrust</div>
    <button id="startBtn">LAUNCH</button>
  </div>

  <div id="deathOverlay" class="hidden" style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(3,3,12,0.88);text-align:center;">
    <div style="font-size:13px;letter-spacing:4px;color:#ff3df0;margin-bottom:6px;">SIGNAL LOST</div>
    <div class="score" id="finalScore">0</div>
    <div style="font-size:13px;color:#a9c7d8;margin-bottom:20px;" id="newBestMsg"></div>
    <button id="retryBtn">RE-LAUNCH</button>
  </div>

  <div id="footer">GRAVITY DRIFT — an original game by <a href="https://github.com/Mohak-Mittal" target="_blank">Mohak Mittal</a></div>
</div>

<script>
(() => {
  const canvas = document.getElementById('c');
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;

  const overlay = document.getElementById('overlay');
  const deathOverlay = document.getElementById('deathOverlay');
  const startBtn = document.getElementById('startBtn');
  const retryBtn = document.getElementById('retryBtn');
  const hCores = document.getElementById('hCores');
  const hTime = document.getElementById('hTime');
  const hBest = document.getElementById('hBest');
  const finalScore = document.getElementById('finalScore');
  const newBestMsg = document.getElementById('newBestMsg');

  let best = Number(localStorage.getItem('gravityDriftBest') || 0);
  hBest.textContent = best;

  let running = false;
  let mouse = { x: W/2, y: H/2, down: false };
  let ship, wells, cores, particles, startTime, cores_collected, animId;

  function resetGame() {
    ship = {
      x: W/2, y: H - 80,
      vx: 0, vy: 0,
      radius: 7,
      trail: []
    };
    wells = [];
    const wellCount = 3;
    for (let i = 0; i < wellCount; i++) {
      wells.push({
        x: 150 + Math.random() * (W - 300),
        y: 120 + Math.random() * (H - 300),
        mass: 1800 + Math.random() * 1200,
        radius: 18 + Math.random() * 10,
        hue: 180 + i * 45,
        orbitAngle: Math.random() * Math.PI * 2,
        orbitSpeed: (Math.random() - 0.5) * 0.006,
        orbitRadius: 0
      });
    }
    cores = [];
    spawnCore();
    particles = [];
    cores_collected = 0;
    startTime = performance.now();
  }

  function spawnCore() {
    let x, y, tooClose;
    do {
      x = 60 + Math.random() * (W - 120);
      y = 60 + Math.random() * (H - 120);
      tooClose = wells.some(w => Math.hypot(w.x - x, w.y - y) < w.radius + 60);
    } while (tooClose);
    cores.push({ x, y, radius: 8, pulse: Math.random() * Math.PI * 2 });
  }

  function addBurst(x, y, color, n = 18) {
    for (let i = 0; i < n; i++) {
      const a = Math.random() * Math.PI * 2;
      const s = 1 + Math.random() * 4;
      particles.push({
        x, y,
        vx: Math.cos(a) * s, vy: Math.sin(a) * s,
        life: 1, color
      });
    }
  }

  function update(dt) {
    const difficulty = 1 + cores_collected * 0.12;

    const dx = mouse.x - ship.x, dy = mouse.y - ship.y;
    const dist = Math.hypot(dx, dy) || 1;
    const thrust = mouse.down ? 0.55 : 0.28;
    ship.vx += (dx / dist) * thrust;
    ship.vy += (dy / dist) * thrust;

    for (const w of wells) {
      w.orbitAngle += w.orbitSpeed * difficulty * dt;
      w.x += Math.cos(w.orbitAngle) * 0.15 * difficulty;
      w.y += Math.sin(w.orbitAngle * 1.3) * 0.15 * difficulty;
      w.x = Math.max(60, Math.min(W - 60, w.x));
      w.y = Math.max(60, Math.min(H - 60, w.y));

      const wdx = w.x - ship.x, wdy = w.y - ship.y;
      const wdist = Math.hypot(wdx, wdy) || 1;
      const force = (w.mass * difficulty) / (wdist * wdist);
      ship.vx += (wdx / wdist) * force * dt * 0.06;
      ship.vy += (wdy / wdist) * force * dt * 0.06;

      if (wdist < w.radius + ship.radius) {
        return 'dead';
      }
    }

    ship.vx *= 0.985;
    ship.vy *= 0.985;

    ship.x += ship.vx * dt;
    ship.y += ship.vy * dt;

    if (ship.x < ship.radius) { ship.x = ship.radius; ship.vx *= -0.6; }
    if (ship.x > W - ship.radius) { ship.x = W - ship.radius; ship.vx *= -0.6; }
    if (ship.y < ship.radius) { ship.y = ship.radius; ship.vy *= -0.6; }
    if (ship.y > H - ship.radius) { ship.y = H - ship.radius; ship.vy *= -0.6; }

    ship.trail.push({ x: ship.x, y: ship.y });
    if (ship.trail.length > 26) ship.trail.shift();

    for (let i = cores.length - 1; i >= 0; i--) {
      const c = cores[i];
      c.pulse += 0.08 * dt;
      const cd = Math.hypot(c.x - ship.x, c.y - ship.y);
      if (cd < c.radius + ship.radius + 4) {
        addBurst(c.x, c.y, '255,204,51', 24);
        cores.splice(i, 1);
        cores_collected++;
        spawnCore();
        if (cores_collected % 4 === 0 && wells.length < 6) {
          wells.push({
            x: 150 + Math.random() * (W - 300),
            y: 120 + Math.random() * (H - 300),
            mass: 1800 + Math.random() * 800,
            radius: 16 + Math.random() * 8,
            hue: 180 + Math.random() * 180,
            orbitAngle: Math.random() * Math.PI * 2,
            orbitSpeed: (Math.random() - 0.5) * 0.006
          });
        }
      }
    }

    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.x += p.vx; p.y += p.vy;
      p.vx *= 0.94; p.vy *= 0.94;
      p.life -= 0.02 * dt;
      if (p.life <= 0) particles.splice(i, 1);
    }

    return 'ok';
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    ctx.fillStyle = 'rgba(255,255,255,0.4)';
    for (let i = 0; i < 60; i++) {
      const sx = (i * 137.5) % W;
      const sy = (i * 91.3 + 40) % H;
      ctx.globalAlpha = 0.15 + (Math.sin(performance.now()/900 + i) + 1) * 0.15;
      ctx.fillRect(sx, sy, 1.4, 1.4);
    }
    ctx.globalAlpha = 1;

    for (const w of wells) {
      const grd = ctx.createRadialGradient(w.x, w.y, 0, w.x, w.y, w.radius * 6);
      grd.addColorStop(0, `hsla(${w.hue}, 100%, 60%, 0.35)`);
      grd.addColorStop(1, 'transparent');
      ctx.fillStyle = grd;
      ctx.beginPath();
      ctx.arc(w.x, w.y, w.radius * 6, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.arc(w.x, w.y, w.radius, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${w.hue}, 90%, 55%)`;
      ctx.shadowColor = `hsl(${w.hue}, 100%, 60%)`;
      ctx.shadowBlur = 20;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    for (const c of cores) {
      const pulse = 1 + Math.sin(c.pulse) * 0.25;
      ctx.beginPath();
      ctx.arc(c.x, c.y, c.radius * pulse, 0, Math.PI * 2);
      ctx.fillStyle = '#ffcc33';
      ctx.shadowColor = '#ffcc33';
      ctx.shadowBlur = 18;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    for (const p of particles) {
      ctx.globalAlpha = Math.max(p.life, 0);
      ctx.fillStyle = `rgb(${p.color})`;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2.4, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    for (let i = 0; i < ship.trail.length; i++) {
      const t = ship.trail[i];
      ctx.globalAlpha = (i / ship.trail.length) * 0.5;
      ctx.fillStyle = '#00f0ff';
      ctx.beginPath();
      ctx.arc(t.x, t.y, 2.4, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    ctx.beginPath();
    ctx.arc(ship.x, ship.y, ship.radius, 0, Math.PI * 2);
    ctx.fillStyle = '#eafffe';
    ctx.shadowColor = '#00f0ff';
    ctx.shadowBlur = 16;
    ctx.fill();
    ctx.shadowBlur = 0;
  }

  let lastTime = performance.now();
  function loop(now) {
    if (!running) return;
    const dt = Math.min((now - lastTime) / 16.67, 2.2);
    lastTime = now;

    const state = update(dt);
    draw();

    hCores.textContent = cores_collected;
    hTime.textContent = ((now - startTime) / 1000).toFixed(1) + 's';

    if (state === 'dead') {
      endGame();
      return;
    }
    animId = requestAnimationFrame(loop);
  }

  function endGame() {
    running = false;
    addBurst(ship.x, ship.y, '255,61,240', 40);
    draw();
    const score = cores_collected * 100 + Math.floor((performance.now() - startTime) / 100);
    finalScore.textContent = score;
    if (score > best) {
      best = score;
      localStorage.setItem('gravityDriftBest', best);
      hBest.textContent = best;
      newBestMsg.textContent = '★ NEW BEST ★';
    } else {
      newBestMsg.textContent = '';
    }
    deathOverlay.classList.remove('hidden');
  }

  function startGame() {
    overlay.classList.add('hidden');
    deathOverlay.classList.add('hidden');
    resetGame();
    running = true;
    lastTime = performance.now();
    animId = requestAnimationFrame(loop);
  }

  canvas.addEventListener('mousemove', e => {
    const r = canvas.getBoundingClientRect();
    mouse.x = (e.clientX - r.left) * (W / r.width);
    mouse.y = (e.clientY - r.top) * (H / r.height);
  });
  canvas.addEventListener('mousedown', () => mouse.down = true);
  canvas.addEventListener('mouseup', () => mouse.down = false);
  canvas.addEventListener('touchmove', e => {
    e.preventDefault();
    const t = e.touches[0];
    const r = canvas.getBoundingClientRect();
    mouse.x = (t.clientX - r.left) * (W / r.width);
    mouse.y = (t.clientY - r.top) * (H / r.height);
    mouse.down = true;
  }, { passive: false });
  canvas.addEventListener('touchend', () => mouse.down = false);

  startBtn.addEventListener('click', startGame);
  retryBtn.addEventListener('click', startGame);
})();
</script>
</body>
</html>
```

</details>

<sub>💡 To make it live: paste the code above into a file named `index.html`, push it to a new repo, enable **GitHub Pages** in that repo's settings, and you'll have a shareable link in under a minute.</sub>

<br/>

## 🧭 About

I'm a BCA student (6th semester, S.D. College Barnala, affiliated with Punjabi University, Patiala) from Barnala, Punjab — and a self-taught game developer and 3D artist working toward founding my own game studio. I spend most of my time in **Unreal Engine 5** and **Blender**, and I build the tools and systems around my games myself: backends, voice assistants, productivity apps, whatever the project needs.

- 🎮 Deepening **C++** specifically for game development
- 🧠 Comfortable across **C, C++, HTML, CSS, Java, Python** — self-taught, medium-to-strong depth
- ☁️ Ship full-stack side projects on **Cloudflare Workers**
- 🎯 Long game: my own studio, shipping original titles

<br/>

## 🛠️ Built with

<div align="center">

<img src="https://img.shields.io/badge/Unreal_Engine_5-0E1128?style=for-the-badge&logo=unrealengine&logoColor=white" />
<img src="https://img.shields.io/badge/Blender-F5792A?style=for-the-badge&logo=blender&logoColor=white" />
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white" />
<img src="https://img.shields.io/badge/Cloudflare_Workers-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />

</div>

<br/>

## 🚀 Projects

<table>
<tr>
<td width="50%" valign="top">

### 🌌 VOID RIFT
Top-down roguelite shooter — the culmination of a series of web games I built to level up my combat and enemy-AI systems.
- Six distinct enemy AI types
- Full ability + XP/leveling system
- Ten escalating difficulty waves
- WASD + mouse controls

`JavaScript` `Canvas` `Game AI`

</td>
<td width="50%" valign="top">

### ⚔️ Solo Leveling RPG Tracker
A Solo Leveling–inspired productivity app that turns your real tasks into idle dungeon combat — canonical character roster, E-through-Monarch ranking, equip slots.
- Idle dungeon combat loop
- Canonical Solo Leveling character store
- 3D-rendered UI elements

`Three.js` `Vanilla JS` `localStorage`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💪 FitForge
An AI fitness web app that builds vegetarian meal plans, tracks streaks, and scales difficulty as you progress — 20 achievements to unlock.
- AI-generated meal planning via Groq
- Streak tracking + progressive difficulty
- 20-achievement system

`Cloudflare Workers` `Groq API` `JavaScript`

</td>
<td width="50%" valign="top">

### 🧰 ToolZone
A free online tools platform, still growing — percentage, discount, and GST calculators live, more on the way, built with a modular per-tool file structure so new tools drop in clean.

`JavaScript` `Modular Architecture`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎨 Portfolio + ARIA
My personal site — dark neon cyberpunk aesthetic, UE5/Blender showcases, and **ARIA**: a full-screen HUD voice assistant (JARVIS/Friday-style) with radar sweeps and a Groq-powered Llama backend that actually knows my portfolio content.
- Full-screen HUD: radar rings, conic sweep, hex grid
- Groq Llama backend via Cloudflare Worker
- Web Speech API with local-voice prioritization

`Cloudflare Workers` `Groq` `Web Speech API`

</td>
<td width="50%" valign="top">

### 🤖 Jarvis PC Assistant
A Python voice assistant that controls my PC by voice — modular by design, with dedicated modules for listening, reasoning, speech, and system control.
- `listener.py` → `brain.py` → `speaker.py` → `system.py`
- Custom file indexer for fast local lookup

`Python` `Voice Control` `Automation`

</td>
</tr>
</table>

<br/>

## 📊 GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Mohak-Mittal&show_icons=true&theme=radical&hide_border=true&bg_color=0b0b1e&title_color=00f0ff&icon_color=ff3df0&text_color=e6f7ff" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mohak-Mittal&layout=compact&theme=radical&hide_border=true&bg_color=0b0b1e&title_color=00f0ff&text_color=e6f7ff" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Mohak-Mittal&theme=radical&hide_border=true&background=0b0b1e&ring=00f0ff&fire=ff3df0&currStreakLabel=00f0ff" />

</div>

<br/>

## 📡 Connect

<div align="center">

<a href="https://mohak-mittal.github.io/Portfolio" target="_blank"><img src="https://img.shields.io/badge/Portfolio-00f0ff?style=for-the-badge&logo=googlechrome&logoColor=black" /></a>
<!-- add your real handles below -->
<a href="#"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="#"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="mailto:you@example.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>

</div>

<br/>

<div align="center">
<sub>🎮 Currently deepening C++ for game dev · Building toward my own studio, one system at a time.</sub>
</div>
