import pygame

from classes.background import Background
from classes.player import Player
from classes.suriken import Suriken
from const import WIDTH, HEIGHT, FPS, RED, BLUE, WHITE, suriken_img, bcgrnd1_img
from methods import draw_health, draw_text, show_start_screen

# Создание игровых (технических) переменных
pygame.init()  # создание игры
pygame.mixer.init()  # создание (подключение) звуков
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание экрана
pygame.display.set_caption("Run, sausage, run!")  # определяем название игры
clock = pygame.time.Clock()  # Переменная, которая поможет убедиться, что игра работает с нужным FPS

# Создание внутренних переменных
suriken_img.set_colorkey(WHITE)  # делает цвет прозрачным на этой картинке
best_score = 0
font_name = pygame.font.match_font('comicsansms')
# Создать группы спрайтов, чтобы работать с ними со всеми одновременно
all_sprites = pygame.sprite.Group()
all_surikens = pygame.sprite.Group()
player = Player()  # создаем переменную player класса Player
all_sprites.add(player)  # добавляем игрока в группу всех спрайтов
backgroundItem = Background()

for i in range(0, 15):
    suriken = Suriken()
    all_surikens.add(suriken)
    all_sprites.add(suriken)

game_over = True
running = True

while running:
    if game_over:
        if player != None and player.score > best_score:
            best_score = player.score

        show_start_screen(screen, backgroundItem.background, backgroundItem.background_rect, font_name, best_score, player, clock)
        game_over = False
        all_sprites = pygame.sprite.Group()
        all_surikens = pygame.sprite.Group()
        player = Player()  # создаем переменную player класса Player
        all_sprites.add(player)  # добавляем игрока в группу всех спрайтов

        for i in range(0, 15):
            suriken = Suriken()
            all_surikens.add(suriken)
            all_sprites.add(suriken)

    clock.tick(FPS)

    screen.blit(backgroundItem.background, backgroundItem.background_rect)
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
    all_surikens.update()
    player.update(screen, backgroundItem)

    # отрисовка
    all_sprites.draw(screen)  # вносим изменения спрайтов на экран
    draw_health(screen, 175, 5, player.health, BLUE)
    draw_text(screen, str(player.score), 12, 100, 100, font_name, RED)
    pygame.display.flip()  # обновление экран (отображение нового кадра)

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
# DONE: убрать фон сюрикена
# DONE: сменить форму спрайта сюрикена на круг
# DONE: сделать "Best score"

# git add *
# git commit
# git push
