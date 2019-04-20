import pygame
from random import randint
from pathlib import Path
from constants import WINDOWS_WIDTH, WINDOWS_HEIGHT


_WIDTH = 50

class Dalek(pygame.sprite.Sprite):
    """Representation of a Dalek in the game.

    Daleks are the entities that will cause the main character to die.
    Crashing into a dalek will cause the game to end.

    Attributes:
        image: An image instance provided by Pygame.
        rect: The rect surface that will occupy the object instance.
        speed: An int that gives the rate of change to move the object.
    """

    def __init__(self):
        """ Init a random Dalek. """
        super(Dalek, self).__init__()

        path = Path.cwd() / 'assets' / 'image' / 'dalek.png'
        image = pygame.image.load(str(path))
        scale = (_WIDTH, round(image.get_height() * _WIDTH / image.get_width()))

        self.image = pygame.transform.scale(image, scale)
        self.rect = self.image.get_rect(center=(
            WINDOWS_WIDTH + _WIDTH,
            randint(_WIDTH, WINDOWS_HEIGHT - _WIDTH)
        ))
        self.speed = randint(7, 10)

    def update(self):
        """ Change the position of the Dalek given its speed. """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

