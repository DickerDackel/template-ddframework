from os import environ
from types import SimpleNamespace

import pygame

from ddframework.app import App
from ddframework.statemachine import StateMachine
from ddframework.cache import cache as CACHE

import zegame.config as C
import zegame.globals as G

from zegame.states import SelfCheck, Splash, Title, Instructions, Game, Highscores
from zegame.utils import load_spritesheet


def main():
    if environ.get('XDG_SESSION_TYPE', '') == 'wayland':
        environ['SDL_VIDEODRIVER'] = 'wayland'

    pygame.init()

    w = pygame.Window(size=C.WINDOW.size, position=pygame.WINDOWPOS_CENTERED)
    app = App(C.TITLE, window=w, resolution=C.SCREEN.size, fps=C.FPS, bgcolor=C.COLORS.background)
    # app = App(C.TITLE, window=None, resolution=C.SCREEN.size, fps=C.FPS, bgcolor=C.COLORS.background)
    pygame.mouse.set_visible(False)

    G.renderer = app.renderer

    fname = C.ASSETS / 'spritesheet.png'
    name = fname.stem
    texture, t_rects = load_spritesheet(fname, app.renderer)
    CACHE['atlas'][name] = t_rects
    CACHE['texture'][name] = texture

    states = SimpleNamespace(
        selfcheck=SelfCheck(app),
        splash=Splash(app),
        title=Title(app),
        instructions=Instructions(app),
        game=Game(app),
        highscores=Highscores(app),
    )

    sm = StateMachine()
    sm.add(states.selfcheck, states.splash)
    sm.add(states.splash, states.title)
    sm.add(states.title, states.instructions, states.game)
    sm.add(states.instructions, states.highscores, states.game)
    sm.add(states.highscores, states.title, states.game)
    sm.add(states.game, states.highscores)

    walker = sm.walker(states.selfcheck)
    app.run(walker)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
