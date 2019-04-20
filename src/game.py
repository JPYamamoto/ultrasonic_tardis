import pygame
from pygame.locals import *
from pathlib import Path
from gpiozero import DistanceSensor
from constants import *
from entities.tardis import Tardis
from entities.dalek import Dalek
from entities.star import Star


def main():
    """Main loop interface to run the game.

    Runs the game with each cycle in the loop being a single frame.
    In each iteration, all data required to display the frame is
    computed.
    Some events will be triggered asynchrounously after a given amount
    of seconds.

    Returns:
        Nothing. But game will be run on a new window.
    """
    sensor = DistanceSensor(echo=17, trigger=4, max_distance=MAX_DISTANCE,
                            threshold_distance=0.2)

    # Initialize game tools.
    pygame.init()
    screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize variables.
    tardis = Tardis()
    daleks = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    running = True

    # Create event to spawn daleks.
    NEWDALEK = pygame.USEREVENT + 1
    pygame.time.set_timer(NEWDALEK, 1500)

    # Create event to spawn stars.
    NEWSTAR = pygame.USEREVENT + 2
    pygame.time.set_timer(NEWSTAR, 500)

    # Game loop.
    while running:

        # Handle events.
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == NEWDALEK:
                dalek = Dalek()
                daleks.add(dalek)
            elif event.type == NEWSTAR:
                star = Star()
                stars.add(star)

        # Black background.
        screen.fill((0, 0, 0))

        # Generate next frame for each object.
        tardis.update(sensor.distance)
        daleks.update()
        stars.update()

        # Draw on screen each object.
        # Order is important to keep z-index.
        for star in stars:
            screen.blit(star.image, star.rect)
        for dalek in daleks:
            screen.blit(dalek.image, dalek.rect)
        screen.blit(tardis.image, tardis.rect)

        # Detect collisions (TARDIS 💥 Dalek)
        if pygame.sprite.spritecollideany(tardis, daleks):
            running = False

        # Draw everything onto the screen.
        pygame.display.flip()
        # Update a given number (FPS) of times per second.
        clock.tick(FPS)

