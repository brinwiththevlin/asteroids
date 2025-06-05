"""Class representing asteroids for game."""

import random
from typing import final, override

import pygame
from pygame.surface import Surface

from asteroids.circleshape import CircleShape
from asteroids.constants import ASTEROID_MIN_RADIUS
from asteroids.groups import asteroids, drawable, updatable


@final
class Asteroid(CircleShape):
    """Class representing asteroids for game."""

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Constructor for asteroid class.

        Args:
            x: x position for center of asteroid
            y: y position for center of asteroid
            radius: radius of asteroid
        """
        super().__init__(x, y, radius, updatable, drawable, asteroids)

    @override
    def draw(self, screen: Surface) -> None:
        """Draws a circle on screen representing the asteroid.

        Args:
            screen: pygame screen
        """
        _ = pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    @override
    def update(self, dt: int) -> None:
        """Update position of asteroid.

        Args:
            dt: delta from frame rate
        """
        self.position += self.velocity * dt

    def split(self) -> None:
        """Splits asteroid into two smaller parts."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2
        r = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, r)
        a1.velocity = v1

        a2 = Asteroid(self.position.x, self.position.y, r)
        a2.velocity = v2
