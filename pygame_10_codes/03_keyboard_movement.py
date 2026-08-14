import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
player = pygame.Rect(380, 230, 40, 40)
speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    player.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
    player.clamp_ip(screen.get_rect())
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (80, 180, 255), player)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
