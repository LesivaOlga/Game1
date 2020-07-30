from os import path

import pygame

WIDTH = 600
HEIGHT = 400
FPS = 60
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
game_folder = path.dirname(__file__)  # корневая папка игры
assets_folder = path.join(game_folder, 'assets')
sausage_img = pygame.image.load(path.join(assets_folder, 'sausage.png'))  # загрузка изображения сосиски
suriken_img = pygame.image.load(path.join(assets_folder, 'suriken.jpg'))  # загрузка изображения сюрикена
bcgrnd1_img = pygame.transform.scale(pygame.image.load(path.join(assets_folder, 'background.jpg')),
                                     (WIDTH, HEIGHT))
bcgrnd2_img = pygame.transform.scale(pygame.image.load(path.join(assets_folder, '2.jpg')), (WIDTH, HEIGHT))
bcgrnd3_img = pygame.transform.scale(pygame.image.load(path.join(assets_folder, '3.jpg')), (WIDTH, HEIGHT))
bcgrnd4_img = pygame.transform.scale(pygame.image.load(path.join(assets_folder, '4.jpg')), (WIDTH, HEIGHT))

