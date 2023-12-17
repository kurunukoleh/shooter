import pygame
import enemes
import tank
import bullets
import time
import random

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((800 , 500))
fps = pygame.time.Clock()

pygame.mixer.music.load("m6l1/space.ogg")
fon = pygame.image.load("m6l1/galaxy.jpg")
fon = pygame.transform.scale(fon , (800 , 500))
fonlose = pygame.image.load("pixelartlose.png")
fonlose = pygame.transform.scale(fonlose , (800 , 500))
fonwin = pygame.image.load("pixelartwin.png")
fonwin = pygame.transform.scale(fonwin , (800 , 500))
shootsound = pygame.mixer.Sound('m6l1/fire.ogg')
islose = False
iswin = False
lichbul = -1
bullsit = []
enmylist = []
fixtime1 = time.time()
fixtime2 = time.time()

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

rocket = tank.Tank(300 , 400 , 100 , 100 , "m6l1/rocket.png" , 5)

for i in range(30):
    enmylist.append(enemes.Enemy(random.randint(0 , 750) , random.randint(-3000 , 0) , 50 , 50 ,  "m6l1/asteroid.png" , 2))

game = True
while game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    rocket.move()
    rocket.shoot()
    #print(rocket.shoot())
    if time.time() - fixtime1 > 0.5:
        fixtime1 = time.time()
        if rocket.shoot() == True:
            shootsound.play()
            bullsit.append(bullets.Bullshit(rocket.hitbox.x + 45 , rocket.hitbox.y , 10 , 20 , "m6l1/bullet.png" , 10))

    for enemy1 in enmylist:
        if rocket.hitbox.colliderect(enemy1.hitbox):
            #game = False
            #pygame.quit()
            islose = True
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
        if item.hitbox.y < 0 :
            bullsit.pop(0)

    if time.time() - fixtime2 > 30 :
        iswin = True
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
    fps.tick(60)