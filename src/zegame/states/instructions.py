import pygame

import pygame._sdl2 as sdl2

from ddframework.app import GameState, StateExit
from pgcooldown import Cooldown

import zegame.config as C


class Instructions(GameState):
    def __init__(self, app):
        self.app = app

        label = C.FONTS.giant.render('Instructions', False, C.COLORS.default)
        self.texture = sdl2.Texture.from_surface(self.app.renderer, label)
        self.rect = label.get_rect(center=C.SCREEN.center)

    def reset(self, *args, **kwargs):
        self.cooldown = Cooldown(5)
        ...

    def restart(self, from_state, result):
        ...

    def dispatch_event(self, e):
        if e.type == pygame.QUIT:
            raise StateExit(-1)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                raise StateExit(-1)
            elif e.key == pygame.K_SPACE:
                raise StateExit(0)
            elif e.key == pygame.K_RETURN:
                raise StateExit(1)

    def update(self, dt):
        if self.cooldown.cold():
            raise StateExit(0)

        ...

    def draw(self):
        self.texture.draw(dstrect=self.rect)
