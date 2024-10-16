from pygame import Surface
import pygame
from circleshape import CircleShape
from groups import asteroids, updatable, drawable


class Asteroid(CircleShape):
    containers = (asteroids, updatable, drawable)

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += self.velocity * dt
