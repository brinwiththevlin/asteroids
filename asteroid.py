import random
from pygame import Surface
import pygame
from circleshape import CircleShape
from groups import asteroids, updatable, drawable
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = (asteroids, updatable, drawable)

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def destroy(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, radius)
            a1.velocity = v1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, radius)
            a2.velocity = v2 * 1.2
