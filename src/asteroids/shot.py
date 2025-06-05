import pygame
from pygame.surface import Surface

from asteroids.circleshape import CircleShape
from asteroids.constants import SHOT_RADIUS
from asteroids.groups import drawable, shots, updatable


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS, shots, drawable, updatable)

    def draw(self, screen: Surface) -> None:
        """Draws a circle on screen representing the asteroid.

        Args:
            screen: pygame screen
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: int) -> None:
        """Update position of asteroid.

        Args:
            dt: delta from frame rate
        """
        self.position += self.velocity * dt
