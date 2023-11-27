class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize game's settings."""
        #Screen Settings
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (36, 33, 36)

        #Ship settings
        self.ship_speed = 1.5