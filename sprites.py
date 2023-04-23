import pygame as pg, sys
from pygame.locals import *

pg.init()
display_info = pg.display.Info()


class Arrow(pg.sprite.Sprite):
    def __init__(self, x, y, images, dir):
        super().__init__()
        self.images = images
        self.rect = images[0].get_rect()
        self.rect.midtop = (x, y)
        self.x = x
        self.y = y
        self.dir = dir
        self.cur_img = 0
        self.prev_change = 0
    def get_pos(self):
        return self.y

    def get_image(self):
        return self.images[self.cur_img]


class DynamicArrow(Arrow):
    def __init__(self, x, y, images, dir):
        super().__init__(x, y, images, dir)

    def check_death(self):
        if self.rect.bottom <= 0:
            pg.sprite.Sprite.kill(self)
            return True
        return False

    def move(self, y_shift):
        self.y -= y_shift
        self.rect.midtop = (self.x, self.y)
        if self.prev_change == 10:
            self.prev_change = 0
            self.cur_img = self.cur_img + 1 if self.cur_img < 15 else 0
        else:
            self.prev_change += 1
        self.check_death()




class StaticArrow(Arrow):
    def __init__(self, x, y, images, dir):
        super().__init__(x, y, images, dir)

    def collision(self):
        self.cur_img = 1
        self.prev_change = 0

    def update(self):
        if self.cur_img:
            if self.prev_change == 5:
                self.prev_change = 0
                self.cur_img = 0
            else:
                self.prev_change += 1
