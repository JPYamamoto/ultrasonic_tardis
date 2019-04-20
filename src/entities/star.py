import pygame
from random import randint
from pathlib import Path
from constants import WINDOWS_WIDTH, WINDOWS_HEIGHT


class Star(pygame.sprite.Sprite):
    """Object representing a star generated at random.

    There are five different asset images that a star can take. Each
    star will be randomly assigned one of those, and displayed for a
    random number of frames (ranging from 10 to 120) at a random
    position.

    Attributes:
        image: An image instance provided by Pygame.
        rect: The rect surface that will occupy the object instance.
        count: The number of frames it will be displayed.
    """

    def __init__(self):
        """ Init a random Star. """
        super(Star, self).__init__()

        filename = 'star{}.png'.format(randint(1, 5))
        path = Path.cwd() / 'assets' / 'image' / filename

        self.image = pygame.image.load(str(path))
        self.rect = self.image.get_rect(
            center=(randint(50, 1150), randint(50, 950))
        )
        self.count = randint(10, 120)

    def update(self):
        """ Update the number of frames that the instance is missing to
        be displayed on screen."""
        self.count -= 1

        if self.count <= 0:
            self.kill()

