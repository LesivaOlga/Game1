import pygame

from const import WIDTH, HEIGHT, sausage_img, bcgrnd1_img, bcgrnd2_img, bcgrnd3_img, bcgrnd4_img



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(sausage_img, (40, 40))
        # self.image = pygame.Surface((40, 40))
        # self.image.fill(RED)
        self.rect = self.image.get_rect()  # Берем прямоугольник, который отвечает за спрайт
        # у rect есть centerx, centery - центр по оси X прямоугльника и центр по оси Y прямоугольника
        # у rect есть left, right, top, bottom - левая граница, правая граница, верхняя граница, нижняя граница
        # у rect есть x, y - координата по оси X и по оси Y
        self.rect.left = 5
        self.rect.bottom = HEIGHT - 5
        self.speedy = 0
        self.speedx = 2
        self.timer = pygame.time.get_ticks()
        self.jumping = False
        self.down = False
        self.health = 100
        self.score = 0
        self.background_timer = pygame.time.get_ticks()

    def hit(self, count):
        self.health -= count
        if self.health < 0:
            self.health = 0

    def update(self, screen, backgroundItem):
        if self.jumping and pygame.time.get_ticks() - self.timer >= 500:
            if self.speedy < 0:
                self.speedy = -self.speedy
            elif self.speedy > 0:
                self.speedy = 0
                self.jumping = False
            self.timer = pygame.time.get_ticks()
        elif self.down and pygame.time.get_ticks() - self.timer >= 200:  # разгибается
            self.image = pygame.transform.scale(sausage_img, (40, 40))
            old_rect = self.rect
            self.rect = self.image.get_rect()
            self.rect.x = old_rect.x
            self.rect.y = old_rect.y - 20
            self.down = False
            self.timer = pygame.time.get_ticks()
        if (self.rect.left > WIDTH):
            self.rect.left = 5
            self.rect.bottom = HEIGHT - 5
            self.score += 1

            if pygame.time.get_ticks() - self.background_timer >= 2000:
                backgroundItem.bckgrnd_counter += 1
                if backgroundItem.bckgrnd_counter >= 5:
                    backgroundItem.bckgrnd_counter = 1

                if backgroundItem.bckgrnd_counter == 1:
                    backgroundItem.background = bcgrnd1_img
                    backgroundItem.background_rect = backgroundItem.background.get_rect()
                elif backgroundItem.bckgrnd_counter == 2:
                    backgroundItem.background = bcgrnd2_img
                    backgroundItem.background_rect = backgroundItem.background.get_rect()
                elif backgroundItem.bckgrnd_counter == 3:
                    backgroundItem.background = bcgrnd3_img
                    backgroundItem.background_rect = backgroundItem.background.get_rect()
                elif backgroundItem.bckgrnd_counter == 4:
                    backgroundItem.background = bcgrnd4_img
                    backgroundItem.background_rect = backgroundItem.background.get_rect()

                screen.blit(backgroundItem.background, backgroundItem.background_rect)
                self.background_timer = pygame.time.get_ticks()

        if (self.rect.bottom >= HEIGHT):
            self.rect.bottom = HEIGHT - 5

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and not self.jumping and not self.down:
            self.jumping = True
            self.timer = pygame.time.get_ticks()
            self.speedy = -8
        if keystate[pygame.K_c] and not self.jumping and not self.down:  # сгибается
            self.image = pygame.transform.scale(sausage_img, (40, 20))
            old_rect = self.rect
            self.rect = self.image.get_rect()
            self.rect.x = old_rect.x
            self.rect.y = old_rect.y + 20

            self.down = True
            self.timer = pygame.time.get_ticks()

        self.rect.x += self.speedx
        self.rect.y += self.speedy
