import pygame
import enemes
import tank
import bullets
import time
import random
import settings

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((800 , 500))
fps = pygame.time.Clock()

fon = pygame.image.load(settings.fon_texture)
fon = pygame.transform.scale(fon , (800 , 500))
fonlose = pygame.image.load(settings.lose_texture)
fonlose = pygame.transform.scale(fonlose , (800 , 500))
fonwin = pygame.image.load(settings.win_texture)
fonwin = pygame.transform.scale(fonwin , (800 , 500))
#bomtexture = pygame.image.load(settings.boom_texture)
#bomtexture = pygame.transform.scale(bomtexture , (100 , 100))

pygame.mixer.music.load(settings.musick)
shootsound = pygame.mixer.Sound(settings.fire_sound)
bomsound = pygame.mixer.Sound(settings.bom_sound)
winsound = pygame.mixer.Sound(settings.win_sound)
losesound = pygame.mixer.Sound(settings.lose_sound)

islose = False
iswin = False
lichbul = -1
bullsit = []
enmylist = []
fixtime1 = time.time()
fixtime2 = time.time()

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(settings.musik_volume)

rocket = tank.Tank(300 , 400 , 100 , 100 , settings.rocket_texture , settings.player_speed)

for i in range(settings.asteroid_count):
    enmylist.append(enemes.Enemy(random.randint(0 , 750) , random.randint(-100 * settings.asteroid_count , 0) , settings.asteroid_size , settings.asteroid_size ,  settings.mateor_texture , settings.asteroid_speed))

game = True
while game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    rocket.move()
    rocket.shoot()
    #print(rocket.shoot())
    if rocket.shoot() == True:
        if time.time() - fixtime1 > 0.5:
            fixtime1 = time.time()
            shootsound.play()
            bullsit.append(bullets.Bullshit(rocket.hitbox.x + 45 , rocket.hitbox.y , 15 , 30 , settings.bull_texture , settings.bull_speed))

    for enemy1 in enmylist:
        if rocket.hitbox.colliderect(enemy1.hitbox):
            #game = False
            #pygame.quit()
            islose = True
            losesound.play()
            shootsound.set_volume(0)
            bomsound.set_volume(0)
            rocket.hitbox.x = 10000
            rocket.hitbox.y = 10000
            pygame.mixer.music.stop()
            #losesound.play()
            pygame.mixer.quit()

    for colbul in bullsit:
        lichbul +=1
        lich  = -1
        for colenem in enmylist:
            lich += 1
            if colbul.hitbox.colliderect(colenem.hitbox):
                enmylist.pop(lich)
                bullsit.pop(lichbul)
    lichbul = -1

    for item in bullsit:
        if item.hitbox.y < 0:
            bullsit.pop(0)

    if time.time() - fixtime2 > settings.asteroid_count :
        iswin = True
        shootsound.set_volume(0)
        pygame.mixer.music.stop()
        if time.time() - fixtime2 < settings.asteroid_count + 0.02:
            winsound.play()
        #winsound.play()
        pygame.mixer.quit()

    window.fill((255, 0, 0))
    window.blit(fon , [0 , 0])
    rocket.render(window)

    for enemy in enmylist:
        enemy.move()
        enemy.render(window)

    for bull in bullsit:
        bull.move()
        bull.render(window)

    if iswin == True:
        window.blit(fonwin , [0 , 0])
    if islose == True:
        window.blit(fonlose , [0 , 0])

    pygame.display.flip()
    fps.tick(settings.fps)