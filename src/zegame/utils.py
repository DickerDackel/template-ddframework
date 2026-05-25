import json

import pygame
import pygame._sdl2.video as sdl2


def load_spritesheet(fname, renderer):
    image = pygame.image.load(fname)
    texture = sdl2.Texture.from_surface(renderer, image)

    with open(fname.with_suffix('.json')) as f:
        rects = json.load(f)

    res = {}
    for k, v in rects.items():
        res[k] = pygame.Rect(v)

    return texture, res
