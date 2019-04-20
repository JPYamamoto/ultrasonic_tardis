import pygame
from pathlib import Path
from constants import WINDOWS_HEIGHT

_WIDTH = 80
_OFFSET = 0.1


class Tardis(pygame.sprite.Sprite):
    """Object representing a TARDIS (the main character).


    Attributes:
        image: An image instance provided by Pygame.
        rect: The rect surface that will occupy the object instance.
    """

    def __init__(self):
        """ Init the TARDIS (player entity). """
        super(Tardis, self).__init__()

        path = Path.cwd() / 'assets' / 'image' / 'tardis.png'
        image = pygame.image.load(str(path))
        scale = (_WIDTH, round(image.get_height() * _WIDTH / image.get_width()))

        self.image = pygame.transform.scale(image, scale)
        self.rect = self.image.get_rect(center=(150, 0))

    def update(self, distance):
        """Move the TARDIS according to the info of the sensor.

        The TARDIS will move in the y-axis (up and down) given a
        position ranging from 0 to 1, as a float.
        It will be retrieved by getting the distance measured by the
        ultrasonic sensor, and only taking into account a certain RANGE
        after a certain OFFSET.

        Args:
            distance: The distance measured by the ultrasonic sensor.

        Returns:
            Nothing. This method is only used to modify the internal
            state of the object.
        """
        if distance < _OFFSET:
            distance = _OFFSET

        distance = (distance - _OFFSET) * 5
        distance = 1 - distance
        self.rect.center = (150, WINDOWS_HEIGHT * distance)

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > WINDOWS_HEIGHT:
            self.rect.bottom = WINDOWS_HEIGHT

