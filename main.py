# 1 - подключить библиотеки
# 2 - создать глобальные перменные
# 3 - создать окно игры

import pygame

# ширина, высота, фпс (частота кадров), основные цвета
WIDTH = 400
HEIGHT = 500
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
clock = pygame.time.Clock()