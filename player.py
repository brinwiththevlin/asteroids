from pygame import Surface, Vector2
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOT_COOLDOWN, PLAYER_SHOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED
from groups import updatable, drawable
from shot import Shot


class Player(CircleShape):
    containers = (updatable, drawable)

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation: float = 0
        self.cooldown = 0

        # in the player class

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def triangle(self) -> list[Vector2]:
        forward: Vector2 = Vector2(0, 1).rotate(self.rotation)
        right: Vector2 = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown <= 0:
            self.cooldown = PLAYER_SHOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

