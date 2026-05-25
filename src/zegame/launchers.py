from random import random

import glm
import tinyecs as ecs

from ddframework.cache import cache as CACHE
from ddframework.dynamicsprite import PRSA
from glm import vec2

import zegame.config as C

from zegame.compsys import Sprite
from zegame.types import EntityID, Entity, Comp


def mk_player(pos) -> EntityID:
    prsa = PRSA(pos=(C.SCREEN.centerx, 3 * (C.SCREEN.height / 4)))

    atlas = CACHE['texture']['spritesheet']
    rect = CACHE['atlas']['spritesheet']['player-white']
    sprite = Sprite(atlas, rect)

    eid = ecs.create_entity(Entity.PLAYER)

    ecs.add_component(eid, Comp.PRSA, prsa)
    ecs.add_component(eid, Comp.SPRITE, sprite)

    return eid


def mk_bouncer(pos) -> EntityID:
    prsa = PRSA(pos=vec2(pos))

    angle = glm.radians(random() * 360)
    momentum = glm.rotate(glm.vec2(100, 0), angle)

    atlas = CACHE['texture']['spritesheet']
    rect = CACHE['atlas']['spritesheet']['bullet-white']
    sprite = Sprite(atlas, rect)

    eid = ecs.create_entity()
    ecs.add_component(eid, Comp.PRSA, prsa)
    ecs.add_component(eid, Comp.SPRITE, sprite)
    ecs.add_component(eid, Comp.MOMENTUM, momentum)

