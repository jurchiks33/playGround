class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize game's settings."""
        #Screen Settings
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (36, 33, 36)

        #Ship settings
        self.ship_speed = 2.5

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)