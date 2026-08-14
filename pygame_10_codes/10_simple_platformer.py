import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
player = pygame.Rect(100, 400, 40, 50)
platforms = [pygame.Rect(0, 450, 800, 50), pygame.Rect(250, 350, 180, 20), pygame.Rect(550, 270, 150, 20)]
vy = 0
on_ground = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and on_ground:
            vy = -12
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*5
    vy += 0.5
    player.y += int(vy)
    on_ground = False
    for p in platforms:
        if player.colliderect(p) and vy >= 0:
            player.bottom = p.top
            vy = 0
            on_ground = True
    player.clamp_ip(screen.get_rect())
    screen.fill((40,60,100))
    for p in platforms: pygame.draw.rect(screen, (120,90,60), p)
    pygame.draw.rect(screen, (255,200,80), player)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
