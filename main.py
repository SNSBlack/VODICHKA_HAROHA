from random import random
from Object1 import Object1
from confing import *
from Player import *

pg.init()

screen = pg.display.set_mode((confing['w'], confing['h']))
pg.display.set_caption(confing['title'])

obstacle_group = pg.sprite.Group()
all_sprite = pg.sprite.Group()

player = Player()
all_sprite.add(player)
clock = pg.time.Clock()

obstacle_group = pg.sprite.Group()


def new_mobs():
    Object_bottom = Object1(confing['w'], random.randint(-100, 100))
    Object_top = Object1(confing['w'], random.randint(500, confing['h']))
    obstacle_group.add(Object_top, Object_bottom)
    all_sprite.add(obstacle_group)


SPAWN_SPRITE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_SPRITE, 1500)

pg.time.set_timer(pg.USEREVENT, 50)

run = True
score = 0
while run:

    clock.tick(confing['fps'])
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()

    all_sprite.update()
    all_sprite.draw(screen)



    pg.display.flip()

pg.quit()
