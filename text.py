import pygame as pg


class Text:
    def __init__(self, surface, text, font_size=32, font=None, letter_color=(0, 0, 0), letter_back=None):
        self.surface = surface
        self.font = pg.font.Font(font, font_size)
        self.text = self.font.render(text, True, letter_color, letter_back)

    def write_c(self, x, y):  # center
        textRect = self.text.get_rect()  # text size
        textRect.center = (x, y)
        self.surface.blit(self.text, textRect)

    def write_tl(self, x, y):  # topleft
        textRect = self.text.get_rect()  # text size
        textRect.topleft = (x, y)
        self.surface.blit(self.text, textRect)


