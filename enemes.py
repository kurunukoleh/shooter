import pygame

import settings


class Enemy:
    def __init__(self , x , y , w , h , speed , texture1 , texture2 , texture3 , num):
        if num == 1 :
            texture = texture1
        elif num == 2:
            texture = texture2
        else:
            texture = texture3
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))

    def move(self):
        self.hitbox.y += self.speed

