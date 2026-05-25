from enum import StrEnum, auto

import pygame

import pygame._sdl2 as sdl2
import tinyecs as ecs

from ddframework.app import GameState, StateExit
from ddframework.statemachine import StateMachine

from pgcooldown import Cooldown

import zegame.config as C

from zegame.types import Comp
from zegame.compsys import sys_apply_momentum, sys_bounce, sys_draw_sprite
from zegame.launchers import mk_player, mk_bouncer


class Phases(StrEnum):
    CREATE = auto()
    LINGER = auto()


sm = StateMachine()
sm.add(Phases.CREATE, Phases.LINGER)
sm.add(Phases.LINGER, None)


class Game(GameState):
    def __init__(self, app):
        self.app = app

        label = C.FONTS.giant.render('Game', False, C.COLORS.default)
        self.texture = sdl2.Texture.from_surface(self.app.renderer, label)
        self.rect = label.get_rect(center=C.SCREEN.center)

    def reset(self, *args, **kwargs):
        self.cooldown = Cooldown(15)

        ecs.reset()
        self.walker = sm.walker()
        self.state = next(self.walker)

    def restart(self, from_state, result):
        ...

    def dispatch_event(self, e):
        if e.type == pygame.QUIT:
            raise StateExit(-1)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                raise StateExit(0)

    def update_create(self, dt):
        screen = self.app.logical_rect

        mk_player((screen.centerx, 3 * (screen.height / 4)))
        mk_bouncer(screen.center)

        self.state = next(self.walker)

    def update_linger(self, dt):
        ecs.run_system(dt, sys_apply_momentum, Comp.PRSA, Comp.MOMENTUM)
        ecs.run_system(dt, sys_bounce, Comp.PRSA, Comp.SPRITE, Comp.MOMENTUM, world=self.app.logical_rect)

    def update(self, dt):
        if self.cooldown.cold():
            raise StateExit(0)

        {Phases.CREATE: self.update_create,
         Phases.LINGER: self.update_linger}[self.state](dt)

    def draw(self):
        self.texture.draw(dstrect=self.rect)
        ecs.run_system(0, sys_draw_sprite, Comp.SPRITE, Comp.PRSA)
