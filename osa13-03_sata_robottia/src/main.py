# TEE RATKAISUSI TÄHÄN:
import pygame
 
pygame.init()
naytto = pygame.display.set_mode((640, 480))
 
robo = pygame.image.load("robo.png")
 
naytto.fill((0, 0, 0))
for i in range(10):
    for j in range(10):
        naytto.blit(robo, (20+10*i+40*j, 100+i*20))
pygame.display.flip()
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
# TEE RATKAISUSI TÄHÄN:ö