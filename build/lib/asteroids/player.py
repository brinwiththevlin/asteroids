"""player class module."""

import pygame

from asteroids.circlshape import CircleShape
from asteroids.constants import PLAYER_RADIUS


class Player(CircleShape):

    def __init__(self, x: float, y: float, *groups: pygame.sprite._Group) -> None:
        super().__init__(x, y, PLAYER_RADIUS, *groups)

        self.rotation = 0
