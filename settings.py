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
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

#IMG Stuff
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')

CAVE_FOLDER = path.join(img_folder,'cave')
CAVE_WALL_FOLDER = path.join(CAVE_FOLDER,'walls')
CAVE_FLOOR_FOLDER = path.join(CAVE_FOLDER,'floors')

CAVE_WALL_IMGS = [
    path.join(CAVE_WALL_FOLDER,'cave_wall.png'),
    path.join(CAVE_WALL_FOLDER,'cave_wall2.png'),
    path.join(CAVE_WALL_FOLDER,'cave_wall3.png'),
    path.join(CAVE_WALL_FOLDER,'cave_wall4.png')
    ]

CAVE_FLOOR_IMGS = [
    path.join(CAVE_FLOOR_FOLDER,'cave_floor.png')
    ]