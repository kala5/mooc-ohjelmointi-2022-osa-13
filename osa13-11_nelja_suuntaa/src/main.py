import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
x = 0
y = 480-robo.get_height()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                x -= 10
            if tapahtuma.key == pygame.K_RIGHT:
                x += 10
            if tapahtuma.key == pygame.K_UP:
                y -= 10
            if tapahtuma.key == pygame.K_DOWN:
                y += 10

        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()