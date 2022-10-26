# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
x = 0
y = 480-robo.get_height()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:

            if tapahtuma.key == pygame.K_LEFT and x > 0:
                x -= 10
            if tapahtuma.key == pygame.K_RIGHT and x < 640-robo.get_width():
                x += 10
            if tapahtuma.key == pygame.K_UP and y > 0:
                y -= 10
                print(y+robo.get_height())
            if tapahtuma.key == pygame.K_DOWN and y < 480-robo.get_height():
                y += 10
            

        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()