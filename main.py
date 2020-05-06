# 1 - подключить библиотеки
# 2 - создать глобальные перменные
# 3 - создать окно игры

import pygame

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect() # Берем прямоугольник, который отвечает за спрайт
        # у rect есть centerx, centery - центр по оси X прямоугльника и центр по оси Y прямоугольника
        # у rect есть left, right, top, bottom - левая граница, правая граница, верхняя граница, нижняя граница
        # у rect есть x, y - координата по оси X и по оси Y
        self.rect.left = 10
        self.rect.bottom = HEIGHT - 10
        self.speedy = 0
        self.timer = pygame.time.get_ticks()
        self.jumping = False
        self.down = False

    def update(self):
        if pygame.time.get_ticks() - self.timer >= 250:
            if self.jumping:
                if self.speedy < 0:
                    self.speedy = -self.speedy
                elif self.speedy > 0:
                    self.speedy = 0
                    self.jumping = False
            elif self.down:
                self.image = pygame.Surface((40, 40))
                self.image.fill(RED)
                old_rect = self.rect
                self.rect = self.image.get_rect()
                self.rect.x = old_rect.x
                self.rect.y = old_rect.y - 20

                self.down = False

            self.timer = pygame.time.get_ticks()

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and not self.jumping and not self.down:
            self.jumping = True
            self.timer = pygame.time.get_ticks()
            self.speedy = -10
        if keystate[pygame.K_c] and not self.jumping and not self.down:
            self.image = pygame.Surface((40, 20))
            self.image.fill(BLUE)
            old_rect = self.rect
            self.rect = self.image.get_rect()
            self.rect.x = old_rect.x
            self.rect.y = old_rect.y + 20

            self.down = True
            self.timer = pygame.time.get_ticks()

        self.rect.y += self.speedy


# игровой цикл

# Создать группы спрайтов, чтобы работать с ними со всеми одновременно
all_sprites = pygame.sprite.Group()
player = Player() # создаем переменную player класса Player
all_sprites.add(player) # добавляем игрока в группу всех спрайтов

running = True
while running:
    clock.tick(FPS)

    # обработка ввода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обновление данных
    all_sprites.update()

    # отрисовка
    screen.fill(BLACK) # заполнение экрана цветом
    all_sprites.draw(screen) # вносим изменения спрайтов на экран
    pygame.display.flip() # обновление экран (отображение нового кадра)

pygame.quit() 
