import os
import pygame as pg

confing = {
    'w': 600,
    'h': 600,
    'title': 'пульт от ядерки',
    'bg': "orange",
    'fps': 60}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')

player_img = pg.image.load(os.path.join(media_folder, 'HAVAI.png'))

object_img = pg.image.load(os.path.join(media_folder, 'VADICHKA.png'))
