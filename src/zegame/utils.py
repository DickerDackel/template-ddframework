from random import random

import json

import glm
import pygame
import pygame._sdl2.video as sdl2


def load_spritesheet(fname, renderer):
    image = pygame.image.load(fname)
    texture = sdl2.Texture.from_surface(renderer, image)

    with open(fname.with_suffix('.json')) as f:
        cells = json.load(f)

    sprites = {name: pygame.Rect(rect) for name, rect in cells.items()}

    return texture, sprites


def random_vector(min_speed, max_speed):
    angle = glm.radians(random() * 360)
    length = min_speed + random() * (max_speed - min_speed)
    v = glm.vec2(1, 0) * length

    return glm.rotate(v, angle)
