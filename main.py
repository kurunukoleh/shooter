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
fon = pygame.image.load("m6l1/galaxy.jpg")
fon = pygame.transform.scale(fon , (800 , 500))

shootsound = pygame.mixer.Sound('m6l1/fire.ogg')
bullsit = []
enmylist = []
fixtime1 = time.time()

rocket = tank.Tank(300 , 400 , 100 , 100 , "m6l1/rocket.png" , 5)

for i in range(5):
    enmylist.append(enemes.Enemy(random.randint(0 , 750) , random.randint(-1000 , 0) , 50 , 50 ,  "m6l1/asteroid.png" , 2))

game = True
while game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()


    rocket.move()
    rocket.shoot()
    #print(rocket.shoot())
    if time.time() - fixtime1 > 0.2:
        fixtime1 = time.time()
        if rocket.shoot() == True:
            shootsound.play()
            bullsit.append(bullets.Bullshit(rocket.hitbox.x + 45 , rocket.hitbox.y , 10 , 20 , "m6l1/bullet.png" , 10))

    for enemy1 in enmylist:
        if rocket.hitbox.colliderect(enemy1.hitbox):
            game = False
            pygame.quit()

    for item3 in bullsit:
        if item3.hitbox.y < -100 :
            bullsit.pop(0)

    for item in bullsit:
        item.move()

    window.fill((255, 0, 0))
    window.blit(fon , [0 , 0])
    rocket.render(window)

    for enemy in enmylist:
        enemy.move()
        enemy.render(window)

    for item2 in bullsit:
        item2.render(window)

    pygame.display.flip()
    fps.tick(60)