import random

import pygame

from const import WIDTH, suriken_img


class Suriken(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(suriken_img, (25, 25))
        # self.image = pygame.Surface((25,25))
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.right = 600
        self.rect.centery = random.randint(150, 400)
        self.rect.centerx = WIDTH + random.randint(100, 1000)
        self.speedx = -3

    def update(self):
        if (self.rect.right < 0):
            self.rect.centery = random.randint(250, 350)
            self.rect.centerx = WIDTH + random.randint(100, 1000)
        self.rect.x += self.speedx
