import pygame, random
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
snake = [(300,300),(280,300),(260,300)]
direction = (20,0)
food = (random.randrange(0,600,20), random.randrange(0,600,20))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            keys = {pygame.K_UP:(0,-20), pygame.K_DOWN:(0,20),
                    pygame.K_LEFT:(-20,0), pygame.K_RIGHT:(20,0)}
            if event.key in keys: direction = keys[event.key]
    head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
    if not (0 <= head[0] < 600 and 0 <= head[1] < 600) or head in snake:
        snake = [(300,300),(280,300),(260,300)]
        direction = (20,0)
    else:
        snake.insert(0, head)
        if head == food:
            food = (random.randrange(0,600,20), random.randrange(0,600,20))
        else: snake.pop()
    screen.fill((10,35,15))
    for part in snake: pygame.draw.rect(screen, (80,220,100), (*part,18,18))
    pygame.draw.rect(screen, (230,70,70), (*food,18,18))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
