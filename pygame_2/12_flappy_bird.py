import pygame
pygame.init()
screen=pygame.display.set_mode((800,500))
clock=pygame.time.Clock()
font=pygame.font.Font(None,50)
running=True
x,y=400,250
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    x+=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*5
    y+=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*5
    x=max(20,min(780,x)); y=max(20,min(480,y))
    screen.fill((20,20,30))
    pygame.draw.circle(screen,(80,200,255),(x,y),30)
    screen.blit(font.render("PROJECT 12: Flappy Bird",True,"white"),(20,20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
