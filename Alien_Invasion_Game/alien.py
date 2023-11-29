import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        #Load alien image and set its rect attribute.
        self.image = pygame.image.load('Alien_Invasion_Game/Pictures/enemy.bmp')
        self.rect = self.image.get_rect()

        