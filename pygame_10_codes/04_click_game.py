import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
target = pygame.Rect(100, 100, 60, 60)
score = 0
font = pygame.font.Font(None, 42)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and target.collidepoint(event.pos):
            score += 1
            target.topleft = (random.randint(0, 740), random.randint(70, 440))
    screen.fill((18, 18, 28))
    pygame.draw.rect(screen, (255, 90, 100), target, border_radius=12)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
