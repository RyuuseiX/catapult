import pygame as pg
from text import Text


class Rec(Text):
    def __init__(self, x=0, y=0, w=0, h=0, rgb=(230, 230, 230)):
        self.x = x  # Position X
        self.y = y  # Position Y
        self.w = w  # Width
        self.h = h  # Height
        self.RGB = rgb  # light gray

    def draw(self, surface, text='', font_size=32, font=None, letter_color=(0, 0, 0), letter_back=None):
        pg.draw.rect(surface, self.RGB, (self.x, self.y, self.w, self.h))
        if text != '':
            textOnButton = Text(surface, text, font_size, font, letter_color, letter_back)
            textOnButton.write_c(self.x + self.w / 2, self.y + self.h/ 2)



class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rec.__init__(self, x, y, w, h)
        self.status = False

    def isMouseOn(self):
        (posx, posy) = pg.mouse.get_pos()
        if self.x <= posx <= self.x + self.w and self.y <= posy <= self.y + self.h:
            self.status = True
        else:
            self.status = False
        return self.status


