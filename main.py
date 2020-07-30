 # 1 - подключить библиотеки
# 2 - создать глобальные перменные
# 2 - создать глобальные перменные
# 2 - создать глобальные перменные
# 2 - создать глобальные перменные
# 3 - создать окно игры

import pygame
import random
from os import path

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

game_folder = path.dirname(__file__)   # корневая папка игры
assets_folder = path.join(game_folder, 'assets')

sausage_img = pygame.image.load(path.join(assets_folder, 'sausage.png')) # загрузка изображения сосиски
suriken_img = pygame.image.load(path.join(assets_folder, 'suriken.jpg')) # загрузка изображения сюрикена
suriken_img.set_colorkey(WHITE) # делает цвет прозрачным на этой картинке

# Загружаем 4 картинки для фона
bcgrnd1_img = pygame.image.load(path.join(path.dirname(__file__) , 'background.jpg'))
bcgrnd2_img = pygame.image.load(path.join(assets_folder, '2.jpg'))
bcgrnd3_img = pygame.image.load(path.join(assets_folder, '3.jpg'))
bcgrnd4_img = pygame.image.load(path.join(assets_folder, '4.jpg'))

# Меняем размер картинок
bcgrnd1_img = pygame.transform.scale(bcgrnd1_img, (WIDTH, HEIGHT))
bcgrnd2_img = pygame.transform.scale(bcgrnd2_img, (WIDTH, HEIGHT))
bcgrnd3_img = pygame.transform.scale(bcgrnd3_img, (WIDTH, HEIGHT))
bcgrnd4_img = pygame.transform.scale(bcgrnd4_img, (WIDTH, HEIGHT))

bckgrnd_counter = 1                     # счетчик номера фона
background = bcgrnd1_img                # текущий фон
background_rect = background.get_rect() # спрайт текущего фона

best_score = 0

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
        self.image = pygame.transform.scale(sausage_img, (40, 40))
        # self.image = pygame.Surface((40, 40))
        # self.image.fill(RED)
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
        self.score = 0

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
        elif self.down and pygame.time.get_ticks() - self.timer >= 200: # разгибается
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

            global bckgrnd_counter # берем глобальную переменную
            global background
            global background_rect
            bckgrnd_counter += 1
            if bckgrnd_counter >= 5:
                bckgrnd_counter = 1

            if (bckgrnd_counter == 1):
                background = bcgrnd1_img       
                background_rect = background.get_rect()
            elif bckgrnd_counter == 2:
                background = bcgrnd2_img       
                background_rect = background.get_rect()
            elif bckgrnd_counter == 3:
                background = bcgrnd3_img       
                background_rect = background.get_rect()
            elif bckgrnd_counter == 4:
                background = bcgrnd4_img       
                background_rect = background.get_rect()

            screen.blit(background, background_rect)

        if (self.rect.bottom >= HEIGHT):
            self.rect.bottom = HEIGHT - 5
              
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and not self.jumping and not self.down:
            self.jumping = True
            self.timer = pygame.time.get_ticks()
            self.speedy = -8
        if keystate[pygame.K_c] and not self.jumping and not self.down: # сгибается
            self.image = pygame.transform.scale(sausage_img, (40, 20))
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

font_name = pygame.font.match_font('comicsansms')
def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_start_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Run, sausage, run!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, " Нажмите пробел для прыжка, и C для приседания", 18, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажми любую клавишу для старта", 18, WIDTH / 2, HEIGHT * 3 / 4)
    draw_text(screen, "Лучший счет: " + str(best_score), 18, WIDTH / 2, HEIGHT * 6 / 7)
    if player != None:
        draw_text(screen,"Счет: " + str(player.score), 18, WIDTH / 2, HEIGHT * 4 / 5)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

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

game_over = True
running = True
while running:
    if game_over:
        if player != None and player.score > best_score:
            best_score = player.score

        show_start_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        all_surikens = pygame.sprite.Group()
        player = Player() # создаем переменную player класса Player
        all_sprites.add(player) # добавляем игрока в группу всех спрайтов

        for i in range (0, 15):
            suriken = Suriken()
            all_surikens.add(suriken)
            all_sprites.add(suriken)

    clock.tick(FPS)

    screen.blit(background, background_rect)
    # обработка ввода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hits = pygame.sprite.spritecollide(player, all_surikens, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.hit(10)
        if player.health <= 0:
            game_over = True
        new_suriken = Suriken()
        all_surikens.add(new_suriken)
        all_sprites.add(new_suriken)

    # обновление данных
    all_sprites.update()

    # отрисовка
    all_sprites.draw(screen) # вносим изменения спрайтов на экран
    draw_health(screen, 175, 5, player.health, BLUE)
    draw_text(screen, str(player.score), 12, 100, 100, RED)
    pygame.display.flip() # обновление экран (отображение нового кадра)

pygame.quit() 

# DONE: исправить подпрыгивание при первом приседании игрока
# DONE: увеличить время прыжка игрока
# DONE: добавить жизни игрока
# DONE: уменьшать жизни игрока при столкновении с сюрикеном
# DONE: добавить изображения к спрайтам
# DONE: сделать счёт
# DONE: сделать экран окончания
# DONE: сделать так, чтобы был пол
# DONE: добавить сменяющийся фон (несколько картинок сменяют друг друга)
# TODO: убрать фон сюрикена
# TODO: сменить форму спрайта сюрикена на круг
# TODO: сделать "Best score"

# git add *
# git commit
