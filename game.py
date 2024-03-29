import pygame
import enemes
import tank
import bullets
import time
import random
import settings
import json

def start():
    with open('data.json', 'r', encoding='utf-8') as f:
        dota = json.load(f)
    asteroid_count = int(dota['asteroid_count'])
    asteroid_speed = int(dota['asteroid_speed'])
    asteroid_size = int(dota['asteroid_size'])
    player_speed = int(dota['player_speed'])
    bull_speed = int(dota['bull_speed'])
    fps1 = int(dota['fps'])
    musik_volume = int(dota['musik_volume']) / 100
    recordlist = dota['record']
    record = max(recordlist)
    asteroid_cocentration = int(dota['asteroid_concentration'])/100
    playertexture = dota['skin']
    money = int(dota['balance'])

    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((800, 500))
    fps = pygame.time.Clock()

    fon = pygame.image.load(settings.fon_texture)
    fon = pygame.transform.scale(fon, (800, 500))
    fonlose = pygame.image.load(settings.lose_texture)
    fonlose = pygame.transform.scale(fonlose, (800, 500))
    fonwin = pygame.image.load(settings.win_texture)
    fonwin = pygame.transform.scale(fonwin, (800, 500))
    #bomtexture = pygame.image.load(settings.boom_texture)
    #bomtexture = pygame.transform.scale(bomtexture , (100 , 100))

    pygame.mixer.music.load(settings.musick)
    shootsound = pygame.mixer.Sound(settings.fire_sound)
    bomsound = pygame.mixer.Sound(settings.bom_sound)
    winsound = pygame.mixer.Sound(settings.win_sound)
    losesound = pygame.mixer.Sound(settings.lose_sound)

    islose = False
    iswin = False
    #lichbul = -1
    bullsit = []
    enmylist = []
    fixtime1 = time.time()
    fixtime2 = time.time()
    nmet  = 0

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Збито: ' + str(nmet) + " " + "з " + str(asteroid_count), 1, (180, 0, 0))
    text2 = f1.render('Рекорд: ' + str(record) , 1, (200, 200, 10))


    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(musik_volume)

    rocket = tank.Tank(300, 400, 100, 100, playertexture, player_speed )

    for i in range(asteroid_count):
        enmylist.append(enemes.Enemy(random.randint(0, 750), random.randint(-100 * (asteroid_count/asteroid_cocentration), 0),asteroid_size, asteroid_size,
                                     asteroid_speed , settings.mateor_texture1 , settings.mateor_texture2 , settings.mateor_texture3 ,
                                     random.randint(1 ,3)))

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        rocket.move()
        rocket.shoot()
        # print(rocket.shoot())
        if rocket.shoot():
            if time.time() - fixtime1 > 0.5:
                fixtime1 = time.time()
                shootsound.play()
                bullsit.append(bullets.Bullshit(rocket.hitbox.x + 45, rocket.hitbox.y, 15, 30, settings.bull_texture,
                                                bull_speed))

        for enemy1 in enmylist:
            if rocket.hitbox.colliderect(enemy1.hitbox):
                # game = False
                # pygame.quit()
                islose = True
                losesound.play()
                shootsound.set_volume(0)
                bomsound.set_volume(0)
                rocket.hitbox.x = 10000
                rocket.hitbox.y = 10000
                pygame.mixer.music.stop()
                #pygame.mixer.quit()

        for colbul in bullsit:
            #lichbul += 1
            #lich = -1
            for colenem in enmylist:
                #lich += 1
                if colbul.hitbox.colliderect(colenem.hitbox):
                    nmet +=1
                    text1 = f1.render('Збито: ' + str(nmet) + " " + "з " + str(asteroid_count), 1, (180, 0, 0))
                    try:
                        enmylist.remove(colenem)
                        bullsit.remove(colbul)
                        bomsound.play()
                    except:
                        pass
        lichbul = -1

        for item in bullsit:
            if item.hitbox.y < 0:
                bullsit.pop(0)

        if time.time() - fixtime2 > asteroid_count/asteroid_cocentration + 3:
            iswin = True
            text3 = f1.render('Результат: ' + str(nmet) + " " + "з " + str(asteroid_count), 1, (200, 200, 200))
            shootsound.set_volume(0)
            pygame.mixer.music.stop()
            if time.time() - fixtime2 < asteroid_count/asteroid_cocentration + 3.02:
                money += nmet
                dota["record"].append(int(nmet))
                dota['balance'] = money
                with open('data.json', 'w', ) as f:
                    json.dump(dota, f, indent=4)
                winsound.play()
            #pygame.mixer.quit()

        window.fill((255, 0, 0))
        window.blit(fon, [0, 0])
        rocket.render(window)

        for enemy in enmylist:
            enemy.move()
            enemy.render(window)

        for bull in bullsit:
            bull.move()
            bull.render(window)

        window.blit(text1, (10, 10))
        window.blit(text2, (500, 10))

        if iswin == True:
            window.blit(fonwin, [0, 0])
            window.blit(text3 , (100 , 200))
            window.blit(text2 , (50 , 250))
        if islose == True:
            window.blit(fonlose, [0, 0])

        pygame.display.flip()
        fps.tick(fps1)