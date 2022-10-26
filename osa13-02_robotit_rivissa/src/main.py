# TEE RATKAISUSI TÄHÄN:
import pygame
 
pygame.init()
naytto = pygame.display.set_mode((640, 480))
 
robo = pygame.image.load("robo.png")
 
naytto.fill((0, 0, 0))
for i in range(10):
    naytto.blit(robo, (50+50*i, 100))
pygame.display.flip()
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
# TEE RATKAISUSI TÄHÄN: