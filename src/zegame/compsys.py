from typing import NamedTuple

import tinyecs as ecs

import pygame
import pygame._sdl2.video as sdl2

from ddframework.dynamicsprite import PRSA
from glm import vec2

from zegame.types import EntityID, Vector


class Sprite(NamedTuple):
    atlas: sdl2.Texture
    rect: pygame.Rect


def sys_apply_momentum(dt: float, eid: EntityID, prsa: PRSA, momentum: Vector) -> None:
    """Apply momentum to the PRSA."""

    prsa.pos += momentum * dt


def sys_apply_mouse(dt: float, eid: EntityID, prsa: PRSA, *, mouse: Vector) -> None:
    """Apply the mouse position to the PRSA."""

    prsa.pos = vec2(mouse)


def sys_bounce(dt: float, eid: EntityID, prsa: PRSA, sprite: Sprite, momentum: Vector, world: pygame.Rect) -> None:
    """Bounce the sprite within the given container."""

    rect = sprite.rect.move_to(center=prsa.pos)
    if prsa.scale != 1:
        rect.scale_by_ip(prsa.scale)

    if rect.left < world.left:
        rect.left = world.left - rect.left
        momentum.x = -momentum.x
    elif rect.right > world.right:
        rect.right = 2 * world.right - rect.right
        momentum.x = -momentum.x
    if rect.top < world.top:
        rect.top = world.top - rect.top
        momentum.y = -momentum.y
    elif rect.bottom > world.bottom:
        rect.bottom = 2 * world.bottom - rect.bottom
        momentum.y = -momentum.y


def sys_container(dt: float, eid: EntityID, rect: pygame.Rect, *, world: pygame.Rect) -> None:
    """Kill the entity if it has left the given boundaries."""

    if not world.colliderect(rect):
        ecs.remove_entity(eid)


def sys_draw_sprite(dt: float, eid: EntityID, sprite: Sprite, prsa: PRSA) -> None:
    """Draw a sprite transformed and positioned by the PRSA."""

    texture = sprite.atlas

    bkp_alpha = texture.alpha
    texture.alpha = prsa.alpha

    dstrect = sprite.rect.move_to(center=prsa.pos)
    if prsa.scale != 1:
        dstrect.scale_by_ip(prsa.scale)

    texture.draw(srcrect=sprite.rect, dstrect=dstrect, angle=prsa.rotation)

    texture.alpha = bkp_alpha
