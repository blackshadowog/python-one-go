import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
x, y = 100, 250
vx = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += vx
    if x <= 25 or x >= 775:
        vx *= -1
    screen.fill((20, 30, 45))
    pygame.draw.circle(screen, (255, 80, 80), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
