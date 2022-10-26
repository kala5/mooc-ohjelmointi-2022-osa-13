import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
nopeus = 1
nopeus = 1
kello = pygame.time.Clock()

määrä = 20

robo_sijainnit = []

while len(robo_sijainnit) < määrä: # lisäätään aluksi määrä verran robotteja
    robo_sijainnit.append([random.randint(0,640-robo.get_width()), random.randint(-800,-50)])


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))

    if len(robo_sijainnit) < määrä:
        robo_sijainnit.append([random.randint(0,640-robo.get_width()), random.randint(-425,-50)])

    for sijainti in robo_sijainnit:
        if nopeus > 0 and sijainti[1]+robo.get_height() >= 480:
            if sijainti[0] < 320:
                sijainti[0] += -nopeus
            else:
                sijainti[0] += nopeus
            naytto.blit(robo, (sijainti[0], sijainti[1]))
        else:
            sijainti[1] += nopeus
            naytto.blit(robo, (sijainti[0], sijainti[1]))

        if sijainti[0] <= 0-robo.get_width() or sijainti[0] >= 640+robo.get_width():
            robo_sijainnit.remove(sijainti)
        
    pygame.display.flip()

    kello.tick(120)