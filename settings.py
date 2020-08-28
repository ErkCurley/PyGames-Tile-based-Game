import pygame as pg
from os import path


# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250.0
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

#IMG Stuff
GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER, 'maps')
IMG_FOLDER = path.join(GAME_FOLDER, 'img')

MAP_FILE = path.join(MAP_FOLDER,'Lava Pass.tmx')
PLAYER_IMG = 'manBlue_gun.png'
