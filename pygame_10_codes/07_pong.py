import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
ball = pygame.Rect(390, 240, 20, 20)
left = pygame.Rect(30, 200, 15, 100)
right = pygame.Rect(755, 200, 15, 100)
vx, vy = 5, 4
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    keys = pygame.key.get_pressed()
    left.y += (keys[pygame.K_s]-keys[pygame.K_w])*6
    right.y += (keys[pygame.K_DOWN]-keys[pygame.K_UP])*6
    left.clamp_ip(screen.get_rect()); right.clamp_ip(screen.get_rect())
    ball.x += vx; ball.y += vy
    if ball.top <= 0 or ball.bottom >= 500: vy *= -1
    if ball.colliderect(left) or ball.colliderect(right): vx *= -1
    if ball.left < 0 or ball.right > 800: ball.center = (400,250); vx *= -1
    screen.fill((15,15,15))
    pygame.draw.rect(screen, (255,255,255), left)
    pygame.draw.rect(screen, (255,255,255), right)
    pygame.draw.ellipse(screen, (255,100,100), ball)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
