 # 1 - подключить библиотеки
# 2 - создать глобальные перменные
# 3 - создать окно игры

import pygame
import random

# ширина, высота, фпс (частота кадров), основные цвета
WIDTH = 600
HEIGHT = 400
FPS = 60

# цвета задаются по RGB (КЗС) от 0 до 255
# Черный - 0 цветов 
# Белый - все цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# настройка игрового окна

pygame.init() # создание игры
pygame.mixer.init() # создание (подключение) звуков
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создание экрана
pygame.display.set_caption("Run, sausage, run!") # определяем название игры
clock = pygame.time.Clock() # Переменная, которая поможет убедиться, что игра работает с нужным FPS

def draw_health(surf, x, y, pct, colour):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, colour, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect() # Берем прямоугольник, который отвечает за спрайт
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

    def hit(self, count):
        self.health -= count
        if self.health < 0:
            self.health = 0

    def update(self):
        if self.jumping and pygame.time.get_ticks() - self.timer >= 500:
            if self.speedy < 0:
                self.speedy = -self.speedy
            elif self.speedy > 0:
                self.speedy = 0
                self.jumping = False
            self.timer = pygame.time.get_ticks()
        elif self.down and pygame.time.get_ticks() - self.timer >= 200:
            self.image = pygame.Surface((40, 40))
            self.image.fill(RED)
            old_rect = self.rect
            self.rect = self.image.get_rect()
            self.rect.x = old_rect.x
            self.rect.y = old_rect.y - 20
            self.down = False
            self.timer = pygame.time.get_ticks()
        if (self.rect.left > WIDTH):
            self.rect.left = 5
            self.rect.bottom = HEIGHT - 5
        if (self.rect.bottom >= HEIGHT):
            self.rect.bottom = HEIGHT - 5
              
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and not self.jumping and not self.down:
            self.jumping = True
            self.timer = pygame.time.get_ticks()
            self.speedy = -8
        if keystate[pygame.K_c] and not self.jumping and not self.down:
            self.image = pygame.Surface((40, 20))
            self.image.fill(RED)
            old_rect = self.rect
            self.rect = self.image.get_rect()
            self.rect.x = old_rect.x
            self.rect.y = old_rect.y + 20

            self.down = True
            self.timer = pygame.time.get_ticks()

        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Suriken(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image.fill(WHITE)
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

# игровой цикл

# Создать группы спрайтов, чтобы работать с ними со всеми одновременно
all_sprites = pygame.sprite.Group()
all_surikens = pygame.sprite.Group()

player = Player() # создаем переменную player класса Player
all_sprites.add(player) # добавляем игрока в группу всех спрайтов

for i in range (0, 15):
    suriken = Suriken()
    all_surikens.add(suriken)
    all_sprites.add(suriken)

running = True
while running:
    clock.tick(FPS)

    # обработка ввода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hits = pygame.sprite.spritecollide(player, all_surikens, True)
    for hit in hits:
        player.hit(10)
        if player.health <= 0:
            running = False
        new_suriken = Suriken()
        all_surikens.add(new_suriken)
        all_sprites.add(new_suriken)

    # обновление данных
    all_sprites.update()

    # отрисовка
    screen.fill(BLACK) # заполнение экрана цветом
    all_sprites.draw(screen) # вносим изменения спрайтов на экран
    draw_health(screen, 175, 5, player.health, BLUE)
    pygame.display.flip() # обновление экран (отображение нового кадра)

pygame.quit() 

# DONE: исправить подпрыгивание при первом приседании игрока
# DONE: увеличить время прыжка игрока
# TODO: добавить жизни игрока
# TODO: уменьшать жизни игрока при столкновении с сюрикеном
# TODO: добавить изображения к спрайтам
# TODO: сделать счёт
# TODO: сделать так, чтобы был пол

# git add *
# git commit
# git push