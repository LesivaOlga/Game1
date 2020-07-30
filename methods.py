import pygame

from const import WHITE, WIDTH, HEIGHT, FPS


def draw_health(surf, x, y, pct, colour):
    if pct < 0:
        pct = 0
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, colour, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_text(surf, text, size, x, y, font_name, color=WHITE):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def show_start_screen(screen, background, background_rect, font_name, best_score, player, clock):
    screen.blit(background, background_rect)
    draw_text(screen, "Run, sausage, run!", 64, WIDTH / 2, HEIGHT / 4, font_name)
    draw_text(screen, " Нажмите пробел для прыжка, и C для приседания", 18, WIDTH / 2, HEIGHT / 2, font_name)
    draw_text(screen, "Нажми любую клавишу для старта", 18, WIDTH / 2, HEIGHT * 3 / 4, font_name)
    draw_text(screen, "Лучший счет: " + str(best_score), 18, WIDTH / 2, HEIGHT * 6 / 7, font_name)
    if player is not None:
        draw_text(screen, "Счет: " + str(player.score), 18, WIDTH / 2, HEIGHT * 4 / 5, font_name)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
