# Tämän osan tehtävissä ei ole automaattisia testejä, vaan testi antaa pisteet
# automaattisesti, kun lähetät ratkaisun palvelimelle. Lähetä ratkaisu vasta
# sitten, kun se on valmis ja vastaa tehtävänannon vaatimuksia. Vaikka tehtävissä
# ei ole testejä, kurssin henkilökunta näkee lähetetyt ratkaisut.

# TEE RATKAISUSI TÄHÄN:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
leveys = naytto.get_width() - robo.get_width()
korkeus = naytto.get_height() - robo.get_height()
naytto.blit(robo, (0,0))
naytto.blit(robo, (leveys, 0))
naytto.blit(robo, (0, korkeus))
naytto.blit(robo, (leveys, korkeus))
pygame.display.flip()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()