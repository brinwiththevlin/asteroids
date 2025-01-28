"""sprite classes."""

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """base class for game objects."""

    def __init__(self, x: float, y: float, radius: float, *groups: pygame.sprite._Group) -> None:
        super().__init__(*groups)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
