import pygame

from asteroidfield import AsteroidField
# from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from groups import updatable, drawable, asteroids, shots


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    _ = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            if thing.radius != 0 and thing.collision(player):
                print("game over!")
                return
            for b in shots:
                if thing.collision(b):
                    thing.destroy()
                    b.kill()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
