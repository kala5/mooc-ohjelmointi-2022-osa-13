import pygame 

 
 

pygame.init() 

naytto = pygame.display.set_mode((640, 480)) 

 
 

robo = pygame.image.load("robo.png") 

 
 

x = 0 

y = 0 

nopeus = 1 

kello = pygame.time.Clock() 

 
 

sivulle = True 

 
 

while True: 

    for tapahtuma in pygame.event.get(): 

        if tapahtuma.type == pygame.QUIT: 

            exit() 

 
 

    naytto.fill((0, 0, 0)) 

    naytto.blit(robo, (x, y)) 

    pygame.display.flip() 

 
 

    if sivulle: 

        x += nopeus 

    else:  

        y += nopeus 

 
 

    if nopeus > 0 and x+robo.get_width() >= 640: # 1. kulma 

        sivulle = False 

 
 

    if nopeus > 0 and y+robo.get_height() >= 480: # 2. kulma 

        nopeus = -nopeus 

        sivulle = True 

 
 

    if nopeus < 0 and x <= 0: # 3. kulma 

        sivulle = False 

 
 

    if nopeus < 0 and y <= 0: # alku / 4. kulma 

        sivulle = True 

        nopeus = -nopeus 

 
 

    kello.tick(250) 

 