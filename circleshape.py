import pygame
from typing import Self


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x:float, y:float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers) #type: ignore
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other: Self) -> bool:
        dist = self.position.distance_to(other.position)
        return dist <= self.radius or dist <= other.radius
