import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
player = pygame.Rect(380, 430, 40, 30)
bullets = []
speed = 6
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(pygame.Rect(player.centerx-3, player.top-10, 6, 12))
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*speed
    player.clamp_ip(screen.get_rect())
    for b in bullets[:]:
        b.y -= 9
        if b.bottom < 0: bullets.remove(b)
    screen.fill((5, 5, 20))
    pygame.draw.rect(screen, (70, 180, 255), player)
    for b in bullets: pygame.draw.rect(screen, (255, 240, 80), b)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
