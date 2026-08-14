import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
rect = pygame.Rect(100, 100, 50, 50)
dx, dy = 5, 4
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect.x += dx
    rect.y += dy
    if rect.left <= 0 or rect.right >= 800: dx *= -1
    if rect.top <= 0 or rect.bottom >= 500: dy *= -1
    screen.fill((35, 20, 45))
    pygame.draw.rect(screen, (100, 255, 150), rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
