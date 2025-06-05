"""asteroid game."""

import logging
import sys

import pygame
from pygame import display

from asteroids.asteroidfield import AsteroidField
from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from asteroids.groups import asteroids, drawable, shots, updatable
from asteroids.player import Player

# Set up basic configuration
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")



def main() -> None:
    """Driver function for asteroids game."""
    logging.info("Starting asteroids!")
    logging.info(f"width: {SCREEN_WIDTH}")
    logging.info(f"height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            for s in shots:
                if s.is_colliding(thing):
                    s.kill()
                    thing.split()

            if player.is_colliding(thing):
                logging.info("Game over!")
                sys.exit(0)

        for thing in drawable:
            thing.draw(screen)

        display.flip()
        dt = clock.tick() / 1000


if __name__ == "__main__":
    main()
