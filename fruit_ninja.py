"""
Fruit Ninja — Hand-Tracked Edition
Controls : Index finger via webcam (MediaPipe)
Stack    : Python • Pygame-CE • OpenCV • MediaPipe • NumPy
"""

import pygame
import cv2
import mediapipe as mp
import numpy as np
import threading
import random
import math
import time
import sys
from collections import deque

# ─── CONFIG ────────────────────────────────────────────────────────────────────
WIDTH, HEIGHT   = 1280, 720
FPS             = 60
TRAIL_LEN       = 22
GRAVITY         = 0.28
FRUIT_SPEED_MIN = 9
FRUIT_SPEED_MAX = 14
SPAWN_INTERVAL  = 1.3      # seconds between waves
MAX_MISSES      = 5
SLICE_SPEED_MIN = 8        # min finger px/frame to register a slice
FONT_PATH       = None     # use pygame default

# Fruit palette  (name, body_color, seed_color, highlight)
FRUIT_DATA = [
    ("Watermelon", (60,179,60),   (20,100,20),   (100,230,100)),
    ("Orange",     (255,160,30),  (200,100,10),  (255,210,80)),
    ("Apple",      (220,30,30),   (180,20,20),   (255,100,100)),
    ("Mango",      (255,200,0),   (210,140,0),   (255,240,100)),
    ("Kiwi",       (100,170,60),  (50,100,20),   (160,220,100)),
    ("Strawberry", (220,40,60),   (160,10,30),   (255,120,140)),
    ("Grape",      (130,50,190),  (80,20,140),   (200,130,255)),
    ("Lemon",      (255,240,40),  (200,180,0),   (255,255,150)),
]

BOMB_COLOR    = (30, 30, 30)
BOMB_FUSE_COL = (255, 200, 0)

# ─── PROCEDURAL AUDIO ──────────────────────────────────────────────────────────
def make_slice_sound(freq=440, duration=0.08, sample_rate=22050):
    frames = int(sample_rate * duration)
    t = np.linspace(0, duration, frames, False)
    wave = np.sin(2 * np.pi * freq * t) * np.exp(-t * 30)
    wave = (wave * 32767).astype(np.int16)
    stereo = np.column_stack([wave, wave])
    return pygame.sndarray.make_sound(stereo)

def make_bomb_sound(sample_rate=22050):
    duration = 0.3
    frames = int(sample_rate * duration)
    t = np.linspace(0, duration, frames, False)
    wave = np.random.uniform(-1, 1, frames) * np.exp(-t * 8)
    low  = np.sin(2 * np.pi * 80 * t) * np.exp(-t * 5) * 0.6
    wave = (wave + low) * 32767 * 0.5
    wave = wave.clip(-32767, 32767).astype(np.int16)
    stereo = np.column_stack([wave, wave])
    return pygame.sndarray.make_sound(stereo)

def make_miss_sound(sample_rate=22050):
    duration = 0.15
    frames = int(sample_rate * duration)
    t = np.linspace(0, duration, frames, False)
    freq_sweep = np.linspace(300, 100, frames)
    wave = np.sin(2 * np.pi * freq_sweep * t / sample_rate * np.arange(frames))
    wave = (wave * 32767 * np.exp(-t * 10)).astype(np.int16)
    stereo = np.column_stack([wave, wave])
    return pygame.sndarray.make_sound(stereo)

# ─── HAND TRACKER (threaded) ───────────────────────────────────────────────────
class HandTracker:
    def __init__(self):
        self.mp_hands   = mp.solutions.hands
        self.hands      = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
        )
        self.cap         = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

        self.finger_pos  = None   # (x, y) in game coords
        self.lock        = threading.Lock()
        self._running    = True
        self._thread     = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _run(self):
        while self._running:
            ret, frame = self.cap.read()
            if not ret:
                continue
            frame = cv2.flip(frame, 1)
            rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res   = self.hands.process(rgb)
            pos   = None
            if res.multi_hand_landmarks:
                lm = res.multi_hand_landmarks[0].landmark[8]  # index fingertip
                pos = (int(lm.x * WIDTH), int(lm.y * HEIGHT))
            with self.lock:
                self.finger_pos = pos

    def get_pos(self):
        with self.lock:
            return self.finger_pos

    def stop(self):
        self._running = False
        self.cap.release()

# ─── PARTICLES ─────────────────────────────────────────────────────────────────
class Particle:
    __slots__ = ["x","y","vx","vy","life","max_life","color","size"]
    def __init__(self, x, y, color):
        self.x = x + random.uniform(-6, 6)
        self.y = y + random.uniform(-6, 6)
        angle  = random.uniform(0, 2*math.pi)
        speed  = random.uniform(2, 9)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = self.max_life = random.randint(20, 45)
        self.color = color
        self.size   = random.randint(3, 9)

    def update(self):
        self.x  += self.vx
        self.y  += self.vy
        self.vy += 0.3
        self.vx *= 0.97
        self.life -= 1

    def draw(self, surf):
        alpha = self.life / self.max_life
        r, g, b = self.color
        col = (int(r*alpha), int(g*alpha), int(b*alpha))
        s   = max(1, int(self.size * alpha))
        pygame.draw.circle(surf, col, (int(self.x), int(self.y)), s)

# ─── SCORE POP ─────────────────────────────────────────────────────────────────
class ScorePop:
    def __init__(self, x, y, text, color, font):
        self.x = x; self.y = y
        self.text  = text
        self.color = color
        self.font  = font
        self.life  = self.max_life = 55
        self.vy    = -1.5

    def update(self):
        self.y    += self.vy
        self.life -= 1

    def draw(self, surf):
        alpha = self.life / self.max_life
        col   = tuple(int(c * alpha) for c in self.color)
        img   = self.font.render(self.text, True, col)
        surf.blit(img, (self.x - img.get_width()//2, int(self.y)))

# ─── FRUIT ─────────────────────────────────────────────────────────────────────
class Fruit:
    def __init__(self):
        self.data   = random.choice(FRUIT_DATA)
        self.name, self.color, self.seed_col, self.hi_col = self.data
        self.radius = random.randint(32, 50)
        self.x      = random.randint(self.radius, WIDTH - self.radius)
        self.y      = HEIGHT + self.radius
        angle       = random.uniform(math.pi*0.55, math.pi*0.95)
        speed       = random.uniform(FRUIT_SPEED_MIN, FRUIT_SPEED_MAX)
        self.vx     = math.cos(angle) * speed * random.choice([-1,1])
        self.vy     = -speed
        self.rot    = random.uniform(0, 360)
        self.rot_v  = random.uniform(-4, 4)
        self.sliced = False
        self.alive  = True
        # half-fruit drift after slice
        self.halves = []

    def update(self):
        if self.sliced:
            for h in self.halves:
                h[0] += h[2]
                h[1] += h[3]
                h[3] += GRAVITY * 1.2
                h[4] += h[5]
            return
        self.x   += self.vx
        self.y   += self.vy
        self.vy  += GRAVITY
        self.rot += self.rot_v
        if self.y > HEIGHT + self.radius + 50:
            self.alive = False

    def slice(self, angle=0):
        self.sliced = True
        # two halves diverge
        for sign in (-1, 1):
            self.halves.append([
                self.x, self.y,
                self.vx + math.cos(angle+math.pi/2)*sign*3,
                self.vy - 2,
                self.rot, self.rot_v * sign
            ])

    def is_gone(self):
        if not self.sliced:
            return not self.alive
        return all(h[1] > HEIGHT + 80 for h in self.halves)

    def draw(self, surf):
        if self.sliced:
            self._draw_halves(surf)
        else:
            self._draw_whole(surf, self.x, self.y, self.rot)

    def _draw_whole(self, surf, cx, cy, rot, alpha=255):
        r = self.radius
        # body
        pygame.draw.circle(surf, self.color, (int(cx), int(cy)), r)
        # highlight
        hx = int(cx - r * 0.3)
        hy = int(cy - r * 0.3)
        pygame.draw.circle(surf, self.hi_col, (hx, hy), max(3, r//3))
        # outline
        pygame.draw.circle(surf, (0,0,0), (int(cx), int(cy)), r, 2)

    def _draw_halves(self, surf):
        for h in self.halves:
            cx, cy, _, _, rot, _ = h
            if cy > HEIGHT + 60:
                continue
            r = self.radius
            # clip draw to a half-circle (simple: draw full then cover)
            tmp = pygame.Surface((r*2+4, r*2+4), pygame.SRCALPHA)
            pygame.draw.circle(tmp, (*self.color, 220), (r+2, r+2), r)
            pygame.draw.circle(tmp, (*self.hi_col, 180), (r//2+2, r//2+2), max(2, r//3))
            # inner flesh line
            pygame.draw.line(tmp, (*self.seed_col, 255), (2, r+2), (r*2+2, r+2), 3)
            rot_surf = pygame.transform.rotate(tmp, rot)
            rr = rot_surf.get_rect(center=(int(cx), int(cy)))
            surf.blit(rot_surf, rr)

# ─── BOMB ──────────────────────────────────────────────────────────────────────
class Bomb:
    def __init__(self):
        self.radius = 36
        self.x      = random.randint(self.radius, WIDTH - self.radius)
        self.y      = HEIGHT + self.radius
        angle       = random.uniform(math.pi*0.6, math.pi*0.9)
        speed       = random.uniform(FRUIT_SPEED_MIN, FRUIT_SPEED_MAX - 1)
        self.vx     = math.cos(angle) * speed * random.choice([-1,1])
        self.vy     = -speed
        self.rot    = 0
        self.rot_v  = random.uniform(-3, 3)
        self.alive  = True
        self.fuse_t = 0

    def update(self):
        self.x    += self.vx
        self.y    += self.vy
        self.vy   += GRAVITY
        self.rot  += self.rot_v
        self.fuse_t += 1
        if self.y > HEIGHT + self.radius + 50:
            self.alive = False

    def is_gone(self):
        return not self.alive

    def draw(self, surf):
        cx, cy, r = int(self.x), int(self.y), self.radius
        pygame.draw.circle(surf, BOMB_COLOR, (cx, cy), r)
        pygame.draw.circle(surf, (50,50,50), (cx, cy), r, 2)
        # fuse spark
        fuse_flicker = int(abs(math.sin(self.fuse_t * 0.4)) * 255)
        fuse_col = (255, fuse_flicker, 0)
        fx = int(cx + math.cos(math.radians(self.rot + 45)) * r)
        fy = int(cy - math.sin(math.radians(self.rot + 45)) * r)
        pygame.draw.line(surf, BOMB_FUSE_COL, (cx, cy - r), (fx, fy - 8), 3)
        pygame.draw.circle(surf, fuse_col, (fx, fy - 10), 5)
        # skull
        font_size = max(16, r - 8)
        # simple circle eyes
        ex, ey = cx - 7, cy - 4
        pygame.draw.circle(surf, (255,255,255), (ex, ey), 5)
        pygame.draw.circle(surf, (255,255,255), (ex+14, ey), 5)
        pygame.draw.circle(surf, (0,0,0), (ex+1, ey), 2)
        pygame.draw.circle(surf, (0,0,0), (ex+15, ey), 2)

# ─── BLADE TRAIL ───────────────────────────────────────────────────────────────
class BladeTrail:
    def __init__(self):
        self.points = deque(maxlen=TRAIL_LEN)

    def update(self, pos):
        if pos:
            self.points.append(pos)

    def draw(self, surf):
        pts = list(self.points)
        n   = len(pts)
        if n < 2:
            return
        for i in range(1, n):
            alpha = i / n
            w     = max(1, int(alpha * 8))
            r     = int(255 * alpha)
            g     = int(220 * alpha)
            b     = int(100 * (1 - alpha))
            try:
                pygame.draw.line(surf, (r, g, b), pts[i-1], pts[i], w)
            except Exception:
                pass

    def get_velocity(self):
        pts = list(self.points)
        if len(pts) < 3:
            return 0
        dx = pts[-1][0] - pts[-3][0]
        dy = pts[-1][1] - pts[-3][1]
        return math.hypot(dx, dy)

    def get_angle(self):
        pts = list(self.points)
        if len(pts) < 2:
            return 0
        dx = pts[-1][0] - pts[-2][0]
        dy = pts[-1][1] - pts[-2][1]
        return math.atan2(dy, dx)

# ─── SCREEN SHAKE ──────────────────────────────────────────────────────────────
class ScreenShake:
    def __init__(self):
        self.intensity = 0
        self.duration  = 0

    def trigger(self, intensity=8, duration=15):
        self.intensity = intensity
        self.duration  = duration

    def get_offset(self):
        if self.duration <= 0:
            return (0, 0)
        self.duration -= 1
        decay = self.duration / 15
        ox = random.randint(-int(self.intensity*decay), int(self.intensity*decay))
        oy = random.randint(-int(self.intensity*decay), int(self.intensity*decay))
        return (ox, oy)

# ─── BACKGROUND ────────────────────────────────────────────────────────────────
def draw_background(surf, t):
    # Animated deep-dark gradient
    top    = (10, 5, 25)
    bot    = (30, 10, 50)
    for y in range(HEIGHT):
        blend = y / HEIGHT
        r = int(top[0]*(1-blend) + bot[0]*blend)
        g = int(top[1]*(1-blend) + bot[1]*blend)
        b = int(top[2]*(1-blend) + bot[2]*blend)
        pygame.draw.line(surf, (r,g,b), (0,y), (WIDTH,y))
    # subtle pulse lines
    for i in range(0, WIDTH, 80):
        wave = int(math.sin(t * 0.04 + i * 0.05) * 3)
        col  = (40, 15, 70)
        pygame.draw.line(surf, col, (i+wave, 0), (i+wave, HEIGHT), 1)

# ─── HUD ───────────────────────────────────────────────────────────────────────
def draw_hud(surf, score, misses, combo, font_big, font_med, font_small):
    # Score
    score_txt = font_big.render(str(score), True, (255,255,255))
    surf.blit(score_txt, (WIDTH//2 - score_txt.get_width()//2, 12))

    # Misses (red ✕ marks)
    for i in range(MAX_MISSES):
        col = (220,30,30) if i < misses else (60,60,80)
        mx  = 20 + i * 36
        font_med.render("✕", True, col)
        t = font_med.render("✕", True, col)
        surf.blit(t, (mx, 14))

    # Combo
    if combo > 1:
        ctxt = font_med.render(f"✦ {combo}x COMBO ✦", True, (255,220,50))
        surf.blit(ctxt, (WIDTH - ctxt.get_width() - 20, 14))

    # Bottom bar
    pygame.draw.line(surf, (60,30,90), (0, HEIGHT-1), (WIDTH, HEIGHT-1), 2)

# ─── GAME OVER ─────────────────────────────────────────────────────────────────
def draw_game_over(surf, score, font_big, font_med):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,170))
    surf.blit(overlay, (0,0))

    t1 = font_big.render("GAME OVER", True, (220,30,30))
    t2 = font_med.render(f"Score: {score}", True, (255,255,255))
    t3 = font_med.render("Press  R  to restart   |   ESC to quit", True, (160,160,180))

    surf.blit(t1, (WIDTH//2 - t1.get_width()//2, HEIGHT//2 - 100))
    surf.blit(t2, (WIDTH//2 - t2.get_width()//2, HEIGHT//2 - 10))
    surf.blit(t3, (WIDTH//2 - t3.get_width()//2, HEIGHT//2 + 60))

# ─── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    pygame.init()
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("🍉 Fruit Ninja — Hand Tracked")
    clock  = pygame.time.Clock()

    # Fonts
    font_big   = pygame.font.SysFont("Arial", 52, bold=True)
    font_med   = pygame.font.SysFont("Arial", 32, bold=True)
    font_small = pygame.font.SysFont("Arial", 22)

    # Sounds
    slice_sounds = [make_slice_sound(f, 0.07) for f in [380, 440, 520, 600]]
    bomb_sound   = make_bomb_sound()
    miss_sound   = make_miss_sound()
    for s in slice_sounds: s.set_volume(0.35)
    bomb_sound.set_volume(0.6)
    miss_sound.set_volume(0.4)

    # Hand tracker
    print("[INFO] Initialising webcam + MediaPipe…")
    tracker = HandTracker()
    time.sleep(1.0)
    print("[INFO] Ready!")

    def reset_game():
        return dict(
            fruits    = [],
            particles = [],
            pops      = [],
            trail     = BladeTrail(),
            shake     = ScreenShake(),
            score     = 0,
            misses    = 0,
            combo     = 0,
            combo_t   = 0,
            game_over = False,
            t         = 0,
            last_spawn= time.time(),
        )

    G = reset_game()

    running = True
    while running:
        dt = clock.tick(FPS)
        G["t"] += 1

        # ── Events ──
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r and G["game_over"]:
                    G = reset_game()

        if G["game_over"]:
            draw_background(screen, G["t"])
            draw_game_over(screen, G["score"], font_big, font_med)
            pygame.display.flip()
            continue

        # ── Spawn fruits/bombs ──
        now = time.time()
        if now - G["last_spawn"] > SPAWN_INTERVAL:
            G["last_spawn"] = now
            wave = random.randint(1, 3)
            for _ in range(wave):
                if random.random() < 0.12:
                    G["fruits"].append(Bomb())
                else:
                    G["fruits"].append(Fruit())

        # ── Hand tracker → blade ──
        finger = tracker.get_pos()
        G["trail"].update(finger)

        vel   = G["trail"].get_velocity()
        angle = G["trail"].get_angle()
        is_slicing = vel > SLICE_SPEED_MIN and finger is not None

        # ── Combo decay ──
        if G["combo_t"] > 0:
            G["combo_t"] -= 1
        else:
            G["combo"] = 0

        # ── Check slices / misses ──
        for obj in G["fruits"]:
            if obj.is_gone():
                continue
            if isinstance(obj, Bomb):
                if is_slicing:
                    dx = finger[0] - obj.x
                    dy = finger[1] - obj.y
                    if math.hypot(dx, dy) < obj.radius + 6:
                        obj.alive = False
                        bomb_sound.play()
                        G["shake"].trigger(18, 25)
                        G["combo"] = 0
                        G["combo_t"] = 0
                        # big red particles
                        for _ in range(60):
                            p = Particle(obj.x, obj.y, (220, 30, 30))
                            p.size = random.randint(6, 16)
                            G["particles"].append(p)
                        G["misses"] += 2
                        G["pops"].append(ScorePop(int(obj.x), int(obj.y)-20,
                                                  "BOMB! -2", (255,80,80), font_med))
            else:
                if not obj.sliced:
                    # missed?
                    if obj.y > HEIGHT + 5 and obj.vy > 0:
                        G["misses"] += 1
                        miss_sound.play()
                        G["combo"] = 0
                        G["pops"].append(ScorePop(int(obj.x), HEIGHT-60,
                                                  "MISS!", (200,80,80), font_small))
                        obj.alive = False
                        continue
                    # sliced?
                    if is_slicing:
                        dx = finger[0] - obj.x
                        dy = finger[1] - obj.y
                        if math.hypot(dx, dy) < obj.radius + 8:
                            obj.slice(angle)
                            G["combo"] += 1
                            G["combo_t"] = 55
                            pts = 10 + (G["combo"] - 1) * 5
                            G["score"] += pts
                            random.choice(slice_sounds).play()
                            G["shake"].trigger(4, 8)
                            # juice particles
                            for _ in range(30):
                                G["particles"].append(Particle(obj.x, obj.y, obj.color))
                            for _ in range(8):
                                G["particles"].append(Particle(obj.x, obj.y, obj.hi_col))
                            label = f"+{pts}" + (" 🔥" if G["combo"] > 2 else "")
                            G["pops"].append(ScorePop(int(obj.x), int(obj.y)-20,
                                                      label, (255,240,80), font_med))

        # Check game over
        if G["misses"] >= MAX_MISSES:
            G["game_over"] = True

        # Remove gone objects
        G["fruits"]    = [f for f in G["fruits"]    if not f.is_gone()]
        G["particles"] = [p for p in G["particles"] if p.life > 0]
        G["pops"]      = [p for p in G["pops"]      if p.life > 0]

        # ── Update ──
        for f in G["fruits"]:    f.update()
        for p in G["particles"]: p.update()
        for p in G["pops"]:      p.update()

        # ── Draw ──
        draw_background(screen, G["t"])

        ox, oy = G["shake"].get_offset()
        game_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        for f in G["fruits"]:    f.draw(game_surf)
        for p in G["particles"]: p.draw(game_surf)
        G["trail"].draw(game_surf)

        # Finger cursor
        if finger:
            pygame.draw.circle(game_surf, (255,255,255), finger, 8, 2)
            if is_slicing:
                pygame.draw.circle(game_surf, (255,240,80), finger, 14, 2)

        screen.blit(game_surf, (ox, oy))
        for p in G["pops"]: p.draw(screen)

        draw_hud(screen, G["score"], G["misses"], G["combo"],
                 font_big, font_med, font_small)

        pygame.display.flip()

    tracker.stop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
