import pygame

class Ship:
    """A class to manage ship."""
    def __init__(self, ai_game):
        """Initialize ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('Alien_Invasion_Game/Pictures/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag starting with ship that is not moving.
        self.move_right = False
    
    def update(self):
        """Update the ships position based on the movement flag."""
        if self.move_right:
            self.rect.x += 1
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
