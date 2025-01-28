"""player class module."""

from __future__ import annotations

import pygame
from pygame.surface import Surface

from asteroids.circlshape import CircleShape
from asteroids.constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    """Player class."""

    def __init__(self, x: float, y: float, *groups: pygame.sprite.Group) -> None:
        """Constructor for player class.

        Args:
            x: x position of center of player
            y: y position of center of player
            groups: sprite groups the player belongs to
        """
        super().__init__(x, y, PLAYER_RADIUS, *groups)

        self.rotation = 0

    # in the player class
    def triangle(self) -> list[pygame.Vector2]:
        """Returns a tuple for the position of the three corners."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: Surface) -> None:
        """Draws player on screen.

        Args:
            screen: surface to draw player triangle on.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        """Rotates the sprite at constant speed.

        Args:
            dt: delta from frame rate
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        """Update rotation state based on button press.

        Args:
            dt: delta from frame rate
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
