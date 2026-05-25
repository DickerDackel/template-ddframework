from importlib.resources import files
from types import SimpleNamespace

import pygame

TITLE = 'ZeGame'
SCREEN = pygame.Rect(0, 0, 640, 360)
WINDOW = pygame.Rect(0, 0, 1920, 1080)
FPS = 60

ASSETS = files('zegame.assets')

pygame.font.init()

basefont = ASSETS / 'DSEG14Classic-Regular.ttf'
FONTS = SimpleNamespace(
    tiny=pygame.font.Font(basefont, 6),
    small=pygame.font.Font(basefont, 8),
    normal=pygame.font.Font(basefont, 11),
    large=pygame.font.Font(basefont, 16),
    larger=pygame.font.Font(basefont, 24),
    huge=pygame.font.Font(basefont, 32),
    giant=pygame.font.Font(basefont, 64),
)

COLORS = SimpleNamespace(
    background=pygame.Color('darkslategrey'),
    default=pygame.Color('limegreen'),
)

SPRITES = {
    'player-white':      pygame.Rect( 0,  0, 16, 16),
    'player-yellow':     pygame.Rect(16,  0, 16, 16),
    'player-lightblue':  pygame.Rect(32,  0, 16, 16),
    'player-lightgreen': pygame.Rect(48,  0, 16, 16),
    'player-pink':       pygame.Rect(64,  0, 16, 16),
    'player-red':        pygame.Rect(16, 16, 16, 16),
    'player-green':      pygame.Rect(32, 16, 16, 16),
    'player-blue':       pygame.Rect(48, 16, 16, 16),
    'player-purple':     pygame.Rect(64, 16, 16, 16),

    'bullet-white':      pygame.Rect( 0, 32, 16, 16),
    'bullet-yellow':     pygame.Rect(16, 32, 16, 16),
    'bullet-lightblue':  pygame.Rect(32, 32, 16, 16),
    'bullet-lightgreen': pygame.Rect(48, 32, 16, 16),
    'bullet-pink':       pygame.Rect(64, 32, 16, 16),
    'bullet-red':        pygame.Rect(16, 48, 16, 16),
    'bullet-green':      pygame.Rect(32, 48, 16, 16),
    'bullet-blue':       pygame.Rect(48, 48, 16, 16),
    'bullet-purple':     pygame.Rect(64, 48, 16, 16),
}
