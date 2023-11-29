import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load alien image and set its rect attribute.
        self.image = pygame.image.load('Alien_Invasion_Game/Pictures/enemy.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top lef of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move alien to the right."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x