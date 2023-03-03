import pygame as pg, sys
from pygame.locals import *

pg.init()
display_info = pg.display.Info()


class Arrow(pg.sprite.Sprite):
    def __init__(self, x, y, image, dim):
        super().__init__()
        image = pg.transform.scale(image, (dim, dim))
        self.image = image
        self.rect = image.get_rect()
        self.rect.midtop = (x, y)
        self.x = x
        self.y = y


class DynamicArrow(Arrow):
    def __init__(self, x, y, image, dim):
        super().__init__(x, y, image, dim)

    def move(self, y_shift):
        self.y -= y_shift
        self.rect.midtop = (self.x, self.y)


class StaticArrow(Arrow):
    def __init__(self, x, y, image, dim):
        super().__init__(x, y, image, dim)
