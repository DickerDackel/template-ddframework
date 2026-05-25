import pygame

import pygame._sdl2 as sdl2

from ddframework.app import GameState, StateExit
from ddframework.cache import cache as CACHE
from pgcooldown import Cooldown

import zegame.config as C


class SelfCheck(GameState):
    def __init__(self, app):
        self.app = app

        label = C.FONTS.giant.render('SelfCheck', False, C.COLORS.default)
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

    def update(self, dt):
        if self.cooldown.cold():
            raise StateExit(0)

        atlas = CACHE['texture']['spritesheet']
        rects = list(CACHE['atlas']['spritesheet'].values())

        for srcrect in rects:
            atlas.draw(srcrect=srcrect, dstrect=srcrect)

        ...

    def draw(self):
        self.texture.draw(dstrect=self.rect)
