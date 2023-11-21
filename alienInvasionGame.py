import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

def __init__(self):
    """Initialize game, and create gae resources."""
    pygame.init
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")