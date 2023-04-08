from confing import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.speedx = None
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        if keystate[pg.K_s]:
            self.speedy = 8
        if keystate[pg.K_w]:
            self.speedy = -8
        if keystate[pg.K_SPACE]:
            self.speedy = -16
        if keystate[pg.K_LSHIFT]:
            self.speedy = -2

        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.x >confing['w']-100:
            self.rect.x -=10
        if self.rect.x < 0:
            self.rect.x +=10

        if self.rect.bottom < confing['h']:
            self.rect.y += 5


        else:
            self.rect.bottom = confing['h']


        if self.rect.top < 0:
            self.rect.top = 0


