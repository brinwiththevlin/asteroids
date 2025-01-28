"""sprite classes."""

import pygame
from pygame.surface import Surface


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """base class for game objects."""

    def __init__(self, x: float, y: float, radius: float, *groups: pygame.sprite.Group) -> None:
        """CircleShape constructor.

        Args:
            x: x position of circle center
            y: y position of circle center
            radius: radius of circle
            groups: sprite groups circe is a part of
        """
        super().__init__(*groups)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: Surface):
        # sub-classes must override
        raise NotImplementedError

    def update(self, dt: int):
        # sub-classes must override
        raise NotImplementedError
