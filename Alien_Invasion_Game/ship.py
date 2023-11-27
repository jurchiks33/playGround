import pygame

class Ship:
    """A class to manage ship."""
    def __init__(self, ai_game):
        """Initialize ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('Alien_Invasion_Game/Pictures/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        #movement flag starting with ship that is not moving.
        self.move_right = False
        self.move_left = False
    
    def update(self):
        """Update the ships position based on the movement flag."""
        #Update ships x value not the rect

        if self.move_right:
            self.x += self.settings.ship_speed
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
