"""player class module."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

import pygame

from asteroids.circleshape import CircleShape
from asteroids.constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_COUNTDOWN
from asteroids.groups import drawable, updatable
from asteroids.shot import Shot

if TYPE_CHECKING:
    from pygame.surface import Surface


@final
class Player(CircleShape):
    """Player class."""

    def __init__(self, x: float, y: float) -> None:
        """Constructor for player class.

        Args:
            x: x position of center of player
            y: y position of center of player
        """
        super().__init__(x, y, PLAYER_RADIUS, updatable, drawable)

        self.rotation: float = 0
        self.timer: float = 0

    # in the player class
    def triangle(self) -> list[pygame.Vector2]:
        """Returns a tuple for the position of the three corners."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: Surface) -> None:
        """Draws player on screen.

        Args:
            screen: surface to draw player triangle on.
        """
        _ = pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        """Rotates the sprite at constant speed.

        Args:
            dt: delta from frame rate
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    @override
    def update(self, dt: float) -> None:
        """Update rotation state based on button press.

        Args:
            dt: delta from frame rate
        """
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

    def move(self, dt: float) -> None:
        """Update position based on rotation.

        Args:
            dt: delta from frame rate
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) -> None:
        """Shoot bullets."""
        self.timer = SHOT_COUNTDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
