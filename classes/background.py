from const import bcgrnd1_img


class Background:
    bckgrnd_counter = 1  # счетчик номера фона
    background = bcgrnd1_img  # текущий фон
    background_rect = background.get_rect()  # спрайт текущего фона
