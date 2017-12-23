# define colors
import pygame as pg
vec = pg.math.Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024  # 16*64 32*32 or 64*16
HEIGHT = 768  # 16*448 or 32*24 or 64*12
FPS = 60
TITLE = 'Tilemap game'
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'wall.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 175
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'hitman1_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(35, 10)
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DMG = 10

# gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150

# NPC settings
NPC_HEALTH = 100
NPC_KNOCKBACK = 10
NPC_DMG = 10
NPC_IMG = 'zoimbie1_hold.png'
NPC_SPEED = [75, 100, 125, 150, 175, 75, 100, 125, 150]
NPC_HIT_RECT = pg.Rect(0, 0, 25, 25)
AVOID_RADIUS = 50

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png', 'whitePuff18.png']
FLASH_DURATION = 40

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
NPC_LAYER = 2
EFFECT_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png'}
HEALTH_PACK_AMOUNT = 20
