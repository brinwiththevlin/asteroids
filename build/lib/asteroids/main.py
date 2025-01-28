"""asteroid game."""

import logging

import pygame
from pygame import display

from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Set up basic configuration
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    logging.info("Starting asteroids!")
    logging.info(f"width: {SCREEN_WIDTH}")
    logging.info(f"height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # TODO: add fill
        display.flip()
        dt = clock.tick() /1000


if __name__ == "__main__":
    main()
