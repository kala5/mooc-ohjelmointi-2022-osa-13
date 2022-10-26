# TEE RATKAISUSI TÄHÄN:
# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint
 
pygame.init()
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))
 
robo = pygame.image.load("robo.png")
 
x = randint(0,leveys-robo.get_width())
y = randint(0,korkeus-robo.get_height())

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN :
            print("painoit nappia kohdassa", tapahtuma.pos, "ja robon koordinaatit olivat", x,y)
            range1 = range(x, x+robo.get_width())
            range2 = range(y, y+robo.get_height())
            
            if tapahtuma.pos[0] in range1 and tapahtuma.pos[1] in range2:
                x = randint(0,leveys-robo.get_width())
                y = randint(0,korkeus-robo.get_height())
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x,y))
    pygame.display.flip()