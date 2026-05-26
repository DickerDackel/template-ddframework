from enum import StrEnum, auto
from typing import Hashable, Sequence, TypeAlias

import pygame
import glm

EntityID: TypeAlias = Hashable
Vector: TypeAlias = (pygame.Vector2 | glm.vec2 | Sequence[float])


class Entity(StrEnum):
    PLAYER = auto()


class Comp(StrEnum):
    KILLED = auto()
    MOMENTUM = auto()
    ON_KILL = auto()
    PRSA = auto()
    RAMP_ALPHA = auto()
    RAMP_ANGLE = auto()
    RAMP_SCALE = auto()
    SPRITE = auto()


class Prop(StrEnum):
    WANTS_MOUSE = auto()
    IS_CONTAINED = auto()
    IS_UNCONSTRAINED = auto()
    IS_KILLED = auto()
