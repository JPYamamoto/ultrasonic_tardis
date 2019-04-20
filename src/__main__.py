#!/usr/bin/env python3

import game

"""
Doctor Who themed game that uses an Ultrasonic sensor connected to a
Raspberry Pi in order to control a TARDIS and prevent it from crashing
into the Daleks!
"""

__author__ = "Juan Pablo Yamamoto"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the game """
    game.main()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
