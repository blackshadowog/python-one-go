import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)
start = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    seconds = (pygame.time.get_ticks()-start)//1000
    screen.fill((20,25,40))
    text = font.render(f"{seconds:02}", True, (100,220,255))
    screen.blit(text, text.get_rect(center=(400,250)))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
