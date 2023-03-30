import pygame as pg, sys
from pygame.locals import *

pg.init()
display_info = pg.display.Info()


class Arrow(pg.sprite.Sprite):
    def __init__(self, x, y, image, dim, dir):
        super().__init__()
        image = pg.transform.scale(image, (dim, dim))
        self.image = image
        self.rect = image.get_rect()
        self.rect.midtop = (x, y)
        self.x = x
        self.y = y
        self.dir = dir
    def get_pos(self):
        return self.y


class DynamicArrow(Arrow):
    def __init__(self, x, y, image, dim, dir):
        super().__init__(x, y, image, dim, dir)

    def check_death(self):
        if self.rect.bottom <= 0:
            pg.sprite.Sprite.kill(self)
            print("Miss")

    def move(self, y_shift):
        self.y -= y_shift
        self.rect.midtop = (self.x, self.y)
        self.check_death()


class StaticArrow(Arrow):
    def __init__(self, x, y, image, dim, dir):
        super().__init__(x, y, image, dim, dir)
